import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("student_performance.csv")
print(df.head())

#chart code here 

plt.figure(figsize=(5,8))
plt.plot(
df=["StudentName"],
dg=["FinalMarks"],
marker="o",
color="blue"
)

plt.title("Student Final Marks")
plt.xlabel("Student")
plt.ylabel("FinalMarks")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()