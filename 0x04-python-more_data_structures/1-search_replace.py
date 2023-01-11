#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            list_new.append(replace)
        else:
            list_new.append(my_list[i])
    return list_new
