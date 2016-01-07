movies =["Golden eye",1947,"Brossman",91,["The mask",["Die anotherday",1998,"king kong"]]]
print(movies)
for a in movies:
    if isinstance(a,list):
        for b in a:
            if isinstance(b,list):
                for deeper_item in b:
                    print(deeper_item)
            else:
                 print(b)
    else:
        print(a)
