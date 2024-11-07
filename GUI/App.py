import tkinter as tk
import customtkinter as ctk

# Import the components
from components.dashboard import Dashboard
from components.safe_house import SafeHouse
from components.analytics import Analytics
from components.alerts import Alerts
from components.radar import Radar
from components.about import About
from components.contact import Contact
from components.settings import Settings

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
        
        # Theme Color Options
        self.theme_color_label = ctk.CTkLabel(self.sidebar_frame, text="Theme Color:", anchor="w")
        self.theme_color_label.grid(row=10, column=0, padx=20, pady=(20, 5))
        self.theme_color_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["blue", "green", "dark-blue"], command=self.change_theme_color_event)
        self.theme_color_optionmenu.grid(row=11, column=0, padx=20, pady=10)
        
        # Set default values after the widgets are created
        self.appearance_mode_optionmenu.set("System")
        self.scaling_optionmenu.set("100%")
        self.theme_color_optionmenu.set("blue")
        
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
        
        # Main Content Area (Dashboard, Safe House, etc.)
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Placeholder for content area
        self.content_label = ctk.CTkLabel(self.main_frame, text="Welcome to Fire Detection System")
        self.content_label.grid(row=0, column=0, padx=20, pady=20)
    
    def clear_main_content(self):
        """Clear the main content area."""
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

    # Sidebar button events
    def show_dashboard(self):
        self.clear_main_content()
        dashboard = Dashboard(self.main_frame)
        dashboard.render()
    
    def show_safe_house(self):
        self.clear_main_content()
        safe_house = SafeHouse(self.main_frame)
        safe_house.render()
    
    def show_analytics(self):
        self.clear_main_content()
        analytics = Analytics(self.main_frame)
        analytics.render()
    
    def show_alerts(self):
        self.clear_main_content()
        alerts = Alerts(self.main_frame)
        alerts.render()
    
    def show_radar(self):
        self.clear_main_content()
        radar = Radar(self.main_frame)
        radar.render()
    
    def show_about(self):
        self.clear_main_content()
        about = About(self.main_frame)
        about.render()
    
    def show_contact(self):
        self.clear_main_content()
        contact = Contact(self.main_frame)
        contact.render()
    
    def show_settings(self):
        self.clear_main_content()
        settings = Settings(self.main_frame)
        settings.render()

    # Event Handlers
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
