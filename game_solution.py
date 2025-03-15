import tkinter as tk
from tkinter import Tk, PhotoImage, Label, Button, Text
import random

canvas = None
leftKey = ""
rightKey = ""
global label1

# Function to configure the main menu
def configure_mainwindow():
    global settings_icon
    global title
    global start_button
    global settings_button
    global bg
    global label1
    global leftKey
    global rightKey
    # Destroy any previous components
    title.destroy()
    start_button.destroy()
    settings_button.destroy()
    # Add background image
    label1 = Label(window, image=bg)
    label1.place(x=0, y=0)
    # Add the title
    title = Label(window, text="Balloon Pop", width=10, height="1", font=("Snap ITC", 50, "bold"), background="#027496", foreground="#FFFFFF")
    title.place(x=170, y=160)
    # Add a button to start game
    start_button = Button(window, text="Start New Game", font=("Aptos", 20, "bold"), background="#027496", foreground="#FFFFFF", command=configure_gamewindow)
    start_button.place(x=300, y=270)
    # Add settings button to customise controls
    settings_button = Button(window, image=settings_icon, height="50", width="50", text="Settings", background="#01538D",  command=configure_leftsettingswindow)
    settings_button.place(x=0, y=0)
    # Change size, background colour and title of window
    window.geometry("800x600")
    window.configure(background='#000000')
    window.title("Balloon Pop: MAIN MENU")


# Function to allow user to customise right control
def configure_rightsettingswindow():
    global rightKey
    global title
    # Change title of window
    window.title("Balloon Pop: SETTINGS")
    title.destroy()
    start_button.destroy()
    settings_button.destroy()
    # Add instruction label
    title = Label(window, text="Enter a key to move right", background='#01538D', foreground='#FFFFFF', font=("Aptos", 25, "bold"))
    title.place(x=0, y=0)

    # Function to handle the keypress
    def key_handler(event):
        global rightKey
        # Use keycodes to get key pressed
        rightKey = event.keycode
        # Return to main menu
        configure_mainwindow()
    window.bind("<Key>", key_handler)


# Function to allow user to customise left control
def configure_leftsettingswindow():
    global leftKey
    global title
    # Change title of window 
    window.title("Balloon Pop: SETTINGS")
    title.destroy()
    start_button.destroy()
    settings_button.destroy()
    # Add instruction label 
    title = Label(window, text="Enter a key to move left", background='#01538D', foreground='#FFFFFF', font=("Aptos", 25, "bold"))
    title.place(x=0, y=0)

    # Function to handle the keypress
    def key_handler(event):
        global leftKey
        # Use keycodes to get key pressed
        leftKey = event.keycode
        # Go to page to get right key
        configure_rightsettingswindow()
    window.bind("<Key>", key_handler)

# Configure the leaderboard page
def configure_leaderboard():
    global canvas
    global leaderboard_button
    global pause_button
    global return_button
    global playagain_button
    # Reset the canavs 
    canvas.delete("all")
    leaderboard_button.destroy()
    pause_button.destroy()
    # Add clouds in background
    # Cloud 1 
    canvas.create_oval(400, -50, 500, 50, fill="white", outline="white")
    canvas.create_oval(360, -10, 430, 60, fill="white", outline="white")
    canvas.create_oval(460, -20, 540, 60, fill="white", outline="white")
    # Cloud 2
    canvas.create_oval(100, 100, 200, 200, fill="white", outline="white")
    canvas.create_oval(60, 140, 130, 210, fill="white", outline="white")
    canvas.create_oval(160, 130, 240, 210, fill="white", outline="white")
    # Cloud 3
    canvas.create_oval(600, 200, 700, 300, fill="white", outline="white")
    canvas.create_oval(560, 240, 630, 310, fill="white", outline="white")
    canvas.create_oval(660, 230, 740, 310, fill="white", outline="white")
    # Cloud 4
    canvas.create_oval(300, 350, 400, 450, fill="white", outline="white")
    canvas.create_oval(260, 390, 330, 460, fill="white", outline="white")
    canvas.create_oval(360, 380, 440, 460, fill="white", outline="white")
    # Cloud 5
    canvas.create_oval(0, 500, 100, 600, fill="white", outline="white")
    canvas.create_oval(-40, 540, 30, 610, fill="white", outline="white")
    canvas.create_oval(60, 530, 140, 610, fill="white", outline="white")
    # Cloud 6
    canvas.create_oval(400, 600, 500, 700, fill="white", outline="white")
    canvas.create_oval(360, 640, 430, 710, fill="white", outline="white")
    canvas.create_oval(460, 630, 540, 710, fill="white", outline="white")
    canvas.create_text(350, 50, text="Leaderboard", font=("Aptos", 25, "bold"), fill="black")
    # Change position of button to play the game again
    playagain_button.place(x=25, y=25)
    playagain_button.config(font=("Aptos", 12, "bold"), background="#49B2C7", foreground="white")
    # Open the leaderboard file
    f = open("leaderboard.txt")
    # Store each line in file in leaderboard array
    leaderboard = []
    # Boolean variable to skip a loop so only names are added to leaderboard page
    skipLine = False
    for x in f:
        # Add each line in file to leaderboard array
        leaderboard.append(x)
    f.close()
    y_num = 130
    # Add names and corresponding score to leaderboard
    for x in range (len(leaderboard)):
        # Make sure the line isn't empty and it's not the last line in the file and it's not a score
        if leaderboard[x] != "" and (x+1) < len(leaderboard) and not(skipLine):
            # Write to canvas the name and score
            canvas.create_text(375, y_num, text=leaderboard[x] + ": " + leaderboard[x + 1], font=("Aptos", 18), fill="#1D3F47")
            # Increase y value  
            y_num += 80
            # Skip the next loop as it will be a score
            skipLine = True
            if (x+1) < len(leaderboard):
                x += 2
        else:
            skipLine = False
            continue
    # Add return button to return to main menu
    return_button = Button(window, text="Return to Main Menu", command=configure_mainwindow, font=("Aptos", 12, "bold"), background="#49B2C7", foreground="white")
    return_button.place(x=500, y=25)


# Configure the game
def configure_gamewindow():
    global t
    global speed
    global username
    global text_box
    global enter_button
    global leaderboard_button
    global canvas
    global triangleMovement
    global ballMovement
    global keyPresses
    global invincible
    global label1
    global return_button
    global balloon
    global redBalloon
    
    # If player chooses to play again it should reset the canvas and any buttons
    try:
        canvas.destroy()
        label1.destroy()
        return_button.destroy()
    except:
        pass
    invincible = False
    # Array of key presses recorded for the cheat code
    keyPresses = []
    # Allows spikes to move down the window
    triangleMovement = True
    # Allows balloon to move left and right 
    ballMovement = True 
    # Reset score to 0
    t = 0
    # Initial speed of spikes is 4 
    speed = 4
    # Change title of window
    window.title("Balloon Pop")
    title.destroy()
    start_button.destroy()
    window.geometry("700x750")
    settings_button.destroy()
    # Add properties to canvas
    canvas = tk.Canvas(window, width=700, height=750, bg="#72CADC")
    canvas.pack(fill="both", expand=True)
    # Add background
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill="#72CADC", outline="#72CADC")
    # Cloud 1
    canvas.create_oval(400, -50, 500, 50, fill="white", outline="white")
    canvas.create_oval(360, -10, 430, 60, fill="white", outline="white")
    canvas.create_oval(460, -20, 540, 60, fill="white", outline="white")
    # Cloud 2 
    canvas.create_oval(100, 100, 200, 200, fill="white", outline="white")
    canvas.create_oval(60, 140, 130, 210, fill="white", outline="white")
    canvas.create_oval(160, 130, 240, 210, fill="white", outline="white")
    # Cloud 3
    canvas.create_oval(600, 200, 700, 300, fill="white", outline="white")
    canvas.create_oval(560, 240, 630, 310, fill="white", outline="white")
    canvas.create_oval(660, 230, 740, 310, fill="white", outline="white")
    # Cloud 4
    canvas.create_oval(300, 350, 400, 450, fill="white", outline="white")
    canvas.create_oval(260, 390, 330, 460, fill="white", outline="white")
    canvas.create_oval(360, 380, 440, 460, fill="white", outline="white")
    # Cloud 5
    canvas.create_oval(0, 500, 100, 600, fill="white", outline="white")
    canvas.create_oval(-40, 540, 30, 610, fill="white", outline="white")
    canvas.create_oval(60, 530, 140, 610, fill="white", outline="white")
    # Cloud 6
    canvas.create_oval(400, 600, 500, 700, fill="white", outline="white")
    canvas.create_oval(360, 640, 430, 710, fill="white", outline="white")
    canvas.create_oval(460, 630, 540, 710, fill="white", outline="white")
    # Text displaying the player's score
    score = canvas.create_text(325, 50, text="0", font=("Arial", 18), fill="black")
    # Initial coordinates of the balloon
    balloon_x = 300
    balloon_y = 575
    # Radius of balloon
    balloon_radius = 50
    # Create balloon
    redBalloon = PhotoImage(file="red_balloon.png")
    balloon = canvas.create_image(balloon_x, balloon_y, image=redBalloon, anchor="nw")

    # Function to activate the cheat code when up arrow key is pressed twice consecutively 
    def activate_cheatcode():
        global invincible
        global blueBalloon
        global t
        # Change colour of balloon to blue
        blueBalloon = PhotoImage(file="blue_balloon.png")
        canvas.itemconfig(balloon, image=blueBalloon)
        # Boolean variable used in the function move_triangles
        invincible = True
        # Lose 5 points from score
        t -= 5 
        # Update score on text
        canvas.itemconfig(score, text=str(t))
        # After 5 seconds deactivate the cheat code and return to normal
        window.after(5000, deactivate_cheatcode)

    # Function to deactivate the cheat code, after it is activated for 5 seconds
    def deactivate_cheatcode():
        global invincible
        global redBalloon
        # Change colour of balloon back to red
        redBalloon = PhotoImage(file="red_balloon.png")
        canvas.itemconfig(balloon, image=redBalloon)
        # Boolean variable set back to false
        invincible = False

    # Function which is called whenever player presses a key
    def key_handler(event):
        global ballMovement
        global keyPresses
        # Add the keycode of key press to array
        keyPresses.append(event.keycode)
        # If balloon is allowed to move
        if ballMovement:
            # If player presses a key corresponding to custom left key
            if event.keycode == leftKey:
                # Call function to move position of balloon
                move_left_key()
            # If player presses a key corresponding to custom right key
            elif event.keycode == rightKey:
                # Call function to move position of balloon
                move_right_key()
            # If player presses enter key which is the bosskey
            elif event.keycode == 13:
                # Pause the game before opening bosskey window
                pause_game()
                # Open bosskey window
                bossWindow = tk.Toplevel()
                bossWindow.geometry("1280x720")
                bossWindow.configure(background='#000000')
                # Add a screenshot of balckboard as bosskey
                blackBoardImg = PhotoImage(file="blackBoard.png")
                screenshot = Label(bossWindow, image=blackBoardImg)
                screenshot.place(x=0, y=0)
                bossWindow.title("BlackBoard")
                bossWindow.mainloop()
                # Allow game to be resumed after closing bosskey window
                resume_game()
            # If player enters up arrow key
            elif event.keycode == 38:
                # If player enters up arrow key twice by checking the array of key presses
                if keyPresses[len(keyPresses) - 2] == 38 and len(keyPresses) > 1:
                    # Call function to activate cheat code
                    activate_cheatcode()
            # If player didn't customise controls, use left arrow key as default left key
            elif leftKey == "" and event.keycode == 37:
                move_left_key()
            # If player didn't customise controls, use right arrow key as default right key
            elif rightKey == "" and event.keycode == 39:
                move_right_key()

    # Function to move balloon to the left 
    def move_left_key():
        balloon_pos = canvas.bbox(balloon)
        # Make sure balloon doesn't leave frame on the left
        if balloon_pos[0] > 8:
            # Move position of balloon 8 pixels to the left
            canvas.move(balloon, -8, 0)

    # Function to move balloon to the right.
    def move_right_key():
        balloon_pos = canvas.bbox(balloon)
        # Make sure balloon doesn't leave frame on the right.
        if balloon_pos[2] < 692:
            # Move position of balloon 8 pixels to the right.
            canvas.move(balloon, 8, 0)
    # Call key_handler function for every key press.
    window.bind("<Key>", key_handler)
    # Array to store falling spikes.
    triangles = []

    # Function to create a new falling spike.
    def create_triangle():
        # Random x-position for the spike
        x1 = random.randint(50, 600)  
        # Width of the spike
        x2 = x1 + 20  
        # Center point of the spike
        x3 = x1 + 10  
        # Start from the top of the screen
        y = 0  
        # Create a spike
        spike = canvas.create_polygon(x1, y, x2, y, x3, y + 30, fill="grey", outline="black")
        # Add each spike to array
        triangles.append(spike)

    # Function to move the triangles down
    def move_triangles():
        global speed
        global invincible
        global leaderboard_button
        global t
        global triangleMovement
        global playagain_button
        # If spikes are allowed to move (e.g. game is not paused)
        if triangleMovement:
            for triangle in triangles:
                # Move the triangle down by a number of pixels depending on the current difficulty of game (as score increases, speed of spike increases)
                canvas.move(triangle, 0, speed)  
                triangle_pos = canvas.coords(triangle)
                balloon_pos = canvas.bbox(balloon)
                # If the triangle goes off the screen, remove it
                if triangle_pos[3] > 750:  
                    canvas.delete(triangle)
                    triangles.remove(triangle)
                    # Increment score
                    t += 1  
                    # For every 10 points the score increases by increases the speed by 2 
                    if t%10 == 1:
                        speed += 2
                    # Update the score display
                    canvas.itemconfig(score, text=str(t))  
                # Check if the spike hits the balloon if cheat code not activated 
                if not(invincible):
                    # Check if the spike's coordinates coincides with the balloon's coordinates
                    if (triangle_pos[0] < balloon_pos[2] and  # Left side of the triangle
                        triangle_pos[2] > balloon_pos[0] and  # Right side of the triangle
                        triangle_pos[1] < balloon_pos[3] and  # Top side of the balloon
                        triangle_pos[3] > balloon_pos[1]):
                        # Tell user the game is over
                        canvas.create_text(325, 375, text="Game Over!", font=("Arial", 24), fill="red")
                        global ballMovement
                        # Don't allow the ball after user loses the game
                        ballMovement = False
                        # Add button to navigate to leaderboard
                        leaderboard_button = Button(window, text="See Leaderboard", command=configure_leaderboard, font=("Aptos", 18), background="#9FDBE1", foreground="black")
                        leaderboard_button.place(x=225, y=450)
                        # Add button to allow user to play game again
                        playagain_button = Button(window, text="Play Again", command=configure_gamewindow, font=("Aptos", 18), background="#9FDBE1", foreground="black", width=14)
                        playagain_button.place(x=225, y=510)
                        # Check if the username entered is new or user has previously played
                        if check_in_file(username):
                            # If user had played previously only change their score
                            change_score(username)
                        else:
                            # If user is new add name and score to file 
                            # Store each line in leaderboard text file in array 
                            leaderboard = []
                            # Separate leaderboard into arrays for names and scores
                            names = []
                            scores = []
                            # Open the text file to append to it
                            f = open("leaderboard.txt", "a")
                            # Add username and score to text file
                            f.write(username)
                            f.write(str(t))
                            f.write("\n")
                            # Close the text file
                            f.close()
                            f = open("leaderboard.txt")
                            # Add each non-empty line in text file to the leaderboard array
                            for x in f:
                                if x != "":
                                    leaderboard.append(x)
                            f.close()
                            # Add alternate lines to names and scores, so all even indices are added to names, and all odd are added to scores
                            for x in range(len(leaderboard)):
                                # Check if index is even 
                                if x % 2 == 0:
                                    names.append(leaderboard[x])
                                else:
                                    scores.append(leaderboard[x])
                            n = len(scores)
                            # Sort the list of names and scores according to score in descending order, using bubble sort
                            # Iterate for each item in scores
                            for i in range(n):
                                # Only iterate for each item except for the last elements that are already in correct position
                                for j in range(0, n-i-1):
                                    if int(scores[j]) < int(scores[j+1]):
                                        # Swap if the element found is smaller than the next element
                                        scores[j], scores[j+1] = scores[j+1], scores[j]
                                        names[j], names[j+1] = names[j+1], names[j]
                            # Add the sorted names and scores back into leaderboard
                            for i in range(n):
                                leaderboard[2*i] = names[i]
                                leaderboard[(2*i) + 1] = scores[i]
                            # Open text file to overwrite previous content
                            f = open("leaderboard.txt", "w")
                            # Write each item in leaderboard back to the leaderboard text file, in correct order
                            for x in range(len(leaderboard)):
                                f.write(leaderboard[x])
                            # Close the file
                            f.close()
                            # As user is new, this score will be a high score for them
                            canvas.create_text(325, 410, text="*NEW HIGH SCORE: " + str(t) + "*", font=("Arial", 18), fill="black")
                        return
            # Create new spikes periodically
            # Random chance to spawn a new triangle
            if random.randint(1, 20) == 1:
                create_triangle()
            # Repeat this function every 50ms, so it is called recursively
            window.after(50, move_triangles)  
    
    # Function to get the text entered by user for their username
    def get_text():
        global text_box
        global username
        global enter_button
        global name
        global bgName
        # Get the text from the text box
        entered_text = text_box.get("1.0", tk.END)
        # Change username to user's username
        username = entered_text
        text_box.destroy()
        enter_button.destroy()
        canvas.delete(name)
        canvas.delete(bgName)
        # Start the game by spikes falling down
        move_triangles()

    # Function for score of user to change if they have played previously
    def change_score(user_name):
        global score
        global t
        # Open the text file
        f = open("leaderboard.txt")
        # Store each line in leaderboard text file in array 
        leaderboard = []
        # Add each non-empty line in text file to the leaderboard array
        for x in f:
            if x != "":
                leaderboard.append(x)
        f.close()
        # Separate leaderboard into arrays for names and scores
        names = []
        scores = []
        # Find the username in leaderboard array
        for x in range(len(leaderboard)):
            # If the username is found 
            if leaderboard[x] == user_name:
                # Ensure user's previous score is less than new score
                if int(leaderboard[x+1]) < t:
                    # Change the scor to new high score
                    leaderboard[x+1] = str(t) + "\n"
                    # Display text for new high score
                    canvas.create_text(325, 410, text="*NEW HIGH SCORE: " + str(t) + "*", font=("Arial", 18), fill="black")
        # Add alternate lines to names and scores, so all even indices are added to names, and all odd are added to scores
        for x in range(len(leaderboard)):
            # Check if index is even 
            if x % 2 == 0:
                names.append(leaderboard[x])
            else:
                scores.append(leaderboard[x])
        n = len(scores)
        # Sort the list of names and scores according to score in descending order, using bubble sort
        # Iterate for each item in scores
        for i in range(n):
            # Only iterate for each item except for the last elements that are already in correct position
            for j in range(0, n-i-1):
                if int(scores[j]) < int(scores[j+1]):
                    # Swap if the element found is smaller than the next element
                    scores[j], scores[j+1] = scores[j+1], scores[j]
                    names[j], names[j+1] = names[j+1], names[j]
        # Add the sorted names and scores back into leaderboard
        for i in range(n):
            leaderboard[2*i] = names[i]
            leaderboard[(2*i) + 1] = scores[i]
        # Open text file to overwrite previous content
        f = open("leaderboard.txt", "w")
        # Write each item in leaderboard back to the leaderboard text file, in correct order
        for x in range(len(leaderboard)):
            f.write(leaderboard[x])
        # Close the file
        f.close()

    # Check if user is already on leaderboard
    def check_in_file(user_name):
        # Open the text file
        f = open("leaderboard.txt")
        match = False
        # Check every line in text file
        for x in f:
            # If the username is in the text file then user has previously played
            if x == user_name:
                # Change Boolean variable to be true
                match = True
        # Close the text file 
        f.close()
        return match
    
    # Resume the game
    def resume_game():
        global triangleMovement
        # Allow for spikes to fall
        triangleMovement = True
        move_triangles()
        # Allow balloon to be moved
        global ballMovement
        ballMovement = True
        # Change resume button to pause button
        pause_button.config(text="l>", command=pause_game, font=("Aptos", 18, "bold"), background="#49B2C7", foreground="white")

    # Pause the game
    def pause_game():
        # Stop movement of spikes
        global triangleMovement
        triangleMovement = False
        move_triangles()
        # Stop movement of balloon
        global ballMovement
        ballMovement = False
        # Change pause button to resume button
        pause_button.config(text="ll", command=resume_game, font=("Aptos", 18, "bold"), background="#49B2C7", foreground="white")

    # Function to dispay text box and allow user to enter username 
    def enter_name():
        global username
        global text_box
        global enter_button
        global name
        global bgName
        bgName = canvas.create_rectangle(175, 340, 475, 450, fill="#49B2C7", outline="#308A9C")
        # Display information
        name = canvas.create_text(325, 375, text="Enter your name:", font=("Arial", 18), fill="black")
        # Display the text box
        text_box = Text(window, height=1, width=25)
        text_box.place(x=200, y=400)
        # Display enter button, which calls get_text function
        enter_button = Button(window, text="Enter", command=get_text, background="#72CADC", foreground="black")
        enter_button.place(x=420, y=395)
    global pause_button
    # Add pause button to window
    pause_button = Button(window, text="l>", command=pause_game, font=("Aptos", 18, "bold"), background="#49B2C7", foreground="white")
    pause_button.place(x=25, y=25)
    # Call function to allow user to enter their name
    enter_name()
# Create window
window = Tk()  
global title
global bg
bg = PhotoImage(file="sky.png") # Image Credits (Pixaby) : https://pixabay.com/photos/sky-clouds-forms-air-atmosphere-5534319/
# Show image using label
label1 = Label(window, image=bg)
label1.place(x=0, y=0)
# Display the title
title = Label(window, text="Balloon Pop", width=10, height="1", font=("Snap ITC", 50, "bold"), background="#027496", foreground="#FFFFFF")
title.place(x=170, y=160)
# Display a start button to load a new game
start_button = Button(window, text="Start New Game", font=("Aptos", 20, "bold"), background="#027496", foreground="#FFFFFF", command=configure_gamewindow)
start_button.place(x=300, y=270)
# Add seetings button to allow user to customise controls
settings_icon = PhotoImage(file="settings_icon.png") 
settings_button = Button(window, image=settings_icon, height="50", width="50", text="Settings", background="#01538D",  command=configure_leftsettingswindow)
settings_button.place(x=0, y=0)
# Call function to configure the main window 
configure_mainwindow()
window.mainloop()