import random
import tkinter as tk
from tkinter import messagebox
import pygame
from pygame import mixer
import config

# Constants
config.life_dealer = 3
config.life_player = 3

# Function to play one round of the game
def play_round():
    # Initialize revolver for each round
    revolver = [0, 0, 0, 0, 0, 0]
    # Load sounds
    gunshot_sound = mixer.Sound("gunshot.wav")
    click_sound = mixer.Sound("click.wav")

    random_numbers = random.sample([1, 2, 3, 4, 5, 6], 3)
    for num in random_numbers:
        revolver[num - 1] = 1

    bullets = 3
    dud = 3
    choice = "dealer"  # Starting with the dealer's turn
    for i in range(6):
        if choice == "dealer":
            num = random.randint(0, 1)
            if num == 0 and revolver[i] == 1:  # Dealer shoots themselves
                config.life_dealer -= 1
                bullets -= 1
                gunshot_sound.play()
                text_widget.insert(tk.END, "Dealer shoots himself! Bang!! \nYou win!!\n")
                text_widget.see(tk.END)
                choice = "dealer"
            elif num == 0 and revolver[i] == 0:  # Dealer gets a dud
                dud -= 1
                bullets -= 1
                click_sound.play()
                text_widget.insert(tk.END, "Dealer shoots himself! It's a dud!!\n")
                text_widget.see(tk.END)
                choice = "dealer"
            elif num == 1 and revolver[i] == 1:  # Dealer shoots player
                config.life_player -= 1
                bullets -= 1
                gunshot_sound.play()
                text_widget.insert(tk.END, "Dealer shoots YOU! Bang!!\nYou LOSE!!\n")
                text_widget.see(tk.END)
                choice = "player"
            elif num == 1 and revolver[i] == 0:  # Dealer gets a dud
                dud -= 1
                click_sound.play()
                text_widget.insert(tk.END, "Dealer shoots YOU! It's a dud!!\n")
                text_widget.see(tk.END)
                choice = "player"
        else:
            try:
                chk = int(input_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter 0 or 1.")
                return
            if chk not in [0, 1]:
                messagebox.showerror("Error", "Invalid input. Please enter 0 or 1.")
                return
            if chk == 0 and revolver[i] == 1:  # Player shoots themselves
                config.life_player -= 1
                bullets -= 1
                gunshot_sound.play()
                text_widget.insert(tk.END, "YOU shoot yourself! Bang!! You are dead\nYou LOSE!!\n")
                text_widget.see(tk.END)
                choice = "player"
            elif chk == 0 and revolver[i] == 0:  # Player gets a dud
                dud -= 1
                click_sound.play()
                text_widget.insert(tk.END, "YOU shoot yourself! It's a dud!!\n")
                text_widget.see(tk.END)
                choice = "player"
            elif chk == 1 and revolver[i] == 1:  # Player shoots dealer
                config.life_dealer -= 1
                bullets -= 1
                gunshot_sound.play()
                text_widget.insert(tk.END, "You shoot the DEALER! Bang!! Dealer dies\nYou win!!\n")
                text_widget.see(tk.END)
                choice = "dealer"
            elif chk == 1 and revolver[i] == 0:  # Player gets a dud
                dud -= 1
                click_sound.play()
                text_widget.insert(tk.END, "You shoot the DEALER! It's a dud!!\n")
                text_widget.see(tk.END)
                choice = "dealer"
        
        if config.life_dealer == 0:
            text_widget.insert(tk.END, "You win!!!\n")
            text_widget.see(tk.END)  # Scroll to the end
            break
        elif config.life_player == 0:
            text_widget.insert(tk.END, "Dealer wins!!!\n")
            text_widget.see(tk.END)  # Scroll to the end
            break

# Initializing Pygame
pygame.init()
mixer.init()

# Creating Tkinter GUI
root = tk.Tk()
root.title("Russian Roulette Game")

# Background Image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# GUI Components
label = tk.Label(root, text="Russian Roulette Game", font=("Helvetica", 20))
label.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_round)
play_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=5)

input_label = tk.Label(root, text="Whom do you want to shoot?\nPress 1 for Dealer\nPress 0 to test your luck")
input_label.pack(pady=5)

input_entry = tk.Entry(root)
input_entry.pack(pady=5)

text_widget = tk.Text(root, height=10, width=50)
text_widget.pack(pady=5)

# Main loop
root.mainloop()
