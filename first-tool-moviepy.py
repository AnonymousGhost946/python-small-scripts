from moviepy.editor import VideoFileClip

# Get user input for the video file path and crop points
userInput = input("Enter the path of the video file: ")
cropStart = int(input("Enter the start point (in seconds) to crop video: "))
cropEnd = int(input("Enter the end point (in seconds) to end video: "))

# Load the video file and create a subclip
clip = VideoFileClip(userInput).subclip(cropStart, cropEnd)

# Save the new clip
clip.write_videofile("short_video.mp4")



#path of video 
# /home/kali/Desktop/python-scripting/python-project/video.mp4