import Randomiser
import OffsetEditor

while True:
    # Open Messages
    print("\n\n\nPut chart FOLDERS in 'Charts' file.**********************\n")

    # Questions
    print("What evils will be commited to your chart?\n1 = Randomiser\n2 = Chart Offset")
    Decisions = int(input("Enter Number: "))
    print("\n\n\n\n\n\n\n")
    if Decisions == 1:
        #try:
            Randomiser.Randomiser()
        #except Exception as e:
            #print("oh no an error...")
           # print(e)
    elif Decisions == 2:
        try:
            OffsetEditor.EditOffset()
        except Exception as e:
            print("oh no an error...")
            print(e)

    RestartCheck = str(input("Files Edited!..probably.\nPress Enter to close or type 1 to edit more."))
    if RestartCheck != "1":
        break