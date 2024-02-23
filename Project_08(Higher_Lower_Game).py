from List_people import people_list
import random as r
from HLlogo import Title, vs
import os
print(Title)
count = 0 
def display_account_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {description}, {country}"

def check(guess, follower_1, follower_2):
    if follower_1 < follower_2:
        return guess == 2 # If return condition satisfies then it returns true otherwise false
    else:
        return guess == 1

def game():
    account_1 = r.choice(people_list)
    account_2 = r.choice(people_list)
    while account_1 == account_2:
        account_2 = r.choice(people_list)
    print(f"compare 1: {display_account_info(account_1)}")
    print(vs)
    print(f"compare 2: {display_account_info(account_2)}")


    guess = int(input("Who has more follower's? Type 1 or 2 : "))

    followers_count_1 = account_1["followers"]
    followers_count_2 = account_2["followers"]
    is_correct = check(guess, followers_count_1, followers_count_2)
    os.system('cls')
    print(Title)
    if is_correct == True:
        global count
        count +=1
        print(f"Your are right. Your score is : {count}")
        game()
    else:
        print(f"You are wrong.. your final score is : {count}")

game()