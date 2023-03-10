# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cassandra = Character("Cassandra",color = "#ed2b24")
define cyrus = Character("Cyrus",color = "#321bff")
define you = Character("You",color = "#f0f0f0ff")
define barry = Character("Barry",color ="#1a8cd3")
# The game starts here.

label start:
    #Ominous and sad music playing TBA
    play music "audio/Music/Makai Symphony - Dragon Castle.mp3" fadein 0.5 volume 0.5
    "How did it end up like this?"
    "At some point..."
    "Things just fell apart"
    


    #TBA
    scene bg eye
    with dissolve
    "Where did it all went wrong?"
    scene bg casDestruction
    with fade
    "I remember"
    "It all begin when..."
    

    label background:
        #slowly fade into office, TBA
        stop music fadeout 1.5
        #Crowd noises
        play sound "audio/Sound/office-ambience-6322.mp3"
        scene bg office
        with Dissolve(1.0)
        you "Breath IN...{w}Breath OUT..."
        you "(I got this)"
        "???" "Hi there, are you the newbie?"
        scene bg cystand
        you "Oh! Yes, I'm the new hire it's my first day!"
        "???" "Well then, I'm Cyrus, and let me be the first to welcome you to Big Energy Corp"
        cyrus "..."
        you "..."
        cyrus "Oh that's right, the boss wants to see you, but she's currently occupied"
        cyrus "We are blocking the way, let's go sit down"
        scene bg cysit
        with fade
        cyrus "In the mean time"
        cyrus "I guess I should ask"
        cyrus "why here?"
        you "Because..."


        


    $ casAf = 0
    $ cyAf = 0
    label choices:
    menu:
        "For the big bucks":
            jump cyrusNormal

        "For the enviroment!":
            jump cyrusHappy

    label casEnters: 
        play music "audio/music/Onycs - Shine.mp3" fadein 0.5 volume 0.5   
        "???" "Ah, yes. Welcome to Big Energy Corp."
        scene bg casnormal
        with dissolve
        cassandra "So..."
        cassandra "Tell me"
        cassandra "Are you excited to be here?"
    menu:
        "Yes I am!":
            jump CasHappy
            
        "No, I'm not":
            jump CasDisgust

label cyrusNormal:
    cyrus "I see"
    cyrus "..."
    you "..."
    jump casEnters

#cyrus is happy scenario
label cyrusHappy:
    $cyAf += 5
    cyrus "..."
    cyrus "First time I've heard someone at this company say that"
    scene bg cysmile
    with dissolve
    cyrus "You might just..."
    jump casEnters

#Cassandra is happy scenario 
label CasHappy:
    cassandra "..."
    scene bg cassmile
    with dissolve
    cassandra "Well, why wouldn't you be? After all, we do some amazing work here."
    $ casAf += 5
    jump Common

#Cassandra is disguted with you scenario
label CasDisgust:
    cassandra "..."
    scene bg casdisgust
    with dissolve
    cassandra "Well, then why are you here"
    $ casAf -= 5
    jump Common


#Common scenario
label Common:
    #Casssandra sprite TBA
    #generic office back ground as replacement
    scene bg corridor
    with fade
    #Casual music
    stop music fadeout 1.0
    play music "audio/Music/Corporate Motivational (loop).mp3" fadein 1.5 volume 0.5

    
    cassandra "Big. Eneregy. Corp. is solely responsible for ensuring new up-and-coming residential districts get electricity."
    cassandra "And with you as out Chief energy coordinator, you get the priviledge of determining where that energy comes from."
    cassandra "I was in your shoes a long time ago, and I made very cost-efficient choices and look at me now!"
    you "hehehehe...Oh yeah?"
    cassandra "If I have one piece of advice to give you"
    cassandra "It's to..."
    cassandra "{b}SAVE{w=1.0} MONEY!!!{w}{/b}"
    cassandra "Money makes the world go round, wouldn't be here without it"
    
    cassandra "Anyway, here's your cubicle."
    scene bg youcubicle
    with dissolve
    cassandra "The Harminee project should be coming your way in the next few hours. I expect great things!"
    #foot steps sounds TBA

    you "(Oh boy)"
    scene bg cubicle
    with dissolve
    you "Well, guess I'll..."
    play sound "audio/Sound/door-knock-47175.mp3"
    "KNOCK KNOCK" with hpunch
    you "Wahhhhhh!!!"
    #energetic music TBA
    scene bg barry
    with fade
    "???" "Sup bro, so you are the new guy?"
    you "Hey, who are you?"
    "???" "Your co-worker! I'm Barry just a couple cubicles down. Thought I'd say hi to the new guy..."
    barry "Oh you are a girl"
    barry "..."
    barry "Anyway, anything I can help with?"
    barry "First day's always a little overwhelming. I still remember my first day..."
    you "Uh..."
    barry "Need me to show you the ropes?"
    you "Yeah...that'd be great Ahahahahaha..."
    barry "Don't worry about it, I was just like you once. Here, lemme show you how this works."
    jump end

label end:
    scene bg title
    with dissolve
    $ renpy.pause(2.0)
    return
