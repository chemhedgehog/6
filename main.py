def rot(num):
    num = str(num)
    n = len(num)
    for i in range(n):
        if num[i]=='6':
            return int(num[:i]+'9'+num[i+1:])
    return int(num)

