import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

src_video = "/Users/abc/Documents/KenhYTB/nhacthien_long/Video_Hoan_Chinh_Nhac_Thien_50Phut.mp4"
out_dir = "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo"
font_path = "/Library/Fonts/Arial Unicode.ttf"

# 5 Golden Time segments from 50min video with high emotional climax:
# 1. 03:20 -> 03:40 (20s): Tiếng sáo trúc & chuông xoay thanh tao (Khung Sáng 07:15)
# 2. 12:10 -> 12:30 (20s): Giai điệu mưa rơi & piano du dương (Khung Trưa 11:45)
# 3. 21:00 -> 21:20 (20s): Chuông chùa cổ & đàn tranh tĩnh tại (Khung Chiều 17:30)
# 4. 28:15 -> 28:35 (20s): Hòa tấu 432Hz xoa dịu lo âu sâu lắng (Khung Tối 19:45)
# 5. 37:30 -> 37:50 (20s): Mưa đêm êm đềm & thiền định đưa vào giấc ngủ (Khung Đêm 21:15)

segments = [
    {
        "name": "Short_04_Binh_Minh_Thanh_Tinh.mp4",
        "start": "00:03:20",
        "duration": "20",
        "line1": "MỘT NIỆM THANH TỊNH",
        "line2": "KHỞI ĐẦU NGÀY MỚI AN YÊN",
        "cta": "BẤM VIDEO LIÊN QUAN NGHE TRỌN 50 PHÚT ⬇️",
        "title": "Một Niệm Thanh Tịnh: Khởi Đầu Ngày Mới Bình An Cùng Nhạc Thiền #Shorts",
        "schedule": "2026-09-12T00:15:00Z", # 07:15 AM VN (UTC+7) -> 00:15 UTC
        "time_vn": "07:15 Sáng (12/09)"
    },
    {
        "name": "Short_05_Nghi_Trua_Xoa_Diu_Tam.mp4",
        "start": "00:12:10",
        "duration": "20",
        "line1": "BUÔNG HẾT LO ÂU",
        "line2": "NGHỈ TRƯA THANH THẢN TÂM TRÍ",
        "cta": "BẤM VIDEO LIÊN QUAN NGHE TRỌN 50 PHÚT ⬇️",
        "title": "Buông Bỏ Mệt Mỏi: 20 Giây Nhạc Thiền Trị Liệu Cho Giấc Trưa Bình Yên #Shorts",
        "schedule": "2026-09-12T04:45:00Z", # 11:45 AM VN -> 04:45 UTC
        "time_vn": "11:45 Trưa (12/09)"
    },
    {
        "name": "Short_06_Hoang_Hon_Tan_So.mp4",
        "start": "00:21:00",
        "duration": "20",
        "line1": "TIẾNG CHUÔNG BUÔNG XẢ",
        "line2": "RŨ BỎ MỆT MỎI SAU GIỜ LÀM",
        "cta": "BẤM VIDEO LIÊN QUAN NGHE TRỌN 50 PHÚT ⬇️",
        "title": "Rũ Bỏ Áp Lực Cuối Ngày: Tiếng Chuông Chùa Xua Tan Mọi Muộn Phiền #Shorts",
        "schedule": "2026-09-12T10:30:00Z", # 17:30 PM VN -> 10:30 UTC
        "time_vn": "17:30 Chiều (12/09)"
    },
    {
        "name": "Short_07_Hoa_Tau_432Hz_Tam_An.mp4",
        "start": "00:28:15",
        "duration": "20",
        "line1": "TẦN SỐ 432HZ CHỮA LÀNH",
        "line2": "TÂM AN VẠN SỰ AN LÀNH",
        "cta": "BẤM VIDEO LIÊN QUAN NGHE TRỌN 50 PHÚT ⬇️",
        "title": "Tần Số 432Hz Chữa Lành: Nghe Để Thân Thể Nhẹ Nhàng & Tâm Trí Tĩnh Lặng #Shorts",
        "schedule": "2026-09-12T12:45:00Z", # 19:45 PM VN -> 12:45 UTC
        "time_vn": "19:45 Tối (12/09)"
    },
    {
        "name": "Short_08_Mua_Dem_Ngu_Sau.mp4",
        "start": "00:37:30",
        "duration": "20",
        "line1": "MƯA ĐÊM TĨNH MỊCH",
        "line2": "CHÌM SÂU VÀO GIẤC NGỦ AN LÀNH",
        "cta": "BẤM VIDEO LIÊN QUAN NGHE TRỌN 50 PHÚT ⬇️",
        "title": "Mưa Đêm Thiền Định: Nghe 20 Giây Này Tự Nhiên Ngủ Ngon Đến Sáng #Shorts",
        "schedule": "2026-09-12T14:15:00Z", # 21:15 PM VN -> 14:15 UTC
        "time_vn": "21:15 Đêm (12/09)"
    }
]

W, H = 1080, 1920

for idx, seg in enumerate(segments, 4):
    overlay_img_path = f"/Users/abc/.gemini/antigravity/scratch/overlay_{idx}.png"
    out_file = os.path.join(out_dir, seg["name"])
    
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    font_large = ImageFont.truetype(font_path, 52)
    font_sub = ImageFont.truetype(font_path, 40)
    font_cta = ImageFont.truetype(font_path, 34)
    
    def draw_text_shadow(draw_c, x, y, text, font, fill, shadow=(0,0,0,230)):
        for dx, dy in [(-3,-3), (3,-3), (-3,3), (3,3), (0,3), (3,0)]:
            draw_c.text((x+dx, y+dy), text, font=font, fill=shadow)
        draw_c.text((x, y), text, font=font, fill=fill)
    
    bbox1 = draw.textbbox((0, 0), seg["line1"], font=font_large)
    w1 = bbox1[2] - bbox1[0]
    draw_text_shadow(draw, (W - w1) // 2, 330, seg["line1"], font_large, (255, 230, 130, 255))
    
    bbox2 = draw.textbbox((0, 0), seg["line2"], font=font_sub)
    w2 = bbox2[2] - bbox2[0]
    draw_text_shadow(draw, (W - w2) // 2, 420, seg["line2"], font_sub, (255, 255, 255, 255))
    
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
        print(f"✅ Đã dựng xong: {out_file}")
    else:
        print(f"❌ Lỗi:", res.stderr[-300:])

print("HOÀN TẤT RENDER 5 SHORTS!")
