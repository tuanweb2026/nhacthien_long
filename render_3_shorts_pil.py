import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

src_video = "/Users/abc/Documents/KenhYTB/nhacthien_long/Video_Hoan_Chinh_Nhac_Thien_50Phut.mp4"
out_dir = "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo"
font_path = "/Library/Fonts/Arial Unicode.ttf"

segments = [
    {
        "name": "Short_01_Nghe_Khi_Mat_Ngu.mp4",
        "start": "00:00:45",
        "duration": "20",
        "line1": "MẤT NGỦ, TÂM BẤT AN?",
        "line2": "HÃY THỞ SÂU VÀ LẮNG NGHE...",
        "cta": "BẤM VIDEO LIÊN QUAN ĐỂ NGHE TRỌN 50 PHÚT ⬇️"
    },
    {
        "name": "Short_02_Tieng_Mua_Ranh_Roi_Tam_Tri.mp4",
        "start": "00:09:15",
        "duration": "20",
        "line1": "MỆT MỎI THÌ BUÔNG XẢ",
        "line2": "TIẾNG MƯA XOA DỊU TÂM HỒN",
        "cta": "BẤM VIDEO LIÊN QUAN ĐỂ NGHE TRỌN 50 PHÚT ⬇️"
    },
    {
        "name": "Short_03_Chuong_Chua_Tinh_Tam.mp4",
        "start": "00:17:45",
        "duration": "20",
        "line1": "TIẾNG CHUÔNG THỨC TỈNH",
        "line2": "TÂM AN VẠN SỰ AN",
        "cta": "BẤM VIDEO LIÊN QUAN ĐỂ NGHE TRỌN 50 PHÚT ⬇️"
    }
]

W, H = 1080, 1920

for idx, seg in enumerate(segments, 1):
    overlay_img_path = f"/Users/abc/.gemini/antigravity/scratch/overlay_{idx}.png"
    out_file = os.path.join(out_dir, seg["name"])
    
    # Create transparent PNG overlay with text
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    font_large = ImageFont.truetype(font_path, 54)
    font_sub = ImageFont.truetype(font_path, 42)
    font_cta = ImageFont.truetype(font_path, 34)
    
    # Helper to draw text with drop shadow
    def draw_text_shadow(draw_c, x, y, text, font, fill, shadow=(0,0,0,230)):
        for dx, dy in [(-3,-3), (3,-3), (-3,3), (3,3), (0,3), (3,0)]:
            draw_c.text((x+dx, y+dy), text, font=font, fill=shadow)
        draw_c.text((x, y), text, font=font, fill=fill)
    
    # Text line 1
    bbox1 = draw.textbbox((0, 0), seg["line1"], font=font_large)
    w1 = bbox1[2] - bbox1[0]
    draw_text_shadow(draw, (W - w1) // 2, 330, seg["line1"], font_large, (255, 230, 130, 255))
    
    # Text line 2
    bbox2 = draw.textbbox((0, 0), seg["line2"], font=font_sub)
    w2 = bbox2[2] - bbox2[0]
    draw_text_shadow(draw, (W - w2) // 2, 420, seg["line2"], font_sub, (255, 255, 255, 255))
    
    # CTA box at bottom
    bbox3 = draw.textbbox((0, 0), seg["cta"], font=font_cta)
    w3 = bbox3[2] - bbox3[0]
    h3 = bbox3[3] - bbox3[1]
    
    bx1 = (W - w3) // 2 - 25
    by1 = 1530
    bx2 = bx1 + w3 + 50
    by2 = by1 + h3 + 30
    
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=15, fill=(0, 0, 0, 200), outline=(255, 230, 130, 220), width=3)
    draw.text(((W - w3) // 2, by1 + 15), seg["cta"], font=font_cta, fill=(255, 255, 255, 255))
    
    img.save(overlay_img_path, "PNG")
    
    # FFmpeg: blurred background + center foreground + overlay PNG
    vf = (
        "[0:v]split=2[bg][fg];"
        "[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5[bg_b];"
        "[fg]scale=1080:-1[fg_s];"
        "[bg_b][fg_s]overlay=(W-w)/2:(H-h)/2[base];"
        "[base][1:v]overlay=0:0[v]"
    )
    
    cmd = [
        "/usr/local/bin/ffmpeg", "-y",
        "-ss", seg["start"],
        "-t", seg["duration"],
        "-i", src_video,
        "-i", overlay_img_path,
        "-filter_complex", vf,
        "-map", "[v]",
        "-map", "0:a",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "22",
        "-c:a", "aac",
        "-b:a", "192k",
        out_file
    ]
    
    print(f"Rendering {seg['name']}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ Thành công: {out_file} ({os.path.getsize(out_file)} bytes)")
    else:
        print(f"❌ Lỗi:", res.stderr[-400:])

print("TẤT CẢ ĐÃ HOÀN TẤT!")
