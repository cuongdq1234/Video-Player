import tkinter as tk
from check_videos1 import CheckVideos
from create_video_list import CreateVideoList
from update_video import UpdateVideos

def create_check_videos_window():
    check_video_window = tk.Toplevel(window)  
    CheckVideos(check_video_window)  

def create_video_list_window():
    video_list_window = tk.Toplevel(window)  
    CreateVideoList(video_list_window)  

def create_update_videos_window():
    update_video_window = tk.Toplevel(window) 
    UpdateVideos(update_video_window)  

window = tk.Tk()
window.geometry("520x200")
window.title("Video Player")

header_label = tk.Label(window, text="Click one of the buttons below")
header_label.pack(padx=10, pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

check_videos_button = tk.Button(button_frame, text="Check Videos", command=create_check_videos_window)
check_videos_button.grid(row=0, column=0, padx=10)

create_video_list_button = tk.Button(button_frame, text="Create Video List", command=create_video_list_window)
create_video_list_button.grid(row=0, column=1, padx=10)

update_videos_button = tk.Button(button_frame, text="Update Videos", command=create_update_videos_window)
update_videos_button.grid(row=0, column=2, padx=10)

status_label = tk.Label(window, text="", font=("Helvetica", 10))
status_label.pack(padx=10, pady=10)

window.mainloop()
