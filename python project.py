import random
answerlist=["world","look","hello","goodbye"]
random.shuffle(answerlist)
answer = list(answerlist[0])

#print answer

#empty list called display
display = []

#this will contain used letters
used = []

#adds variable answer to display
display.extend(answer)

#adds what is in display the answer to used
used.extend(display)


for i in range (len(display)):
    #to replace each index with '_'
     display[i]="_"
     
#the join command puts a space between each '_'
print (' '.join(display))
print()

#counter stops once all letters guessed
count=0

incorrect=5

#keeps asking until all letters guessed
while count<len(answer) and incorrect>0:
    guess=input("please guess a letter: ")
    guess=guess.lower()
    print(count) 

    #iterates through letter in answer
    for i in range(len(answer)):
        if answer[i]==guess and guess in used:
        #replace index of guess with letter they guessed
           display[i]=guess
           count=count + 1

           #print(used)
           used.remove(guess)
        
    if guess not in display:
        incorrect=incorrect-1
        print("sorry,wrong guess.You have",incorrect,"chances left")
    print("you have guessed: ",count,"correct letters.")
    print("you have",incorrect,"chances left")
      

    print(' '.join(display))
    print()
    
if count==len(answer):
    print("well done you guessed the word")

else:
    print("unfortunately you ran out of chances")

   
