# This is a simple chatbot. Practicing the lesson I just learned without looking at it's code.


running = True


print("Hello! My name is Apollo. I'm a simple chatbot that's ready to learn about space. What's your name?")
my_name = input("Enter Name: ")

print("Apollo: Nice to meet you, " + my_name + ". Could you teach me the names of the planets in our solar system?")
planets = input("Enter Planets: ")

print("Apollo: So the planets are " + planets + ". Does that sound right, " + my_name + "?")
answer = input("y/n:").lower()
farewell = "Wow! that was easy. I can't wait to learn more about space in the future! Until next time, " + my_name + "!"
try_again = "Oh no! This is harder than I thought. Can you repeat that?"


if answer == "y":
    print(farewell)
    running = False
else:
    print("Oh no... Maybe we should try again next time..") 
    

    







