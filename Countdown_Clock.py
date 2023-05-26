import time
import pygame
import math

pygame.init()
#Hiển thị màn hình, cài đặt fps, âm thanh, phông chữ và các biến
screen = pygame.display.set_mode((500,600))

GREY = (125, 125, 125)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
#total để lưu trữ thời gian ban đầu, total_secs là thời gian tạm thời, start để bắt đầu đếm ngược
total = 0
total_secs = 0
start = False

font = pygame.font.SysFont('sans', 30)
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('+', True, BLACK)
text_4 = font.render('-', True, BLACK)
text_5 = font.render('Start', True, BLACK)
text_6 = font.render('Reset', True, BLACK)

total_secs = 0
total = 0
start = False

running = True

sound = pygame.mixer.Sound('alarm.mp3')
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(GREY)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    #vẽ nút điều khiển, truyền vị trí chữ

    pygame.draw.rect(screen, WHITE, (50,50,50,50))
    pygame.draw.rect(screen, WHITE, (50,150,50,50))
    pygame.draw.rect(screen, WHITE, (150,50,50,50))
    pygame.draw.rect(screen, WHITE, (150,150,50,50))
    pygame.draw.rect(screen, WHITE, (250,150,100,50))
    pygame.draw.rect(screen, WHITE, (250,50,100,50))
    
    pygame.draw.rect(screen, WHITE, (100,500,300,50))
    pygame.draw.rect(screen, BLACK, (105,505,290,40))

    pygame.draw.circle(screen, BLACK, (200,350), 100)
    pygame.draw.circle(screen, WHITE, (200,350), 95)
    pygame.draw.circle(screen, RED, (200,350), 5)

    screen.blit(text_1, (60,60))
    screen.blit(text_2, (60,160))
    screen.blit(text_3, (160,60))
    screen.blit(text_4, (160,160))
    screen.blit(text_5, (260,60))
    screen.blit(text_6, (260,160))

    #Khai báo 3 biến total_secs, total, start để đánh dấu khi nào thì đếm ngược
    for event in pygame.event.get():
    	#Xét xem nhấp chuột vào trường hợp nào: nút quit, nút start,...
    	if event.type == pygame.QUIT:
    		running = False

    	if event.type == pygame.MOUSEBUTTONDOWN:
    		if event.button == 1:
	    		pygame.mixer.pause()
	    		if (50 < mouse_x < 100) and (50 < mouse_y < 100):
	    			print("press +mins")
	    			total_secs += 60
	    			total = total_secs
	    		if (150 < mouse_x < 200) and (50 < mouse_y < 100):
	    			print("press +secs")
	    			total_secs += 1
	    			total = total_secs
	    		if (50 < mouse_x < 100) and (150 < mouse_y < 200):
	    			print("press -mins")
	    			total_secs -= 60
	    			total = total_secs
	    		if (150 < mouse_x < 200) and (150 < mouse_y < 200):
	    			print("press -secs")
	    			total_secs -= 1
	    			total = total_secs 
	    		if (250 < mouse_x < 350) and (150 < mouse_y < 200):
	    			total_secs = 0
	    			total = total_secs
	    		if (250 < mouse_x < 350) and (50 < mouse_y < 100):
	    			start = True
	    			total = total_secs
	    			print("press Start")
	    		print("total_secs: " + str(total_secs))
    #Sau khi bấm start, số giây giảm 1, cần tính tọa đồ của dây kim, dây giờ và xét trường hợp dừng
    if start:
    	total_secs -= 1
    	if total_secs == 0:
    		start = False
    		pygame.mixer.Sound.play(sound)
    time.sleep(0.03)
    if total_secs < 0:
    	start = False
    	total_secs = 0

    #Hiện thị thời gian
    mins = int(total_secs / 60)
    secs = total_secs - 60 * mins
    time_now = str(mins) + ':' + str(secs)
    text_time = font.render(time_now, True, BLACK)
    screen.blit(text_time, (110,110))

    #Vẽ kim giờ, kim phút
    y_mins = 350 - 95 * math.cos(15 * mins* math.pi / 180)
    x_mins = 200 + 95 * math.sin(15 * mins * math.pi / 180)
    pygame.draw.line(screen, BLACK, (200,350), (x_mins, y_mins))

    y_secs = 350 - 90 * math.cos(6 * secs* math.pi / 180)
    x_secs = 200 + 90 * math.sin(6 * secs* math.pi / 180)
    pygame.draw.line(screen, RED, (200,350), (x_secs, y_secs))

    if total != 0:
    	pygame.draw.rect(screen, RED, (105,505, int(290 * (total_secs/ total)), 40))
    
    pygame.display.flip()

pygame.quit()



