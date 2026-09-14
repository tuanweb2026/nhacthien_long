import sys, os, json, time, urllib.request, re
from datetime import datetime

sys.path.insert(0, "/Users/abc/.gemini/antigravity/scratch/1995lido_youtube_management")
import youtube_api_auto_uploader as uploader

# 1. Load target shorts list
target_file = "/Users/abc/Documents/KenhYTB/nhacthien_long/target_shorts_under_10_views.json"
with open(target_file, "r", encoding="utf-8") as f:
    target_videos = json.load(f)

print(f"🎯 TỔNG SỐ SHORTS CẦN HỒI SINH (< 10 VIEWS, >= 3 NGÀY TRƯỚC): {len(target_videos)} VIDEO")

tokens = uploader.get_tokens()
access_token = tokens["access_token"]

def generate_million_view_title(old_title):
    t = old_title.split("#")[0].strip()
    t = re.sub(r'^(Kinh Nikaya|Kinh Trung Bộ|Thảo Dương TV)\s*[:\-|]?\s*', '', t, flags=re.IGNORECASE).strip()
    t = t.replace("Lời Khuyên Bình An", "").strip(" -:|")
    
    # Keyword based transformation
    if "Nước Ấm" in t or "Khỏe Mạnh" in t:
        return "1 Ly Nước Ấm Sáng Sớm: Bí Mật Trường Thọ & Tráng Kiện Của Người Xưa #Shorts"
    elif "Hơi Thở" in t or "Bình Yên" in t:
        return "Tâm Bất An? Trở Về Với Hơi Thở: Bí Quyết Định Tâm Trong 10 Giây #Shorts"
    elif "Kỷ Luật" in t or "Phiên Bản" in t:
        return "Kỷ Luật Là Đỉnh Cao Của Tự Do: Muốn Đổi Đời Hãy Nghe Lời Phật Dạy #Shorts"
    elif "Thời Gian" in t or "Ưu Tiên" in t:
        return "Bận Rộn Nhưng Vẫn Nghèo? Nhận Ra Sự Thật Này Cuộc Đời Sẽ Khác #Shorts"
    elif "Vùng An Toàn" in t:
        return "Vùng An Toàn Đang Giết Chết Tương Lai Bạn: Lời Cảnh Tỉnh Sâu Sắc #Shorts"
    elif "Việc Tốt" in t or "Nở Hoa" in t:
        return "1 Hành Động Thiện Mỗi Ngày: Cách Gieo Nhân Lành Đổi Vận Mệnh Cực Nhanh #Shorts"
    elif "Chúc Bạn" in t or "An Yên" in t or "Phúc Lành" in t:
        return "Chúc Bạn Một Đời Bình An: Lời Khai Thị Che Chở Mọi Giông Bão Cuộc Đời #Shorts"
    elif "Bữa Cơm" in t or "Gia Đình" in t:
        return "Gia Đạo Bất Hòa Thì Làm Gì? Lời Phật Dạy Về Năng Lượng Gắn Kết #Shorts"
    elif "Cho Đi" in t or "Giàu Nhanh" in t:
        return "Muốn Giàu Sang Trước Hết Phải Biết Bố Thí: Luật Nhân Quả Bất Biến #Shorts"
    elif "Món Quà" in t or "Tiền Bạc" in t:
        return "Để Lại Gì Cho Con Cái? Phật Dạy Thứ Quý Giá Hơn Cả Núi Tiền #Shorts"
    elif "Nghèo" in t or "Bần Cùng" in t or "Keo Kiệt" in t:
        return "Vì Sao Cả Đời Bần Cùng Thiếu Thốn? Cội Rễ Nằm Ở Tính Keo Kiệt Này #Shorts"
    elif "Xấu Xí" in t or "Dung Mạo" in t or "Kém Xinh" in t:
        return "Muốn Dung Nhan Xinh Đẹp, Dễ Mến: Đừng Bao Giờ Phạm Phải Lỗi Này #Shorts"
    elif "Đoản Mạng" in t or "Chết Trẻ" in t or "Sống Thọ" in t:
        return "Nhân Gì Khiến Đoản Mạng, Chết Yểu? Lời Phật Cảnh Tỉnh Muôn Đời #Shorts"
    elif "Ôm Đau" in t or "Bệnh Tật" in t:
        return "Vì Sao Thân Thể Ôm Đau Triền Miên? Gieo Nhân Này Thân Sẽ Tráng Kiện #Shorts"
    elif "Trí Tuệ" in t or "Kém Cỏi" in t or "Đần Độn" in t:
        return "Muốn Khai Mở Trí Tuệ Uyên Bác, Sáng Suốt: Hãy Làm Ngay Điều Này #Shorts"
    elif "Ngạo Mạn" in t or "Kiêu Căng" in t:
        return "Cái Bẫy Của Sự Kiêu Ngạo: Cội Rễ Đưa Đến Bại Vong Nhanh Nhất #Shorts"
    elif "Nghiệp" in t or "Chủ Nhân" in t:
        return "Nhắm Mắt Xuôi Tay Ta Mang Được Gì? Sự Thật Về Nghiệp Báo Luân Hồi #Shorts"
    else:
        clean = t.strip()
        if len(clean) > 52: clean = clean[:52]
        return f"{clean}: Lời Phật Dạy Rất Thấm | Nghe Để Tâm An #Shorts"

# Million-View SEO Description with Direct Channel Subscribe Link & 50min Pillar Link
def get_seo_content():
    desc = (
        "🌿 Dừng lại 20 giây để buông xả muộn phiền và đón nhận năng lượng bình an từ lời dạy của Đức Phật. Khi tâm tĩnh lặng, mọi nghịch cảnh ngoài kia tự khắc bình yên.\n\n"
        "👉 Bấm ĐĂNG KÝ KÊNH @1995lido để cùng gieo duyên lành và nuôi dưỡng tâm an mỗi ngày: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n"
        "🎶 Thưởng thức trọn bộ hòa tấu thiền định 50 phút ru ngủ & xoa dịu lo âu: https://www.youtube.com/watch?v=dCugzxszCJc\n\n"
        "#loiphatday #kinhnikaya #taman #chualanh #nhan_qua #buongbo #thaoduongtv #shorts"
    )
    tags = ["loi phat day", "kinh nikaya", "tam an", "chua lanh", "nhan qua", "buong bo muon phien", "thaoduongtv", "shorts"]
    return desc, tags

comment_cta = (
    "🌸 Mỗi lượt ĐĂNG KÝ KÊNH là một hạt giống thiện lành cùng Thảo Dương TV lan tỏa Phật pháp đến muôn nơi. Bấm Đăng Ký để tâm luôn an bạn nhé! 🙏🌿\n"
    "👉 Nghe trọn bộ hòa tấu thiền 50 phút đưa vào giấc ngủ sâu: https://www.youtube.com/watch?v=dCugzxszCJc"
)

log_output = "/Users/abc/Documents/KenhYTB/nhacthien_long/revive_batch2_under_10_views.json"
results = []

for idx, item in enumerate(target_videos, 1):
    vid = item["id"]
    old_title = item["title"]
    new_title = generate_million_view_title(old_title)[:95]
    desc, tags = get_seo_content()
    
    print(f"\n[{idx}/{len(target_videos)}] Đang cập nhật video: {vid}")
    print(f"   Old: {old_title[:45]}...")
    print(f"   New: {new_title}")
    
    # 1. Update Video Snippet
    get_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={vid}"
    req = urllib.request.Request(get_url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(req) as r:
            snippet = json.loads(r.read().decode())["items"][0]["snippet"]
            snippet["title"] = new_title
            snippet["description"] = desc
            snippet["tags"] = tags
            
            up_url = "https://www.googleapis.com/youtube/v3/videos?part=snippet"
            up_req = urllib.request.Request(
                up_url,
                data=json.dumps({"id": vid, "snippet": snippet}).encode("utf-8"),
                headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
                method="PUT"
            )
            with urllib.request.urlopen(up_req) as up_r:
                print("   ✅ Đã đổi Tiêu đề & SEO thành công!")
    except Exception as e:
        print(f"   ❌ Lỗi cập nhật snippet: {e}")
        continue
        
    # 2. Add Subscribe Call-To-Action Comment
    c_url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet"
    c_payload = {
        "snippet": {
            "videoId": vid,
            "topLevelComment": {"snippet": {"textOriginal": comment_cta}}
        }
    }
    c_req = urllib.request.Request(
        c_url,
        data=json.dumps(c_payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(c_req) as c_r:
            print("   ✅ Đã đăng bình luận kêu gọi Đăng ký kênh!")
    except Exception as e:
        print(f"   ⚠️ Bình luận note: {e}")

    results.append({
        "id": vid,
        "old_title": old_title,
        "new_title": new_title,
        "views": item["views"],
        "published_vn": item["published_vn"],
        "updated_at": datetime.now().isoformat()
    })
    
    with open(log_output, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    time.sleep(2) # Safe cooldown

print(f"\n🎉 HOÀN THÀNH HỒI SINH {len(results)}/{len(target_videos)} SHORTS DƯỚI 10 VIEWS!")
