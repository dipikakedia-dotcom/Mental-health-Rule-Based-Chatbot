
print("Type 'bye' to exit")

while True:
    message=input("User:").lower()
     # EXIT
    if message == "bye":
        print("Bot: Take care! Stay strong and remember that it's okay to ask for help. 💙")
        break
    # greetings and domain selection
    if message=="hi" or message=="hello":
        print(" BOT: Hello!, How can I help you?")
        print("Kindly choose the appropriate domain that you are facing problems with: ")
        print("1. Health issues")
        print("2. Self doubt")
        print("3. Family or relationship issues")
        print("4. Academic stress")
        print("5. General low mood")

        domain= input("\nUser: ").lower()

    #domain 1= health issues
    if domain == "health issues" or domain == "1":

        print("BOT:I understand health issues can be draining both mentally and physically. Kindly explain your problem to me, so that i can help")

        problem = input("Bot: Kindly explain your problem to me.\nUser: ").lower()

        if "ache" in problem or "pain" in problem or "allergy" in problem or "uneasy" in problem:
            print(" BOT:Normal levels of pain can be tolerable, if it exceeds, i would advise you to consult a doctor for professional help")
        else:
          print("BOT:Thank you for sharing. Please consider speaking toa healthcare professional when you're concerned")

    elif domain == "self doubt" or domain == "2":
        print("BOT:Self doubt is the most neglected sort of depression, people dont usually adress it. Please feel free to open up to me.")
    
        problem = input("Bot: Kindly explain your problem to me.\nUser: ")

        if "doubt"in problem or "concentrate" in problem or "ability" in problem or "sad" in problem or "nothing" in problem:
            print("BOT:Its normal to feel that way sometimes, but i would recommend you to do a few activities that keep you engaged and happy. You can focus on you hobbies or run to that one 'happy place' that every person has. just spend some time alone, try affirtmations and do things that make you feel better." )
        else:
         print("BOT:Thank you for opening up. Remember that one difficult moment does not define your abilities.")
         #DOMAIN-3 FAMILY OR RELATIONSHIP ISSUES
    elif domain == "family or relationship issues" or domain == "3":
        print("BOT:Maintaining bonds can itself be a task, explain your problem to me, i might help.")
    
        problem = input("Bot: Kindly explain your problem to me.\nUser: ")
        if "bond" in problem or "understand"in problem or "friend" in problem:
            print("Not every person feels understood at all times, i would recommend proper communication and take some time to reflect on your actions. stay compassioante and handle situations gently. i hope everything gets better as soon as possible.")
        else:
         print("BOT:I understand. Take some time to reflect and remember to be compassionate toward yourself")

         #domain-4 academic stress
    elif domain == "academic stress" or domain == "4":
        print("woah! tough one, but im sure you have the mind of a genious. tell me whats bothering you?")
    
        problem= input("BOT:Kindly explain your problem to me.\nUser: ")
        if "study" in problem or "focus" in problem:
            print("Chin up champion. i know you can do it, just make a proper timetable, watch a few roadmaps and start concentrating, you are good to go!")
        else:
            print("Bot: Don't put too much pressure on yourself. Let's take things one step at a time.")

    #domain-5 general low mood 
    elif domain == "general low mood" or domain == "5":
        print(" sometimes feeling low is common, you can vent here")
    
        problem= input("BOT:Kindly explain your problem to me.\nUser: ")
        if "sad" in problem or "low" in problem:
            print("i see what you are feeling right now. dont dismiss your feelings. its alright to feel sad sometimes. but if you need more help, i would advice you to visit a therapist")
        else:
             print("Bot: Thank you for sharing that with me.You don't have to handle everything alone.")
     # SAFETY
    elif ("torture" in domain or
              "abuse" in domain or
              "unsafe" in domain):

        print("Bot: I'm concerned about your safety.If you're in immediate danger, please contact local emergency services or a trusted person nearby.")

    else:
            print("Bot: I didn't understand that choice. "
                  "Please choose one of the available domains.")
   

       
   