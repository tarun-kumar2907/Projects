""" 
- ask what do you want log or view
- ask the name of the person from three choices(Tarun, Somu, Divya)
- ask what do you want to read/log diet or excercise
- choose which pair is it 
- do the operation i.e. actually read or write
log/view --> person --> diet/exer 
"""
def getdate():
    import datetime
    return datetime.datetime.now()

def Tarun(n):
    if(n==1):
     file1 = input("Which file do you want to open: Diet(1) or Excercise(2): ")
     file1=int(file1)
     if(file1==1):
        with open("tarun_diet.txt","a") as f:
            date = getdate()
            date=str(date)
            f.write("[")
            f.write(date)
            f.write("] ")
            f.write(input("Enter the food you ate: "))
            f.write("\n")
     elif(file1==2):
        with open("tarun_excercise.txt","a") as f:
            date = getdate()
            date=str(date)
            f.write("[")
            f.write(date)
            f.write("] ")
            f.write(input("Enter the Excercise you did: "))
            f.write("\n")    
    elif(n==2):
     file1 = input("Which file do you want to open: Diet(1) or Excercise(2): ")
     file1=int(file1)
     if(file1==1):
        with open("tarun_diet.txt","r") as f:
            print(f.read())
     elif(file1==2):
        with open("tarun_excercise.txt","r") as f:
            print(f.read()) 

def Somu(n):
    if(n==1):
     file1 = input("Which file do you want to open: Diet(1) or Excercise(2): ")
     file1=int(file1)
     if(file1==1):
        with open("somu_diet.txt","a") as f:
            date = getdate()
            date=str(date)
            f.write("[")
            f.write(date)
            f.write("] ")
            f.write(input("Enter the food you ate: "))
            f.write("\n")
     elif(file1==2):
        with open("somu_excercise.txt","a") as f:
            date = getdate()
            date=str(date)
            f.write("[")
            f.write(date)
            f.write("] ")
            f.write(input("Enter the Excercise you did: "))
            f.write("\n")    
    elif(n==2):
     file1 = input("Which file do you want to open: Diet(1) or Excercise(2): ")
     file1=int(file1)
     if(file1==1):
        with open("somu_diet.txt","r") as f:
            print(f.read())
     elif(file1==2):
        with open("somu_excercise.txt","r") as f:
            print(f.read()) 

def Divya(n):
    if(n==1):
     file1 = input("Which file do you want to open: Diet(1) or Excercise(2): ")
     file1=int(file1)
     if(file1==1):
        with open("divya_diet.txt","a") as f:
            date = getdate()
            date=str(date)
            f.write("[")
            f.write(date)
            f.write("] ")
            f.write(input("Enter the food you ate: "))
            f.write("\n")
     elif(file1==2):
        with open("divya_excercise.txt","a") as f:
            date = getdate()
            date=str(date)
            f.write("[")
            f.write(date)
            f.write("] ")
            f.write(input("Enter the Excercise you did: "))
            f.write("\n")    
    elif(n==2):
     file1 = input("Which file do you want to open: Diet(1) or Excercise(2): ")
     file1=int(file1)
     if(file1==1):
        with open("divya_diet.txt","r") as f:
            print(f.read())
     elif(file1==2):
        with open("divya_excercise.txt","r") as f:
            print(f.read()) 

def log():
    name = input("Choose the person: Tarun(1), Somu(2), Divya(3): ")
    name=int(name)
    if(name==1):
        Tarun(1)
    if(name==2):
        Somu(1)
    if(name==3):
        Divya(1)

def read():
    name = input("Choose the person: Tarun(1), Somu(2), Divya(3): ")
    name=int(name)
    if(name==1):
        Tarun(2)
    if(name==2):
        Somu(2)
    if(name==3):
        Divya(2)
    
log_or_read = input("What do you want to do Log(1) or Read(2): ")
log_or_read=int(log_or_read)
if(log_or_read==1):
    log()
if(log_or_read==2):
    read()
