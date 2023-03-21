import random
import time
username = str(input("Hello there Friend \U0001F44B! What is your name? ")) 
health_points = 30
passed_route = False
user_action = {
        "Rest" : 5,
        "Water": 7,
        "bug spray": 7,
        "Recovery gel" : 8,  
        "Play dead" : 10
    }

def end_game(username, health_points, passed_route): 
    #End of the game
    if health_points >= 30 and passed_route == True:
        print(f"🎊 Well done {username} 🎊 You successfully completed your walk and ended this game with {health_points} health points! You won the game! Here's a cookie 🍪")
    elif health_points < 30 and passed_route == True:
        print(f"Good try in completing your walk {username}. Sadly, you ended with {health_points} health points, so you didn't win 😢. Let's hope you'll win next time!")
    else:
        print(f"Ah... You ended this game with {health_points} health points. Sorry to say that you lost the game this time around, {username} .Better luck next time! 😭😭")

def route_one(health_points, user_action, passed_route):
    #function executed if user chooses route one
    time.sleep(2)
    obstacle_two = int(input(f"You are walking along and you come across a tree that holds a wasp nest 🪰... and the wasps look angry... what do you do next, {username} 😦? 1. Turn around, 2. Walk past the nest, 3. Put on bug spray (Enter 1, 2 or 3) "))
    if obstacle_two == 3:
        health_points = health_points + user_action["bug spray"]
        print(f"Wise choice my friend! You put on the bug spray and wow you can walk past the nest with no problem 😆 (+7 HP). HP: {health_points}")
        passed_route = True
    else:
        health_points = health_points - 10
        print(f"OUCHHHHH! The wasps followed you and now you're covered in wasp stings 😫. (-10 HP) HP: {health_points}")
        gel_or_no_gel = float(input("Quick, you might have some gel on you - pick a number between 1-10 "))
        if gel_or_no_gel >= 1 and gel_or_no_gel <= 10 and (gel_or_no_gel % 2) == 0:
            health_points = health_points + user_action["Recovery gel"]
            print(f"Phew... thank goodness you grabbed the Recovery Gel before you left 🥲 (+8 HP). Now you can finish your walk! Health points {health_points} ")
            passed_route = True
            time.sleep(3)
        elif gel_or_no_gel >= 1 and gel_or_no_gel <= 10 and not (gel_or_no_gel % 2) == 0:
            print(f"Well... you forgot the recovery gel at home but the stings aren't too bad, thankfully. You can still complete the walk 🥲. Health points: {health_points}")
            passed_route = True
            time.sleep(3)
        else:
            health_points = health_points - 5
            print(f"Hmmmm... looks like you can't follow the instructions 🤧 (-5 HP). Health points: {health_points}")
            time.sleep(3)
        
    end_game(username, health_points, passed_route)


def route_two(health_points, user_action, passed_route):
    time.sleep(2)
    obstacle_two = int(input(f"You are walking along and you come across a tree that holds a wasp nest 🪰... and the wasps look angry... what do you do next, {username} 😦? 1. Turn around, 2. Walk past the nest, 3. Put on bug spray "))
    if obstacle_two == 3:
        health_points = health_points + user_action["bug spray"]
        print(f"Wise choice my friend! You put on the bug spray and wow you can walk past the nest with no problem 😆 (+7 HP). HP: {health_points}")
        passed_route = True
    else:
        health_points = health_points - 7
        print(f"OUCHHHHH! The wasps followed you and now you're covered in wasp stings 😫 (-7 HP). HP: {health_points}")
        print("Quick, you might have some gel on you but there are too many items in your bag")
        gel_or_no_gel = float(input("It's too hard to find it, let's hope you grab it's the first thing you grab out of your bag ... pick a number between 1-10 "))
        if gel_or_no_gel >= 1 and gel_or_no_gel <= 10 and (gel_or_no_gel % 2) == 0:
            health_points = health_points + user_action["Recovery gel"]
            print(f"Yay! You grabbed the Recovery Gel 🥲 (+8 HP). Now you can finish your walk! Health points {health_points} ")
            passed_route = True
            time.sleep(3)
        elif gel_or_no_gel >= 1 and gel_or_no_gel <= 10 and not (gel_or_no_gel % 2) == 0:
            print(f"Well... you forgot the recovery gel at home but the stings aren't too bad, thankfully. You can still complete the walk 🥲. Health points: {health_points}")
            passed_route = True
            time.sleep(3)
        else:
            health_points = health_points - 5
            print(f"Hmmmm... looks like you can't follow the instructions. The pain has gotten worse 🤧 (-5 HP). Health points: {health_points}")
            time.sleep(3)

    time.sleep(3)
    print("You're walking along and you decide to enter a forest 🌳 . It feels really good to be surrounded by trees and nature...")
    time.sleep(3)
    print("... wait")
    time.sleep(3)
    print("... what's that sound")
    time.sleep(3)
    health_points = health_points - 8
    print(f"Oh my gosh 😨.... A GRIZZLY BEAR IS COMING TOWARDS YOU 🐻 !!!! (-8 HP) HP: {health_points}")
    time.sleep(3)
    objective_two = int(input("QUICK WHAT DO YOU DO?? 1. Fight Back, 2. Play Dead, 3. Turn Around, 4. Continue walking like nothing is happening (Enter 1, 2, 3 or 4) "))
    if objective_two == 2:
        print("You decide to play dead. The bear is coming closer and closer...")
        time.sleep(3)
        print("He starts to sniff you ... 😨")
        time.sleep(3)
        print("and... he turns away and walks deeper into the forest.")
        time.sleep(3)
        health_points = health_points + user_action["Play dead"]
        print(f"AND YOU STAYED ALIVE!!!!! 🥳🥳🥳 (+10 HP) HP: {health_points}")
        time.sleep(3)
        print("It's safe to say the run should end here. 😅")
        passed_route = True
    else: 
        health_points = health_points - 8
        print(f"Why did you decide to do that?? Now the bear is charging at you !!! 😱 (-8 HP) HP: {health_points}")
        time.sleep(3)
        retry = int(input("QUICK DO SOMETHING!!! 1. Play dead, 2.Run away "))
        if retry == 1:
            health_points = health_points + user_action["Play dead"]
            print("You finally decide to drop down and play dead. The bear is coming closer and closer...")
            time.sleep(3)
            print("He starts to sniff you...")
            time.sleep(3)
            print("and... he turns away and walks deeper into the forest.")
            time.sleep(3)
            print(f"AND YOU'RE ALIVE!!!!! 🥳🥳 (+10 HP) HP: {health_points}")
            time.sleep(3)
            print("It's safe to say the run should end here.")
            passed_route = True
         
        else:
            health_points = health_points - 10
            print(f"Oh {username}... sorry to say that you have now died. Rest in Piece (-10 HP).💀 HP: {health_points}")
    
    time.sleep(4)
    end_game(username, health_points, passed_route)




def game(username, health_points, passed_route):
    #introduce user to the game
    print(f"Welcome {username}! We're so excited that you can join us on this adventure 😃!")
    print("The aim of the game is easy. You just need to complete your walk in one piece! Just make sure your Health points (HP) don't go below 30!")
    time.sleep(4)

    #shows user how many health points they have at the start
    print(f"HP: {health_points}")
    time.sleep(4)

    #introduces the story for the game 
    print("The sun is shining 🌅 and the birds are singing 🐦. You can't help but think that it's the perfect day to go on a walk.")
    time.sleep(4)
    print("You put on your shoes👟, grab your gear 🎒 and head out the door")
    time.sleep(3)

    #Challenge one
    health_points = health_points - 5
    time.sleep(3)
    print(f"You've walked for 2 miles in the sun and find yourself getting dehydrated 🥵. (- 5 HP). HP: {health_points}")
    time.sleep(3)

    obstacle_one = int(input("What do you wish to do? 1. Rest, 2. Drink water, 3. Continue (Enter 1, 2 or 3) "))
    if obstacle_one == 1:
        health_points = health_points + user_action["Rest"]
        print(f"You have decided to rest 😌 (+5 HP). Health points: {health_points}")
        time.sleep(3)

    elif obstacle_one == 2:
        health_points = health_points + user_action["Water"]
        print(f"You have decided to drink water 💧 (+7 HP). HP: {health_points}")
        time.sleep(3)
   
    elif obstacle_one == 3:
        health_points = health_points - 5
        print(f"You have decided to continue walking, but you feel more tired and dehydrated 🥴 (- 5 HP). HP: {health_points}")
        time.sleep(3)
        
    else:
        health_points = health_points - 5
        print(f"Well... looks like you couldn't decide on anything. You continue along the hike anyway, but feel more tired and dehyrated 🥴 (- 5 HP). HP: {health_points}")
        time.sleep(3)
    
    
    #User decides whether to go through route 1 or 2
    route_decision = int(input("You continue walking and come across two diverging paths. Which path would you like to take? 🤔 Enter 1 or 2. HINT - Route 1 looks... easier than route 2 🤫"))
    if route_decision == 1:
        route_one(health_points, user_action, passed_route)     

    elif route_decision == 2:
        route_two(health_points, user_action, passed_route)
    else: 
        print("Well... you didn't answer the question properly. The game has now ended 🙁.")
           
game(username, health_points, passed_route)