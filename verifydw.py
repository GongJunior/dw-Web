class Error(Exception):
    pass

class MappingError(Error):
    #Checking map.csv for blanks
    def __init__(self, message, errors):
        self.message = message
        self.errors = errors
class DicewareError(Error):
    #Checking map.csv for blanks
    def __init__(self, message, errors):
        self.message = message
        self.errors = errors

class ValidRow:
    def __init__(self, row: int, row_data: dict):
        self.is_blank_word = False
        self.is_blank_roll = False
        self.is_dup_word = False
        self.is_dup_roll = False
        self.is_int_error = False
        self.is_range_error = False
        self.row = row
        self.row_data = row_data
    
    def ValidateRow(self, all_rolls: list, all_words: list):
        self.is_blank_word = True if self.row_data['word'] == '' else False 
        self.is_blank_roll = True if self.row_data['roll'] == '' else False 
        self.is_dup_word = self.__CheckForDups(all_words,self.row_data['word'])
        self.is_dup_roll = self.__CheckForDups(all_rolls,self.row_data['roll'])
        try:
            self.is_int_error = not type(int(self.row_data['roll'])) is int
            self.is_range_error = not 11111 <= int(self.row_data['roll']) <= 66666
        except ValueError:
            self.is_int_error = True
    
    def __CheckForDups(self,sample_list, current_val)-> bool:
        set_elems = set()
        for elem in sample_list:
            if elem in set_elems and elem == current_val:
                return True
            else:
                set_elems.add(elem)
        return False 
    
    def IsValid(self):
        if self.is_dup_word + self.is_dup_roll + self.is_int_error + self.is_range_error + self.is_blank_word + self.is_blank_roll > 0:
            return False
        return True

def ValidateMappingFile(mapping: list):
    errors = [map for map in mapping if map['file'] == '' or map['name'] == '']
    if len(errors) > 0:
        raise MappingError('Mapping errors, review map.csv',errors)
    print('Mapping file is valid!')

def ValidateWordList(words: list)-> (int,list):
    r_list = []
    w_list = []
    errors = []
    for row in words:
        r_list.append(row['roll'])
        w_list.append(row['word'])
    for i,word in enumerate(words):
        row = ValidRow(i+2,word)
        row.ValidateRow(r_list,w_list)
        if not row.IsValid(): errors.append(row)
    return (len(r_list), errors)