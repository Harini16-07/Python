#Hangman

import random
print("Hey,Welcome to Hangman!")
fruits=["apple","banana","mango","strawberry","blurberry","kiwi","pineapple","papaya","cherry","peach","orange","grapes"]
while True:
  ran=random.choice(fruits)
  chances=len(ran)+2
  guess=""
  start=input("Do you wanna play? y/n").lower().strip()
  if(start=="n"):
        print("Thank you for playing")

        quit()
  elif(start != "y"):
        print("Invalid,choose y or n")
    
  print("HINT: Its a name of a fruits")
  print("Number of letters are:",len(ran))

  while chances>0:
    failed=0
    for char in ran:
       if char in guess:
        print(char,end="")
       else:
          print("_",end="")
          failed=failed+1
    print()

    if failed==0:
       print("You won")
       break
    
    user=input("Enter a character : ").lower().strip()

    guess+=user

    
    if user not in ran:
       chances=chances-1
       print("Wrong")
       
       
    if chances==0:
        print("oops!Your dead")
        print("The word was",ran)
       
    
       
    

    