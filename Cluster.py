import csv

def getPicksValue():
    file = open('draft_values.csv', 'r')
    reader = csv.reader(file, skipinitialspace=True)
    values = {}
    for row in reader:
        values[(row[0])] = (row[2])
    values.pop('pick')
    file.close()
    return values


def getStandings():
    file = open('standings.csv', 'r')
    reader = csv.reader(file, skipinitialspace=True)
    standings = {}
    for row in reader:
        fullTeam = row[0] + row[3]
        standings[fullTeam] = row[7]
    file.close()
    return standings


def getTeamPicks():
    file = open('teamPicks.csv', 'r')



def main():
    diccPicks = getPicksValue()
    diccStandings = getStandings()
    diccTeamPicks = getTeamPicks()

main()