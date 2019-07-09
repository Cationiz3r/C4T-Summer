from youtube_dl import YoutubeDL
import os
import json

options = {
    'default_search': 'ytsearch5',
    # 'outtmpl': '%(id)s', # lấy tên file đown về là id của video
        'postprocessors': [{
        'key': 'FFmpegExtractAudio', # Tách lấy audio
        'preferredcodec': 'mp3', # Format ưu tiên là mp3
        'preferredquality': '192', # Chất lượng bitrate
    }]
}

yDL = YoutubeDL(options)

while True:
    clear = lambda: os.system("cls")
    clear()

    print()
    print("  1] Show ALL songs")
    print("  2] Show details of a song")
    print("  3] Play a song")
    print("  4] Search and Download a song")
    print("  5] Exit")

    inp = int(input("\n  Enter: "))

    url = "https://www.youtube.com/watch?v=r_XIEmrZKvU"

    if (inp == 4):
        search = input("\n  Search: ")
        searchRes = yDL.extract_info(search, False)

        clear()

        print()
        for i in range(5):
            print(" ",i + 1, end = "] ")
            print(searchRes["entries"][i]["title"])

        inp = int(input("\n  Enter: "))

        yDL.download(["http://www.youtube.com/watch?v=" + searchRes["entries"][inp - 1]["id"]])
    
