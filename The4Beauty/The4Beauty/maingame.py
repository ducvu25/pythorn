import pygame
import random
from pygame import mixer
import datetime
import time

# Initialize game elements
pygame.init()  # Khởi tạo pygame tương đương ở cuối có quit game
size = (1300, 540)  # Đặt kích thước cho game
screen = pygame.display.set_mode(size)  # Đặt kích thước cho game
pygame.display.set_caption("UEH ZeroWaste Campus")  # Đặt tên cho game
done = False  # Đặt biến done = False để khi chạy game thì nó sẽ chạy vô hạn
clock = pygame.time.Clock()  # fps frame per second

# Defines general colours
SKY = (150, 240, 255)  # Màu xanh
GRASS = (126, 200, 80)
IVORY = (250, 250, 235)  # Màu ngà voi
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Sets general variables: nên đặt trước vì nếu đặt trong vòng lặp thì sẽ có một số biến
key = 0  # Đặt biến key = 0 để khi chạy game thì nó sẽ chạy cho tới khi có điều kiện dừng
start = 0  # Đặt biến start = 0 để khi chạy game thì nó sẽ chạy cho tới khi có điều kiện dừng
level = 1  # Đặt biến level = 1 để khi chạy game thì nó sẽ chạy cho tới khi có điều kiện dừng
paused = 0  # Đặt biến paused = 0 để khi chạy game thì nó sẽ chạy cho tới khi có điều kiện dừng
wasteSpawnTimer = 0  # Thời gian tạo ra rác
cloudSpawnTimer = 0  # Thời gian tạo ra mây
score = 0  # Điểm
score_threshold = 10  # Điểm cần đạt để qua màn đầu tiên
font = pygame.font.SysFont('Arial', 22)  # Đặt font chữ cho các thông báo

# Sound effect
# Thư viện mixer của pygame để chạy nhạc
succ_sound = mixer.Sound("sound/laserbeam.wav")
switch_sound = mixer.Sound("sound/switch.wav")
levelup_sound = mixer.Sound("sound/levelup.wav")
negative_sound = mixer.Sound("sound/negative.wav")
intake_sound = mixer.Sound("sound/intake.wav")
move_sound = mixer.Sound("sound/grass.wav")

# Sets graphics for  func music buttons
functionms = pygame.image.load('function.png')
functionms_rect = functionms.get_rect()
functionms_rect.center = (25, 95)
functionstatus = True

# Sets graphics for music buttons
musicbutton = pygame.image.load('music.png')
musicbutton_rect = musicbutton.get_rect()
musicbutton_rect.center = (25, 52)
musicstatus = True

# Cú pháp: pygame.transform.scale(image, (width, height))
# Sets graphics for bins: nhập lại phân chia theo độ lớn như vầy để khi nữa mà có chỉnh sửa thì đỡ gây ra sai phạm trong chỉnh sửa graphics.
organicbot = pygame.transform.scale(
    pygame.image.load('img/bins/organicbot.png'), (60, 100))
organicclose = pygame.transform.scale(
    pygame.image.load('img/bins/organicclose.png'), (60, 40))
organicopen = pygame.transform.scale(
    pygame.image.load('img/bins/organicopen.png'), (60, 50))
plasticbot = pygame.transform.scale(
    pygame.image.load('img/bins/plasticbot.png'), (60, 100))
plasticclose = pygame.transform.scale(
    pygame.image.load('img/bins/plasticclose.png'), (60, 40))
plasticopen = pygame.transform.scale(
    pygame.image.load('img/bins/plasticopen.png'), (60, 50))
glassbot = pygame.transform.scale(
    pygame.image.load('img/bins/glassbot.png'), (60, 100))
glassclose = pygame.transform.scale(
    pygame.image.load('img/bins/glassclose.png'), (60, 40))
glassopen = pygame.transform.scale(
    pygame.image.load('img/bins/glassopen.png'), (60, 50))
paperbot = pygame.transform.scale(
    pygame.image.load('img/bins/paperbot.png'), (60, 100))
paperclose = pygame.transform.scale(
    pygame.image.load('img/bins/paperclose.png'), (60, 40))
paperopen = pygame.transform.scale(
    pygame.image.load('img/bins/paperopen.png'), (60, 50))
metalbot = pygame.transform.scale(
    pygame.image.load('img/bins/metalbot.png'), (60, 100))
metalclose = pygame.transform.scale(
    pygame.image.load('img/bins/metalclose.png'), (60, 40))
metalopen = pygame.transform.scale(
    pygame.image.load('img/bins/metalopen.png'), (60, 50))
ewastebot = pygame.transform.scale(
    pygame.image.load('img/bins/ewastebot.png'), (60, 100))
ewasteclose = pygame.transform.scale(
    pygame.image.load('img/bins/ewasteclose.png'), (60, 40))
ewasteopen = pygame.transform.scale(
    pygame.image.load('img/bins/ewasteopen.png'), (60, 50))


# Sets graphics for screens: chỉnh độ lớn của cái khung làm, thì ở đây Huy cố mở rộng ra nhưng mà không thành công lắm:
lockscreen = pygame.transform.scale(pygame.image.load(
    'img/screens/Lock Screen.png'), (1300, 540))
level1 = pygame.transform.scale(pygame.image.load(
    'img/screens/Level 1.png'), (800, 540))
level2 = pygame.transform.scale(pygame.image.load(
    'img/screens/Level 2.png'), (800, 540))
level3 = pygame.transform.scale(pygame.image.load(
    'img/screens/Level 3.png'), (800, 540))
level4 = pygame.transform.scale(pygame.image.load(
    'img/screens/Level 4.png'), (800, 540))
level5 = pygame.transform.scale(pygame.image.load(
    'img/screens/Level 5.png'), (800, 540))
endscreen = pygame.transform.scale(pygame.image.load(
    'img/screens/End Screen.png'), (960, 540))
# Tạo nút play:
play_button = pygame.transform.scale(
    pygame.image.load('img/Play button.png'), (66, 70))
# Đặt nút play ở vị trí (600,390) trên khung lockscreen
lockscreen.blit(play_button, (870, 390))


# Sets graphics for HUD
# Đặt kích thước của các phím là 60px x 60px
a_key = pygame.transform.scale(pygame.image.load('img/a.png'), (60, 60))
s_key = pygame.transform.scale(pygame.image.load('img/s.png'), (60, 60))
d_key = pygame.transform.scale(pygame.image.load('img/d.png'), (60, 60))
f_key = pygame.transform.scale(pygame.image.load('img/f.png'), (60, 60))
g_key = pygame.transform.scale(pygame.image.load('img/g.png'), (60, 60))
h_key = pygame.transform.scale(pygame.image.load('img/h.png'), (60, 60))

# Độ rộng và cao của HUD là 260px và 540px
hud = pygame.transform.scale(pygame.image.load('img/hud.png'), (500.95, 540))
# Head up display: bảng hướng dẫn.

# Sets variables related to the player
binpositionx = 320
binpositiony = 410
binvelocityx = 0
bintype = "organic"
binSucc = False  # True if the player has successfully sorted a waste item
# biến binSucc là định nghĩa trạng thái hoàn thành của thùng, nếu mà thùng đủ điểm rồi thì nó sẽ là True

# -----EVERYTHING WASTE-----


class Waste:  # Gom thuộc tính lại cho các đối tượng rác
    # Khởi tạo các thuộc tính của đối tượng rác
    def __init__(self, wasteID, wasteX, wasteY, wasteSpeed, wasteWidth, wasteHeight):
        self.ID = wasteID
        self.x = wasteX
        self.y = wasteY
        self.speed = wasteSpeed
        self.width = wasteWidth
        self.height = wasteHeight

    def draw(self):  # Vẽ đối tượng rác, mấy hành động sau không bắt buộc phải có, chỉ là để tạo ra hiệu ứng cho đối tượng rác
        # wasteType là biến lưu trữ hình ảnh của đối tượng rác, tính từ 0 nên phải trừ đi 1
        wasteType = wasteGraphics[self.ID - 1]
        screen.blit(wasteType, (int(self.x), int(self.y)))


waste_list = []  # List of waste items currently in the game # danh sách các đối tượng rác hiện có trong game
remove_waste = []  # List of waste items to be removed from the game danh sách các đối tượng rác sẽ bị xóa khỏi game
waste_pool = []  # danh sách các đối tượng rác có thể xuất hiện trong game
for i in range(1, 14):
    # 9 cái organic và 4 cái nhựa #Khởi tạo các id rác trong pool cho level 1
    waste_pool.append(i)
waste_randomizer = 1  # A random number drawn from waste_pool
waste_widths = [40, 40, 32, 32, 32, 50, 40, 35, 40, 46, 48, 41, 20, 45, 45, 40, 45,
                50, 49, 45, 35, 57, 45, 45, 30, 47, 30, 41, 40, 38, 24, 56, 40, 42, 40, 42, 40]
waste_heights = [42, 38, 48, 56, 56, 40, 54, 47, 38, 43, 42, 50, 63, 38, 37, 53, 39,
                 47, 42, 52, 52, 44, 48, 47, 52, 39, 56, 50, 52, 59, 49, 44, 48, 46, 52, 53, 51]
waste_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
             19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
wasteGraphics = [pygame.transform.scale(pygame.image.load('img/waste/or (1).png'),
                                        (waste_widths[0], waste_heights[0])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (2).png'),
                                        (waste_widths[1], waste_heights[1])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (3).png'),
                                        (waste_widths[2], waste_heights[2])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (4).png'),
                                        (waste_widths[3], waste_heights[3])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (5).png'),
                                        (waste_widths[4], waste_heights[4])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (6).png'),
                                        (waste_widths[5], waste_heights[5])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (7).png'),
                                        (waste_widths[6], waste_heights[6])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (8).png'),
                                        (waste_widths[7], waste_heights[7])),
                 pygame.transform.scale(pygame.image.load('img/waste/or (9).png'),
                                        (waste_widths[8], waste_heights[8])),
                 pygame.transform.scale(pygame.image.load('img/waste/plt (1).png'),
                                        (waste_widths[9], waste_heights[9])),
                 pygame.transform.scale(pygame.image.load('img/waste/plt (2).png'),
                                        (waste_widths[10], waste_heights[10])),
                 pygame.transform.scale(pygame.image.load('img/waste/plt (3).png'),
                                        (waste_widths[11], waste_heights[11])),
                 pygame.transform.scale(pygame.image.load('img/waste/plt (4).png'),
                                        (waste_widths[12], waste_heights[12])),
                 pygame.transform.scale(pygame.image.load('img/waste/gls (1).png'),
                                        (waste_widths[13], waste_heights[13])),
                 pygame.transform.scale(pygame.image.load('img/waste/gls (2).png'),
                                        (waste_widths[14], waste_heights[14])),
                 pygame.transform.scale(pygame.image.load(
                     'img/waste/gls (3).png'), (waste_widths[15], waste_heights[15])),
                 pygame.transform.scale(pygame.image.load('img/waste/gls (4).png'),
                                        (waste_widths[16], waste_heights[16])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (1).png'),
                                        (waste_widths[17], waste_heights[17])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (2).png'),
                                        (waste_widths[18], waste_heights[18])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (3).png'),
                                        (waste_widths[19], waste_heights[19])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (4).png'),
                                        (waste_widths[20], waste_heights[20])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (5).png'),
                                        (waste_widths[21], waste_heights[21])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (6).png'),
                                        (waste_widths[22], waste_heights[22])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (7).png'),
                                        (waste_widths[23], waste_heights[23])),
                 pygame.transform.scale(pygame.image.load('img/waste/pp (8).png'),
                                        (waste_widths[24], waste_heights[24])),
                 pygame.transform.scale(pygame.image.load('img/waste/mt (1).png'),
                                        (waste_widths[25], waste_heights[25])),
                 pygame.transform.scale(pygame.image.load('img/waste/mt (2).png'),
                                        (waste_widths[26], waste_heights[26])),
                 pygame.transform.scale(pygame.image.load('img/waste/mt (3).png'),
                                        (waste_widths[27], waste_heights[27])),
                 pygame.transform.scale(pygame.image.load('img/waste/mt (4).png'),
                                        (waste_widths[28], waste_heights[28])),
                 pygame.transform.scale(pygame.image.load('img/waste/mt (5).png'),
                                        (waste_widths[29], waste_heights[29])),
                 pygame.transform.scale(pygame.image.load('img/waste/mt (6).png'),
                                        (waste_widths[30], waste_heights[30])),
                 pygame.transform.scale(pygame.image.load('img/waste/ew (1).png'),
                                        (waste_widths[31], waste_heights[31])),
                 pygame.transform.scale(pygame.image.load('img/waste/ew (2).png'),
                                        (waste_widths[32], waste_heights[32])),
                 pygame.transform.scale(pygame.image.load('img/waste/ew (3).png'),
                                        (waste_widths[33], waste_heights[33])),
                 pygame.transform.scale(pygame.image.load('img/waste/ew (4).png'),
                                        (waste_widths[34], waste_heights[34])),
                 pygame.transform.scale(pygame.image.load('img/waste/ew (5).png'),
                                        (waste_widths[35], waste_heights[35])),
                 pygame.transform.scale(pygame.image.load('img/waste/ew (6).png'),
                                        (waste_widths[36], waste_heights[36])),]

# -----EVERYTHING CLOUDS----- vẽ mây mùa gió lùa


class Cloud:    # Cái nào random thì phải tạo 1 cái class riêng
    def __init__(self, cloudID, cloudX, cloudY, cloudSpeed):
        self.ID = cloudID
        self.x = cloudX
        self.y = cloudY
        self.speed = cloudSpeed

    def draw(self):
        if not rain:
            screen.blit(cloudGraphics[self.ID], (int(self.x), int(self.y)))
        else:
            screen.blit(cloudGraphics2[self.ID], (int(self.x), int(self.y)))


cloud_list = []
cloud_widths = [70, 90, 120, 150]
cloud_heights = [70, 80, 100, 160]
remove_cloud = []

cloud_randomizer = 0  # Để random mây
cloudGraphics = [pygame.transform.scale(pygame.image.load('img/cloud.png'), (cloud_widths[0], cloud_heights[0])),
                 pygame.transform.scale(pygame.image.load(
                     'img/cloud.png'), (cloud_widths[1], cloud_heights[1])),
                 pygame.transform.scale(pygame.image.load(
                     'img/cloud.png'), (cloud_widths[2], cloud_heights[2])),
                 pygame.transform.scale(pygame.image.load('img/cloud.png'), (cloud_widths[3], cloud_heights[3]))]
cloudGraphics2 = [pygame.transform.scale(pygame.image.load('img/cloud2.png'), (cloud_widths[0], cloud_heights[0])),
                  pygame.transform.scale(pygame.image.load(
                      'img/cloud3.png'), (cloud_widths[1] + 50, cloud_heights[1] + 50)),
                  pygame.transform.scale(pygame.image.load(
                      'img/cloud2.png'), (cloud_widths[2] + 50, cloud_heights[2] + 50)),
                  pygame.transform.scale(pygame.image.load('img/cloud3.png'), (cloud_widths[3], cloud_heights[3]))]
background_rain_img = pygame.image.load('img/rain.jpg')
background_rain_img = pygame.transform.scale(background_rain_img, (1300, 540))
rain = False
# Title screen music: này không cần sửa quá
mixer.music.load('sound/title music.mp3')
pygame.mixer.music.set_volume(0.4)
mixer.music.play(-1)  # -1 để nó chạy liên tục, vòng lặp vô hạn

# -------Title Screen-------
pygame.display.set_caption("Pause and Resume Game")

# Title screen music: lockscreen # Title screen loop
while not done and start == 0:  # not done là chưa bấm nút play #start = 0 là chưa bắt đầu game
    # Tracks user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User has quit the game.")
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # phim Enter để bắt đầu game
                start = 1  # start = 1 để bắt đầu game
                paused = 1  # paused = 1 để bắt đầu game
                # Gameplay music
                mixer.music.load('sound/game music.mp3')
                pygame.mixer.music.set_volume(0.36)
                mixer.music.play(-1)
        if event.type == pygame.MOUSEBUTTONDOWN:  # nhấn nút play để bắt đầu game
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 600 < mouse_x < 600 + play_button.get_width() and 390 < mouse_y < 390 + play_button.get_height():  # nếu nhấn vào nút play
                start = 1
                paused = 1
                # Gameplay music
                mixer.music.load('sound/game music.mp3')
                pygame.mixer.music.set_volume(0.1)
                mixer.music.play(-1)

            else:  # nếu không nhấn vào nút play
                start = 0
                # nếu không nhấn enter hoặc click chuột vào nút play thì vẫn ở màn hình vẫn ở lockscreen.
                paused = 0
    # Displays graphics
    screen.fill(IVORY)  # màu nền
    screen.blit(lockscreen, (0, 0))
    pygame.display.flip()
    clock.tick(60)


class Clock:
    def __init__(self, m, s):  # đặt thời gian
        self.m = float(m)
        self.s = float(s)

    def update(self, delta):  # cập nhật thời gian
        self.s -= float(delta)
        if self.s <= 0:
            self.s = 60
            self.m -= 1
        s1 = str(int(self.m))  # chuyển đổi sang chuỗi
        if len(s1) == 1:
            s1 = "0" + s1

        s2 = str(int(self.s))
        if len(s2) == 1:
            s2 = "0" + s2
        time_ = font.render(s1 + ":" + s2, 2, BLACK)
        screen.blit(time_, (0, 0))
# -------Main Program-------


clock_ = Clock(1, 40)  # đặt thời gian ban đầu
while not done and start == 1:
    start_time = datetime.datetime.now()  # thời gian bắt đầu frame
    # Tracks user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User has quit the game.")
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            # If the user clicks on the music button, toggle the music status
            # rect là hình chữ nhật #event.pos là vị trí chuột
            if musicbutton_rect.collidepoint(event.pos):
                if musicstatus:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                # not là phủ định #musicstatus = 1 là bật nhạc #musicstatus = 0 là tắt nhạc
                musicstatus = not musicstatus

            # If the user clicks on the functionms object, toggle the sound effects status
            if functionms_rect.collidepoint(event.pos):
                if functionstatus:
                    move_sound.set_volume(1)
                    intake_sound.set_volume(1)
                    negative_sound.set_volume(2)
                    levelup_sound.set_volume(1)
                    switch_sound.set_volume(1)
                    succ_sound.set_volume(1)
                else:
                    move_sound.set_volume(0)
                    intake_sound.set_volume(0)
                    negative_sound.set_volume(0)
                    levelup_sound.set_volume(0)
                    switch_sound.set_volume(0)
                    succ_sound.set_volume(0)
                functionstatus = not functionstatus

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Bin movement controls
                key = "Left"
            if event.key == pygame.K_RIGHT:
                key = "Right"
            if event.key == pygame.K_SPACE:
                binSucc = True
                succ_sound.play()  # phát âm thanh khi nhấn phím space, tiếng hút rác
            if event.key == pygame.K_a:  # Bin swap controls
                if bintype != "organic":
                    switch_sound.play()
                bintype = "organic"
            if event.key == pygame.K_s:
                if bintype != "plastic":
                    switch_sound.play()
                bintype = "plastic"
            if event.key == pygame.K_d and level >= 2:
                if bintype != "glass":
                    switch_sound.play()
                bintype = "glass"
            if event.key == pygame.K_f and level >= 3:
                if bintype != "paper":
                    switch_sound.play()
                bintype = "paper"
            if event.key == pygame.K_g and level >= 4:
                if bintype != "metal":
                    switch_sound.play()
                bintype = "metal"
            if event.key == pygame.K_h and level >= 5:
                if bintype != "ewaste":
                    switch_sound.play()
                bintype = "ewaste"

        # thả phím thì bin dừng lại, không di chuyển hoặc hút rác vào thùng nữa.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  # Bin movement controls
                if key == "Left":
                    key = 0
            if event.key == pygame.K_RIGHT:
                if key == "Right":
                    key = 0
            if event.key == pygame.K_SPACE:
                binSucc = False
                succ_sound.stop()

    # Bin succ ----
    if binSucc:  # nếu nhấn phím space thì bin sẽ hút rác vào
        for i in range(len(waste_list)):  # len(waste_list) là độ dài của waste_list
            waste = waste_list[i]
            # dùng để kiểm tra xem rác có đang ở gần bin không
            if abs(waste.x + (waste.width / 2) - (binpositionx + 30)) <= 30:
                waste.y += 3  # nếu rác trong khoảng x bin thì rác sẽ hút vào bin nhanh hơn
                # nếu rác ở vị trí tới giữa thùng rác thì không bỏ rác dô được nữa
                if waste.y >= binpositiony and waste.y <= (binpositiony + 40):
                    remove_waste.append(waste)  # thêm rác vào remove_waste
                    intake_sound.play()  # range của stop lớn hơn id bởi vì không lấy stop number
                    if (bintype == "organic" and waste.ID in range(1, 10)) or (  # 9 loại rác
                            # 4 loại rác
                            bintype == "plastic" and waste.ID in range(10, 14)) or (
                            # 4 loại rác
                            bintype == "glass" and waste.ID in range(14, 18)) or (
                            # 8 loại rác
                            bintype == "paper" and waste.ID in range(18, 26)) or (
                            # 6 loại rác
                            bintype == "metal" and waste.ID in range(26, 32)) or (
                            bintype == "ewaste" and waste.ID in range(32, 38)):  # 6 loại rác
                        score += 1

                    else:
                        if score > 0:  # Prevents score from going negative
                            score -= 1
                        negative_sound.play()  # tiếng oh no
        for i in remove_waste:  # remove_waste là list chứa rác đã bị hút vào thùng rác
            if i in waste_list:  # kiểm tra xem rác có trong waste_list không
                waste_list.remove(i)  # Để xóa rác khỏi waste_list

    # Bin movement --- #nếu mà vừa di chuyển vừa hút dô thì nó chậm,
    if key == "Left" and binSucc == False:  # Adds velocity leftward, normal speed
        binvelocityx += -1.3
    if key == "Right" and binSucc == False:  # Adds velocity rightward, normal speed
        binvelocityx += 1.3
    if key == "Left" and binSucc == True:  # Adds velocity leftward, succ speed hút dô
        binvelocityx += -0.9
    if key == "Right" and binSucc == True:  # Adds velocity rightward, succ speed
        binvelocityx += 0.9
# chỉ có velocityx là vì chỉ di chuyển theo trục x nằm ngang
    if binSucc == True and binvelocityx > 2.4:  # Sets a cap on rightward velocity at 2.4 while succing
        binvelocityx = 2.4  # giới hạn tốc độ di chuyển của bin
    if binSucc == True and binvelocityx < -2.4:  # Sets a cap on leftward velocity at 2.4 while succing
        binvelocityx = -2.4  # giới hạn tốc độ di chuyển của bin

    if binvelocityx >= -0.9 and binvelocityx <= 0.9:  # Velocity decays if already close to 0
        binvelocityx = 0
    if binvelocityx > 0:  # Velocity decays if positive
        binvelocityx -= 0.9
    if binvelocityx < 0:  # Velocity decays if negative
        binvelocityx += 0.9

    if abs(binvelocityx * 10) in range(5, 10):  # Plays the move sound if the bin is moving
        move_sound.play()
    if binvelocityx == 0:
        move_sound.stop()

    binpositionx += binvelocityx  # làm cho bin di chuyển theo trục x
    if binpositionx < 10 and binvelocityx < 0:  # bin không di chuyển qua trái màn hình
        binpositionx = 10
    if binpositionx > 630 and binvelocityx > 0:  # bin không di chuyển qua phải màn hình
        binpositionx = 630

    # Bin swap –––
    if key == "Organic":  # Swaps bin to Organic
        bintype = "organic"
    if key == "Plastic":  # Swaps bin to Plastic
        bintype = "plastic"
    if key == "Glass":  # Swaps bin to Glass
        bintype = "glass"
    if key == "Paper":  # Swaps bin to Paper
        bintype = "paper"
    if key == "Metal":  # Swaps bin to Metal
        bin = "metal"
    if key == "Ewaste":  # Swaps bin to Ewaste
        bin = "ewaste"

    # Waste spawn
    if paused == 0:  # nếu game chưa bị pause thì mới spawn rác
        wasteSpawnTimer += 1  # tức là mỗi 1s sẽ spawn 1 rác
        if wasteSpawnTimer == 120:  # hết 120s thì tạo vòng lặp mới
            # random 1 rác trong waste_pool
            waste_randomizer = random.choice(waste_pool)
            # Ở trong phân lớp waste tạo ra 1 rác mới, có toạ độ x random từ 10 đến 650, toạ độ y = 0, tốc độ random từ +3 đến 3 + level, chiều rộng = 35, chiều cao = 35
            newWaste = Waste(waste_randomizer, random.randint(
                10, 650), 0, random.randint(level + 5, level*3 + 5) / 4, 35, 35)  # tốc độ rơi từ [5 + lv, 5 + lv*3]
            waste_list.append(newWaste)  # thêm rác mới vào waste_list
            wasteSpawnTimer = 0  # reset lại wasteSpawnTimer

    # Cloud spawn
    cloudSpawnTimer += 1
    if cloudSpawnTimer == 480:
        cloud_randomizer = random.randint(0, 3)
        newCloud = Cloud(cloud_randomizer, 700, random.randint(
            0, 300), random.randint(2, 5) / 10)
        cloud_list.append(newCloud)
        cloudSpawnTimer = 0

    # Level up system
    if level == 1 and score >= 10:
        score = 0  # Resets the score for the next threshold
        level += 1  # Increments the level
        # cài đặt thời tiết
        if (random.randint(0, 5) > 1):
            rain = True
            mixer.music.load('sound/rain.mp3')
            pygame.mixer.music.set_volume(0.4)
            mixer.music.play(-1)
        else:
            rain = False
            mixer.music.load('sound/game music.mp3')
            pygame.mixer.music.set_volume(0.1)
            mixer.music.play(-1)
        clock_ = Clock(1, 20)  # đặt thời gian
        paused = 1  # Pauses the game
        score_threshold = 15  # Sets the new score threshold
        levelup_sound.play()  # Sound effect for levelling up
        waste_pool.extend((14, 15, 16, 17))  # Adds in more items for lv2
        waste_list = []  # Deletes all current trash items
    if level == 2 and score >= 15:  # Simile
        score = 0
        level += 1
        if (random.randint(0, 5) > 2):
            rain = True
            mixer.music.load('sound/rain.mp3')
            pygame.mixer.music.set_volume(0.4)
            mixer.music.play(-1)
        else:
            rain = False
            mixer.music.load('sound/game music.mp3')
            pygame.mixer.music.set_volume(0.1)
            mixer.music.play(-1)
        clock_ = Clock(1, 10)
        paused = 1
        score_threshold = 20
        levelup_sound.play()  # Sound effect for levelling up
        waste_pool.extend((18, 19, 20, 21, 22, 23, 24, 25)
                          )  # Adds in more items for lv3
        waste_list = []  # Deletes all current trash items
    if level == 3 and score >= 20:
        score = 0
        level += 1
        if (random.randint(0, 5) > 3):
            rain = True
            mixer.music.load('sound/rain.mp3')
            pygame.mixer.music.set_volume(0.4)
            mixer.music.play(-1)
        else:
            rain = False
            mixer.music.load('sound/game music.mp3')
            pygame.mixer.music.set_volume(0.1)
            mixer.music.play(-1)
        clock_ = Clock(1, 0)
        paused = 1
        score_threshold = 25
        levelup_sound.play()  # Sound effect for levelling up
        # Adds in more items for lv4
        waste_pool.extend((26, 27, 28, 29, 30, 31))
        waste_list = []  # Deletes all current trash items
    if level == 4 and score >= 25:
        score = 0
        level += 1
        paused = 1
        if (random.randint(0, 5) > 1):
            rain = True
            mixer.music.load('sound/rain.mp3')
            pygame.mixer.music.set_volume(0.4)
            mixer.music.play(-1)
        else:
            rain = False
            mixer.music.load('sound/game music.mp3')
            pygame.mixer.music.set_volume(0.1)
            mixer.music.play(-1)
        clock_ = Clock(0, 50)
        score_threshold = 30
        levelup_sound.play()  # Sound effect for levelling up
        # Adds in more items for lv5
        waste_pool.extend((32, 33, 34, 35, 36, 37))
        waste_list = []  # Deletes all current trash items
    if level == 5 and score >= 30:
        score = 0
        level += 1
        paused = 1
        if (random.randint(0, 5) > 2):
            rain = True
            mixer.music.load('sound/rain.mp3')
            pygame.mixer.music.set_volume(0.4)
            mixer.music.play(-1)
        else:
            rain = False
            mixer.music.load('sound/game music.mp3')
            pygame.mixer.music.set_volume(0.1)
            mixer.music.play(-1)
        clock_ = Clock(0, 30)
        levelup_sound.play()  # Sound effect for levelling up
        waste_list = []

    # Pauses the game when level increments
    if paused > 0:
        paused += 1  # nếu game bị pause thì paused sẽ tăng lên 1

    # Unpause game after level increments when key is pressed. Does not work if level is at 6, which means that the infographic is displaying.
    if paused > 30 and event.type == pygame.KEYDOWN and level < 6:
        if event.key == pygame.K_RETURN:
            paused = 0  # nếu nhấn enter thì game sẽ tiếp tục chơi
    if paused > 30 and event.type == pygame.KEYDOWN and level == 6:
        if event.key == pygame.K_RETURN:
            done = True  # nếu nhấn enter thì game sẽ kết thúc

    # Draws in the background sky and grass
    screen.fill(SKY)
    # hiển thị trời mưa
    if rain:
        screen.blit(background_rain_img, (0, 0))
    pygame.draw.rect(screen, GRASS, (0, 490, 960, 50), 0)

    # Draw in and move the clouds
    for i in range(len(cloud_list)):
        cloud = cloud_list[i]
        cloud.x -= cloud.speed
        cloud.draw()
        if cloud.x < -50:
            remove_cloud.append(cloud)
    for i in remove_cloud:
        if i in cloud_list:
            cloud_list.remove(i)

    # Draw bin sprite layers that are behind the waste items
    if bintype == "organic":
        if binSucc:
            screen.blit(organicopen, (binpositionx, binpositiony - 20))
        else:
            screen.blit(organicbot, (binpositionx, binpositiony))
            screen.blit(organicclose, (binpositionx, binpositiony - 8))
    if bintype == "plastic":
        if binSucc:
            screen.blit(plasticopen, (binpositionx, binpositiony - 20))
        else:
            screen.blit(plasticbot, (binpositionx, binpositiony))
            screen.blit(plasticclose, (binpositionx, binpositiony - 8))
    if bintype == "glass":
        if binSucc:
            screen.blit(glassopen, (binpositionx, binpositiony - 20))
        else:
            screen.blit(glassbot, (binpositionx, binpositiony))
            screen.blit(glassclose, (binpositionx, binpositiony - 8))
    if bintype == "paper":
        if binSucc:
            screen.blit(paperopen, (binpositionx, binpositiony - 20))
        else:
            screen.blit(paperbot, (binpositionx, binpositiony))
            screen.blit(paperclose, (binpositionx, binpositiony - 8))
    if bintype == "metal":
        if binSucc:
            screen.blit(metalopen, (binpositionx, binpositiony - 20))
        else:
            screen.blit(metalbot, (binpositionx, binpositiony))
            screen.blit(metalclose, (binpositionx, binpositiony - 8))
    if bintype == "ewaste":
        if binSucc:
            screen.blit(ewasteopen, (binpositionx, binpositiony - 20))
        else:
            screen.blit(ewastebot, (binpositionx, binpositiony))
            screen.blit(ewasteclose, (binpositionx, binpositiony - 8))

    # Draw in and apply gravity to the waste items
    for i in range(len(waste_list)):
        waste = waste_list[i]
        waste.y += waste.speed
        waste.draw()

    # Draw bin sprite layers that are in front of the waste items
    if bintype == "organic":
        if binSucc:
            screen.blit(organicbot, (binpositionx, binpositiony))
    if bintype == "plastic":
        if binSucc:
            screen.blit(plasticbot, (binpositionx, binpositiony))
    if bintype == "glass":
        if binSucc:
            screen.blit(glassbot, (binpositionx, binpositiony))
    if bintype == "paper":
        if binSucc:
            screen.blit(paperbot, (binpositionx, binpositiony))
    if bintype == "metal":
        if binSucc:
            screen.blit(metalbot, (binpositionx, binpositiony))
    if bintype == "ewaste":
        if binSucc:
            screen.blit(ewastebot, (binpositionx, binpositiony))

    # Draw HUD
    # toạ độ của HUD tính từ trái qua là 800, từ trên xuống là 0
    screen.blit(hud, (700, 0))
    tracker = font.render(str(score) + "/" + str(score_threshold), 1, BLACK)
    lvldisplay = font.render(str(level), 1, BLACK)
    screen.blit(tracker, (904, 506))
    screen.blit(lvldisplay, (795, 506))

    # Bin icons
    if level >= 1 and level != 6:
        screen.blit(pygame.transform.scale(organicbot, (30, 50)), (732, 110))
        screen.blit(pygame.transform.scale(plasticbot, (30, 50)), (813, 110))
        screen.blit(pygame.transform.scale(a_key, (20, 20)), (749, 100))
        screen.blit(pygame.transform.scale(s_key, (20, 20)), (830, 100))
    if level >= 2 and level != 6:
        screen.blit(pygame.transform.scale(glassbot, (30, 50)), (893, 110))
        screen.blit(pygame.transform.scale(d_key, (20, 20)), (911, 100))
    if level >= 3 and level != 6:
        screen.blit(pygame.transform.scale(paperbot, (30, 50)), (973, 110))
        screen.blit(pygame.transform.scale(f_key, (20, 20)), (992, 100))
    if level >= 4 and level != 6:
        screen.blit(pygame.transform.scale(metalbot, (30, 50)), (1053, 110))
        screen.blit(pygame.transform.scale(g_key, (20, 20)), (1073, 100))
    if level >= 5 and level != 6:
        screen.blit(pygame.transform.scale(ewastebot, (30, 50)), (1133, 110))
        screen.blit(pygame.transform.scale(h_key, (20, 20)), (1154, 100))

    # Draw pop-up screens between levels
    if level == 1 and paused > 0:
        screen.blit(level1, (215, 0))
    if level == 2 and paused > 0:
        screen.blit(level2, (215, 0))
    if level == 3 and paused > 0:
        screen.blit(level3, (215, 0))
    if level == 4 and paused > 0:
        screen.blit(level4, (215, 0))
    if level == 5 and paused > 0:
        screen.blit(level5, (215, 0))
    if level == 6:
        screen.blit(endscreen, (0, 0))

    screen.blit(musicbutton, musicbutton_rect)
    screen.blit(functionms, functionms_rect)
    end_time = datetime.datetime.now()  # thời gian kết thúc frame
    delta_time = end_time - start_time  # thời gian 1 frame
    # print(delta_time.total_seconds())
    clock_.update(delta_time.total_seconds())  # cập nhật thời gian
    if (clock_.m < 0):  # kiểm tra thời gian còn lại
        start = 0
    # Updates screen
    pygame.display.flip()

    # 60 fps
    clock.tick(60)
    pygame.display.update()
