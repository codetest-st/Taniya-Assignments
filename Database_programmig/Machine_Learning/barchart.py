import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("cleaned_student_performance.csv")
print(df.head())

#chart code here 

plt.figure(figsize=(5,8))
plt.bar(
df=["StudentName"],
dg=["FinalMarks"],
color="orange"
)

plt.title("Student Marks Comparison")
plt.xlabel("Student")
plt.ylabel("FinalMarks")
plt.xticks(rotation=45)
plt.show()