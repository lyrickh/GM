from impression import create_impression_from_json


_FAKE_DB = set()


def read_from_file(file_name):
    """
    Loads in a file of newline separated json objects, converts to Impressions and adds
    to the RAM cache

    :param file_name: `string` file of json impressions to be read
    :return:
    """
    global _FAKE_DB

    with open(file_name) as f:
        content = f.read()
    string_impressions = content.split("\n")

    for string_impression in string_impressions:
        if string_impression:
            impression = create_impression_from_json(string_impression)

            _FAKE_DB.add(impression)


if __name__ == "__main__":
    read_from_file("./example/impressions-shortlist")
