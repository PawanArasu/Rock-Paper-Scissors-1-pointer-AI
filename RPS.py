import random

Cmds = ['r','p','s']
ai_cmd = random.choice(Cmds)
print("This is a one pointer game SO be Careful with ur decisions!! all the best")

player_cmd = input('rock: r, paper: p, scissor: s ; ')


def fun():
    ai_score = 0
    player_score = 0

    if ai_score <= 3 or player_score <= 3:

        win = False

        #if player wins

        if ai_cmd == 'p' and player_cmd == 's':
            win = True

        if ai_cmd == 'r' and player_cmd == 'p':
            win = True

        if ai_cmd == 's' and player_cmd == 'r':
            win = True


        if win == True:
            
            #when player wins
            player_score = player_score + 1
            print('You win!!')

        else:

            #if same commands
            if ai_cmd == player_cmd:
                print("Well thats a tie, better luck next time!")
                return

            #else ai wins
            else:
                ai_score = ai_score + 1    
                print('AI wins!!,better luck next time!')

    
fun()


        

 




