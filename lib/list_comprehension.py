#!/usr/bin/env python3

def return_evens(num_list):
    if len(num_list)<1:
        return([])
    else:
         returned_list =[ num * 1 for num in num_list if num % 2 ==0]
         return returned_list

def make_exclamation(sentence_list):
    if len(sentence_list) <1:
        return([])
    else:
        returned_with_exclamtions =[sentance + "!" for sentance in sentence_list]
        return returned_with_exclamtions