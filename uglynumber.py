__author__ = 'Siam'

prime =[2,3,5]
ugly =[1]

for i in xrange(2,100):
    num =i
    j=0
    current =[]
    flag =0
    while(j<len(prime)):
        if(num%prime[j]==0):
            num = num/prime[j]
            if prime[j] not in current:
                current.append(prime[j])
            continue
        else:
            j = j+1

    if(num!=1):
        current.append(num)
    if(len(current) == 0):
        continue

    flag =1
    for x in xrange(0,len(current)):
        if(current[x] in prime):
            continue
        else:
            flag =0

    if(flag == 1):
        ugly.append(i)

print ugly