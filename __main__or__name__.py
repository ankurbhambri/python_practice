''' 
Python files are called modules and they are identified by the .py file extension. 

A module can define functions, classes, and variables.

So when the interpreter runs a module, the __name__ variable will be 
set as  __main__ if the module that is being run is the main program.

But if the code is importing the module from another module, 
then the __name__  variable will be set to that module’s name. 

The variable __name__ for the file/module that is run will be 
always __main__. But the __name__ variable for all other modules 
that are being imported will be set to their module's name. '''


print("File one __name__ is set to: {}" .format(__name__))
