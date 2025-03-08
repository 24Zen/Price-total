import math

a = float(input("Enter your cost: "))
b = 10
c = 1


result = a/(b-c)
bestprice = a + result
rounded_number = math.ceil(bestprice)

print("Your cost is: %.3f" %result)
print("Your best price for sale is : %.3f" %bestprice )
print("Your totalbest price for sale is :%.3f" %rounded_number )