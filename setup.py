import os, csv
from app import db, Names, Words
from verifydw import *

#create db if it doesn't exist
if not os.path.isfile('dw.db'):
    #create db from classes
    from app import db
    db.create_all()
    print('dw.db created...')

    #map filename to name of list
    map_loc = os.path.join('resources','map.csv')

    #import raw data
    with open(map_loc,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        map_rows = list(reader)

    try:
        ValidateMappingFile(map_rows)
    except MappingError as e:
        print(e.message)
        for i in e.errors:
            print(i)

    for row in map_rows:
        words_loc = os.path.join('dwlists',row['file'])
        name = Names(name=row['name'])
        with open(words_loc,newline='', encoding='utf-8-sig') as csvwords:
            word_reader = csv.DictReader(csvwords)
            word_rows = list(word_reader)
        print(f'Importing words from { words_loc }...')
        count,errors = ValidateWordList(word_rows)
        try:
            if count != 7776 or len(errors) > 0: raise DicewareError("Error in file",errors)
        except DicewareError as e:
            print(f'Errors found in {words_loc}')
            print(e.message)
            for _ in e.errors:
                print(f'row: {_.row}\troll: {_.row_data["roll"]}\tword: {_.row_data["word"]}')
            continue

        for word_row in word_rows:
            word = Words(roll=int(word_row['roll']), word=word_row['word'])
            name.words.append(word)
        db.session.add(name)
        print(f'{words_loc} has successfully been added \u2714')

    print('Comitting lists to the database...\u2714')
    db.session.commit()
else:
    print('dw.db already exists, please remove db to build from word lists.')