import re
from collections import Counter

#A function to find all the words in a file
def fn1(str):
    return re.findall(r'\w+',str.lower())

#A counter will count the frequency of the words and store it in a key-value pair
#We have over a million words in big.txt
dict=Counter(fn1(open('big.txt').read()))

#A function to reurn probability of a word
def Prob(word):
    n=sum(dict.values())
    return dict[word]/n

#A menu-driven program
char=input('Do you wish to check the most frequently occuring words in our database(Y/N)? :) ')

if(char.lower()=='y'):
    num=int(input('Enter the number upto which you want the most frequently occuring words: '))
    print("WORD    PROBABILITY")
    
    for i in range(0,num):
        #most_common method stores the most common word in a list of tuples, a bit like 2D array
        #Refer link https://docs.python.org/2/library/collections.html
        print(dict.most_common(num)[i][0],"   ",Prob(dict.most_common(num)[i][0])) 
else:
    #Code for correcting the spelling goes here
    print('OkBye :(')
    
print('Okay Bye. Have a nice day.')


