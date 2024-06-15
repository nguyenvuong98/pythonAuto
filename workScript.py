import json

name_file_json = 'workScript.json'


def get_data_json():
    with open(name_file_json) as openfile:
        output_data = json.load(openfile)
    
    return output_data

def write_data_json(data):
    work_data_json = json.dumps(data, indent=4)
    
    with open(name_file_json, 'w') as outfile:
        outfile.write(work_data_json)

def get_works():
    data_json = get_data_json()

    return data_json["works"]

