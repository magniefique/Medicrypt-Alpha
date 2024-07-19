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
        bg_color=MEDICRYPT_COLORS["default_bg"]
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

    btn_frame = CTkFrame(
        master=encrypt_frame,
        width=720,
        height=40,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )
    btn_frame.grid(column=0, row=3, pady=5, sticky="nw")

    algo1_btn = CTkButton(
        master=btn_frame,
        text="FY-Logistic",
        text_color=MEDICRYPT_COLORS["default_bg"],
        width=100,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
    )
    algo1_btn.grid(column=0, row=0, padx=5, sticky='w')

    algo2_btn = CTkButton(
        master=btn_frame,
        text="ILM-Cosine",
        text_color=MEDICRYPT_COLORS["default_bg"],
        width=100,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
    )
    algo2_btn.grid(column=1, row=0, padx=5, sticky='w')

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
    encrypt_btn.grid(column=0, row=4, padx=4, pady=20, sticky='w')

    # Center the encrypt frame within the master_frame
    encrypt_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    encrypt_frame.place(relx=0.5, rely=0.5, anchor='center')

def encryptDisplayNew(master_frame, switch_func):
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

    nav = CTkFrame(
        master=encrypt_frame,
        width=650,
        height=60,
        fg_color=MEDICRYPT_COLORS["default_bg"],
        bg_color=MEDICRYPT_COLORS["default_bg"]
    )
    nav.grid_propagate(False)
    nav.grid(column=0, row=0, pady=2, sticky="w")

    # Configure grid rows for nav to center the button vertically
    nav.grid_rowconfigure(0, weight=1)
    nav.grid_rowconfigure(2, weight=1)

    # Create the back button and place it at the left of the nav frame, centered vertically
    back_btn = CTkButton(
        master=nav,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="Back",
        width=40,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "menu")
    )
    back_btn.grid(column=0, row=1, pady=0, sticky='w')

    main = CTkFrame(
        master=encrypt_frame,
        width=650,
        height=380
    )
    main.grid(column=0, row=1, pady=2)

    file_inpt = CTkEntry(
        master=main,
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
    file_inpt.grid(column=0, row=0, padx=2, pady=[50, 5])

    # Create the button to upload a file
    upload_btn = CTkButton(
        master=main,
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
    upload_btn.grid(column=1, row=0, padx=2, pady=[50, 5])

    password_inpt = CTkEntry(
        master=main,
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
    password_inpt.grid(column=0, row=1, columnspan=2, padx=2, pady=5)

    # Center the encrypt frame within the master_frame
    encrypt_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    encrypt_frame.place(relx=0.5, rely=0.5, anchor='center')

def browseFile(file_inpt):
    global getFilename
    filename = filedialog.askopenfilename(filetypes=((".mp4 files", ".mp4"), ("All files", "*")))
    getFilename = filename
    file_inpt.delete(0, END)
    file_inpt.insert(0, filename)
