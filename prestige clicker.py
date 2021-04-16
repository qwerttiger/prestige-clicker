#imports
import pygame
import math
##################################################
pygame.init() #initialise pygame
screen=pygame.display.set_mode([700,700]) #set screen
pygame.display.set_caption("Prestige Clicker") #set caption
##################################################
#variables
points=0
totalpoints=0
metapoints=0
totalmetapoints=0
unlockedmeta=False
wscreen=0
upgrades=["0"]
##################################################
def drawtext(text,pos,size=30,colour=(0,0,0)): #draw text
  draw=pygame.font.SysFont("Arial",size).render(text,True,colour)
  screen.blit(draw,(pos[0]-draw.get_width()/2,pos[1]-draw.get_height()/2))
##################################################
while True: #main loop
  if points>=25: #unlock meta
    unlockedmeta=True
  for event in pygame.event.get(): #for every event
    if event.type==pygame.MOUSEBUTTONDOWN: #if click
      pos=pygame.mouse.get_pos() #get click position
      if 200<=pos[0]<=500 and 150<=pos[1]<=225 and wscreen==0: #if click +points
        points+=(1+dec(metapoints)/10)*(1+99*int(upgrades[0])) #add points
        totalpoints+=(1+dec(metapoints)/10)*(1+99*int(upgrades[0])) #add total points
      if 200<=pos[0]<=500 and 475<=pos[1]<=550 and unlockedmeta and points>=25 and wscreen==0: #if metapoints
        metapoints+=math.floor(math.sqrt(totalpoints)/5)-totalmetapoints #get metapoints
        totalmetapoints+=math.floor(math.sqrt(totalpoints)/5)-totalmetapoints #add total metapoints
        points=0 #reset points
      if 0<=pos[0]<=100 and 50<=pos[1]<=125 and metapoints>=1 and wscreen==1: #if buy upgrades
        metapoints-=1 #buy upgrades
        upgrades[0]="1" #get upgrade effect
      if pos[1]<50: #switch screen stuff
        if pos[0]<=233:
          wscreen=0
        elif pos[0]<=467:
          wscreen=1
        else:
          wscreen=2
    if event.type==pygame.QUIT: #if quitting pygame
      pygame.quit()
  #next stuff are drawing
  screen.fill((255,255,255))
  pygame.draw.line(screen,(0,0,0),(0,50),(700,50),2)
  pygame.draw.line(screen,(0,0,0),(233,0),(233,50),2)
  pygame.draw.line(screen,(0,0,0),(467,0),(467,50),2)
  drawtext("Points",(117,25),20)
  drawtext("Upgrades",(350,25),20)
  drawtext("Achievements",(583,25),20)
  if wscreen==0:
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(200,150,300,75),2)
    drawtext("+ "+str((1+dec(metapoints)/10)*(1+99*int(upgrades[0])))+" Points",(350,187))
    drawtext(str(points)+" Points",(350,90),80)
    if unlockedmeta:
      pygame.draw.rect(screen,(0,0,0),pygame.Rect(200,475,300,75),2)
      if points>=25:
        drawtext("+"+str(math.floor(math.sqrt(totalpoints)/5)-totalmetapoints)+" Meta-Points",(350,513))
      else:
        drawtext("+0 Meta-Points",(350,513))
      drawtext(str(metapoints)+" Meta-Points",(350,610),80)
  if wscreen==1:
    for i in range(100,701,100):
      pygame.draw.line(screen,(0,0,0),(i,50),(i,700),2)
    pygame.draw.line(screen,(0,0,0),(0,125),(700,125),2)
    for i in range(200,701,100):
      pygame.draw.line(screen,(0,0,0),(0,i),(700,i),2)
    if unlockedmeta:
      if upgrades[0]=="0":
        drawtext("Points x100: 1MP",(50,87),15)
      else:
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,50,100,75))
        drawtext("Points x100: 1MP",(50,87),15,(255,255,255))
  if wscreen==0:
     pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,233,50))
     drawtext("Points",(117,25),20,(255,255,255))
  if wscreen==1:
     pygame.draw.rect(screen,(0,0,0),pygame.Rect(233,0,234,50))
     drawtext("Upgrades",(350,25),20,(255,255,255))
  if wscreen==2:
     pygame.draw.rect(screen,(0,0,0),pygame.Rect(467,0,233,50))
     drawtext("Achievements",(583,25),20,(255,255,255))
  pygame.display.flip()
