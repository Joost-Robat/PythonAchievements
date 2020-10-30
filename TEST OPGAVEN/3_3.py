import time
weekdag = input('geef een dag aan\n').lower()
print("test")
time.sleep(2)
if weekdag == "zondag" or weekdag == "zaterdag":
	print("Het is weekend!")
elif weekdag == "maandag":
	print("Het is de kutste dag van de week...")
elif weekdag == "dinsdag":
	print("Dinsdag is niet zo erg...")
elif weekdag == "woensdag":
	print("Woensdag betekent halverwege!")
elif weekdag == "donderdag":
	print("Donderdag dus de week is bijna voorrbij!")
elif weekdag == "vrijdag":
	print("VRIJDAG IS DE BESTE DAG VAN DE WEEK!")
else:
	print('geef een dag aan')