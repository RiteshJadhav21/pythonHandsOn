

patients_dobs=['21-01-1998','26-10-1999','12-01-1985']
curr_yr=2022
def get_yob(dob):
    return dob.split('-')[2]

patients_yobs= list(map(get_yob,patients_dobs ))

print(patients_yobs)

def get_ages(yob):
    return curr_yr-yob

patients_ages = list(map(get_ages,patients_yobs))
print(patients_ages)

def get_adult_age(age):
    return age >= 18


adult_patient_age = list(map(get_adult_age, patients_ages))
print(adult_patient_age)

def get_patient_status(get_yob, get_ages, dobs):
         pass






