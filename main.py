# %%

import numpy as np
import matplotlib.pyplot as plt



# ----------- SCATTER PLOT -----------
# 1. SCATTER PLOT IS USED TO DISPLAY THE RELATIONSHIP BETWEEN TWO VARIABLES.
# 2. IT IS USED TO SEE THE CORRELATION BETWEEN TWO VARIABLES.
# 3. IT IS USED TO SEE THE DISTRIBUTION OF DATA POINTS.

X_data = np.random.rand(100) * 100
y_data = np.random.rand(100) * 100

plt.scatter(X_data, y_data, color="red", marker="*", s = 100, alpha=0.5)
plt.show()



# %%
# ----------- LINE PLOT -----------
# 1. LINE PLOT IS USED TO DISPLAY THE RELATIONSHIP BETWEEN TWO VARIABLES.
# 2. IT IS USED TO SEE THE CORRELATION BETWEEN TWO VARIABLES.
# 3. IT IS USED TO SEE THE DISTRIBUTION OF DATA POINTS.

X_data = [2007 + x for x in range(1, 16)]
y_data = [10, 70, 85, 60, 64, 56, 47, 34, 23, 45, 67, 78, 89, 90, 100]

plt.plot(X_data, y_data, color="crimson", lw="2", marker="o", markersize=10, markerfacecolor="white", markeredgewidth=1, markeredgecolor="black")
plt.show()



# %%
# ----------- BAR CHART -----------
# 1. BAR CHART IS USED TO DISPLAY THE RELATIONSHIP BETWEEN TWO VARIABLES.
# 2. IT IS USED TO SEE THE CORRELATION BETWEEN TWO VARIABLES.
# 3. IT IS USED TO SEE THE DISTRIBUTION OF DATA POINTS.

X_data = ["C++", "Python", "Java", "C#", "JavaScript"]
y_data = [20, 50, 70, 40, 60]

plt.bar(X_data, y_data, color="grey", edgecolor="black", linewidth=2, align='center')
plt.xlabel("Programming Languages", labelpad=20)
plt.show()




# %%
# ----------- HISTOGRAM -----------
# 1. HISTOGRAM IS USED TO DISPLAY THE DISTRIBUTION OF DATA.
# 2. IT IS USED TO SEE THE FREQUENCY OF DATA POINTS.

X_data = np.random.normal(20, 0.2, 1000)

plt.hist(X_data, bins=20, color="skyblue", edgecolor="black", linewidth=2)
plt.show()



# %%
# ----------- PIE CHART -----------
# 1. PIE CHART IS USED TO DISPLAY THE DISTRIBUTION OF DATA.
# 2. IT IS USED TO SEE THE FREQUENCY OF DATA POINTS.

languages = ["C++", "Python", "Java", "C#", "JavaScript"]
popularity = [20, 50, 70, 40, 60]
explodes = [0, 0.1, 0, 0, 0]

plt.pie(popularity, labels=languages, explode=explodes, shadow=False, autopct="%.2f%%", startangle=90)
plt.show()



# %%
# ----------- BOXPLOT -----------
# 1. BOXPLOT IS USED TO DISPLAY THE DISTRIBUTION OF DATA.
# 2. IT IS USED TO SEE THE FREQUENCY OF DATA POINTS.

point_1 = np.linspace(0, 20, 200)
point_2 = np.linspace(20, 200, 200)
point_3 = np.linspace(200, 220, 250)
point_4 = np.linspace(220, 280, 200)

all_points = np.concatenate((point_1, point_2, point_3, point_4))
plt.boxplot(all_points)
plt.show()



# %%
# SIMPLE DESIGN WITH TITLE AND LABELS
years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
income = [30, 20, 50, 80, 90, 100, 70, 80, 90, 100]

plt.plot(years, income)
plt.title("Income Progress Report", pad=20, fontsize=20, color="red", fontweight="bold", fontname="Comic Sans MS")
plt.xlabel("Years", labelpad=20, fontsize=12, fontweight="bold", fontname="Comic Sans MS")
plt.ylabel("Income", labelpad=20, fontsize=12, fontweight="bold", fontname="Comic Sans MS")
plt.show()


# %%
# DESIGN WITH MULTIPLE LINES

line_1 = [10, 20, 50, 40, 30, 60, 90, 80, 90, 100]
line_2 = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
line_3 = [30, 60, 50, 60, 90, 80, 90, 70, 110, 120]

y_ticks = list(range(0, 130, 10))

plt.plot(years, line_1, label="Company 1")
plt.plot(years, line_2, label="Company 2")
plt.plot(years, line_3, label="Company 3")
plt.xticks(years)
plt.yticks(y_ticks, [f"${i}K" for i in y_ticks])
plt.legend(loc="lower right")
plt.show()



# %%
# STYLING THE PIE CHART

scores = [20, 70, 60, 30, 40]
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

plt.pie(scores, labels=None, autopct="%.2f%%")
plt.legend(labels=players)
plt.show()



# %%
# PLOTTING DIFFERENT GRAPHS
x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)
plt.figure(2)
plt.plot(x2, y2)
plt.show()


# %%
# PLOT MULTIPLE IMAGES

x = np.arange(100)

fig, axis = plt.subplots(2, 2)

axis[0, 0].plot(x, np.sin(x))
axis[0, 0].set_title("Sine Graph")

axis[0, 1].plot(x, np.cos(x))
axis[0, 1].set_title("Cosine Graph")

axis[1, 0].plot(x, np.random.random(100))
axis[1, 0].set_title("Random Graph")

axis[1, 1].plot(x, np.log(x))
axis[1, 1].set_title("Tan Functions")

plt.tight_layout() # To adjust the layout
plt.savefig("output.png", dpi=300, bbox_inches="tight", transparent=False) # Save the plot in a file



# %%
# CREATING 3D GRAPH
axis = plt.axes(projection="3d")

x = np.arange(1, 50, 0.1)
y = np.sin(x)
z = np.cos(x)

axis.plot(x, y, z)
plt.show()
# %%
