def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Sscore = 0
    Kscore = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            Kscore += (len(string)-i)
        else:
            Sscore += (len(string)-i)
    
    if Kscore > Sscore:
        print("Kevin", Kscore)
    else:
        print("Stuart", Sscore)
        
if __name__ == '__main__':
    s = input("Enter your string ")
    minion_game(s)