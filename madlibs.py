from termcolor import colored
##This program acts as a madLib program asking the user for input and constructing
##a story out of said inputs

#Unsure how to implement dictionaries in this example, but a dictrionary is constructed as follows:
# released = {
# 		"iphone" : 2007,
# 		"iphone 3G" : 2008,
# 		"iphone 3GS" : 2009,
# 		"iphone 4" : 2010,
# 		"iphone 4S" : 2011,
# 		"iphone 5" : 2012
# 	}


def squidward():
    #gather words for story
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")
    anothernoun = input("Enter another noun: ")
    #print story
    print("Squidward %s %s but the %s was utterly surprised by it." % (colored(verb + "ed","yellow"), (colored(noun, "yellow")), colored(anothernoun, "yellow")))

def spongebob():
    #gather words for story
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    #form the tuple
    tup1= (adj1,adj2)
    #print story
    print("Spongebob is %s and %s" % (colored(tup1[0], "yellow"), colored(tup1[1], "yellow")))

def patrick():
    #gather data for story
    adj1 = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    num = int(input("Enter a number "))
    #form the list
    li= [adj1,noun,num]
    #print story
    print("Patrick had a %s %s which he sold for %s doubloons" % (colored(li[0], "yellow"), colored(li[1], "yellow"), colored(int(li[2]), "yellow")))

#ask user which story to present
story = input("Which story would you like? Options: \033[92msquidward, spongebob, patrick \033[37m")
if story == "squidward":
    squidward()
elif story == "spongebob":
    spongebob()
elif story == "patrick":
    patrick()
else:
    print("Doesn't Exist.")
