#Python virtual environments are used to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has.
#pip install virtualenv
#To create a virtual environment we use the venv module and specify the directory we want to create the virtual environment in
#mkdir virtualEnvDir
#python3 -m venv virtualEnvDir
#To activate a virtual environment we use the source command
#source <name of virtual environment>/bin/activate

#The virtual environment is now active and we can install modules without affecting the global Python installation. By default the venv will not contain any globally installed modules

#If we run the which command we can see that the python command is now pointing to the python binary in the virtual environment
#which python

#To deactivate the virtual environment we use the deactivate command
#deactivate


