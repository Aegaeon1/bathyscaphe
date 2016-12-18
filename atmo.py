import random
import sys

m = 10
n = 10

v=[[0 for col in range(m)] for row in range(n)]
#u=[[random.randint(0,1000) for col in range(m)] for row in range(n)]

u=[[0 for col in range(m)] for row in range(n)]

u[2][2]=100


user=""

while user != "q":

	d=[[0 for col in range(m)] for row in range(n)]
	for i in range(m) :
		out = ""
		for j in range(n) :
			out +=  str(int(u[i][j]))+" "
		print(out +"\n")
	for i in range(m) :
		for j in range(n) :
			neighbors = []

			if(i!=0):
				neighbors.append(u[i-1][j])
				
			if(i!=m-1):
				neighbors.append(u[i+1][j])
				
			if(j!=0):
				neighbors.append(u[i][j-1])
				
			if(j!=n-1):
				neighbors.append(u[i][j+1])
				
			v[i][j] += sum(neighbors)/len(neighbors) - u[i][j]
			v[i][j] = v[i][j]* 0.99
			d[i][j] = v[i][j]

			v[i][j] =0 
	for i in range(m) :
		for j in range(n) :
		
			u[i][j] += d[i][j]

	user = sys.stdin.read(1)
