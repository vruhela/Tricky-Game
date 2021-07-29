print("Hello Welcome to the game Tricky Questions. Try answering The questions correct about your family and check your thinking with your family.. So, Let's get started")
ans = (input("So,are you ready to pay this game (type yes/no):"))
score = 0
total_q = 5

if ans == 'no':
    quit()
    
if ans == 'yes':
    print("mark for each question is +100")
    
    
a=str(input("So,Let's get started. Our First question to you is that What is Vedansh's favourite Subject in School?"))
if a=='Maths':
    score += 1
    print("That's Correct!")
elif a== 'Math':
    score += 1
    print("That's Correct!")
elif a== 'math':
    score += 1
    print("That's Correct!")
elif a== 'maths':
    score += 1
    print("That's Correct!")     
else:
    print("That's InCorrect!")
    print(" The Correct Answer is:- maths")

print("Next question to you is:-")
c=str(input("2:- What is Vedansh's Favourite Sport?"))
if c== 'Cricket':
     score += 1
     print("That's Correct!")
elif c== 'cricket':
    score += 1
    print("That's Correct!")
elif c== 'table tennis':
    score += 1
    print("That's Correct!")
elif c=='Table Tennis':
    score += 1
    print("That's Correct!")
elif c== 'Table tennis':
    score += 1
    print("That's Correct!")
elif c== 'TT':
    score += 1
    print("That's Correct!")
elif c== 'tt':
    score += 1
    print("That's Correct!")    
else:
    print("That's Incorrect!")
    print("The Correct Answer is Cricket or you can say Table Tennis ")

b=str(input("3:- What is Vedansh's favourite food?"))
if b== 'Chole Bhature':
    score += 1
    print("That's Correct!")
elif b== 'chole bhature':
    score += 1
    print("That's Correct!")
elif b== 'Chole bhature':
    score += 1
    print("That's Correct!")
elif b== 'chole Bhature':
    score += 1
    print("That's Correct!")     
else:
     print("That's Incorrect!")
     print("The Correct Answer is:- Chole Bhature")

d=str(input("4:- What is vedansh's Passion?"))
if d== 'Computing':
    score += 1 
    print("That's Correct!")
elif d== 'Learning Computer':
    score += 1
    print("That's Correct!")
elif d== 'Learning':
    score += 1
    print("That's Correct!")    
elif d== 'computing':
    score += 1
    print("That's Correct!")
elif c== 'Linux':
    score += 1
    print("That's Correct!")
elif d== 'Learning Linux':
    score += 1
    print("That's Correct!")    
else:
    print("That's Incorrect!")
    print("The Correct Answer is Computing,Learning,Learning Linux,Linux,Learning Computer")

e=str(input("5:- In which sector do Vedansh want to go in future?"))
if e== 'IT Sector':
    score += 1
    print("That's Correct!")
elif e== 'IT':
    score += 1
    print("That's Correct!")
elif e== 'IAS Sector':
    score += 1
    print("That's Correct!")
elif e== 'IAS':
    score += 1
    print("That's Correct!")
elif e== 'it':
    score += 1
    print("That's Correct!")
else:
    print("That's Incorrect!")
    print("The Correct Answer is IT or can be IAS")

print('Thanks a lot for playing this game. You got',score,"questions correct.")
mark = (score/total_q) * 100
print("Mark: ", mark)
print("Good Bye")


    
    
    

    

    


    
