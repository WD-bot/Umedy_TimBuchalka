def func(p1,p2,*args,k,**kwargs): #two key word parameters p1,p2
    #then a var positional parameter *args accepts variable number of arguments
    #k is a keyword parameter
    # and the var but for KeyWordArgs **kwargs
    print("positional-or-keyword:....{}, {}".format(p1,p2))
    print("var-positional (*args):...{}".format(args))
    print("keyword:..................{}".format(k))
    print("var-keyword:..............{}".format(kwargs))


func(1,2,3,4,5,9,k=6,key1=7,key2=8) #python learns how to stp for "k="
