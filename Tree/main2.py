import pygame
import time

width = 1200
height = 750
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# FPS
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
        self.surface = pygame.image.load(link).convert_alpha()
        self.w, self.h = size
        self.x, self.y = index
        self.delta = 0
        self.surface = pygame.transform.scale(self.surface, size)

    def draw(self):
        surface_tempt = pygame.transform.scale(
            self.surface, (self.w - self.delta, self.h - self.delta))
        if (self.delta > 0 and self.delta < 10):
            # print(str(self.w - self.delta) + " " + str(self.h - self.delta) + "\n")
            self.delta += 3
        else:
            self.delta = 0
        screen.blit(surface_tempt, (self.x - (self.w - self.delta) /
                    2, self.y - (self.h - self.delta)/2))

    def click(self, x, y):
        if (x > self.x - self.w/2 and x < self.x + self.w/2
           and y > self.y - self.h/6 and y < self.y + self.h/6):
            self.delta = 1
            return True
        return False


class Text:
    def __init__(self, link, link2, size, index, name):
        self.surface = pygame.image.load(link).convert_alpha()
        self.w, self.h = size
        self.x, self.y = index
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h/6))
        self.name = name + ": "
        if name == "Value":
            self.num = "0"
        else:
            self.num = ""
        self.mouse = 0
        self.mouse_surface = pygame.image.load(link2).convert_alpha()
        self.mouse_surface = pygame.transform.scale(
            self.mouse_surface, (2, self.h/6))

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))
        if (self.mouse != 0):
            self.mouse += 1
            if (self.mouse % 7 == 0):
                screen.blit(self.mouse_surface, (self.x - 3 +
                            len(self.name)*14 + len(self.num)*14, self.y))
                self.mouse = 1
        if (self.num == ""):
            if self.name == "Value: ":
                self.num = "0"
            else:
                self.num = ""
        if self.name == "Value: ":
            text_surface = font.render(self.name + str(self.num), True, BLACK)
        else:
            text_surface = font.render(self.name + self.num, True, BLACK)
        screen.blit(text_surface, (self.x, self.y))

    def click(self, x, y):
        if (x > self.x and x < self.x + self.w
           and y > self.y and y < self.y + 20):
            return True
        return False

    def push(self, event):
        # if(self.num == 0):
        #     return
        if self.name == "Value: ":
            if event in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3,
                         pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                         pygame.K_8, pygame.K_9]:
                if (self.mouse != 0):
                    if self.num == "0":
                        self.num = str(event - 48)
                    else:
                        self.num += str(event - 48)
        elif event >= 97 and event <= 122:
            if (self.mouse != 0):
                self.num += chr(event - 32)

        elif event == pygame.K_BACKSPACE:
            if self.num != "" and self.num != "0":
                self.num = self.num[:len(self.num) - 1]


class ButtonNode:
    def __init__(self, link, link2, size, index, value, name):
        self.surface1 = pygame.image.load(link).convert_alpha()
        self.surface2 = pygame.image.load(link2).convert_alpha()
        self.w, self.h = size
        self.x, self.y = index
        self.check = 0
        self.value = value
        self.name = name
        self.click = False
        self.surface1 = pygame.transform.scale(self.surface1, size)
        self.surface2 = pygame.transform.scale(self.surface2, size)

    def draw(self, x, y):
        if (self.click == True):
            self.x, self.y = x, y
        if self.check == 0:
            screen.blit(self.surface1, (self.x -
                        (self.w)/2, self.y - (self.h)/2))
        else:
            screen.blit(self.surface2, (self.x -
                        (self.w)/2, self.y - (self.h)/2))
        text_surface = font.render(str(self.value), True, BLACK)
        screen.blit(text_surface, (self.x - (self.w)/2 -
                    len(str(self.value))*7 + 27, self.y - (self.h)/2 + 20))
        text_surface = font.render(self.name, True, BLACK)
        screen.blit(text_surface, (self.x - (self.w)/2 -
                    len(self.name)*10 + 25, self.y - (self.h)/2))

    def check_click(self, x, y):
        if (self.x - (self.w)/2 < x and self.x + (self.w)/2 > x
                and y > self.y - (self.h)/2 and y < self.y + (self.h)/2):
            self.x, self.y = x, y
            self.click = True
            return True
        return False


def mui_ten(A, B, value):
    pygame.draw.line(screen, BLACK, (A), (B))
    pygame.draw.circle(screen, (255, 0, 220), (B), 5)
    text_surface = font.render(str(value), True, BLACK)
    x, y = (A[0] + B[0])/2, (A[1] + B[1])/2
    screen.blit(text_surface, ((x + B[0])/2 -
                len(str(value))*7 + 27, (y + B[1])/2))


class Matrix:
    def __init__(self):
        self.matrix = []
        self.arr = []

    def draw(self, x, y, index):
        for i, j, t in self.matrix:
            mui_ten((self.arr[i].x, self.arr[i].y),
                    (self.arr[j].x, self.arr[j].y), t)

        j = 0
        for i in self.arr:
            if j == index:
                i.check = 1
            else:
                i.check = 0
            j += 1
            i.draw(x, y)

    def conect(self, A, B, value):
        if ([A, B, value] not in self.matrix):
            self.matrix.append([A, B, value])

    def push(self, value, name):
        if name not in self.arr:
            self.arr.append(ButtonNode('./btn1.png', './btn2.png',
                            (50, 50), (800, 200), value, name))

    def delete(self, A, B):
        for i in range(len(self.matrix)):
            if self.matrix[i][0] == A and self.matrix[i][1] == B:
                del self.matrix[i]

    def check_click(self, x, y):
        for i in range(1, len(self.arr) + 1):
            if (self.arr[-i].check_click(x, y)):
                break


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def matrix_to_adj_list(matrix):
    num_vertices = len(matrix)
    adj_list = {}
    for i in range(num_vertices):
        adj_list[i] = []
        for j in range(num_vertices):
            if matrix[i][j] != 0:
                adj_list[i].append(j)
    return adj_list


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def h_score_average(current, goal, graph):
    total_weight = 0
    num_neighbors = 0
    for neighbor, weight in enumerate(graph[goal]):
        if weight > 0:
            num_neighbors += 1
            total_weight += abs(graph[current]
                                [neighbor] - graph[goal][neighbor])
    return total_weight / num_neighbors if num_neighbors > 0 else 0


def Search(matrix, start, goal):
    n = len(matrix.arr)  # Độ dài cạnh của ma trận
    A = [[0 for j in range(n)] for i in range(n)]
    for i in range(len(matrix.matrix)):
        A[matrix.matrix[i][0]][matrix.matrix[i][1]] = matrix.matrix[i][2]
    print(A)

    open_set = set([start])
    closed_set = set()
    g_score = [float('inf')] * len(matrix.arr)
    g_score[start] = 0
    f_score = [float('inf')] * len(matrix.arr)
    ds_ke = matrix_to_adj_list(A)
    f_score[start] = h_score_average(start, goal, ds_ke)
    came_from = {}
    while open_set:
        # Lấy đỉnh trong danh sách mở có giá trị f-score nhỏ nhất
        current = min(open_set, key=lambda x: f_score[x])
        if current == goal:
            # Đã tìm thấy đường đi từ đỉnh xuất phát đến đỉnh đích
            return reconstruct_path(came_from, current)
        open_set.remove(current)  # Loại bỏ đỉnh hiện tại khỏi danh sách mở
        closed_set.add(current)  # Thêm đỉnh hiện tại vào danh sách đóng
        #
        for neighbor in ds_ke[current]:
            # Tính toán giá trị g-score mới cho đỉnh kề
            tentative_g_score = g_score[current] + A[current][neighbor]

            # Nếu đỉnh kề chưa được xét, thêm nó vào danh sách mở và cập nhật các thông tin về đỉnh kề
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                open_set.add(neighbor)
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + \
                    h_score_average(neighbor, goal, ds_ke)
    return None


bg_surface = pygame.image.load('./bg.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (width, height))
btnInsert = Button('./btnInsert.png', (200, 150), (200, 200))
btnSearch = Button('./btnSearch.png', (200, 150), (200, 310))
btnConnect = Button('./btnConnect.png', (200, 150), (200, 400))
btnDelete = Button('./btnDelete.png', (200, 150), (200, 550))
textInsert1 = Text('./text.png', './mouse.png', (150, 150), (120, 240), "Name")
textInsert2 = Text('./text.png', './mouse.png',
                   (150, 150), (120, 270), "Value")
textSearch = Text('./text.png', './mouse.png', (150, 150), (120, 340), "Name")
textConnect1 = Text('./text.png', './mouse.png',
                    (150, 150), (120, 420), "Name 1")
textConnect2 = Text('./text.png', './mouse.png',
                    (150, 150), (120, 450), "Name 2")
textConnect3 = Text('./text.png', './mouse.png',
                    (150, 150), (120, 480), "Value")
textDelete1 = Text('./text.png', './mouse.png',
                   (150, 150), (120, 580), "Name 1")
textDelete2 = Text('./text.png', './mouse.png',
                   (150, 150), (120, 610), "Name 2")
# root = Tree()
matrix = Matrix()
matrix.push(10, "A")
matrix.push(15, "B")
matrix.push(20, "C")
matrix.push(25, "D")
matrix.push(25, "E")
matrix.conect(0, 2, 7)
matrix.conect(0, 1, 15)
matrix.conect(0, 4, 15)
matrix.conect(1, 3, 2)
node_surface = ButtonNode('./btn1.png', './btn2.png',
                          (50, 50), (800, 200), 100, "A")
search = -1
texts = [Text('./text.png', './mouse.png', (150, 150), (120, 240), "Name"),
         Text('./text.png', './mouse.png', (150, 150), (120, 270), "Value"),
         Text('./text.png', './mouse.png', (150, 150), (120, 340), "Name"),
         Text('./text.png', './mouse.png', (150, 150), (120, 420), "Name 1"),
         Text('./text.png', './mouse.png', (150, 150), (120, 450), "Name 2"),
         Text('./text.png', './mouse.png', (150, 150), (120, 480), "Value"),
         Text('./text.png', './mouse.png', (150, 150), (120, 580), "Name 1"),
         Text('./text.png', './mouse.png', (150, 150), (120, 610), "Name 2")]
a = []
while True:
    screen.blit(bg_surface, (0, 0))
    btnInsert.draw()
    btnSearch.draw()
    btnConnect.draw()
    btnDelete.draw()
    for text in texts:
        text.draw()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if len(a) == 0 or search == -1:
        index = -1
    else:
        index = a[search]
        search += 1
        if (search >= len(a)):
            search = -1
    matrix.draw(mouse_x, mouse_y, index)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # nếu click chuột

            pygame.draw.circle(screen, (255, 220, 220), (mouse_x, mouse_y), 15)
            print('Clicked at:', mouse_x, mouse_y)

            matrix.check_click(mouse_x, mouse_y)
            for text in texts:
                text.mouse = 0

            for text in texts:
                if text.click(mouse_x, mouse_y) == True:
                    text.mouse = 1
                    break

            if btnInsert.click(mouse_x, mouse_y) == True:
                if (texts[0].num != ""):
                    matrix.push(int(texts[1].num), texts[0].num)
                    texts[1].num = "0"
                    texts[0].num = ""
                break
            if btnSearch.click(mouse_x, mouse_y) == True:
                if texts[2].num != "":
                    d = -1
                    for i in range(len(matrix.arr)):
                        if texts[2].num == matrix.arr[i].name:
                            d = i
                    if d != -1:
                        a = Search(matrix, 0, d)
                        search = 0
                texts[2].num = ""

                break
            if btnConnect.click(mouse_x, mouse_y) == True:
                if (texts[5].num != 0 and texts[3].num != "" and texts[4].num != ""):
                    d1 = -1
                    d2 = -1
                    for i in range(len(matrix.arr)):
                        if texts[3].num == matrix.arr[i].name:
                            d1 = i
                        if texts[4].num == matrix.arr[i].name:
                            d2 = i
                    if d1 != -1 and d2 != -1:
                        matrix.conect(d1, d2, int(texts[5].num))
                    texts[5].num = "0"
                    texts[3].num = ""
                    texts[4].num = ""
                break
            if btnDelete.click(mouse_x, mouse_y) == True:
                if (texts[6].num != "" and texts[7].num != ""):
                    d1 = -1
                    d2 = -1
                    for i in range(len(matrix.arr)):
                        if texts[6].num == matrix.arr[i].name:
                            d1 = i
                        if texts[7].num == matrix.arr[i].name:
                            d2 = i
                    if d1 != -1 and d2 != -1:
                        matrix.delete(d1, d2)
                texts[6].num = ""
                texts[7].num = ""
                break

        elif event.type == pygame.MOUSEBUTTONUP:
            # node_surface.click = False
            for i in matrix.arr:
                i.click = False
        elif event.type == pygame.KEYDOWN:
            for text in texts:
                if text.mouse != 0:
                    text.push(event.key)
    # node_surface.draw(mouse_x, mouse_y)
    pygame.display.update()
    fpsclock.tick(FPS)
