
# write a program to dictionary of hindi words with value as their english translation .provide user with an option   to look it up!
dict = {

    "kursi" :"chair",
    "pani" : "water",
      "khidki":"window",
      "kalam": "Pen"

}
 
print(dict.keys())
word = input("enter the hindi words = ")

print("the meaning is = ")
print(dict.get(word,))
