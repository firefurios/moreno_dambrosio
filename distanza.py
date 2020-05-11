import numpy as np
class Minima:
	def __init__(self,P,N):
		self.num=0
		self.dist=np.linalg.norm(P[2]-P[1])
		for i in range(N):
			for k in range(i+1,N):
				self.newdist=np.linalg.norm(P[k]-P[i])
				if self.newdist<=self.dist:
					self.dist=self.newdist
					self.n1=k
					self.n2=i
				self.num+=1

	def count(self):
		return self.num

	def norma(self):
		return self.dist

	def points(self):
		return [self.n1,self.n2]
