import tkinter as tk
import video_library as lib

class UpdateVideos:
    def __init__(self, window):
        self.window = window
        self.window.title("Update Videos")
        
        tk.Label(window, text="Enter Video Number:").grid(row=0, column=0, padx=10, pady=10)
        self.video_entry = tk.Entry(window)
        self.video_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(window, text="Enter New Rating:").grid(row=1, column=0, padx=10, pady=10)
        self.rating_entry = tk.Entry(window)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(window, text="Enter New Play Count:").grid(row=2, column=0, padx=10, pady=10)
        self.play_count_entry = tk.Entry(window)
        self.play_count_entry.grid(row=2, column=1, padx=10, pady=10)
        
        update_button = tk.Button(window, text="Update Video", command=self.update_video)
        update_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.status_label = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def update_video(self):
        video_number = self.video_entry.get()
        new_rating = self.rating_entry.get()
        add_play_count = self.play_count_entry.get()
        
        if new_rating.isdigit():
            lib.set_rating(video_number, int(new_rating))
        
        if add_play_count.isdigit():
            for _ in range(int(add_play_count)):
                lib.increment_play_count(video_number)
        
        if lib.get_name(video_number) is not None:
            self.status_label.config(text=f"Video {video_number} updated.")
        else:
            self.status_label.config(text=f"Video {video_number} not found.")
