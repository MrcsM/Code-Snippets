# this was used for my game design course, since we used pygame I wanted to test out mouse detection
# i created this, it does literally nothing except spawn a blue dot on a black screen wherever you click.
# like this was my 2nd day of game design class and i just wanted to make sure i knew what i was doing

import pygame

screen = pygame.display.set_mode((800, 800))

if __name__ == "__main__":
    locations = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                locations.append(pygame.mouse.get_pos())
                pygame.draw.circle(pygame.display.get_surface(), (0, 0, 255), pygame.mouse.get_pos(), 10)
                pygame.display.update()
        try: circle
        except NameError: circle = None
        if circle is not None:
            if circle.center in locations:
                pygame.draw.circle(pygame.display.get_surface(), (255, 0, 0), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 5)
            else:
                pygame.draw.circle(pygame.display.get_surface(), (0, 0, 0), circle.center, 5)
                circle = pygame.draw.circle(pygame.display.get_surface(), (255, 0, 0), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 5)
        pygame.display.flip()
