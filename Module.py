import nester

movies =["Golden eye",1947,"Brossman",91,["The mask",["Die anotherday",1998,"king kong"]]]
print(movies)
def print_lol(the_list,level):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level)
        else:
            for tab_stop in range(level):

               print("\t", end='')
            print(each_item)





