import numpy as np
import matplotlib.pyplot as plt





def bern_bandit(m1,m2,trials):
    red = 1
    blue = 1
    
    n_r = 0
    n_b = 0
    
    for x in range(trials):
        sample = np.random.uniform(0,1)
        if sample >= (float(blue)/float(blue+red)):
            n_r += 1
            reward_sample = np.random.uniform(0,1)
            if reward_sample < m1:
                red += 1
        else:
            reward_sample = np.random.uniform(0,1)
            n_b += 1
            if reward_sample < m2:
                blue += 1
    est_m1 = float(red)/float(n_r)
    est_m2 = float(blue)/float(n_b)
    return [n_r,n_b,red,blue,est_m1,est_m2]


regret= []
episodes = 1000
regret_blue = 0
for t in range(1,2001):
    for k in range(episodes):
        regret_blue += bern_bandit(0.6,0.4,t*10)[1]
    regret.append((float(regret_blue)/float(1000)))
    regret_blue = 0
ax = range(10,20001,10)
plt.plot(ax,regret,color = 'r')
plt.xlabel("No of times arm pulled")
plt.ylabel("Regret")
plt.title("Bernoulli bandit")
plt.show()





        
