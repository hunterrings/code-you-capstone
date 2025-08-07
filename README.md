DATASETS:
    Most Streamed Spotify Songs 2024
        URL: https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024
    
    YouTube Trending Videos (Updated Daily)
        URL: https://www.kaggle.com/datasets/pyuser11/youtube-trending-videos-updated-daily/data

DATA DICTIONARY:
    Most Streamed Spotify Songs 2024
        Track Name: Name of the song.
        Album Name: Name of the album the song belongs to.
        Artist: Name of the artist(s) of the song.
        Release Date: Date when the song was released.
        ISRC: International Standard Recording Code for the song.
        All Time Rank: Ranking of the song based on its all-time popularity.
        Track Score: Score assigned to the track based on various factors.
        Spotify Streams: Total number of streams on Spotify.
        Spotify Playlist Count: Number of Spotify playlists the song is included in.
        Spotify Playlist Reach: Reach of the song across Spotify playlists.
        Spotify Popularity: Popularity score of the song on Spotify.
        YouTube Views: Total views of the song's official video on YouTube.
        YouTube Likes: Total likes on the song's official video on YouTube.
        TikTok Posts: Number of TikTok posts featuring the song.
        TikTok Likes: Total likes on TikTok posts featuring the song.
        TikTok Views: Total views on TikTok posts featuring the song.
        YouTube Playlist Reach: Reach of the song across YouTube playlists.
        Apple Music Playlist Count: Number of Apple Music playlists the song is included in.
        AirPlay Spins: Number of times the song has been played on radio stations.
        SiriusXM Spins: Number of times the song has been played on SiriusXM.
        Deezer Playlist Count: Number of Deezer playlists the song is included in.
        Deezer Playlist Reach: Reach of the song across Deezer playlists.
        Amazon Playlist Count: Number of Amazon Music playlists the song is included in.
        Pandora Streams: Total number of streams on Pandora.
        Pandora Track Stations: Number of Pandora stations featuring the song.
         Streams: Total number of streams on Soundcloud.
        Shazam Counts: Total number of times the song has been Shazamed.
        TIDAL Popularity: Popularity score of the song on TIDAL.
        Explicit Track: Indicates whether the song contains explicit content.
   
    YouTube Trending Videos (Updated Daily)
        title: The title of the video.
        description: The video's description.
        publishedDate: The date and time when the video was published (in a machine-readable format).
        publishedText: The date and time when the video was published (in a human-readable format).
        videoId: The unique igit dentifier for the video.
        videoUrl: The URL of the video.
        channelName: The name of the channel that published the video.
        channelId: The unique identifier for the channel.
        channelUrl: The URL of the channel.
        thumbnails: URLs for the video's thumbnail images in different resolutions.
        views: The number of views the video has received.
        viewsText: The number of views in a human-readable format (e.g., "1.2M views").
        duration: The duration of the video (in a machine-readable format).
        durationText: The duration of the video in a human-readable format (e.g., "3:24").
        verified: A boolean indicating whether the channel is verified or not.
        creatorOnRise: A boolean indicating whether the channel is marked as a "Creator on the Rise" by YouTube.
        isShort: A boolean indicating whether the video is a YouTube Shorts video or not.

PROJECT SETUP:
# Step-by-step directions on how to download, install, and run your project
# Instructions for setting up the virtual environment
# You should test this process by cloning your repo into a new folder or onto a different machine
# Have others test your project and test theirs. 

Welcome to my capstone project. 

Here are the steps for setting everying up and running a demonstration. 

1. Create a new virtual environment in Python by using the 'venv' command. Ensure that the correct Python interpreter is specified on your PATH. 

2. Download the two datasets linked above. I did this by using the Kaggle CLI tool. This requires that you install the Kaggle Python package ('pip install kaggle'). You will also need to download an authentication key from their website. The Kaggle website has additional information about where the kaggle.json file shoudl be located depending on your machine. These downloads are zipped and will need to be extracted.


PROJECT OVERVIEW:
# A description of what the user should expect from the project once it's running
# Assume the reviewer has no coding background, so keep language clear and simple

TECHNOLOGIES USED:
# List all key tools/libraries used and explain their role in the project
#   Example: “Pandas was used to clean and manipulate the dataset to identify trends in customer behavior.”
#   Example: “The project was developed in Jupyter Notebooks to allow for clean, narrative-driven presentation of both code and results.”
    Python
        matplotlib
    pandas
    Jupyter
    Kaggle - Pulic API

