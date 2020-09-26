import pygame
import mapper

pygame.init()

def main():
  screen = pygame.display.set_mode([500, 500])
  m = mapper.Map(1785852800490497919)
  m.set_name("Diamond Seed")
  m.set_coordiantes(237,64,113)

  running = True
  while running:
    for event in pygame.event.get():  
      if event.type == pygame.QUIT:
        running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0,0,255),(m.coordinates.x,m.coordinates.z),5)
    pygame.display.flip()

if __name__ == "__main__":
  main()