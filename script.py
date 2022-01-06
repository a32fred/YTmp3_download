import youtube_dl
def run():
    video_url = input("pfv coloque o link do seu video aqui:")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download Finalozado!!! {}".format(filename))

if __name__=='__main__':
    run()
