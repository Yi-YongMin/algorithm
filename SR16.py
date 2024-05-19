import tkinter as tk
from PIL import Image, ImageTk


class FixedSizeCropper:
    def __init__(self, master, path):
        self.master = master
        self.path = path
        self.image = Image.open(self.path)
        self.render = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(
            master, width=self.render.width(), height=self.render.height()
        )
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.render)

        # 마우스 이벤트 바인딩
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # 클릭한 위치를 중심으로 32x32 크기의 이미지를 잘라냄
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        left = max(x - 12, 0)
        top = max(y - 12, 0)
        right = left + 24
        bottom = top + 24

        # 경계 조정 (이미지 경계 넘어가는 것 방지)
        if right > self.image.width:
            right = self.image.width
            left = right - 24
        if bottom > self.image.height:
            bottom = self.image.height
            top = bottom - 24

        cropped = self.image.crop((left, top, right, bottom))
        cropped.save("cropped_24x24.png")  # 저장 파일 이름
        cropped.show()  # 잘라낸 이미지 표시


def main():
    root = tk.Tk()
    app = FixedSizeCropper(root, "C:\\Set5\\baby.png")  # 이미지 파일 경로
    root.mainloop()


if __name__ == "__main__":
    main()
