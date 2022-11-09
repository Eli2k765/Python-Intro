import sys
import time

#sys has a lot of useful functions for interacting with the system
print(sys.version)
print(sys.platform)
print(sys.path)

#sys also has a lot of useful functions for handling I/O
for line in sys.stdin:
    if line.strip() == "exit":
        break
    sys.stdout.write(">> {}".format(line))

for i in range(1, 10):
    sys.stdout.write("{}".format(i))
    sys.stdout.flush()
    time.sleep(0.3)

#to get arguments from the command line we use sys.argv, the first argument is always the name of the script.
print(sys.argv)


#We can use sys.exit() to exit the script to handle errors or to exit the script

if len(sys.argv) < 2:
    print("Usage: python3 introToSys.py ARG ARG")
    sys.exit(1)

#We can then reference the arguments by their index
print("Argument 1: {}".format(sys.argv[1]))
print("Argument 2: {}".format(sys.argv[2]))
#More error handling
try:
    sys.argv[3]
except IndexError:
    print("Not enough arguments")
    sys.exit(1)
