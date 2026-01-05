# Declare characters used by this game.
define g = Character("You")
define b = Character("Myst")
define w = Character("???")
define n = Character("[player_name]")

# The game starts here.
label start:
    play music "audio/backgroundmusic.mp3" loop
######################CHAPTER ONE###########################
    scene chapterscreen
    centered "CHAPTER ONE"
    with fade

    # Show a background
    scene placeholder
    with fade

    # Show character sprite
    #how eileen happy
    show ginger cat phone idle at left

    "You sit on the end of a bench, scrolling on your phone as you wait for the bus."

    "The ambient noises of nature flood your ears."

    show black cat silent idle at right
    with moveinright

    "A few minutes pass, and a stranger makes their way to the bus station. They sit themself at the other end of the bench."

    "The silence between you two grow longer."
    
    menu:

        "You..."

        "Compliment their outfit.":

            jump compliment

        "Stay silent.":

            jump later

    
label compliment:

    show ginger cat talk smile at left
    with dissolve  
    g"I like your outfit."

    show ginger cat smile at left
    with dissolve

    show black cat blush talk at right
    with dissolve
    
    w"Oh, thank you!"
    
    w"I love your hair!"

    show black cat smile blush at right
    with dissolve

    show ginger cat smile blush at left
    with dissolve
    
    g"Thank you."

    show ginger cat blush at left
    with dissolve

    "You both smile at each other, hearts warm from the compliment."
    
    "Eventually, the bus arrives."

    "Although you both take the same bus, you do not sit next to each other."

    scene black with fade
    scene chapterscreen
    centered "CHAPTER TWO"
    with fade

    jump chaptertwo

label later:

    "You continue to scroll on your phone."

    "Nothing much changes between you two."

    menu:
        "You decide to..."
        
        "Keep scrolling on your phone.":
            jump quiet
        
        "Compliment their outfit.":
            jump compliment

label quiet:

    "You keep attending to business on your phone."

    "The awkwardness grows."

    menu:
        "Will you..."
        
        "Put in your earphones.":
            jump quietfr
            
        "Mention the bus always being late":
            jump busmention

label quietfr:
    
    show ginger cat earphone in at left
    with dissolve

    "You mute out the outside noises."

    "The two of you remain like this until the bus arrives."

    scene black with fade

    scene chapterscreen
    centered "CHAPTER TWO"
    with fade

    jump chaptertwosilence

label busmention:
    show ginger cat talk smile at left
    with dissolve
    
    g"It's funny how the bus is always late here."

    show black cat smile at right
    with dissolve

    show ginger cat smile at left
    with dissolve

    "They chuckle a little, nodding."

    show black cat talk at right
    with dissolve
    
    w"The day it shows up on time, it'll be a miracle."

    show ginger cat smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    "The two of you chuckle at their comment."

    "Eventually, the bus arrives."

    "Although you both take the same bus, you do not sit next to each other."

    scene black with fade
#########CHAPTER TWO TALK#############
    scene chapterscreen
    centered "CHAPTER TWO"
    with fade

    jump chaptertwo

    label chaptertwo:

        scene placeholder
        with fade
        show ginger cat phone idle at left

        "You arrive to the bus stop again, sitting in the same spot you did yesterday."

        show black cat silent idle at right
        with moveinright

        "As time passes, the same person you saw yesterday arrives."

        "They also sit in the same spot they did yesterday."

        show ginger cat smile
        with dissolve

        show black cat smile
        with dissolve

        "You both give each other a nod."

        show ginger cat talk smile at left
        with dissolve

        g"How's your day going?"

        show ginger cat smile at left
        with dissolve

        show black cat talk at right
        with dissolve

        w"Not bad, how about yours?"

        show ginger cat talk smile at left
        with dissolve

        show black cat smile at right
        with dissolve

        g"Same here. Same old same old, waiting for the late bus as always."
        show ginger cat smile at left
        with dissolve

        show black cat talk at right
        with dissolve

        w"No way! Me too!"

        show ginger cat talk smile at left
        with dissolve

        "You both laugh together."

        menu name:

            "Do you..."

            "Ask for their name.":
                jump askname

            "Decide against it for now.":
                jump noname

    label askname:

        show black cat smile at right
        with dissolve

        show ginger cat question at left
        with dissolve

        g"By the way, what's your name?"

        show ginger cat smile at left
        with dissolve

        show black cat blush talk at right
        with dissolve

        w"Oh! My name is Myst. How about you?"

        show ginger cat talk smile at left
        with dissolve

        show black cat smile at right
        with dissolve

        $ player_name = renpy.input("My name is", default="Artorias", length=30).strip()

        show ginger cat smile at left
        with dissolve

        show black cat talk at right
        with dissolve

        b"Nice to officially meet you, [player_name]."

        show ginger cat smile blush at left
        with dissolve

        show black cat smile at right
        with dissolve

        n"Same to you, Myst."

        show ginger cat talk smile at left 
        with dissolve

        show black cat talk at right
        with dissolve

        "You both continue small talk until the bus arrives."

        "Although you both take the same bus, you do not sit next to each other."

        scene black with fade

        jump chapterthree

    label noname:
        "Deciding it is not time yet to ask for their name, you end up just creating small talk until the bus arrives."

        "Although you both take the same bus, you do not sit next to each other."

        scene black with fade

        jump chapterthreename


##########CHAPTER TWO SILENCE###############
    label chaptertwosilence:

        scene placeholder
        with fade

        show ginger cat sit silence at left

        "You arrive to the bus stop again, sitting in the same spot you did yesterday."

        show black cat silent idle at right
        with moveinright

        "As time passes, the same person you saw yesterday arrives."

        "They also sit in the same spot they did yesterday."

        menu secondchance:

            "You two sit in silence once again."

            "You..."

            "Pull out your phone":
                jump nearquietend

            "Ask them how their day is going.":
                jump redemption

label nearquietend:
    show ginger cat phone idle
    
    "You pull out your phone, answering texts and scrolling through social media."

    "They seem too shy to strike up a conversation."

    menu endgamechoice:

        "Do you..."

        "Start a conversation.":
            jump redemption
        
        "Keep quiet.":
            jump finalchoice

label redemption:

    show ginger cat talk smile at left
    with dissolve

    g"How's your day going?"

    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    w"Not bad, how about yours?"

    show ginger cat talk smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    g"Same here. Same old same old, waiting for the late bus as always."
    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    w"No way! Me too!"

    show ginger cat talk smile at left
    with dissolve

    "You both laugh together."
    
    "You both continue small talk until the bus arrives."

    "Although you both take the same bus, you do not sit next to each other."

    scene black with fade

    jump chapterthreename

label finalchoice:

    "You two remain like this until the bus arrives."

    "Although you both take the same bus, you do not sit next to each other."

    scene black with fade

    #########CHAPTER THREE ENDING SILENCE#############
    scene chapterscreen
    centered "CHAPTER THREE"
    with fade
    
    scene placeholder
    with fade

    show ginger cat sit silence at left

    "You arrive to the bus stop, repeating the same thing as yesterday."

    "However, the other person never showed up."

    "You sit there in silence, waiting for the bus."

    "Surprisingly, the bus arrived on time."

    scene chapterscreen
    centered "ENDING THREE"
    centered "You did not start up a conversation."
    with fade

    return

############CHAPTER THREE KNOWS NAME#############

label chapterthree:
    scene chapterscreen
    centered "CHAPTER THREE"
    with fade

    scene placeholder
    with fade

    show ginger cat talk smile at left
    show black cat talk at right

    "This has become a daily routine for you two."

    "You always expect Myst at the same time, sitting at the same spot, both striking up small talk now."

    "Both of you have gotten to know each other a little more."

    show ginger cat smile at left
    with dissolve

    b"...and that basically sums up the story."

    show ginger cat talk smile at left
    with dissolve
    show black cat smile at right
    with dissolve

    n"Woah! Maybe I need to start reading that book. I haven't gone book shopping in forever."

    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    b"Might be your time then!"

    show ginger cat smile blush at right
    with dissolve
    show black cat smile at left
    with dissolve

    n"Might be! Haha!"

    "You think of a question to ask."

    menu semipersonal:
        "So..."

        "Ask where they take the bus to.":
            jump headto

        "Ask them if they have any plans for the day.":
            jump plansforday

label headto:

    show ginger cat talk smile at left
    with dissolve

    n "So, where you taking the bus to?"

    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    b "I'm going to head to the mall, do some grocery shopping."

    b "How about you?"

    show ginger cat talk smile at left
    with dissolve
    show black cat smile at right
    with dissolve

    n "I'm actually heading home. I usually spend my freetime there."

    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    b "Haha that's cool."

    show ginger cat smile at left
    with dissolve

    show black cat silent idle at right
    with dissolve

    "That felt a bit awkward."

    "Who asks where someone is taking the bus to?"

    "You both take the same bus, sitting slightly closer to each other now."

    scene black with fade

    jump chapterfourendingtwo

label plansforday:

    show ginger cat talk smile at left
    with dissolve

    n "Got any plans for the day?"

    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    b "I'm gonna grab some groceries n' maybe walk around the mall area for a bit. You?"

    show ginger cat talk smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    n "Just gonna head home for the day. Maybe read a book now just so I can give you a little summary in return."

    show ginger cat smile at left
    with dissolve

    "Myst smiles at the answer."

    "You both take the same bus, sitting slightly closer to each other now."

    scene black with fade

    jump chapterfourendingone



############CHAPTER THREE DONT KNOW NAME#############

label chapterthreename:
    scene chapterscreen
    centered "CHAPTER THREE"
    with fade

    scene placeholder
    with fade

    show ginger cat talk smile at left
    show black cat talk at right

    "The next day, everything is the same. You both sit in the same spots."

    "Once again, you both strike up some small talk."

    menu namefinalchance:
        "Will you..."

        "Ask what their name is.":
            jump lastchangeasked
        
        "Decide against it again.":
            jump didntaskagain

label lastchangeasked:

    show black cat smile at right
    with dissolve

    show ginger cat question at left
    with dissolve
    g"By the way, what's your name?"

    show ginger cat smile at left
    with dissolve

    show black cat blush talk at right
    with dissolve

    w"Oh! My name is Myst. How about you?"

    show ginger cat talk smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    $ player_name = renpy.input("My name is", default="Artorias", length=30).strip()

    show ginger cat smile at left
    with dissolve

    show black cat talk at right
    with dissolve

    b"Nice to officially meet you, [player_name]."

    show ginger cat smile blush at left
    with dissolve

    show black cat smile at right
    with dissolve

    n"Same to you, Myst."

    show ginger cat talk smile at left 
    with dissolve

    show black cat talk at right
    with dissolve

    "You both continue small talk until the bus arrives."

    "You both take the same bus, sitting slightly closer to each other."

    scene black with fade

    jump chapterfourendingone


label didntaskagain:
    "You decide against asking what their name is."

    "You oddly enjoy the animosity between you two."

    "You both continue small talk until the bus arrives."

    "You both take the same bus, sitting slightly closer to each other."

    scene black with fade

    jump chapterfourendingtwo

####################CHAPTER FOUR, CONTINUE##################
label chapterfourendingone:

    scene chapterscreen
    centered "CHAPTER FOUR"
    with fade

    scene placeholder
    with fade

    show ginger cat smile at left
    with moveinleft

    show black cat smile at right

    "When arriving to the bus stop, you noticed Myst already there."

    "It takes you by surprise."

    show black cat talk at right
    with dissolve

    b"You're late!"

    "You roll your eyes at their sarcasm."

    show ginger cat talk smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    n"I'm quite on time, actually."

    show ginger cat smile at left
    with dissolve

    "You both smile."

    "Your friendship has grown from the day you two first met."

    "You both start sitting next to each other."

    show black cat talk at right
    with dissolve

    b"Any plans for the day?"

    show ginger cat talk smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    n"As usual, no. Let me guess, you too, do not have plans?"

    show ginger cat smile at left
    with dissolve

    show black cat blush talk at right
    with dissolve

    b"Oh wow, you know me so well!"

    show ginger cat smile at left
    with dissolve

    show black cat smile at right
    with dissolve

    "The both of you chuckle."

    show black cat blush talk at right
    with dissolve

    b"I was actually meaning to ask you. Would you like to hang out today? Head to a bookshop or something?"

    "Your smile grows wider at the offer."

    show ginger cat smile blush at left
    with dissolve

    show black cat smile blush at right
    with dissolve

    n"I'd love to!"

    show black cat blush talk at right
    with dissolve

    "The two of you are smiling ear to ear, engulfed in your conversation."

    "You both take the same bus, sitting next to each other."

    jump chapterfive


##########CHAPTER 4, SECOND ENDING#####################
label chapterfourendingtwo:

    scene chapterscreen
    centered "CHAPTER FOUR"
    with fade

    scene placeholder
    with fade

    show ginger cat talk smile at left
    show black cat talk at right

    "This has become a daily routine for you two."

    "You both enjoy the small chat together while waiting for the bus."

    "It makes both your days a little bit brighter."

    "You both take the same bus, sitting slightly closer to each other."

    scene chapterscreen
    centered "ENDING TWO"
    centered "You both enjoy your daily small talks."
    with fade

    return

label chapterfive:

    scene chapterscreen
    centered "CHAPTER FIVE"
    with fade

    scene placeholder
    with fade

    show ginger cat talk smile at left
    show black cat talk at right

    "You both started leaving a little earlier and staying out a little longer to continue talking to each other."

    show ginger cat look right at left
    with dissolve

    show black cat blush talk at right
    with dissolve

    b"[player_name]..."

    "You look a little scared at the random pause."

    b"I just want to say thank you. For being my friend. For striking up that conversation all the way back then."

    b"I enjoy talking to you."

    show ginger cat blush at left
    with dissolve

    show black cat smile blush at right
    with dissolve

    "You relax, now heartwarmed."

    show ginger cat smile blush at left
    with dissolve

    n"And I enjoy talking to you, Myst."

    "You both take the same bus, sitting next to each other."

    scene chapterscreen
    centered "ENDING ONE"
    centered "You both formed a friendship together."
    with fade

    return


    



    











