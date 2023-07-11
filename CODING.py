from Function import*
from math import*

#Student Attendance
def studAttendance():
    
    loop=True
    while loop:
        
        weekLst=["01","02","03","04","05","06","07","08","09","10","11","12"]
        NameList={}
        content=[]
        state="0"
        quiz=["\tCourse Code [(Q)uit]: ","\tSession Code (L#/P#/T#) [(Q)uit]: "
              ,"\tWeek number (01-12) [(Q)uit] : "]
        
        OpenFile("StudentAttendance.txt")
        option=input("\tOption [(Q)uit] >> ")
        with open ("studBio.txt","r") as f:
            for line in f:
                studID=line.strip("\n").split("|")[0]
                studName=line.strip("\n").split("|")[1]
                NameList[studID]=studName
        
        
        
        if option == "1":
            ClearPage()
            loop2=True
            while loop2:
                print("\t"+"-"*70)
                print("\t\t\tStudent View-Weekly Attendance")
                print("\t"+"-"*70)
                print("")
                print("")
                ID=input("\tStudent ID [(Q)uit]: ")
                print("")
                print("")
                print("\t"+"-"*70)
                while ID not in NameList and ID.upper()!="Q":
                    ClearPage()
                    print("\t"+"-"*70)
                    print("\t\t\tStudent View-Weekly Attendance")
                    print("\t"+"-"*70)
                    print("")
                    print("")
                    print("\tInvalid ID. Please try again")
                    ID=input("\tStudent ID [(Q)uit]: ")
                    print("")
                    print("")
                    print("\t"+"-"*70)
                    ClearPage()

                if ID.upper()=="Q":
                    loop2=False
                    ClearPage()
                    
                else:
                    i=0
                    loop3=True
                    while loop3:
                        if "Q" not in content and i<3:
                            content.append(input(quiz[i]))
                            i+=1

                        elif "Q" in content:
                            print("\t"+"-"*70)
                            option=input("\t(Q)uit and Exit (R)eset: ")
                            ClearPage()
                            loop3=False
            
                        elif i==3:
                            studCourse=content[0]
                            studClass=content[1]
                            week=content[2]
                            fileName=studCourse+studClass+"wk"+week+".txt"
                            if fileExists(fileName):
                                with open (fileName,"r") as f:
                                    f_lines=f.readlines()
                                    f.seek(0)
                                    for line in f_lines:
                                        if ID in line:
                                            state=line.strip("\n").split("|")[2]
                                                   
                                if state != "Absent" or state != "Medical":
                                     
                                    in_out_list=[]
                                    
                                    ClearPage()
                                    with open (fileName,"r") as f:
                                        
                                        f_lines=f.readlines()
                                        f.seek(0)
                                        for line in f_lines:
                                            if ID in line:
                                                timeIn=line.strip("\n").split("|")[-2]
                                                timeOut=line.strip("\n").split("|")[-1]
                                                in_out_list=[timeIn,timeOut]
                                                    
                                    time="  --  ".join(in_out_list)
                                    print("\t"+"-"*70)
                                    print("\t\t\tStudent View-Week",week,"Attendance")
                                    print("\t\t\t\t" + NameList[ID])
                                    print("\t"+"-"*70)

                                    print("\tJoinned Time | Leave Time\n")
                                    print("\t" + time + "\n")
                                    print("")

                                    in_hour=int(in_out_list[0][0:2])
                                    in_minute=int(in_out_list[0][3:5])
                                    out_hour=int(in_out_list[1][0:2])
                                    out_minute=int(in_out_list[1][3:5])
                                    total_time=(out_hour*60+out_minute)-(in_hour*60+in_minute)
                                    print("\tTotal time in class is %0d minutes\n" %total_time)
                                        
                                    if total_time > 96 :
                                        print("")
                                        print("\tYou attended the class\n")
                                        print("\t"+"-"*70)
                                    else:
                                        print("")
                                        print("\tYou are absent the class\n")
                                        print("\t"+"-"*70)
                                    key=input("\t(C)ontinue (Q)uit >> ")
                                    if key.upper()=="C":
                                        i=0
                                        content=[]
                                        ClearPage()
                                        print("\t"+"-"*70)
                                        print("\t\t\tStudent View-Weekly Attendance")
                                        print("\t\t\t\tID : "+ID)
                                        print("\t"+"-"*70)
                                        
                                    elif key.upper()=="Q":
                                        loop2=False
                                        loop3=False
                                        ClearPage()
                                                
                                    
                                else:
                                    print("\t"+"-"*70)
                                    print("\t\t\tStudent View-Weekly Attendance")
                                    print("\t\t\t" + NameList[ID])
                                    print("\t"+"-"*70)

                                    print("\tJoinned Time | Leave Time\n")
                                    print("\t[You are absent for today]\n")
                                    print("")

                                    print("\tTotal time in class is 0 minutes")
                                    key=input("(C)ontinue (Q)uit >> ")
                                    if key.upper()=="C":
                                        i=0
                                        content=[]
                                        ClearPage()
                                        print("\t"+"-"*70)
                                        print("\t\t\tStudent View-Weekly Attendance")
                                        print("\t\t\t\tID : "+ID)
                                        print("\t"+"-"*70)
                                            
                                    elif key.upper()=="Q":
                                        loop2=False
                                        loop3=False
                                        ClearPage()
                                        
                                    else:
                                        print("\tInvalid input. Please try again")
                                        input("\tPress ENTER to continue")
                                        ClearPage()
                                        loop2=False
                                        loop3=False
                                
                            else:
                                print("\tAttendance doesn't exist. Please try again")
                                input("\tPress ENTER to continue")
                                ClearPage()
                                i=0
                                content=[]
     
                        else:
                            print("\tInvalid input. Please try again")
                            input("\tPress ENTER to continue")
                            ClearPage()
                            print("\t"+"-"*70)
                            print("\t\t\tStudent View-Weekly Attendance")
                            print("\t\t\t\tID : "+ID)
                            print("\t"+"-"*70)
                            i=0
                            content=[]
                
            
        elif option == "2":
            ClearPage()
            loop2=True
            while loop2:
                print("\t"+"-"*70)
                print("\t\t\tStudent View-Whole Semester Attendance")
                print("\t"+"-"*70)
                print("")
                print("")
                ID=input("\tStudent ID [(Q)uit]: ")
                print("")
                print("")
                print("\t"+"-"*70)
                while ID not in NameList and ID.upper()!="Q":
                    ClearPage()
                    print("\t"+"-"*70)
                    print("\t\t\tStudent View-Weekly Attendance")
                    print("\t"+"-"*70)
                    print("")
                    print("")
                    print("\tInvalid ID. Please try again")
                    ID=input("\tStudent ID [(Q)uit]: ")
                    print("")
                    print("")
                    print("\t"+"-"*70)
                    ClearPage()

                if ID.upper()=="Q":
                    loop2=False
                    ClearPage()
                    
                else:
                    i=0
                    loop3=True
                    while loop3:
                        if "Q" not in content and i<2:
                            ClearPage()
                            print("\t"+"-"*70)
                            print("\t\t\tStudent View-Weekly Attendance")
                            print("\t"+"-"*70)
                            print("")
                            print("")
                            content.append(input(quiz[i]))
                            i+=1

                        elif "Q" in content:
                            print("\t"+"-"*70)
                            option=input("\t(Q)uit and Exit (R)eset: ")
                            loop3=False
            
                        else:
                            studCourse=content[0]
                            studClass=content[1]
                            ClearPage()
                            print("\t"+"-"*70)
                            print("\t\t\tStudent View-Whole Semester Attendance")
                            print("\t\t\t" + NameList[ID])
                            print("\t"+"-"*70)
                            fileName=studCourse+studClass+"wk"+weekLst[0]+".txt"
                            
                            if fileExists(fileName):
                                for i in range(12):
                                    fileName=studCourse+studClass+"wk"+weekLst[i]+".txt"
                                    with open (fileName,"r") as f:
                                        f_lines=f.readlines()
                                        f.seek(0)
                                        for line in f_lines:
                                            if ID in line:
                                                state=line.strip("\n").split("|")[2]
                                                
                                    if state != "Absent" or state != "Medical":
                                        in_out_list=[]
                                        with open (fileName,"r") as f:
                                            f_lines=f.readlines()
                                            f.seek(0)
                                            for line in f_lines:
                                                if ID in line:
                                                    timeIn=line.strip("\n").split("|")[-2]
                                                    timeOut=line.strip("\n").split("|")[-1]
                                                    in_out_list=[timeIn,timeOut]

                                        in_hour=int(in_out_list[0][0:2])
                                        in_minute=int(in_out_list[0][3:5])
                                        out_hour=int(in_out_list[1][0:2])
                                        out_minute=int(in_out_list[1][3:5])
                                        total_time=(out_hour*60+out_minute)-(in_hour*60+in_minute)
                                            
                                        if total_time > 96 :
                                            state="Attended"
                                        else:
                                            state="Absent"

                                        print("\tAttendence week %2d | %s |" %(i+1,state))
                                        print("")
                                                    
                                        
                                    else:
                                        print("\tAttendence week %2d | %s |" %(i+1,state))
                                        print("")
                                        
                                print("\t"+"-"*70)      
                                key=input("\t(C)ontinue (Q)uit >> ")
                                if key.upper()=="C":
                                    i=0
                                    content=[]
                                    ClearPage()
                                    print("\t"+"-"*70)
                                    print("\t\t\tStudent View-Weekly Attendance")
                                    print("\t\t\t\tID : "+ID)
                                    print("\t"+"-"*70)
                                        
                                elif key.upper()=="Q":
                                    loop2=False
                                    loop3=False
                                    ClearPage()
                                    
                                else:
                                    print("\tInvalid input. Please try again")
                                    input("\tPress ENTER to continue")
                                    ClearPage()
                                    loop2=False
                                    loop3=False
                            else:
                                print("\tAttendance doesn't exist. Please try again")
                                input("\tPress ENTER to continue")
                                ClearPage()
                                i=0
                                content=[]
                                print("\t"+"-"*70)
                                print("\t\t\tStudent View-Weekly Attendance")
                                print("\t\t\t\tID : "+ID)
                                print("\t"+"-"*70)
                                
                                
                                
        elif option.upper()=="Q":
            loop=False
            loop2=False
            ClearPage()
                
        else:
            print("")
            print("\tError input, Try again1")
            input("\tPress ENTER to continue")
            loop2=False

#Course Record Maintenance
def courseRec():
    CourseList=returnValue()
    option="true"
    loop=True
    time=0
    page=1
    while loop:
        #Title
        print("\t"+"-"*70)
        print("\t\t\tUTAR CFS Course Records Maintenance")
        print("\t"+"-"*70)

        #Read file and print
        readPage(page)

        #Input
        print("\t"+"-"*70)
        print("\t(A)dd (D)elete (E)dit (N)ext(P)revPage (Q)uit: ")
        print("\t"+"-"*70)
        option=input("\tOption >>")
        
            
        if option.upper() == "A":
            addCourse()
            ClearPage()
            
            
        elif option.upper() == "D":
            CourseCode=input("\tCourse Code: ")
            delCourse(CourseCode)
            ClearPage()
            
            
        elif option.upper() == "E":
            CourseCode=input("\tCourse Code: ")
            CourseName=input("\tCourse Name: ")
            updateCourse(CourseCode,CourseName)
            
        
        elif option.upper() == "N":
            
            totalpage=ceil(len(CourseList)/15)
            if page == totalpage:
                page=totalpage
                print("\tThis is last page, Try again")
                input("\tPress ENTER to continue")
                ClearPage()
                    
            elif page<totalpage:
                page+=1
                ClearPage()

        elif option.upper() == "P":
            
            totalpage=ceil(len(CourseList)/15)
            if page == 1:
                page=1
                print("\tThis is first page, Try again")
                input("\tPress ENTER to continue")
                ClearPage()
                    
            elif page > 1:
                page-=1
                ClearPage()

        elif option.upper() == "Q":
            print("\tQuitting...")
            print(page)
            loop=False
            ClearPage()
        else:
            print("")
            print("\tError input, Try again")
            input("\tPress ENTER to continue")
            
            
#Student Record Maintenance
def studRec():
    loop=True
    while loop:
        #Title
        print("\t"+"-"*70)
        print("\t\t\tUTAR CFS Student Records Maintenance")
        print("\t"+"-"*70)

        #Read file and print
        readStudFile()

        #Input
        print("\t"+"-"*70)
        print("\t(A)dd (D)elete (E)dit (Q)uit: ")
        print("\t"+"-"*70)
        option=input("\tOption >>")

        if option.upper() == "A":
            addStud()
            option="false"
            ClearPage()

        elif option.upper() == "D":
            studID=input("\tStudent ID   : ")
            delStud(studID)

        elif option.upper() == "E":
            studID=input("\tStudent ID   : ")
            studName=input("\tStudent Name : ")
            studIC  =input("\tStudent IC    : ")
            mode=input("\tADD @ DELETE course(A/D): ").upper()
            studCourse=input("\tCourse(Code Format-FHSC1024): ")
            updateStud(studID,studName,studIC,mode,studCourse)

        elif option.upper() == "Q":
            print("\tQuitting...")
            loop=False
            ClearPage()
            
        else:
            print("")
            print("\tError input, Try again")
            input("\tPress ENTER to continue")
            
#CRUD
def CRUD():
    loop=True
    while loop:
        
        #Read file and print
        option=readCRUD()

        if option.upper() == "R":
            ClearPage()
            
        elif option.upper() == "Q":
            print("\tQuitting...")
            loop=False
            ClearPage()

        else:
            print("")
            print("\tError input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()
            
#Bulk loading
def bulk():
    content=[]
    quiz=["\tCourse Code [(Q)uit to stop]: ",
          "\tSession Code (L#/P#/T#) [(Q)uit to stop]: "]
    weekLst=["01","02","03","04","05","06","07","08","09","10","11","12"]
    loop=True
    while loop:
        
        i=0
        loop2=True
        print("\t"+"-"*70)
        print("\t\t\tBulk Attendance Loading")
        print("\t"+"-"*70)
        while loop2:
            if "Q" not in content and i<2:
                content.append(input(quiz[i]))
                i+=1

            elif "Q" in content:
                print("\t"+"-"*70)
                option=input("\t(Q)uit and Exit (R)eset: ")
                loop2=False

            else:
                ClearPage()
                studCourse=content[0]
                studClass=content[1]
                stateList=["Absent","Medical"]
                barlist=[]
                finalbarlist=[]
                
                full_attend_list=[]
                final_full_list=[]
                
                studlist=[]
                latelist=[]
                 
                nolatelist=[]
                medicalList=[]
                ClearPage()
                
                for week in range(12):
                    fileName=studCourse+studClass+"wk"+weekLst[week]+".txt"
                    if fileExists(fileName):
                        with open (fileName,"r") as f:
                            f_lines=f.readlines()
                            f.seek(0)
                            for line in f_lines:
                                
                                studID=line.strip("\n").split("|")[0]
                                studName=line.strip("\n").split("|")[1]
                                state=line.strip("\n").split("|")[2]
                                timeIn=line.strip("\n").split("|")[-2]
                                timeOut=line.strip("\n").split("|")[-1]
                                studDetail=[studID,studName]
                                
                                if state not in stateList:

                                    in_hour=int(timeIn[0:2])
                                    in_minute=int(timeIn[3:5])
                                    out_hour=int(timeOut[0:2])
                                    out_minute=int(timeOut[3:5])
                                    
                                    total_time=(out_hour*60+out_minute)-(in_hour*60+in_minute)
                                       
                                    if total_time < 96 :
                                        latelist.append(studDetail)
                                        
                                    else:
                                        nolatelist.append(studDetail)
                        
                                elif "Absent" in state:
                                    latelist.append(studDetail)

                                elif "Medical" in state:
                                    medicalList.append(studDetail)

                
                    else:
                        print("\tAttendance file is missing. Please try again")
                        input("\tPress ENTER to continue")
                        ClearPage()
                        i=0
                        content=[]
                        print("\t"+"-"*70)
                        print("\t\t\tBulk Attendance Loading")
                        print("\t"+"-"*70)
                        
                loop2=False
        ClearPage()                      
        OpenFile("Bulk.txt")            
        option=input("\tOption [(Q)uit] >> ")
        
        if option == "1":
            
            for lateID in latelist:
                if latelist.count(lateID) >= 3:
                    barlist.append(lateID)
                    
                    
                    
            for element in barlist:
                if element not in finalbarlist:
                    finalbarlist.append(element)
                    finalbarlist=sorted(finalbarlist)
                    
            fileName=content[0] + content[1]+"(BarList).txt"       
            with open(fileName,"w") as f:
                f.write ('\t'+'-'*70+'\n\t\t\t  Barlist-'+content[0]+'\n\t'+'-'*70+'\n')
                f.write('\t\t\tStudent ID\tName\n\t\t\t----------\t----\n')
                for element in finalbarlist:
                    f.write("\t\t\t%s\t\t%s\n" %(element[0],element[1]))
                f.write('\t'+'-'*70+'\n')
            print("\t"+"-"*70)
            print("\tLoding in progress")
            print("\tBarlist Report generated...")
            input("\tPress ENTER to continue")
            ClearPage()
            
            
        elif option == "2":
            
            for fullattend in nolatelist:
                if nolatelist.count(fullattend) == 12:
                    full_attend_list.append(fullattend)
            
            for element in full_attend_list:
                if element not in final_full_list:
                    final_full_list.append(element)
                    final_full_list=sorted(final_full_list)
            fileName=content[0] + content[1]+"(FullAttendance).txt"    
            with open(fileName,"w") as f:
                f.write ('\t'+'-'*70+'\n\t\t\tFull Attendence Report-'+content[0]+'\n\t'+'-'*70+'\n')
                f.write('\t\t\tStudent ID\tName\n\t\t\t----------\t----\n')
                for element in final_full_list:
                    f.write("\t\t\t%s\t\t%s\n" %(element[0],element[1]))
                f.write('\t'+'-'*70+'\n')
            print("\t"+"-"*70)
            print("\tLoding in progress")
            print("\tFull Attendence Report generated...")
            input("\tPress ENTER to continue")
            ClearPage()
            
            
        elif option.upper() == "Q":
            loop=False
            ClearPage()
        else:
            print("")
            print("\tError input, Try again")
            input("\tPress ENTER to continue")
            ClearPage()

#Reporting
def report():
    content=[]
    quiz=["\tCourse Code [(Q)uit]: ",
          "\tSession Code (L#/P#/T#) [(Q)uit]: ",]
    loop=True
    while loop:
        print("\t"+"-"*70)
        print("\t\t\t\tReporting")
        print("\t"+"-"*70)
        i=0
        loop2=True
        while loop2:
            if "Q" not in content and i<2:
                content.append(input(quiz[i]))
                i+=1

            elif "Q" in content:
                print("\t"+"-"*70)
                option=input("\t(Q)uit and Exit (R)eset: ")
                loop2=False
                loop=False

            else:
                ClearPage()
                OpenFile("Reporting.txt")
                option=input("\tOption [(Q)uit] >> ")
                ClearPage()
                if option == "1":
                    fileName=content[0] + content[1]+"(BarList).txt"
                    with open (fileName,"r") as f:
                        for x in f:
                            print(x)
                    key=input("\t(C)ontinue / (Q)uit >> ")
                    if key.upper()=="C":
                        i=0
                        content=[]
                        ClearPage()
                        print("\t"+"-"*70)
                        print('\t'+'-'*70+'\n\t\t\t\t\tReport \n\t'+'-'*70+'\n')
                        print("\t"+"-"*70)
                            
                    elif key.upper()=="Q":
                        loop2=False
                        loop=False
                        ClearPage()
                        
                    else:
                        print("\tInvalid input. Please try again")
                        input("\tPress ENTER to continue")
                        ClearPage()
                        loop2=False
                        loop=False
                    
                elif option == "2":
                    fileName=content[0] + content[1]+"(FullAttendance).txt"
                    with open (fileName,"r") as f:
                        for x in f:
                            print(x)
                    key=input("\t(C)ontinue / (Q)uit >> ")
                    if key.upper()=="C":
                        i=0
                        content=[]
                        ClearPage()
                        print("\t"+"-"*70)
                        print('\t'+'-'*70+'\n\t\t\t\t\tReport \n\t'+'-'*70+'\n')
                        print("\t"+"-"*70)
                            
                    elif key.upper()=="Q":
                        loop2=False
                        loop=False
                        ClearPage()
                        
                    else:
                        print("\tInvalid input. Please try again")
                        input("\tPress ENTER to continue")
                        ClearPage()
                        loop2=False
                        loop=False
                    
                    
                elif option == "Q":
                    loop2=False
                    loop=False
                    ClearPage()
                    
                else:
                    print("\tInvalid input, Try again")
                    input("\tPress ENTER to continue")
                    ClearPage()
    
            
#MainMenu
loop=True
while loop:
    OpenFile("MainMenu.txt")
    key = input("\tEnter(1/2/Q): ")
#Student view
    if key == "1":
        ClearPage()
        loop2=True
        while loop2:
            OpenFile("StudentView.txt")
            opt = input("\tOption[(Q)uit]: ")
            
            if opt == "1":
                ClearPage()
                studAttendance()
                
            elif opt.upper() == "Q":
                loop2=False
                ClearPage()
                
            else:
                print("\tInvalid input, Try again")
                input("\tPress ENTER to continue")
                ClearPage()
                
#Admin view            
    elif key == "2":
        ClearPage()
        loop3=True
        while loop3:
            OpenFile("AdminView.txt")
            option = input("\tOption[(Q)uit]: ")
            ClearPage()
            if option == "1":
                loop4=True
                while loop4:
                    OpenFile("SYSMaintenanceMenu.txt")
                    opt=input("\tOption[(Q)uit]: ")
                    ClearPage()
                    if opt == "1":
                        courseRec()
                        loop4=False
                        ClearPage()
                        
                    elif opt == "2":
                        studRec()
                        loop4=False
                        ClearPage()
                        
                    elif opt.upper() == "Q":
                        loop4=False
                        ClearPage()
                        
                    else:
                        print("\tInvalid input, Try again")
                        input("\tPress ENTER to continue")
                        ClearPage()
                        
            elif option == "2":
                CRUD()
                
                
            elif option == "3":
                bulk()
                ClearPage()

            elif option == "4":
                report()
                ClearPage()
                
            elif option.upper() == "Q":
                loop3=False

            else:
                print("\tInvalid input, Try again")
                input("\tPress ENTER to continue")
                ClearPage()
        
    elif key.upper() == "Q":
        loop=False
        ClearPage()
        
    else:
        print("\tInvalid input, Try again")
        input("\tPress ENTER to continue")
        ClearPage()

