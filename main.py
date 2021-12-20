def sort_sentence(sentence):
    import operator
    a = sentence.split(' ')
    dict_unsorted = {i : len(i) for i in a}
    sorted_d = sorted(dict_unsorted.items(), key=operator.itemgetter(1))
    str_ = ''
    for key, i in sorted_d:
        str_ += key + ' '
    return str_