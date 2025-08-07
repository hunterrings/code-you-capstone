import pandas as pd
import glob
import os
joined_files = os.path.join("C:/Users/Code/projects/capstone/youtube-trending-videos-updated-daily\music", "music_2024*.csv")
joined_list = glob.glob(joined_files)
ydf = pd.concat(map(lambda f: pd.read_csv(f, encoding='Mac_Roman'), joined_list), ignore_index=True)
print(ydf.shape)
print(ydf.columns)
print(ydf.dtypes)
print(ydf.describe(include='all'))
print(ydf.head)

print(ydf[['title', 'channelName', 'publishedDate', 'views', 'duration']].head(25))