# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    renpy.music.register_channel("baby", "sfx", False)
    renpy.music.register_channel("kara", "sfx", False)
define g = Character("George")
define f = Character("Chuk")
define l = Character("Luka")
define c = Character("Caden")
image george = "george.png"
image anggeorge = "angrgeorge.png"
image embgeorge = "embgeorge.png"
image sadgeorge = "sadgeorge.png"
image hapgeorge = "happygeorge.png"
image bg1 = "rain.png"
image sasgeorge = "sassygeorge.png"
image bg2 = "concert.png"


# The game starts here.

label start:
    $ renpy.music.set_volume(0.5, .5, channel="music")
    $ renpy.music.set_volume(0.10, .10, channel="kara")
    $ renpy.music.set_volume(2, 2, channel="baby")
    play music "music.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
show george
"This is George. He is really gay and he wants to bang your father."

g "HELLO."
jump gay

label gay:
menu: 
    "What do you want to tell George?"
    
    "You're gay as fuck. What are you even wearing, that looks super homo.":
       $ say1 = "homo"
       g "Thanks mom."
    "You are so hot, wanna be my personal hooker?": 
        $ say1 = "hook"
        hide george
        show embgeorge
        g "Of course mom."

hide embgeorge
show george
g "So, how's your day going?"
jump hook
label hook:
menu:
    "What do you want to tell George?"
    
    "Alright, but it'd be even better if you killed yourself.":
        $ say2 = "kys"
        if say2 == "kys":
            hide george
            show sadgeorge
            g "I don't know how to tie a noose."
        jump noose
    
    "Horrible, now that you're in it.":
            if say1 == "homo":
                hide george
                show anggeorge
            g "Why are you being so mean mom?"
jump mean

label noose:
    menu:
        "What do you want to tell George?"
    
        "I can teach you if you'd like.":
            hide sadgeorge
            show hapgeorge
            g "Thanks mom!"
            "No problem bafoon."
            hide hapgeorge
            show sadgeorge
            g "I'm not a bafoon!"
            "Yes you are."
            hide sadgeorge
            show anggeorge
            g "No I'm not!!"
            "Lying is a sin, you're a bafoon."
            hide anggeorge
            show sasgeorge
            g "NO I NOT!"
            hide sasgeorge
            show anggeorge
            g "WHY ARE YOU BEING SO MEAN MOM?"
        "There are other ways to kill yourself you stupid bafoon.":
            if say1 == "hook": 
                hide sadgeorge
                show hapgeorge
                play sound "georgelaugh.mp3"
                g "XDDDDDDDDDD"
            if say1 == "homo":
                hide hapgeorge
                hide george
                show sadgeorge
                g "I'm not a bafoon!"
                "Yes you are."
                hide sadgeorge
                show anggeorge
                g "No I'm not!!"
                "Lying is a sin, you're a bafoon."
                hide anggeorge
                show sasgeorge
                g "NO I NOT!"
                hide sasgeorge
                show anggeorge
                g "WHY ARE YOU BEING SO MEAN MOM?"
    
    
        


label mean:
menu:
    "What do you want to tell George?"
    
    "My mother died a minute ago.":
        hide anggeorge
        hide george
        show sadgeorge
        g "Aww..."
        hide sadgeorge
        hide george
        show hapgeorge
        g "Is your dad single now?"
    "You're gay.":
        hide anggeorge
        show hapgeorge
        g "Thanks mom!"
g "Wanna see my Brittany Spears impression?"
        
menu:
    "Yes":
        pass
    "Yes":
        pass

$ renpy.music.stop(fadeout=1.0)
hide bg1
show bg2
show hapgeorge
play kara "karaoke.mp3"
play baby "baby.mp3"
g "Oh baby baby"
g "How was I supposeddd to knowwwwwwwww"
g "something wasn't riiiight heeeeeeeere"
g "Oh baby baby"
play music "music.mp3"
hide bg2
hide hapgeorge
show bg1
show hapgeorge
g "What did you think?"

menu:
    "What do you want to tell George?"
    
    "That was beautiful.":
        pass
    "That was amazing.":
        pass
    "That was fantastic":
        pass
    "That was magnificent.":
        pass
        
g "Thanks mom!"


        



    
    
    
    
        
        
    

    # This ends the game.

return
