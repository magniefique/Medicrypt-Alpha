from customtkinter import *
from assets.colors import *
import fisher_yates_encrypt


def progressDisplay(master_frame, switch_func, file):
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

    runEncryption(file)


def runEncryption(file):
    e = fisher_yates_encrypt.Encrypt()
    e.readVideo(file)
