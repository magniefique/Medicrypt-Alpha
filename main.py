from customtkinter import *
import tabs.screen_menu as screen_menu
import tabs.screen_encrypt as screen_encrypt
import tabs.screen_decrypt as screen_decrypt
import tabs.screen_progress as screen_progress
import tabs.screen_done as screen_done
from assets.colors import *

# Function to switch tabs
def switchTab(root_frame, tab_name, file=None, progress=None):
    # Clear current contents of the frame
    for widget in root_frame.winfo_children():
        widget.destroy()

    # Display the selected tab
    if tab_name == "menu":
        screen_menu.menuDisplay(root_frame, switchTab)

    elif tab_name == "encrypt":
        screen_encrypt.encryptDisplayNew(root_frame, switchTab)

    elif tab_name == "decrypt":
        screen_decrypt.decryptDisplayNew(root_frame, switchTab)

    elif tab_name == "progress1":
        screen_progress.progressRun1(root_frame, switchTab, file, progress)

    elif tab_name == "progress2":
        screen_progress.progressRun2(root_frame, switchTab, file, progress)

    elif tab_name == "complete1":
        screen_done.doneDisplay(root_frame, switchTab, file, "ENCRYPTION")
    
    elif tab_name == "complete2":
        screen_done.doneDisplay(root_frame, switchTab, file, "DECRYPTION")

# Main function for the Application
def mainFunc():
    # Configurations for the window
    main_win = CTk()
    main_win.geometry("720x720")
    main_win.resizable(False, False)
    main_win.config(background=MEDICRYPT_COLORS["default_bg"])
    main_win.title("Medicrypt")

    # Main Frame
    main_frame = CTkFrame(
        master=main_win,
        width=720,
        height=720,
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