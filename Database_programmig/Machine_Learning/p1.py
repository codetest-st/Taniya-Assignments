import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("student_performance.csv")
print(df.head())

#chart code here 

plt.figure(figsize=(5,8))
plt.title("Chart Title")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.grid(True)
plt.show()