# PsifosPoll: Library for Election Result Algorithms
PsifosPoll is a Python library developed by the electronic voting system Psifos team. For more information about our work, visit the Psifos Participa UChile instance page: [Psifos Participa UChile](https://participa.uchile.cl/).

## Description
PsifosPoll is a Python library designed to contain different algorithms for calculating the result of an election. Currently, the library includes the algorithm for preferential ranking voting, Single Transferable Vote (STV), in its Weighted Inclusive Gregory Method version with a droop quota.

## Resources
- STV Versions: For more information about different versions of STV, it is recommended to consult the paper "DETERMINING THE RESULT: Transferring Surplus Votes in the Western Australian Legislative Council."

- PsifosPoll Implementation: If you want to learn more about the version of STV implemented by this library, we suggest reviewing the paper "Shuffle-Sum: Coercion-Resistant Verifiable Tallying for STV Voting" in section I.c.

## Installation
You can install PsifosPoll using the pip package manager. Run the following command in your terminal:
```
bash
Copy code
pip install psifospoll
Usage Example
Here is a basic example of how to use PsifosPoll with STV:

python
Copy code
from psifospoll import STVElection

def stvTally(s, candidates_list, ballot_list):
    election = STVElection()
    election.runElection(s, candidates_list, ballot_list)
    print(election.getRoundResumes())
    print(election.getTalliesResumes())
    print(election.getWinnersList())

# Voting example
l1 = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 1],
    [3, 4, 5, 1, 2],
    [4, 5, 1, 2, 3],
    [1, 2, 3, 4, 5],
]
cand = [1, 2, 3, 4, 5]
stvTally(3, cand, l1)
```
In this example, STV runs for 3 rounds, and candidates 1, 3 and 4 are elected.

## More Examples
You can find more examples of possible inputs for STV in the examples.py file of the library.

## Contributions
We would love to receive contributions! If you want to make a Pull Request (PR), make sure the code used is formatted with the black library. You can do this by running the following command in the PsifosPoll directory:
```
black .
```

## Contact
If you have any questions, feel free to contact us at participa@uchile.cl.

Thank you for using PsifosPoll!
