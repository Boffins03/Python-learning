def minion_game(S):
    S = S.strip().upper()
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0

    # Count substrings starting with each letter
    for i in range(len(S)):
        print(S[i])
        if S[i] in vowels:
            kevin_score += len(S) - i
            print(f"kevin_score-{kevin_score}")
        else:
            stuart_score += len(S) - i
            print(f"stuart_score-{stuart_score}")

    # Determine the winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)