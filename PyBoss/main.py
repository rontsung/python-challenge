import os
import csv
# import dictionary of state abbreviations
import us_state_abbrev as abbr
# select csv
data1 = os.path.join("employee_data1.csv")
# information from csv will be classified and placed in these lists
emp_id = []
first = []
last = []
dob = []
ssn = []
state = []
with open(data1,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # run through all rows of the csv
    for row in csvreader:
        # don't include the header in the classification
        if row[1] == "Name":
            continue
        # classify each ID
        emp_id.append(row[0])
        # break each name into first and last, then add each to appropriate list
        space = row[1].find(" ")
        f = row[1][:space] 
        first.append(f)
        l = row[1][space+1:]
        last.append(l)
        # break the date into year, month, and day, and re-sort into appropriate format
        year = row[2][:4]
        month = row[2][5:7]
        day = row[2][8:]
        dob.append(month+'/'+day+'/'+year)
        # blot out first digits of SSN and add to list
        new_ssn = "***-**-"+row[3][7:]
        ssn.append(new_ssn)
        # use state abbreviation
        a = abbr.us_state_abbrev[row[4]]
        state.append(a)
# zip the lists to a tuple
total = zip(emp_id, first, last, dob, ssn, state)
# new header
header = ['Emp ID','First Name','Last Name','DOB','SSN','State']
# output file
output = os.path.join('boss.csv')
# write the header and then the tuple to the output file
with open(output, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(header)
    writer.writerows(total)



