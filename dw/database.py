from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from datetime import datetime, timedelta
from dw import db
import csv

def init_db():

    db_loc = current_app.config['SQLALCHEMY_DATABASE_URI']

    from dw.models import Name, Word
    from dw.verifydw import ValidateMappingFile, MappingError, ValidateWordList, DicewareError

    if Path(db_loc[10:]).exists():
        print(f'db found @{db_loc}')

        words_loc = Path(__file__).parent.absolute() / 'static/dwlists'
        map_loc = Path(__file__).parent.absolute() / 'static/dwmap.csv'
        current_tables = Name.query.order_by(Name.last_updated.desc()).all()

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
            file_loc = words_loc / row['file']
            file_utc = datetime.now() - timedelta(seconds=file_loc.stat().st_mtime) 
            name = Name(name=row['name'])
            found_names = [(t.last_updated,t) for t in current_tables if t.name == name.name]
            db_utc = found_names[0][0] if found_names else None

            if db_utc is not None and len(found_names) < 2:
                if file_utc <= db_utc:
                    continue
            if len(found_names) > 0:
                print(f'Removing: { name } x {len(found_names)}')
                Name.query.filter_by(name=name.name).delete()

            with open(file_loc,newline='', encoding='utf-8-sig') as csvwords:
                word_reader = csv.DictReader(csvwords)
                word_rows = list(word_reader)
            print(f'Importing words from { file_loc }...')
            count,errors = ValidateWordList(word_rows)

            try:
                if count != 7776 or len(errors) > 0: raise DicewareError("Error in file",errors)
            except DicewareError as e:
                print(f'Errors found in {file_loc}')
                print(e.message)
                for _ in e.errors:
                    print(f'row: {_.row}\troll: {_.row_data["roll"]}\tword: {_.row_data["word"]}')
                continue

            for word_row in word_rows:
                word = Word(roll=int(word_row['roll']), word=word_row['word'])
                name.words.append(word)
            db.session.add(name)
            print(f'{file_loc} has successfully been added \u2714')

        print('Comitting any changes to the database...\u2714')
        db.session.commit()
    else:
        print(f'db not found @{db_loc}, run flask migrate to create.')

