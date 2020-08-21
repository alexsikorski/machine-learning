import os
import pickle


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
    # print(filtered_videos[0])


if __name__ == "__main__":
    main()
