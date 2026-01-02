# You have to use the fundamentals of Python taught in module2
# 1.Read file bank-data.csv
# 2.Build a set of unique jobs
# 3.Read the input from the command line –profession
# 4.Check if the professionis onthe list
# 5.Print whetherthe client is eligible
# Enhancements for codeYou can try these enhancements in code
# 1.Compute max and min age for loan eligibility based on data in CSVfile
# 2.Store max and min age in the dictionary
# 3.Make the professionalcheck case insensitive
# 4.Currently program ends after the check. Take the input in the whileloop and end only if the user types "END" for the profession

import csv

profession_ages = {}
profession_job = set()
with open('./files/bank-data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        profession = row['job']
        profession_job.add(row['job'].upper())
        age = int(row['age'])
        if profession not in profession_ages:
            profession_ages[profession] = []
        profession_ages[profession].append(age)

while True:
    read_job = input('Enter Profession :')

    if read_job.upper() == "END":
        print("Program ended.")
        break

    if read_job.upper() in set(profession_job):
        print("Profession Present")

    with open('./files/bank-data.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['job'].upper() == read_job.upper():
                if row['y'].upper() == 'YES':
                    print("Client is eligible")
                    break

for profession, ages in profession_ages.items():
    print(f"Profession: {profession}")
    print(f"  Minimum eligible age: {min(ages)}")
    print(f"  Maximum eligible age: {max(ages)}")