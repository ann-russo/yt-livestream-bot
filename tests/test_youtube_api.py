from youtube_notifier.youtube_api import check_live_stream

if __name__ == "__main__":
    streams = check_live_stream()
    if streams:
        print(f"Live stream detected: {streams[0]['snippet']['title']}")
    else:
        print("No live streams found.")
