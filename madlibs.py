from termcolor import colored
##This program acts as a madLib program asking the user for input and constructing
##a story out of said inputs

#gather words for Squidward story
def squidward():
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    anothernoun = input("Enter another noun: ")
    print("Squidward %s %s but the %s was utterly surprised by it." % (colored(verb + "ed","yellow"), (colored(noun, "yellow")), colored(anothernoun, "yellow")))

def spongebob():
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    tup1= (adj1,adj2)
    print("Spongebob is %s and %s" % (colored(tup1[0], "yellow"), colored(tup1[1], "yellow")))

#construct story
story = input("Which story would you like? Options: \033[92msquidward, spongebob \033[37m")
if story == "squidward":
    squidward()
elif story == "spongebob":
    spongebob()
else:
    print("Doesn't Exist.")
