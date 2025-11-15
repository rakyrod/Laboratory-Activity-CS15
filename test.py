import random 

adjectives = ["Fluffy" , "Speedy" ,"Tiny" , "Happy", "Brave"]
noun = ["Paws", "Tail" , "Whiskers", "Fur" , "Claws"]

print("🐾 Welcome to the Pet Name Generator! 🐾")
count = int(input("How many pet names would you like to generate?:"))

print("Here are your pet names")

for i in range(count):
    name = random.choice(adjectives) + random.choice(noun)
print(f"{i+1}. {name}")
