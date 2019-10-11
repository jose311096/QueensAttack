import numpy as np


def queensAttack (n,k,r_q,c_q,obs_f,obs_c):

    #creamos el tablero
    m=np.zeros((n,n)) 

    #colocamos a la reina en el tablero
    m[r_q-1,c_q-1] = 1

    #colocamos los obstaculos en el tablero
    for i in range(k):
        m[obs_f[i]-1,obs_c[i]-1]=2
    
    #jugadas arriba
    fa=r_q-1
    vali = True

    while(fa>=0):
        if(m[fa,c_q-1]==2):
            vali=False
        if(vali==True):
            m[fa,c_q-1]=3
            fa=fa-1
        elif(vali==False):
            m[fa,c_q-1]=0
            fa=fa-1
            

    #jugadas abajo
    fab=r_q-1
    vali2 = True

    while(fab<=n-1):
        if( m[fab,c_q-1]==2):
            vali2=False
        if(vali2==True):
            m[fab,c_q-1]=3
            fab=fab+1
        elif(vali2==False):
            m[fab,c_q-1]=0
            fab=fab+1
        

    #jugadas izquierda
    ca=c_q-1
    vali3 = True

    while(ca>=0):
        if( m[r_q-1,ca]==2):
            vali3=False
        if(vali3==True):
            m[r_q-1,ca]=3
            ca=ca-1
        elif(vali3==False):
            m[r_q-1,ca]=0
            ca=ca-1

    #jugadas derecha
    cd=c_q-1
    vali4 = True

    while(cd<=n-1):
        if( m[r_q-1,cd]==2):
            vali4=False
        if(vali4==True):
            m[r_q-1,cd]=3
            cd=cd+1
        elif(vali4==False):
            m[r_q-1,cd]=0
            cd=cd+1

    
    #jugadas diagonal 1
    fa1=r_q-2
    ca1=c_q-2
    vali5=True

    if(fa1<0 or ca1<0):
        print()
    else:
        while(fa1>=0 and ca1>=0):
            if( m[fa1,ca1]==2):
                vali5=False
            if(vali5==True):
                m[fa1,ca1]=3
                fa1=fa1-1
                ca1=ca1-1
            elif(vali5==False):
                m[fa1,ca1]=0
                fa1=fa1-1
                ca1=ca1-1


    #jugadas diagonal 2
    fa2=r_q-2
    cs1=c_q
    vali6=True

    if(fa2<0 or cs1>n-1):
        print()
    else:
        while(fa2>=0 and cs1<=n-1):
            if( m[fa2,cs1]==2):
                vali6=False
            if(vali6==True):
                m[fa2,cs1]=3
                fa2=fa2-1
                cs1=cs1+1
            elif(vali6==False):
                m[fa2,cs1]=0
                fa2=fa2-1
                cs1=cs1+1


    #jugadas diagonal 3
    fs=r_q
    ca2=c_q-2
    vali7= True

    if(fs>n-1 or ca2<0):
        print()
    else:
        while(fs<=n-1 and ca2>=0):
            if(m[fs,ca2]==2):
                vali7=False
            if(vali7==True):
                m[fs,ca2]=3
                fs=fs+1
                ca2=ca2-1
            elif(vali7==False):
                m[fs,ca2]=0
                fs=fs+1
                ca2=ca2-1


    #jugadas diagonal 4
    fs2=r_q
    cs2=c_q
    vali8=True

    if(fs2>n-1 or cs2>n-1):
        print()
    else:
        while(fs2<=n-1 and cs2<=n-1):
            if(m[fs2,cs2]==2):
                vali8=False
            if(vali8==True):
                m[fs2,cs2]=3
                fs2=fs2+1
                cs2=cs2+1
            elif(vali8==False):
                m[fs2,cs2]=0
                fs2=fs2+1
                cs2=cs2+1

    
    #colocamos los obstaculos en el tablero
    for i in range(k):
        m[obs_f[i]-1,obs_c[i]-1]=2

    #colocamos a la reina en el tablero
    m[r_q-1,c_q-1] = 1
        

    #contamos las casillas jugables
    contador=0

    for i in range(n):
        for j in range(n):
            if(m[i,j]==3):
                contador=contador+1

    print ()
    print (m)
    print ()
    print ("el numero de casillas jugables por la reina es: " + str(contador))
    
    
    return()


r_q,c_q,n,k,a,b = 0,0,0,0,0,0

validar = 1


#pedimos la longitud y los obstaculos y validamos el tamaño maximo del tablero
while validar <=1:
    print ("Ingrese la longitud del tablero y el numero de obstaculos:")
    n,k=map(int,input().split())
    if(n>0 and n<=100000):
        validar = 2

validar2 = 1

#pedimos la posicion de la reina y validamos que este dentro del tablero
while validar2 <=1 :
    print ("Ingrese la fila y la columna de la posicion de la reina:")
    r_q,c_q=map(int, input().split())
    if(r_q<=n and c_q<=n):
        validar2 = 2


obs_f = [0] * k
obs_c = [0] * k
validar3 = 1


#pedimos la posicion de los obstaculos y validamos que no se ubiquen en la posicion de la reina
for i in range(k):
    validar3=1
    while validar3 <=1 :
        print ("Ingrese fila y columna del obstaculo #" + str(i+1) +":")
        obs_f[i],obs_c[i]=map(int, input().split())
        if (obs_f[i] != r_q or obs_c[i] != c_q):
            if(obs_f[i] <= n and obs_c[i] <= n):
                validar3 = 2

queensAttack(n,k,r_q,c_q,obs_f,obs_c)
