def delete(arr: list, index: int = None):
    # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
        index = len(arr) - 1

    if index < 0 or index >= len(arr):
        return arr.copy()

    start = arr[:index]
    end = arr[index+1:]

    res = start + end

    return res


def main():

    print(delete([0, 0, 1, 2], index=1))  # [0, 1]
    print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
    print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]


if __name__ == "__main__":
    main()
