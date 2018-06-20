import json
from impression import create_impression_from_json
from db import add_impression


def read_from_file(file_name):
    """
    Loads in a file of newline separated json objects, converts to Impressions and adds
    to the RAM cache

    :param file_name: `string` file of json impressions to be read
    :return:
    """

    with open(file_name) as f:
        content = f.read()
    string_impressions = content.split("\n")

    for string_impression in string_impressions:
        if string_impression:
            impression = create_impression_from_json(json.loads(string_impression))
            add_impression(impression)


if __name__ == "__main__":
    read_from_file("../example/impressions-shortlist")
