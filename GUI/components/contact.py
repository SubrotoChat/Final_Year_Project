#contact.py

import customtkinter as ctk

class Contact:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.frame = None

    def render(self):
        """Render the content for the Contact section."""
        self.clear_content()  # Remove any previous content

        # Create a new frame for Contact content
        self.frame = ctk.CTkFrame(self.parent_frame)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        label = ctk.CTkLabel(self.frame, text="Contact", font=ctk.CTkFont(size=20, weight="bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        # Add additional widgets as needed
        contact_info_label = ctk.CTkLabel(self.frame, text="Contact information for the Fire Detection System.")
        contact_info_label.grid(row=1, column=0, padx=20, pady=10)

    def clear_content(self):
        """Clear the content of the parent frame to avoid stacking multiple frames."""
        for widget in self.parent_frame.winfo_children():
            widget.grid_forget()
