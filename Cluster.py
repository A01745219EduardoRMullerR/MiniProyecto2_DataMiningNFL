import csv

diccTeamNamesBefore2016 = {"Bills": "BUF", "Jets": "NYJ", "Dolphins": "MIA", "Patriots": "NE", "Ravens": "BAL", "Bengals": "CIN"
                 ,"Browns": "CLE", "Giants": "NYG", "Cardinals": "ARI", "Texans": "HOU", "Steelers": "PIT", "Colts": "IND",
                 "Jaguars": "JAX", "Bears": "CHI", "Seahawks": "SEA", "49ers": "SF", "Buccaneers": "TB", "Lions": "DET",
                 "Titans": "TEN", "Saints": "NO", "Panthers": "CAR", "Rams": "STL", "Chargers": "SD", "Cowboys": "DAL",
                "Eagles": "PHI", "Redskins":"WAS", "Falcons": "ATL", "Packers": "GB", "Vikings": "MIN", "Chiefs": "KC",
                "Broncos": "DEN", "Raiders": "OAK"}
diccTeamNamesThrough2020 = {"Bills": "BUF", "Jets": "NYJ", "Dolphins": "MIA", "Patriots": "NE", "Ravens": "BAL", "Bengals": "CIN"
                 ,"Browns": "CLE", "Giants": "NYG", "Cardinals": "ARI", "Texans": "HOU", "Steelers": "PIT", "Colts": "IND",
                 "Jaguars": "JAX", "Bears": "CHI", "Seahawks": "SEA", "49ers": "SF", "Buccaneers": "TB", "Lions": "DET",
                 "Titans": "TEN", "Saints": "NO", "Panthers": "CAR", "Rams": "LA", "Chargers": "LAC", "Cowboys": "DAL",
                "Eagles": "PHI", "Redskins": "WAS", "Falcons": "ATL", "Packers": "GB", "Vikings": "MIN", "Chiefs": "KC",
                "Broncos": "DEN", "Raiders": "LV"}

def getPicksValue():
    file = open('draft_values.csv', 'r')
    reader = csv.reader(file, skipinitialspace=True)
    values = {}
    for row in reader:
        values[(row[0])] = (row[2])
    values.pop('pick')
    for key in values:
        x = float(values[key])
        values[key] = x
    file.close()
    return values


def getStandings():
    file = open('standings.csv', 'r')
    reader = csv.reader(file, skipinitialspace=True)
    standings = {}
    for row in reader:
        fullTeam = row[0] + row[3]
        standings[fullTeam] = row[7]
    standings.pop('seasonteam')
    for key in standings:
        x = float(standings[key])
        standings[key] = x
    file.close()
    return standings


def getTeamPicks():
    file = open('teamPicks.csv', 'r')
    reader = csv.reader(file, delimiter = '\t')
    colleges = []
    team = []
    pick = []

    for row in reader:
        colleges.append(row[-1])
        team.append(row[4])
        pick.append(row[2])
    return team, pick, colleges


def getSingleCollegesList(collegesRaw):
    colleges = []
    for k in collegesRaw:
        if k not in colleges:
            colleges.append(k)
    return colleges


def getAssocNamesLetters(diccStandings):
    names = []
    letters = []
    oldLetters = list(diccTeamNamesBefore2016.values())
    oldNames = list(diccTeamNamesBefore2016.keys())
    newLetters = list(diccTeamNamesThrough2020.values())
    newNames = list(diccTeamNamesThrough2020.keys())
    for team in diccStandings:
        team_lst = list(team)
        team_lst.remove(team_lst[0])
        team_lst.remove(team_lst[0])
        team_lst.remove(team_lst[0])
        team_lst.remove(team_lst[0])
        teamLetters = "".join(team_lst)
        letters.append(teamLetters)
        teamName = ""
        if teamLetters in oldLetters:
            for n in range(0, len(oldLetters)):
                if oldLetters[n] == teamLetters:
                    teamName = oldNames[n]
                    names.append(teamName)
        elif teamLetters in newLetters:
            for n in range(0, len(newLetters)):
                if newLetters[n] == teamLetters:
                    teamName = newNames[n]
                    names.append(teamName)
    return names, letters



def getAverageTeamPctanDrafts(diccStandings, diccPicks, team, pick):
    avgPcts = {}
    draftValueperTeam = {}
    names, letters = getAssocNamesLetters(diccStandings)
    for n in range(0, len(team)-1, 1):
        draftValueKeys = list(draftValueperTeam.keys())
        draftValueValues = list(draftValueperTeam.values())
        pickNumber = pick[n]
        value = diccPicks[pickNumber]
        t = team[n]
        if t not in draftValueKeys:
            draftValueperTeam[t] = value
        else:
            before = draftValueperTeam[t]
            newValue = before + value
            draftValueperTeam[t] = newValue
    pctsDic = {}
    pctsTeam = []
    for n in range(0, 31):
        pcts = []
        t = letters[n]
        for item in diccStandings:
            item_lst = list(item)
            item_lst.remove(item_lst[0])
            item_lst.remove(item_lst[0])
            item_lst.remove(item_lst[0])
            item_lst.remove(item_lst[0])
            i = "".join(item_lst)
            if t == i:
                pct = diccStandings[item]
                pcts.append(pct)
        avg = (sum(pcts))/len(pcts)
        pctsTeam.append(avg)
        pctsDic[t] = avg
    return pctsDic, draftValueperTeam


def showResults(teamAvgPct, teamDraftValue, param):
    file = open("resultsPct.csv", 'w')
    file2 = open('resultsDraft.csv', 'w')
    teamsPct = []
    pctList = []
    for team in teamAvgPct:
        file.write(team)
        file.write(" ")
        file.write(str(teamAvgPct[team]))
        file.write("\n")
    for team in teamDraftValue:
        file2.write(team)
        file2.write(" ")
        file2.write(str(teamDraftValue[team]))
        file2.write("\n")


    print(teamsPct)
    print(pctList)


def main():
    diccPicks = getPicksValue()
    diccStandings = getStandings()
    team, pick, college = getTeamPicks()
    colleges_Single = getSingleCollegesList(college)
    teamAvgPct, teamDraftValue = getAverageTeamPctanDrafts(diccStandings, diccPicks, team, pick)
    showResults(teamAvgPct, teamDraftValue, getAssocNamesLetters(diccStandings))
    print(college)
    print(colleges_Single)
    print("Performance: \n", teamAvgPct, "\nDraftValue: \n", teamDraftValue)



main()