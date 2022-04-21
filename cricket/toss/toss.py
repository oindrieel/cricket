import random


def check(player_run):
    if player_run > 10:
        return 0


def toss():
    print("TOSS")
    bot_choice = random.choice(["bating", "bowling"])
    bot_run = random.randrange(0, 11)
    player_run = int(input("Enter your run: "))
    player_choice = input("heads/tails: ")
    player_toss = input("bating/bowling: ")
    total_run = (player_run + bot_run) % 2
    if player_choice == "heads":
        if total_run != 0:
            return "player", player_toss
        else:
            return "bot", bot_choice
    else:
        if total_run == 0:
            return "player", player_toss
        else:
            return "bot", bot_choice
