import picamera
import time
import code
import pygame, sys
from pygame.locals import *

Cam = picamera.PiCamera() #create a camera object for controlling PiCamera
c = pygame.time.Clock() #create a clock object for timing 
pygame.init()
#code.interact(local=locals()) #creates interactive python shell for user inpu
w = 1800
h = 1000
size = (w,h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Raspberry Pi Camera')
PREVIEW_TOGGLE = False

Cam.capture('image.jpg')
img=pygame.image.load('image.jpg')
screen.blit(img,(0,0))
c.tick(0.5) #ensure only three images per second max
Cam.capture('image.jpg')
print 'Image Captured'

#screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
            if event.key == K_p:   
	    	# if press 'p' on keyboard then toggle between
		# preview start and preview stop
                if PREVIEW_TOGGLE == False:
                    Cam.start_preview()
                    PREVIEW_TOGGLE = True
                elif PREVIEW_TOGGLE == True:
                    Cam.stop_preview()
                    PREVIEW_TOGGLE = False
            if event.key == K_c:    
		# if press 'c' on keybaord then capture image
		# save to file named imapge.jpg and display in pygame window 
                Cam.capture('image.jpg')
                img=pygame.image.load('image.jpg')
                screen.blit(img,(0,0))
                # pygame.display.flip() #update the display
                c.tick(0.5) #ensure only three images per second max                    
                Cam.capture('image.jpg')
		print 'Image Captured'
            if event.key == K_i:
                code.interact(local=locals()) # creates interactive python shell for 
                                              # user to control camera
    pygame.display.flip()
    c.tick(.5)

#    pygame.display.update()
#print 'doing stuff'
#testfunction = 'running function complete'
#def testcamera():
#    print testfunction

#testcamera 

#Cam.start_preview()
#sleep(10)
#Cam.stop_preview()
#DISPLAYSURF = pygame.display.set_mode((200, 150))
#pygame.display.set_caption('Raspberry Pi Camera')

#DISPLAYSURF = pygame.display.set_mode((200, 150))
#pygame.display.set_caption('Raspberry Pi Camera')

#WHITE = (255,255,255)
#BRACK = (0,0,0)
#GREEN = ( 0, 255, 0)
#RED = ( 255, 0, 0)

#DISPLAYSURF.fill(WHITE)
#pygame.draw.rect(DISPLAYSURF, GREEN, (100, 100, 200, 200))
