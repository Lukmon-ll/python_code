Playing = input("Are you interested in playing a game ")
if(Playing.lower() == "yes"):
    print("Common lets play")
else:
    quit()
    
score = 0
name = input("Enter your first name to begin ")
answer = input("What does CPU stand for ")
if answer.lower() == "central processing unit":
    print("That's correct")
    score += 1
else:
    print("Incorrect answer")

answer = input("What does RAM stand for ")
if answer.lower() == "random access memory":
    print("That's correct")
    score += 1
else:
    print("Incorrect answer")

answer = input("What does IOT stand for ")
if answer.lower() == "internet of things":
    print("That's correct")
    score += 1
else:
    print("Incorrect answer")

answer = input("What does WWW stand for ")
if answer.lower() == "world wide web":
    print("That's correct")
    score += 1
else:
    print("Incorrect answer")

print(name + " You got " + str(score) + " questions correct")



