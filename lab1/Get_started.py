'''
Installing Python

Many computers already have Python installed.
To check on Windows:
1. Search for "Python" in the Start menu.
2. Open Command Prompt and type:
   python --version
'''
print("Check Python version with: python --version")

'''
Running Python Files

Python is an interpreted language. You write .py files in a text editor and run them in the Python interpreter.
To run a Python file, type this in the command line:
   python hi_world.py
'''
print("Run your Python file with: python hi_world.py")

'''
Checking Python Version

You can check the Python version in your code using the sys module.
'''
import sys
print("Your Python version is:", sys.version)

'''
Using Python in Command Line

You can run Python directly in the command line for quick tests.
1. Open Python by typing: py
2. Write code directly, for example:
   >>> print("Hello World")
   Hello World
3. Exit Python by typing: exit()
'''
print("Use 'py' in Command Prompt for interactive Python mode.")
