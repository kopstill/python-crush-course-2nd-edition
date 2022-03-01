import matplotlib.pyplot as plt

plt.style.use('seaborn')

plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus'] = False

x_values = [1, 2, 3, 4, 5]
# x_values = range(1, 5001)
y_values = [x_value ** 3 for x_value in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)

ax.set_title("立方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的立方", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
