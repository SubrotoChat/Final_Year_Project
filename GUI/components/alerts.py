#alerts.py

import customtkinter as ctk

class Alerts:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.frame = None

    def render(self):
        """Render the content for the Alerts section."""
        self.clear_content()  # Remove any previous content

        # Create a new frame for Alerts content
        self.frame = ctk.CTkFrame(self.parent_frame)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        label = ctk.CTkLabel(self.frame, text="Alerts", font=ctk.CTkFont(size=20, weight="bold"))
        label.grid(row=0, column=0, padx=20, pady=20)

        # Add additional widgets as needed
        alerts_info_label = ctk.CTkLabel(self.frame, text="Real-time alerts will be shown here.")
        alerts_info_label.grid(row=1, column=0, padx=20, pady=10)

    def clear_content(self):
        """Clear the content of the parent frame to avoid stacking multiple frames."""
        for widget in self.parent_frame.winfo_children():
            widget.grid_forget()
