import subprocess
import json

from config import path_to_java
from config import encoding


def get_worksheet_id(data):
    return data.get('worksheet')


def get_user(data):
    return data.get('user')


def get_sample_data(data):
    return data.get('samples')


def main():
    # Call java jar file to query shire database
    o = subprocess.check_output([path_to_java, '-jar', 'query_shire.jar', '20-00', 'true'])
    s = o.decode(encoding)
    d = json.loads(s)


if __name__ == '__main__':
    main()