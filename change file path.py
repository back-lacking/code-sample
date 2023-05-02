import platform 
if platform.system() == "Windows":
    SPACE = pygame.transform.scale(pygame.image.load(os.path.join('.\Assets\space.png')), (WIDTH, HEIGHT))
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('.\Assets\spaceship_yellow.png'))
    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('.\Assets\spaceship_red.png'))
    bulletHitSound = pygame.mixer.Sound('.\Assets\Grenade+1.mp3')
    bulletFireSound = pygame.mixer.Sound('.\Assets\Gun+Silencer.mp3')
else:
    SPACE = pygame.transform.scale(pygame.image.load(os.path.join('./Assets/space.png')), (WIDTH, HEIGHT))
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('./Assets/spaceship_yellow.png'))
    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('./Assets/spaceship_red.png'))
    bulletHitSound = pygame.mixer.Sound('./Assets/Grenade+1.mp3')
    bulletFireSound = pygame.mixer.Sound('./Assets/Gun+Silencer.mp3')