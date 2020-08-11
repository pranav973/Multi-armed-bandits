import numpy as np
import matplotlib.pyplot as plt
import math

def thompson(mean,n,ep):
	
	
	 # for beta distributions
	regret = 0
	for x in range(ep):
		arm_count = [0,0]
		par = [1,1,1,1]
		for y in range(n):
			sample1 = np.random.beta(par[0],par[1],1)
			sample2 = np.random.beta(par[2],par[3],1)
			if sample1 > sample2:

				arm_count[0] += 1
				if np.random.uniform(0,1,1) < mean[0]:
					par[0] += 1
				else:
					par[1] += 1
			else:
				arm_count[1] += 1
				regret += mean[0]-mean[1]
				if np.random.uniform(0,1,1) < mean[1]:
					par[2] += 1
				else:
					par[3] += 1
	return regret/ep
mean = np.random.uniform(0,1,2)
mean = mean.tolist()
mean.sort(reverse = True)
x_axis = [1000,2000,4000,5000,7000,10000,12000,15000,20000,25000,30000]
mod_axis = [math.log(x) for x in x_axis]
regret_axis = [thompson(mean,x,10) for x in x_axis]
plt.plot(mod_axis,regret_axis,color = "r")
plt.xlabel("logT")
plt.ylabel("avg_regret")
plt.title("Thompson sampling")
plt.show()



