

patients_dobs=['21-01-1998','26-10-1999','12-01-1985']
curr_yr=2022
def get_yob(patients_dobs):
    patients_yobs=[]
    for dob in patients_dobs:
        patients_yobs.append(int(dob.split('-')[2]))
    return patients_yobs

def get_ages(yobs):
    ages =[]
    for yr in yobs:
        ages.append(curr_yr - yr)
    return ages

def get_patient_status(get_yob, get_ages, dobs):
    is_major=[]
    yobs= get_yob(dobs)
    ages= get_ages(get_yob(dobs))
    for age in ages:
        if age >= 18:
            is_major.append(ages)
    return  is_major




print(get_patient_status(get_yob,get_ages ,patients_dobs))

