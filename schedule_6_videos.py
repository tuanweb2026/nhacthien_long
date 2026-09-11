import sys, os, json, time, urllib.request
from datetime import datetime, timedelta

sys.path.insert(0, "/Users/abc/.gemini/antigravity/scratch/1995lido_youtube_management")
import youtube_api_auto_uploader as uploader

tokens = uploader.get_tokens()
access_token = tokens["access_token"]

# 6 videos mapping
videos = [
    {"id": "ZiJdqlzItl0", "title": "Bình Yên Tự Tại & Chìm Sâu Vào Giấc Ngủ"},
    {"id": "q1JKFGr4d_w", "title": "Mưa Đêm Thanh Lọc Năng Lượng Tiêu Cực"},
    {"id": "HOZb04FDmss", "title": "Hòa Tấu Thiền Định Nuôi Dưỡng Tâm An (432Hz)"},
    {"id": "j2grYzWijds", "title": "Âm Hưởng Kinh Điển & Tĩnh Lặng Trí Tuệ"},
    {"id": "wfeVoIfPpik", "title": "Tiếng Mưa Rơi Trong Tĩnh Lặng"},
    {"id": "yS5u-txdZKY", "title": "Thiền Sâu & Buông Xả Thân Tâm"}
]

# Start scheduling starting in 15 minutes, spaced 10 minutes apart:
# Current local time in Vietnam: 00:30 (12/09) -> UTC: 17:30 (11/09)
# Video 1: +15m
# Video 2: +25m
# Video 3: +35m
# Video 4: +45m
# Video 5: +55m
# Video 6: +65m

now_utc = datetime.utcnow()
print(f"Current UTC time: {now_utc.isoformat()}Z")

results = []
for idx, v in enumerate(videos):
    delay_mins = 15 + idx * 10
    publish_time_utc = (now_utc + timedelta(minutes=delay_mins)).strftime("%Y-%m-%dT%H:%M:00Z")
    publish_time_vn = (now_utc + timedelta(minutes=delay_mins) + timedelta(hours=7)).strftime("%H:%M ngày %d/%m")
    
    url = "https://www.googleapis.com/youtube/v3/videos?part=status"
    payload = {
        "id": v["id"],
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_time_utc
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        method="PUT"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"✅ Video {idx+1}: '{v['title']}' -> ĐÃ LÊN LỊCH PHÁT: {publish_time_vn} (UTC: {publish_time_utc})")
            results.append({
                "video_id": v["id"],
                "title": v["title"],
                "publish_vn": publish_time_vn,
                "publish_utc": publish_time_utc,
                "edit_url": f"https://studio.youtube.com/video/{v['id']}/edit"
            })
    except Exception as e:
        print(f"❌ Lỗi lên lịch video {v['id']}: {e}")
    time.sleep(2)

with open("/Users/abc/Documents/KenhYTB/nhacthien_long/phan1_musicful_done/schedule_success.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n🎉 HOÀN TẤT LÊN LỊCH TẤT CẢ 6 VIDEO CÁCH NHAU 10 PHÚT!")
