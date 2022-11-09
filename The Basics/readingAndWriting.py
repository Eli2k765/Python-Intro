#To open the file, use the built-in open() function.
#The open() function takes two parameters; filename, and mode.


#There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists


#In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

#write() will overwrite any existing file with the same name.
f = open("demofile.txt", "w")
f.write("This is the first test line.")
f.close()

f = open("demofile.txt", "rt")
print(f.read())
f.close()

#append() will add to the end of the file.
f = open("demofile.txt", "a")
f.write("\nThis is the second test line.")
f.close()

#readlines() will read the file line by line.
f = open("demofile.txt", "r")
print(f.readlines())

#If we try to read the file again, we get an empty string, because we have already reached the end of the file:
print("There's nothing left to read: ", f.read())

#To read the file again, we have to use the seek() method to set the file position to the beginning of the file:
f.seek(0)
print(f.read())

#readline() will read one line of the file:
print(f.readline())

#There are some other functions that can be used to get more information about the file:

#The tell() method returns the position of the file read/write pointer, in bytes:
f.seek(5)
print(f.tell())

#The name attribute returns the name of the file:
print(f.name)

#The closed attribute returns if the file is closed or not:
print(f.closed)

#The mode attribute returns the mode the file was opened in:
print(f.mode)
f.close()

