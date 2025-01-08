import re

def string2list(string_list):
    temp = string_list.split(', ')
    return temp


def string2string(string_list):
    temp = string_list.split('返回：')
    return temp[-1]