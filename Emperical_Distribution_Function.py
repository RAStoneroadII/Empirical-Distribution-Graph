# Emperical Distribution Function for a small array/list
import pandas as pd
import matplotlib.pyplot as plt
original_list = [1.0,-1.2,0.4,1.3,-0.3,-1.4,0.4,-0.5,-0.2,-1.3,-1.0,-1.3,2.0,1.0,0.3,0.4,2.1,0.0] #Test data w/in brackets
item_count = len(original_list)
original_list.sort()
empirical_list = []
for numbers in original_list:
    empirical_list.append(numbers / item_count)
plt.plot(empirical_list)
plt.title('Emperical Distribution Function')
plt.xlabel('Data points')
plt.show()

