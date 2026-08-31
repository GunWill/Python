print("This project takes 5 data values as measurements and computes the min, max, avg & range of said values\n")
print("It is intended to be used for a neat little robot\n")


def m1() -> None: #Defined a function to call back to in case an invalid measurement is detected
    try:
        measurement1 = float(input("Enter first Measurement in Centimeters\n")) #Measurement 1-5
        measurement2 = float(input("Enter second Measurement in Centimeters\n")) 
        measurement3 = float(input("Enter third Measurement in Centimeters\n"))
        measurement4 = float(input("Enter fourth Measurement in Centimeters\n"))
        measurement5 = float(input("Enter fifth Measurement in Centimeters\n"))
    except ValueError: #Error if a non-numeric input is detected
        print("Invalid measurement, please begin again") #Prompts the user to enter the measurements again
        m1() 
   

print("The max value is", max(measurement1, measurement2, measurement3, measurement4, measurement5)) 
print("The min value is", min(measurement1, measurement2, measurement3, measurement4, measurement5)) 
measurements = [measurement1, measurement2, measurement3, measurement4, measurement5] #Put measurements in array to divide by a "dynamic" length, even though its always a length of 5
print("The average value is", sum(measurements)/len(measurements)) 


    print("The max value is", max(measurement1, measurement2, measurement3, measurement4, measurement5)) #Computes max, wish I used the array for this but I didnt think about it until later
    print("The min value is", min(measurement1, measurement2, measurement3, measurement4, measurement5)) #Computes min
    measurements = [measurement1, measurement2, measurement3, measurement4, measurement5] #Put measurements in array to divide by a "dynamic" length, even though its always a length of 5
    print("The average value is", sum(measurements)/len(measurements))  #Computes average w/ array values & length
    print("The range of values is: ", max(measurements)-min(measurements)) #Computes range w/ array values & length
m1() #Calls function

