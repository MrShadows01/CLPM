# Import Library
from os import system
import sys
from colorama import Fore
import time 
def GetTime():
    x = time.localtime()
    year = x.tm_year
    Month = x.tm_mon
    Day = x.tm_mday
    Hour = x.tm_hour
    Mints = x.tm_min
    Secound = x.tm_sec
    Time = "{}/{}/{} - {}:{}:{}".format(year, Month,Day,Hour,Mints,Secound)
    return Time
# ● Symbol
# Class Methods For CLPM(Command line Project Mannager)
class CLPM(object):
    def __init__(self) :
        pass
    def Create_Projects(self,Name,Description,Time): # For Create New Project
        print("Create New Project This Information \nProject Name {}\nDescription {}\nTime {}\n".format(Name,Description,Time))
        ReadFileLog = open("LogFile.txt","r")
        LOgFiles = open("LogFile.txt","+a")
        Pro_name = ReadFileLog.read()
        if(Name in Pro_name):
            print("Project Exists")
            LOgFiles.write("\nCLPM Closed in {}\t (because Project Existed) ".format(GetTime()))
            
        else:
            LOgFiles.write("\nProject {} Created in {} \nDescription :{}".format(Name,Time,Description))
            LOgFiles.close()
    def Delete_Projects(self,Name): # For Delete Project
        pass
    def Show_Projects():# Show Projects List
        pass 
    def Edit_Projects(self,Name): # For Edit Project
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
    def Err0(text):
        Err0 = Fore.RED+"Error 0x01 Commnad Not Found ({}) ".format(text)+Fore.RESET
        return Err0
def Show_log():
    ShowLog = open("LogFile.txt","r")
    Log = ShowLog.read()
    print(Fore.GREEN+f"{Log}"+Fore.RESET)
# Def For Help Messages
def Help():
    
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
    LogFile = open("LogFile.txt","+a")
    Time = GetTime()
    LogFile.write("\nOpen CLPM {}".format(Time))
    LogFile.close()
    CLPMs = CLPM()
    Argv = sys.argv
    Argv1 = Argv[1]
    if(len(Argv) <= 1):
        RUN = RUN()
    else:
        if(Argv1.lower() == "-help"):
            system("cls"or"clear")
            Help()
        elif(Argv1.lower() == "-log"):
            Show_log()
        elif(Argv1.lower() == "-e"):
            print("-e")
        elif(Argv1 == "-l"):
            print("-l")
        elif(Argv1.lower() == "-d"):
            print("-d")
        elif(Argv1.lower() == "-add"):
            ProjectName = Argv[2]
            PrjectDescription = Argv[3].replace("/"," ")
            Time = GetTime()
            CLPMs.Create_Projects(ProjectName, PrjectDescription,Time)           
        else:
            system("cls"or"clear")
            print(Error.Err0(Argv1))
            Help()
            
        
