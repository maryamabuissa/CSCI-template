
import os
import random
from pynput import keyboard

# Grid size
WIDTH, HEIGHT = 10, 10
player_x, player_y = 5, 5
target_x, target_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
score = 0
running = True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board():
    clear_screen()
    print(f"Score: {score} | Use Arrow Keys to move, ESC to exit.\n")
    for y in range(HEIGHT):
        row_str = ""
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row_str += " P "
            elif x == target_x and y == target_y:
                row_str += " * "
            else:
                row_str += " . "
        print(row_str)
    print()

def on_press(key):
    global player_x, player_y, target_x, target_y, score, running
    
    if key == keyboard.Key.esc:
        running = False
        return False  # Stop listener

    # Movement logic
    if key == keyboard.Key.up and player_y > 0:
        player_y -= 1
    elif key == keyboard.Key.down and player_y < HEIGHT - 1:
        player_y += 1
    elif key == keyboard.Key.left and player_x > 0:
        player_x -= 1
    elif key == keyboard.Key.right and player_x < WIDTH - 1:
        player_x += 1

    # Check if player caught the target
    if player_x == target_x and player_y == target_y:
        score += 1
        target_x = random.randint(0, WIDTH - 1)
        target_y = random.randint(0, HEIGHT - 1)

    draw_board()

# Initial render
draw_board()

# Start the pynput keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
