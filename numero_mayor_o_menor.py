import random
n=random.randint(0, 5)
o=random.randint(0, 5)


print("...................................................................")
print("......................Numero mayor o menor.........................")
print("...................................................................")


# imput 

n=int(input("digite un numero"))
o=int(input("digite un nuemero"))

# prosesing

h= n>o
p= n<o

 
# output

if n>o:
 print(n,'es mayor que',o )
elif n<o:
 print(n,'es menor que',o )
else:
 print(n,'es igual a',o )



