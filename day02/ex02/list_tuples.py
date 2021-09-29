def gen_tuples(start, end):
    returned_list = [(y,x) for x in range(start, end+1) for y in range(x,0,-1) ]
    return returned_list
