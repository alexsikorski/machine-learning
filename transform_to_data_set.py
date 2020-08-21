import os
import pickle
import pandas as pd
import re


def dur_to_sec(duration):
    ISO_8601 = re.compile(
        'P'
        '(?:(?P<years>\d+)Y)?'
        '(?:(?P<months>\d+)M)?'
        '(?:(?P<weeks>\d+)W)?'
        '(?:(?P<days>\d+)D)?'
        '(?:T'
        '(?:(?P<hours>\d+)H)?'
        '(?:(?P<minutes>\d+)M)?'
        '(?:(?P<seconds>\d+)S)?'
        ')?')
    units = list(ISO_8601.match(duration).groups()[-3:])
    units = list(reversed([int(x) if x != None else 0 for x in units]))
    return sum([x * 60 ** units.index(x) for x in units])


def load_pkl(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


def main():
    pkl_count = 0
    videos = []

    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".pkl"):
                print("Opening", subdir, "file...", file)
                pkl_count += 1
                videos += load_pkl(subdir + "/" + file)

    seen = set()
    filtered_videos = []
    for video in videos:
        for (k, v) in video.items():
            if k == "title":
                # if it already exists, update
                if v in seen:
                    for filtered_video in filtered_videos:
                        for (f_k, f_v) in filtered_video.items():
                            if f_k == "title":
                                if f_v == v:
                                    filtered_videos.remove(filtered_video)
                                    filtered_videos.append(video)

                # if doesnt, add entry
                if v not in seen:
                    seen.add(v)
                    filtered_videos.append(video)

    print("---------------------------------------------")
    print("Number of unique videos:", len(filtered_videos))

    pandas_dict = {'id': [], 'publishedAt': [], 'title': [], 'description': [], 'channelId': [], 'tags': [],
                   'views': [], 'comments': [], 'duration': [], 'dimension': [], 'definition': [],
                   'licensedContent': [], 'projection': [], 'likes': [], 'dislikes': []}

    for video in filtered_videos:
        for (key_original, v_original) in video.items():
            for (k, v) in pandas_dict.items():
                if key_original == 'id':
                    if k == 'id':
                        v.append(v_original)
                elif key_original == 'publishedAt':
                    if k == 'publishedAt':
                        v.append(v_original)
                elif key_original == 'title':
                    if k == 'title':
                        v.append(v_original)
                elif key_original == 'description':
                    if k == 'description':
                        v.append(v_original)
                elif key_original == 'channelId':
                    if k == 'channelId':
                        v.append(v_original)
                elif key_original == 'tags':
                    if k == 'tags':
                        v.append(v_original)
                elif key_original == 'views':
                    if k == 'views':
                        v.append(v_original)
                elif key_original == 'comments':
                    if k == 'comments':
                        v.append(v_original)
                elif key_original == 'duration':
                    if k == 'duration':
                        # transform duration into seconds
                        seconds = dur_to_sec(v_original)
                        v.append(seconds)
                elif key_original == 'dimension':
                    if k == 'dimension':
                        v.append(v_original)
                elif key_original == 'definition':
                    if k == 'definition':
                        v.append(v_original)
                elif key_original == 'licensedContent':
                    if k == 'licensedContent':
                        v.append(v_original)
                elif key_original == 'projection':
                    if k == 'projection':
                        v.append(v_original)
                elif key_original == 'likes':
                    if k == 'likes':
                        v.append(v_original)
                elif key_original == 'dislikes':
                    if k == 'dislikes':
                        v.append(v_original)

    df = pd.DataFrame.from_dict(pandas_dict)
    df.to_csv("top-youtube-videos.csv", index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
