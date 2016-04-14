__author__ = 'Siam'

def min(a,b,c):
    if(a<b):
        if(a<c):
            return a
        else:
            return c
    else:
        if(b<c):
            return b
        else:
            return c

ugly =[1]
k=0
i2=i3=i5=1
i=0
while(1):
    starting_length = len(ugly)
    if(len(ugly) ==1500):
        break

    two = i2*2
    three = i3*3
    five = i5*5

    unum = min(two,three,five)

    if(two<five and two == three):
        if i2 in ugly:
            if unum not in ugly:
                ugly.append(unum)
        i2 = i2+1
        i3 = i3+1
    elif(two<three and two == five):
        if i2 in ugly:
            if unum not in ugly:
                ugly.append(unum)
        i2 = i2+1
        i5 = i5+1

    elif(three<two and three == five):
        if i3 in ugly:
            if unum not in ugly:
                ugly.append(unum)
        i3 = i3+1
        i5 = i5+1

    else:
        if(unum == two):
            if i2 in ugly:
                if unum not in ugly:
                    ugly.append(unum)
            i2 = i2+1
        elif(unum == three):
            if i3 in ugly:
                if unum not in ugly:
                    ugly.append(unum)
            i3 = i3+1
        else:
            if i5 in ugly:
                if unum not in ugly:
                    ugly.append(unum)
            i5 = i5+1

    ending_length = len(ugly)

    if(ending_length>starting_length):
        print ugly[len(ugly)-1]
    #ugly.append(unum)
    i=i+1


#print ugly