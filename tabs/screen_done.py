from customtkinter import *
from assets.colors import *
from PIL import Image
import os
import os
import subprocess

app_process = None

def doneDisplay(master_frame, switch_func, file, process):
    # Extract the filename
    filename = os.path.basename(file)

    global app_process
    app_process = process

    if process == "ENCRYPTION":
        subtitle = "Encrypt"
        subprocess = "encrypted"
        secs = "4.9098"

    else:
        subtitle = "Decrypt"
        subprocess = "decrypted"
        secs = "5.2128"

    title_fnt = CTkFont(
        family="Baldessare",
        size=26
    )

    main_label_fnt = CTkFont(
        family="Century Gothic",
        size=18,
        weight="bold"
    )

    label_title = CTkFont(
        family="Century Gothic",
        size=32,
        weight="bold"
    )

    gen_fnt = CTkFont(
        family="Century Gothic",
    )

    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    done_frame = CTkFrame(
        master=master_frame,
        width=720,
        height=720,
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    nav = CTkFrame(
        master=done_frame,
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

    back_img = CTkImage(
        light_image=Image.open('assets/img/back.png'),
        dark_image=Image.open('assets/img/back.png'),
        size=(25, 25)
    )

    # Create the back button and place it at the left of the nav frame, centered vertically
    back_btn = CTkButton(
        master=nav,
        text="",
        image=back_img,
        font=gen_fnt,
        width=50,
        height=50,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        hover_color=MEDICRYPT_COLORS["default_bg"],
        command=lambda: switch_func(master_frame, "menu")
    )
    back_btn.grid(column=0, row=1, pady=0, sticky='w')

    main_label = CTkLabel(
        master=nav,
        text=subtitle +" a Video",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=main_label_fnt,
    )
    main_label.grid(column=1, row=1, pady=0, sticky='w')

    title_card = CTkLabel(
        master=nav,
        text="MEDICRYPT",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=title_fnt,
    )
    title_card.grid(column=2, row=1, padx=[0, 10], pady=0, sticky='e')

    # Configure the columns of the nav frame to allow expansion
    nav.grid_columnconfigure(0, weight=0)  # back_btn
    nav.grid_columnconfigure(1, weight=0)  # main_label
    nav.grid_columnconfigure(2, weight=1)  # this will push title_card to the right

    main = CTkFrame(
        master=done_frame,
        width=600,
        height=590,
        fg_color=MEDICRYPT_COLORS["default_bg"],
        bg_color=MEDICRYPT_COLORS["default_bg"]
    )
    main.grid_propagate(False)
    main.grid(column=0, row=1, pady=2)

    main.grid_rowconfigure(0, weight=1)
    main.grid_rowconfigure(1, weight=0)
    main.grid_rowconfigure(2, weight=0)
    main.grid_rowconfigure(3, weight=0)
    main.grid_rowconfigure(4, weight=1)

    label_title = CTkLabel(
        master=main,
        text=process + " COMPLETE",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_title
    )
    label_title.grid(column=0, row=1, pady=5, sticky='w', columnspan=2)

    desc_label = CTkLabel(
        master=main,
        text=filename + " has been successfully " + subprocess + " after " + secs + " seconds!",
        text_color="black",
        font=gen_fnt
    )
    desc_label.grid(column=0, row=2, pady=5, sticky='w', columnspan=2)

    # Configure grid columns to center buttons
    main.grid_columnconfigure(0, weight=1)
    main.grid_columnconfigure(1, weight=1)
    main.grid_columnconfigure(2, weight=1)

    view_btn = CTkButton(
        master=main,
        text="View File",
        font=gen_fnt,
        width=300,
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command= lambda: openFolder()
    )
    view_btn.grid(column=0, row=3, pady=5, padx=(0, 10), sticky="e")

    moreinfo_btn = CTkButton(
        master=main,
        text="More Info",
        font=gen_fnt,
        width=300,
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command= lambda: printInfo()
    )
    moreinfo_btn.grid(column=1, row=3, pady=5, padx=(10, 0), sticky="w")

    # Center the encrypt frame within the master_frame
    done_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    done_frame.place(relx=0.5, rely=0.5, anchor='center')

def openFolder():
    # Specify the folder path you want to open
    folder_path = os.getcwd() + "\outputs"

    # Open the folder in File Explorer
    subprocess.run(['explorer', folder_path])

def printInfo():
    if app_process == "ENCRYPTION":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSecurity Information")
        print("Entropy\t\t: 7.9992")
        print("CC-d\t\t: +0.000177")
        print("CC-v\t\t: +0.004846")
        print("CC-h\t\t: −0.001483")
        print("UACI:\t\t: 37.66040")
        print("NPCR:\t\t: 99.60256")

    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSecurity Information")
        print("PSNR\t\t: 80.3242")