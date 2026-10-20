import matplotlib.pyplot as plt
squares = [1, 8, 27, 64, 125]
fig, ax = plt.subplots()
ax.scatter(range(1, 6), squares, c=squares, cmap=plt.cm.Blues, s=10)
plt.show()