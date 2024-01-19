from psifospoll import STVElection


def stvTally(s, candidates_list, ballot_list):
    election = STVElection()
    election.runElection(s, candidates_list, ballot_list)
    print('round resumes', election.getRoundResumes())
    print('tallies resumes', election.getTalliesResumes())
    print('winners list', election.getWinnersList())
    print('quota', election.getQuota())


l1 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]
cand = [1, 2, 3, 4, 5]
stvTally(3, cand, l1)
