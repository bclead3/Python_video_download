# Documentation
# https://python-pytube.readthedocs.io/en/latest/index.html
# Another website
# https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/


# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "Downloads"  # to_do

# link of the video to be downloaded
# link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
#link = "https://www.youtube.com/watch?v=prIElcJOrOM"

links = [
         'https://www.youtube.com/watch?v=2K7TU1Hh_3U'
         ]
for link in links:
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(link)
    except:
        print("Connection Error")  # to handle exception

    # filters out all the files with "mp4" extension
    # mp4files = yt.filter('mp4')

    # to set the name of the file
    # yt.set_filename('CompleteGuideToStarship-Falcon9vsStarship')

    # get the video with the extension and
    # resolution passed in the get() function
    d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    try:
        # downloading the video
        d_video.download(SAVE_PATH)
    except:
        print("Some Error!")

print('Task Completed!')
