import tkinter as tk 

# ウィンドウを作成
root = tk.Tk()
root.title("Stick Figure")

def draw_stick_figure(canvas):
    # 頭
    canvas.create_oval(50, 50, 100, 100, outline="black", width=2)

    # 胴体
    canvas.create_line(75, 100, 75, 170, fill="black", width=2)

    # 左腕
    canvas.create_line(75, 140, 25, 100, fill="black", width=2)

    # 右腕
    canvas.create_line(75, 140, 125, 100, fill="black", width=2)

    # 左脚
    canvas.create_line(75, 170, 50, 230, fill="black", width=2)

    # 右脚
    canvas.create_line(75, 170, 100, 230, fill="black", width=2)


# Canvasを作成してウィンドウに配置
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# 棒人間を描画
draw_stick_figure(canvas)

# ウィンドウの表示
root.mainloop()