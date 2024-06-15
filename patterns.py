# ===========  USING STRINGS =============

# -------  left triangle -------

str1 = input("String:")
lenght = len(str1)
for i in range(lenght):
    for j in range(i+1):
        print(str1[i],end=" ")
    print()


# -------  left triangle (len - increment )-------

str1 = input("String:")
lenght = len(str1)
for i in range(lenght):
    for j in range(i+1):
        print(str1[j],end=" ")
    print()


# -------  right triangle -------

str1 = input("String:")
lenght = len(str1)
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(str1[i],end=" ")
    print()


# -------  right triangle (len-incre) -------

str1 = input("String:")
lenght = len(str1)
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(str1[j],end=" ")
    print()

# -------  pyramid (len-incre) -------

str1 = input("String:")
lenght = len(str1)
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(str1[j],end=" ")
    print() 

#------ right inverted triangle ---------

str1 = input("String: ")
length = len(str1)
for i in range(length):
    for j in range(i-0):
        print(" ",end=" ")
    for j in range(i+0,length):
        print(str1[i], end=" ")
    print()

 #------ left inverted triangle ---------

str1 = input("String: ")
length = len(str1)
for i in range(length):
    for j in range(i+0,length):
        print(str1[i], end=" ")
    print()

#------ left inverted triangle (len-incre) ---------

str1 = input("String: ")
length = len(str1)
for i in range(length):
    for j in range(i+0,length):
        print(str1[j], end=" ")
    print() 

#------ inverted pyramid ---------

str1 = input("String: ")
length = len(str1)
for i in range(length):
    for j in range(i):
        print(" ", end="")
    for j in range(i-0,length):
        print(str1[i], end=" ")
    print() 

#------ diamond ---------

str1 = input("String:")
lenght = len(str1)
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(str1[j],end=" ")
    print() 
length = len(str1)
for i in range(length):
    for j in range(i+0):
        print(" ", end="")
    for j in range(i+0,length):
        print(str1[i], end=" ")
    print()       

 # ===========  USING STAR " * " =============

#-------- right triangle ---------

for i in range(0,5):
    for j in range(i):
        print("*",end=" ")
    print()  

#-------- left triangle ---------

for i in range(0,5):
    for j in range(0,5-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print() 

#-------- pyramid ---------

for i in range(0,5):
    for j in range(0,5-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()  

#-------- right inverted triangle ---------

for i in range(0,5):
    for j in range(i,5):
        print("*",end=" ")
    print() 

#-------- left inverted triangle ---------

for i in range(0,5):
    for j in range(i-0):
        print(" ",end=" ")
    for j in range(i+0,5):
        print("*",end=" ")
    print()

#-------- inverted pyramid ---------

for i in range(0,5):
    for j in range(i-0):
        print(" ",end="")
    for j in range(i+0,5):
        print("*",end=" ")
    print()

#------- Diamond --------

for i in range(0,5):
    for j in range(0,5-i-1):
        print(" ",end="")
    for j in range(i+0):
        print("*",end=" ")
    print()
for i in range(0,3):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+0,3):
        print("*",end=" ")
    print()  

# ===========  USING convertion of int to chr =============

#-------- right triangle ---------

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()

#-------- right triangle (len incre) ---------

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
              
#-------- left triangle ---------

for i in range(65,70):
    for j in range(70-i-1):
        print(" ",end=" ")
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()

#-------- left triangle (len incre)---------

for i in range(65,70):
    for j in range(70-i-i):
        print(" ",end=" ")
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print() 

#-------- right inverted triangle ---------

for i in range(65,70):
    for j in range(i-0,70):
        print(chr(i),end=" ")
    print()

#-------- right inverted triangle (len-incre) ---------

for i in range(65,70):
    for j in range(i-0,70):
        print(chr(j),end=" ")
    print() 

#-------- left inverted triangle ---------

for i in range(65,70):
    for j in range(i-65):
        print(" ",end=" ")
    for j in range(i+0,70):
        print(chr(i),end=" ")
    print()

#-------- pyramid ---------

for i in range(65,70):
    for j in range(i-65):
        print("",end=" ")
    for j in range(i+0,70):
        print(chr(i),end=" ")
    print() 

#-------- diamaind ---------

for i in range(65,70):
    for j in range(0,70-i-1):
        print(" ",end="")
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()
for i in range(65,70):
    for j in range(i-65):
        print(" ",end="")
    for j in range(i+0,70):
        print(chr(i),end=" ")
    print() 


n=6
for i in range(0,n+1):
    print(" "*(n-i), end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()


#---- 0WN ------

for i in range (1,10):
    for j in range(10-i-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()
