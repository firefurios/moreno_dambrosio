import string
import numpy as np
import sys
from distanza import Minima

D=int(input("numero di dimensioni: "))
if D<1: sys.exit()
a=int(input("digita 0 per inserimento manuale, 1 per caricamento punti da file: "))
if a==0:
	N=int(input("numero di punti: "))
	if N<2: sys.exit()
	P=np.zeros(shape=(N,D))
	for i in range(N):
		print("inserisci le coordinate: ")
		for j in range(D):
			P[i][j]=float(input())
if a==1:
	N=0
	name=input("inserisci il nome del file: ")
	file=open(name,"r")
	for line in file:
		line=line.strip("\n")
		N+=1
	file.close()
	if N<2: sys.exit()
	P=np.zeros(shape=(N,D))
	f=open(name,"r")
	Q=f.readlines()
	for i in range(N):
		for j in range(D):
			P[i][j]=float((Q[i].split())[j])
	f.close()
b=Minima(P,N)
num=b.count()
dist=b.norma()
n1=b.points()[0]
n2=b.points()[1]
print("numero di punti = {}".format(N))
print("la distanza minore vale {} e separa i punti P{} = {} e P{} = {}".format(
																dist,n1,P[n1],n2,P[n2]))
print("numero di cicli = {}, ovvero la somma degli interi da 1 a N-1, con N numero di punti".format(num))