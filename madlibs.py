##This program acts as a madLib program asking the user for input and constructing
##a story out of said inputs

#gather words for Squidward story
def squidward():
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    anothernoun = input("Enter another noun: ")
    print("Squidward %sed %s but the %s was utterly surprised by it." % (verb, noun, anothernoun))

#construct story
story = input("Which story would you like? Options: squidward  ")
if story == "squidward":
    squidward()
else:
    print("Doesn't Exist.")
