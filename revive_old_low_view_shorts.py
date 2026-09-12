import sys, os, json, time, urllib.request
from datetime import datetime, timedelta

sys.path.insert(0, "/Users/abc/.gemini/antigravity/scratch/1995lido_youtube_management")
import youtube_api_auto_uploader as uploader

# 1. Load low-view report
report_path = "/Users/abc/Documents/KenhYTB/nhacthien_long/low_view_shorts_report.json"
if not os.path.exists(report_path):
    print("Không tìm thấy low_view_shorts_report.json")
    sys.exit(1)

with open(report_path, "r", encoding="utf-8") as f:
    lows = json.load(f)

# Cutoff: Only videos published >= 5 days ago from now (<= 2026-09-07 16:30:00)
now = datetime(2026, 9, 12, 16, 30, 0)
cutoff_date = now - timedelta(days=5)

target_videos = []
for it in lows:
    try:
        pub_dt = datetime.strptime(it["published_utc"], "%Y-%m-%dT%H:%M:%SZ")
        if pub_dt <= cutoff_date and it["status"] == "public":
            target_videos.append(it)
    except:
        pass

print(f"🎯 TỔNG SỐ VIDEO CẦN HỒI SINH (>= 5 NGÀY, VIEW < 5): {len(target_videos)} VIDEO")

tokens = uploader.get_tokens()
access_token = tokens["access_token"]

def generate_hook_title(old_title):
    t = old_title
    # Clean hashtags & fluff
    t = t.split("#")[0].strip()
    t = t.replace("Kinh Nikaya:", "").replace("Kinh Nikaya", "").replace("Kinh Trung Bộ:", "").strip()
    t = t.replace("Lời Khuyên Bình An", "").replace("-", "").strip()
    
    # Smart Hook transformation
    if "Hành Động Tạo Nên Số Phận" in t:
        return "3 Hành Động Quyết Định Phúc Họa Cả Đời Bạn | Lời Phật Dạy Rất Thấm #Shorts"
    elif "Thiện" in t or "Ác" in t:
        return "Gieo Nhân Gì Gặt Quả Nấy: Sự Thật Về Nghiệp Báo Không Thể Tránh #Shorts"
    elif "Hạnh Phúc" in t or "Nhận Thức" in t:
        return "Làm Sao Để Bớt Khổ Đau? Bí Quyết Tâm An Của Đức Phật #Shorts"
    elif "Bạn Thực Sự Là Ai" in t or "Danh Và Sắc" in t:
        return "Bạn Thực Sự Là Ai? Sự Thật Về Thân Xác Khi Nhắm Mắt Xuôi Tay #Shorts"
    elif "Làm Chủ Cảm Xúc" in t:
        return "Làm Chủ Cơn Giận Trong 30 Giây: Lời Phật Dạy Trị Liệu Cảm Xúc #Shorts"
    elif "Giác Quan" in t or "Đánh Lừa" in t:
        return "Đừng Để Cảm Xúc Đánh Lừa: Cách Đức Phật Nhìn Thấu Cuộc Đời #Shorts"
    elif "Tứ Diệu Đế" in t or "Con Đường" in t:
        return "4 Sự Thật Giúp Thoát Khỏi Trầm Cảm & Bế Tắc Cuộc Sống #Shorts"
    elif "Chay Mặn" in t:
        return "Ăn Chay Hay Ăn Mặn Mới Đúng? Lời Phật Khai Thị Bất Ngờ #Shorts"
    elif "Chánh Mạng" in t or "Kiếm Tiền" in t:
        return "Kiếm Tiền Thế Nào Để Đêm Về Ngủ Ngon? Lời Phật Về Chánh Mạng #Shorts"
    elif "Chánh Định" in t or "Tĩnh Lặng" in t:
        return "Tâm Bất An Thì Làm Gì? Cách Ngồi Yên Cho Lòng Thanh Thản #Shorts"
    elif "Biết Ơn" in t:
        return "Phép Màu Của Lòng Biết Ơn: Đổi Vận Mệnh Chỉ Bằng 1 Ý Niệm #Shorts"
    elif "Chữa Mọi Nỗi Đau" in t or "Toa Thuốc" in t:
        return "Toa Thuốc Chữa Lành Mọi Tổn Thương Tâm Hồn Của Đức Phật #Shorts"
    elif "Tuổi Già" in t or "Hơi Thở Cuối Cùng" in t or "Chết" in t:
        return "Khoảnh Khắc Trút Hơi Thở Cuối Cùng: Nghe Để Không Phải Hối Hận #Shorts"
    elif "Chánh Niệm" in t:
        return "4 Nơi Trú Ẩn Cho Tâm Hồn Khi Thế Giới Quá Mệt Mỏi #Shorts"
    elif "Bố Thí" in t:
        return "Gieo Phước Gì Để Con Cháu Được Giàu Sang, Bình An Cả Đời? #Shorts"
    else:
        clean_t = t.strip()
        if len(clean_t) > 55: clean_t = clean_t[:55]
        return f"{clean_t}: Lời Phật Dạy Rất Thấm | Nghe Để Tâm An #Shorts"

# Standard Million-View Description & Tags
def get_seo_pack():
    desc = (
        "🌿 Cuộc sống có bao muộn phiền, hãy dừng lại đôi phút để lắng nghe lời dạy thâm sâu của Đức Phật. Khi tâm an định, mọi sóng gió ngoài kia tự khắc hóa hư không.\n\n"
        "👉 Bấm ĐĂNG KÝ KÊNH @1995lido để gieo duyên thiện lành và đón nhận năng lượng bình an mỗi ngày: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n"
        "🎶 Nghe trọn bộ 50 phút hòa tấu thiền định ru ngủ & trị liệu lo âu: https://www.youtube.com/watch?v=dCugzxszCJc\n\n"
        "#loiphatday #kinhnikaya #taman #chualanh #nhan_qua #buongbo #thaoduongtv #shorts"
    )
    tags = ["loi phat day", "kinh nikaya", "tam an", "chua lanh", "nhan qua", "buong bo muon phien", "thaoduongtv", "shorts"]
    return desc, tags

comment_template = (
    "🌸 Mỗi lượt ĐĂNG KÝ KÊNH là một hạt giống thiện lành cùng Thảo Dương TV lan tỏa Phật pháp đến muôn nơi. Bấm Đăng Ký để tâm luôn an bạn nhé! 🙏🌿\n"
    "👉 Nghe trọn bộ hòa tấu thiền 50 phút đưa vào giấc ngủ sâu: https://www.youtube.com/watch?v=dCugzxszCJc"
)

results = []
log_file = "/Users/abc/Documents/KenhYTB/nhacthien_long/revive_update_results.json"

for idx, item in enumerate(target_videos, 1):
    vid = item["id"]
    old_title = item["title"]
    new_title = generate_hook_title(old_title)[:95]
    desc, tags = get_seo_pack()
    
    print(f"\n[{idx}/{len(target_videos)}] Đang hồi sinh video: {vid}")
    print(f"   Cu: {old_title[:45]}...")
    print(f"   Moi: {new_title}")
    
    # 1. Update snippet (Title, Description, Tags)
    get_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={vid}"
    req = urllib.request.Request(get_url, headers={"Authorization": f"Bearer {access_token}"})
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode())
            snippet = data["items"][0]["snippet"]
            
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
        
    # 2. Add Call-To-Action Comment
    c_url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet"
    c_payload = {
        "snippet": {
            "videoId": vid,
            "topLevelComment": {"snippet": {"textOriginal": comment_template}}
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
        print(f"   ⚠️ Lỗi bình luận (có thể đã có comment): {e}")

    results.append({
        "id": vid,
        "old_title": old_title,
        "new_title": new_title,
        "views": item["views"],
        "published_vn": item["published_vn"],
        "updated_at": datetime.now().isoformat()
    })
    
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    time.sleep(2) # Small cooldown between API calls

print(f"\n🎉 HOÀN THÀNH HỒI SINH {len(results)}/{len(target_videos)} VIDEO SHORTS CŨ!")
