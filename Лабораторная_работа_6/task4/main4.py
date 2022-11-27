# Так и не смог разобраться, в какой кодировке передан файл в задании, потому переименовал его на "input_old.csv", а
# на его место положил файл из задания task3

import json

INPUT_FILE = "input.csv"


def get_row_dict(names, values):
    res = {}
    for i in range(len(names)):
        res[names[i]] = values[i]
    return res


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    res = []
    is_first = True
    with open(filename, 'r', newline=new_line) as input_f:
        for line in input_f:
            line = line.strip()
            if is_first:
                names = line.split(delimiter)
                is_first = False
                continue

            values = line.split(delimiter)
            tmp = get_row_dict(names, values)
            res.append(tmp)
    return res


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
