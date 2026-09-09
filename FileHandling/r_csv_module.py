import csv
with open("Student.csv", "r") as file:
   reader= csv.reader(file)
   for row in reader:
      print(row)
