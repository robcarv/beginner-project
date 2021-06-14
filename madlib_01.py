#  string concatenatuion ( aka how to put strings toguether)
# supose we eante to create a string that says "subscibre to _____"
youtuber = " Put your name here"  # some string variables

# #  a few ways to do this
# print ("subscribe to " + youtuber)
# print ("subscribe to {}" .format(youtuber) )
# print (f"subscribe to {youtuber }")]

adj  =input ("Adjectives :")
verb1 =input("verb: ")
verb2 =input("verb: ")
famous_person= input ("Name of famous person: ")

madlib = f"computer program is so {adj} , It make me so exited  all the time because \
    I love to {verb1}. Stay hydrate and {verb2} like your are {famous_person}"

print(madlib)