import tkinter as tk
import customtkinter as ctk

# Setting up appearance and theme
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Default Theme: "blue", "green", "dark-blue"

class FireDetectionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("Fire Detection System")
        self.geometry("1200x700")  # Adjust the size for responsiveness
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar Frame - Left Sidebar (Main Navigation)
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsw")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Fire Detection", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Sidebar Navigation Buttons
        self.sidebar_button_dashboard = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.show_dashboard)
        self.sidebar_button_dashboard.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_safe_house = ctk.CTkButton(self.sidebar_frame, text="Safe House", command=self.show_safe_house)
        self.sidebar_button_safe_house.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_analytics = ctk.CTkButton(self.sidebar_frame, text="Analytics", command=self.show_analytics)
        self.sidebar_button_analytics.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_alerts = ctk.CTkButton(self.sidebar_frame, text="Alerts", command=self.show_alerts)
        self.sidebar_button_alerts.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_button_radar = ctk.CTkButton(self.sidebar_frame, text="Radar", command=self.show_radar)
        self.sidebar_button_radar.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
        
        # Appearance Mode Options
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(20, 5))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=7, column=0, padx=20, pady=10)
        
        # UI Scaling Options
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(20, 5))
        self.scaling_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=9, column=0, padx=20, pady=10)
        
        # Right Vertical Sidebar (Settings, About, etc.)
        self.right_sidebar_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=2, rowspan=3, sticky="ns")
        
        # Buttons in the right vertical sidebar
        self.right_sidebar_button_about = ctk.CTkButton(self.right_sidebar_frame, text="About", command=self.show_about)
        self.right_sidebar_button_about.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        
        self.right_sidebar_button_contact = ctk.CTkButton(self.right_sidebar_frame, text="Contact", command=self.show_contact)
        self.right_sidebar_button_contact.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.right_sidebar_button_settings = ctk.CTkButton(self.right_sidebar_frame, text="Settings", command=self.show_settings)
        self.right_sidebar_button_settings.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        # Theme color changing option
        self.theme_color_label = ctk.CTkLabel(self.right_sidebar_frame, text="Theme Color:", anchor="w")
        self.theme_color_label.grid(row=3, column=0, padx=20, pady=(20, 5))

        # Option Menu for theme colors (restrict to predefined options)
        self.theme_color_optionmenu = ctk.CTkOptionMenu(self.right_sidebar_frame, values=["blue", "green", "dark-blue"], command=self.change_theme_color_event)
        self.theme_color_optionmenu.grid(row=4, column=0, padx=20, pady=10)

        # Main Content Area (Dashboard, Safe House, etc.)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Placeholder for content area
        self.content_label = ctk.CTkLabel(self.main_frame, text="Welcome to Fire Detection System")
        self.content_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Set default values
        self.appearance_mode_optionmenu.set("System")
        self.scaling_optionmenu.set("100%")
    
    # Sidebar button events
    def show_dashboard(self):
        self.clear_main_content()
        dashboard_text = """Dashboard Content:
        
        - Overview of fire detection status
        - Real-time data from sensors
        - Safety status"""
        dashboard_label = ctk.CTkLabel(self.main_frame, text=dashboard_text, justify="left")
        dashboard_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_safe_house(self):
        self.clear_main_content()
        safe_house_text = """Safe House Content:
        
        - Emergency evacuation plan
        - Safe house locations
        - Escape routes"""
        safe_house_label = ctk.CTkLabel(self.main_frame, text=safe_house_text, justify="left")
        safe_house_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_analytics(self):
        self.clear_main_content()
        analytics_text = """Analytics Content:
        
        - Historical fire data
        - Risk analysis and predictions
        - Graphs and charts"""
        analytics_label = ctk.CTkLabel(self.main_frame, text=analytics_text, justify="left")
        analytics_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_alerts(self):
        self.clear_main_content()
        alerts_text = """Alerts Content:
        
        - Active fire alerts
        - Notifications and warnings
        - Critical event log"""
        alerts_label = ctk.CTkLabel(self.main_frame, text=alerts_text, justify="left")
        alerts_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_radar(self):
        self.clear_main_content()
        radar_text = """Radar Content:
        
        - Real-time fire detection radar feed
        - Map with detected hotspots
        - Sensor network coverage"""
        radar_label = ctk.CTkLabel(self.main_frame, text=radar_text, justify="left")
        radar_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_about(self):
        self.clear_main_content()
        about_text = """About the Fire Detection System:
        
        This system is designed to detect fire risks in buildings and send alerts to the users. 
        It provides analytics and a safe house feature for emergency situations."""
        about_label = ctk.CTkLabel(self.main_frame, text=about_text, justify="left")
        about_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_contact(self):
        self.clear_main_content()
        contact_text = """Contact Information:
        
        - Email: support@firedetect.com
        - Phone: +123456789"""
        contact_label = ctk.CTkLabel(self.main_frame, text=contact_text, justify="left")
        contact_label.grid(row=0, column=0, padx=20, pady=20)
    
    def show_settings(self):
        """Show the Settings page with the following features:
        - Adjust Detection Sensitivity
        - Configure Alert Notifications
        - Manage User Profiles
        - Set Threshold, Alert Sound, Notification Channels, etc."""
        
        self.clear_main_content()
        
        # Create the settings interface
        
        # Detection Sensitivity
        self.sensitivity_label = ctk.CTkLabel(self.main_frame, text="Detection Sensitivity:", anchor="w")
        self.sensitivity_label.grid(row=0, column=0, padx=20, pady=(20, 5))
        
        self.sensitivity_slider = ctk.CTkSlider(self.main_frame, from_=0, to=100, number_of_steps=10, command=self.update_sensitivity)
        self.sensitivity_slider.set(50)  # Set initial value
        self.sensitivity_slider.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.sensitivity_value_label = ctk.CTkLabel(self.main_frame, text="Sensitivity: 50%", anchor="w")
        self.sensitivity_value_label.grid(row=2, column=0, padx=20, pady=(5, 20))
        
        # Detection Threshold
        self.threshold_label = ctk.CTkLabel(self.main_frame, text="Detection Threshold (Temp):", anchor="w")
        self.threshold_label.grid(row=3, column=0, padx=20, pady=(20, 5))
        
        self.threshold_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Enter temperature (°C)")
        self.threshold_entry.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        
        self.threshold_value_label = ctk.CTkLabel(self.main_frame, text="Threshold: None", anchor="w")
        self.threshold_value_label.grid(row=5, column=0, padx=20, pady=(5, 20))
        
        # Alert Sound Toggle
        self.sound_label = ctk.CTkLabel(self.main_frame, text="Enable Alert Sound:", anchor="w")
        self.sound_label.grid(row=6, column=0, padx=20, pady=(20, 5))
        
        self.sound_checkbox = ctk.CTkCheckBox(self.main_frame, text="Enable Sound", command=self.toggle_sound)
        self.sound_checkbox.grid(row=7, column=0, padx=20, pady=10, sticky="w")
        
        self.sound_status_label = ctk.CTkLabel(self.main_frame, text="Sound: Disabled", anchor="w")
        self.sound_status_label.grid(row=8, column=0, padx=20, pady=(5, 20))
        
        # Notification Channel
        self.channel_label = ctk.CTkLabel(self.main_frame, text="Select Notification Channel:", anchor="w")
        self.channel_label.grid(row=9, column=0, padx=20, pady=(20, 5))
        
        self.channel_optionmenu = ctk.CTkOptionMenu(self.main_frame, values=["Email", "SMS", "Push Notification"], command=self.change_channel)
        self.channel_optionmenu.set("Email")  # Default value
        self.channel_optionmenu.grid(row=10, column=0, padx=20, pady=10, sticky="ew")
        
        self.channel_value_label = ctk.CTkLabel(self.main_frame, text="Notification Channel: Email", anchor="w")
        self.channel_value_label.grid(row=11, column=0, padx=20, pady=(5, 20))
        
        # Auto Response
        self.auto_response_label = ctk.CTkLabel(self.main_frame, text="Enable Auto-Response:", anchor="w")
        self.auto_response_label.grid(row=12, column=0, padx=20, pady=(20, 5))
        
        self.auto_response_checkbox = ctk.CTkCheckBox(self.main_frame, text="Enable Auto-Response", command=self.toggle_auto_response)
        self.auto_response_checkbox.grid(row=13, column=0, padx=20, pady=10, sticky="w")
        
        self.auto_response_status_label = ctk.CTkLabel(self.main_frame, text="Auto-Response: Disabled", anchor="w")
        self.auto_response_status_label.grid(row=14, column=0, padx=20, pady=(5, 20))
        
        # Save Settings Button
        self.save_button = ctk.CTkButton(self.main_frame, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=15, column=0, padx=20, pady=(20, 10), sticky="ew")
    
    def clear_main_content(self):
        """Clear the main content area."""
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

    # Event Handlers for Settings
    def update_sensitivity(self, value):
        """Update the sensitivity value based on slider input."""
        sensitivity_percentage = int(float(value))
        self.sensitivity_value_label.configure(text=f"Sensitivity: {sensitivity_percentage}%")

    def toggle_sound(self):
        """Toggle alert sound on or off."""
        if self.sound_checkbox.get():
            self.sound_status_label.configure(text="Sound: Enabled")
        else:
            self.sound_status_label.configure(text="Sound: Disabled")

    def change_channel(self, selected_channel):
        """Change notification channel (Email, SMS, Push Notification)."""
        self.channel_value_label.configure(text=f"Notification Channel: {selected_channel}")

    def toggle_auto_response(self):
        """Enable or disable auto-response."""
        if self.auto_response_checkbox.get():
            self.auto_response_status_label.configure(text="Auto-Response: Enabled")
        else:
            self.auto_response_status_label.configure(text="Auto-Response: Disabled")

    def save_settings(self):
        """Save all settings and display a message."""
        threshold_value = self.threshold_entry.get()
        notification_channel = self.channel_optionmenu.get()
        print(f"Settings Saved:")
        print(f"Detection Threshold: {threshold_value}")
        print(f"Notification Channel: {notification_channel}")
        # Additional settings can be saved or processed here

        # Show a message that the settings were saved
        saved_label = ctk.CTkLabel(self.main_frame, text="Settings saved successfully!", fg_color="green")
        saved_label.grid(row=16, column=0, padx=20, pady=10)
    
    def clear_main_content(self):
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()
    
    # Event handlers
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
    
    def change_theme_color_event(self, new_color: str):
        ctk.set_default_color_theme(new_color)

if __name__ == "__main__":
    app = FireDetectionApp()
    app.mainloop()
