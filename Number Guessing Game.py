import random
guesses=0
start=int(input("Enter the Range"))
    
if start<=0:
    print("Try a number greater than zero")
    quit()
else:
    pass

randomnumber= random.randint(1,start)
while True:
  guesses=guesses+1
  uguess=int(input("Guess a number"))

  if uguess<=0:
       print("try a number greater than zero,next time")
       quit()
  else:
    pass

  if(uguess==randomnumber):
      print("You Got it Right")
      break
  else:
       print("You Got it Wrong!")
      
print("The Number of guesses : ",guesses)
