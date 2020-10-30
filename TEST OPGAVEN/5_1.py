import sys, time

def function(name, place):
    print("Ch1: Who this man...")
    time.sleep(1)
    print("Ch2: It's ya boi")
    time.sleep(1)
    print("Ch1: Eyoooo "+ name)
    time.sleep(1)
    print("Ch2:Ey "+ name+ " You down to hang bro")
    time.sleep(1)
    print("Ch1: sure thing.")
    time.sleep(1)
    print("Ch2: Where you at man...")
    time.sleep(1)
    print("Ch1: " + place)
    time.sleep(1)
    print("Ch2: I'll go your way!")
    time.sleep(1)
    print("Ch1: Ight")
    time.sleep(1)
    print("*call ends*")

function(sys.argv[1], sys.argv[2])