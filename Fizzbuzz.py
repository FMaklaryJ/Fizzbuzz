#This code is to solve a game called FizzBuzz.
#Rules are as follows:
#Person/program starts counting up from 1.
#Whenever a number is divisible with 3, the program says "Fizz" in stead of the number.
#Whenever a number is divisible with 5, the program says "Buzz".
#If the number is divisible with both 3 and 5, the program says "FizzBuzz."
#That's it.

#The idea is to demonstrate how a coder thinks when making a project.

#For instance, one could make two cases where it only checks for mod 3 and 5,
#or one could generalise it to make it easily adaptable to changes in the game,
#in case somebody wanted to change the rules to FizzBuzzGlork,
#or maybe somebody wanted to start with negative numbers in stead.
#What precautions somebody takes when programming reflects the way they think.


import time #Libraries
import numpy as np

j=0 #Initial condition for counting

numlist=np.array([3,5]) #list of numbers to be replaced with words
stringlist=np.array(['Fizz','Buzz']) #list of words
while 1==1:
    j+=1
    string=str(j) #Default string to be printed if no number is to be replaced
    string2='' #String to be manipulated if number should be replaced
    
    for i in range(numlist.size): 
        if j % numlist[i] == 0:#Checks modulus of number
            string2+=stringlist[i] #Appends word to string2
            string=string2 #Sets string to be printed
    
    print(string+'\n') #Prints string
    time.sleep(0.5) #Waits for 0.5 seconds
