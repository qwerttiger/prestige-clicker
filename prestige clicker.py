import pygame
pygame.init()
screen=pygame.display.set_mode([700,700])
pygame.display.set_caption("Prestige Clicker")
screen.fill((255,255,255))
pygame.draw.rect(screen,(0,0,0),pygame.Rect(200,50,300,75),2)
gold=0
while True:
  for event in pygame.event.get():
    if event.type==pygame.MOUSEBUTTONDOWN:
      pos=pygame.mouse.get_pos()
      if 200<=pos[0]<=500 and 50<=pos[1]<=125:
        gold+=1
    if event.type==pygame.QUIT:
      pygame.quit()
  pygame.display.flip()
  print(gold)
