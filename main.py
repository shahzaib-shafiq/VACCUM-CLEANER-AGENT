import random

class Environment:
    def __init__(self):
        # 0 indicates Clean, 1 indicates Partially Clean, and 2 indicates Dirty
        self.Locationcondition = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
                                  'K': 0}

        # instantiate location and conditions
        ROOMS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

        for i in ROOMS:
            self.Locationcondition[i] = random.randint(0, 2)


class Agent(Environment):
    # Agent Class For Agent Tasks
    def __init__(self):
        super().__init__()

        #print(self.Locationcondition)
        # Check Room Condition and Perform Action
        # 0 Clean
        # 1 Patially Clean
        # 2 Dirty

        ''' Clean the Dirt
        # if else condition to check room condition
        # checking the current condition of room'''

    CurrentLocation=0

    def CheckRoom(self):
     i=0
     alreadyvisited = []
     CurrentLocation = random.randint(1, 11)
     while i < 11:



        # if Vacuum at A
        if CurrentLocation == 1:
            print("Vacuum Cleaner is  in Room A")
            # if Location is CLEAN
            if self.Locationcondition['A'] == 0:
                print("Location A is Clean")
                #Agent can Only Move to Room B
                alreadyvisited.append(CurrentLocation)
                CurrentLocation=2;
                print("Moving Right")

            elif self.Locationcondition['A'] == 1:
                # Agent can Only Move to Room B
                print("Location A is Partially Clean\nCleaning Room A\nRoom A is Cleaned")
                self.Locationcondition['A'] = 0
                alreadyvisited.append(CurrentLocation)
                CurrentLocation = 2;
                print("Moving Right")
            else:
                print("Location A is Dirty\nCleaning Room A\nRoom A is Cleaned")
                self.Locationcondition['A'] = 0;
                CurrentLocation = 2;
                alreadyvisited.append(CurrentLocation)
                # Agent can Only Move to Room B

            print("Moving Right")
            print("Moving to Room B")

        elif CurrentLocation == 2:
                print("Vacuum Cleaner is  in Room B")
                if self.Locationcondition['B'] == 0:
                    print("Location B is Clean")
                    CurrentLocation=random.randint(1,3)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 1 or v == 2):
                            CurrentLocation=3
                            print("Moving Right")
                        elif(v == 3 or v==2):
                            CurrentLocation=1
                            print("Moving Left")
                elif self.Locationcondition['B'] == 1:
                    print("Location B is Partially Clean\nCleaning Room B\nRoom B is Cleaned")
                    self.Locationcondition['B'] = 0
                    CurrentLocation = random.randint(1, 3)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 1 or v == 2):
                            CurrentLocation=3
                            print("Moving Right")
                        elif(v == 3 or v == 2):
                            CurrentLocation=1
                            print("Moving Left")
                else:
                    print("Location B is Dirty\nCleaning Room B\nRoom B is Cleaned")
                    self.Locationcondition['B'] = 0;
                    CurrentLocation = random.randint(1, 3)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 1 or v == 2):

                            CurrentLocation=3
                            print("Moving Right")
                        elif(v == 3 or v == 2):
                            CurrentLocation=1
                            print("Moving left")
        elif CurrentLocation == 3:
                print("Vacuum Cleaner is  in Room C")

                if self.Locationcondition['C'] == 0:
                    print("Location C is Clean")
                    CurrentLocation = random.randint(2,4)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 2 or v == 3):
                            CurrentLocation=4
                            print("Moving Right")
                        elif(v == 4 or v == 3):
                            CurrentLocation=2
                            print("Moving Left")
                elif self.Locationcondition['C'] == 1:

                    print("Location C is Partially Clean\nCleaning Room C\nRoom C is Cleaned")
                    self.Locationcondition['C'] = 0
                    CurrentLocation = random.randint(2, 4)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 2 or v == 3):
                            CurrentLocation=4

                        elif(v == 4 or v == 3):
                            CurrentLocation=2
                        print("Moving Left")
                else:
                    print("Location C is Dirty\nCleaning Room C\nRoom C is Cleaned")
                    self.Locationcondition['C'] = 0;
                    CurrentLocation = random.randint(2, 4)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 2  or v == 3 ):
                            CurrentLocation=4

                        elif(v == 4 or v == 3):
                            CurrentLocation=2

        elif CurrentLocation == 4:
                print("Vacuum Cleaner is in Room D")
                # if Location is Dirty
                if self.Locationcondition['D'] == 0:
                    print("Location D is Clean")
                    CurrentLocation = random.randint(3,5)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 3 or v == 4):
                            CurrentLocation=5

                        elif(v == 5 or v == 4):
                            CurrentLocation=3

                elif self.Locationcondition['D'] == 1:
                    print("Location D is Partially Clean\nCleaning Room D\nRoom D is Cleaned")
                    self.Locationcondition['D'] = 0
                    CurrentLocation = random.randint(3, 5)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 3 or v == 4):
                            CurrentLocation=5

                        elif(v == 5 or v == 4):
                            CurrentLocation=3

                else:
                    print("Location D is Dirty\nCleaning Room D\nRoom D is Cleaned")
                    self.Locationcondition['D'] = 0;
                    CurrentLocation = random.randint(3, 5)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 3 or v == 4):
                            CurrentLocation=5

                        elif(v == 5 or v == 4):
                            CurrentLocation=3

        elif CurrentLocation == 5:
                print("Vacuum Cleaner is in Room E")

                if self.Locationcondition['E'] == 0:
                    print("Location E is Clean")
                    CurrentLocation = random.randint(4, 6)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 4 or v == 5):
                            CurrentLocation=6

                        elif(v == 6 or v == 5):
                            CurrentLocation=4

                elif self.Locationcondition['E'] == 1:

                    print("Location E is Partially Clean\nCleaning Room E\nRoom E is Cleaned")
                    self.Locationcondition['E'] = 0
                    CurrentLocation = random.randint(4, 6)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 4 or v == 5):
                            CurrentLocation=6

                        elif(v == 6 or v == 5):
                            CurrentLocation=4

                else:
                    print("Location E is Dirty\nCleaning Room E\nRoom E is Cleaned")
                    self.Locationcondition['E'] = 0;
                    CurrentLocation = random.randint(4, 6)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 4 or v== 5):

                            CurrentLocation=6

                        elif(v == 6 or v == 5):
                            CurrentLocation=4
        elif CurrentLocation == 6:
                print("Vacuum Cleaner is in Room F")

                if self.Locationcondition['F'] == 0:
                    print("Location F is Clean")
                    CurrentLocation = random.randint(5,7)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 5 or v == 6 ):
                            CurrentLocation=7
                        elif(v == 7 or v == 6):
                            CurrentLocation=5
                elif self.Locationcondition['F'] == 1:

                    print("Location F is Partially Clean\nCleaning Room F\nRoom F is Cleaned")
                    self.Locationcondition['F'] = 0
                    CurrentLocation = random.randint(5, 7)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 5 or v == 6):
                            CurrentLocation=7
                        elif(v == 7 or v == 6):
                            CurrentLocation=5
                else:
                    print("Location F is Dirty\nCleaning Room F\nRoom F is Cleaned")
                    self.Locationcondition['F'] = 0;
                    CurrentLocation = random.randint(5, 7)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 5 or v == 6):
                            CurrentLocation=7
                        elif(v == 7 or v == 6):
                            CurrentLocation=5
        elif CurrentLocation == 7:
                print("Vacuum Cleaner is in Room G")
                # if Location is Dirty
                if self.Locationcondition['G'] == 0:
                    print("Location G is Clean")
                    CurrentLocation = random.randint(6,8)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 6 or v == 7):
                            CurrentLocation=8
                        elif(v == 8 or v == 7):
                            CurrentLocation=6
                elif self.Locationcondition['G'] == 1:

                    print("Location G is Partially Clean\nCleaning Room G\nRoom G is Cleaned")
                    self.Locationcondition['G'] = 0
                    CurrentLocation = random.randint(6, 8)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 6 or v == 7):
                            CurrentLocation=8
                        elif(v == 8 or v == 7):
                            CurrentLocation=6
                else:
                    print("Location G is Dirty\nCleaning Room G\nRoom G is Cleaned")
                    self.Locationcondition['G'] = 0;
                    CurrentLocation = random.randint(6, 8)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 6 or v == 7):
                            CurrentLocation=8
                        elif(v == 8 or v == 7):
                            CurrentLocation=6
        elif CurrentLocation == 8:
                print("Vacuum Cleaner is  in Room H")

                if self.Locationcondition['H'] == 0:
                    print("Location H is Clean")
                    CurrentLocation = random.randint(7,9)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 7 or v == 8):
                            CurrentLocation=9
                        elif(v == 9 or v == 8):
                            CurrentLocation=7
                elif self.Locationcondition['H'] == 1:
                    print("Location H is Partially Clean\nCleaning Room H\nRoom H is Cleaned")
                    self.Locationcondition['H'] = 0
                    CurrentLocation = random.randint(7, 9)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 7 or v == 8):
                            CurrentLocation=9
                        elif(v == 9 or v == 8):
                            CurrentLocation=7
                else:
                    print("Location H is Dirty\nCleaning Room H\nRoom H is Cleaned")
                    self.Locationcondition['H'] = 0;
                    CurrentLocation = random.randint(7, 9)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 7 or v == 8):
                            CurrentLocation=9
                        elif(v == 9 or v == 8):
                            CurrentLocation=7
        elif CurrentLocation == 9:
                print("Vacuum Cleaner is in Room I")
                # if Location is Dirty
                if self.Locationcondition['I'] == 0:
                    print("Location I is Clean")
                    CurrentLocation = random.randint(8,10)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 8 or v == 9):
                            CurrentLocation=10
                        elif(v == 10 or v == 9):
                            CurrentLocation=8
                elif self.Locationcondition['I'] == 1:
                    print("Location I is Partially Clean\nCleaning Room I\nRoom I is Cleaned")
                    self.Locationcondition['I'] = 0
                    CurrentLocation = random.randint(8, 10)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 8 or v == 9):
                            CurrentLocation = 10
                        elif (v == 10 or v == 9):
                            CurrentLocation = 8
                else:
                    print("Location I is Dirty\nCleaning Room I\nRoom I is Cleaned")
                    self.Locationcondition['I'] = 0;
                    CurrentLocation = random.randint(8, 10)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 8 or v == 9):
                            CurrentLocation = 10
                        elif (v == 10 or v == 9):
                            CurrentLocation = 8

        elif CurrentLocation == 10:
                print("Vacuum Cleaner is in Room J")
                # if Location is Dirty
                if self.Locationcondition['J'] == 0:
                    print("Location J is Clean")
                    CurrentLocation = random.randint(9,11)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 9 or v == 10):
                            CurrentLocation=11
                        elif(v == 11 or v == 10):
                            CurrentLocation=9
                elif self.Locationcondition['J'] == 1:

                    print("Location J is Partially Clean\nCleaning Room J\nRoom J is")
                    self.Locationcondition['J'] = 0
                    CurrentLocation = random.randint(9, 11)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 9 or v == 10):
                            CurrentLocation=11
                        elif(v == 11 or v == 10):
                            CurrentLocation=9
                else:
                    print("Location J is Dirty\nCleaning Room J\nRoom J is Cleaned")
                    self.Locationcondition['J'] = 0;
                    CurrentLocation = random.randint(9, 11)
                    alreadyvisited.append(CurrentLocation)
                    for v in alreadyvisited:
                        if (v == 9 or v == 10):
                            CurrentLocation=11
                        elif(v == 11 or v == 10):
                            CurrentLocation=9
        elif CurrentLocation == 11:
                print("Vacuum Cleaner is in Room K")
                # if Location is Dirty
                if self.Locationcondition['K'] == 0:
                    print("Location K is Clean")
                    CurrentLocation=10
                    alreadyvisited.append(CurrentLocation)
                elif self.Locationcondition['K'] == 1:

                    print("Location K is Partially Clean\nCleaning Room K\nRoom K is Cleaned")
                    self.Locationcondition['K'] = 0
                    CurrentLocation = 10
                    alreadyvisited.append(CurrentLocation)
                else:
                    print("Location K is Dirty\nCleaning Room K\nRoom K is Cleaned")
                    self.Locationcondition['K'] = 0;
                    CurrentLocation = 10
                    alreadyvisited.append(CurrentLocation)
        i+=1
     print("\nTotal Rooms Visited",i)
     print(alreadyvisited)





__name__ == '__main__'
E=Environment()
agent=Agent()
print("Rooms states Random Initlization")
print(agent.Locationcondition)
agent.CheckRoom()
