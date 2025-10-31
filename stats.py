def count_words(txt):
    num_words = len(txt.split())
    return num_words


def count_chars(txt):
    dic = {}

    for char in txt.lower():
        if not dic.get(char):
            dic[char] = 1
        else:
            dic[char] += 1

    return dic


def sort_dicts(dict):
    lst = []
    for key in dict:
        lst.append({ "char": key, "num": dict[key]})
    lst.sort(reverse=True, key=sort_on)
    return lst


def sort_on(dict):
    return dict["num"]
