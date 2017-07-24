#Josh Richardson
# Group 56

import time

def factorial(num):
    if(num == 1):			#base case
        return 1
    else :
        return num * factorial(num - 1)

def fibonacci(num):
    if(num == 0) or (num == 1):	#base cases
        return 1
    else :
        return fibonacci(num - 1) + fibonacci(num - 2)

def valid_int(description):	#we are going to do this a lot, so use a function
    while True:
        try:
            valid = int(raw_input("Please enter " + description + " (int): "))
        except:
            print "That's not an integer."
        else:
            return valid

upper_bound = valid_int("an upper bound")

while True:
    calculation = raw_input("Please enter FIB for fibonacci or FACT for factorial: ")
    if calculation.upper() == "FIB":
        total_time = 0
        for num in range(1, upper_bound + 1):
            start = time.clock()
            fib = fibonacci(num)
            end = time.clock()
            total_time += (end - start)
            print "Calculating fibonacci(" + str(num) + ") = " + str(fib) + "  took: " + str(end-start) + " seconds."
        break
    if calculation.upper() == "FACT":
        total_time = 0
        for num in range(1, upper_bound + 1):
            start = time.clock()
            fact = factorial(num)
            end = time.clock()
            total_time += (end - start)
            print "Calculating factorial(" + str(num) + ") = " + str(fact) + "  took: " + str(end-start) + " seconds."
        break
    else:
        pass

print "Total time: " + str(total_time) + " seconds."
