import tkinter as tk

# ウィンドウを作成
root = tk.Tk()
root.title("Moving Stick Figure")

def draw_stick_figure(canvas, x):
    # 頭
    canvas.create_oval(50 + x, 50, 100 + x, 100, outline="black", width=2)

    # 胴体
    canvas.create_line(75 + x, 100, 75 + x, 170, fill="black", width=2)

    # 左腕
    canvas.create_line(75 + x, 140, 25 + x, 100, fill="black", width=2)

    # 右腕
    canvas.create_line(75 + x, 140, 125 + x, 100, fill="black", width=2)

    # 左脚
    canvas.create_line(75 + x, 170, 50 + x, 230, fill="black", width=2)

    # 右脚
    canvas.create_line(75 + x, 170, 100 + x, 230, fill="black", width=2)

def move_stick_figure():
    global x_position
    canvas.delete("all")  # 既存の図形を削除
    draw_stick_figure(canvas, x_position)
    x_position += 5  # 移動量を設定
    root.after(50, move_stick_figure) 


# Canvasを作成してウィンドウに配置
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# 初期位置
x_position = 0

# アニメーションを開始
move_stick_figure()

# イベントループを開始
root.mainloop()