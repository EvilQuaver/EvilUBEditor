import os

def FindCharts():
    ChartList = []
    for chart in os.listdir(f"{os.path.dirname(__file__)}\Charts"):
        if os.path.isdir(f"{os.path.dirname(__file__)}\Charts\{chart}"):
            for file in os.listdir(f"{os.path.dirname(__file__)}\Charts\{chart}"):
                if file.endswith(".txt"):
                    ChartList.append([chart, file, f"{os.path.dirname(__file__)}\Charts\{chart}/{file}"])
    return ChartList



def WriteChart(chart):
    if not os.path.isdir(f"{os.path.dirname(__file__)}\ChartOutput\{chart[0]}"):
         os.mkdir(f"{os.path.dirname(__file__)}\ChartOutput\{chart[0]}")

    with open(f"{os.path.dirname(__file__)}\ChartOutput\{chart[0]}\{chart[1]}", "w") as BeatMap:
            if not chart[3]:
                BeatMap.write("// Edited with Evil Editor\n")
            BeatMap.writelines(chart[4])
            print(f"Randomised: {chart[1]}\n")





def SaveLastSettings(Mode, Settings):
    with open (f"{os.path.dirname(__file__)}\LastSettings.txt", "r") as SettingsFile:
        ModeExists = False
        NewSettings = []
        SettingsString = []
        for line in Settings:
            FixLine = str(line).replace("[]", "")
            SettingsString.append(FixLine)
        SettingsString = ",".join(SettingsString)

        for line in SettingsFile:
            if line.__contains__(Mode):
                ModeExists = True
                NewSettings.append(f"{Mode},{SettingsString}")
            else:
                NewSettings.append(line)
        if not ModeExists:
            NewSettings.append(f"{Mode}, {SettingsString}")
    with open (f"{os.path.dirname(__file__)}\LastSettings.txt", "w") as SettingsFile:
        SettingsFile.writelines(NewSettings)



def FetchLastSettings(Mode):
    with open (f"{os.path.dirname(__file__)}/LastSettings.txt", "r") as SettingsFile:
        for line in SettingsFile:
            if line.__contains__(Mode):
                GetSettings = line.split(",")
                return GetSettings
        return "None"