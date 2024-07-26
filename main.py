import pygame,random

pygame.init()

def draw(window,data):
    window.fill((0,0,0))
    x = 0
    for i in data:
        rect = pygame.rect.Rect(x*(window.get_width()/len(data)),window.get_height()-(i*window.get_height()),(window.get_width()/len(data)),i*window.get_height())
        pygame.draw.rect(window,(0,255,255),rect,3)
        x += 1


    pygame.display.update()

def main():
    window = pygame.display.set_mode((1500,600))
    runing = True
    data = [i/100 for i in range(1,100)]
    random.shuffle(data)

    draw(window,data)
    isSorted = False
    while runing:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                runing = False
        if (not isSorted):
            for n in range(len(data)-1,0,-1):
                for i in range(n):
                    if data[i] > data[i + 1]:
                        data[i], data[i + 1] = data[i + 1], data[i]
                        draw(window,data)
        
            isSorted = True

   
    pygame.quit()


if (__name__ == "__main__"):
    main()