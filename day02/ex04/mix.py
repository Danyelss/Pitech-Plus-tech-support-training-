def mix_list(list1, list2, list3, list4):
    returned_list = [ { str(list1[i]) : { "key_2" : list2[i], "key_3" : list3[i], "key_4" : list4[i] } } for i in range(len(list1))]
    return returned_list