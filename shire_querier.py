import subprocess
import json

from config import path_to_java
from config import encoding


def query_shire(worksheet_id, test_db_or_not):
    return subprocess.check_output([path_to_java, '-jar', 'query_shire.jar', worksheet_id, test_db_or_not])


def query_shire_to_file(worksheet_id, test_db_or_not, output_filename):
    return subprocess.check_output([path_to_java, '-jar', 'query_shire.jar', worksheet_id, test_db_or_not,
                                    output_filename])


def load_shire_file(file_name):
    try:
        with open(file_name) as f:
            shire_data = json.load(f)
    except IOError:
        raise FileNotFoundError(f"Unable to load data from file {file_name}. File not found.")
    return shire_data


def convert_bin_to_dictionary(bin_data):
    s = bin_data.decode(encoding)
    return json.loads(s)


def get_worksheet_id(data):
    return data.get('worksheet')


def get_user(data):
    return data.get('user')


def get_sample_data(data):
    return data.get('samples')


def main():
    # Call java jar file to query shire database
    o = query_shire("20-00", "true")
    d = convert_bin_to_dictionary(o)
    print(o)


if __name__ == '__main__':
    main()
