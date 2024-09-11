import matplotlib.pyplot as plt
import random
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)
x_data = []
for i in range(1000):
    x_data.append(random.uniform(-5, 5))
# print(x_data)
ax.plot(x_data)
fig.savefig("temp_utter.png")
