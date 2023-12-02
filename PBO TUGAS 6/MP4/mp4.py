
import tkinter as tk
import cv2

class VideoPlayer:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack()

        self.btn_play = tk.Button(window, text="Play", width=10, command=self.play_video)
        self.btn_play.pack()

        self.btn_pause = tk.Button(window, text="Pause", width=10, command=self.pause_video)
        self.btn_pause.pack()

        self.btn_stop = tk.Button(window, text="Stop", width=10, command=self.stop_video)
        self.btn_stop.pack()

        self.play = True
        self.update()

    def play_video(self):
        self.play = True

    def pause_video(self):
        self.play = False

    def stop_video(self):
        self.vid.release()

    def update(self):
        if self.play:
            ret, frame = self.vid.read()
              
# File MP4 yang ingin diputar
video_source = "videocia.mp4"

# Membuat instance dari kelas VideoPlayer
root = tk.Tk()
app = VideoPlayer(root, "Video Player", video_source)
root.mainloop()
