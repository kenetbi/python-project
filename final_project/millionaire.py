#Who wants to be a millionaire?
import time

is_playing = True
score = 0
winnings = 0

questions = [{"question": "Which planet is known as the Red Planet?", "choices": ["A: Venus", "B: Mars", "C: Jupiter", "D: Saturn"], "answer": "B", "prize": 50000},
             {"question": "What is the chemical symbol for Gold?", "choices": ["A: Ag", "B: Au", "C: Al", "D: As"], "answer": "B", "prize": 100000},
             {"question": "Which of these artists painted the Mona Lisa?", "choices": ["A: Vincent van Gogh", "B: Pablo Picasso", "C: Leonardo da Vinci", "D: Claude Monet"], "answer": "C", "prize": 150000},
             {"question": "What is the capital of France?", "choices": ["A: London", "B: Berlin", "C: Paris", "D: Madrid"], "answer": "C", "prize": 200000},
             {"question": "How many continents are there?", "choices": ["A: 5", "B: 6", "C: 7", "D: 8"], "answer": "C", "prize": 500000}]

print("======================================================================================")
print("                       Welcome to Who Wants to Be a Millionaire!")
print("======================================================================================")

print("You will be asked a series of questions. Each correct answer will increase your score.")
print("You can choose to walk away at any time by entering 'W'.")
print("Let's get started!")
print("---------------------------------------------------------------------------------------")
print("")


while is_playing and score < len(questions):
    print(f"Question {score + 1}:")
    print(questions[score]["question"])
    print(questions[score]["choices"])

    while True:
        answer = input("Choose your answer (A, B, C, D) or W(Walk Away): ").upper()

        if answer not in ["A", "B", "C", "D", "W"]:
            print("Invalid input! Please enter A, B, C, D or W.")
            print("")
            continue
        elif answer == "W":
            print("You chose to walk away. Game over.")
            is_playing = False
            break
        
        correct_confirmed = False

        while True:
            confirm = input(f"\nYou chose {answer}. Is that your final answer? (Y/N): ").upper()

            if confirm not in ["Y", "N"]:
                print("Invalid input! Please enter Y or N.")
                print("")
                continue
            elif confirm == "Y":
                print("Answer confirmed.")
                print("")
                time.sleep(2)
                if answer == questions[score]["answer"]:
                    print("Correct! The right answer is:", questions[score]["answer"])
                    winnings += questions[score]["prize"]
                    score += 1
                    correct_confirmed = True
                    print(f"Your winnings are now: ${winnings}\n")
                    break
                else:
                    print("Wrong answer! Game over.")
                    is_playing = False
                    winnings /= 2
                    break
            else:
                print("Answer not confirmed. Please choose again.")
                print("")
                break
        if not is_playing or correct_confirmed:
            break
        
if score == len(questions):
    print(f"Your final score is: {score} out of {len(questions)}")
    print("Congratulations! You've answered all questions correctly and won the game!")
    print("You are a millionaire! Enjoy your winnings!")
else:
    print(f"Your final score is: {score} out of {len(questions)}\nYou are a millionaire in spirit! Better luck next time!")

print(f"Your total winnings are: ${winnings}\n")