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
"""
L1=[1,2,3],[1,0,1],[0,0,0]
L2=[3,2,1],[0,3,0],[0,0,0]
"""
####################somme_matrix(A,B)

####################prod_matrix_vect(A,u)
def prod_matrix_vect(A,u):
    lenght_a=len(A)
    lenght_u=len(u)
    lenght_a0=len(A[0])
    C=[[]]
    if(lenght_a==lenght_u and lenght_a0==lenght_u):
        for i in range (lenght_a):
            w=0
            for k in range (lenght_a0):
                w=w+A[k][i]*u[i]
            C[0].append(w)
            
        
    return(C)

"""
L1=[1,2,3,4],[1,0,1,0],[0,0,0,0],[1,2,3,4]
a=[1,3,1,3]
print_matrix(prod_matrix_vect(L1,a))
"""
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

"""
L1=[1,2,3],[1,0,1],[0,0,0]
L2=[3,2,1],[0,3,0],[0,0,0]
print_matrix(prod_matrix(L1,L2))
"""
####################prod_matrix(A,B)

####################transpose(A)
def transpose(A):
    lenght_col=len(A)
    lenght_lin=len(A[0])
    C=[]
    for i in range (lenght_lin):
        C.append([])
        for j in range (lenght_col):
             C[i].append(A[j][i])
            
    return(C)

"""
L1=[1,2,3],[1,0,1],[0,0,0]
print_matrix(transpose(L1))
"""
####################transpose(A)

####################carre(n,xmin,ymin,a)
def carre(n,xmin,ymin,a):
    x=0
    y=1
    z=2
    W=[[],[],[]]
    dx=a/(n-1) #variation de x
    dy=a/(n-1) #variation de y
    for i in range (n):
        for j in range (a):
            px=xmin+dx*i+j
            py=ymin+dy*i
            W[x].append(px)
            W[y].append(py)
            W[z].append(f(px,py))
    
    return (W)
"""
n=50 #nombre de points
xmin=-1 #bornes de x
ymin=-1 #bornes de y
lenght_cube=100
W=carre(n,xmin,ymin,lenght_cube)
"""
####################carre(n,xmin,ymin,a)

####################renderer_3D
def renderer_3D(W)
    x=0
    y=1
    z=2
    fig = plt.figure() #Création de la figure
    ax = plt.axes(projection='3d') #Definition du tracé 3D
    ax.scatter3D(W[x],W[y],W[z]); #Définition des axes
    plt.show()

"""
L1=[1,2,3],[1,0,1],[0,0,0]
renderer_3D(L1)
"""
####################renderer_3D
