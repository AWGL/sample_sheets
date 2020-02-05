import unittest
import os
import getpass
from sample_sheets import *


class TestShire(unittest.TestCase):
    def setUp(self) -> None:
        test_raw_data = query_shire("20-00", "true")
        self.test_data = convert_bin_to_dictionary(test_raw_data)

    def test_worksheet_id(self):
        self.assertEqual(get_worksheet_id(self.test_data), "20-00")

    def test_user(self):
        self.assertEqual(get_user(self.test_data), getpass.getuser())

    def test_samples(self):
        self.assertEqual(get_sample_data(self.test_data),
                         [{"labNo": "19M1", "position": "1", "worksheet": "20-00", "test": "CRM Panel",
                           "updatedDate": "2020-01-20 00:00:00", "sex": "m", "referralReason": "Colorectal",
                           "firstName": "David", "comments": "FOCUS4"},
                          {"labNo": "19M2", "position": "2", "worksheet": "20-00", "test": "CRM Panel",
                           "updatedDate": "2020-01-25 00:00:00", "sex": "m", "referralReason": "Melanoma",
                           "firstName": "Peter", "comments": None},
                          {"labNo": "19M3", "position": "3", "worksheet": "20-00", "test": "CRM Panel",
                           "updatedDate": "2019-05-14 00:00:00", "sex": "f", "referralReason": "Colorectal",
                           "firstName": "Susan", "comments": "FOCUS4"},
                          {"labNo": "19M4", "position": "4","worksheet": "20-00", "test": "CRM Panel",
                           "updatedDate": "2020-01-25 00:00:00", "sex": "m", "referralReason": "Melanoma",
                           "firstName": "Thomas", "comments": None}])

    def test_file_generation(self):
        query_shire_to_file("20-00", "true", "test.json")
        assert os.path.exists("test.json")
        os.remove("test.json")

    def test_file_load(self):
        query_shire_to_file("20-00", "true", "test.json")
        data_from_file = load_shire_file("test.json")
        assert type(data_from_file) is dict and data_from_file
        os.remove("test.json")


if __name__ == '__main__':
    unittest.main()