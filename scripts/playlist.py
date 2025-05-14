from pytube import Playlist

def find_youtube_links_and_titles_from_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        youtube_links_and_titles = [(video.title, video.watch_url) for video in playlist.videos]
        return youtube_links_and_titles
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    links_and_titles = find_youtube_links_and_titles_from_playlist(playlist_url)
    if links_and_titles:
        print("Found YouTube links and titles:")
        with open("playlist_links_and_titles.txt", "w", encoding="utf-8") as file:
            for title, link in links_and_titles:
                print(f"{title}, {link}")
                file.write(f"{title}, {link}\n")
    else:
        print("No YouTube links found or an error occurred.")

