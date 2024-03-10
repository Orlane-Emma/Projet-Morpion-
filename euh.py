import random
import time
from datetime import date

'''
This class has a beautiful name right ?
It's just a class to define some useless stuff
C'est au piff !!!
'''
class Alexandra:
    data_dictionary = {} #Dic to keep all the data, keep track of the mood
    list_color = ["red", "black", "blue", "brown", "blond", "purple", "orange"]
    def __init__(self, mood, outfit_style, food) -> None:  #Attributs init
        self.name = "Jane Alexandra"
        self.hair_color = random.choice(self.list_color) #We choose the hair color randomly between this list
        self.food = food
        self.mood = mood
        self.ootd = outfit_style
        print('-'*7, '#'*6, 'STARTIIIIIINNGGG', '#'*6, '-'*7) #first print after Alexandra class object creation
        today = date.today()
        hello_message = f"Hellooo {self.name}, i'm happy to see you today {today.strftime("%B %d, %Y")}"
        print("\033[94m {}\033[00m" .format(hello_message)) #print with the color blue

    def choose_hairstyle(self): #Method to choose a hairstyle according to the hair color
        print('*'*10)
        print(f'Hey {self.name}, the hair color today is {self.hair_color} yeahhh !')
        if self.hair_color in ('black', 'blond', 'brown'):
            print("\t \t Hairstyle choices : <Braids> \t <Ponytail> \t <Afrooo> \t <Wig> ")
            fav_style = input('Which hairstyle do you prefer ? : ')
            print(f"Ouhh i like the {fav_style} style too, it's giviiing")
        elif self.hair_color in ('purple', 'orange'):
            print("Today we are trying an uncommon color, that's exciting !")
        elif self.hair_color == 'red':
            print("That's Bibi color, so nice !!")
        else:
            raise RuntimeError(f'The hair_color {self.hair_color} is unacceptable')
    
    def handle_my_mood(self): # Method to help with the mood
        if(self.mood == 'sad'):
            attempts = 1
            solutions_for_sad_mood = {1:'Open your music app and play your fav Rema song',
                                      2: 'Do Yoga, Try the mountain position and the dog one ;)',
                                      3: 'Go get fresh air outside ',
                                      4: 'Take deep breaths'}
            print("\033[25m Oh no ! You are sad :(\033[40m")
            print('When you are sad, i am sad too \n Lets try to remove this sadness')
            while(attempts<5):
                print(f" Can you try to {solutions_for_sad_mood[attempts]} ?")
                answer = input('Do you want to ? Yes/No : ')
                if answer.upper() == 'NO':
                    print('-------------------------------------------- Dommage ----------------------- ')
                    if attempts == 4:
                            print('Sorry i wish i could help you')
                            print('Try to talk to someone, you are not alone ok ? <3')
                            break
                    print('Okay, i have another solution for you.')
                    attempts+=1
                    continue
                elif answer.upper() == 'YES':
                    time.sleep(5)
                    it_worked = input('Hey, did it change your sad mood ? Yes/No : ')
                    if it_worked.upper() == 'NO':
                        print('Okay, let us try something else')
                        print('----------------------------------FAIL---------')
                        attempts+=1
                        continue
                    elif it_worked.upper() == 'YES':
                        print("\033[94m !!!!  Yaaahhh so cool, stay happy please, life is beautiful !!!! \033[00m")
                        break
        elif self.mood == 'happy':
            happy_reasons = input('Oh great you are happy today, why ? :')
            print(f'I would be happy too because of {happy_reasons}')
    
    def choose_outfit_items():
        pass

    def evaluate_food(self):
        pass

#End of class definition                  

#Now let's create an object of this class and try our methods
alexandra_jane = Alexandra(mood='sad', food=['chicken', 'rice'], outfit_style='classy' )
#First, we choose your hairstyle
alexandra_jane.choose_hairstyle()
#Handle your mood 
alexandra_jane.handle_my_mood()