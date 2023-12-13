import json
import zipfile
import tkinter as tk
from tkinter import Canvas

# JSONファイルからキーポイントを読み込む関数
def read_keypoints_from_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data['people']

# 肩の線を描画する関数
def draw_shoulder_line(canvas, person_data, color):
    # 肩の座標を取得
    shoulder = [
        int(person_data["pose_keypoints_2d"][6]), int(person_data["pose_keypoints_2d"][7]),
        int(person_data["pose_keypoints_2d"][3]), int(person_data["pose_keypoints_2d"][4]),
        int(person_data["pose_keypoints_2d"][15]), int(person_data["pose_keypoints_2d"][16])
    ]
    # 肩の線を描画
    canvas.create_line(shoulder[0], shoulder[1], shoulder[2], shoulder[3], fill=color, width=2)
    canvas.create_line(shoulder[2], shoulder[3], shoulder[4], shoulder[5], fill=color, width=2)

# ZIPファイルからデータを読み込んで描画する関数
def load_and_draw(zip_file_path, json_file_path, canvas):
    with zipfile.ZipFile(zip_file_path) as zip_f:
        with zip_f.open(json_file_path) as file:
            data = json.load(file)

    # 人物データを取得
    people_data = data["people"]
    # 1人目の肩の線を描画（赤）
    draw_shoulder_line(canvas, people_data[0], "red")
    # 2人目の肩の線を描画（青）
    draw_shoulder_line(canvas, people_data[1], "blue")

#ウィンドウの作成
root = tk.Tk()
root.title("Shoulder Lines")

# キャンバスの作成
canvas = Canvas(root, width=2000, height=1000)
canvas.pack()

load_and_draw('kabeposter.zip', 'kabeposter/kabeposter_000000000000_keypoints.json', canvas)

# ウィンドウの表示
root.mainloop()