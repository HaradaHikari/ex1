file_name = "data.txt"

total = 0

# ファイルを開いて内容を読み込み
with open(file_name, "r") as file:
    for line in file:
        try:
            # 行を整数に変換し、和に加える
            total += int(line)
        except ValueError:
            # 整数に変換できない行は無視
            pass

# 和を出力
print("整数の和:", total)