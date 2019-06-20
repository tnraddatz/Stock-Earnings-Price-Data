from matplotlib import pyplot as plt

plt.scatter([-4,-3,-2,-1,0,1, 2, 3, 4], [-4,-3,-2,-1,0,1, 2, 3, 4])
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('Actual Result')
plt.ylabel('Estimate Result')
plt.show()