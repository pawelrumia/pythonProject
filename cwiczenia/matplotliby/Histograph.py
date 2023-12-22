import matplotlib.pyplot as plt
histograph_data = [1,2,3,4,5,6,7,8,9,10,3,6,2,7,1,8,2,5,0,25,8,3,2,6,11,14,13,16,17,12,1,8,18]
plt.hist(histograph_data, cumulative=True)
plt.show()