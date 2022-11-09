#To perform dll injection on a remote process we will perform the following steps: 
#1. Open a handle to the remote process using OpenProcess.
#2. Allocate memory in the remote process using VirtualAllocEx.
#3. Write the DLL path to the allocated memory using WriteProcessMemory.
#4. Create a remote thread in the remote process using CreateRemoteThread.
#5. Close the handle to the remote process using CloseHandle.

#First lets import the necessary libraries.
from ctypes import *
from ctypes.wintypes import *

#Next we will establish the ctypes for the functions we will be using.
#OpenProcess is a function that opens an existing process object.
#The OpenProcess function is defined in the kernel32.dll library.
#There are four parameters that OpenProcess takes.
#1. The access to the process object.
#2. A value that indicates whether the function returns a handle to a process object that has the PROCESS_QUERY_INFORMATION and PROCESS_VM_READ access rights.
#3. The identifier of the process to be opened.
#4. A pointer to a variable that receives a value that is nonzero if the function succeeds and zero if the function fails.
OpenProcess = windll.kernel32.OpenProcess
OpenProcess.argtypes = [DWORD, BOOL, DWORD]
OpenProcess.restype = HANDLE

#VirtualAllocEx is a function that allocates a new region of memory in the virtual address space of a specified process.
#The VirtualAllocEx function is defined in the kernel32.dll library.
#There are five parameters that VirtualAllocEx takes.
#1. A handle to the process whose memory space is to be allocated.
#2. A pointer to the starting address of the region to allocate.
#3. The size of the region to allocate, in bytes.
#4. The type of memory allocation.
#5. The memory protection for the region of pages to be allocated.
VirtualAllocEx = windll.kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD, DWORD]
VirtualAllocEx.restype = LPVOID

#WriteProcessMemory is a function that writes data to an area of memory in a specified process.
#The WriteProcessMemory function is defined in the kernel32.dll library.
#There are five parameters that WriteProcessMemory takes.
#1. A handle to the process memory to be modified.
#2. A pointer to the base address in the specified process to which data is written.
#3. A pointer to the buffer that contains data to be written in the address space of the specified process.
#4. The number of bytes to be written to the specified process.
#5. A pointer to a variable that receives the number of bytes transferred into the specified process.
WriteProcessMemory = windll.kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = [HANDLE, LPVOID, LPCVOID, SIZE_T, POINTER(SIZE_T)]
WriteProcessMemory.restype = BOOL

#CreateRemoteThread is a function that creates a thread that runs in the virtual address space of another process.
#The CreateRemoteThread function is defined in the kernel32.dll library.
#There are eight parameters that CreateRemoteThread takes.
#1. A handle to the process in which the thread is to be created.
#2. A pointer to a SECURITY_ATTRIBUTES structure that specifies a security descriptor for the new thread and determines whether child processes can inherit the returned handle.
#3. The initial size of the stack, in bytes. The system rounds this value to the nearest page.
#4. A pointer to the application-defined function of type LPTHREAD_START_ROUTINE to be executed by the thread and represents the starting address of the thread in the remote process.
#5. A pointer to a variable to be passed to the thread function.
#6. The flags that control the creation of the thread.
#7. A pointer to a variable that receives the thread identifier.
#8. A pointer to a variable that receives the handle to the new thread.
CreateRemoteThread = windll.kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = [HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, POINTER(DWORD)]
CreateRemoteThread.restype = HANDLE

#CloseHandle is a function that closes an open object handle.
#The CloseHandle function is defined in the kernel32.dll library.
#There are one parameter that CloseHandle takes.
#1. A valid handle to an open object.
CloseHandle = windll.kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL

#Next we will define the constants that we will be using.
#PROCESS_ALL_ACCESS is a constant that specifies all possible access flags for the process object.
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

#PAGE_EXECUTE_READWRITE is a constant that specifies that the memory can be read, written, or executed.
PAGE_EXECUTE_READWRITE = 0x40

#Now we will define the variables that we will be using.
#dllPath is a variable that contains the path to the dll that we will be injecting.
dllPath = "C:\\Users\\Public\\Documents\\test.dll"

#processName is a variable that contains the name of the process that we will be injecting the dll into.
processName = "notepad.exe"

#Now we will define the functions that we will be using.
#GetProcessId is a function that gets the process identifier for the specified process name.
#There are one parameter that GetProcessId takes.
#1. The name of the process.
def GetProcessId(processName):
    #First we will create a snapshot of all the processes in the system.
    hProcessSnap = windll.kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    #Next we will check if the snapshot was created successfully.
    if hProcessSnap == INVALID_HANDLE_VALUE:
        #If the snapshot was not created successfully we will return 0.
        return 0
    #Next we will create a PROCESSENTRY32 structure.
    pe32 = PROCESSENTRY32()
    #Next we will set the size of the structure.
    pe32.dwSize = sizeof(PROCESSENTRY32)
    #Next we will check if we can get the first process in the snapshot.
    if not windll.kernel32.Process32First(hProcessSnap, byref(pe32)):
        #If we cannot get the first process in the snapshot we will close the snapshot and return 0.
        windll.kernel32.CloseHandle(hProcessSnap)
        return 0
    #Next we will loop through all the processes in the snapshot.
    while True:
        #Next we will check if the name of the process matches the process name we are looking for.
        if pe32.szExeFile == processName:
            #If the name of the process matches the process name we are looking for we will close the snapshot and return the process identifier.
            windll.kernel32.CloseHandle(hProcessSnap)
            return pe32.th32ProcessID
        #Next we will check if we can get the next process in the snapshot.
        if not windll.kernel32.Process32Next(hProcessSnap, byref(pe32)):
            #If we cannot get the next process in the snapshot we will close the snapshot and return 0.
            windll.kernel32.CloseHandle(hProcessSnap)
            return 0

#InjectDll is a function that injects a dll into a process.
#There are two parameters that InjectDll takes.
#1. The process identifier of the process that we will be injecting the dll into.
#2. The path to the dll that we will be injecting.
def InjectDll(dwProcessId, dllPath):
    #First we will get a handle to the process that we will be injecting the dll into.
    hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, dwProcessId)
    #Next we will check if the handle to the process was created successfully.
    if hProcess == 0:
        #If the handle to the process was not created successfully we will return 0.
        return 0
    #Next we will get the address of the LoadLibraryA function.
    pLoadLibraryA = windll.kernel32.GetProcAddress(windll.kernel32.GetModuleHandleA("kernel32.dll"), "LoadLibraryA")
    #Next we will allocate memory in the process that we will be injecting the dll into.
    pRemoteBuf = VirtualAllocEx(hProcess, 0, len(dllPath), MEM_COMMIT, PAGE_EXECUTE_READWRITE)
    #Next we will check if the memory was allocated successfully.
    if pRemoteBuf == 0:
        #If the memory was not allocated successfully we will close the handle to the process and return 0.
        CloseHandle(hProcess)
        return 0
    #Next we will write the path to the dll into the memory that we allocated in the process that we will be injecting the dll into.
    n = c_ulong(0)
    if not WriteProcessMemory(hProcess, pRemoteBuf, dllPath, len(dllPath), byref(n)):
        #If the path to the dll was not written successfully we will free the memory that we allocated in the process that we will be injecting the dll into and close the handle to the process and return 0.
        VirtualFreeEx(hProcess, pRemoteBuf, 0, MEM_RELEASE)
        CloseHandle(hProcess)
        return 0
    #Next we will create a thread in the process that we will be injecting the dll into.
    hThread = CreateRemoteThread(hProcess, 0, 0, pLoadLibraryA, pRemoteBuf, 0, 0)
    #Next we will check if the thread was created successfully.
    if hThread == 0:
        #If the thread was not created successfully we will free the memory that we allocated in the process that we will be injecting the dll into and close the handle to the process and return 0.
        VirtualFreeEx(hProcess, pRemoteBuf, 0, MEM_RELEASE)
        CloseHandle(hProcess)
        return 0
    #Next we will wait for the thread to finish.
    WaitForSingleObject(hThread, INFINITE)
    #Next we will free the memory that we allocated in the process that we will be injecting the dll into.
    VirtualFreeEx(hProcess, pRemoteBuf, 0, MEM_RELEASE)
    #Next we will close the handle to the thread.
    CloseHandle(hThread)
    #Next we will close the handle to the process.
    CloseHandle(hProcess)
    #If the dll was injected successfully we will return 1.
    return 1

#Now we will call the functions that we defined.
#First we will get the process identifier of the process that we will be injecting the dll into.
dwProcessId = GetProcessId(processName)
#Next we will check if the process identifier was found successfully.
if dwProcessId == 0:
    #If the process identifier was not found successfully we will print a message to the screen.
    print "Could not find process."
else:
    #Next we will inject the dll into the process.
    if not InjectDll(dwProcessId, dllPath):
        #If the dll was not injected successfully we will print a message to the screen.
        print "Could not inject dll."
    else:
        #If the dll was injected successfully we will print a message to the screen.
        print "Dll injected successfully."

#Now we will wait for the user to press a key before we exit the program.
raw_input("Press any key to exit.")
