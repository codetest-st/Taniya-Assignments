with open("student.csv", "r") as file:
    header=file.readline().strip().split()
    print(header)
    for h in header:
        print("%10s |" %(h), end="")
    print()

    for line in file:
        data = line.strip().split()
        Student_id = data[0]
        Name = data[1]
        Attendance = data[2]
        Marks = data[3]
        Result = data[4]
        print("%10s | %10s | %10s | %10s |" %(Student_id,Name,Attendance,Marks,Result))