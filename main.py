from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=h_GGd7HfKQ8')
videos = list(
    filter(
        lambda x: getattr(x, "mime_type", None) == "video/mp4"
        and getattr(x, "resolution", None) and not getattr(x, "is_progressive", True), yt.streams)
)

print(yt.title)
for i, video in enumerate(videos):
    resolution = getattr(video, "resolution")
    print(f"{i + 1}: {resolution}")

choice = int(input("Enter resolution: "))
index = choice - 1
if index not in range(len(videos)):
    print("Error")
else:
    videos[index].download()
