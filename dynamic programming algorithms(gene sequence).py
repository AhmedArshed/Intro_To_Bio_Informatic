import numpy as np
flag=True
r=0
col=0
r_str=""
col_str=""
f=open("input2.txt")
for W in f:
    if flag==True:
        r=len(W)
        r_str=W
    else:
        col=len(W)
        col_str=W
    flag=False
f.close()
matrix=np.zeros((r,col),np.int32)

#scoring
match=input("enter match score ")
indel=input("enter indel score ")
mismatch=input("enter mismatch score ")


def fillinfarray():
    for i in range(1, r):
        for j in range(1, col):
            matrix[i,j] = max(  matrix[i-1, j-1] + score(i, j),
                                    matrix[i-1, j] + indel,
                                    matrix[i, j-1] + indel)
def score( i, j):
    if r_str[i-1]==col_str[j-1]:
        return match
    else:
        return mismatch 
    # else:
    #     matrix[0,0]=0
    #     matrix[0,1]=indel 
    #     matrix[1,0]=indel
    #     return a = matrix
def aligment( i, j):
    if i>0:
        n1=r_str[i-1]
    else:
        n1='_'
    if j>0:
        n2=col_str[j-1]
    else:
        n2='_'
    return (n1, n2)

def _traceback():
    alignment= []
    i = r-1
    j = col-1
    while i >0 and j>0:
        if matrix[i-1, j-1] + score(i, j) == matrix[i,j]:
            alignment.append((r_str[i-1],col_str[j-1]))
            i -= 1
            j -= 1
        elif matrix[i-1, j] + indel == matrix[i,j]:
            alignment.append(aligment(i, 0))
            i -= 1
        else:
            alignment.append(aligment(0, j))
            j -= 1
    alignment.reverse()
    print (alignment)

fillinfarray()
_traceback()
print (matrix)