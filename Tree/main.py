import pygame

width = 1200
height = 750
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#FPS
fpsclock = pygame.time.Clock()
FPS = 30 
pygame.init()

# Cấu hình màn hình
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tree")
# Khởi tạo font
font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, link, size, index):
        self.surface =  pygame.image.load(link).convert_alpha()
        self.w, self.h = size
        self.x, self.y = index
        self.delta = 0
        self.surface = pygame.transform.scale(self.surface, size)
    
    def draw(self):
        surface_tempt = pygame.transform.scale(self.surface, (self.w - self.delta, self.h - self.delta))
        if(self.delta > 0 and self.delta < 10):
            #print(str(self.w - self.delta) + " " + str(self.h - self.delta) + "\n")
            self.delta += 3
        else:
            self.delta = 0;
        screen.blit(surface_tempt, (self.x - (self.w- self.delta)/2, self.y - (self.h- self.delta)/2))
        
    def click(self, x, y):
        if(x > self.x - self.w/2 and x < self.x + self.w/2 
           and y > self.y - self.h/6 and y < self.y + self.h/6):
            self.delta = 1
            return True
        return False
class Text:
    def __init__(self, link, link2, size, index):
        self.surface =  pygame.image.load(link).convert_alpha()
        self.w, self.h = size
        self.x, self.y = index
        self.surface = pygame.transform.scale(self.surface, (self.w , self.h/6))
        self.num = "0"
        self.mouse = 0
        self.mouse_surface =  pygame.image.load(link2).convert_alpha()
        self.mouse_surface = pygame.transform.scale(self.mouse_surface, (2 , self.h/6))
    
    def draw(self):
        screen.blit(self.surface, (self.x, self.y))
        if(self.mouse != 0):
            self.mouse += 1
            if(self.mouse % 7 == 0):
                screen.blit(self.mouse_surface, (self.x - 3 + len(self.num)*14, self.y))
                self.mouse = 1
        if(self.num == ""):
            self.num = "0"
        text_surface = font.render(str(self.num), True, BLACK)
        screen.blit(text_surface, (self.x, self.y))

    def click(self, x, y):
        if(x > self.x and x < self.x + self.w
           and y > self.y and y < self.y + self.h):
            self.mouse = 1
            return True
        return False
    def push(self, event):
        if(self.num == 0):
            return
        if event in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3,
                             pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                             pygame.K_8, pygame.K_9]:
                if(self.mouse != 0):
                    if self.num == "0":
                        self.num = str(event - 48)
                    else:
                        self.num += str(event - 48)
                print(event)
        elif event == pygame.K_BACKSPACE:
            if self.num != "0":
                self.num = self.num[:len(self.num) - 1]
class ButtonNode:
    def __init__(self, link, link2, size, index):
        self.surface1 =  pygame.image.load(link).convert_alpha()
        self.surface2 =  pygame.image.load(link2).convert_alpha()
        self.w, self.h = size
        self.x, self.y = index
        self.check = 0
        self.surface1 = pygame.transform.scale(self.surface1, size)
        self.surface2 = pygame.transform.scale(self.surface2, size)

    def draw(self):
        if self.check == 0:
            screen.blit(self.surface1, (self.x - (self.w)/2, self.y - (self.h)/2))
        else:
            screen.blit(self.surface2, (self.x - (self.w)/2, self.y - (self.h)/2))      
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def push(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        node_p = self.root
        while True:
            if node_p.value > value:
                if node_p.left is None:
                    node_p.left = Node(value)
                    return
                node_p = node_p.left
            elif node_p.value < value:
                if node_p.right is None:
                    node_p.right = Node(value)
                    return
                node_p = node_p.right
            else:
                return
    def inorder_print(self, start, bac, x):
        if start:
            if start.left:
                pygame.draw.line(screen, BLACK, ((800 + x, bac*100 + 200)), ((800 + (x - 150/(bac + 1)), (bac + 1)*100 + 200)))
                self.inorder_print(start.left, bac + 1, x - 150/(bac + 1))
            if start.right:
                pygame.draw.line(screen, BLACK, ((800 + x, bac*100 + 200)), ((800 + (x + 150/(bac + 1)), (bac + 1)*100 + 200)))
                self.inorder_print(start.right, bac + 1, x + 150/(bac + 1))

            node_surface = ButtonNode('./Tree/btn1.png', './Tree/btn2.png', (50, 50), (800 + x, bac*100 + 200))
            node_surface.draw()
            text_surface = font.render(str(start.value), True, BLACK)
            screen.blit(text_surface, (800 + x - len(str(start.value)*10), bac*100 + 190))

    def search(self, start, bac, x, value):
        if start:
            node_surface = ButtonNode('./Tree/btn1.png', './Tree/btn2.png', (50, 50), (800 + x, bac*100 + 200))
            node_surface.check = 1
            node_surface.draw()
            text_surface = font.render(str(start.value), True, BLACK)
            screen.blit(text_surface, (800 + x - len(str(start.value)*10), bac*100 + 190))
            pygame.display.update()
            fpsclock.tick(FPS/6)
            node_surface.check = 0
            node_surface.draw()
            text_surface = font.render(str(start.value), True, BLACK)
            screen.blit(text_surface, (800 + x - len(str(start.value)*10), bac*100 + 190))
            pygame.display.update()
            if start.value > value:
                self.search(start.left, bac + 1, x - 150/(bac + 1), value)
            elif start.value < value:
                self.search(start.right, bac + 1, x + 150/(bac + 1), value)
            else:
                fpsclock.tick(FPS/10)
                return True
        return False  
bg_surface = pygame.image.load('./Tree/bg.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (width, height))
btnInsert = Button('./Tree/btnInsert.png', (200, 150), (200, 200))
btnSearch = Button('./Tree/btnSearch.png', (200, 150), (200, 350))
textInsert = Text('./Tree/text.png', './Tree/mouse.png', (150, 150), (120, 250))
textSearch = Text('./Tree/text.png', './Tree/mouse.png', (150, 150), (120, 400))
root = Tree()

search = None
while True:
    screen.blit(bg_surface, (0, 0))
    btnInsert.draw()
    btnSearch.draw()
    textInsert.draw()
    textSearch.draw()
    root.inorder_print(root.root, 0, 0)
    # screen.blit(btn1, btn1_rect)
    # screen.blit(btn2, btn2_rect)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # nếu click chuột
            mouse_x, mouse_y = event.pos # lấy tọa độ chuột và vẽ hình tròn
            pygame.draw.circle(screen, (255, 220, 220), (mouse_x, mouse_y), 15)
            print('Clicked at:', mouse_x, mouse_y)
            if textInsert.click(mouse_x, mouse_y) == True:
                pass
            else:
                textInsert.mouse = 0

            if textSearch.click(mouse_x, mouse_y) == True:
                pass
            else:
                textSearch.mouse = 0

            if btnInsert.click(mouse_x, mouse_y) == True:
                value = int(textInsert.num)
                root.push(value)
                textInsert.num = "0"
                break
            if btnSearch.click(mouse_x, mouse_y) == True:
                search = int(textSearch.num)
                root.search(root.root, 0, 0, search)
                textSearch.num = "0"
                break
        elif event.type == pygame.KEYDOWN:
            textInsert.push(event.key)
            textSearch.push(event.key)

    pygame.display.update()
    fpsclock.tick(FPS)