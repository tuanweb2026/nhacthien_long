import subprocess
import os

work_dir = "/Users/abc/Documents/KenhYTB/nhacthien_long"
src_dir = os.path.join(work_dir, "phan1_musicful_done")

f1 = os.path.join(src_dir, "bai1deepsleep.mp4")
f2 = os.path.join(src_dir, "Bai2_muaroitinhlang.mp4")
f3 = os.path.join(src_dir, "bai3_tinhlangtritue.mp4")

# We want roughly ~50 minutes of continuous relaxing meditation
# Sequence: Bai 1 (8m47s) -> Bai 2 (8m29s) -> Bai 3 (7m45s) -> Bai 1 -> Bai 2 -> Bai 3 = ~50m05s
concat_list = os.path.join(work_dir, "concat_list.txt")
with open(concat_list, "w") as f:
    for item in [f1, f2, f3, f1, f2, f3]:
        f.write(f"file '{item}'\n")

output_mp4 = os.path.join(work_dir, "Video_Hoan_Chinh_Nhac_Thien_50Phut.mp4")
print("Rendering concat to:", output_mp4)

cmd = [
    "/usr/local/bin/ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    output_mp4
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
if res.returncode == 0:
    print("Success! Output file size:", os.path.getsize(output_mp4))
else:
    print("Error:", res.stderr)
