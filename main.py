'''
Display of dictionary functions in Python 3
Created by Synda Simmers
'''

import random


    
#function to display current selection 
def disp_selection():
    for key, value in my_dict.items():
        print(key, ", ", value , "genre.")
    return "End of list"
 
#function to make a donation
def make_dono():
    re_dono = True
    while re_dono == True:
        
        print("What is the title of the book?")
        title = str(input())
        print("What is the genre? 1: Horror, 2: Non-fiction, 3: Romance, 4: Action.")
        genre = int(input())
        my_dict[title]= (genre_dict[genre])
        print(my_dict)
        print("Thank you for your donation, would you like to make another? (Y/N)")
        ans = str(input())
        re_dono = yes_no(ans)
        
                
    print("Any entered titles have been added.")
    
#Function for handling checkouts
def check_out():
    re_check = True 
    while re_check == True:
        print("Would you like to select a book by 1: title or 2: by random?")
        genre_ans = int(input())
        if genre_ans == 1:
            print("The selections are:")
            for key in my_dict.keys():
                print(key)
            err_check = False
            while err_check == False:
                print("Which would you like?")
                selection = str(input())
                if selection in my_dict: 
                    my_dict.pop(selection)
                    print("Okay, that has been checked out for you.")
                    err_check = True
          
                else: 
                    print("That is not a title in our library, please try again.")
            
            
        elif genre_ans == 2:
            print("How spontaneous. The book that has been selected is: ")
            key_check = random.choice(list(my_dict))
            print(key_check)
            my_dict.pop(key_check)
            
        else: 
            print("That was not a correct selection.")
            continue

        print("Would you like to check out another book?(Y/N)")
        ans = str(input())
        re_check = yes_no(ans)
        
#yes/no function
def yes_no(answer):
    
    input_err = True
    marker = False
    while input_err == True:
        
        if answer == 'Y'or answer == 'y':
            input_err = False
            marker = True
        elif answer == 'N'or answer == 'n':
            print("That's okay.")
            input_err = False
            marker = False
        else:
            print("That was not a valid selection, please try again.")
            print("Enter (Y/N).")
            marker = False
            continue
    
    return marker

# Driver Code

#creation of dictionary  
my_dict ={"Goosebumps": "Horror", "Killer Pizza": "Horror", "Love at Dawn": "Romance"}

#creation of genre dictionary
genre_dict = {1 : "Horror", 2 : "Non-fiction", 3 : "Romance", 4 : "Action"}

#creation of job description dictionary
job_dict = {"Job title " : "Librarian", "Shift time": "Day shift", "Salary": "competitive"}

#introduction
print("Hello, welcome to the library.")
print("We unfortunately only have the following selections:")
disp_selection()

other = 0

print("Would you like to make a donation today? (Y/N)")
ans = str(input())
if yes_no(ans) == True:
    make_dono()
    
else:
    other = 1

print("Would you like to checkout a book today?(Y/N)")
ans = str(input())
if yes_no(ans) == True:
    check_out()
else:
    other += 1
    
if other >= 2:
    print("It seems like you at the library for a different reason today.")
    print("Are you here to learn about our open position? (Y/N)")
    ans = str(input())
    if yes_no(ans)== True:
        print("Ah, very good. Here is the information for the position.")
        for key, value in job_dict.items():
            print( key,": ", value)
        print("Send in your application as soon as you can.")
        
    else :
        print("Thats too bad... I wonder why you came today.")
        wait = input()
        print("...")
        wait = input()
        print("...")
        wait = input()
        print("Sir, please leave")
        exit() 
        

        
print("Thank you for visiting us today!")
exit()
