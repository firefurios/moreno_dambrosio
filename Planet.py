import numpy as np
class Planet:
	def __init__(self,M,m,rx,ry,rz,vx,vy,vz,dt,num,n):
		self.R=np.zeros(shape=(n+1,num,3))
		self.V=np.zeros(shape=(n+1,num,3))
		self.A=np.zeros(shape=(n+1,num,3))
		self.E=np.zeros(n)
		for i in range(num):
			self.R[0][i]=[rx[i],ry[i],rz[i]]
			self.V[0][i]=[vx[i],vy[i],vz[i]]
		for ns in range(n):
			for i in range(num):
				self.E[ns]+=0.5*m[i]*(np.linalg.norm(self.V[ns][i]))**2-(
						6.67e-11*M*m[i]/(np.linalg.norm(self.R[ns][i])))
				self.A[ns+1][i]=-(self.R[ns][i]/((np.linalg.norm(self.R[ns][i]))**3))*6.67e-11*M
				for j in range(num):
					if j!=i:
						self.A[ns+1][i]-=6.67e-11*m[j]*(
						(self.R[ns][i]-self.R[ns][j])/((np.linalg.norm(self.R[ns][i]-self.R[ns][j]))**3))
						self.E[ns]-=6.67e-11*m[j]*m[i]/(np.linalg.norm(self.R[ns][i]-self.R[ns][j]))
			self.V[ns+1]=self.V[ns]+0.5*self.A[ns]*dt
			self.R[ns+1]=self.R[ns]+self.V[ns+1]*dt
			self.V[ns+1]=self.V[ns+1]+0.5*self.A[ns+1]*dt
			print(self.E[ns]/self.E[0])


	def pos(self):
		return self.R
