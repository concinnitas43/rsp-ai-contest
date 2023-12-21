from enum import Enum, auto

class Hand(Enum):
    R = auto()
    P = auto()
    S = auto()
    
def succ(hand: Hand) -> Hand:
    if hand == Hand.R:
        return Hand.P
    elif hand == Hand.P:
        return Hand.S
    else:
        return Hand.R

def pred(hand: Hand) -> Hand:
    if hand == Hand.R:
        return Hand.S
    elif hand == Hand.P:
        return Hand.R
    else:
        return Hand.P

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


def flip(hist: History) -> History:
    return [(match[1], match[0]) for match in hist]
