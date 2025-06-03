universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

#enrollment_stats:
def enrollment_stats( universities):
    total_students=[]
    tuition_fees=[]
    for singleuni in universities:
        name,students,tuition=singleuni
        total_students.append(students)
        tuition_fees.append(tuition)
    return total_students, tuition_fees

def mean(data):
    return sum(data)/len(data)
def median(data2):
    sorted_data=sorted(data2)
    n=len(sorted_data)
    if n%2==1:
        return sorted_data[n//2]
    else:
        mid1=sorted_data[n/2]
        mid2=sorted_data[n/2+1]
        return (mid1+mid2)/2
    
# Main

enrollments,tuitions=enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)
mean_students = mean(enrollments)
mean_tuition = mean(tuitions)
median_students = median(enrollments)
median_tuition = median(tuitions)

print("*****************")
print("UNIVERSITY STATS")
print("*****************")
print(f"Total students: {total_students}")
print(f"Total tuition: ${total_tuition}")
print(f"\nStudent mean: {mean_students:.2f}")
print(f"Student median: {median_students}")
print(f"Tuition mean: ${mean_tuition:.2f}")
print(f"Tuition median: ${median_tuition}")