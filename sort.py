def sort_dictionary(dict):
    newListTuple = []
    sortedValues = sorted(dict.values(), key=lambda x:x[1])
    for i in sortedValues:
        for key,value in dict.items():
            if (value == i):
                newListTuple.append((key, value[0]))
    return newListTuple