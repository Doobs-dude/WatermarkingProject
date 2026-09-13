import tkinter as tk
import re
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.geometry("1600x900") #standard geometry of a PC
root.title("TK UI")

uploaded_img = None
name_entry = None
email_entry = None 
title_entry = None
copyright_entry = None

def load_image(path): #path used as a parameter
    image = Image.open(path)
    return ImageTk.PhotoImage(image)


def show_screen(screen): # the output of the load image used as a parameter
    label = tk.Label(root, image=screen)
    label.image = screen #prevents the screen from being erased
    label.place(x=0, y=0, relheight=1, relwidth=1)


def open_watermark_upload():
    print("opening verifier upload...")
    watermark_upload = load_image("GUI_test/Verifier_upload.png")
    watermark_upload_label = tk.Label(root, image = watermark_upload)
    watermark_upload_label.image = watermark_upload #prevents the screen from being erased
    watermark_upload_label.place(x=0, y=0, relheight=1, relwidth=1)
    watermark_upload_label.bind("<Button-1>", lambda event: upload_image())


def open_infopage():
    print("Loading info page...") # a statement showing the infopage function was called
    infopage_screen = load_image("GUI_test/information_page.png") # the infopage screen is displayed instead of the main 
    show_screen(infopage_screen)


def submit_watermarkupload(overall_validity):
    percentage_screen = load_image("GUI/Watermark_percentage.png")
    show_screen(percentage_screen)

    if overall_validity > 70: #percentage gotten from prototype 2 used to cateogorise
        status = "Watermark Found"
    elif 20 < overall_validity <= 70:
        status= "Watermark Distorted"
    else:
        status = "No Watermark Found"
    
    message = f"{overall_validity} - {status}" #example 75 - watermark found
    #percentage displayed as a label in the center
    #screen design lets label be positioned this way
    label = tk.Label(root, text=message, font=("Helvetica", 24, "bold italic"), fg="black", bg=None)
    label.place(relx=0.5, rely=0.5, anchor='center')
     

def exit_button(x_axis, y_axis):
    pass
    exit_button = load_image()
    exit_buttonlabel = tk.Label(root, image = exit_button)
    exit_buttonlabel.place(x = x_axis, y = y_axis, width = 120, height = 120)
    exit_buttonlabel.bind("<button-1>", lambda event: load_mainscreen())
    
def open_form():
    print("Loading...") # a statement showing the form function was called
    form_screen = load_image("GUI_test/form_background.png") # the form screen is displayed instead of the main 
    show_screen(form_screen)
    the_inputs() #calls the form function for inputs

def the_inputs():

    global name_entry, email_entry, title_entry, copyright_entry #the entries are made global to allow change
    
    name_entry = tk.Entry(root, font = ("arial", 10)) #standard name entry
    name_entry.place(x=545, y=80, width=500) #entry place correctly placed

    email_entry = tk.Entry(root, font = ("arial", 10)) #standard email entry
    email_entry.place(x=545, y=217, width=500) # entry place correctly placed
    
    title_entry = tk.Entry(root, font = ("arial", 10))#standard title entry
    title_entry.place(x=545, y=350, width=500)

    copyright_entry = tk.Entry(root, font = ("arial", 10))#standard copyright entry
    copyright_entry.place(x=545, y=505, width=500)

    upload_button = tk.Button(root, command= upload_image)#the button is made to call upload function
    upload_button.place(x=545, y=653, width = 400, height = 50)


    submit_image = load_image("GUI_test/form_submit.png") #submit button is made a different label to enable interactivity
    submit_label = tk.Label(root, image = submit_image)
    submit_label.image = submit_image #prevention of garbage collection
    submit_label.place(x=530, y=800)
    submit_label.bind("<Button-1>", lambda event: submit_form()) # submit form is called to validate inputs

def upload_image():
    global uploaded_img #make the image global to use the image for the algorithm 
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])  #use file diolog for the user input
    if file_path:
        uploaded_img = load_image(file_path)  #make it tkinter applicable 



def submit_form():

    if not name_entry.get().strip(): #name entry validation
        messagebox.showerror("no name","please enter your name")
        return
    elif not email_entry.get().strip(): #email entry validation
        messagebox.showerror("no email","please enter an email address")
        return
    elif not uploaded_img: #image upload validation
        messagebox.showerror("no image", "please input an image file")
        return
    
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #email pattern validation
    if not re.match(email_pattern, email_entry.get().strip()):
        messagebox.showerror("email not valid","please enter a valid email address")
        return
    
    #print statements to signify inputs
    print("user's name: " + name_entry.get().strip()) 
    print("user's email: " + email_entry.get().strip())
    if title_entry:
        print("title: " + title_entry.get().strip())
    elif copyright_entry:
        print("copyright: " + copyright_entry.get().strip())
    print(uploaded_img)
    return messagebox.showinfo("loading", "your image is being watermarked") # if everything is a success

    

    
    
        


def load_mainscreen():
    main_screen = load_image("GUI_test/main_background.png")
    watergen_button = load_image("GUI_test/watergen_button.png")
    waterver_button = load_image("GUI_test/waterver_button.png")
    info_button = load_image("GUI_test/info_button.png")

    show_screen(main_screen)

    watergen_buttonlabel = tk.Label(root, image = watergen_button)
    watergen_buttonlabel.image = watergen_button #prevents the screen from being erased
    watergen_buttonlabel.place(x=175, y=270, width=590, height = 320)
    watergen_buttonlabel.bind("<Button-1>", lambda event: open_form())

    waterver_buttonlabel = tk.Label(root, image = waterver_button)
    waterver_buttonlabel.image = waterver_button #prevents the screen from being erased
    waterver_buttonlabel.place(x=835, y=270, width=590, height= 320)
    waterver_buttonlabel.bind("<Button-1>", lambda event : open_watermark_upload())

    info_buttonlabel = tk.Label(root, image = info_button)
    info_buttonlabel.image = info_button #prevents the screen from being erased
    info_buttonlabel.place(x=1500, y=10, width=108, height=108)
    info_buttonlabel.bind("<Button-1>", lambda event : open_infopage())

load_mainscreen()



root.mainloop() 

print("overall validity: 12.1%")

