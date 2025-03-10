import os
import sys
import socket

# a. Get the machine type
print(f"Machine Type: {os.uname().machine}")

# b. Get the processor type
print(f"Processor Type: {os.uname().sysname}")

# c. Set the default timeout for a socket (in seconds) to 50 seconds
socket.setdefaulttimeout(50)

# d. Get the default socket timeout
print(f"Default Socket Timeout: {socket.getdefaulttimeout()} seconds")

# e. Get the operating system name
print(f"Operating System Name: {sys.platform}")

# f. Get the current process ID
print(f"Current Process ID: {os.getpid()}")

# g. Fork a new process (Unix-based systems only)
if hasattr(os, "fork"):
    pid = os.fork()
    if pid == 0:
        # Child process
        print(f"Child Process ID: {os.getpid()}")
        print("Child process exiting...")
        sys.exit()
    else:
        # Parent process
        print(f"Parent Process ID: {os.getpid()}")
        os.wait()  # Wait for the child process to finish


# File operations using os module
file_name = "fdpractice.txt"

# a. Open (or create) a file named fdpractice.txt
fd = os.open(file_name, os.O_RDWR | os.O_CREAT)

# b. Print the current process ID
print(f"Current Process ID: {os.getpid()}")

# c. Open the file for writing and reading
os.write(fd, b"Some string to write to the file")

# d. Fork a new process
if hasattr(os, "fork"):
    pid = os.fork()
    if pid == 0:
        # Child process
        print(f"Child Process ID: {os.getpid()}")
        os.lseek(fd, 0, os.SEEK_SET)  # Move the file pointer back to the beginning
        content = os.read(fd, 100)  # Read up to 100 bytes
        print(f"Child Read from file: {content.decode()}")
        os.close(fd)
        sys.exit()
    else:
        # Parent process
        print(f"Parent Process ID: {os.getpid()}")
        os.wait()  # Wait for the child process to finish
        os.close(fd)  # Close the file

print("Program execution completed.")
