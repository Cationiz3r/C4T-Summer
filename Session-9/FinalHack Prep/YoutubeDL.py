from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}

print()
link = input("  Enter URL: ")
print()

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

