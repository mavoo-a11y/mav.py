questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs ?: ",
             "What is the most abundant gas in Earth ?: ",
             "How many bones are in a human body ?: ",
             "Which planet in the solar system is the biggest ?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. earth", "C. Neptune", "D. Jupiter"))

answers = ("C", "D", "A", "A", "D" )
guesses = []
score = 0
question_num = 0

for question in questions:
   print("-----------------------")
   print(question)
   for option in options[question_num]:
       print(option)

   guess = input("Enter (A, B, C, D): ").upper()
   guesses.append(guess)
   if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
   else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer ")
   question_num += 1

# print("Correct answers: ", end= " ")

for answer in answers:
                print(answer, end=" ")
                print()
                print("guesses: ", end=" ")

             
score_percent = int(score / len(questions) * 100)
print (f"Your score is {score_percent}%")
