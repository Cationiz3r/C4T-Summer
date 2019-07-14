from youtube_dl import YoutubeDL
import os
import json
from pygame import mixer
import msvcrt as m

# options = {
#     'default_search': 'ytsearch5',
#     # 'outtmpl': '%(id)s', # lấy tên file đown về là id của video
#         'postprocessors': [{
#         'key': 'FFmpegExtractAudio', # Tách lấy audio
#         'preferredcodec': 'mp3', # Format ưu tiên là mp3
#         'preferredquality': '192', # Chất lượng bitrate
#     }]
# }

options = {
    'outtmpl': '%(title)s.%(ext)s',
    'default_search': 'ytsearch5',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

yDL = YoutubeDL(options)
clear = lambda: os.system("cls")

# Global Setting (Unchangable 4 now)
allow_song_fadeout = False
fade_duration = 3000

while True:
    clear()

    print()
    print("  1] Show ALL songs")
    print("  2] Show details of a song")
    print("  3] Play a song")
    print("  4] Search and Download a song")
    print("  5] Exit")

    inp = int(input("\n  Enter: "))

    url = "https://www.youtube.com/watch?v=r_XIEmrZKvU"

    if (inp == 1):
        clear()
        print()

        reader = open("song_list.txt", "rb")
        for idx, val in enumerate(reader):
            # print(" ", idx + 1, end = "] ")
            print(" ", val.decode("utf-8").replace("\n", ""))

        print()
        input()

        reader.close()

    elif (inp == 2):
        clear()
        print()

        music_list = []

        print("  0] Exit")
        reader = open("song_list.txt", "rb")
        for idx, val in enumerate(reader):
            print(" ", idx + 1, end = "] ")
            song_name = val.decode("utf-8").replace("\n", "")
            print(song_name)
            music_list.append(song_name)
        
        inp = int(input("\n Enter: "))

        if (inp == 0):
            continue

        with open(music_list[inp - 1] + ".json") as json_file:
            clear()

            detail = json.load(json_file)
            print("\n  Title:", detail["title"])
            print("    Uploader:", detail["uploader"])
            print("    Duration: ", end = "")
            if (detail["duration"] < 60):
                print(detail["duration"], "seconds")
            else:
                print("About", (detail["duration"] + 30) // 60, "minutes")
            print("    URL: http://www.youtube.com/watch?v=" + detail["id"])
            print()

            reader.close()
            json_file.close()

            input()

    elif (inp == 3):
        clear()
        print()

        music_list = []

        print("  0] Exit")
        reader = open("song_list.txt", "rb")
        for idx, val in enumerate(reader):
            print(" ", idx + 1, end = "] ")
            song_name = val.decode("utf-8").replace("\n", "")
            print(song_name)
            music_list.append(song_name)
        
        inp = int(input("\n Enter: "))

        if (inp == 0):
            continue

        playing = True

        mixer.init()
        player = mixer.music
        player.load(music_list[inp - 1] + ".mp3")
        player.play()

        while True:
            clear()

            print("\n  Current:", music_list[inp - 1])
            if (playing):
                print("    Playing song..")
            else:
                print("    Song stopped")

            print("\n [P] Play / Pause   [S] Stop\n")
            key = str(m.getch())[2].upper()

            if (key == "P"):
                if (playing):
                    player.pause()
                    playing = False
                else:
                    player.unpause()
                    playing = True
            elif (key == "S"):
                if (allow_song_fadeout):
                    player.fadeout(fade_duration)
                else:
                    player.stop()
                break


    elif (inp == 4):
        clear()
        search = input("\n  Search: ")
        clear()
        searchRes = yDL.extract_info(search, False)

        clear()

        print("  0] Exit")
        print()
        for i in range(5):
            print(" ",i + 1, end = "] ")
            print(searchRes["entries"][i]["title"])

        inp = int(input("\n  Enter: "))
        clear()

        if (inp == 0):
            continue

        yDL.download(["http://www.youtube.com/watch?v=" + searchRes["entries"][inp - 1]["id"]])

        with open("song_list.txt", "ab") as out:
            out.write(searchRes["entries"][inp - 1]["title"].encode("utf-8") + b"\n") # Add Song
        with open(searchRes["entries"][inp - 1]["title"] + ".json", "w") as out: # Store Data
            json.dump(searchRes["entries"][inp - 1], out)

    elif (inp == 5):
        clear()
        break
            
    
