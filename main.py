from customtkinter import *
import tabs.screen_menu as screen_menu
import tabs.screen_encrypt as screen_encrypt
import tabs.screen_decrypt as screen_decrypt
import tabs.screen_progress as screen_progress
from assets.colors import *

# Function to switch tabs
def switchTab(root_frame, tab_name, file=None):
    # Clear current contents of the frame
    for widget in root_frame.winfo_children():
        widget.destroy()

    # Display the selected tab
    if tab_name == "menu":
        screen_menu.menuDisplay(root_frame, switchTab)

    elif tab_name == "encrypt":
        screen_encrypt.encryptDisplay(root_frame, switchTab)

    elif tab_name == "decrypt":
        screen_decrypt.decryptDisplay(root_frame, switchTab)

    elif tab_name == "progress":
        screen_progress.progressDisplay(root_frame, switchTab, file)


# Main function for the Application
def mainFunc():
    # Configurations for the window
    main_win = CTk()
    main_win.geometry("720x480")
    main_win.resizable(False, False)
    main_win.config(background=MEDICRYPT_COLORS["default_bg"])
    main_win.title("Medicrypt")

    # Main Frame
    main_frame = CTkFrame(
        master=main_win,
        width=720,
        height=480,
        bg_color=MEDICRYPT_COLORS["default_bg"],
        fg_color=MEDICRYPT_COLORS["default_bg"],
    )

    main_frame.pack(expand=True, fill="both")

    # Display the initial tab
    switchTab(main_frame, "menu")

    # Main loop of the application
    main_win.mainloop()

if __name__ == "__main__":
    mainFunc()
