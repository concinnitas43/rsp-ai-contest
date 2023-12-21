from enum import Enum, auto

class Hand(Enum):
    R = auto()
    P = auto()
    S = auto()
    

Match = (Hand, Hand)

def evaluate(match: Match) -> int:
    if match[0] == match[1]:
        return 0
    elif match[0] == Hand.R and match[1] == Hand.S:
        return 1
    elif match[0] == Hand.P and match[1] == Hand.R:
        return 1
    elif match[0] == Hand.S and match[1] == Hand.P:
        return 1
    else:
        return -1 

History = list[Match]

