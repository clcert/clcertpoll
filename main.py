from src import STVElection


def stvTally(s, candidates_list, ballot_list):
    election = STVElection()
    election.runElection(s, candidates_list, ballot_list)
    print(election.getRoundResumes)
    print(election.getTalliesResumes)
    print(election.getWinnersList)


l1 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]
cand = [1, 2, 3, 4, 5]
stvTally(3, cand, l1)
