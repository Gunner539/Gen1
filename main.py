from collections.abc import Iterable

nested_list = [
    ['a', 'b', 'c', ['11', '22', ['33', '44', ['13', '1a']]]],
    ['d', 'e', 'f'],
    [1, 2, None],
    'aer'
]

def get_flat_list(nested_list, flat_list):
    for el in nested_list:
        if isinstance(el, Iterable) and type(el) != str:
            get_flat_list(el, flat_list)
        else:
            flat_list.append(el)

    return flat_list


def flat_generator(nested_list):
    flat_list = get_flat_list(nested_list, [])
    limit = len(flat_list)
    cursor = 0
    while cursor < limit:
        yield flat_list[cursor]
        cursor += 1


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)