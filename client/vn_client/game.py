import pygame
import requests

API_URL = "http://127.0.0.1:5000"

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Visual Novel Client")
font = pygame.font.SysFont(None, 48)

def draw_text(text):
    screen.fill((30,30,30))
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (50, 250))
    pygame.display.flip()

def main():
    try:
        r = requests.get(API_URL)
        msg = r.json().get("message", "API not reachable")
    except Exception as e:
        msg = f"Error: {e}"

    draw_text(msg)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()