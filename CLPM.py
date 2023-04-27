# Import Library
from os import system
import sys
from colorama import Fore
# ● Symbol
# Class Methods For CLPM(Command line Project Mannager)
class CLPM(object):
    def __init__(self) :
        pass
    def Create_Projects(self,Name,Description,Time): # For Create New Project
        pass
    def Delete_Projects(self,Name): # For Delete Project
        pass
    def Show_Projects():# Show Projects List
        pass 
    def Edit_Projects(self,Name): # For Edit Project
        pass
    def Show_log():
        pass
# Class Methods For Run CLPM on Command Line
class RUN(object):
    def __init__(self):
        RUN.Start() # Go To Def Start
    def Start(): # Start Application
        try:
           try:
                while True:
                    input()
            # Code Here
           except EOFError: # if Ctrl-Z Press Show This Massage
            pass
        except KeyboardInterrupt: # if Ctrl+c Press Show This Massage
            pass  
# Class Methods For Error Messages
class Error(object):
    Err0 = "Command Not Found Please try -help"
# Def For Help Messages
def Help():
    system("cls"or"clear")
    print("Usage: CLPM <Command> [options]")
    print("\tExample: CLPM -L (show Your Project List)")
    print("\tCommand\t\tDescription")
    print("\t●●●●●●●●●●●\t_____________________".replace("_","●"))
    #11,21 Column
    print("\t"+"{"+Fore.GREEN+"@"+Fore.RESET+"}"+" -Add     \tFor Created New Project Ex.(CLPM -Add Project_Name)")
    print("\t"+"{"+Fore.GREEN+"@"+Fore.RESET+"}"+" -d     \tFor Delete Project Ex.(CLPM -d Project_Name)")
    print("\t"+"{"+Fore.GREEN+"@"+Fore.RESET+"}"+" -l     \tFor Show List Projects Ex.(CLPM -l)")
    print("\t"+"{"+Fore.GREEN+"@"+Fore.RESET+"}"+" -e     \tFor Edit Project Ex.(CLPM -e Project_Name)")
    print("\t"+"{"+Fore.GREEN+"@"+Fore.RESET+"}"+" -log     \tFor Show Log Project Ex.(CLPM -log Project_Name)")
    print("\t"+"{"+Fore.GREEN+"@"+Fore.RESET+"}"+" -help     \tFor Show help")
# Start CLPM 
if __name__ == "__main__":
    CLPM = CLPM()
    Argv = sys.argv
    if(len(Argv) <= 1):
        RUN = RUN()
    else:
        if(Argv[1] == "-help"):
            Help()
        if(Argv[1] == "-log"):
            pass
        if(Argv[1] == "-e"):
            pass
        if(Argv[1] == "-l"):
            pass
        if(Argv[1] == "-d"):
            pass
        if(Argv[1] == "-Add"):
            pass
        else:
            Help()
            
        