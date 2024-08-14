import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib

class CreateVideoList:
    def __init__(self, window):
        self.window = window
        self.window.title("Create Video List")
        
        self.playlist = []
        
        tk.Label(window, text="Enter Video Number:").grid(row=0, column=0, padx=10, pady=10)
        self.video_entry = tk.Entry(window)
        self.video_entry.grid(row=0, column=1, padx=10, pady=10)
        
        add_button = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist)
        add_button.grid(row=0, column=2, padx=10, pady=10)
        
        play_button = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        play_button.grid(row=1, column=0, padx=10, pady=10)
        
        reset_button = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.playlist_text = tkst.ScrolledText(window, width=40, height=10)
        self.playlist_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        self.status_label = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def add_to_playlist(self):
        video_number = self.video_entry.get()
        name = lib.get_name(video_number)
        if name:
            self.playlist.append(video_number)
            self.update_playlist_display()
            self.status_label.config(text=f"Added {name} to playlist.")
        else:
            self.status_label.config(text=f"Video {video_number} not found.")
    
    def update_playlist_display(self):
        self.playlist_text.delete("1.0", tk.END)
        for video_number in self.playlist:
            name = lib.get_name(video_number)
            self.playlist_text.insert(tk.END, f"{video_number}: {name}\n")
    
    def play_playlist(self):
        for video_number in self.playlist:
            lib.increment_play_count(video_number)
        self.status_label.config(text="Playlist played!")
    
    def reset_playlist(self):
        self.playlist = []
        self.update_playlist_display()
        self.status_label.config(text="Playlist reset.")
