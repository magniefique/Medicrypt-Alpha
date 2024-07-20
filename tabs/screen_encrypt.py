from customtkinter import *
from assets.colors import *
from PIL import Image

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

    encrypt_fnt = CTkFont(
        family="Century Gothic",
        size=18,
        weight="bold"
    )

    title_fnt = CTkFont(
        family="Baldessare",
        size=26
    )

    main_label_fnt = CTkFont(
        family="Century Gothic",
        size=18,
        weight="bold"
    )

    gen_fnt = CTkFont(
        family="Century Gothic",
    )

    label_fnt = CTkFont(
        family="Century Gothic",
        weight="bold"
    )

    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    # Create the encrypt frame
    encrypt_frame = CTkFrame(
        master=master_frame,
        width=720,
        height=720,
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    nav = CTkFrame(
        master=encrypt_frame,
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
        text="Encrypt a Video",
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
        master=encrypt_frame,
        width=600,
        height=590,
        fg_color=MEDICRYPT_COLORS["default_bg"],
        bg_color=MEDICRYPT_COLORS["default_bg"]
    )
    main.grid_propagate(False)
    main.grid(column=0, row=1, pady=2)

    main.grid_columnconfigure(0, weight=1)
    main.grid_columnconfigure(3, weight=1)

    file_label = CTkLabel(
        master=main,
        text="Video File",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    file_label.grid(column=0, row=0, columnspan=2, padx=2, pady=[5, 0], sticky="w")

    file_inpt = CTkEntry(
        master=main,
        text_color="black",
        placeholder_text="Enter a file path or choose a file",
        font=gen_fnt,
        width=550,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    file_inpt.grid(column=0, row=1, padx=2, pady=5)

    upload_img = CTkImage(
        light_image=Image.open('assets/img/folder.png'),
        dark_image=Image.open('assets/img/folder.png'),
        size=(25, 25)
    )

    # Create the button to upload a file
    upload_btn = CTkButton(
        master=main,
        text="",
        image=upload_img,
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
    upload_btn.grid(column=1, row=1, padx=2, pady=5)

    password_label = CTkLabel(
        master=main,
        text="Password",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    password_label.grid(column=0, row=2, columnspan=2, padx=2, pady=[5, 0], sticky="w")

    password_inpt = CTkEntry(
        master=main,
        text_color="black",
        placeholder_text="Enter a password",
        font=gen_fnt,
        width=605,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    password_inpt.grid(column=0, row=3, columnspan=2, padx=2, pady=5)

    algo_label = CTkLabel(
        master=main,
        text="Choose an Encryption Algorithm",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    algo_label.grid(column=0, row=4, columnspan=2, padx=2, pady=[5, 0], sticky="w")

    algo_frame = CTkFrame(
        master=main,
        width=600,
        height=60,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )
    algo_frame.grid(column=0, row=5, pady=5, sticky="nsew", columnspan=2)

    # Configure btn_frame grid to have equal weights for centering the buttons
    algo_frame.grid_columnconfigure(0, weight=1)
    algo_frame.grid_columnconfigure(1, weight=1)
    algo_frame.grid_columnconfigure(2, weight=1)

    algo_var = StringVar(value="other")

    algo_1 = CTkRadioButton(
        master=algo_frame,
        text="FY-Logistic",
        text_color="black",
        font=gen_fnt,
        value="FY-Logistic",
        variable=algo_var
    )
    algo_1.grid(column=0, row=0, padx=2, pady=5, sticky="ew")

    algo_2 = CTkRadioButton(
        master=algo_frame,
        text="ILM-Cosine",
        text_color="black",
        font=gen_fnt,
        value="ILM-Cosine",
        variable=algo_var
    )
    algo_2.grid(column=1, row=0, padx=2, pady=5, sticky="ew")

    lock_img = CTkImage(
        light_image=Image.open('assets/img/lock.png'),
        dark_image=Image.open('assets/img/lock.png'),
        size=(22, 22)
    )

    encrypt_btn = CTkButton(
        master=main,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="START ENCRYPTION",
        font=encrypt_fnt,
        image=lock_img,
        width=400,
        height=60,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "progress1", getFilename, "ENCRYPTING")
    )
    encrypt_btn.grid(column=0, row=6, padx=4, pady=20, sticky='ew', columnspan=2)

    # Center the encrypt frame within the master_frame
    encrypt_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    encrypt_frame.place(relx=0.5, rely=0.5, anchor='center')

def browseFile(file_inpt):
    global getFilename
    filename = filedialog.askopenfilename(filetypes=((".avi files", ".avi"), ("All files", "*")))
    getFilename = filename
    file_inpt.delete(0, END)
    file_inpt.insert(0, filename)
