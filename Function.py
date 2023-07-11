import os
from math import*
fileName=""
NameSorted=""
#Dectect file location
def fileExists(filePath):
    exists=os.path.exists(filePath)
    return exists

#open file and print all
def OpenFile(fileName):
    with open(fileName,"r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip("\n"))

#clear page
def ClearPage():
    os.system("cls")
#--------------------------------------------------------------------------------
#Courses part
#Read course code and descrption from courses.txt file
def readCourseFile():
    course=[]
    with open ("courses.txt","r") as f:
        for line in f:
            CourseCode=line.strip("\n").split("|")[0]
            CourseName=line.strip("\n").split("|")[1]
            course.append([CourseCode,CourseName])
            CourseSorted=sorted(course)
        for count in range(15):
            num = count + 1
            print(("\t%2d \t%s \t%s"%(num,CourseSorted[count][0],CourseSorted[count][1])))

def returnValue():
    course=[]
    with open ("courses.txt","r") as f:
        for line in f:
            CourseCode=line.strip("\n").split("|")[0]
            CourseName=line.strip("\n").split("|")[1]
            course.append([CourseCode,CourseName])
            CourseSorted=sorted(course)
        return CourseSorted
        
def readPage(pageNum):
    course=[]
    with open ("courses.txt","r") as f:
        for line in f:
            CourseCode=line.strip("\n").split("|")[0]
            CourseName=line.strip("\n").split("|")[1]
            course.append([CourseCode,CourseName])
            CourseSorted=sorted(course)
        CourseList=CourseSorted
        totalpage=ceil(len(CourseList)/15)
        total=len(CourseList)
        least=len(CourseList)%15
        count=0
        if pageNum == 1 and least != 0:
            count=0
            total=15
            
        elif pageNum<totalpage and least != 0:
            total=15*pageNum
            count=total-15
            
        elif pageNum == totalpage and least != 0:
            count=total-least
            
        elif pageNum == totalpage and least ==0:
            count=total-15
            
        else:
            count=0
            total=least
            
        for i in range(count,total):
            num = i + 1
            print("\t%2d \t%s \t%s" %(num,CourseSorted[i][0],CourseSorted[i][1]))

def addCourse():
    loop=True
    while loop:
        with open ("courses.txt","a+") as f:
            CourseCode=input("\tCourse(Code Format-FHSC1024): ")
            CourseName=input("\tCourse Name: ")
            if CourseCode=="" or CourseName=="":
                print("")
                print("\tInvalid input, Try again")
                input("\tPress ENTER to continue")
            else:
                wStr=CourseCode+" | "+CourseName+"\n"
                f.write(wStr)
                print("\tSuccess to add")
                input("\tPress ENTER to continue")
                f.truncate()
                loop=False
                
            

def delCourse(CourseCode):
    with open("courses.txt","r+") as f:
        if CourseCode=="":
            print("\tInvalid input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
        else:
            f_lines=f.readlines()
            f.seek(0)
            for line in f_lines:
                if CourseCode not in line:
                    f.write(line)
            print("\tSuccess to delete")
            input("\tPress ENTER to continue")
            f.truncate()

def updateCourse(CourseCode,CourseName):
    list1=[str(CourseCode),str(CourseName)]
    with open("courses.txt","r+") as f:
        if CourseName=="" or CourseCode=="":
            print("\tInvalid input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
        else:
            f_lines=f.readlines()
            f.seek(0)
            for line in f_lines:
                if CourseCode not in line:
                    f.write(line)
                else:
                    wStr=" | ".join(list1)+"\n"
                    f.write(wStr)
            print("\tSuccess to update")
            input("\tPress ENTER to continue")
            f.truncate()
    
#---------------------------------------------------------------------------------
#Student Record
#Read Student Record File
def readStudFile():
    studList=[]
    with open ("StudBio.txt","r") as f:
        for line in f:
            studId=line.strip("\n").split("|")[0]
            studName=line.strip("\n").split("|")[1]
            studIC=line.strip("\n").split("|")[2]
            studCourse=line.strip("\n").split("|")[3:len(line)]
            course="|".join(studCourse)
            studList.append([studName,studId,studIC,str(course)])
            studRecSorted=sorted(studList)
            
        for count in range(len(studRecSorted)):
            num = count + 1
            print(("\t%02d \t%2s \t%s \t%s \t%s"%(num,studRecSorted[count][1],
                                                   studRecSorted[count][0],
                                                   studRecSorted[count][2],
                                                   studRecSorted[count][3])))

#Add Student Record
def addStud():
    CList=[]
    with open ("StudBio.txt","a+") as f:
        studID  =input("\tStudent ID   : ") 
        studName=input("\tStudent Name : ")
        studIC  =input("\tStudent IC   : ")
        loop=True
        while loop:
            total=int(input("\tTotal Course : "))
            for i in range(total):
                course=input("\tCourse %d(Code Format-FHSC1024): " %(i+1))
                if course not in CList:
                    CList.append(course)
                else:
                    print("\tThe Course has be recorded, Try again")
                    input("\tPress ENTER to continue")
                    loop=False
            loop=False
        false=0
        for i in range(total):
            if course[i] == "":
                false+=1
                
        if studID == "" or studName == "" or studIC == "" or false>0 :
            print("")
            print("\tInvalid input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
        else:
            course="|".join(CList)
            wStr=studID+"|"+studName+"|"+studIC+"|"+course+"\n"
            f.write(wStr)
            print("\tSuccess to add")
            input("\tPress ENTER to continue")

#Update Student Record
def updateStud(studID,studName,studIC,mode,studCourse):
    list1=[str(studID),str(studName),str(studIC),str(studCourse)]
    with open("StudBio.txt","r+") as f:
        if studID == "" or studName == "" or studIC == "" or studCourse == "":
            print("\tInvalid input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
        else:
            f_lines=f.readlines()
            f.seek(0)
            for line in f_lines:
                if studID not in line:
                    f.write(line)
                elif studID in line and mode == "A":
                    course=line.strip("\n").split("|")[3:]
                    list1 += course
                    wStr="|".join(list1)+"\n"
                    f.write(wStr)
                elif studID in line and mode == "D":
                    whole=line.strip("\n").split("|")
                    idx=whole.index(studCourse)
                    whole.pop(idx)
                    wStr="|".join(whole)+"\n"
                    f.write(wStr)
                    
            print("\tSuccess to update")
            input("\tPress ENTER to continue")
            f.truncate()
            
#Delete Student Record
def delStud(studID):
    with open("StudBio.txt","r+") as f:
        if studID == "":
            print("\tInvalid input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
        else:
            f_lines=f.readlines()
            f.seek(0)
            for line in f_lines:
                if studID not in line:
                    f.write(line)
            print("\tSuccess to delete :",studID)
            input("\tPress ENTER to continue")
            f.truncate()
#---------------------------------------------------------------------------------
#CRUD
def readCRUD():
    global fileName
    content=[]
    quiz=["\tCourse Code                               (Q)uit to stop: ",
          "\tSession Code (L#/P#/T#)                   (Q)uit to stop: ",
          "\tWeek Number(01-14)                        (Q)uit to stop: ",
          "\tSession date (18-01-2021 to 23-04-2021)   (Q)uit to stop: ",
          "\tSession Start Time  (08:00:00 AM to 05:30:00 PM) (Q)uit to stop: ",
          "\tSession End   TIme  (08:00:00 AM to 05:30:00 PM) (Q)uit to stop: "]
    i=0
    loop=True
    while loop:
        #Title
        print("\t"+"-"*70)
        print("\t\t\tUTAR CFS Student Attendance File maintenance")
        print("\t"+"-"*70)
        loop2=True
        while loop2:
            if "Q" not in content and i<6:
                content.append(input(quiz[i]))
                i+=1
                
            elif "Q" in content:
                option=input("\t(Q)uit and Exit (R)eset: ")
                loop=False
                loop2=False
                return option
            
            else:
                
                fileName=content[0]+content[1]+"wk"+content[2]+".txt"
                #Dectect file exist
                if not fileExists(fileName):
                    option=input("\t(Q)uit and Exit (R)eset (G)enerate new file: ")
                    #Generate file
                    loop3=True
                    while loop3:
                        if option.upper() == "G":
                            with open("studBio.txt","r") as fileobj:
                                studList=[]
                                f_lines=fileobj.readlines()
                                for line in f_lines:
                                    if content[0] in line:
                                        studID=line.strip("\n").split("|")[0]
                                        studName=line.strip("\n").split("|")[1]
                                        studList.append([studID,studName])
                                        NameSorted=sorted(studList)
                            with open (fileName,"w+") as f:
                                for x in NameSorted:
                                    ID=x.strip("\n").split("|")[0]
                                    name=x.strip("\n").split("|")[1]
                                    detail=[ID,name,"Joined ",content[3],content[4],content[5]]
                                    wStr="|".join(detail)+"\n"
                                    f.write(wStr)
                                
                            print("\tSuccess to generate ",fileName," file.")
                            input("\tPress ENTER to continue")
                            option="R"
                            loop3=False
                            loop2=False
                            loop=False
                            return option
                        else:
                            loop3=False
                            loop2=False
                            loop=False
                            return option
                    
                else:
                    loop3=True
                    while loop3:
                        print("\tFile Exists, ",end="")
                        option=input("(Q)uit and Exit (R)eset (M)aintain existing (G)enerate new file:")
                        ClearPage()
                        if option.upper() == "G":
                            loop3=True
                        elif option.upper() == "M":
                            loop3=False
                            maintain(content)
                            return maintain(content)
                        else:
                            loop3=False
                            loop2=False
                            loop=False
                            return option
            
#CRUD Maintaining file exist
#search course name from courses.txt file
def maintain(content):
    loop=True
    while loop:
        with open ("courses.txt","r") as f:
            f_lines=f.readlines()
            f.seek(0)
            for line in f_lines:
                if content[0] in line:
                    CourseName=line.strip("\n").split("|")[1]
                    print("\t"+"-"*80)
                    print("\t\t\t%s(%s)"%(content[0],CourseName))
                    print("\t"+"-"*80)
                    print("\t\t\tUTAR CFS Course Student Attendance Maintainence")
                    print("\t"+"-"*80)

        #print all data in 
        list1=[]
        with open (fileName,"r") as f:
            f_lines=f.readlines()
            f.seek(0)
            for line in f_lines:
                alldetail=line.strip("\n").split("|")
                list1.append(alldetail)
            for i in range(0,len(list1)):
                num2 = i +1
                print(("\t%02d \t%s \t%-7s \t%s \t%s \t%s "%(num2,list1[i][1],list1[i][2],
                                                        list1[i][3],list1[i][4],list1[i][5])))

        #Input
        print("\t"+"-"*80)
        print("\t(A)dd (D)elete (E)dit (Q)uit: ")
        print("\t"+"-"*80)
        option=input("\tOption >> ")
        if option.upper() == "A":
            with open (fileName,"a+") as f:
                studID=input("\tStudent ID   :")
                studName=input("\tStudent Name: ")
                f_lines=f.readlines()
                f.seek(0)
                if studName=="" :
                    print("")
                    print("\tInvalid input, Try again")
                    input("\tPress ENTER to continue")
                    ClearPage()
                else:
                    for line in f_lines:
                        if studName not in line:
                            f.write(line)
                        else:
                            print("\t",studName," are recorded in ",fileName,".")
                            input("\tPress ENTER to continue")
                            ClearPage()
                    wStr=studID + "|" + studName + "|Joined|"+ content[3]+"|"+content[4]+"|"+content[5]+"\n"
                    f.write(wStr)
                    print("\tSuccess to add ",studName," into ",fileName,".")
                    input("\tPress ENTER to continue")
                    ClearPage()
                    
        elif option.upper() == "D":
            with open(fileName,"r+") as f:
                studName=input("\tStudent Name: ")
                if studName == "":
                    print("\tInvalid input, Try again")
                    input("\tPress ENTER to continue")
                    ClearPage()
                else:
                    f_lines=f.readlines()
                    f.seek(0)
                    for line in f_lines:
                        if studName not in line:
                            f.write(line)
                    print("\tSuccess to DELETE")
                    input("\tPress ENTER to continue")
                    f.truncate()
                    
        elif option.upper() == "E":
            i=0
            content2=[]
            quiz2=["\tStudent ID                               (Q)uit to stop: ",
                   "\tStudent Name                             (Q)uit to stop: ",
                   "\tAttendance status(Joined/Absent/Medical) (Q)uit to stop: ",
                   "\tLogin Time(08:00:00 AM to 05:30:00 PM)   (Q)uit to stop: ",
                   "\tLogout Time(08:00:00 AM to 05:30:00 PM)  (Q)uit to stop: "]
            loop2=True
            while loop2:     
                if "Q" not in content2 and i<5:
                    content2.append(input(quiz2[i]))
                    i+=1
                        
                    if i == 3:
                        if content2[2]=="Medical" or content2[2]=="Absent" :
                            list1=[content2[0],content2[1],content2[2],content[3],"---NONE---","---NONE---"]
                            wStr="|".join(list1)+"\n"
                            with open (fileName,"r+") as f:
                                f_lines=f.readlines()
                                f.seek(0)
                                for line in f_lines:
                                    if content2[0] not in line:
                                        f.write(line)
                                    else:
                                        f.write(wStr)
                                        loop2=False
                                f.truncate()
                            ClearPage()
                                
                        else:
                            content2.append(input(quiz2[i]))
                            i+=1
                        
                elif i == 5:
                    with open (fileName,"r+") as f:
                        content2.insert(3,content[3])
                        f_lines=f.readlines()
                        f.seek(0)
                        for line in f_lines:
                            if content2[0] not in line:
                                f.write(line)
                            else:
                                wStr="|".join(content2)+"\n"
                                f.write(wStr)
                        f.truncate()
                        
                    print("\tSuccess to edit")
                    input("\tPress ENTER to continue")
                    loop2=False
                    ClearPage()
                else:
                    option=input("\t(Q)uit and Exit (R)eset: ")
                    loop=False
                    return option
                
        elif option.upper() == "Q":
            loop=False
            return option

        else:
            print("")
            print("\tError input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
    
#--------------------------------------------------------------------------------







    
