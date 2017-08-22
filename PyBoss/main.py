import os
import csv
import us_state_abbrev

data1 = os.path.join("..", "Pythonday1", "employee_data1.csv")
data2 = os.path.join("..", "Pythonday1", "employee_data2.csv")
counter = 0
current = data1
emp_id = []
first = []
last = []
dob = []
ssn = []
state = []
while counter < 2:
    with open(current,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            if row[1] == "Name":
                continue
            emp_id.append(row[0])
            space = row[1].find(" ")
            f = row[1][:space] 
            first.append(f)
            l = row[1][space+1:]
            last.append(l)
            dob.append(row[2])
            new_ssn = "***-**-"+row[3][7:]
            ssn.append(new_ssn)
            abb = us_state_abbrev.us_state_abbrev[row[4]]
            state.append(abb)
    current = data2
    counter = counter + 1
total = zip(emp_id, first, last, dob, ssn, state)
header = ['Emp ID','First Name','Last Name','DOB','SSN','State']
output = os.path.join('boss.csv')
with open(output, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(header)
    writer.writerows(total)
