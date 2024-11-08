import cv2
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import os
from datetime import datetime

class Camera:
    def __init__(self, parent):
        self.parent = parent
        self.camera_frame = ctk.CTkFrame(self.parent, width=700, height=800)
        self.camera_frame.grid(row=0, column=0, sticky="nsew")

        # Ensure 'records' folder exists for saving images/videos
        os.makedirs("records", exist_ok=True)

        self.video_label = tk.Label(self.camera_frame)
        self.video_label.pack(fill="both", expand=True)

        # State variables
        self.cap = None
        self.is_running = False
        self.is_recording = False
        self.zoom_factor = 1.0
        self.camera_index = 0  # Default to integrated camera
        self.fps = 30  # Default frame rate
        self.aspect_ratios = {
            "4:3": (640, 480),
            "16:9": (1280, 720),
            "1:1": (640, 640),
            "21:9": (1920, 820)
        }

        # Control Buttons
        self.controls_frame = ctk.CTkFrame(self.camera_frame)
        self.controls_frame.pack(side="bottom", fill="x", pady=10)

        self.start_button = ctk.CTkButton(self.controls_frame, text="Start Camera", command=self.toggle_camera)
        self.start_button.grid(row=0, column=0, padx=10)

        self.aspect_ratio_button = ctk.CTkOptionMenu(
            self.controls_frame, values=list(self.aspect_ratios.keys()), command=self.change_aspect_ratio
        )
        self.aspect_ratio_button.set("4:3")
        self.aspect_ratio_button.grid(row=0, column=1, padx=10)

        self.zoom_in_button = ctk.CTkButton(self.controls_frame, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.grid(row=0, column=2, padx=10)

        self.zoom_out_button = ctk.CTkButton(self.controls_frame, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.grid(row=0, column=3, padx=10)

        self.capture_button = ctk.CTkButton(self.controls_frame, text="Capture Image", command=self.capture_image)
        self.capture_button.grid(row=1, column=2, padx=10)

        self.record_button = ctk.CTkButton(self.controls_frame, text="Start Recording", command=self.toggle_recording)
        self.record_button.grid(row=1, column=3, padx=10)

        self.camera_select_button = ctk.CTkOptionMenu(
            self.controls_frame, values=["Integrated Camera", "External Camera"], command=self.change_camera_source
        )
        self.camera_select_button.set("Integrated Camera")
        self.camera_select_button.grid(row=0, column=4, padx=10)

        self.fps_button = ctk.CTkOptionMenu(
            self.controls_frame, values=["30 FPS", "45 FPS", "60 FPS"], command=self.change_fps
        )
        self.fps_button.set("30 FPS")
        self.fps_button.grid(row=0, column=5, padx=10)

        # Video writer for recording
        self.video_writer = None

    def toggle_camera(self):
        if not self.is_running:
            self.start_camera()
            self.start_button.configure(text="Stop Camera")
        else:
            self.stop_camera()
            self.start_button.configure(text="Start Camera")

    def start_camera(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)
        self.is_running = True
        self.update_frame()

    def stop_camera(self):
        self.is_running = False
        self.stop_recording()
        if self.cap:
            self.cap.release()
        self.video_label.configure(image="")

    def change_aspect_ratio(self, ratio):
        width, height = self.aspect_ratios.get(ratio, (640, 480))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def zoom_in(self):
        if self.zoom_factor < 4.0:  # Set max zoom to 4x for better flexibility
            self.zoom_factor += 0.2

    def zoom_out(self):
        if self.zoom_factor > 1.0:
            self.zoom_factor -= 0.2

    def capture_image(self):
        if self.is_running:
            ret, frame = self.cap.read()
            if ret:
                filename = f"records/image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                cv2.imwrite(filename, frame)
                print(f"Image saved: {filename}")

    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
            self.record_button.configure(text="Stop Recording")
        else:
            self.stop_recording()
            self.record_button.configure(text="Start Recording")

    def start_recording(self):
        if self.is_running:
            width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            filename = f"records/video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            self.video_writer = cv2.VideoWriter(filename, fourcc, self.fps, (width, height))
            self.is_recording = True
            print(f"Recording started: {filename}")

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.video_writer.release()
            self.video_writer = None
            print("Recording stopped.")

    def update_frame(self):
        if self.is_running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Apply zoom effect
                h, w = frame.shape[:2]
                center_x, center_y = w // 2, h // 2
                radius_x, radius_y = int(w / (2 * self.zoom_factor)), int(h / (2 * self.zoom_factor))
                cropped_frame = frame[center_y - radius_y:center_y + radius_y, center_x - radius_x:center_x + radius_x]
                frame = cv2.resize(cropped_frame, (w, h))

                # Convert to Tkinter format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)

                # Write frame to video if recording
                if self.is_recording and self.video_writer:
                    self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

            self.parent.after(int(1000 / self.fps), self.update_frame)  # Adjust refresh rate based on FPS

    def change_camera_source(self, source):
        self.camera_index = 0 if source == "Integrated Camera" else 1
        if self.is_running:
            self.stop_camera()
            self.start_camera()

    def change_fps(self, fps_option):
        fps_map = {"30 FPS": 30, "45 FPS": 45, "60 FPS": 60}
        self.fps = fps_map.get(fps_option, 30)
        if self.is_running:
            self.cap.set(cv2.CAP_PROP_FPS, self.fps)

    def render(self):
        self.camera_frame.tkraise()

    def destroy(self):
        self.stop_camera()
