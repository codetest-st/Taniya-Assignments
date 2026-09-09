import pandas as pd
import matplotl_student_performance.csv")
print(df.head())

#chart code here 
course_avg=df.groupby("Course")["FinalMarks"].mean()

plt.figure(figsize=(5,7))
course_avg.plot(kind="bar",color="green")

plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("AverageMarks")
plt.xticks(rotation=0)
plt.show()