from cricket.toss import toss
from cricket.bowling import bowling
from cricket.bating import bating

toss_player, toss_result = toss.toss()
if toss_player == "player" and toss_result == "bating":
    print("now you are bating")
    run = bating.bating_innings_1()
    print("now you are bowling")
    winner = bowling.bating_innings_2(run)
elif toss_player == "player" and toss_result == "bowling":
    print("now you are bowling")
    run = bowling.bowling_innings_1()
    print("now you are bating")
    winner = bating.bating_innings_2(run)
elif toss_player == "bot" and toss_result == "bating":
    print("now you are bowling")
    run = bowling.bowling_innings_1()
    print("now you are bating")
    winner = bating.bating_innings_2(run)
else:
    print("now you are bating")
    run = bating.bating_innings_1()
    print("now you are bowling")
    winner = bowling.bating_innings_2(run)
if winner == "player":
    print("Congratulations!, you won")
else:
    print("Better luck next time")
