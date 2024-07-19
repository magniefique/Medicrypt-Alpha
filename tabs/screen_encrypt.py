from customtkinter import *
from assets.colors import *

getFilename = None


def encryptDisplay(master_frame, switch_func):
    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    # Create the encrypt frame
    encrypt_frame = CTkFrame(
        master=master_frame,
        width=720,
        height=480,
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    back_btn = CTkButton(
        master=encrypt_frame,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="Back",
        width=40,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "menu")
    )
    back_btn.grid(column=0, row=0, pady=5, sticky='nw')

    file_inpt = CTkEntry(
        master=encrypt_frame,
        text_color=MEDICRYPT_COLORS["default_btn"],
        placeholder_text="Enter a file path or choose a file",
        font=None,
        width=550,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    file_inpt.grid(column=0, row=1, padx=2, pady=[50, 5])

    # Create the button to upload a file
    upload_btn = CTkButton(
        master=encrypt_frame,
        text="File",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=None,
        width=50,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
        hover_color=MEDICRYPT_COLORS["default_bg"],
        command=lambda: browseFile(file_inpt)
    )
    upload_btn.grid(column=1, row=1, padx=2, pady=[50, 5])

    password_inpt = CTkEntry(
        master=encrypt_frame,
        text_color=MEDICRYPT_COLORS["default_btn"],
        placeholder_text="Enter a password",
        font=None,
        width=605,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    password_inpt.grid(column=0, row=2, columnspan=2, padx=2, pady=5)

    encrypt_btn = CTkButton(
        master=encrypt_frame,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="Encrypt",
        width=100,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "progress", getFilename)
    )
    encrypt_btn.grid(column=0, row=3, pady=20, sticky='w')

    # Center the encrypt frame within the master_frame
    encrypt_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    encrypt_frame.place(relx=0.5, rely=0.5, anchor='center')


def browseFile(file_inpt):
    global getFilename
    filename = filedialog.askopenfilename(filetypes=((".mp4 files", ".mp4"), ("All files", "*")))
    getFilename = filename
    file_inpt.delete(0, END)
    file_inpt.insert(0, filename)
