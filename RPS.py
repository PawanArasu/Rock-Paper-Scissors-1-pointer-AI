import random

Cmds = ['r','p','s']
ai_cmd = random.choice(Cmds)
print("Thisis a one pointer game SO be Careful with ur decisions!! all the best")

p_cmd = input('rock: r,paper: p,scissor: s ; ')




def fun():
    ai_s = 0
    p_s = 0

    if ai_s <= 3 or p_s <= 3:

        #if same cmds

        if ai_cmd == 'p' and p_cmd == 'p':
            return 

        if ai_cmd == 'r' and p_cmd == 'r':
            return

        if ai_cmd == 's' and p_cmd == 's':
            return

        #if player wins

        if ai_cmd == 'p' and p_cmd == 's':
            p_s = p_s+1
            print('You win!!')

        if ai_cmd == 'r' and p_cmd == 'p':
            p_s = p_s+1    
            print('You win!!')

        if ai_cmd == 's' and p_cmd == 'r':
            p_s = p_s+1
            print('You win!!')


        #if AI wins

        if ai_cmd == 's' and p_cmd == 'p':
            ai_s = ai_s+1
            print('AI wins!!,better luck next time!')

        if ai_cmd == 'p' and p_cmd == 'r':
            ai_s = ai_s+1    
            print('AI wins!!,better luck next time!')

        if ai_cmd == 'r' and p_cmd == 's':
            ai_s = ai_s+1    
            print('AI wins!!,better luck next time!')


    
fun()


        

 




