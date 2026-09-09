with open("Student.csv", "w") as file:
    file.write("StudentId,Name,Attendance,Marks\n")
    file.write("1,Taniya,70,90\n")
    file.write("2,Rasti,75,92\n")
    file.write("3,Shivam,80,85\n")
    print("CSV file created.")