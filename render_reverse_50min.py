import subprocess
import os

folder = "/Users/abc/Documents/KenhYTB/nhacthien_long/phan1_musicful_done"
out_dir = "/Users/abc/Documents/KenhYTB/nhacthien_long"

# Reverse order: Bai 6 -> Bai 5 -> Bai 4 -> Bai 3 -> Bai 2 -> Bai 1
files = [
    os.path.join(folder, "Bai6 _Binhyen tutai.mp4"),
    os.path.join(folder, "Bai5_Muademthanlocnangluongtieucuc.mp4"),
    os.path.join(folder, "bai4_Thiendinhanduongtaman.mp4"),
    os.path.join(folder, "bai3_tinhlangtritue.mp4"),
    os.path.join(folder, "Bai2_muaroitinhlang.mp4"),
    os.path.join(folder, "bai1_deepsleep.mp4")
]

concat_list = os.path.join(out_dir, "concat_reverse_list.txt")
with open(concat_list, "w") as f:
    for item in files:
        f.write(f"file '{item}'\n")

out_video = os.path.join(out_dir, "Video_Nhac_Thien_Dao_Nguoc_50Phut_Chuan.mp4")
print("Rendering concat to:", out_video)

cmd = [
    "/usr/local/bin/ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    out_video
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print(f"✅ RENDER THÀNH CÔNG! Dung lượng: {os.path.getsize(out_video)} bytes")
else:
    print("❌ Lỗi:", res.stderr)
