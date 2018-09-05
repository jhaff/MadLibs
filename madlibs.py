from termcolor import colored
import random
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
    #print story, notice the concatenation
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
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter yet another noun ")
    #form the list
    li= [noun1,noun2,noun3]
    random.shuffle(li);
    #print story
    print("Patrick had a huge %s, a tiny %s, and a wonderful %s." % (colored(li[0], "yellow"), colored(li[1], "yellow"), colored(li[2], "yellow")))

def krabs():
    #gather data for story

    adj1 = input("Enter an adjective: "),
    noun1 = input("Enter a noun: "),
    verb1= input("Enter a past tense verb: "),

    words = {
		"adjective" : adj1,
		"noun" : noun1,
		"verb" : verb1,
	}
    #print story
    print("Mr Krabs had a %s %s and then he %s." % (colored(words["adjective"], "yellow"), colored(words["noun"], "yellow"), colored(words["verb"], "yellow")))


#ask user which story to present
story = input("Which story would you like? Options: \033[92msquidward, spongebob, patrick, krabs \033[37m")

while True:
    if story == "squidward":
        squidward()
        break
    elif story == "spongebob":
        spongebob()
        break
    elif story == "patrick":
        patrick()
        break
    elif story == "krabs":
        krabs()
        break
    else:
        print("Doesn't Exist.")
