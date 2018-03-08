def muliply_by_two(loopnum):
    return loopnum, loopnum*2

    
my_list = [1, 2, 3]
for i in my_list:
    original, changed = muliply_by_two(i)
    print(original)
    print(changed)
