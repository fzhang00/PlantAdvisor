# Animal Quiz by Zhang Lao Shi

def check_guess(guess, correct_answer):
    """Check player's answer, and offer three chances total"""
    global score
    still_guessing = True
    if guess.lower() == correct_answer.lower():
        still_guessing = False
        score = score + 1

    # offer two more chances:
    attempts = 1
    while still_guessing and attempts<3:
        print("You have tried ", attempts, " times")
        guess = input("Try again! ")
        attempts = attempts + 1
        if guess.lower() == correct_answer.lower():
            still_guessing = False
            score = score + 1
    # At this point, player has either answered the correct answer,
    # or has used up all three chances. Give them proper response.
    if attempts == 3 and still_guessing: # player has used all three chances
        print("The correct answer is :", correct_answer)
    else:
        print("Bingo!")

# main program
questions = [
    "What's the biggest ocean on earth? ",
    "What the name of the planet that has life on it in this solar system",
    "What is the biggest planet in our solar system?",
]
answers = ["Pacific", "Earth", "Jupiter"]
score = 0
for i in range(len(questions)):

    guess = input(questions[i])
    check_guess(guess, answers[i])

print("You score is ", score)

# Want to make it harder?
# 1. Add more questions
# 2. Ask question randomly
#

