def get_count_char(str_: str):
    # TODO подсчитать количество каждой буквы в строке в аргументе str_
    lower_str = str_.lower()

    res_dict = {}
    for char in lower_str:
        if not str.isalpha(char):
            continue
        if res_dict.get(char) is None:
            res_dict[char] = 1
        else:
            res_dict[char] += 1

    return res_dict


def second_func(count_dict: dict):
    amount = 0
    for value in count_dict.values():
        amount += value
    res_dict = {}

    for key in count_dict:
        res_dict[key] = count_dict[key] / amount

    return res_dict


def main():
    main_str = """
        Данное предложение будет разбиваться на отдельные слова.
        В качестве разделителя для встроенного метода split будет выбран символ пробела.
        На выходе мы получим список отдельных слов.
        Далее нужно отсортировать слова в алфавитном порядке,
        а после сортировки склеить их с помощью метода строк join. Приступим!!!!
        """

    count_dict = get_count_char(main_str)
    print(count_dict)


if __name__ == "__main__":
    main()
