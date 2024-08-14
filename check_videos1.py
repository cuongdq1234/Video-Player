import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END) 
    text_area.insert("1.0", content) 

class CheckVideos:
    def __init__(self, window):
        self.window = window
        self.window.title("Check Videos")

        self.list_button = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        self.list_button.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(window, text="Enter Video Number:").grid(row=0, column=1, padx=10, pady=10)
        self.input_text = tk.Entry(window, width=3)
        self.input_text.grid(row=0, column=2, padx=10, pady=10)

        self.check_video_button = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        self.check_video_button.grid(row=0, column=3, padx=10, pady=10)

        self.list_text = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_text.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_text = tk.Text(window, width=24, height=4, wrap="none")
        self.video_text.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_label = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def check_video_clicked(self):
        key = self.input_text.get() 
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_text, video_details) 
        else:
            set_text(self.video_text, f"Video {key} not found") 
        self.status_label.configure(text="Check Video button was clicked!")

   
    def list_videos_clicked(self):
        video_list = lib.list_all() 
        set_text(self.list_text, video_list)  
        self.status_label.configure(text="List Videos button was clicked!")
        
