
################################
# FizzBuzz !
################################

num = 1
fizzcount = 0
buzzcount = 0
fizbuzxount = 0

while (num <= 100000):
	if (num % 3 == 0) and (num % 5 == 0):
		print(str(num) + ": FizzBuzz!")
		fizbuzxount += 1
	elif (num % 3 == 0):
		print(str(num) + ": Fizz!")
		fizzcount += 1
	elif (num % 5 == 0):
		print(str(num) + ": Buzz!")
		buzzcount += 1
	else:
		print(str(num) + ".")

	num +=1

print("____________________________________________")
print("Fizz\t\tBuzz\t\tFizzBuzz")
print(str("{:,}".format(fizzcount)) + "\t\t" + str("{:,}".format(buzzcount)) + "\t\t" + str("{:,}".format(fizbuzxount)))
print("____________________________________________")
