#Step2, Load background and cargo
import pygame

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True


player = pygame.image.load("player.png")

key_up=key_down=key_left=key_right = False
player_pos=[130,100]
screen.blit(player, player_pos)

#---------------------------------------------
#2.1 load more images
background = pygame.image.load("sky.jpg")
cargo = pygame.image.load("货.png")
#---------------------------------------------

while keep_going:

    screen.fill(0)
    
    #----------------------------------------
    #2.2 load the background
    screen.blit(background,(0,0))
    # if you image is small, you need use double loop to fill the background
    #for x in range( int(width/background.get_width())+1):
    #    for y in range(int(height/background.get_height())+1):
    #        screen.blit(background,(x*100,y*100))
    
    # 2.3 load the balloon cargo
    screen.blit(cargo,(0,30))
    screen.blit(cargo,(0,135))
    screen.blit(cargo,(0,240))
    screen.blit(cargo,(0,345))
    #----------------------------------------

    screen.blit(player, (130,100))
    
    pygame.display.flip() 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going = False

screen.blit(player, player_pos)
#3.3 monitor the key down and up
for event in pygame.event.get():
      if event.type==pygame.QUIT:
          keep_going = False
      if event.type == pygame.KEYDOWN:
          if event.key==pygame.K_w:
              key_up=True
          elif event.key==pygame.K_a:
              key_left=True
          elif event.key==pygame.K_s:
              key_down=True
          elif event.key==pygame.K_d:
              key_right=True
      if event.type == pygame.KEYUP:
          if event.key==pygame.K_w:
              key_up=False
          elif event.key==pygame.K_a:
              key_left=False
          elif event.key==pygame.K_s:
              key_down=False
          elif event.key==pygame.K_d:
              key_right=False

if key_up:
      player_pos[1]-=1
elif key_down:
      player_pos[1]+=1
if key_left:
      player_pos[0]-=1
elif key_right:
    player_pos[0]+=1


pygame.quit()
exit(0) 