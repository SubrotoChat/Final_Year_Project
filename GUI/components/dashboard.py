#dashboard.py

import customtkinter as ctk
from tkinter import Canvas, Scrollbar

class Dashboard:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.frame = None

    def render(self):
        # Ensure there is no existing content before setting up the new frame
        self.clear_content()

        # Create a frame for the dashboard content
        self.frame = ctk.CTkFrame(self.parent_frame)
        self.frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.parent_frame.rowconfigure(0, weight=1)
        self.parent_frame.columnconfigure(0, weight=1)

        # Create the tabview for different sections
        self.create_tabview()

    def create_tabview(self):
        # Create the Tabview with 3 tabs
        self.tabview = ctk.CTkTabview(self.frame, width=1100, height=700)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Add tabs for Overview, Real-time Data, Safety Status, and Emergency Notifications
        self.tabview.add("Overview of Fire Detection Status")
        self.tabview.add("Real-Time Data from Sensors")
        self.tabview.add("Safety Status")
        self.tabview.add("Emergency Notifications")
        
        # Configure individual tabs
        self.tabview.tab("Overview of Fire Detection Status").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Real-Time Data from Sensors").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Safety Status").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Emergency Notifications").grid_columnconfigure(0, weight=1)
        
        # Add content to each tab
        self.add_overview_content()
        self.add_real_time_data_content()
        self.add_safety_status_content()
        self.add_emergency_notifications_content()

    def add_overview_content(self):
        # Create content for the "Overview of Fire Detection Status" tab
        overview_content_frame = ctk.CTkFrame(self.tabview.tab("Overview of Fire Detection Status"))
        overview_content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        overview_content_frame.columnconfigure(0, weight=1)

        # Title for the tab content
        overview_label = ctk.CTkLabel(overview_content_frame, text="Fire Detection Status Overview", font=ctk.CTkFont(size=18, weight="bold"))
        overview_label.pack(pady=10)

        # Add additional content (Example: Real-time data summary, status, etc.)
        example_label = ctk.CTkLabel(overview_content_frame, text="This is the overview content for fire detection status")
        example_label.pack(pady=10)

    def add_real_time_data_content(self):
        # Create content for the "Real-Time Data from Sensors" tab
        real_time_content_frame = ctk.CTkFrame(self.tabview.tab("Real-Time Data from Sensors"))
        real_time_content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        real_time_content_frame.columnconfigure(0, weight=1)

        # Title for the tab content
        real_time_label = ctk.CTkLabel(real_time_content_frame, text="Real-Time Data from Sensors", font=ctk.CTkFont(size=18, weight="bold"))
        real_time_label.pack(pady=10)

        # Add additional content (Example: Sensor data visualization or status)
        example_label = ctk.CTkLabel(real_time_content_frame, text="This is the real-time data from sensors")
        example_label.pack(pady=10)

    def add_safety_status_content(self):
        # Create content for the "Safety Status" tab
        safety_status_content_frame = ctk.CTkFrame(self.tabview.tab("Safety Status"))
        safety_status_content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        safety_status_content_frame.columnconfigure(0, weight=1)

        # Title for the tab content
        safety_status_label = ctk.CTkLabel(safety_status_content_frame, text="Safety Status", font=ctk.CTkFont(size=18, weight="bold"))
        safety_status_label.pack(pady=10)

        # Add additional content (Example: Safety checks or status)
        example_label = ctk.CTkLabel(safety_status_content_frame, text="This is the safety status content")
        example_label.pack(pady=10)

    def add_emergency_notifications_content(self):
        # Create content for the "Emergency Notifications" tab
        emergency_content_frame = ctk.CTkFrame(self.tabview.tab("Emergency Notifications"))
        emergency_content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        emergency_content_frame.columnconfigure(0, weight=1)

        # Title for the tab content
        emergency_label = ctk.CTkLabel(emergency_content_frame, text="Emergency Notifications", font=ctk.CTkFont(size=18, weight="bold"))
        emergency_label.pack(pady=10)

        # Add additional content (Example: Notifications, alerts, etc.)
        example_label = ctk.CTkLabel(emergency_content_frame, text="This is the emergency notifications content")
        example_label.pack(pady=10)

    def clear_content(self):
        """Clear the content of the parent frame to avoid stacking multiple frames."""
        if self.frame:  # Only clear if self.frame exists
            for widget in self.frame.winfo_children():
                widget.grid_forget()
