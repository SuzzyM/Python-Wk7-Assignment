import pandas as pd

df = pd.read_csv("C:\\Users\\DONN\\Downloads\\mtcars-parquet.csv")

df.head(10)


import pyplot as plt
x_values = [1, 2, 3]
y_values = [6, 7, 8]

plt.plot(x_values, y_values)

plt.show()