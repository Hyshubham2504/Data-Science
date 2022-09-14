def sum_eo(n,t):
    sum=0
    if t=='e':
        for i in range(2,n,2):
            sum+=i
        return sum
    elif t=='o':
        for i in range(1,n,2):
            sum+=i
        return sum
    else:
        return -1
print(sum_eo(10,'o'))