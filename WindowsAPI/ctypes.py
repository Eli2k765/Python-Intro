#Ctypes is a module that allows you to call Windows API functions from Python.

from ctypes import *

#Lets first go over the different types of data that ctypes supports. The following are the most common types of data that you will use when calling Windows API functions.

# c_char - A single character
# c_byte - A single byte
# c_ubyte - An unsigned byte
# c_short - A 16-bit integer
# c_ushort - An unsigned 16-bit integer
# c_int - A 32-bit integer
# c_uint - An unsigned 32-bit integer
# c_long - A 32-bit integer
# c_ulong - An unsigned 32-bit integer
# c_longlong - A 64-bit integer
# c_ulonglong - An unsigned 64-bit integer
# c_float - A 32-bit floating point number
# c_double - A 64-bit floating point number
# c_char_p - A pointer to a null-terminated string
# c_wchar_p - A pointer to a null-terminated unicode string
# c_void_p - A pointer to a void type

c0 = c_char(b'a')
print(c0)
print(c0.value)

class POINT(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]

p = POINT()
p.x = 10
p.y = 20
print(p.x)
print(p.y)

