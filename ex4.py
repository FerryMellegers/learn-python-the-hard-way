#Creates the int "cars" with a value of 100
cars = 100
#Creates the int "space_in_a_car" with a value of 4.0, which is a floating point
space_in_a_car = 4.0
#Creates the int "drivers" with a value of 30
drivers = 30
#Creates the int "passengers" with a value of 90
passengers = 90
#Creates the int "cars_not_driven" which is constructed by subtracting the int "cars" by the int "drivers"
cars_not_driven = cars - drivers
#Creates the int "cars driven" which simply equals the int "drivers"
cars_driven = drivers
#Creates the int "carpool_capacity" which is constructed by taking the int "cars_driven" and multiplying it by the int "space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car
#Creates the int "average_passegers_per_car" by taking the int "passengers" and "deviding" it by the int "cars_driven"
average_passengers_per_car = passengers / cars_driven

#prints words using the quotes, and writing the int "cars" in between so that the sentence has a variable constructed inside
print "There are", cars, "cars available."
#uses the same principle of the line above
print "There are only", drivers, "drivers."
#uses the same principle of the line above
print "There will be", cars_not_driven, "empty cars today."
#uses the same principle of the line above
print "We can transport", carpool_capacity, "people today."
#uses the same principle of the line above
print "We have", passengers, "to carpool today."
#uses the same principle of the line above
print "We need to put about", average_passengers_per_car, "in each car."
#uses the same principle of the line above

#1) 4.0 is used because there is a chance that the math of the oquasion would be wrong otherwise.
#   By making it a floating point the oquasion is effectively able to have decimals for when the number gets devided.
#2) Executed
#3) Executed
#4) Executed
#5) Executed
#6) Executed