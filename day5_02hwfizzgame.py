#print number 1 to 100.But: if divisible by 3 print "Fizz".if by 5, print 'Buzz'.
#  if both,print'fizzbuzz'.if by 7,print 'bazz' if by both 3 and 7 print 'fizzbazz' .
# *** print the numbers but also count how many of each type***
Fizz_count=0
Buzz_count=0
fizzbuzz_count=0
bazz_count=0
fizzbazz_count=0
for i in range(1,101):
    if i % 5 ==0 and i % 3 ==0:
        print(f"{"fizzbuzz"!r}")
        fizzbuzz_count += 1

    elif i % 7 ==0 and i % 3 ==0:
        print(f"{"fizzbazz"!r}")
        fizzbazz_count += 1
    elif i % 5 ==0:
        print(f"{"Buzz"!r}")
        Buzz_count += 1
    elif i % 3 ==0:
        print(f"{"Fizz"!r}")
        Fizz_count += 1

    elif i % 7 ==0:
        print(f"{"bazz"!r}")
        bazz_count +=1
    else: 
        print(i)
print(f"The no of Fizz are {Fizz_count}")
print(f"The no of Buzz are {Buzz_count}")
print(f"The no of FizzBuzz are {fizzbuzz_count}")
print(f"The no of Bazz are {bazz_count}")
print(f"The no of FizzBazz are {fizzbazz_count}")



    
    
        