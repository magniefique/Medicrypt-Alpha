from customtkinter import *
from assets.colors import *
from PIL import Image

def decryptDisplay(master_frame, switch_func):
    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    # Create the decrypt frame
    decrypt_frame = CTkFrame(
        master=  master_frame,
        width=720, 
        height=480, 
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    back_btn = CTkButton(
        master=decrypt_frame,
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
        master=decrypt_frame,
        text_color="black",
        placeholder_text="Enter a file path or choose a file",
        font= None,
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
        master=decrypt_frame,
        text="File",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font= None,
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

    hash_inpt = CTkEntry(
        master=decrypt_frame,
        text_color="black",
        placeholder_text="Enter a file path for a hash list or choose a file",
        font= None,
        width=550,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    hash_inpt.grid(column=0, row=2, padx=2, pady=5)

    # Create the button to upload a file
    upload_hash_btn = CTkButton(
        master=decrypt_frame,
        text="File",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font= None,
        width=50,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
        hover_color=MEDICRYPT_COLORS["default_bg"],
        command=lambda: browseHashFile(hash_inpt)
    )
    upload_hash_btn.grid(column=1, row=2, padx=2, pady=5)

    password_inpt = CTkEntry(
        master=decrypt_frame,
        text_color="black",
        placeholder_text="Enter a password",
        font= None,
        width=605,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    password_inpt.grid(column=0, row=3, columnspan=2, padx=2, pady=5)

    btn_frame = CTkFrame(
        master=decrypt_frame,
        width=720,
        height=40,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )
    btn_frame.grid(column=0, row=4, pady=5, sticky="nw")

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

    decrypt_btn = CTkButton(
        master=decrypt_frame,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="Decrypt",
        width=100,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "menu")
    )
    decrypt_btn.grid(column=0, row=5, padx=4, pady=20, sticky='w')

    # Center the decrypt frame within the master_frame
    decrypt_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    decrypt_frame.place(relx=0.5, rely=0.5, anchor='center')

def decryptDisplayNew(master_frame, switch_func):
    
    
    decrypt_fnt = CTkFont(
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

    # Create the decrypt frame
    decrypt_frame = CTkFrame(
        master=master_frame,
        width=720,
        height=720,
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    nav = CTkFrame(
        master=decrypt_frame,
        width=620,
        height=60,
        fg_color=MEDICRYPT_COLORS["default_bg"],
        bg_color=MEDICRYPT_COLORS["default_bg"]
    )
    nav.grid_propagate(False)
    nav.grid(column=0, row=0, pady=2, sticky="w")

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

    main = CTkFrame(
        master=decrypt_frame,
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

    hash_label = CTkLabel(
        master=main,
        text="Hash List File",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    hash_label.grid(column=0, row=2, columnspan=2, padx=2, pady=[5, 0], sticky="w")

    hash_inpt = CTkEntry(
        master=main,
        text_color="black",
        placeholder_text="Enter a file path or choose a hash list file",
        font=gen_fnt,
        width=550,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
    )
    hash_inpt.grid(column=0, row=3, padx=2, pady=5)

    hash_upload_img = CTkImage(
        light_image=Image.open('assets/img/file.png'),
        dark_image=Image.open('assets/img/file.png'),
        size=(25, 25)
    )

    # Create the button to upload a file
    hash_upload_btn = CTkButton(
        master=main,
        text="",
        image=hash_upload_img,
        width=50,
        height=50,
        corner_radius=0,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
        border_width=2,
        border_color=MEDICRYPT_COLORS["default_btn"],
        hover_color=MEDICRYPT_COLORS["default_bg"],
        command=lambda: browseHashFile(file_inpt)
    )
    hash_upload_btn.grid(column=1, row=3, padx=2, pady=5)

    password_label = CTkLabel(
        master=main,
        text="Password",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    password_label.grid(column=0, row=4, columnspan=2, padx=2, pady=[5, 0], sticky="w")

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
    password_inpt.grid(column=0, row=5, columnspan=2, padx=2, pady=5)

    algo_label = CTkLabel(
        master=main,
        text="Choose an decryption Algorithm",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=label_fnt
    )
    algo_label.grid(column=0, row=6, columnspan=2, padx=2, pady=[5, 0], sticky="w")

    algo_frame = CTkFrame(
        master=main,
        width=600,
        height=60,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )
    algo_frame.grid(column=0, row=7, pady=5, sticky="nsew", columnspan=2)

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

    unlock_img = CTkImage(
        light_image=Image.open('assets/img/unlock.png'),
        dark_image=Image.open('assets/img/unlock.png'),
        size=(22, 22)
    )

    decrypt_btn = CTkButton(
        master=main,
        text_color=MEDICRYPT_COLORS["default_bg"],
        text="START DECRYPTION",
        font=decrypt_fnt,
        image=unlock_img,
        width=400,
        height=60,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "menu")
    )
    decrypt_btn.grid(column=0, row=8, padx=4, pady=20, sticky='ew', columnspan=2)

    # Center the decrypt frame within the master_frame
    decrypt_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    decrypt_frame.place(relx=0.5, rely=0.5, anchor='center')

def browseFile(file_inpt):
    filename = filedialog.askopenfilename(filetypes=((".mp4 files", ".mp4"), ("All files", "*")))
    file_inpt.delete(0, END)
    file_inpt.insert(0, filename)

def browseHashFile(file_inpt):
    filename = filedialog.askopenfilename(filetypes=((".txt files", ".txt"), ("All files", "*")))
    file_inpt.delete(0, END)
    file_inpt.insert(0, filename)