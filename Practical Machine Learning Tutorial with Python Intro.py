import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
import random
import time


##########################

style.use("fivethirtyeight")
# style.use("ggplot")

def create_data(hm, variation, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variation, variation)
        ys.append(y)
        if correlation and correlation == "pos":
            val += step
        elif correlation and correlation == "neg":
            val -= step
    xs = [i for i in range((len(ys)))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def slop_and_interception(xs, ys):
    m = ( (mean(xs) * mean(ys)) - (mean(xs * ys)) ) / ( (mean(xs)**2) - (mean(xs**2)) )
    b = mean(ys) - m * mean(xs)
    return m, b

def squared_error(ys_orignal, ys_line):
    return (sum((ys_orignal - ys_line)**2))

def coffeicient_of_determation(ys_orignal, ys_line):
#######################    y_mean_line = [mean(ys_orignal) for y in ys_orignal]
    y_mean_line = mean(ys_orignal)
    sqr_error_ys = squared_error(ys_orignal, ys_line)
    sqr_error_mean = squared_error(ys_orignal, y_mean_line)
    return 1 - (sqr_error_ys / sqr_error_mean)

xs, ys = create_data(100, 100, 2, correlation="pos")

m, b = slop_and_interception(xs, ys)
print("slop m = ", m)
print("intercepiton of Y axies b = ", b)

regression_line = [(m * x) + b for x in xs]

mean_of_y = mean(ys)
print(mean_of_y)

predict_x = 22
predict_y = (m * predict_x) + b

r_squared = coffeicient_of_determation(ys, regression_line)

print(r_squared)

plt.scatter(xs, ys, color="r", label="xs & ys points")
plt.scatter(predict_x, predict_y, color="k", label="predict point")
plt.plot(xs, regression_line, color="g", label="regression line", linewidth=1)
plt.axhline(mean_of_y, linewidth=1)
plt.legend(loc=4)
plt.show()

