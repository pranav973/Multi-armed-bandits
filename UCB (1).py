import numpy as np
import matplotlib.pyplot as plt
import math

# Bernolli bandits with "k" arms, n plays

def ucb(mean,k,alpha,n,ep):
	
	regret = 0
	for a in range(ep):
		est_mean = np.zeros(k)
		for t in range(k):
			if np.random.uniform(0,1,1) < mean[t]:
				
				est_mean[t] = 1
			
		arm_count = np.ones(k)
		for x in range(1,n+1):
			con = (alpha*math.log(x))/2.0
			con = np.sqrt(con)
			ucb = est_mean+con*np.power(arm_count,-0.5)
			arm_played = np.where(ucb == max(ucb))[0][0]
			arm_count[arm_played] += 1
			regret += mean[0]-mean[arm_played]
			if np.random.uniform(0,1,1) < mean[arm_played]:
				est_mean[arm_played] = (float(arm_count[arm_played]-1)/arm_count[arm_played])*est_mean[arm_played]+(1.0/arm_count[arm_played])
			else:
				est_mean[arm_played] = (float(arm_count[arm_played]-1)/arm_count[arm_played])*est_mean[arm_played]
	return regret/ep



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
	

# multiple episodes
''' We will create a bandit with 2 arms and run the experiment for different number of times , each 50 episodes
'''
mean = [0.4,0.6]
mean = mean.tolist()
mean.sort(reverse = True)
no_runs = [100,200,500,750,1000,1500,2000,2500,3000,5000,7500,10000,12500,15000,17500,20000,22500,25000,27500,30000]
log_T = [math.log(x) for x in no_runs]
avg_regret = [ucb(mean,2,2.0,x,100) for x in no_runs]
regret_axis = [thompson(mean,x,100) for x in no_runs]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(no_runs,avg_regret,color = 'r',label='UCB')
ax1.scatter(no_runs,regret_axis,color = 'b',label='Thompson')
plt.legend(loc="upper left")
plt.xlabel("logT")
plt.ylabel("avg_reward")
plt.title("Regret_comparison")
plt.show()
