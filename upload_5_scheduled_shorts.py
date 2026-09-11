import sys, os, json, time, urllib.request
from datetime import datetime

sys.path.insert(0, "/Users/abc/.gemini/antigravity/scratch/1995lido_youtube_management")
import youtube_api_auto_uploader as uploader

# Function to upload with schedule (publishAt)
def upload_scheduled_video(video_path, title, description, tags, publish_at_utc):
    tokens = uploader.get_tokens()
    if not tokens:
        print("⚠️ Chưa tìm thấy token cấp quyền trong token.json!")
        return False
        
    access_token = tokens["access_token"]
    clean_title = title[:95]
    
    # In YouTube API v3: to schedule a video, status.privacyStatus MUST be 'private', and publishAt set in UTC
    metadata = {
        "snippet": {
            "title": clean_title,
            "description": description,
            "tags": tags,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_at_utc,
            "selfMade": True
        }
    }
    
    upload_url = "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status"
    meta_bytes = json.dumps(metadata).encode("utf-8")
    file_size = os.path.getsize(video_path)
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json; charset=UTF-8",
        "X-Upload-Content-Length": str(file_size),
        "X-Upload-Content-Type": "video/mp4"
    }
    
    req = urllib.request.Request(upload_url, data=meta_bytes, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            location = resp.headers.get("Location")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"❌ Upload Initiation HTTP {e.code} Error: {err_body}")
        return False
    except Exception as e:
        print(f"❌ Upload Initiation Failed: {e}")
        return False
        
    print(f"📡 Đang truyền tải {file_size / (1024*1024):.2f} MB lên YouTube...")
    with open(video_path, "rb") as f:
        video_bytes = f.read()
        
    upload_req = urllib.request.Request(location, data=video_bytes, headers={
        "Content-Length": str(file_size),
        "Content-Type": "video/mp4"
    }, method="PUT")
    
    try:
        with urllib.request.urlopen(upload_req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            video_id = result.get("id")
            print(f"🎉 LÊN LỊCH THÀNH CÔNG! Video ID: {video_id}")
            return video_id
    except Exception as e:
        print(f"❌ Binary Upload Failed: {e}")
        return False

# 5 Golden Time Slots for Tomorrow (12/09/2026):
# Vietnam is UTC+7
# Slot 1: 07:15 Sáng VN -> 00:15 UTC (2026-09-12T00:15:00Z)
# Slot 2: 11:45 Trưa VN -> 04:45 UTC (2026-09-12T04:45:00Z)
# Slot 3: 17:30 Chiều VN -> 10:30 UTC (2026-09-12T10:30:00Z)
# Slot 4: 19:45 Tối VN -> 12:45 UTC (2026-09-12T12:45:00Z)
# Slot 5: 21:15 Đêm VN -> 14:15 UTC (2026-09-12T14:15:00Z)

scheduled_list = [
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_04_Binh_Minh_Thanh_Tinh.mp4",
        "title": "Một Niệm Thanh Tịnh: Khởi Đầu Ngày Mới Bình An Cùng Nhạc Thiền #Shorts",
        "description": "Thanh lọc tâm trí buổi sớm mai cùng giai điệu sáo trúc thiền định. Bấm vào nút \"Video liên quan\" bên dưới để nghe trọn 50 phút nuôi dưỡng tâm an bạn nhé! 🙏🌿\n\n👉 Nghe trọn bộ 50 phút: https://www.youtube.com/watch?v=dCugzxszCJc\n#nhacthien #ngaymoianlanh #loiphatday #thaoduongtv #432hz #shorts",
        "tags": ["nhac thien buoi sang", "thanh tinh", "loi phat day", "tam an", "thaoduongtv", "shorts"],
        "publish_at": "2026-09-12T00:15:00Z",
        "slot_vn": "07:15 Sáng (12/09)"
    },
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_05_Nghi_Trua_Xoa_Diu_Tam.mp4",
        "title": "Buông Bỏ Mệt Mỏi: 20 Giây Nhạc Thiền Trị Liệu Cho Giấc Trưa Bình Yên #Shorts",
        "description": "Nghỉ trưa nhẹ nhàng, buông hết áp lực cùng tiếng mưa thiền định. Bấm vào nút \"Video liên quan\" bên dưới để nghe bản 50 phút giúp giấc ngủ sâu và tái tạo năng lượng!\n\n👉 Nghe trọn bộ 50 phút: https://www.youtube.com/watch?v=dCugzxszCJc\n#nhacthien #nghitrua #chualanh #buongbo #thaoduongtv #shorts",
        "tags": ["nhac thien nghi trua", "nhac ngu ngon", "chua lanh tam hon", "thaoduongtv", "shorts"],
        "publish_at": "2026-09-12T04:45:00Z",
        "slot_vn": "11:45 Trưa (12/09)"
    },
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_06_Hoang_Hon_Tan_So.mp4",
        "title": "Rũ Bỏ Áp Lực Cuối Ngày: Tiếng Chuông Chùa Xua Tan Mọi Muộn Phiền #Shorts",
        "description": "Tan sở mệt mỏi, hãy để tiếng chuông chùa đưa tâm bạn trở về giây phút hiện tại tĩnh lặng. Bấm vào nút \"Video liên quan\" để thưởng thức trọn bộ hòa tấu 50 phút.\n\n👉 Nghe trọn bộ 50 phút: https://www.youtube.com/watch?v=dCugzxszCJc\n#tiengchuongchua #tinhlang #loiphatday #kinhnikaya #thaoduongtv #shorts",
        "tags": ["tieng chuong chua", "xa stress", "nhac thien phat giao", "thaoduongtv", "shorts"],
        "publish_at": "2026-09-12T10:30:00Z",
        "slot_vn": "17:30 Chiều (12/09)"
    },
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_07_Hoa_Tau_432Hz_Tam_An.mp4",
        "title": "Tần Số 432Hz Chữa Lành: Nghe Để Thân Thể Nhẹ Nhàng & Tâm Trí Tĩnh Lặng #Shorts",
        "description": "Tần số sóng âm 432Hz tự nhiên hỗ trợ xoa dịu lo âu và phục hồi cảm xúc. Bấm nút \"Video liên quan\" bên dưới để thả lỏng thân tâm cùng bản nhạc 50 phút nhé!\n\n👉 Nghe trọn bộ 50 phút: https://www.youtube.com/watch?v=dCugzxszCJc\n#nhacthien432hz #tanso432hz #chualanh #taman #thaoduongtv #shorts",
        "tags": ["nhac thien 432hz", "tan so chua lanh", "thu gian tam tri", "thaoduongtv", "shorts"],
        "publish_at": "2026-09-12T12:45:00Z",
        "slot_vn": "19:45 Tối (12/09)"
    },
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_08_Mua_Dem_Ngu_Sau.mp4",
        "title": "Mưa Đêm Thiền Định: Nghe 20 Giây Này Tự Nhiên Ngủ Ngon Đến Sáng #Shorts",
        "description": "Mưa rơi êm đềm đưa bạn vào giấc ngủ say nồng, không mộng mị. Bấm nút \"Video liên quan\" bên dưới để bật hòa tấu 50 phút nghe ngủ trọn đêm nay nhé! 🙏🌸\n\n👉 Nghe trọn bộ 50 phút: https://www.youtube.com/watch?v=dCugzxszCJc\n#muadem #nhacthienngungon #deepsleep #chualanh #thaoduongtv #shorts",
        "tags": ["mua dem ngu ngon", "nhac thien ngu sau", "chua mat ngu", "thaoduongtv", "shorts"],
        "publish_at": "2026-09-12T14:15:00Z",
        "slot_vn": "21:15 Đêm (12/09)"
    }
]

output_results = []
log_file = "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/scheduled_5_shorts_results.json"

for idx, item in enumerate(scheduled_list, 1):
    print(f"\n==================== [LÊN LỊCH SHORTS {idx}/5 - {item['slot_vn']}] ====================")
    vid_id = upload_scheduled_video(
        video_path=item["file"],
        title=item["title"],
        description=item["description"],
        tags=item["tags"],
        publish_at_utc=item["publish_at"]
    )
    if vid_id:
        output_results.append({
            "slot": item["slot_vn"],
            "title": item["title"],
            "video_id": vid_id,
            "edit_url": f"https://studio.youtube.com/video/{vid_id}/edit",
            "shorts_url": f"https://youtube.com/shorts/{vid_id}",
            "publish_at_utc": item["publish_at"]
        })
        print(f"✅ ĐÃ ĐẶT LỊCH THÀNH CÔNG: {item['slot_vn']} (ID: {vid_id})")
    time.sleep(3)

with open(log_file, "w", encoding="utf-8") as f:
    json.dump(output_results, f, ensure_ascii=False, indent=2)

print("\n🎉 HOÀN THÀNH LÊN LỊCH TẤT CẢ 5 VIDEO SHORTS KHUNG GIỜ VÀNG NGÀY MAI!")
