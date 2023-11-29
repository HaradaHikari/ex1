import zipfile
import json

 # 入力ファイル
InputZipFile = "kabeposter.zip"

# ファイルの読み込み
# zipファイル
with zipfile.ZipFile(InputZipFile, "r") as zip_file:
    InputFiles = zip_file.namelist()
    for InputFile in InputFiles:
        if InputFile.endswith("00_keypoints.json"):
            # jsonファイル
            with zip_file.open(InputFile, "r") as f:
                data = json.load(f)

   # 2人の鼻と首の座標を表示
for person_id, person_data in enumerate(data['people']):
    nose = person_data['pose_keypoints_2d'][:3]  # 鼻の座標
    neck = person_data['pose_keypoints_2d'][3:6]  # 首の座標

    print(f"{person_id + 1}人目")
    print("鼻 - X:", nose[0], "Y:", nose[1], "C:", nose[2])
    print("首 - X:", neck[0], "Y:", neck[1], "C:", neck[2])
    print()