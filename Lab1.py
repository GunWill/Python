
try:
    measurement1 = float(input("Enter first Measurement in Centimeters\n"))
except ValueError:
    print("Invalid 1st measurement")


try:
    measurement2 = float(input("Enter second Measurement in Centimeters\n"))
except ValueError:
    print("Invalid 2nd measurement") 



try:
    measurement3 = float(input("Enter third Measurement in Centimeters\n"))
except ValueError:
    print("Invalid 3rd measurement")
        


try:
    measurement4 = float(input("Enter fourth Measurement in Centimeters\n"))
except ValueError:
    print("Invalid 4th measurement") 
      


try:
    measurement5 = float(input("Enter fifth Measurement in Centimeters\n"))
except ValueError:
    print("Invalid 5th measurement")  
   
print("The max value is", max(measurement1, measurement2, measurement3, measurement4, measurement5)) 
print("The min value is", min(measurement1, measurement2, measurement3, measurement4, measurement5)) 
measurements = [measurement1, measurement2, measurement3, measurement4, measurement5] #Put measurements in array to divide by a "dynamic" length, even though its always a length of 5
print("The average value is", sum(measurements)/len(measurements)) 