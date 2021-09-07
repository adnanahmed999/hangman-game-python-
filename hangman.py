
print("Lets Play HANGMAN ;) ")
word="1"   #putting it 1 for now to perform next command
while all(i.isalpha() or i.isspace() for i in word)==False:  #to check there are no special symbols and numbers (spaces allowed)
    word=input("Input the Sentence or Word (only alphabets): ")
word_list=list(word)  #covert string to list,each letter of word is element of list
for i in range(len(word_list)):
    if word_list[i]==" ":
        word_list[i]="-"  #replacing spaces by -
blanks_to_fill=[]        #to print blanks with words correctly guessed
letters_not_in_word=[]   #to print letters which are not in word if guess is wrong
letters_done=[]          #letters which are guessed
counter=0                #counter to draw hangman

def initial_blanks():
    for i in word:
        if i==" ":
            blanks_to_fill.append(" ")
        else:
            blanks_to_fill.append("_")   #to draw blanks initially i.e only underscores and spaces

def print_list(any_list):
    for i in any_list:
        print(i,end=" ")
    print() #to print each element of any_list (argument)

#the below functions are to draw respective parts of hangman and corresponding ROW

def stand_hinge():
    print(" ",end="")
    for j in range(7):
        print("_",end="")
    print()
    print(" |",end="")
    for j in range(5):
        print(" ",end="")
    print("|")

def stand_base():
    for j in range(7):
        print(" ",end="")
    print("^")

def man_face():
    print(" O",end="")
    for j in range(5):
        print(" ",end="")
    print("|")

def both_hands():
    print("\|/",end="")
    for j in range(4):
        print(" ",end="")
    print("|")

def man_chest():
    print(" |",end="")
    for j in range(5):
        print(" ",end="")
    print("|")

def left_hand():
    print("\|",end="")
    for j in range(5):
        print(" ",end="")
    print("|")

def left_leg():
    print("/",end="")
    for j in range(6):
        print(" ",end="")
    print("|")

def both_legs():
    print("/ \\",end="")
    for j in range(4):
        print(" ",end="")
    print("|")

def spaces_and_single_line(X):
    for k in range(X):
        for j in range(7):
            print(" ",end="")
        print("|")

def show_hanging():
    global counter

    if counter==0:
        stand_hinge()
        spaces_and_single_line(5)
        stand_base()

    if counter==1:
        stand_hinge()
        man_face()
        spaces_and_single_line(4)
        stand_base()

    if counter==2:
        stand_hinge()
        man_face()
        man_chest()
        spaces_and_single_line(3)
        stand_base()

    if counter==3:
        stand_hinge()
        man_face()
        man_chest()
        man_chest()
        spaces_and_single_line(2)
        stand_base()

    if counter==4:
        stand_hinge()
        man_face()
        left_hand()
        man_chest()
        spaces_and_single_line(2)
        stand_base()

    if counter==5:
        stand_hinge()
        man_face()
        both_hands()
        man_chest()
        spaces_and_single_line(2)
        stand_base()

    if counter==6:
        stand_hinge()
        man_face()
        both_hands()
        man_chest()
        left_leg()
        spaces_and_single_line(1)
        stand_base()

    if counter==7:
        stand_hinge()
        man_face()
        both_hands()
        man_chest()
        both_legs()
        spaces_and_single_line(1)
        stand_base()
        print("the Man is hanged")

    counter=counter+1  #increase counter for next chance

def guess_check(guess):
    letters_done.append(guess)  #append the guessed letter in this list
    if guess in word_list:   #if guessed letter in word_list
        print()    #just for neatness
        print()
        print("###### Found :) ######")
        for i in range(len(word_list)):  #match with each element to search
            if guess==word_list[i]:
                word_list[i]="-"   #replace the letter in "word_list" by -, so that the same letter is not there again
                blanks_to_fill[i]=guess    #replace the blank by that letter
    else:
        print()
        print()
        print("!!!!! Not Found :( !!!!!")
        letters_not_in_word.append(guess)  #if guess wrong, append it seperately to show letters not in word
        show_hanging() #each time word not found, print hanman according to value in counter

def check_if_to_continue():
    check=0   #this function returns 0 if the whole word is found, i.e all letters in word_list replaces by - (according to guess check function)
    for i in word_list:
        if i!="-":   #if any of the letter is not found, return 1
            check=1
    return check

def guess_a_letter():
    while check_if_to_continue()==1 and counter<=7:  #counter=8 means man hanged
        print()
        print()
        print("******Next Attempt*****")
        print_list(blanks_to_fill)
        print("letters u discover not in word:= ",end=" ")
        print_list(letters_not_in_word)

        guess=""
        while len(guess)!=1 or guess in letters_done or guess.isalpha()!=True: #to check guess should be single letter and alphabets only
            guess=input("Guess a Single Letter : ")
            if guess in letters_done:
                print()
                print("Letter already Guessed")
                print()

        guess_check(guess)
    print_list(blanks_to_fill)
    print()

show_hanging()    #show hangman without man (initial condition)
initial_blanks()  #show underlines to fill with spaces if sentence
guess_a_letter()  #begin the game

if(check_if_to_continue()==0 and counter<=8): #at last after man hanged, counter will be incremented, hence 8
    print("Conrats you saved the Man!!! Game Won")
elif(check_if_to_continue()==1 and counter==8):
    print("Game Lost, The word is ","(",word,")","Better luck next time" )
