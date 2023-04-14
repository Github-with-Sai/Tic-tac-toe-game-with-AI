#importing and intialising pygame
import pygame
pygame.init()
import pygame.mixer
pygame.mixer.init()

#creating a display surface and naming it
screen=pygame.display.set_mode((1000,650))
pygame.display.set_caption("Tic Tac Toe")

#initialising the colours
white,black=(255,255,255),(0,0,0)
light_brown,dark_brown,bg_brown,bord_brown=(239,221,111),(96,61,2),(205,133,63),(128,0,0)
red,green,blue=(255,0,0),(0,255,0),(0,0,255)
golden_yellow=(255,223,0)


                                        # *****Loading screen with bar column*****

#designing loading screen
    #---screen's border and lining---
screen.fill(bg_brown)
pygame.draw.rect(screen,black,(0,0,1000,650),5)
    #---loading bar column
pygame.draw.rect(screen,black,(196,446,608,18),border_radius=5)
pygame.draw.rect(screen,dark_brown,(200,450,600,10),border_radius=5)
    #---text -"Loading"
text="     Loading..."
font=pygame.font.SysFont("Calibri",35) 
text=font.render(text,True,black,bg_brown)
screen.blit(text,(400,400))

#loop for loading process
while True:
    pygame.draw.rect(screen,light_brown,(200,450,20,10),border_radius=5)
    pygame.display.update()
    pygame.time.delay(500)
    #loading and resizing the images
    while True:
        openning_image=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\tic tac toe game openning image.jpg")
        openning_image=pygame.transform.scale(openning_image,(960,610))
        ticky_bot_image=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\ticky bot image.png")
        taca_bot_image=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\taca bot image.png")
        tony_bot_image=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\tony bot image.png")
        x_image=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\X image.png")
        o_image=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\O image.png")
        x_image_board=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\X image.png")
        o_image_board=pygame.image.load("D:\\Tic tac toe game files\\tic tac toe game related images\\O image.png")
        break
    pygame.draw.rect(screen,light_brown,(200,450,150,10),border_radius=5)
    pygame.display.update()
    pygame.time.delay(500)
    #loading the sounds and musics
    while True:
        openning_music=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\tic tac toe game openning music.mp3")
        mouse_clicking_sound=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\mouse clicking sound.mp3")
        mouse_misclicking_sound=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\mouse misclicking sound.wav")
        message_box_sound=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\message popping sound.wav")
        game_music=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\tic tac toe game music.mp3")
        winning_sound=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\winning sound.wav")
        loosing_sound=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\loosing sound.wav")
        draw_sound=pygame.mixer.Sound("D:\\Tic tac toe game files\\tic tac toe game related musics and sounds\\draw sound.wav")
        break
    pygame.draw.rect(screen,light_brown,(200,450,300,10),border_radius=5)
    pygame.display.update()
    loading_screen_copy=screen.copy()
    pygame.time.delay(500)
    #finding the mouse points for buttons
    while True:
        #---play button---
        play_button_size=(100,50)
        play_button_position=(850,50)
        play_button=pygame.draw.rect(screen,bg_brown,(850,50,100,50))
        #---ticky bot button---
        ticky_button_size=(200,200)
        ticky_button_position=(100,200)
        ticky_button=pygame.draw.rect(screen,bg_brown,(100,200,200,200))
        #---taca bot button---
        taca_button_size=(200,200)
        taca_button_position=(400,200)
        taca_button=pygame.draw.rect(screen,bg_brown,(400,200,200,200))
        #---tony bot button---
        tony_button_size=(200,200)
        tony_button_position=(700,200)
        tony_button=pygame.draw.rect(screen,bg_brown,(700,200,200,200))
        #---next button---
        next_button_size=(100,50)
        next_button_position=(850,550)
        next_button=pygame.draw.rect(screen,bg_brown,(850,550,100,50))
        #---reset button---
        reset_button_size=(100,50)
        reset_button_position=(600,550)
        reset_button=pygame.draw.rect(screen,bg_brown,(600,550,100,50))
        #---change the bot button---
        change_bot_button_size=(200,50)
        change_bot_button_position=(750,550)
        change_bot_button=pygame.draw.rect(screen,bg_brown,(750,550,200,50))
        #---board buttons---
        loc11=pygame.draw.rect(screen,bg_brown,(100,100,150,150))
        loc12=pygame.draw.rect(screen,bg_brown,(250,100,150,150))
        loc13=pygame.draw.rect(screen,bg_brown,(400,100,150,150))
        loc21=pygame.draw.rect(screen,bg_brown,(100,250,150,150))
        loc22=pygame.draw.rect(screen,bg_brown,(250,250,150,150))
        loc23=pygame.draw.rect(screen,bg_brown,(400,250,150,150))
        loc31=pygame.draw.rect(screen,bg_brown,(100,400,150,150))
        loc32=pygame.draw.rect(screen,bg_brown,(250,400,150,150))
        loc33=pygame.draw.rect(screen,bg_brown,(400,400,150,150))
        #---play again button---
        play_again_button_size=(100,50)
        play_again_button_position=(350,350)
        play_again_button=pygame.draw.rect(screen,dark_brown,(350,350,100,50))
        #---re-try button---
        retry_button_size=(100,50)
        retry_button_position=(350,350)
        retry_button=pygame.draw.rect(screen,dark_brown,(350,350,100,50))
        #---exit button---
        exit_button_size=(100,50)
        exit_button_position=(550,350)
        exit_button=pygame.draw.rect(screen,dark_brown,(550,350,100,50))
        #---yes button---
        yes_button_size=(100,50)
        yes_button_position=(350,350)
        yes_button=pygame.draw.rect(screen,dark_brown,(350,350,100,50))
        #---no button---
        no_button_size=(100,50)
        no_button_position=(550,350)
        no_button=pygame.draw.rect(screen,dark_brown,(550,350,100,50))
        #---start button---
        start_button_size=(100,50)
        start_button_position=(350,350)
        start_button=pygame.draw.rect(screen,dark_brown,(350,350,100,50))
        #---bots screen exit button---
        exit_b_button_size=(100,50)
        exit_b_button_position=(50,550)
        exit_b_button=pygame.draw.rect(screen,dark_brown,(50,550,100,50))        
        break
    screen.blit(loading_screen_copy,(0,0))
    pygame.draw.rect(screen,light_brown,(200,450,500,10),border_radius=5)
    pygame.display.update()
    pygame.time.delay(500)
    #creating a text pasting function
    while True:
        def wordings(word,size,position,bg_color):
            font=pygame.font.SysFont("Calibri",size) 
            text=font.render(word,True,black,bg_color)
            screen.blit(text,position)
            pygame.display.update()
        break
    pygame.draw.rect(screen,light_brown,(200,450,550,10),border_radius=5)
    pygame.display.update()
    pygame.time.delay(500)
    #creating a opacification function
    while True:
        def opacificate(surface_size,position,transperancy):
            surface_object=pygame.Surface(surface_size)
            surface_object.set_alpha(transperancy)
            screen.blit(surface_object,position)
            pygame.display.update()
        break
    pygame.draw.rect(screen,light_brown,(200,450,600,10),border_radius=5)
    pygame.display.update()
    pygame.time.delay(500)
    #breaking the loop
    break


                                        # *****First screen (openning screen)*****

#function for openning_screen
def openning_screen():
    #screen's border and lining
    screen.fill(bord_brown)
    pygame.draw.rect(screen,black,(0,0,1000,650),3)
    #pasting the image and lining
    screen.blit(openning_image,(20,20))
    pygame.draw.rect(screen,black,(20,20,960,610),2)
    #designing play button
    pygame.draw.rect(screen,dark_brown,(850,50,100,50))
    pygame.draw.rect(screen,black,(850,50,100,50),1)
    pygame.draw.rect(screen,light_brown,(855,55,90,40),border_radius=10)
    wordings("  Play",33,(860,60),light_brown)

#displaying the openning screen with music
openning_screen()
pygame.display.update()
openning_screen_copy=screen.copy()
openning_music.play()

#checking whether the play button is pressed or not in the openning_screen
message=message1=message2=""
while True:
    #plays the openning music if it ends
    if pygame.mixer.get_busy()==False:
        openning_music.play()
    #getting the events
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_point=pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_point):
                openning_music.stop()
                mouse_clicking_sound.play()
                opacificate(play_button_size,play_button_position,50)
                message1="enter"
            else:
                mouse_misclicking_sound.play()
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_point=pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_point):
                screen.blit(openning_screen_copy,(0,0))
                pygame.display.update()
                message2="enter"
        if event.type==pygame.KEYDOWN:
            mouse_misclicking_sound.play()
        if event.type==pygame.QUIT:
            pygame.quit()
    #breaking the loop 
    if message1==message2=="enter":
        break
pygame.time.delay(500)

#closing the openning screen with gradual darkening
a=0
while a<256:
    opacificate((1000,650),(0,0),a)
    pygame.display.update()
    screen.blit(openning_screen_copy,(0,0))
    a=a+1

    
                                        # *****Second screen(bots selection)*****

#funtion for bot selection screen
def bots_screen():
    global ticky_bot_image,taca_bot_image,tony_bot_image
    #game screen border and lining
    screen.fill(bord_brown)
    pygame.draw.rect(screen,black,(0,0,1000,650),3)
    #game screen background with lining
    pygame.draw.rect(screen,bg_brown,(20,20,960,610),border_radius=25)
    pygame.draw.rect(screen,black,(20,20,960,610),3,border_radius=25)
    #designing buttons for bot selecting
        #----ticky bot button border,background,image
    ticky_bot_image=pygame.transform.scale(ticky_bot_image,(180,180))
    pygame.draw.rect(screen,dark_brown,(100,200,200,200))
    pygame.draw.rect(screen,black,(100,200,200,200),1)
    pygame.draw.rect(screen,light_brown,(110,210,180,180))
    screen.blit(ticky_bot_image,(110,210))
    wordings("          Ticky",30,(100,400),bg_brown)
        #----taca bot button border,background,image
    taca_bot_image=pygame.transform.scale(taca_bot_image,(180,180))
    pygame.draw.rect(screen,dark_brown,(400,200,200,200))
    pygame.draw.rect(screen,black,(400,200,200,200),1)
    pygame.draw.rect(screen,light_brown,(410,210,180,180))
    screen.blit(taca_bot_image,(410,210))
    wordings("           Taca",30,(400,400),bg_brown)
        #----tony bot button border,background,image
    tony_bot_image=pygame.transform.scale(tony_bot_image,(180,180))
    pygame.draw.rect(screen,dark_brown,(700,200,200,200))
    pygame.draw.rect(screen,black,(700,200,200,200),1)
    pygame.draw.rect(screen,light_brown,(710,210,180,180))
    screen.blit(tony_bot_image,(710,210))
    wordings("           Tony",30,(700,400),bg_brown)
    #designing next button
    pygame.draw.rect(screen,dark_brown,(850,550,100,50))
    pygame.draw.rect(screen,black,(850,550,100,50),1)
    pygame.draw.rect(screen,light_brown,(855,555,90,40),border_radius=10)
    wordings("  Next",30,(860,560),light_brown)
    #designing exit button
    pygame.draw.rect(screen,dark_brown,(50,550,100,50))
    pygame.draw.rect(screen,black,(50,550,100,50),1)
    pygame.draw.rect(screen,light_brown,(55,555,90,40),border_radius=10)
    wordings("  Exit",30,(60,560),light_brown)

#displaying the bot selection screen with flash screen
bots_screen()
bots_screen_copy=screen.copy()
pygame.display.update()

#popping the message box 
pygame.time.delay(500)
message_box_sound.play()
pygame.draw.rect(screen,dark_brown,(150,50,700,100),border_radius=30)
pygame.draw.rect(screen,black,(150,50,700,100),1,border_radius=30)
pygame.draw.rect(screen,light_brown,(155,55,690,90),border_radius=30)
pygame.draw.rect(screen,light_brown,(155,55,690,90),1,border_radius=30)
wordings(" Select any one of these bots as your opponent...",30,(200,83),light_brown)
bots_screen_copy=screen.copy()

#getting the selected bot
bot=""
message1=message2=""
while True:
    #getting the events
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_point=pygame.mouse.get_pos()
            if ticky_button.collidepoint(mouse_point):
                bot="ticky"
                mouse_clicking_sound.play()
                screen.blit(bots_screen_copy,(0,0))
                opacificate(ticky_button_size,ticky_button_position,50)
            elif taca_button.collidepoint(mouse_point):
                bot="taca"
                mouse_clicking_sound.play()
                screen.blit(bots_screen_copy,(0,0))
                opacificate(taca_button_size,taca_button_position,50)
            elif tony_button.collidepoint(mouse_point):
                bot="tony"
                mouse_clicking_sound.play()
                screen.blit(bots_screen_copy,(0,0))
                opacificate(tony_button_size,tony_button_position,50)
            elif next_button.collidepoint(mouse_point):
                if bot=="":
                    mouse_misclicking_sound.play()
                else:
                    mouse_clicking_sound.play()
                    opacificate(next_button_size,next_button_position,50)
                    message1="selected"
            elif exit_b_button.collidepoint(mouse_point):
                mouse_clicking_sound.play()
                opacificate(exit_b_button_size,exit_b_button_position,50)
                message1="exit"
            else:
                mouse_misclicking_sound.play()
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_point=pygame.mouse.get_pos()
            if next_button.collidepoint(mouse_point):
                screen.blit(bots_screen_copy,(0,0))
                pygame.display.update()
                message2="selected"
            if exit_b_button.collidepoint(mouse_point):
                screen.blit(bots_screen_copy,(0,0))
                pygame.display.update()
                message2="exit"
        if event.type==pygame.KEYDOWN:
            mouse_misclicking_sound.play()
        if event.type==pygame.QUIT:
            pygame.quit()
    #breaking the loop 
    if message1==message2=="selected" or message1==message2=="exit" :
        break
if message1==message2=="exit":
    pygame.time.delay(500)
    pygame.quit()
pygame.time.delay(500)

#closing the bot selection screen with gradual darkening
a=0
while a<256:
    opacificate((1000,650),(0,0),a)
    pygame.display.update()
    screen.blit(bots_screen_copy,(0,0))
    a=a+1
    

                    #---------third screen (main game screen)----------

#function for game screen designing
def game_screen(bot):
    #globalising the variables
    global ticky_bot_image,taca_bot_image,tony_bot_image,x_image,o_image
    #game screen border and lining
    screen.fill(bord_brown)
    pygame.draw.rect(screen,black,(0,0,1000,650),3)
    #game screen background with lining
    pygame.draw.rect(screen,bg_brown,(20,20,960,610),border_radius=25)
    pygame.draw.rect(screen,black,(20,20,960,610),3,border_radius=25)
    #game board border and lining
    pygame.draw.rect(screen,dark_brown,(80,80,490,490),border_radius=25)
    pygame.draw.rect(screen,black,(80,80,490,490),3,border_radius=25)
    #game board background and lining
    pygame.draw.rect(screen,light_brown,(100,100,450,450),border_radius=25)
    pygame.draw.rect(screen,black,(100,100,450,450),3,border_radius=25)
    #game bord grid lines
    pygame.draw.line(screen,dark_brown,(250,100),(250,550),5)
    pygame.draw.line(screen,dark_brown,(400,100),(400,550),5)
    pygame.draw.line(screen,dark_brown,(100,250),(550,250),5)
    pygame.draw.line(screen,dark_brown,(100,400),(550,400),5)
    #designing the buttons
        #---reset button---
    pygame.draw.rect(screen,dark_brown,(600,550,100,50))
    pygame.draw.rect(screen,black,(600,550,100,50),1)
    pygame.draw.rect(screen,light_brown,(605,555,90,40),border_radius=10)
    wordings("  Reset",27,(610,565),light_brown)
        #---change the bot button---
    pygame.draw.rect(screen,dark_brown,(750,550,200,50))
    pygame.draw.rect(screen,black,(750,550,200,50),1)
    pygame.draw.rect(screen,light_brown,(755,555,190,40),border_radius=10)
    wordings(" Change the bot",26,(760,565),light_brown)
    #placing bot with name 
    pygame.draw.rect(screen,dark_brown,(600,100,150,150))
    pygame.draw.rect(screen,black,(600,100,150,150),1)
    pygame.draw.rect(screen,light_brown,(605,105,140,140),border_radius=10)
    if bot=="ticky":
        ticky_bot_image=pygame.transform.scale(ticky_bot_image,(140,140))
        screen.blit(ticky_bot_image,(605,105))
    if bot=="taca":
        taca_bot_image=pygame.transform.scale(taca_bot_image,(140,140))
        screen.blit(taca_bot_image,(605,105))
    if bot=="tony":
        tony_bot_image=pygame.transform.scale(tony_bot_image,(140,140))
        screen.blit(tony_bot_image,(605,105))
    text=bot.capitalize()
    if bot=="taca" or bot=="tony":
        wordings("       "+text,29,(600,260),bg_brown)
    else:
        wordings("      "+text,29,(600,260),bg_brown)
    x_image=pygame.transform.scale(x_image,(50,50))
    screen.blit(x_image,(650,50))
    #placing the player image 
    pygame.draw.rect(screen,dark_brown,(800,100,150,150))
    pygame.draw.rect(screen,black,(800,100,150,150),1)
    pygame.draw.rect(screen,light_brown,(805,105,140,140),border_radius=10)
    wordings(" You",29,(850,160),light_brown)
    o_image=pygame.transform.scale(o_image,(50,50))
    screen.blit(o_image,(850,50))
   
#displaying the game screen with flash screen
game_screen(bot)
game_screen_copy=screen.copy()
pygame.display.update()
pygame.time.delay(1000)

#popping start message box
    #---opacificating the screen
opacificate((1000,650),(0,0),100)
    #---popping message box
pygame.draw.rect(screen,dark_brown,(300,250,400,200),border_radius=30)
pygame.draw.rect(screen,black,(300,250,400,200),1,border_radius=30)
pygame.draw.rect(screen,light_brown,(310,260,380,180),border_radius=30)
pygame.draw.rect(screen,light_brown,(310,260,380,180),1,border_radius=30)
wordings("  Can we start the game ?",30,(340,300),light_brown)
    #---designing "Start" button in message box  
pygame.draw.rect(screen,dark_brown,(350,350,100,50))
pygame.draw.rect(screen,black,(350,350,100,50),1)
pygame.draw.rect(screen,light_brown,(355,355,90,40),border_radius=10)
wordings("    Start",20,(360,365),light_brown)
    #---designing "exit" button in message box  
pygame.draw.rect(screen,dark_brown,(550,350,100,50))
pygame.draw.rect(screen,black,(550,350,100,50),1)
pygame.draw.rect(screen,light_brown,(555,355,90,40),border_radius=10)
wordings("     Exit",20,(560,365),light_brown)
    #---message box sound
message_box_sound.play()

#checking whether the start button is pressed or not
screen_copy=screen.copy()
message1=message2=""
while True:
    #getting the events
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_point=pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_point):
                mouse_clicking_sound.play()
                opacificate(start_button_size,start_button_position,50)
                message1="start"
            elif exit_button.collidepoint(mouse_point):
                mouse_clicking_sound.play()
                opacificate(exit_button_size,exit_button_position,50)
                message1="exit"
            else:
                mouse_misclicking_sound.play()
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_point=pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_point):
                screen.blit(screen_copy,(0,0))
                pygame.display.update()
                message2="start"
            if exit_button.collidepoint(mouse_point):
                screen.blit(screen_copy,(0,0))
                pygame.display.update()
                message2="exit"  
        if event.type==pygame.KEYDOWN:
            mouse_misclicking_sound.play()
        if event.type==pygame.QUIT:
            pygame.quit()
    #breaking the loop 
    if message1==message2=="start" or message1==message2=="exit" :
        break
if message1==message2=="exit":
    pygame.time.delay(500)
    pygame.quit()
pygame.time.delay(500)

#displaying the game screen 
screen.blit(game_screen_copy,(0,0))
game_music.play()
pygame.display.update()

#pre-game initialization
board=[ ["11","12","13"],
        ["21","22","23"],
        ["31","32","33"] ]
loc_pos={"11":(100,100),"12":(250,100),"13":(400,100),
         "21":(100,250),"22":(250,250),"23":(400,250),
         "31":(100,400),"32":(250,400),"33":(400,400)}
player_loc=""
player_locs=[]
bot_loc=""
bot_locs=[]

#game function
def game():
    #globalising the variables
    global x_image_board,o_image_board,player_locs,bot_locs,player_loc,bot_loc,board
    #highlighting the player's turn
    pygame.time.delay(500)
        #---repasting bot image
    pygame.draw.rect(screen,dark_brown,(600,100,150,150))
    pygame.draw.rect(screen,black,(600,100,150,150),1)
    pygame.draw.rect(screen,light_brown,(605,105,140,140),border_radius=10)
    if bot=="ticky":
        screen.blit(ticky_bot_image,(605,105))
    if bot=="taca":
        screen.blit(taca_bot_image,(605,105))
    if bot=="tony":
        screen.blit(tony_bot_image,(605,105))
    pygame.display.update()
        #---replasting players dummy
    pygame.draw.rect(screen,dark_brown,(800,100,150,150))
    pygame.draw.rect(screen,black,(800,100,150,150),1)
    pygame.draw.rect(screen,light_brown,(805,105,140,140),border_radius=10)
    wordings(" You",29,(850,160),light_brown)
    pygame.display.update()
        #---darkenning the bot
    opacificate((150,150),(600,100),100)
        #---message box
    pygame.draw.rect(screen,dark_brown,(650,350,250,100),border_radius=30)
    pygame.draw.rect(screen,black,(650,350,250,100),1,border_radius=30)
    pygame.draw.rect(screen,light_brown,(655,355,240,90),border_radius=30)
    pygame.draw.rect(screen,black,(655,355,240,90),1,border_radius=30)
    wordings("Your 's turn...",30,(700,383),light_brown)
    #storing the screen changes
    screen_copy=screen.copy()
    # turn of the player: getting the location and placing O in board and board list
    message1=message2=""
    while True:
        #playing the music
        if pygame.mixer.get_busy()==False:
            game_music.play()
        #getting the events
        player_loc=""
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_point=pygame.mouse.get_pos()
                o_image_board=pygame.transform.scale(o_image_board,(150,150))
                if loc11.collidepoint(mouse_point):
                    player_loc="11"
                elif loc12.collidepoint(mouse_point):
                    player_loc="12"
                elif loc13.collidepoint(mouse_point):
                    player_loc="13"
                elif loc21.collidepoint(mouse_point):
                    player_loc="21"
                elif loc22.collidepoint(mouse_point):
                    player_loc="22"
                elif loc23.collidepoint(mouse_point):
                    player_loc="23"
                elif loc31.collidepoint(mouse_point):
                    player_loc="31"
                elif loc32.collidepoint(mouse_point):
                    player_loc="32"
                elif loc33.collidepoint(mouse_point):
                    player_loc="33"
                elif reset_button.collidepoint(mouse_point):
                    opacificate(reset_button_size,reset_button_position,50)
                    game_music.stop()
                    mouse_clicking_sound.play()
                    message1="reset"
                elif change_bot_button.collidepoint(mouse_point):
                    opacificate(change_bot_button_size,change_bot_button_position,50)
                    game_music.stop()
                    mouse_clicking_sound.play()
                    message1="change bot"
                else:
                    mouse_misclicking_sound.play()
            if event.type==pygame.MOUSEBUTTONUP:
                mouse_point=pygame.mouse.get_pos()
                if reset_button.collidepoint(mouse_point):
                    screen.blit(screen_copy,(0,0))
                    pygame.display.update()
                    message2="reset"
                if change_bot_button.collidepoint(mouse_point):
                    screen.blit(screen_copy,(0,0))
                    pygame.display.update()
                    message2="change bot"
            if event.type==pygame.KEYDOWN:
                mouse_misclicking_sound.play()
            if event.type==pygame.QUIT:
                pygame.quit()
        #breaking the loop
        if player_loc!="":
            if player_loc not in player_locs and player_loc not in bot_locs:
                mouse_clicking_sound.play()
                rnum=int(player_loc[0])-1
                cnum=int(player_loc[1])-1
                board[rnum][cnum]="O"
                player_locs=player_locs+[player_loc]
                screen.blit(o_image_board,loc_pos[player_loc])
                pygame.display.update()
                break
            else:
                mouse_misclicking_sound.play()
        if message1==message2=="reset":
            break
        if message1==message2=="change bot":
            break
    if message1==message2=="reset":
        return "reset"
    if message1==message2=="change bot":
        return "change bot"   
    #checking whether the player won or match tied
    locs=[]
        #--horizontal--
    for r in range(0,3,1):
        count=0
        for c in range(0,3,1):
            if board[r][c]=="O":
                locs=locs+[str(r+1)+str(c+1)]
                count=count+1
        if count==3:
            locs=locs+["player won"]
            return locs
        else:
            locs=[]
        #--vertical--
    for r in range(0,3,1):
        count=0
        for c in range(0,3,1):
            if board[c][r]=="O":
                locs=locs+[str(c+1)+str(r+1)]
                count=count+1
        if count==3:
            locs=locs+["player won"]
            return locs
        else:
            locs=[]
        #--first digonal
    count=r=c=0
    for a in range(3):
        if board[r][c]=="O":
            locs=locs+[str(r+1)+str(c+1)]
            count=count+1
        r=r+1
        c=c+1
    if count==3:
        locs=locs+["player won"]
        return locs
    else:
        locs=[]
        #--second diagnol--
    count,c,r=0,0,2
    for a in range(3):
        if board[r][c]=="O":
            locs=locs+[str(r+1)+str(c+1)]
            count=count+1
        r=r-1
        c=c+1
    if count==3:
        locs=locs+["player won"]
        return locs
    else:
        locs=[]
        #--for match tie
    draw,q="yes",0
    for r in board:
        for c in r:
            if c!="O" and c!="X":
                draw="no"
                q=1
                break
        if q==1:
            break
    if draw=="yes":
        return "match tied"
    #highlighting the turn of the bot
    pygame.time.delay(500)
        #---repasting bot image
    pygame.draw.rect(screen,dark_brown,(600,100,150,150))
    pygame.draw.rect(screen,black,(600,100,150,150),1)
    pygame.draw.rect(screen,light_brown,(605,105,140,140),border_radius=10)
    if bot=="ticky":
        screen.blit(ticky_bot_image,(605,105))
    if bot=="taca":
        screen.blit(taca_bot_image,(605,105))
    if bot=="tony":
        screen.blit(tony_bot_image,(605,105))
    pygame.display.update()
        #---replasting players dummy
    pygame.draw.rect(screen,dark_brown,(800,100,150,150))
    pygame.draw.rect(screen,black,(800,100,150,150),1)
    pygame.draw.rect(screen,light_brown,(805,105,140,140),border_radius=10)
    wordings(" You",29,(850,160),light_brown)
    pygame.display.update()
        #---darkenning the player
    opacificate((150,150),(800,100),100)
        #---message box
    pygame.draw.rect(screen,dark_brown,(650,350,250,100),border_radius=30)
    pygame.draw.rect(screen,black,(650,350,250,100),1,border_radius=30)
    pygame.draw.rect(screen,light_brown,(655,355,240,90),border_radius=30)
    pygame.draw.rect(screen,black,(655,355,240,90),1,border_radius=30)
    wordings(bot.capitalize()+"'s turn...",30,(700,383),light_brown)
    #turn of the bot: getting the location and placing X in board and board list
    pygame.time.delay(2000)
    x_image_board=pygame.transform.scale(x_image_board,(150,150))
        #---Tony's game
    if bot=="tony":
        b=count=0
        # Tony's game loop starts
        while True:
            # to place X at correct position for winning
            diagnol_ranges=[ ["11","22","33"],["13","22","31"] ]
            vertical_ranges=[ ["11","21","31"],["12","22","32"],["13","23","33"] ]
            horizontal_ranges=[ ["11","12","13"],["21","22","23"],["31","32","33"] ]
            import random
            ran_arrange=random.randint(1,3)
            if ran_arrange==1:
                tot_ranges= diagnol_ranges+vertical_ranges+horizontal_ranges
            if ran_arrange==2:
                tot_ranges= vertical_ranges+horizontal_ranges+diagnol_ranges
            if ran_arrange==3:
                tot_ranges= horizontal_ranges+diagnol_ranges+vertical_ranges
            for rang in tot_ranges:
                dummy_rang=list(rang)
                for element in rang:
                    r=int(element[0])-1
                    c=int(element[1])-1
                    if board[r][c]=="X":
                        dummy_rang.remove(element)
                        count=count+1   
                if count==2:
                    bot_loc=dummy_rang[0]
                    rnum=int(bot_loc[0])-1
                    cnum=int(bot_loc[1])-1
                    if bot_loc not in bot_locs and bot_loc not in player_locs:
                        board[rnum][cnum]="X"
                        bot_locs=bot_locs+[bot_loc]
                        screen.blit(x_image_board,loc_pos[bot_loc])
                        pygame.display.update()
                        b=1
                        break
                count=0
                if b==1:
                    break
            if b==1:
                break
            # to place X at correct position for resisting the victory of the opponent
            diagnol_ranges=[ ["11","22","33"],["13","22","31"] ]
            vertical_ranges=[ ["11","21","31"],["12","22","32"],["13","23","33"] ]
            horizontal_ranges=[ ["11","12","13"],["21","22","23"],["31","32","33"] ]
            import random
            ran_arrange=random.randint(1,3)
            if ran_arrange==1:
                tot_ranges= diagnol_ranges+vertical_ranges+horizontal_ranges
            if ran_arrange==2:
                tot_ranges= vertical_ranges+horizontal_ranges+diagnol_ranges
            if ran_arrange==3:
                tot_ranges= horizontal_ranges+diagnol_ranges+vertical_ranges
            for rang in tot_ranges:
                dummy_rang=list(rang)
                for element in rang:
                    r=int(element[0])-1
                    c=int(element[1])-1
                    if board[r][c]=="O":
                        dummy_rang.remove(element)
                        count=count+1
                if count==2:
                    bot_loc=dummy_rang[0]
                    rnum=int(bot_loc[0])-1
                    cnum=int(bot_loc[1])-1
                    if bot_loc not in bot_locs and bot_loc not in player_locs:
                        board[rnum][cnum]="X"
                        bot_locs=bot_locs+[bot_loc]
                        screen.blit(x_image_board,loc_pos[bot_loc])
                        pygame.display.update()
                        b=1
                        break
                count=0
                if b==1:
                    break
            if b==1:
                break
            #tony's own move in positioning of X 
            diagnol_ranges=[ ["11","22","33"],["13","22","31"] ]
            vertical_ranges=[ ["11","21","31"],["12","22","32"],["13","23","33"] ]
            horizontal_ranges=[ ["11","12","13"],["21","22","23"],["31","32","33"] ]
            tot_ranges=horizontal_ranges+vertical_ranges+diagnol_ranges
            waste_range=""
            for rang in tot_ranges:
                for element in rang:
                    r=int(element[0])-1
                    c=int(element[1])-1
                    if board[r][c]=="O" :
                        waste_range="yes"
                        break
                if waste_range=="yes":
                    continue
                n=len(rang)
                for x in rang:
                    import random
                    bot_loc=rang[random.randint(0,(n-1))]
                    if bot_loc not in bot_locs and bot_loc not in player_locs:
                        r=int(bot_loc[0])-1
                        c=int(bot_loc[1])-1
                        board[r][c]="X"
                        bot_locs=bot_locs+[bot_loc]
                        screen.blit(x_image_board,loc_pos[bot_loc])
                        pygame.display.update()
                        b=1
                        break
                if b==1:
                    break
            if b==1:
                break
            #to place X in any positions randomly
            locationsA=["11","12","13"]
            locationsB=["21","22","23"]
            locationsC=["31","32","33"]
            import random
            ran_arrange=random.randint(1,3)
            if ran_arrange==1:
                locations=locationsA+locationsB+locationsC
            if ran_arrange==2:
                locations=locationsB+locationsC+locationsA
            if ran_arrange==3:
                locations=locationsC+locationsA+locationsB
            n=len(locations)
            for x in locations:
                import random
                bot_loc=locations[random.randint(0,(n-1))]
                if bot_loc not in bot_locs and bot_loc not in player_locs:
                    rnum=int(bot_loc[0])-1
                    cnum=int(bot_loc[1])-1
                    board[rnum][cnum]="X"
                    bot_locs=bot_locs+[bot_loc]
                    screen.blit(x_image_board,loc_pos[bot_loc])
                    pygame.display.update()
                    b=1
                    break
            if b==1:
                break
        #---tacas game
    if bot=="taca":
        b=count=0
        # Taca's game loop starts
        while True:
            # to place X at correct position for winning
            diagnol_ranges=[ ["11","22","33"],["13","22","31"] ]
            vertical_ranges=[ ["11","21","31"],["12","22","32"],["13","23","33"] ]
            horizontal_ranges=[ ["11","12","13"],["21","22","23"],["31","32","33"] ]
            import random
            ran_arrange=random.randint(1,3)
            if ran_arrange==1:
                tot_ranges= diagnol_ranges+vertical_ranges+horizontal_ranges
            if ran_arrange==2:
                tot_ranges= vertical_ranges+horizontal_ranges+diagnol_ranges
            if ran_arrange==3:
                tot_ranges= horizontal_ranges+diagnol_ranges+vertical_ranges
            for rang in tot_ranges:
                dummy_rang=list(rang)
                for element in rang:
                    r=int(element[0])-1
                    c=int(element[1])-1
                    if board[r][c]=="X":
                        dummy_rang.remove(element)
                        count=count+1   
                if count==2:
                    bot_loc=dummy_rang[0]
                    rnum=int(bot_loc[0])-1
                    cnum=int(bot_loc[1])-1
                    if bot_loc not in bot_locs and bot_loc not in player_locs:
                        board[rnum][cnum]="X"
                        bot_locs=bot_locs+[bot_loc]
                        screen.blit(x_image_board,loc_pos[bot_loc])
                        pygame.display.update()
                        b=1
                        break
                count=0
                if b==1:
                    break
            if b==1:
                break
            #taca's own move in positioning of X
            diagnol_ranges=[ ["11","22","33"],["13","22","31"] ]
            vertical_ranges=[ ["11","21","31"],["12","22","32"],["13","23","33"] ]
            horizontal_ranges=[ ["11","12","13"],["21","22","23"],["31","32","33"] ]
            tot_ranges= vertical_ranges+horizontal_ranges+diagnol_ranges
            waste_range=""
            for rang in tot_ranges:
                for element in rang:
                    r=int(element[0])-1
                    c=int(element[1])-1
                    if board[r][c]=="O" :
                        waste_range="yes"
                        break
                if waste_range=="yes":
                    continue
                n=len(rang)
                for x in rang:
                    import random
                    bot_loc=rang[random.randint(0,(n-1))]
                    if bot_loc not in bot_locs and bot_loc not in player_locs:
                        r=int(bot_loc[0])-1
                        c=int(bot_loc[1])-1
                        board[r][c]="X"
                        bot_locs=bot_locs+[bot_loc]
                        screen.blit(x_image_board,loc_pos[bot_loc])
                        pygame.display.update()
                        b=1
                        break
                if b==1:
                    break
            if b==1:
                break
            #to place X in any positions randomly
            locationsA=["11","12","13"]
            locationsB=["21","22","23"]
            locationsC=["31","32","33"]
            import random
            ran_arrange=random.randint(1,3)
            if ran_arrange==1:
                locations=locationsA+locationsB+locationsC
            if ran_arrange==2:
                locations=locationsB+locationsC+locationsA
            if ran_arrange==3:
                locations=locationsC+locationsA+locationsB
            n=len(locations)
            for x in locations:
                import random
                bot_loc=locations[random.randint(0,(n-1))]
                if bot_loc not in bot_locs and bot_loc not in player_locs:
                    rnum=int(bot_loc[0])-1
                    cnum=int(bot_loc[1])-1
                    board[rnum][cnum]="X"
                    bot_locs=bot_locs+[bot_loc]
                    screen.blit(x_image_board,loc_pos[bot_loc])
                    pygame.display.update()
                    b=1
                    break
            if b==1:
                break
        #---tickys game
    if bot=="ticky":
        b=count=0
        # Ticky's game loop starts
        while True:
            #ticky's own move in positioning of X
            diagnol_ranges=[ ["11","22","33"],["13","22","31"] ]
            vertical_ranges=[ ["11","21","31"],["12","22","32"],["13","23","33"] ]
            horizontal_ranges=[ ["11","12","13"],["21","22","23"],["31","32","33"] ]
            tot_ranges= diagnol_ranges+vertical_ranges+horizontal_ranges
            waste_range=""
            for rang in tot_ranges:
                for element in rang:
                    r=int(element[0])-1
                    c=int(element[1])-1
                    if board[r][c]=="O" :
                        waste_range="yes"
                        break
                if waste_range=="yes":
                    continue
                n=len(rang)
                for x in rang:
                    import random
                    bot_loc=rang[random.randint(0,(n-1))]
                    if bot_loc not in bot_locs and bot_loc not in player_locs:
                        r=int(bot_loc[0])-1
                        c=int(bot_loc[1])-1
                        board[r][c]="X"
                        bot_locs=bot_locs+[bot_loc]
                        screen.blit(x_image_board,loc_pos[bot_loc])
                        pygame.display.update()
                        b=1
                        break
                if b==1:
                    break
            if b==1:
                break
            #to place X in any positions randomly
            locationsA=["11","12","13"]
            locationsB=["21","22","23"]
            locationsC=["31","32","33"]
            import random
            ran_arrange=random.randint(1,3)
            if ran_arrange==1:
                locations=locationsA+locationsB+locationsC
            if ran_arrange==2:
                locations=locationsB+locationsC+locationsA
            if ran_arrange==3:
                locations=locationsC+locationsA+locationsB
            n=len(locations)
            for x in locations:
                import random
                bot_loc=locations[random.randint(0,(n-1))]
                if bot_loc not in bot_locs and bot_loc not in player_locs:
                    rnum=int(bot_loc[0])-1
                    cnum=int(bot_loc[1])-1
                    board[rnum][cnum]="X"
                    bot_locs=bot_locs+[bot_loc]
                    screen.blit(x_image_board,loc_pos[bot_loc])
                    pygame.display.update()
                    b=1
                    break
            if b==1:
                break
    #checking whether the player won or match tied
    locs=[]
        #--horizontal--
    for r in range(0,3,1):
        count=0
        for c in range(0,3,1):
            if board[r][c]=="X":
                locs=locs+[str(r+1)+str(c+1)]
                count=count+1
        if count==3:
            locs=locs+["bot won"]
            return locs
        else:
            locs=[]
        #--vertical--
    for r in range(0,3,1):
        count=0
        for c in range(0,3,1):
            if board[c][r]=="X":
                locs=locs+[str(c+1)+str(r+1)]
                count=count+1
        if count==3:
            locs=locs+["bot won"]
            return locs
        else:
            locs=[]
        #--first digonal
    count=r=c=0
    for a in range(3):
        if board[r][c]=="X":
            locs=locs+[str(r+1)+str(c+1)]
            count=count+1
        r=r+1
        c=c+1
    if count==3:
        locs=locs+["bot won"]
        return locs
    else:
        locs=[]
        #--second diagnol--
    count,c,r=0,0,2
    for a in range(3):
        if board[r][c]=="X":
            locs=locs+[str(r+1)+str(c+1)]
            count=count+1
        r=r-1
        c=c+1
    if count==3:
        locs=locs+["bot won"]
        return locs
    else:
        locs=[]
        #--for match tie
    draw,q="yes",0
    for r in board:
        for c in r:
            if c!="X" and c!="O":
                draw="no"
                q=1
                break
        if q==1:
            break
    if draw=="yes":
        return "match tied"

#indefinite loop runs the game function repetedly
while True:
    #playing the music
    if pygame.mixer.get_busy()==False:
        game_music.play()
    #calling the game gunction
    output=game()
    #checking returned statements
    if type(output)==list:
        if output[3]=="player won":
            game_music.stop()
            pygame.time.delay(500)
            winning_sound.play()
            #highlighting the locations
            screen_copy=screen.copy()
            opacificate((450,450),(100,100),150)
            a=0
            while a<3:
                o_image_board=pygame.transform.scale(o_image_board,(150,150))
                screen.blit(o_image_board,loc_pos[output[a]])
                pygame.display.update()
                a=a+1
            pygame.time.delay(4000)
            screen.blit(screen_copy,(0,0))
            #opacificating the screen
            opacificate((1000,650),(0,0),100)
            #popping message box
            pygame.draw.rect(screen,dark_brown,(300,250,400,200),border_radius=30)
            pygame.draw.rect(screen,black,(300,250,400,200),1,border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),1,border_radius=30)
            wordings("You have won the game !!!",30,(340,300),light_brown)
            #designing "Play again" button in message box  
            pygame.draw.rect(screen,dark_brown,(350,350,100,50))
            pygame.draw.rect(screen,black,(350,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(355,355,90,40),border_radius=10)
            wordings("Play again",20,(360,365),light_brown)
            #designing "exit" button in message box  
            pygame.draw.rect(screen,dark_brown,(550,350,100,50))
            pygame.draw.rect(screen,black,(550,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(555,355,90,40),border_radius=10)
            wordings("     Exit",20,(560,365),light_brown)
            #message box sound
            message_box_sound.play()
            #checking whether the play again button is pressed or not
            screen_copy=screen.copy()
            message1=message2=""
            while True:
                #getting the events
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mouse_point=pygame.mouse.get_pos()
                        if play_again_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(play_again_button_size,play_again_button_position,50)
                            message1="play again"
                        elif exit_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(exit_button_size,exit_button_position,50)
                            message1="exit"
                        else:
                            mouse_misclicking_sound.play()
                    if event.type==pygame.MOUSEBUTTONUP:
                        mouse_point=pygame.mouse.get_pos()
                        if play_again_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="play again"
                        if exit_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="exit"   
                    if event.type==pygame.KEYDOWN:
                        mouse_misclicking_sound.play()
                    if event.type==pygame.QUIT:
                        pygame.quit()
                #breaking the loop 
                if message1==message2=="play again" or message1==message2=="exit":
                    break
            #resetting the game for playing again
            if message1==message2=="play again":
                screen.blit(game_screen_copy,(0,0))
                board=[ ["11","12","13"],
                        ["21","22","23"],
                        ["31","32","33"] ]
                player_loc=""
                player_locs=[]
                bot_loc=""
                bot_locs=[]
                pygame.time.delay(500)
                continue
            else:
                pygame.time.delay(500)
                pygame.quit()
                break
        if output[3]=="bot won":
            game_music.stop()
            pygame.time.delay(500)
            loosing_sound.play()
            #highlighting the locations
            screen_copy=screen.copy()
            opacificate((450,450),(100,100),150)
            a=0
            while a<3:
                x_image_board=pygame.transform.scale(x_image_board,(150,150))
                screen.blit(x_image_board,loc_pos[output[a]])
                pygame.display.update()
                a=a+1
            pygame.time.delay(4000)
            screen.blit(screen_copy,(0,0))
            #opacificating the screen
            opacificate((1000,650),(0,0),100)
            #popping message box
            pygame.draw.rect(screen,dark_brown,(300,250,400,200),border_radius=30)
            pygame.draw.rect(screen,black,(300,250,400,200),1,border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),1,border_radius=30)
            wordings("You have lost the game !!!",30,(340,300),light_brown)
            #designing "Play again" button in message box  
            pygame.draw.rect(screen,dark_brown,(350,350,100,50))
            pygame.draw.rect(screen,black,(350,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(355,355,90,40),border_radius=10)
            wordings("    Retry",20,(360,365),light_brown)
            #designing "exit" button in message box  
            pygame.draw.rect(screen,dark_brown,(550,350,100,50))
            pygame.draw.rect(screen,black,(550,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(555,355,90,40),border_radius=10)
            wordings("     Exit",20,(560,365),light_brown)
            #message box sound
            message_box_sound.play()
            #checking whether the retry button is pressed or not
            screen_copy=screen.copy()
            message1=message2=""
            while True:
                #getting the events
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mouse_point=pygame.mouse.get_pos()
                        if play_again_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(retry_button_size,retry_button_position,50)
                            message1="retry"
                        elif exit_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(exit_button_size,exit_button_position,50)
                            message1="exit"
                        else:
                            mouse_misclicking_sound.play()
                    if event.type==pygame.MOUSEBUTTONUP:
                        mouse_point=pygame.mouse.get_pos()
                        if retry_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="retry"
                        if exit_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="exit"  
                    if event.type==pygame.KEYDOWN:
                        mouse_misclicking_sound.play()
                    if event.type==pygame.QUIT:
                        pygame.quit()
                #breaking the loop 
                if message1==message2=="retry" or message1==message2=="exit":
                    break
            #resetting the game for retrying
            if message1==message2=="retry":
                screen.blit(game_screen_copy,(0,0))
                board=[ ["11","12","13"],
                        ["21","22","23"],
                        ["31","32","33"] ]
                player_loc=""
                player_locs=[]
                bot_loc=""
                bot_locs=[]
                pygame.time.delay(500)
                continue
            else:
                pygame.time.delay(500)
                pygame.quit()
                break
    if type(output)==str:
        if output=="reset":
            incomp_game_screen_copy=screen.copy()
            pygame.time.delay(500)
            #opacificating the board 
            opacificate((1000,650),(0,0),100)
            #popping message box
            pygame.draw.rect(screen,dark_brown,(300,250,400,200),border_radius=30)
            pygame.draw.rect(screen,black,(300,250,400,200),1,border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),1,border_radius=30)
            wordings("Do you want to reset the game ?",25,(340,300),light_brown)
            #designing "yes" button in message box  
            pygame.draw.rect(screen,dark_brown,(350,350,100,50))
            pygame.draw.rect(screen,black,(350,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(355,355,90,40),border_radius=10)
            wordings("      Yes",20,(360,365),light_brown)
            #designing "no" button in message box  
            pygame.draw.rect(screen,dark_brown,(550,350,100,50))
            pygame.draw.rect(screen,black,(550,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(555,355,90,40),border_radius=10)
            wordings("      No",20,(560,365),light_brown)
            #message box sound
            message_box_sound.play()
            #checking whether the yes button is pressed or not
            screen_copy=screen.copy()
            message1=message2=""
            while True:
                #getting the events
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mouse_point=pygame.mouse.get_pos()
                        if yes_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(yes_button_size,yes_button_position,50)
                            message1="reset"
                        elif no_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(no_button_size,no_button_position,50)
                            message1="continue"
                        else:
                            mouse_misclicking_sound.play()
                    if event.type==pygame.MOUSEBUTTONUP:
                        mouse_point=pygame.mouse.get_pos()
                        if yes_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="reset"
                        if no_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="continue"   
                    if event.type==pygame.KEYDOWN:
                        mouse_misclicking_sound.play()
                    if event.type==pygame.QUIT:
                        pygame.quit()
                #breaking the loop 
                if message1==message2=="reset" or message1==message2=="continue":
                    break
            #resetting the game
            if message1==message2=="reset":
                screen.blit(game_screen_copy,(0,0))
                board=[ ["11","12","13"],
                        ["21","22","23"],
                        ["31","32","33"] ]
                player_loc=""
                player_locs=[]
                bot_loc=""
                bot_locs=[]
                pygame.time.delay(500)
                continue
            else:
                pygame.time.delay(500)
                screen.blit(incomp_game_screen_copy,(0,0))
                pygame.display.update()
                continue
        if output=="change bot":
            pygame.time.delay(500)
            screen.blit(bots_screen_copy,(0,0))
            pygame.display.update()
            #getting the selected bot
            bot=""
            message1=message2=""
            while True:
            #getting the events
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mouse_point=pygame.mouse.get_pos()
                        if ticky_button.collidepoint(mouse_point):
                            bot="ticky"
                            mouse_clicking_sound.play()
                            screen.blit(bots_screen_copy,(0,0))
                            opacificate(ticky_button_size,ticky_button_position,50)
                        elif taca_button.collidepoint(mouse_point):
                            bot="taca"
                            mouse_clicking_sound.play()
                            screen.blit(bots_screen_copy,(0,0))
                            opacificate(taca_button_size,taca_button_position,50)
                        elif tony_button.collidepoint(mouse_point):
                            bot="tony"
                            mouse_clicking_sound.play()
                            screen.blit(bots_screen_copy,(0,0))
                            opacificate(tony_button_size,tony_button_position,50)
                        elif next_button.collidepoint(mouse_point):
                            if bot=="":
                                mouse_misclicking_sound.play()
                            else:
                                mouse_clicking_sound.play()
                                opacificate(next_button_size,next_button_position,50)
                                message1="selected"
                        elif exit_b_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(exit_b_button_size,exit_b_button_position,50)
                            message1="exit"
                        else:
                            mouse_misclicking_sound.play()
                    if event.type==pygame.MOUSEBUTTONUP:
                        mouse_point=pygame.mouse.get_pos()
                        if next_button.collidepoint(mouse_point):
                            screen.blit(bots_screen_copy,(0,0))
                            pygame.display.update()
                            message2="selected"
                        if exit_b_button.collidepoint(mouse_point):
                            screen.blit(bots_screen_copy,(0,0))
                            pygame.display.update()
                            message2="exit"        
                    if event.type==pygame.KEYDOWN:
                        mouse_misclicking_sound.play()
                    if event.type==pygame.QUIT:
                        pygame.quit()
                #breaking the loop 
                if message1==message2=="selected" or message1==message2=="exit":
                    break
            if message1==message2=="selected":
                pygame.time.delay(500)
                game_screen(bot)
                game_screen_copy=screen.copy()
                pygame.display.update()
                board=[ ["11","12","13"],
                        ["21","22","23"],
                        ["31","32","33"] ]
                player_loc=""
                player_locs=[]
                bot_loc=""
                bot_locs=[]
                continue
            if message1==message2=="exit":
                pygame.time.delay(500)
                pygame.quit()
        if output=="match tied":
            game_music.stop()
            pygame.time.delay(500)
            draw_sound.play()
            #highlighting the board
            screen_copy=screen.copy()
            opacificate((450,450),(100,100),150)
            pygame.time.delay(3000)
            screen.blit(screen_copy,(0,0))
            #opacificating the screen
            opacificate((1000,650),(0,0),100)
            #popping message box
            pygame.draw.rect(screen,dark_brown,(300,250,400,200),border_radius=30)
            pygame.draw.rect(screen,black,(300,250,400,200),1,border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),border_radius=30)
            pygame.draw.rect(screen,light_brown,(310,260,380,180),1,border_radius=30)
            wordings(" The game ended in tie!!!",30,(340,300),light_brown)
            #designing "Play again" button in message box  
            pygame.draw.rect(screen,dark_brown,(350,350,100,50))
            pygame.draw.rect(screen,black,(350,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(355,355,90,40),border_radius=10)
            wordings("    Retry",20,(360,365),light_brown)
            #designing "exit" button in message box  
            pygame.draw.rect(screen,dark_brown,(550,350,100,50))
            pygame.draw.rect(screen,black,(550,350,100,50),1)
            pygame.draw.rect(screen,light_brown,(555,355,90,40),border_radius=10)
            wordings("     Exit",20,(560,365),light_brown)
            #message box sound
            message_box_sound.play()
            #checking whether the retry button is pressed or not
            screen_copy=screen.copy()
            message1=message2=""
            while True:
                #getting the events
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mouse_point=pygame.mouse.get_pos()
                        if play_again_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(retry_button_size,retry_button_position,50)
                            message1="retry"
                        elif exit_button.collidepoint(mouse_point):
                            mouse_clicking_sound.play()
                            opacificate(exit_button_size,exit_button_position,50)
                            message1="exit"
                        else:
                            mouse_misclicking_sound.play()
                    if event.type==pygame.MOUSEBUTTONUP:
                        mouse_point=pygame.mouse.get_pos()
                        if retry_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="retry"
                        if exit_button.collidepoint(mouse_point):
                            screen.blit(screen_copy,(0,0))
                            pygame.display.update()
                            message2="exit"   
                    if event.type==pygame.KEYDOWN:
                        mouse_misclicking_sound.play()
                    if event.type==pygame.QUIT:
                        pygame.quit()
                #breaking the loop 
                if message1==message2=="retry" or message1==message2=="exit":
                    break
            #resetting the game for retrying
            if message1==message2=="retry":
                screen.blit(game_screen_copy,(0,0))
                board=[ ["11","12","13"],
                        ["21","22","23"],
                        ["31","32","33"] ]
                player_loc=""
                player_locs=[]
                bot_loc=""
                bot_locs=[]
                pygame.time.delay(500)
                continue
            else:
                pygame.time.delay(500)
                pygame.quit()
                break
            

"""
for a in range(0,1000,50):
    pygame.draw.line(screen,red,(a,0),(a,650),1)
for a in range(0,650,50):
    pygame.draw.line(screen,red,(0,a),(1000,a),1)
pygame.display.update()       
"""







