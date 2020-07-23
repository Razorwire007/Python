def most_frequent(str1):
    dict = {}
    for l in str1:
        keys = dict.keys()
        if l in keys:
            dict[l] += 1
           
        else:
            dict[l] = 1
    return dict
print(most_frequent(input()))

    
    
