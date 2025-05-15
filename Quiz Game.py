print("Welcome to Quiz Game!")
a=input("Do you wanna play?").lower().strip()
if(a!="yes"):
    quit()
print("Okayyy!, Let's Play")
print("What does CPU stand for?")
c=0
a1=input("Type your answer").lower().strip()
if(a1=="central processing unit"):
    print("Correct")
    c=c+1
else:
    print("Oops!Incorrect")
print("What does GPU stand for?")
a2=input("Tye Your Answer").lower().strip()
if(a2=="graphics processing unit"):
    print("Correct")
    c=c+1
else:
    print("Incorrect")
print("What does RAM stand for?")
a3=input("Type your Answer").lower().strip()
if(a3=="random access memory"):
    print("Correct")
    c=c+1
else:
    print("incorrect")
print("What does IP stand for?")
a2=input("Tye Your Answer").lower().strip()
if(a2=="internet protocol"):
    print("Correct")
    c=c+1
else:
    print("Incorrect")
print("What does AI stand for?")
a2=input("Tye Your Answer").lower().strip()
if(a2=="artifical intelligence"):
    print("Correct")
    c=c+1
else:
    print("Incorrect")

print("Done with the Game")
print("Now,lets check your marks")
print("You got",c,"question correct")
print("Your Percentage=",(c/5)*100)

