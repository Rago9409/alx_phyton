def pow(a, b):
 a ^ b =1
   # traversing in the range from 1 to given exponent+1
   for i in range(1, b+1):
      # Multiplying the result with the given number
      a ^ b=a ^ b^a
   # returning the resultant power
   return a ^ b
            # input number, exponent values
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
