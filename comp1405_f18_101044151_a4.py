
# coding: utf-8

# In[ ]:


#Rishiheishan Parameswaran
#101044151


# In[1]:


import pygame
pygame.init()


# In[2]:


#Acceptable strings for ouput "yes" will be stored in a variable
yes = "y", "yes"
#The image file names will be initialized
ghostFilename = ""
backgroundFilename = ""


# In[3]:


print("Welcome to the Chroma-Keying Program!")
#The input for instructions will be created
#If the user wants instructions, they will be prompted for the file names
#Else, no instructions will be given, and program will stop if user does not provide file names
instructions = str(input("Do you require instructions? "))
if instructions.lower() in yes:
    print("Please input correctly when prompted. Make sure to include \".bmp\" when typing the file names. ")
    ghostFilename = input("Enter the file name of the ghost image: ")
    backgroundFilename = input("Enter the file name of the background image: ")
else:
    ghostFilename = str(input(""))
    backgroundFilename = str(input(""))
    if(ghostFilename=="")or(backgroundFilename==""):
        print("Please input correctly when prompted.")
        pygame.quit()


# In[4]:


#The images will be loaded and then displayed through setup of the screen size
ghostImage = pygame.image.load(ghostFilename)
backgroundImage = pygame.image.load(backgroundFilename)
(w,h) = backgroundImage.get_rect().size
screen = pygame.display.set_mode((w,h))
screen.blit(backgroundImage,(0,0))
pygame.display.update()


# In[5]:


#The x and y coordinates that represent where the ghost will be centered at will be prompted
#The coordinates must be valid and checked
ghostX = int(input("Enter the x-coordinate at which the ghost must be centered at: "))
ghostY = int(input("Enter the y-coordinate at which the ghost must be centered at: "))
while(ghostX<0)or(ghostX>w):
    ghostX = int(input("Enter the correct x-coordinate at which the ghost must be centered at: "))
while(ghostY<0)or(ghostY>h):
    ghostY = int(input("Enter the correct y-coordinate at which the ghost must be centered at: "))
(w,h) = ghostImage.get_rect().size


# In[ ]:


#A loop will be created to run through all the pixels in the picture
#If the pixel is not green, the average of the pixel will be calculated, setted and displayed to the screen
pixelX = 0
pixelY = 0
while(pixelX!=w)and(pixelY!=h):
    (gr,gg,gb,_) = ghostImage.get_at((pixelX,pixelY))
    (br,bg,bb,_) = backgroundImage.get_at((ghostX+pixelX,ghostY+pixelY))
    if(gg!=255):
        averageRed = (gr+br)//2
        averageGreen = (gg+bg)//2
        averageBlue = (gb+bb)//2
        screen.set_at((pixelX+ghostX,pixelY+ghostY),(averageRed,averageGreen,averageBlue))
    pixelX = pixelX+1
    if(pixelX==w)and(pixelY!=h):
        pixelX = 0
        pixelY = pixelY+1
pygame.display.update()


# In[ ]:


#The pygame window will be forced to stay open until the user tries to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        pygame.display.update()

