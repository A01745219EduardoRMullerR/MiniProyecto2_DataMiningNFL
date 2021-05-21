import csv

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
    collegeValue = {}
    teamPicks = {}
    for row in reader:
        collegeValue[row[-1]] = int(row[2])
        teamPicks[row[4]] = int(row[2])
    return teamPicks, collegeValue


def getColleges(diccPickCollege):
    colleges = []
    for key in diccPickCollege:
        colleges.append(key)
    return colleges


def main():
    diccPicks = getPicksValue()
    diccStandings = getStandings()
    diccTeamPicks, diccPickCollege = getTeamPicks()
    colleges = getColleges(diccPickCollege)
    print(diccPicks)
    print(diccStandings)
    print(diccTeamPicks)
    print(diccPickCollege)
    print(colleges)



main()