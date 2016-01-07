movies =["Golden eye",1947,"Brossman",91,["The mask",["Die anotherday",1998,"king kong"]]]
def print_a(the_list):
    for x in the_list:
        if isinstance(x,list):
            print_a(x)
        else:
            print(x)
print_a(movies)