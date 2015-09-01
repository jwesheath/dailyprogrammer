import json


def find_json_path(this, search_phrase, trace=list()):
    if isinstance(this, (dict, list)):
        for key, value in this.items() if isinstance(this, dict) else enumerate(this):
            if find_json_path(value, search_phrase, trace):
                trace.insert(0, key)
                return ' -> '.join([str(x) for x in trace])
    if this == search_phrase:
            return True
    return False


with open('challenge1.txt') as infile:
    j = json.loads(infile.read())
    print(find_json_path(j, 'dailyprogrammer'))

