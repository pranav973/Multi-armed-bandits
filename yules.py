import numpy as np
import matplotlib.pyplot as plt

def yules(time,m_1,m_2):
    red = 1
    blue = 1
    red_array = [np.random.exponential(1.0/m_1)]
    blue_array = [np.random.exponential(1.0/m_2)]
    t_1 = 0
    t_2 = 0
    while True:
        
        flag1 = True
        flag2 = True
        repro_red = red_array[0]
        repro_blue = blue_array[0]
        if t_1+repro_red <= time:
            for x in range(red):
                red_array[x] -= repro_red
            
            red_array[0] = np.random.exponential(1.0/m_1)
            for t in range(1,red):
                if red_array[t] > red_array[t-1]:
                    break
                else:
                    (red_array[t],red_array[t-1]) = (red_array[t-1],red_array[t])
            red_array.insert(0,0)
            red_array[0] = np.random.exponential(1.0/m_1)
            for t in range(1,red):
                if red_array[t] > red_array[t-1]:
                    break
                else:
                    (red_array[t],red_array[t-1]) = (red_array[t-1],red_array[t])
            red += 1
            flag1 = False
            
            t_1 += repro_red
        if t_2+repro_blue <= time:
            for x in range(blue):
                blue_array[x] -= repro_blue
            
            blue_array[0] = np.random.exponential(1.0/m_2)
            for t in range(1,blue):
                if blue_array[t] > blue_array[t-1]:
                    break
                else:
                    (blue_array[t],blue_array[t-1]) = (blue_array[t-1],blue_array[t])
            blue_array.insert(0,0)
            blue_array[0] = np.random.exponential(1.0/m_2)
            for t in range(1,blue):
                if blue_array[t] > blue_array[t-1]:
                    break
                else:
                    (blue_array[t],blue_array[t-1]) = (blue_array[t-1],blue_array[t])
            blue += 1
            flag2 = False
            
            t_2 += repro_blue
        if flag1 and flag2:
            break
    return [red,blue,t_1,t_2,repro_red,repro_blue]
red_list = []
blue_list = []
for x in range(25):
    red = 0
    blue = 0
    for t in range(20):
       res = yules(5+((0.2)*(x)),0.6,0.4)
       red += res[0]
       blue += res[1]
    red = float(red)/20.0
    blue = float(blue)/20.0
    red_list.append(red)
    blue_list.append(blue)
print(red_list)
print(blue_list)     
plt.scatter(blue,red,color = 'red')
plt.xlabel("No of blue balls")
plt.ylabel("No of red balls")
plt.title("yules process")
plt.show()

       
           
                    
