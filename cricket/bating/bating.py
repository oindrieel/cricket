import random


def anticheat(player_run, bot_run):
    if player_run > 10:
        return bot_run
    else:
        return player_run


def bating_innings_1():
    y = "y"
    total_run = 0
    while y == "y":
        bot_run = random.randrange(1, 11)
        player_run = int(input("Enter your run: "))
        player_run_verified = anticheat(player_run, bot_run)
        if player_run_verified != bot_run:
            total_run += player_run_verified
            print("########################################")
            print("Your run:", player_run_verified)
            print("Bot run", bot_run)
            print("Total run:", total_run)
            print("Status: NOT OUT")
            print("########################################")
            y = "y"
        else:
            print("########################################")
            print("Your run:", player_run_verified)
            print("Bot run", bot_run)
            print("Total run:", total_run)
            print("Status: OUT")
            print("########################################")
            y = "n"
    return total_run


def bating_innings_2(run):
    y = "y"
    total_run = 0
    required_run = run
    while y == "y":
        bot_run = random.randrange(1, 11)
        player_run = int(input("Enter your run: "))
        if bot_run != player_run:
            total_run += player_run
            required_run -= player_run
            print("########################################")
            print("Your run:", player_run)
            print("Bot run", bot_run)
            print("Total run:", total_run)
            print("Required run:", required_run)
            print("Run scored in first innings:", run)
            print("Status: NOT OUT")
            print("########################################")
            if total_run > run:
                y = "n"
                return "player"
        else:
            print("########################################")
            print("Your run:", player_run)
            print("Bot run", bot_run)
            print("Total run:", total_run)
            print("Required run:", required_run)
            print("Run scored in first innings:", run)
            print("Status: OUT")
            print("########################################")
            if total_run > run:
                y = "n"
                return "player"
            else:
                y = "n"
                return "bot"
