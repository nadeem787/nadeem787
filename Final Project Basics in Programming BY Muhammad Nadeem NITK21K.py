import random
#my roll dice program
def rolling(): 
    return random.randint(1,6)+random.randint(1,6)
def play():

    mydice = rolling()
    if mydice in [7,11]:
        return 'Win',1 
    elif mydice in [2,3,12]:
        return 'Loss',1 
    else:
        trys=1 
        my_point=mydice
        while True:
            mydice=rolling()
            trys+=1
            if mydice==my_point:
                return 'Win',trys 
            elif mydice==7:
                return 'Loss',trys 
            else:
                continue


def main():
    rolls = [0]*25
    wins=0
    loss=0
    observations=1000000
    for _ in range(observations):
        outcome,trys = play()
        if outcome=='Win':wins+=1
        else:loss+=1
        if trys<=len(rolls):
            rolls[trys-1]+=1
        else:
            rolls[-1]+=1

    print('Percentage of win: {:.2f}%'.format(wins*100/(observations)))
    print('Percentage of losses: {:.2f}%'.format(loss*100/(observations)))
    print('Percentage of wins or losses based on total number of rolls')
    print()
    print('{:>24}{:>20} '.format('% Resolved','Cummulative %'))
    print('{:<5}{:>20} {:>20}'.format('Rolls','on this roll','of games resolved'))

    for i in range(len(rolls)):
        p_resolved = rolls[i]*100/observations
        c_resolved = sum(rolls[0:i])/observations
        c_resolved = 100*c_resolved
        if i!=len(rolls)-1:
            print('{:>5}{:>19.5f}%{:>19.5f}%'.format(i+1,p_resolved,c_resolved))
        else:
            print('{:>5}{:>19.5f}%{:>19.5f}%'.format(i + 1, p_resolved, 100*sum(rolls)/observations))
main()
