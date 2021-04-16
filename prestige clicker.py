import pygame
import math
from decimal import Decimal as dec
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Prestige Clicker")
points=dec(0)
metapoints=0
unlockedmeta=False
def drawtext(text,pos,size=30,colour=(0,0,0)):
  draw=pygame.font.SysFont("Arial",size).render(text,True,colour)
  screen.blit(draw,(pos[0]-draw.get_width()/2,pos[1]-draw.get_height()/2))
while True:
  if points>=25:
    unlockedmeta=True
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
      pos=pygame.mouse.get_pos()
      if 200<=pos[0]<=500 and 150<=pos[1]<=225:
        points+=1+dec(metapoints)/10
      if 200<=pos[0]<=500 and 475<=pos[1]<=550 and unlockedmeta and points>=25:
        metapoints+=math.floor(math.sqrt(dec(points))/5)
        points=0
    if event.type==pygame.QUIT:
      pygame.quit()
  screen.fill((255,255,255))
  pygame.draw.line(screen,(0,0,0),(0,50),(700,50),2)
  pygame.draw.line(screen,(0,0,0),(233,0),(233,50),2)
  pygame.draw.line(screen,(0,0,0),(467,0),(467,50),2)
  pygame.draw.rect(screen,(0,0,0),pygame.Rect(200,150,300,75),2)
  drawtext("+ "+str(1+dec(metapoints)/10)+" Points",(350,187))
  drawtext(str(points)+" Points",(350,90),80)
  if unlockedmeta:
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(200,475,300,75),2)
    if points>=25:
      drawtext("+"+str(math.floor(math.sqrt(points)/5))+" Meta-Points",(350,513))
    else:
      drawtext("+0 Meta-Points",(350,513))
    drawtext(str(metapoints)+" Meta-Points",(350,610),80)
  pygame.display.flip()
