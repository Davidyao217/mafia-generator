import random

def main():
    nOfPlayer = 5
    names = ["Daren","Ethan", "Veronica", "Ellyn", "Mandy"]
    '''
    nOfPlayer = 0
    names = []

    checker = True
    while(checker): 
        nameinpt = (input("Please enter participant name (enter numeral to finish): "))

        try:
            int(nameinpt)
            it_is = True
        except ValueError:
            it_is = False
        if(it_is):
            break
       
        names.append(nameinpt)
        nOfPlayer = nOfPlayer + 1
    '''
    list = random.sample(range(1, nOfPlayer), 3)
  
    print(names[list[0]] + " is the mafia")    
    print(names[list[1]] + " is the doctor")
    print(names[list[2]] + " is the detective")

if __name__ == '__main__':
    main()

