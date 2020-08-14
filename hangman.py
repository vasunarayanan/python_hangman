import random
word_list=['apple', 'banana', 'orange', 'grape', 'plum', 'strawberry']
word=random.choice(word_list)
len_word=len(word)
print("_ " *(len_word))
i=0
turns=10
guessed=[None]*len_word

for y in range(turns):
        guess=input("enter a guess \n")
        
        
        for x in range(len(word)):
                if guess==word[x]:
                        guessed[x]=guess
                        i=i+1
                        print(guessed)
                        
                if i==len(word):
                        print("You Win")
                        exit()
                
                if guess not in word:
                        print("try again")         
        
        
                      
        left_turns=(int(turns)-int(y))
        message='You have %s turns left'
        print(message % left_turns)
                    
        




