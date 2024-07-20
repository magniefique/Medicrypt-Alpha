from customtkinter import *
from assets.colors import *
import fisher_yates_encrypt
import fisher_yates_encrypt
import threading
import cv2
from PIL import Image, ImageTk
import time
import shutil

def progressDisplay(master_frame, switch_func, file, progress):
    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    # Create the progress frame
    progress_frame = CTkFrame(
        master=master_frame,
        width=720,
        height=480,
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    menu_font = CTkFont(
        family="Times",
        size=48,
        weight="bold"
    )

    progress_label = CTkLabel(
        master=progress_frame,
        text="ENCRYPTING",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=menu_font,
        width=100,
        height=100,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    encrypt_btn = CTkButton(
        master=progress_frame,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="Return to Main Menu",
        width=100,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "menu")
    )

    progress_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    progress_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    progress_frame.place(relx=0.5, rely=0.5, anchor='center')

    # runEncryption(file)

def progressDisplayDecrypt(master_frame, switch_func, file, progress):
    runProgressThread2(master_frame, switch_func, file, progress)

def progressRun1(master_frame, switch_func, file, progress):
    runProgressThread1(master_frame, switch_func, file, progress)

def progressRun2(master_frame, switch_func, file, progress):
    runProgressThread2(master_frame, switch_func, file, progress)

# Run thread for Encryption     
def runProgressThread1(root_frame, func, file, progress):
    t1 = threading.Thread(target=runEncryption, args=(file, ))
    t1.start()
    progressDisplayEncrypt(root_frame, func, file, progress)
    checkComplete(t1, root_frame, func, file, progress)

# Run thread for Encryption     
def runProgressThread2(root_frame, func, file, progress):
    t1 = threading.Thread(target=runDecryption, args=(file, ))
    t1.start()
    progressDisplayEncrypt(root_frame, func, file, progress)
    checkComplete(t1, root_frame, func, file, progress)

def runDecryption(file):
    time.sleep(5)
    # you have to open the source  file in binary mode with 'rb'
    shutil.copy("test2.avi", "outputs/test_decrypt.avi")

# Run Encryption
def runEncryption(file):
    e = fisher_yates_encrypt.Encrypt()
    e.readVideo(file)

def checkComplete(thread, root_frame, func, file, progress):
    if thread.is_alive():
        root_frame.after(100, checkComplete, thread, root_frame, func, file, progress)
        
    else:
        if progress == "ENCRYPTING":
            func(root_frame, "complete1", file)

        else:
            func(root_frame, "complete2", file)

def progressDisplayEncrypt(master_frame, switch_func, file, progress):
    cap = cv2.VideoCapture(file)
    ret, frame = cap.read()
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    title_fnt = CTkFont(
        family="Baldessare",
        size=26
    )

    label_fnt = CTkFont(
        family="Century Gothic",
        size=30,
        weight="bold"
    )

    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    # Create the progress frame
    progress_frame = CTkFrame(
        master=master_frame,
        width=720,
        height=720,
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    nav = CTkFrame(
        master=progress_frame,
        width=620,
        height=60,
        fg_color=MEDICRYPT_COLORS["default_bg"],
        bg_color=MEDICRYPT_COLORS["default_bg"]
    )
    nav.grid_propagate(False)
    nav.grid(column=0, row=0, pady=2, sticky="ew")

    # Configure grid rows for nav to center the button vertically
    nav.grid_rowconfigure(0, weight=1)
    nav.grid_rowconfigure(2, weight=1)

    title_card = CTkLabel(
        master=nav,
        text="MEDICRYPT",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=title_fnt,
    )
    title_card.grid(column=0, row=1, padx=[0, 10], pady=0, sticky='e')

    # Configure the columns of the nav frame to allow expansion
    nav.grid_columnconfigure(0, weight=1)  # back_btn

    main = CTkFrame(
        master=progress_frame,
        width=600,
        height=590,
        fg_color=MEDICRYPT_COLORS["default_bg"],
        bg_color=MEDICRYPT_COLORS["default_bg"]
    )
    main.grid_propagate(False)
    main.grid(column=0, row=1, pady=2)

    main.grid_columnconfigure(0, weight=1)
    main.grid_rowconfigure(0, weight=1)  # Top spacer
    main.grid_rowconfigure(1, weight=0)  # Label
    main.grid_rowconfigure(2, weight=0)  # Image frame
    main.grid_rowconfigure(3, weight=1)  # Bottom spacer

    progress_label = CTkLabel(
        master=main,
        text=progress,
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    progress_label.grid(column=0, row=1, pady=5)

    progress_img = CTkImage(
        light_image=Image.fromarray(rgb_image),
        dark_image=Image.fromarray(rgb_image),
        size=(300, 300),
    )

    progress_img_frame = CTkLabel(
        master=main,
        width=250,
        height=250,
        text="",
        image=progress_img,
    )
    progress_img_frame.grid(column=0, row=2, pady=5)

    progress_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    progress_frame.place(relx=0.5, rely=0.5, anchor='center')    

    animate_dots(progress_label, progress)

# Animation function
def animate_dots(label, base_text="ENCRYPTING"):
    def update_text():
        current_text = label.cget("text")
        if current_text.endswith("..."):
            new_text = base_text
        else:
            new_text = current_text + "."
        label.configure(text=new_text)
        label.after(500, update_text)  # Schedule the function to run after 500 ms

    update_text()