import time
import random

score = int(0)

with open ('usr.txt', 'w') as scorea:
    scorea.write("0")

qcount = int(0)

while qcount < 5:
    with open('questions.txt', 'r') as que:
        questions = que.readlines()

    random_line_number = random.randint(0, len(questions) - 1)

    random_question = questions[random_line_number].strip()

    print(f"Question: {random_question}")


    with open('answers.txt', 'r') as ans:
        answers = ans.readlines()

    ansreal = answers[random_line_number].strip()

    usrinp = str(input("your answer:"))
    if usrinp.lower() == ansreal.lower():
        print("correct")
        score = score+1
        qcount = qcount+1
        with open ('usr.txt', 'w') as scorea:
            scorea.write(str(score))
        print(score)

    else:
        print(f"Nope the answer is: {ansreal}")
        qcount = qcount+1
        print(score)

#some code here is taken from a python stack exchange specifically line 44 and 59 because i didnt want to bother with any other solution
with open ('usr.txt', 'r') as scorech:
    check2 = scorech.readlines()
    check = ''.join(char for char in check2 if char.isalnum())
    print("\n\n_____________________________________\n\nThis is your score:", check)

if str(check) == str(score):
    with open ('hig.txt', 'r') as higsc:
        highscore2 = higsc.readlines()
        num8 = len(highscore2)
        if num8 < 1:
            highscore2 = 0
            if score > 0:
                with open ('hig.txt', 'w') as writehigscq:
                    score2 = str(score)
                    writehigscq.write(score2)
                    print("\n\nNew highscore!")
        elif num8 >= 1:
            highscore = ''.join(char for char in highscore2 if char.isalnum())
            if int(highscore) < int(score):
                with open ('hig.txt', 'w') as writehigsc:
                    score3 = str(score)
                    writehigsc.write(score3)
                    print("\n\nNew highscore!")
    


else:
    print("you cheated")

highscoreclear = input("\n\nDo you want to reset your highscore? (y/n): ")

if highscoreclear == "y":
    with open ('hig.txt', 'w') as clrhigscq:
                    clrhigscq.write("0")
                    print("\nScore cleared")
            
else:
     print("\n highscore kept")

print("\nrestart by clicking the play button")

 # type: ignore
