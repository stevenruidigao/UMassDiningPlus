import youtube_dl as youtube_dl
import ffmpeg
import numpy as np


'''
All livestream links:
Worcester South - https://www.youtube.com/watch?v=89KPOnjHEC4
Worcester North - https://www.youtube.com/watch?v=7wHgOpwHz8k
Berkshire Entrance - https://www.youtube.com/watch?v=70PKbo5ouIM
Hampshire South - https://www.youtube.com/watch?v=RprORF_ggOA
Hampshire North - https://www.youtube.com/watch?v=TWC87AgKJHA

'''
diningStreams = ["https://www.youtube.com/watch?v=89KPOnjHEC4","https://www.youtube.com/watch?v=7wHgOpwHz8k","https://www.youtube.com/watch?v=70PKbo5ouIM","https://www.youtube.com/watch?v=RprORF_ggOA","https://www.youtube.com/watch?v=TWC87AgKJHA"]




def getYoutubeFrameAtTime(youtube_url, time=-1, ytdl_opts=None, save_image=False):
    if ytdl_opts is None:
        ytdl_opts = {
            "format": "bestvideo[height>2160]+bestaudio[acodec=opus]/(bestvideo[height=2160][fps>30]+251)/bestvideo[height=2160]+251/bestvideo[height=2160]+140/(bestvideo[height=1440][fps>30]+251)/bestvideo[height=1440]+251/bestvideo[height=1440]+140/(bestvideo[height=1080][fps>30]+251)/bestvideo[height=1080]+251/bestvideo[height=1080]+140/(bestvideo[height=720][fps>30]+251)/bestvideo+251/bestvideo+bestaudio/best",
        }

    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        youtube_info = ytdl.extract_info(youtube_url, download=False)

        # print("Youtube Info:", youtube_info)

        if "formats" in youtube_info.keys():
            formats = youtube_info["formats"]

        elif "requested_formats" in youtube_info.keys():
            formats = youtube_info["requested_formats"]

        else:
            # print("Youtube Info:", youtube_info)

            raise Exception("No formats found")

        video_url = formats[-2]["url"]
        audio_url = formats[-1]["url"]

        # print("URLs:", video_url, audio_url)

        frame = getFrameAtTime(video_url, time)
        
        if (save_image):
            import matplotlib.pyplot as plt
            plt.imsave(youtube_url.split("=")[-1] + ".png", frame)

        return frame

def getFrameAtTime(video, time=-1):
        video_info = ffmpeg.probe(video)

        # print("Video Info:", video_info)

        if time < 0:
            if "duration" in video_info["format"].keys():
                time = float(video_info["format"]["duration"]) + time

            elif "start_time" in video_info["format"].keys():
                time = 1 + time

            else:
                raise Exception("No time found")

        # print("Time:", time)

        stream, err = (ffmpeg
            .input(video, ss=time)
            .output("pipe:", vframes=1, format="rawvideo", pix_fmt="rgb24")
            .run_async(pipe_stdout=True, pipe_stderr=True)
        ).communicate()
        
        frame = np.asarray(bytearray(stream), dtype="uint8").reshape((video_info["streams"][-1]["height"], video_info["streams"][-1]["width"], 3))
        # print("Shape:", frame.shape)
    
        return frame

for vid in diningStreams:
    getYoutubeFrameAtTime(vid, save_image=True)


#if __name__ == '__main__':

'''nyan_cat = "https://www.youtube.com/watch?v=QH2-TGUlwu4"
video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
nasa = "https://www.youtube.com/watch?v=nA9UZF-SZoQ"
livestream = "https://www.youtube.com/watch?v=7wHgOpwHz8k"
getYoutubeFrameAtTime(nyan_cat, save_image=True, time=-100)
getYoutubeFrameAtTime(video, save_image=True, time=60)
getYoutubeFrameAtTime(nasa, save_image=True, time=-3600)
getYoutubeFrameAtTime(livestream, save_image=True, time=-14000)'''

