####################somme_vect(u,v)
def somme_vect(u,v):
    lenght=len(u)
    w=[]
    if(lenght==len(v)):
        for i in range (lenght):
            w.append(u[i]+v[i])
            
    return(w)

#print(somme_vect([0,2],[2,1]))
####################somme_vect(u,v)

####################prodscal_vect(u,v)
def prodscal_vect(u,v):
    lenght=len(u)
    w=0
    if(lenght==len(v)):
        for i in range (lenght):
            w=w+u[i]*v[i]
            
    return(w)

#print(prodscal_vect([0,2,3],[2,1,3]))
####################prodscal_vect(u,v)

####################identite(n)
def identite(n):
    w=[[1]]
    for i in range (n-1):
        lenght=len(w)
        for j in range (lenght):
            w[j].append(0)
           
        w.append([])
        for j in range (lenght):
            w[lenght].append(0)
           
        w[lenght].append(1)
    return(w)

#print(identite(5))
####################identite(n)

####################print_matrix(m)
def print_matrix(m):
    lenght=len(m)
    for i in range (lenght):
        print(m[i])
        
#print_matrix(identite(5))
####################print_matrix(m)

####################somme_matrix(A,B)
def somme_matrix(A,B):
    lenght_a=len(A)
    lenght_b=len(B)
    C=[]
    if(lenght_a==len(B) and len(A[0])==len(B[0])):
        for i in range (lenght_a):
            C.append([])
            for j in range (lenght_b):
                C[i].append(A[i][j]+B[i][j])
            
    return(C)

#L1=[1,2,3],[1,0,1],[0,0,0]
#L2=[3,2,1],[0,3,0],[0,0,0]
####################somme_matrix(A,B)

####################prod_matrix_vect(A,u)
def prod_matrix_vect(A,u):
    lenght_a=len(A)
    lenght_u=len(u)
    C=[[]]
    if(lenght_a==len(u) and len(A[0])==len(u)):
        for i in range (lenght_a):
            w=0
            for k in range (len(A[0])):
                w=w+A[k][i]*u[i]
            C[0].append(w)
            
        
    return(C)

#L1=[1,2,3,4],[1,0,1,0],[0,0,0,0],[1,2,3,4]
#a=[1,3,1,3]
#print_matrix(prod_matrix_vect(L1,a))
####################prod_matrix_vect(A,u)

####################prod_matrix(A,B)
def prod_matrix(A,B):
    lenght_a=len(A)
    lenght_b=len(B)
    C=[]
    if(len(A[0]) == lenght_b):
        for i in range (lenght_a):
            C.append([])
            for j in range (len(B[0])):#lenght_b
                w=0
                for k in range (lenght_b):
                    w=w+A[i][k]*B[k][j]
                C[i].append(w)
            
        
    return(C)
    
L1=[1,2,3],[1,0,1],[0,0,0]
L2=[3,2,1],[0,3,0],[0,0,0]
print_matrix(prod_matrix(L1,L2))
####################prod_matrix(A,B)
