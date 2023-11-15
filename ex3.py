import zipfile

# 入力ファイル
InputZipFile = "sample.zip"

# 変数の初期化
a = 0 
total = 0 

# zipファイルの読み込み
with zipfile.ZipFile(InputZipFile, "r") as zip_file:
    # zipファイル内のファイルの配列
    InputFiles = zip_file.namelist()
    for InputFile in InputFiles:

        # 「_kgu.txt」をファイル名の最後に持つファイル
        if InputFile.endswith("_kgu.txt"):

            # txtファイルの読み込み
            with zip_file.open(InputFile, "r") as f:

                # ファイル内の数値
                number = f.read()

                # 奇数のもののみのファイル内の数値の和を計算
                if a % 2 == 1:
                    total += int(number)
                a += 1
print(total)
