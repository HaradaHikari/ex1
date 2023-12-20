import zipfile
import json
import tkinter as tk

# 入力ZIPファイル
InputZipFile = "kabeposter.zip"

# Tkinterウィンドウの設定
root = tk.Tk()
root.geometry("1200x800")

# キャンバスの設定
canvas = tk.Canvas(root, width=1200, height=800, bg="white")
canvas.place(x=0, y=0)


# JSONデータを格納するリスト
datas = []

# ZIPファイルを開いてJSONデータを読み込む
with zipfile.ZipFile(InputZipFile, "r") as zip_file:

    # "_keypoints.json" で終わるファイルを抽出
    InputFiles = [f for f in zip_file.namelist() if f.endswith("_keypoints.json")]

    # 各JSONファイルを読み込んでデータをリストに格納
    for InputFile in InputFiles:
        with zip_file.open(InputFile, "r") as f:
            data = json.load(f)
            datas.append(data)

# ラインのリスト
lines = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7),
         (1, 8), (8, 9), (8, 12), (9, 10), (10, 11), (11, 23), (11, 24), (22, 23),
         (12, 13), (13, 14), (14, 21), (14, 19), (19, 20), (0, 15), (0, 16), (15, 17), (16, 18)]

# フレームごとに描画を行う関数
def draw(frame):
    if frame >= len(datas):
        return

    # キャンバスをクリア
    canvas.delete("all")

    for i in range(2):
        keypoints = datas[frame]["people"][i]["pose_keypoints_2d"]

        # 各関節の位置を描画
        for j in range(0, len(keypoints), 3):
            x = keypoints[j] * 1/2
            y = keypoints[j + 1] * 1/2
            if x != 0 and y != 0:
                canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black", width=0, tag="all")

        # 各関節を結ぶラインを描画
        for line in lines:
            x1, y1 = keypoints[line[0] * 3] * 1/2, keypoints[line[0] * 3 + 1] * 1/2
            x2, y2 = keypoints[line[1] * 3] * 1/2, keypoints[line[1] * 3 + 1] * 1/2
            if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
                canvas.create_line(x1, y1, x2, y2, tag="all")

    # 次のフレームを描画するために再帰呼び出し
    root.after(50, draw, frame + 1)

draw(0)
root.mainloop()