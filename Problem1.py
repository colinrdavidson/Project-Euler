"""
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

mult1 = 3 #lowest multiple
mult2 = 5 #next lowest multiple
mult3 = mult1 * mult2 
end = 1000 - 1 #end of multiple range
max1 = 0 #maximum multiple of mult1 in (1, end)
max2 = 0 #maximum multiple of mult2 in (1, end)
max3 = 0 #maximum multiple of mult3 in (1, end)

for x in range(0, mult3 - 1):
  if (max1 == 0) and ((end - x) % mult1 == 0):
    max1 = end - x
    print("max1 is:", max1)
  elif (max2 == 0) and ((end - x) % mult2 == 0):
    max2 = end - x
    print("max2 is: ", max2)
  elif (max3 == 0) and ((end - x) % mult3 == 0):
    max3 = end - x
    print("max3 is: ", max3)

n1 = max1 / mult1
n2 = max2 / mult2
n3 = max3 / mult3
sum1 = mult1 * n1 * (n1 + 1) / 2
sum2 = mult2 * n2 * (n2 + 1) / 2
sum3 = mult3 * n3 * (n3 + 1) / 2
output = sum1 + sum2 - sum3

print("n1:", n1, "n2:", n2, "n3:", n3, "sum1:", sum1, "sum2:", sum2, "sum3:", sum3)
print("output:", output)
