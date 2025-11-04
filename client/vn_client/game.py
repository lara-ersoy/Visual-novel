import pygame, requests, io

API_SCENE = "http://127.0.0.1:5000/api/scene/intro"
STATIC_BASE = "http://127.0.0.1:5000/static/"

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Visual Novel Client")
font = pygame.font.SysFont(None, 48)

def wrap(text, width = 60):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if len(test) <= width
            cur = test
        else:
            lines.append(cur)
            cur = w 
        if cur: lines.append(cur)
        return lines 
    
def draw_box(lines, name = None):
    overlay = pygame.Surface((800, 160), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 440))
    y = 455
    if name:
        name_surf = font.render(name + ":", True, (255, 255, 0))
        screen.blit(name_surf, (20, y))
        y += 28
    for ln in lines:
        surf = font.render(ln, True, (255, 255, 255))
        screen.blit(surf, (20, y))
        y += 26

def main():
    # fetch scene
    scene = requests.get(API_SCENE, timeout=5).json()
    script = scene["script"]
    bg_name = script.get("background")
    dlg = script.get("dialogue", [])

    # load bg if present
    bg_image = None
    if bg_name:
        resp = requests.get(STATIC_BASE + bg_name, timeout=10)
        bg_image = pygame.image.load(io.BytesIO(resp.content)).convert_alpha()

    idx = 0
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN and e.key in (pygame.K_SPACE, pygame.K_RETURN):
                idx = (idx + 1) % max(1, len(dlg))

        if bg_image:
            screen.blit(pygame.transform.scale(bg_image, (800, 600)), (0, 0))
        else:
            screen.fill((30, 30, 30))

        if dlg:
            line = dlg[idx]
            name = line.get("speaker")
            lines = wrap(line.get("line", ""), width=70)
            draw_box(lines, name=name)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()