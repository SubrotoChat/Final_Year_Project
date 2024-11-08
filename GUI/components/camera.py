import cv2
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import os
import datetime

class Camera:
    def __init__(self, parent):
        self.parent = parent
        self.camera_frame = ctk.CTkFrame(self.parent)
        self.camera_frame.grid(row=0, column=0, sticky="nsew")

        self.video_label = tk.Label(self.camera_frame)
        self.video_label.pack(fill="both", expand=True)
        
        self.cap = None
        self.is_running = False
        self.is_recording = False
        self.zoom_level = 1
        self.aspect_ratio = (4, 3)

        # Camera control buttons container
        self.controls_frame = ctk.CTkFrame(self.camera_frame)
        self.controls_frame.pack(fill="x", pady=10)

        # Start/Stop button
        self.toggle_button = ctk.CTkButton(self.controls_frame, text="Open Camera", command=self.toggle_camera)
        self.toggle_button.grid(row=0, column=0, padx=5)

        # Aspect Ratio Button
        self.aspect_button = ctk.CTkButton(self.controls_frame, text="Aspect Ratio", command=self.change_aspect_ratio)
        self.aspect_button.grid(row=0, column=1, padx=5)

        # Zoom In Button
        self.zoom_in_button = ctk.CTkButton(self.controls_frame, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.grid(row=0, column=2, padx=5)

        # Zoom Out Button
        self.zoom_out_button = ctk.CTkButton(self.controls_frame, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.grid(row=0, column=3, padx=5)

        # Snapshot Button
        self.snapshot_button = ctk.CTkButton(self.controls_frame, text="Snapshot", command=self.take_snapshot)
        self.snapshot_button.grid(row=0, column=4, padx=5)

        # Record Button
        self.record_button = ctk.CTkButton(self.controls_frame, text="Record", command=self.toggle_recording)
        self.record_button.grid(row=0, column=5, padx=5)

        # Video writer for recording
        self.out = None

    def toggle_camera(self):
        if not self.is_running:
            self.start_camera()
            self.toggle_button.configure(text="Stop Camera")
        else:
            self.stop_camera()
            self.toggle_button.configure(text="Open Camera")

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.is_running = True
        self.update_frame()

    def stop_camera(self):
        self.is_running = False
        if self.cap:
            self.cap.release()
        if self.is_recording:
            self.toggle_recording()  # Stop recording if camera is stopped
        self.video_label.configure(image="")

    def update_frame(self):
        if self.is_running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = self.apply_zoom(frame)
                frame = self.apply_aspect_ratio(frame)
                
                if self.is_recording:
                    self.out.write(frame)
                
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
            self.parent.after(10, self.update_frame)  # Refresh every 10 ms

    def apply_zoom(self, frame):
        h, w = frame.shape[:2]
        zoom_factor = 1.0 / self.zoom_level
        ch, cw = int(h * zoom_factor), int(w * zoom_factor)
        start_y = (h - ch) // 2
        start_x = (w - cw) // 2
        return frame[start_y:start_y+ch, start_x:start_x+cw]

    def apply_aspect_ratio(self, frame):
        h, w = frame.shape[:2]
        target_ratio = self.aspect_ratio[0] / self.aspect_ratio[1]
        if w / h > target_ratio:
            new_w = int(h * target_ratio)
            start_x = (w - new_w) // 2
            return frame[:, start_x:start_x+new_w]
        else:
            new_h = int(w / target_ratio)
            start_y = (h - new_h) // 2
            return frame[start_y:start_y+new_h, :]

    def change_aspect_ratio(self):
        self.aspect_ratio = (16, 9) if self.aspect_ratio == (4, 3) else (4, 3)

    def zoom_in(self):
        if self.zoom_level < 3:  # Limit zoom level to avoid excessive cropping
            self.zoom_level += 0.5

    def zoom_out(self):
        if self.zoom_level > 1:
            self.zoom_level -= 0.5

    def take_snapshot(self):
        if self.cap and self.is_running:
            ret, frame = self.cap.read()
            if ret:
                filename = f"snapshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Snapshot saved as {filename}")

    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
            self.record_button.configure(text="Stop Recording")
        else:
            self.stop_recording()
            self.record_button.configure(text="Record")

    def start_recording(self):
        if self.cap and self.is_running:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            filename = f"recording_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
            frame_width = int(self.cap.get(3))
            frame_height = int(self.cap.get(4))
            self.out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height))
            self.is_recording = True
            print(f"Recording started: {filename}")

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            if self.out:
                self.out.release()
            print("Recording stopped")

    def render(self):
        self.camera_frame.tkraise()

    def destroy(self):
        self.stop_camera()
        if self.is_recording:
            self.stop_recording()
