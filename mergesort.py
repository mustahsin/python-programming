from random import randint
from time import time

def bubble(A):
    print "bubbble"
    n = len(A)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (A[i]>=A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
            
        


def merge(L,R,A):       # merging 2 sorted array
    nl = len(L)
    nr = len(R)

    i,j,k = 0,0,0

    while(i<nl and j<nr):      # storing the lowest element in final array A
        if(L[i]<=R[j]):
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
        k = k+1

    # if some of the subarray finishes its walkthrouh    
    while(i<nl):
        A[k] = L[i]
        k = k+1
        i=i+1
    while(j<nr):
        A[k] = R[j]
        k=k+1
        j=j+1
            
        

def mergesort(A):
    n = len(A)
    if (n<2):
        return
    mid = n/2

    left = []
    right = []

    for i in range(0,mid):      # creating the leftarray from start to mid
        left.append(A[i])
        
    for i in range(mid,n):     # creating rightarray from mid to end
        right.append(A[i])

    mergesort(left)
    mergesort(right)
    merge(left,right,A)


a=[]

for i in range(1,9000):
    t = randint(1,1000)
    a.append(t)


b = list(a)

#print a
print "merge sort"
start = time()

mergesort(b)
ct = time()

print ct - start

#print a


#a=[]

##for i in range(1,9000):
##    t = randint(1,1000)
##    a.append(t)

#print a

start = time()

bubble(a)

ct = time()

print ct - start

#print a

