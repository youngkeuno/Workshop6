from graphics import*
from time import*
from random import*


#1)
new_list=[]
states=open("states.csv", "r")
for line in states:
	new_line=line.split(",")
	name_state=new_line[0]
	new_list.append(name_state)


#2)
def abc(x):
	for y in x:
		l=len(x)
		n=0
		while n<l:
			if y>= x[n]:
				n=n+1
			else:
				n=l+1
		if n==l:
			print(y)

abc(new_list)

#3) We can still use the same abc() function for finding the largest population.
# We just have to create new_list2 and have it be a list of population sizes.

new_list2=[]
states=open("states.csv", "r")
for line in states:
	new_line=line.split(",")
	pop_state=int(new_line[3])
	new_list2.append(pop_state)

abc(new_list2)

#4)

new_list3=[]
states=open("states.csv", "r")
for line in states:
	new_line=line.split(",")
	x1=new_line[0]
	x2=new_line[1]
	x3=int(new_line[2])
	x4=int(new_line[3])
	y=[x1,x2,x3,x4]
	new_list3.append(y)

#5)

def pop_state(list):
	for x in list:
		l=len(list)
		n=0
		while n<l:
			if x[3]>= list[n][3]:
				n=n+1
			else:
				n=l+1
		if n==l:
			print("and the largest state is:")			
			print(x[0])
			print("with population:")
			print(x[3])

pop_state(new_list3)

#6)

def add_pop_dens(list):
	for x in list:
		y=x[3]/x[2]
		x.append(y)

#7)

def pop_dens_state(list):
	add_pop_dens(list)
	for x in list:
		l=len(list)
		n=0
		while n<l:
			if x[4]>= list[n][4]:
				n=n+1
			else:
				n=l+1
		if n==l:
			print("and the state with the highest population density is:")			
			print(x[0])
			print("with population density of:")
			print(x[4])

pop_dens_state(new_list3)
	

input("press a key to continue")
