import random
import matplotlib.pyplot as plt

user = 0
dict = {}
round = 0
while round < 100000:
    n = random.randint(10, 100)
    l, r = int(user - n/2), int(user + n/2)
    m = random.randint(l, r)
    # game over and reset
    if m == user:
        dict[user] = dict.get(user, 0) + 1
        user = 0
        round += 1
    else:
        user = user + 1
    print(round)


x_axis = []
y_axis = []
for k, v in dict.items():
    x_axis.append(k)
    y_axis.append(v)

plt.bar(x_axis, y_axis)
plt.title('The end position of gamen')
plt.xlabel('position')
plt.ylabel('rounds')
plt.show()


x_axis = []
y_axis = []
for k, v in dict.items():
    x_axis.append(k)
    y_axis.append(v/round*100)

plt.bar(x_axis, y_axis)
plt.title('The end position of gamen')
plt.xlabel('position')
plt.ylabel('rounds percent')
plt.show()


x_axis = ["<10", "10-100", "100-300", ">300"]
x, y, z, t = 0, 0, 0, 0
for k, v in dict.items():
    if k < 10:
        x += v / round * 100
    if k >= 10 and k <= 100:
        y += v / round * 100
    if k > 100 and k <= 300:
        z += v / round * 100
    if k > 300:
        t += v / round * 100
y_axis = [x, y, z, t]
print(x + y + z)

plt.bar(x_axis, y_axis)
plt.text(0, x, '%.2f%%' % x, ha='center', va='bottom')  
plt.text(1, y, '%.2f%%' % y, ha='center', va='bottom')
plt.text(2, z, '%.2f%%' % z, ha='center', va='bottom')
plt.text(3, t, '%.2f%%' % t, ha='center', va='bottom')
plt.title('The end position of gamen')
plt.xlabel('position')
plt.ylabel('rounds percent')
plt.show()
