#take a long form video, clip 1 minute segments, and save them to a folder
#https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames


import cv2
import os

#video path
video_path = '/Users/akshatchavan/Desktop/AutoClipper/video.mp4'
cap = cv2.VideoCapture(video_path)

#make sure that video is opened properly
if cap.isOpened() == False:
    print('Error opening video file')

#get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

#define length of clip in seconds
clip_duration = 60 

#frames per clip
frames_per_clip = int(clip_duration*fps)

#create a folder to save clips
output_folder = 'clips'
if not os.path.exists(output_folder):
    os.makedirs(output_folder, exist_ok=True)

#init frames and clip count
curr_frame = 0
clip_num = 0

#process and save videos
while curr_frame < frame_count:
    # Set video position
    cap.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
    
    # Initialize video writer
    clip_path = os.path.join(output_folder, f'clip_{clip_num}.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(clip_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
    
    for _ in range(frames_per_clip):
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    
    out.release()
    curr_frame += frames_per_clip
    clip_num += 1


# Release the video capture
cap.release()
print("Clipping completed.")



