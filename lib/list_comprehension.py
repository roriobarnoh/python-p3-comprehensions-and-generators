#!/usr/bin/env python3

def return_evens(num_list):
    list = []
    for num in num_list:
        if num % 2 == 0:
            list.append(num)
    return list

def make_exclamation(sentence_list):
    my_array = []
    for sentence in sentence_list:
        my_array.append(sentence + "!")
    return my_array