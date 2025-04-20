import io
from PIL import Image, ImageSequence
from rembg import remove
import imageio
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# tkinter 창 숨기기
Tk().withdraw()

# 파일 선택 창 띄우기
file_path = askopenfilename(
    filetypes=[("GIF files", "*.gif")],
    title="배경을 제거할 GIF를 선택하세요"
)


# GIF 열기
gif = Image.open('input.gif')
frames = []

# 프레임별 배경 제거
for frame in ImageSequence.Iterator(gif):
    rgba = frame.convert("RGBA")
    result = remove(rgba)  # 여기서 Image 객체 반환됨
    frames.append(result)  # 바로 추가하면 됨!

# GIF로 저장
frames[0].save(
    "result/output.gif",
    save_all=True,
    append_images=frames[1:],
    loop=0,
    duration=gif.info.get('duration', 100),
    disposal=2  # 프레임 덮어쓰기 방지용 (투명 처리 시 필요)
)
