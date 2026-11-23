age=23
if age <=12:
    print("Child ticket")
else:
    print("Adult ticket")
is_student=True
if True:
    print ("Student discount")
day="Wednesday"
if day=="Saturday":
    print("Weekend price")
else:
    print("Weekday price")

language="English"
if language=="English":
    print("Hello")
elif language=="Polish":
    print("Czesc")
elif language=="Spanish":
    print("Hola")
elif language =="German":
    print("Guten Tag")
elif language=="Chinese":
    print("Ni hao")
else:
    print("I do not know tis language yet")


word="bus"
dictionary={"child":"children","mouse":"mice"}
if word in dictionary:
    print(dictionary[word])
elif word[-1] in ["s","x","z"] :
    print(word+"es")
elif word[-1]=="y" and word[-2] not in ["a","e","i","o","u"]:
    print(word[:-1]+"ies")
else:
    print(word+"s")
