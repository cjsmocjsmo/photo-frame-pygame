import pygame
import os

# Initialize Pygame
pygame.init()

##################USE THIS IN PRODUCTION
# Define screen size (full screen)
# screen_width = pygame.display.Info().current_w
# screen_height = pygame.display.Info().current_h

# # Set window to fullscreen and hide decorations
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
############################################################################################################


##################USE THIS FOR TESTING

# Define screen size
screen_width = 1300
screen_height = 900

# # Set window size
screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)

#########################################################################################



pygame.display.set_caption("Image Viewer")
# Hide mouse cursor
pygame.mouse.set_visible(False)

# Function to fade an image on the screen
def fade_image(image, pos, fade_in=True, fade_out=True, duration=10):
  clock = pygame.time.Clock()
  step = max(1, int(255 / duration / 60))
  if fade_in:
    # Gradually increase alpha from 0 to 255
    for alpha in range(0, 256, step):
      image.set_alpha(alpha)
      screen.blit(image, pos)
      pygame.display.flip()
      clock.tick(60)
  if fade_out:
    # Gradually decrease alpha from 255 to 0
    for alpha in reversed(range(0, 256, step)):
      image.set_alpha(alpha)
      screen.blit(image, pos)
      pygame.display.flip()
      clock.tick(60)

# Find all JPG images in the directory
pics = []
for root, dirs, files in os.walk("/home/pi/Pictures/MasterPicsResize_SPLIT/"):
  for filename in files:
    if filename.endswith(".jpg"):
      print(os.path.join(root, filename))
      pics.append(pygame.image.load(os.path.join(root, filename)))
  # if filename.endswith(".jpg"):
  #   pics.append(pygame.image.load(os.path.join("/home/pimedia/", filename)))

# Loop through images
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Loop through each image
  for image in pics:
    
    # Resize image to fit the screen (optional)
    # image = pygame.transform.scale(image, (screen_width, screen_height))
    screen_width, screen_height = screen.get_size()
    position = None
    imgw, imgh = image.get_size()
    
    if imgw < imgh:
      image = pygame.transform.scale(image, (600, 800))
      position = ((screen_width - 600) // 2, (screen_height - 800) // 2)
      
    else:
      image = pygame.transform.scale(image, (800, 600))
      position = ((screen_width - 800) // 2, (screen_height - 600) // 2)
    print(position)  

    # screen.blit(image, position)
    # Fade image in
    fade_image(image, position)
    
    # Display image for 30 seconds
    
    pygame.display.flip()
    pygame.time.wait(15 * 1000)  # Wait 30 seconds in milliseconds

    # Fade image out
    fade_image(image, position, fade_in=False)
    pygame.time.wait(12 * 1000)
    screen.fill((0, 0, 0))

# Quit Pygame
pygame.quit()
