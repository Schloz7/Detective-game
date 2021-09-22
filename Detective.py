import time


life = 3
new_life = 3


def Answers_script_2(life): 
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    second_choice()   
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()



def Answers_script_3(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    three_on_three() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_4(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    three_on_four()
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_5(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    animate_the() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_6(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    dissecated() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_7(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    electro()
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_8(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    motherland() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_9(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    first_place() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()
def Answers_script_10(life):    
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    animate_() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    quit()





def Answers_script(life):  
  global new_life 
  if new_life >= 2:
    new_life -= 1    
    print(new_life)
    print("Try again")
    favorite_first() 
  else:      
    print("You lost and gotta captured by Scotland Yard , now you're going to live in the UK ,in a prison cell")
    time.sleep(15)
    quit()

print(" Project \"CodeCademy\" Python Detective-Game")

time.sleep(5)

first_name = input(" Your name here KGB fellow:")

time.sleep(5)

print("You gonna live a day in a life of a KGB spy in the time of today")

time.sleep(5)

print("You're going to have 3 chances , can't be recovered like mistakes in real life")

time.sleep(5)

answer_1 = "RUSSIA"

def favorite_first():
 favorite_first = input("Say something to me right now , where was KGB created in first place ? \n")
 favorite_first = favorite_first.upper()
 if favorite_first == answer_1:
  print("That's the country where you're living right now")     
 else:
  Answers_script(life)
   

favorite_first()


time.sleep(5)
print("You're in your office as a new member of the global order of secret services and") 
time.sleep(5)
print("living right now the most moment of supremacy ever in your home country")
time.sleep(5)
print("Your office is in moscow headquarters, filled with a beautiful black table and a brand") 
time.sleep(5)
print("new chair in white, the walls are painted in RED and with many ads of global enemies of the new order")
time.sleep(5)
print("You just gotta one of them and is a picture of a white male , famous for his large amount of crimes in")
time.sleep(5) 
print("the old soviet union, MURDERER , ROBBER and nevertheless enemy of your country")
time.sleep(5)
answer_2 = "ARGENTINE"

def second_choice():
 second_choice = input("Tell me , in which country has a flag with a sun in the middle and blue over and down : \n 1.Russia \n 2.Argentine \n 3.USA \n 4.France \n")
 second_choice = second_choice.upper()
 if second_choice == answer_2:
  print("You're starting to understand the underworld more and know that this people are famous for their crimes")
  time.sleep(5) 
  print("all over the world of today , you just leave the room without talking and people are not talking to you")
  time.sleep(5)
  print("You leave to the street and see the beautiful city with russian girls everywhere and you kind look handsome")
  time.sleep(5)
  print("you leave to the airport and meet in your first class flight to Argentine a beautiful woman that sitting by") 
  time.sleep(5)
  print("your side all the flight , tells you that she has a place in front of the university UBA in argentine ")
 else:
  Answers_script_2(life)
  


second_choice()
time.sleep(5)
print("Your flight arrived in Buenos Aires ezeiza airport  you kinda happy for the invite to stay with the woman but") 
time.sleep(5)
print("you end refusing , you just used her to make you patch inside the country")
time.sleep(5)
print("You know two things about the suspect his age 50 and that he frequent a place called \"Puerto Madero\" , the place looks")
time.sleep(5)
print("cool with girls everywhere you make your way in the night  ")
time.sleep(5)
print("The suspect in on a place with 2 \"capangas\" you saw him laughing about a stupid joke involving the police of the country")
time.sleep(5)

answer_3 = "INVESTIGATE"

def three_on_three():
 three_on_three = input("BOOM! what happened ? , what??? there was a bomb and exploded , you're BLOODY, with the blood of people around you , DECIDE NOW : \n 1.Investigate \n 2.run like a chicken \n")
 three_on_three = three_on_three.upper()
 if three_on_three == answer_3:
  print("Luck! , you can see a gun with the security guard and he is lying dead on the floor , you got his weapon a Magnum.357")
  time.sleep(8)
  print("The suspect obviously dissapeared , you gotta no time to look confuse and shot somebody that was stopping you to run to") 
  time.sleep(5)
  print("get your enemy that is nothing more that minutes in front of you,you just left the place")
 else:
  Answers_script_3(life)
   


three_on_three()
time.sleep(5)

answer_4 = "LETHAL KICK"

def three_on_four():
  print("You're on Buenos Aires streets and running , you can see the desorientation of the police coming to the place")
  time.sleep(5)
  print("where the bomb exploded , you're running to get your enemy,you even can see him alone a fat old pal running in front of the") 
  time.sleep(5)
  print("justice parlament,he gotta a Taxi pointing a gun to the driver and driving out there's a car with one person on it , but is a") 
  time.sleep(5)
  three_on_four = input("cop what do you do ? \n 1.Lethal Kick \n 2.think about it\n")
  three_on_four = three_on_four.upper()
  if three_on_four == answer_4:
   time.sleep(5)  
   print("You just got it , you're driving at a high speed following the suspect all over buenos aires ,speedy is the key , you are in a") 
   time.sleep(5)
   print("better car and is almost getting him.")
  else:
   Answers_script_4(life)
  


three_on_four()
time.sleep(5)

answer_5 = "ANIMATE HIM"

def animate_the():
 print("Crash!!!! you got him he is leaving with blood all over his head , you are not good neither and you got confused") 
 time.sleep(5)
 print("you leave the car to get him you can hear the police coming towards you with their cars but they are really distant, you gotta") 
 time.sleep(5)
 print("in a fighting , after a while you could lead the situation and shot him on his chest , he is trying to run you know you must interrogate him")
 time.sleep(5)
 animate_the = input("but he fell in the middle of the street. He is without breathing you have few minutes before police, what do you do? \n 1.Animate him \n 2.kill him \n 3.drive out\n")
 animate_the = animate_the.upper()
 if animate_the == answer_5:
  print("That's correct . You need him a bit longer , he is almost diying you know that but you are good after all KGB , he is breathing again")
 else:
  Answers_script_5(life)
   


animate_the()
time.sleep(5)

answer_6 = "NEVER"

def animate_():
 print("He's crying and don't have to much time , you ask him informations about who he serves , he tells you finally") 
 time.sleep(5)
 animate_ = input("and asks you to help him and don't let him to the police \n 1.Never \n 2.Of course \n")
 animate_ = animate_.upper()
 if animate_ == answer_6:
  print("You left running to get a way out and you see the university in front of you , not a normal you see the medical school , UBA")
 else:
  Answers_script_10(life)
  


animate_()

time.sleep(5)
answer_7 = "DISSECATION"

def dissecated():
 print("You enter the university calling attention but you know how deal with and you enter a surgery room") 
 time.sleep(5)
 print("no one's there just you , you wear a doctor's jacket and follow to the next door,you see students in the class") 
 time.sleep(5)
 print("studying you enter the class and the professor asks you.Why you're late ? you tell him you're in the wrong class") 
 time.sleep(5)
 dissecated = input("but he insists and say you to stay , what do you do?\n 1.Dissecation \n 2.Go out \n ")
 dissecated = dissecated.upper()
 if dissecated == answer_7:
  time.sleep(7)   
  print("Excellent , the police is out running and you see the lights on the class windows . You watch the class")
 else:
  Answers_script_6(life)
 


dissecated()
time.sleep(5)
answer_8 = "ELECTROCUTE HIM"

def electro():
 print("You finish the class , sweating , you're walking through the hall and see that police is on the way out the university") 
 time.sleep(5)
 print("you go up stairs you wanna use the windows to leave 1 , 2 , 3 floor no one there, you look at a room with many wires on the floor")
 time.sleep(5)
 print("you're going to the window and got surprised by a lieutenant of the police he asks you your ID,you are with a wire on your hand")
 time.sleep(5)
 electro = input("sparkling with high voltage \n 1.Give fake ID \n 2.Run \n 3.Electrocute him \n")
 electro = electro.upper()
 if electro == answer_8:
  time.sleep(5)   
  print("You did it , he died screaming , the way is clear now , you use the window and left going to the airport, but because you don't wanna") 
  time.sleep(5)
  print("call atention you go to that woman place that you meet coming to Argentine , she accept you and you have to gotta a ride untill the") 
  time.sleep(5)
  print("airport after talking and laughing she drove you till there")
 else:
  Answers_script_7(life)
  


electro()
time.sleep(5)
answer_9 = "RUSSIA"

def motherland():
 motherland = input("She asks you about the ticket she have to buy and you say ?\n 1.Russia \n 2.Netherlands \n 3.France \n")
 time.sleep(5)
 motherland = motherland.upper()
 if motherland == answer_9:
  print("Russia mother land!\n The flight departs after a goodbye and you're in the russian airport of Saint Petersburg , It's almost 23:00")
 else:
  Answers_script_8(life)
 
time.sleep(5)

motherland()
time.sleep(5)
answer_10 = "7"

def first_place():
 print("The best for the last , you got promotion and you're lieutenant , you commander wants you to answer this last question") 
 time.sleep(5)
 first_place = input("what's the position of Russia in your life? \n 1.7 \n 2.4 \n 3.5 \n 4.6 \n 5.2 \n 6.3 \n 7.1\n")
 first_place = first_place.upper()
 if first_place == answer_10:
  print("поздравление")
  time.sleep(5)
 else:
  Answers_script_9(life)
 


first_place()




