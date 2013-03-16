"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Keep factoring and keeping track of largest
"""

toFactor = 600851475143 #number to factor
term = 2 #term to check
largest = 0 #largest factor so far

while toFactor > largest:
  if (toFactor % term) == 0:
    toFactor /= term
    if term > largest:
      largest = term
  else:
    term += 1

print(largest)
    


