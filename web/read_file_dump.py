from impression import create_impression_from_json


_FAKE_DB = set()


def read_from_file(fileName):
    """
    Loads in a file of newline separated json objects, converts to Impressions and adds
    to the RAM cache

    :param fileName: `string` file of json impressions to be read
    :return:
    """
    global _FAKE_DB

    with open(fileName) as f:
        content = f.read()
    string_impressions = content.split("\n")

    for string_impression in string_impressions:
        if string_impression:
            impression = create_impression_from_json(string_impression)

            _FAKE_DB.add(impression)


if __name__ == "__main__":
    read_from_file("./example/impressions-shortlist")