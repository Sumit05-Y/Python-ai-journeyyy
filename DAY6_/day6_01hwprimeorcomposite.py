# Use for with for/else to check if a number is prime.
# Print all primes from 1 to 200. Hint: for i in range(2, num) 
#  if no divisor found, the else block runs

count_prime=0
num = 200
for i in range(2,num):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print(i,end=" ")
