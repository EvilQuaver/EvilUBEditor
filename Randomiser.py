import random
import FileNavigator
from operator import itemgetter

# Function
def Randomiser():

    # Create variables
    RandomiseAll = False
    RandomiseBPM = False
    RandomiseNoteType = False
    RandomiseHolds = False
    RandomisePos = False
    RandomiseDiff = False
    RandomiseLevel = False
    RandomiseRate = 0
    RandomiseNoteFirst = False
    RandomiseHoldsFirst = False
    RandomisePosFirst = False
    NoteCap = 0
    NegativeValues = False

    print("If you've used this mode before and want to use the same settings type 1.\nOtherwise just hit enter.")
    if str(input()) == "1":
        PrevSettings = FileNavigator.FetchLastSettings("Randomiser")
        X, RandomiseAll, RandomiseBPM, RandomiseNoteType, RandomiseNoteFirst, RandomiseHolds, RandomiseHoldsFirst, RandomisePos, RandomisePosFirst, RandomiseDiff, RandomiseLevel, NegativeValues, Constraints, RandomiseRate, NoteCap = PrevSettings
        RandomiseAll = RandomiseAll == "True"
        RandomiseBPM = RandomiseBPM == "True"
        RandomiseNoteType = RandomiseNoteType == "True"
        RandomiseHolds = RandomiseNoteType == "True"
        RandomisePos = RandomisePos == "True"
        RandomiseDiff = RandomiseDiff == "True"
        RandomiseLevel = RandomiseLevel == "True"
        RandomiseRate = int(RandomiseRate)
        RandomiseNoteFirst = RandomiseNoteFirst == "True"
        RandomiseHoldsFirst = RandomiseHoldsFirst == "True"
        RandomisePosFirst = RandomisePosFirst == "True"
        Constraints = Constraints == "True"
        NoteCap = int(NoteCap)
        NegativeValues = NegativeValues == "True"
        # Surely theres a shorter way to do this..
    else:
        print("Randomise settings?\n(If you want the chart to work in game you should probably customise settings.)")
        RandomiseSettings = str(input("Ender Y/N")).lower()
        if any((RandomiseSettings == "y", RandomiseSettings == "yes")):
            RandomiseAll = random.randint(0,1) == 1
            if not RandomiseAll:
                RandomiseBPM = random.randint(0,1) == 1
                RandomiseNoteFirst = random.randint(0,1) == 1
                if RandomiseNoteFirst:
                    RandomiseNoteType = random.randint(0,1) == 1
                RandomiseHoldsFirst = random.randint(0,1) == 1
                if RandomiseHoldsFirst:
                    RandomiseHolds = random.randint(0,1) == 1
                RandomisePosFirst = random.randint(0,1) == 1
                if RandomisePosFirst:
                    RandomisePos = random.randint(0,1) == 1
                RandomiseDiff = random.randint(0,1) == 1
                RandomiseLevel = random.randint(0,1) == 1
            RandomiseRate = random.randint(1,10)
            NoteCap = random.randint(1,1000)
            NegativeValues = random.randint(0,1) == 1
            Constraints = random.randint(0, 1) == 1
        else:

            # Randomise Rate
            print("Randomisation Rate. \n(Lower is more random)")
            RandomiseRate = abs(int(input("Enter Number: ")))

            # Constraints
            print("\n\n\nOnly use intended values?\n(Makes chart more likely to be functional)")
            ConstraintsInput = str(input("Enter Y/N: ")).lower()
            Constraints = any((ConstraintsInput == "y", ConstraintsInput == "yes"))
            if not Constraints:
                print("\n\n\nUse Negative Values?\n(Makes chart less likely to be functional)")
                NegativeValuesInput = str(input("Enter Y/N: ")).lower()
                NegativeValues = any((NegativeValuesInput == "y", NegativeValuesInput == "yes"))

            # Randomise Everything
            print("\n\n\nRandomise Everything? \n(Literally... Everything) \n(May add or reduce note count)")
            RandomiseAllInput = str(input("Enter Y/N: ")).lower()
            if any((RandomiseAllInput == "n", RandomiseAllInput == "no")):
                RandomiseAll = False

                # Randomise Level
                print("\n\n\nRandomise Level?")
                RandomiseLevelInput = str(input("Enter Y/N: ")).lower()
                RandomiseLevel = any((RandomiseLevelInput == "y", RandomiseLevelInput == "yes"))

                # Randomise Difficulty
                print("\n\n\nRandomise Difficulty?")
                RandomiseDiffInput = str(input("Enter Y/N: ")).lower()
                RandomiseDiff =  any((RandomiseDiffInput == "y", RandomiseDiffInput == "yes"))

                # Randomise Position
                print("\n\n\nRandomise Position?")
                RandomisePosFirstInput = str(input("Enter Y/N: ")).lower()
                if any((RandomisePosFirstInput == "y", RandomisePosFirstInput == "yes")):
                    RandomisePosFirst = True

                    # Choose how to randomise position
                    print("\n1 = Randomly Swap Position\n2 = Randomly Generate Position")
                    RandomisePosInput = int(input("Enter 1/2: "))
                    if RandomisePosInput == 1:
                        RandomisePos = False
                    else:
                        RandomisePos = True
                else:
                    RandomisePosFirst = False

                # Randomise Note Type
                print("\n\n\nRandomise Note Type?")
                RandomiseNoteFirstInput = str(input("Enter Y/N: ")).lower()
                if any((RandomiseNoteFirstInput == "y", RandomiseNoteFirstInput == "yes")):
                    RandomiseNoteFirst = True

                    # Choose how to randomise note type
                    print("\n1 = Randomly Swap Type\n2 = Randomly Generate Type")
                    RandomiseNoteTypeInput = int(input("Enter 1/2: "))
                    if RandomiseNoteTypeInput == 1:
                        RandomiseNoteType = False
                    else:
                        RandomiseNoteType = True
                else:
                    RandomiseNoteFirst = False

                # Randomise Holds
                print("\n\n\nRandomise Holds?")
                RandomiseHoldsFirstInput = str(input("Enter Y/N: ")).lower()
                if any((RandomiseHoldsFirstInput == "y", RandomiseHoldsFirstInput == "yes")):
                    RandomiseHoldsFirst = True

                    # Choose how to randomise holds
                    print("\n1 = Randomly Swap Hold\n2 = Randomly Generate Hold")
                    RandomiseHoldsInput = int(input("Enter 1/2: "))
                    if RandomiseHoldsInput == 1:
                        RandomiseHolds = False
                    else:
                        RandomiseHolds = True
                else:
                    RandomiseHoldsFirst = False

                # Randomise BPM
                print("\n\n\nRandomise BPM?")
                RandomiseBPMInput = str(input("Enter Y/N: ")).lower()
                RandomiseBPM = any((RandomiseBPMInput == "y", RandomiseBPMInput == "yes"))

            else:
                RandomiseAll = True
                print("\n Note Cap?\nNo more than this amount will be made")
                NoteCap = abs(int(input("Enter Number: ")))

        RandomiserSettings = [RandomiseAll, RandomiseBPM, RandomiseNoteType, RandomiseNoteFirst, RandomiseHolds, RandomiseHoldsFirst, RandomisePos, RandomisePosFirst, RandomiseDiff, RandomiseLevel, NegativeValues, Constraints, RandomiseRate, NoteCap]
        FileNavigator.SaveLastSettings("Randomiser", RandomiserSettings)

    # Debug kinda maybe just useful to leave it here
    print("\n\n\n\n Settings:")
    print(f"Randomise All: {RandomiseAll}")
    print(f"Randomise BPM: {RandomiseBPM}")
    print(f"Randomise Note Type: {RandomiseNoteType}")
    print(f"Randomise Note Type First: {RandomiseNoteFirst}")
    print(f"Randomise Holds: {RandomiseHolds}")
    print(f"Randomise Holds First: {RandomiseHoldsFirst}")
    print(f"Randomise Position: {RandomisePos}")
    print(f"Randomise Position First: {RandomisePosFirst}")
    print(f"Randomise Difficulty: {RandomiseDiff}")
    print(f"Randomise Level: {RandomiseLevel}")
    print(f"Randomise Negatives: {NegativeValues}")
    print(f"Contraints: {Constraints}")
    print(f"Note Cap: {NoteCap}")
    print(f"Randomise Rate: {RandomiseRate}")
    print("\n\n\n\n\n\n")


    ####################################################################################







    # Randomise
    print("\n\n\n\n\n\n\n\n\nFinding files")
    ChartList = FileNavigator.FindCharts()

    for file in ChartList:
        print(f"\nRandomising: {file[1]}")

        MetaDataFound = False
        TimingPointsFound = False
        HitObjectsFound = False


        ShuffleNoteTypes = []
        ShuffleHolds = []
        ShufflePos = []
        NewBeatMap = []
        NoteStorage = []

        HasBeenEdited = False
        HasBeenCheckedForEdited = False
        DifficultyList = ["Beginner", "Normal", "Hard", "Expert", "UNBEATABLE"]
        StarDifficultyList = ["Evil", "Star", "Videogame", "Horse", "Quaver", "Garn", "Cheese", "Drywall", "The Hunger..."]
        SongLength = 0
        NoteAmt = 0

        ConstrainChoices0 = ["213", "298", "384", "469"]
        ConstrainChoices4 = ["0", "2", "3", "4", "6", "8", "10", "12", "14"]
        ConstrainChoices6 = ["1", "3"]
        ConstrainChoices7 = ["0", "1", "3"]

        with open(file[2], "r") as BeatMap:
            for line in BeatMap:

                # Save MetaData Info
                if line.__contains__("[Metadata]"):
                    MetaDataFound = True
                    NewBeatMap.append(line)
                    continue
                elif MetaDataFound and not TimingPointsFound:
                    if line.__contains__("Version"):
                        if RandomiseDiff or RandomiseAll:
                            RandomDiff = random.randint(0, 5)
                            if RandomDiff == 5:
                                RandomDiff = random.randint(0, 8)
                                NewBeatMap.append(f"Version:{StarDifficultyList[RandomDiff]}\n")
                                continue
                            else:
                                NewBeatMap.append(f"Version:{DifficultyList[RandomDiff]}\n")
                                continue
                    elif line.__contains__("Tags"):
                        if RandomiseLevel or RandomiseAll:
                            NewLine = line.split(",")
                            NewLine[0] = ('Tags:{"Level:"' + str(random.randint(1, 26)))
                            SongLength = int(float(NewLine[2].split(":")[1]))
                            SongLength *= 1000
                            NewLine = ",".join(NewLine)
                            NewBeatMap.append(NewLine)
                            continue
                        else:
                            LengthCheck = line.split(",")
                            LengthCheck[0] = ('Tags:{"Level:"' + str(random.randint(1, 26)))
                            SongLength = int(float(LengthCheck[2].split(":")[1]))
                            SongLength *= 1000

                # Save TimingPoints Info
                if line.__contains__("[TimingPoints]"):
                    TimingPointsFound = True
                    NewBeatMap.append(line)
                    if RandomiseBPM or RandomiseAll:
                        RandomBPMAmt = int(abs(50 / RandomiseRate))
                        for i in range(random.randint(1,RandomBPMAmt)):
                            NewLine = ["0","0","0","2","0","100","1","8"]
                            NewLine[0] = str(random.randint(0, SongLength))
                            NewLine[1] = str((60000 / random.randint(50, 1000)))
                            NewLine[2] = str(random.randint(1, 16))
                            NewLine = ",".join(NewLine)
                            NewLine = NewLine + "\n"
                            NewBeatMap.append(NewLine)
                    continue
                elif TimingPointsFound and not HitObjectsFound:
                    if line.__contains__("[HitObjects]"):
                        NewBeatMap.append(line)
                        HitObjectsFound = True
                        continue
                    elif RandomiseBPM or RandomiseAll:
                        continue
                    else:
                        NewBeatMap.append(line)
                        continue

                # Save Notes Info
                if HitObjectsFound:
                    NewLine = line.split(",")
                    if len(NewLine) > 1:
                        if random.randint(1,RandomiseRate) != 1:
                            NewLine.append("skip")
                            NoteStorage.append(NewLine)
                            continue

                        ShufflePos.append(NewLine[2])
                        if len(NewLine[5].split(":")) > 3:
                            ShuffleHolds.append(NewLine[5].split(":")[0])
                            ShuffleNoteTypes.append([NewLine[0], NewLine[4], NewLine[5].split(":")[1], NewLine[5].split(":")[2]])
                        else:
                            ShuffleHolds.append("0")
                            ShuffleNoteTypes.append([NewLine[0], NewLine[4], NewLine[5].split(":")[0], NewLine[5].split(":")[1]])
                        NoteAmt += 1
                        NewLine.append("keep")
                        NoteStorage.append(NewLine)
                        continue
                
                if not HasBeenCheckedForEdited:
                    if line.__contains__("Evil Editor"):
                        HasBeenEdited = True
                    HasBeenCheckedForEdited = True
                NewBeatMap.append(line)
            







            #############################################################################################

            # Randomise Notes
            if RandomiseAll:
                NoteAmt = random.randint(1,int(abs(NoteCap / RandomiseRate)))
            
            RateControl = int(abs(20000 / RandomiseRate))
            HitObjectsList = []


            while NoteAmt > 1:
                if not RandomiseAll:
                    ThisNote = NoteStorage[0]
                    if ThisNote[-1] == "skip":
                        ThisNote.pop(-1)
                        NoteStorage.pop(0)
                        NoteAmt -= 1
                        HitObjectsList.append(ThisNote)
                        continue
                    else:
                        ThisNote.pop(-1)

                    NewLine = ThisNote
                    EvilEndPart = ThisNote[5].split(":")
                    EvilEndPart[-1] = "0"
                    NewLine.pop(5)
                    if len(EvilEndPart) > 4:
                        HoldNote = True
                    else:
                        HoldNote = False
                else:
                    EvilEndPart = ["0","0","0","0"]
                    NewLine = ["0","192","0","0","0"]
                    HoldNote = False
                



                # Randomise Position
                if RandomisePosFirst and not RandomisePos:
                    Pos = random.randint(0, max(len(ShufflePos) - 1, 0))
                    NewLine[2] = ShufflePos[Pos]
                    ShufflePos.pop(Pos)
                elif RandomisePos:
                    if not NegativeValues:
                        NewLine[2] = str(random.randint(0, SongLength))
                    else:
                        NewLine[2] = str(random.randint(-SongLength, SongLength))





                # Randomise Holds
                if RandomiseHoldsFirst and not RandomiseHolds:
                    HoldNum = random.randint(0, max(len(ShuffleHolds) - 1, 0))

                    if ShuffleHolds[HoldNum] != "0":
                        HoldNote = True
                        EvilEndPart.append("0")
                        HoldNote = ShuffleHolds[HoldNum]
                        NewLine[3] = "128"
                        EvilEndPart[0] = HoldNote
                    else:
                        NewLine[3] = "1"
                    ShuffleHolds.pop(HoldNum)
                elif RandomiseHolds:
                    if Constraints:
                        IsHold = random.randint(0,4)
                        if IsHold == 4:
                            HoldNote = True
                            NewLine[3] = "128"
                            EvilEndPart.append("0")
                            EvilEndPart[0] = str(random.randint(int(NewLine[2]), SongLength))
                        else:
                            NewLine[3] = "1"
                    elif not NegativeValues:
                        IsHold = random.randint(0,4)
                        if IsHold == 4:
                            HoldNote = True
                            NewLine[3] = str(random.randint(0,RateControl))
                            EvilEndPart.append("0")
                            EvilEndPart[0] = str(random.randint(int(NewLine[2]), SongLength))
                        else:
                            NewLine[3] = "1"
                    else:
                        IsHold = random.randint(0,4)
                        if IsHold == 4:
                            HoldNote = True
                            NewLine[3] = str(random.randint(-RateControl,RateControl))
                            EvilEndPart.append("0")
                            EvilEndPart[0] = str(random.randint(-SongLength, SongLength))
                        else:
                            NewLine[3] = "1"
                        




                # Randomise Note Type
                if RandomiseNoteFirst and not RandomiseNoteType:
                    NoteNum = random.randint(0, max(len(ShuffleNoteTypes) - 1, 0))
                    
                    Note = ShuffleNoteTypes[NoteNum]
                    NewLine[0] = Note[0]
                    NewLine[4] = Note[1]
                    if HoldNote:
                        EvilEndPart[1] = Note[2]
                        EvilEndPart[2] = Note[3]
                    else:
                        EvilEndPart[0] = Note[2]
                        EvilEndPart[1] = Note[3]
                    ShuffleNoteTypes.pop(NoteNum)
                elif RandomiseNoteType:
                    if Constraints:
                        NewLine[0] = ConstrainChoices0[random.randint(0,3)]
                        NewLine[4] = ConstrainChoices4[random.randint(0,8)]
                        if HoldNote:
                            EvilEndPart[1] = ConstrainChoices6[random.randint(0,1)]
                            EvilEndPart[2] = ConstrainChoices7[random.randint(0,2)]
                        else:
                            EvilEndPart[0] = ConstrainChoices6[random.randint(0,1)]
                            EvilEndPart[1] = ConstrainChoices7[random.randint(0,2)]
                    elif not NegativeValues:
                        NewLine[0] = str(random.randint(0, RateControl))
                        NewLine[4] = str(random.randint(0, RateControl))
                        if HoldNote:
                            EvilEndPart[1] = str(random.randint(0, RateControl))
                            EvilEndPart[2] = str(random.randint(0, RateControl))
                        else:
                            EvilEndPart[0] = str(random.randint(0, RateControl))
                            EvilEndPart[1] = str(random.randint(0, RateControl))
                    else:
                        NewLine[0] = str(random.randint(-RateControl, RateControl))
                        NewLine[4] = str(random.randint(-RateControl, RateControl))
                        if HoldNote:
                            EvilEndPart[1] = str(random.randint(-RateControl, RateControl))
                            EvilEndPart[2] = str(random.randint(-RateControl, RateControl))
                        else:
                            EvilEndPart[0] = str(random.randint(-RateControl, RateControl))
                            EvilEndPart[1] = str(random.randint(-RateControl, RateControl))
                else:
                    NewLine[0]
                    NewLine[4]
                    if HoldNote:
                        EvilEndPart[1]
                        EvilEndPart[2]
                    else:
                        EvilEndPart[0]
                        EvilEndPart[1]

                # Last part that probably shouldnt be touched but this is the evil editor we do evil things
                if RandomiseAll and not NegativeValues and not Constraints:
                    NewLine[1] = str(random.randint(0,RateControl))
                    if HoldNote:
                        EvilEndPart[3] = str(random.randint(0,RateControl))
                        EvilEndPart[4] = str(random.randint(0,RateControl))
                    else:
                        EvilEndPart[2] = str(random.randint(0,RateControl))
                        EvilEndPart[3] = str(random.randint(0,RateControl))
                elif RandomiseAll and NegativeValues and not Constraints:
                    NewLine[1] = str(random.randint(-RateControl,RateControl))
                    if HoldNote:
                        EvilEndPart[3] = str(random.randint(-RateControl,RateControl))
                        EvilEndPart[4] = str(random.randint(-RateControl,RateControl))
                    else:
                        EvilEndPart[2] = str(random.randint(-RateControl,RateControl))
                        EvilEndPart[3] = str(random.randint(-RateControl,RateControl))
                
                # Remove line from storage
                if not RandomiseAll:
                    NoteStorage.pop(0)

                # Save line
                EvilEndPart = ":".join(EvilEndPart)
                EvilEndPart += ":"
                EvilEndPart = EvilEndPart + "\n"
                NewLine.append(EvilEndPart)
                NoteAmt -= 1
                HitObjectsList.append(NewLine)

            file.append(HasBeenEdited)
            HitObjectsList.sort(key = lambda x: int(x[2]))
            for line in HitObjectsList:
                NewLine = ",".join(line)
                NewBeatMap.append(NewLine)
            file.append(NewBeatMap)






        # Write randomised shit to file
        FileNavigator.WriteChart(file)