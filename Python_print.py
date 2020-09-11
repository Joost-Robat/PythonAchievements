a = True

while a:
	hello = "Hello, my name is {owner}. What's yours?\n"
	print(hello.format(owner = "Joost"))
	
	username = input("My name is:")
	print("Hello " + username, "!")
	
	question = input("Would you like to know the date?yes/no\n")
	if question == "yes":
		import datetime
		
		x = datetime.datetime.now()
		
		print("Today is the " +  x.strftime("%d"), "of " + x.strftime("%B"), ".")
	
	
	test2 = input("Would you like to repeat this conversation? yes/no\n")
	if test2 == "yes":
		continue
	
	a = False
	print("The program shall close now, see you next time " + username, "!")
	print("Also a thank you from my family:")
	def my_function(fname):
		print(fname + "Robat")
	my_function("Anne ")
	my_function("Michael ")
	my_function("Vanessa ")
	import time
	time.sleep(2)
	exit