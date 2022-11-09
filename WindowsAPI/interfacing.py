from ctypes import *

#MessageBoxA is a Windows API function that displays a message box.
#There are four parameters that MessageBoxA takes.
#1. A handle to the window that owns the message box.
#2. The text of the message box.
#3. The text of the title bar.
#4. The type of message box.

MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = [c_int, c_char_p, c_char_p, c_int]
MessageBoxA.restype = c_int

print(MessageBoxA(0, b"Hello World!", b"Hello", 0))

#GetUserNameA is a function that retrieves the name of the user.
#The GetUserNameA function is defined in the advapi32.dll library.
#There are three parameters that GetUserNameA takes.
#1. A pointer to a buffer that receives the user name.
#2. A pointer to a variable that specifies the size of the buffer, in characters.
#3. A pointer to a variable that receives the size of the user name, in characters.

GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = [c_char_p, POINTER(c_int)]
GetUserNameA.restype = c_int

buffer = create_string_buffer(256)
size = c_int(sizeof(buffer))
GetUserNameA(buffer, byref(size))
print(buffer.value)

#GetSystemDirectoryA is a function that retrieves the path of the system directory.
#The GetSystemDirectoryA function is defined in the kernel32.dll library.
#There are two parameters that GetSystemDirectoryA takes.
#1. A pointer to a buffer that receives the path.
#2. A variable that specifies the size of the buffer, in characters.

GetSystemDirectoryA = windll.kernel32.GetSystemDirectoryA
GetSystemDirectoryA.argtypes = [c_char_p, c_int]
GetSystemDirectoryA.restype = c_int

buffer = create_string_buffer(256)
GetSystemDirectoryA(buffer, sizeof(buffer))
print(buffer.value)

#GetWindowRect is a function that retrieves the dimensions of the bounding rectangle of the specified window.
#The GetWindowRect function is defined in the user32.dll library.
#There are two parameters that GetWindowRect takes.
#1. A handle to the window.
#2. A pointer to a RECT structure that receives the screen coordinates of the upper-left and lower-right corners of the window.

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = [c_int, POINTER(RECT)]
GetWindowRect.restype = c_int

class RECT(Structure):
    _fields_ = [('left', c_int), ('top', c_int), ('right', c_int), ('bottom', c_int)]

rect = RECT()
GetWindowRect(0, byref(rect))
print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)


