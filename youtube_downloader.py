import pytube

def download_video(url, resolution=None):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    if resolution is None:
        for index, stream in enumerate(video.streams):
            print(f"{index} - Tag: {stream.itag}, Type: {stream.type}, MIME-Type: {stream.mime_type}, Res: {stream.resolution}")

        index = input("Choice an Index to download: ")
        stream = video.streams[int(index)]
    else:
        stream = video.streams.get_by_itag(itag)
    
    if stream:
        stream.download()
        return stream.default_filename
    else:
        print(f"can't found specified stream in {url}")
        print(f"streams: {video.streams}")
        return ""

def download_videos(urls, resolution):
    for url in urls:
        print(f"downloading {url} with resolution: {resolution}")
        download_video(url, resolution)

def download_playlist(url):
    quality = input("Please choose a quality (low, medium, high, very high):")
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, quality)

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)

    links.pop()

    return links