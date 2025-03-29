import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player 🎵")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 28)

songs = [
    r"C:\Users\Acer Nitro 5\Music\mus\Eminem - Mockingbird [Official Music Video].mp3",
    r"C:\Users\Acer Nitro 5\Music\mus\Eminem - The Real Slim Shady (Official Video - Clean Version).mp3",
    r"C:\Users\Acer Nitro 5\Music\mus\Miyagi & Эндшпиль feat. Рем Дигга - Untouchable (Official Audio).mp3"
]
index = 0

def play_song():
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    update_display()

def update_display():
    screen.fill(WHITE)
    
    controls_text = [
        "Controls:",
        "P - Play/Unpause",
        "S - Pause",
        "N - Next Song",
        "B - Previous Song",
        "ESC - Exit"
    ]

    now_playing = f"Now Playing: {songs[index].split('\\')[-1]}"

    now_playing_text = font.render(now_playing, True, BLACK)
    screen.blit(now_playing_text, (20, 20))

    for i, line in enumerate(controls_text):
        text = font.render(line, True, BLACK)
        screen.blit(text, (20, 60 + i * 30))

    pygame.display.flip() 

play_song()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Unpause
                pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Pause
                pygame.mixer.music.pause()
            elif event.key == pygame.K_n:  # Next
                index = (index + 1) % len(songs)
                play_song()
            elif event.key == pygame.K_b:  # Previous
                index = (index - 1) % len(songs)
                play_song()
            elif event.key == pygame.K_ESCAPE:  # Quit
                running = False
        
        update_display()

pygame.quit()
