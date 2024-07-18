from customtkinter import *
from assets.colors import *

def menuDisplay(master_frame, switch_func):
    # Clear current contents of the master_frame
    for widget in master_frame.winfo_children():
        widget.destroy()

    menu_font = CTkFont(
        family="Times",
        size=48,
        weight="bold"
    )

    btn_font = CTkFont(
        family="Poppins", 
        size=16,
        weight="bold",
    )

    menu_frame = CTkFrame(
        master=  master_frame,
        width=720, 
        height=480, 
        corner_radius=0,
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    medicrypt_logo = CTkLabel(
        master=menu_frame,
        text="MEDICRYPT",
        text_color=MEDICRYPT_COLORS["default_btn"],
        font=menu_font,
        width=100,
        height=100,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )
    medicrypt_logo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    encrypt_btn = CTkButton(
        master=menu_frame,
        text="ENCRYPT",
        font=btn_font,
        width=200,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "encrypt")
    )

    decrypt_btn = CTkButton(
        master=menu_frame,
        text="DECRYPT",
        font=btn_font,
        width=200,
        height=40,
        corner_radius=10,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_btn"],
        command=lambda: switch_func(master_frame, "decrypt")
    )

    encrypt_btn.grid(column=0, row=1, padx=20)
    decrypt_btn.grid(column=1, row=1, padx=20)

    menu_frame.pack_propagate(False)  # Prevent frame from resizing to fit its children
    menu_frame.place(relx=0.5, rely=0.5, anchor='center')