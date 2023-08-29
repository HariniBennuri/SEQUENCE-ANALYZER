import tkinter as tk
from PIL import ImageTk, Image
import pygame
pygame.mixer.init()

def sequence(string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = []
    for i in string:
        number_str.append(alphabet.index(i))
    i = number_str
    step = i[2] - i[0]
    if(alphabet[i[4]] == alphabet[(i[2] + step) % 26]):
        return 2
    else:
        return 3


def result(string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = []
    res = ""
    for i in string:
        number_str.append(alphabet.index(i))
    if sequence(string) == 2:
        step1 = number_str[2] - number_str[0]
        step2 = number_str[3] - number_str[1]
        if step1 < 0:
            step1 = 26 + step1
        if step2 < 0:
            step2 = 26 + step2
        letter = alphabet * 12
        if len(string) % 2 == 0:
            count = 0
            while(count < 6):
                res += letter[((number_str[-2] + (count + 1) * step1) % 26)]
                res += letter[((number_str[-1] + (count + 1) * step2) % 26)]
                count += 1
            return res
    
    if sequence(string) == 3:
        letter = alphabet * 12
        step1 = number_str[3] - number_str[0]
        step2 = number_str[4] - number_str[1]
        step3 = number_str[5] - number_str[2]
        if step1 < 0:
            step1 = 26 + step1
        if step2 < 0:
            step2 = 26 + step2
        if step3 < 0:
            step3 = 26 + step3
        if len(string) % 3 == 0:
            count = 0
            while(count < 4):
                res += letter[((number_str[-3] + (count + 1) * step1) % 26)]
                res += letter[((number_str[-2] + (count + 1) * step2) % 26)]
                res += letter[((number_str[-1] + (count + 1) * step3) % 26)]
                count += 1
            return res
        
# function to create the second window
def create_second_window():
    # create the window
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
    window2 = tk.Toplevel()
    window2.geometry("700x500")
    window2.title("SEQUENCE Analyzer")
    screen_width = window2.winfo_screenwidth()
    screen_height = window2.winfo_screenheight()
    
    # create the image label and position the image
    image1 = Image.open("C:\\Users\\vyshn\\OneDrive\\Pictures\\IMAGE4.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(window2, image=test)
    label1.image = test
    x_coordinate = -150
    y_coordinate = -130
    label1.place(x=x_coordinate, y=y_coordinate)
    
    # create the input labels and entries
    input_label1 = tk.Label(window2, text="STRING 1",fg="purple")
    input_label1.grid(row=0, column=0, padx=10, pady=10)
    input_var1 = tk.StringVar()
    input_entry1 = tk.Entry(window2, textvariable=input_var1)
    input_entry1.grid(row=0, column=1, padx=10, pady=10)

    input_label2 = tk.Label(window2, text="STRING 2",fg="purple")
    input_label2.grid(row=2, column=0, padx=10, pady=10)
    input_var2 = tk.StringVar()
    input_entry2 = tk.Entry(window2, textvariable=input_var2)
    input_entry2.grid(row=2, column=1, padx=10, pady=10)

    # create the function to get the result
    def get_result():
        pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
        pygame.mixer.music.play(loops = 0)
        string1 = input_var1.get()
        string2 = input_var2.get()
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result(string1) + '\n')
        result_text.insert(tk.END, result(string2) + '\n')
        result_text.config(state=tk.DISABLED)

    # create the button to get the result
    button = tk.Button(window2, text="GET RESULT",fg="green" ,command=get_result, height=3, width=30)
    button.grid(row=3, column=0, columnspan=2, padx=20, pady=50)

    
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
    result_label = tk.Label(window2, text="RESULT",fg="purple")
    result_label.grid(row=4, column=0, padx=10, pady=10)
    result_text = tk.Text(window2, height=5, width=50, state=tk.DISABLED)
    result_text.grid(row=4, column=1, padx=20, pady=10)       
# create the exit button
    #pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
   # pygame.mixer.music.play(loops = 0)
    exit_button = tk.Button(window2, text="EXIT",fg="red", command=lambda: (window2.destroy(), window.lift(),window.destroy(),button_click1()))
    exit_button.place(x=650, y=700)

def create_third_window():
    # create the window
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
    window4 = tk.Toplevel() 
    window4.geometry("1400x700")
    window4.title("SEQUENCE Analyzer")
    screen_width = window4.winfo_screenwidth()
    screen_height = window4.winfo_screenheight()
    image1 = Image.open("C:\\Users\\vyshn\\OneDrive\\Pictures\\image2.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(window4, image=test)
    label1.image = test
    x_coordinate = -150
    y_coordinate = -150
    label1.place(x=x_coordinate, y=y_coordinate)
    exit_button = tk.Button(window4, text="EXIT",fg="red",height=1, width=10, command=lambda: (window4.destroy(), window.lift(),button_click1()))
    exit_button.place(x=1300, y=400)    
        
def create_new_window():
    # create the window
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
    window3 = tk.Toplevel() 
    window3.geometry("1000x700")
    window3.title("SEQUENCE Analyzer")
    screen_width = window3.winfo_screenwidth()
    screen_height = window3.winfo_screenheight()
    image1 = Image.open("C:\\Users\\vyshn\\OneDrive\\Pictures\\image3.jpeg")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(window3, image=test)
    label1.image = test
    x_coordinate = -60
    y_coordinate = -80
    label1.place(x=x_coordinate, y=y_coordinate)
    
    # create the button

    button = tk.Button(window3, text="NEXT",fg="green", height=2, width=20, command=create_second_window)
    button.place(x=650, y=500)

def button_click():
# create the main window
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
    create_new_window()

window = tk.Tk()
window.geometry("1000x800")
window.title("SEQUENCE Analyzer")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# create the image label and position the image
image1 = Image.open("C:\\Users\\vyshn\\OneDrive\\Pictures\\image1.jpeg")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
x_coordinate = -60
y_coordinate = -80
label1.place(x=x_coordinate, y=y_coordinate)

# create the button to start the process

button = tk.Button(window, text="PROCEED",fg= "green", height=2, width=20, command=button_click)
button.place(x=650, y=500)
button = tk.Button(window, text="ABOUT",fg="purple", height=2, width=20, command=create_third_window)
button.place(x=850, y=500)
exit_button = tk.Button(window, text="EXIT",fg="red", height=2, width=20, command=lambda:(window.destroy(),button_click1()))
exit_button.place(x=1050, y=500)
def button_click():
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
    create_third_window() 
    
def button_click1():
    pygame.mixer.music.load("el_interface_button_22_hpx.mp3")
    pygame.mixer.music.play(loops = 0)
# start the main event loop
window.mainloop()