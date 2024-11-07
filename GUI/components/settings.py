#settings.py

import customtkinter as ctk
from tkinter import messagebox

class Settings:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.frame = None
        self.output_textbox = None  # Output board to show messages

    def render(self):
        # Clear the current content in the parent frame
        self.clear_content()

        # Create a frame for the settings content
        self.frame = ctk.CTkFrame(self.parent_frame)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.parent_frame.rowconfigure(0, weight=1)
        self.parent_frame.columnconfigure(0, weight=1)

        # Title
        title_label = ctk.CTkLabel(self.frame, text="Settings", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Theme Selection
        theme_label = ctk.CTkLabel(self.frame, text="Theme:")
        theme_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")
        
        theme_option = ctk.CTkOptionMenu(self.frame, values=["Light", "Dark", "System Default"], command=self.change_theme)
        theme_option.grid(row=1, column=1, padx=20, pady=(10, 0))

        # Notification Toggle
        notification_label = ctk.CTkLabel(self.frame, text="Enable Notifications:")
        notification_label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="w")
        
        self.notification_switch = ctk.CTkSwitch(self.frame, text="", command=self.toggle_notifications)
        self.notification_switch.grid(row=2, column=1, padx=20, pady=(10, 0))

        # Sound Settings
        sound_label = ctk.CTkLabel(self.frame, text="Enable Sound:")
        sound_label.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="w")
        
        self.sound_switch = ctk.CTkSwitch(self.frame, text="", command=self.toggle_sound)
        self.sound_switch.grid(row=3, column=1, padx=20, pady=(10, 0))

        # Language Option
        language_label = ctk.CTkLabel(self.frame, text="Language:")
        language_label.grid(row=4, column=0, padx=20, pady=(10, 0), sticky="w")
        
        language_option = ctk.CTkOptionMenu(self.frame, values=["English", "Spanish", "French"], command=self.change_language)
        language_option.grid(row=4, column=1, padx=20, pady=(10, 0))

        # Auto-update Toggle
        auto_update_label = ctk.CTkLabel(self.frame, text="Enable Auto-Updates:")
        auto_update_label.grid(row=5, column=0, padx=20, pady=(10, 0), sticky="w")
        
        self.auto_update_switch = ctk.CTkSwitch(self.frame, text="", command=self.toggle_auto_update)
        self.auto_update_switch.grid(row=5, column=1, padx=20, pady=(10, 0))

        # Data Backup Option
        backup_label = ctk.CTkLabel(self.frame, text="Data Backup:")
        backup_label.grid(row=6, column=0, padx=20, pady=(10, 0), sticky="w")
        
        backup_button = ctk.CTkButton(self.frame, text="Backup Now", command=self.backup_data)
        backup_button.grid(row=6, column=1, padx=20, pady=(10, 0))

        # Save Button
        save_button = ctk.CTkButton(self.frame, text="Save Settings", command=self.save_settings)
        save_button.grid(row=7, column=0, columnspan=2, padx=20, pady=(20, 10))

        # Output Board for Displaying Messages
        self.output_textbox = ctk.CTkTextbox(self.frame, height=100, state="disabled")
        self.output_textbox.grid(row=8, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="nsew")

    def change_theme(self, theme):
        """Change the theme of the application."""
        ctk.set_appearance_mode(theme)
        self.display_message(f"Theme changed to: {theme}")

    def toggle_notifications(self):
        """Toggle notification settings."""
        status = "enabled" if self.notification_switch.get() else "disabled"
        self.display_message(f"Notifications {status.capitalize()}")

    def toggle_sound(self):
        """Toggle sound settings."""
        status = "enabled" if self.sound_switch.get() else "disabled"
        self.display_message(f"Sound {status.capitalize()}")

    def change_language(self, language):
        """Change the language of the application."""
        self.display_message(f"Language changed to: {language}")

    def toggle_auto_update(self):
        """Toggle auto-update setting."""
        status = "enabled" if self.auto_update_switch.get() else "disabled"
        self.display_message(f"Auto-Updates {status.capitalize()}")

    def backup_data(self):
        """Mockup function for data backup."""
        self.display_message("Data backup has been initiated.")
        messagebox.showinfo("Data Backup", "Data backup has been initiated.")

    def save_settings(self):
        """Save settings (for demo purposes, this just prints the values)."""
        theme = ctk.get_appearance_mode()
        notifications_enabled = self.notification_switch.get()
        sound_enabled = self.sound_switch.get()
        auto_update_enabled = self.auto_update_switch.get()

        self.display_message(f"Settings saved: Theme={theme}, Notifications={'enabled' if notifications_enabled else 'disabled'}, "
                             f"Sound={'enabled' if sound_enabled else 'disabled'}, Auto-Update={'enabled' if auto_update_enabled else 'disabled'}")
        messagebox.showinfo("Settings", "Settings have been saved successfully.")

    def display_message(self, message):
        """Helper method to display messages on the output board."""
        self.output_textbox.configure(state="normal")
        self.output_textbox.insert("end", message + "\n")
        self.output_textbox.configure(state="disabled")
        self.output_textbox.yview("end")  # Auto-scroll to the bottom

    def clear_content(self):
        """Clear the content of the parent frame to avoid stacking multiple frames."""
        if self.frame:
            for widget in self.frame.winfo_children():
                widget.grid_forget()
