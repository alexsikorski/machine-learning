import os
import pickle
import pandas as pd


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
    print(filtered_videos[0])

    pandas_dict = {'title': [], 'tags': [],
                   'views': [], 'likes': [], 'dislikes': []}

    for video in filtered_videos:
        for (key_original, v_original) in video.items():
            for (k, v) in pandas_dict.items():
                if key_original == 'title':
                    if k == 'title':
                        v.append(v_original)
                elif key_original == 'tags':
                    if k == 'tags':
                        v.append(v_original)
                elif key_original == 'views':
                    if k == 'views':
                        v.append(v_original)
                elif key_original == 'likes':
                    if k == 'likes':
                        v.append(v_original)
                elif key_original == 'dislikes':
                    if k == 'dislikes':
                        v.append(v_original)
    print(pandas_dict)


    df = pd.DataFrame.from_dict(pandas_dict)
    df.to_csv("top-youtube-videos.csv", encoding='utf-8')


if __name__ == "__main__":
    main()
