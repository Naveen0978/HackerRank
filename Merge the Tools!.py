def merge_the_tools(string, k):
    # your code goes here
     for x in xrange(0,len(string),k):
        u_list=list(set(string[x:x+k]))
        print (''.join(u_list))
