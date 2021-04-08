
from collections import defaultdict

def findWinner(votes, pref="first"):
    if not votes:
        return None

    max_votes, candidate = 0, votes[0]
    vote_counter = defaultdict(int)
    
    for vote in votes:
        vote_counter[vote] += 1
        if vote_counter[vote] > max_votes:
            max_votes = vote_counter[vote]
            candidate = vote
        
        if pref == "last" and vote_counter[vote] >= max_votes:
            candidate = vote


    return candidate




def pass_test_multiple():
    votes = ["A", "B", "A", "B", "D", "B", "A"]
    ans = findWinner(votes)
    assert ans == "B"


def pass_test_single():
    votes = ["A", "B", "A", "C", "D", "B", "A"]
    ans = findWinner(votes)
    assert ans == "A"


def pass_test_multiple_2():
    votes = ["A", "B", "A", "B", "D", "B", "A"]
    ans = findWinner(votes, pref="last")
    assert ans == "A"


def pass_test_single_2():
    votes = ["A", "B", "A", "C", "D", "B", "A"]
    ans = findWinner(votes, pref="last")
    assert ans == "A"





pass_test_multiple()
pass_test_single()
pass_test_multiple_2()
pass_test_single_2()


# [["A","B","C"],["C","D","B"]]
# A - 3, B - 3, C - 4, D - 2

def findWinner2(votes, pref=None, max_first=False):
    if not votes:
        return None

    max_votes, candidate = 0, votes[0]
    vote_counter = defaultdict(int)
    first_place_counter = defaultdict(int)

    for row in votes:
        for ind, cand in enumerate(row):
            if ind == 0:
                first_place_counter[cand] += 1

            vote_counter[cand] += 3 - ind

            if vote_counter[cand] > max_votes:
                max_votes = vote_counter[cand]
                candidate = cand

            if pref and pref == "last" and vote_counter[cand] >= max_votes:
                candidate = cand

    if max_first:
        candidates_with_max_votes = []
        for cand, votes in vote_counter.items():
            if votes == max_votes:
                candidates_with_max_votes.append(cand)

        candidate = candidates_with_max_votes[0]
        first_place_count = first_place_counter[candidate]
        for cand in candidates_with_max_votes:
            if first_place_counter[cand] > first_place_count:
                candidate = cand
                first_place_count = first_place_counter[cand]


    return candidate
            



def pass_test_single_winner_2():
    votes = [["A","B","C"],["C","D","B"]]
    ans = findWinner2(votes)
    print(ans)
    assert ans == "C"


def pass_test_multiple_winner_2():
    votes = [["A","B","C"],["D","C","B"]]
    ans = findWinner2(votes)
    print(ans)
    assert ans == "A"


def pass_test_multiple_winner_2_last():
    votes = [["A","B","C"],["D","C","B"]]
    ans = findWinner2(votes, pref="last")
    print(ans)
    assert ans == "B"




pass_test_single_winner_2()
pass_test_multiple_winner_2()
pass_test_multiple_winner_2_last()



def pass_test_single_winner_2_max_first():
    votes = [["A","B","C"],["D","C","B"]]
    ans = findWinner2(votes, max_first=True)
    print(ans)
    assert ans == "A"


def pass_test_single_winner_2_max_first_false():
    votes = [["A","B","C"],["D","C","B"]]
    ans = findWinner2(votes, pref="last", max_first=False)
    print(ans)
    assert ans == "B"


def pass_test_single_winner_2_max_first_true():
    votes = [["A","B","C"],["D","C","B"],["B", "D", "A"]]
    ans = findWinner2(votes, max_first=True)
    print(ans)
    assert ans == "B"



pass_test_single_winner_2_max_first()
pass_test_single_winner_2_max_first_false()
pass_test_single_winner_2_max_first_true()