import FileNavigator


def EditOffset():
    print("How much will the notes be moved?\nIn milliseconds\nDecimals will crash it probably\nIf this is official editor related try -75\n")
    Offset = int(input("Enter Number(ms): "))


    print("Finding files")
    ChartList = FileNavigator.FindCharts()


    for file in ChartList:
        print(f"Fixing: {file[1]}")

        NewBeatMap = []
        HasFoundObjects = False
        CheckedForEdited = False
        HasBeenEdited = False

        with open(file[2], "r") as BeatMap:
            for line in BeatMap:

                if line.__contains__("[HitObjects]"):
                    HasFoundObjects = True
                    NewBeatMap.append(line)

                elif HasFoundObjects == True:
                    NewLine = line.split(",")

                    if len(NewLine) > 1:
                        Location = int(NewLine[2])
                        Location += Offset
                        NewLine[2] = str(Location)

                        SplitLine = NewLine[5].split(":")
                        if SplitLine[0] != 0:
                            SecondLocation = int(SplitLine[0])
                            SecondLocation += Offset
                            SplitLine[0] = str(SecondLocation)
                            NewLine[5] = ":".join(SplitLine)

                        NewLine = ",".join(NewLine)
                        NewBeatMap.append(NewLine)

                else:
                    NewBeatMap.append(line)
                    if not CheckedForEdited:
                        if line.__contains__("Evil Editor"):
                            HasBeenEdited = True
                        CheckedForEdited = True

        file.append(HasBeenEdited)
        file.append(NewBeatMap)

        FileNavigator.WriteChart(file)