from pathlib import Path
from datetime import datetime, timedelta
import unittest, csv
from dw import db, create_app
from dw.models import Name, Word
from config import TestConfig
from dw.database import init_db
from dw.verifydw import ValidateMappingFile, MappingError

class DbImportCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_demo(self):
        self.assertTrue(False, "Mandatory Fail")

    def test_load_from_empty(self):
        init_db()
        loaded_tables = Name.query.all()
        #get number of valid file to name maps
        #assert num tables loaded -eq num valid maps
        map_loc = Path(__file__).parents[1].absolute() / 'dw/static/dwmap.csv'
        with open(map_loc,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            map_rows = list(reader)
        try:
            ValidateMappingFile(map_rows)
            self.assertTrue(len(loaded_tables), len(map_rows))
        except MappingError as e:
            map_isValid = False
            self.assertTrue(map_isValid)
        #for each table: assert num of words -eq 7776
        for i in loaded_tables:
            with self.subTest(pkg= i.name):
                self.assertEqual(len(i.words), 7776)

    def test_load_with_no_changes(self):
        init_db()
        loaded_tables_1 = Name.query.all()

        init_db()
        loaded_tables_2 = Name.query.all()

        self.assertEqual(len(loaded_tables_1),len(loaded_tables_2))
        for i in loaded_tables_2:
            with self.subTest(pkg= i.name):
                self.assertEqual(len(i.words), 7776)
        self.assertEqual(7776,len(Word.query.all())/len(loaded_tables_2))

        rm= Name.query.filter(Name.id==1).first()
        db.session.delete(rm)
        db.session.commit()
        self.assertEqual(len(loaded_tables_2)-1,len(Name.query.all()))
        self.assertEqual(7776,len(Word.query.all())/(len(loaded_tables_2)-1))

        init_db()
        self.assertEqual(len(loaded_tables_2),len(Name.query.all()))
        self.assertEqual(7776,len(Word.query.all())/len(Name.query.all()))



if __name__ == '__main__':
    unittest.main()