def convert_cel_to_far(celcius):
    return celcius*9/5+32
def convert_far_to_cel(fahrenheit):
    return (fahrenheit-32)*5/9

#MAIN PART
C=float(input("Enter a temperature in degrees C:"))
print(f"{C} degrees C = {round(convert_cel_to_far(C),2)} degress F")

F=float(input("Enter a temperature in degrees F:"))
print(f"{F} degrees F = {round(convert_far_to_cel(F),2)} degress C")


    

