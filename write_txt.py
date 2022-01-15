import csv
from email import header
from email.headerregistry import HeaderRegistry

with open('free.csv','r') as file:
    reader=csv.reader(file)
    header=[]
    header=next(reader)
    rows=[]
    for row in reader:
        rows.append(row)
with open('free.txt','w') as file:
    for row in rows:
        file.write(row[0]+'\t\t\t\t\t\t'+row[1]+'\n'+row[2]+'\n'+row[3]+'\n'+row[4]+'\n'+row[5]+'\n'+row[6]+'\n\n')