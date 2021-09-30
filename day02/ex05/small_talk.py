def summary_dict(string_data):
    listOfDict = [ { "sender" : i.split()[2], "receiver": i.split()[i.split().index("receiver:") + 1], "message": "".join([x + " " for x in i.split() if i.split().index(x) > i.split().index("message:") and i.split().index(x) < i.split().index("receiver:")  ])[:-2][1:] } for i in string_data.split('\n')]
    return listOfDict