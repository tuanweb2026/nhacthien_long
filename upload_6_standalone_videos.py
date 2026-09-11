import sys, os, json, time
from datetime import datetime

sys.path.insert(0, "/Users/abc/.gemini/antigravity/scratch/1995lido_youtube_management")
import youtube_api_auto_uploader as uploader

# Custom uploader function ensuring private status
def upload_private_video(video_path, title, description, tags):
    tokens = uploader.get_tokens()
    if not tokens:
        print("⚠️ Chưa tìm thấy token cấp quyền trong token.json!")
        return False
        
    access_token = tokens["access_token"]
    clean_title = title[:95]
    
    metadata = {
        "snippet": {
            "title": clean_title,
            "description": description,
            "tags": tags,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "private",
            "selfMade": True
        }
    }
    
    import urllib.request
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
        
    print(f"📡 Đang tải {file_size / (1024*1024):.2f} MB lên YouTube (Chế độ Riêng tư/Private)...")
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
            print(f"🎉 TẢI LÊN THÀNH CÔNG! Video ID: {video_id}")
            return video_id
    except Exception as e:
        print(f"❌ Binary Upload Failed: {e}")
        return False

# Mapping 6 videos in /Users/abc/Documents/KenhYTB/nhacthien_long/phan1_musicful_done
folder = "/Users/abc/Documents/KenhYTB/nhacthien_long/phan1_musicful_done"

videos_plan = [
    {
        "index": 1,
        "file": os.path.join(folder, "Bai6 _Binhyen tutai.mp4"),
        "title": "Bình Yên Tự Tại & Chìm Sâu Vào Giấc Ngủ | Sóng Não Delta Ru Điệu An Lành (432Hz)",
        "description": "Lắng nghe giai điệu hòa tấu tĩnh lặng với tần số sóng não Delta êm dịu, giúp buông xả mọi căng thẳng, bất an và chìm sâu vào giấc ngủ an lành không mộng mị.\n\n🌸 Kênh Thảo Dương TV - Nơi nuôi dưỡng tâm an và lan tỏa lời Phật dạy ứng dụng.\n👉 Đăng ký kênh: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n#nhacthien #ngungon #songnaodelta #chualanh #thaoduongtv #432hz",
        "tags": ["nhac thien ngu ngon", "song nao delta", "binh yen tu tai", "nhac thien phat giao", "thaoduongtv", "432hz"]
    },
    {
        "index": 2,
        "file": os.path.join(folder, "Bai5_Muademthanlocnangluongtieucuc.mp4"),
        "title": "Mưa Đêm Thanh Lọc Năng Lượng Tiêu Cực | Hòa Tấu Thiền Định Âm Dương Hòa Hợp",
        "description": "Tiếng mưa đêm rơi nhẹ trên mái ngói hòa quyện tiếng sáo trúc sâu lắng, gột rửa mọi áp lực, lo toan sau một ngày dài mệt mỏi. Hãy thả lỏng thân tâm và lắng nghe.\n\n🌸 Kênh Thảo Dương TV - Nơi nuôi dưỡng tâm an và lan tỏa lời Phật dạy ứng dụng.\n👉 Đăng ký kênh: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n#muadem #nhacthienmua #thanhloctieucuc #chualanh #thaoduongtv #loiphatday",
        "tags": ["mua dem thanh loc", "tieng mua roi", "nhac thien mua", "buong bo muon phien", "thaoduongtv"]
    },
    {
        "index": 3,
        "file": os.path.join(folder, "bai4_Thiendinhanduongtaman.mp4"),
        "title": "Hòa Tấu Thiền Định Nuôi Dưỡng Tâm An | Tần Số 432Hz Phục Hồi Năng Lượng Tích Cực",
        "description": "Giai điệu thiền định với tần số chuẩn 432Hz giúp cân bằng cảm xúc, ổn định nhịp tim và đưa tâm trí trở về trạng thái an nhiên tự tại nhất.\n\n🌸 Kênh Thảo Dương TV - Nơi nuôi dưỡng tâm an và lan tỏa lời Phật dạy ứng dụng.\n👉 Đăng ký kênh: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n#nhacthien432hz #taman #tanso432hz #thienchaptay #thaoduongtv #chualanh",
        "tags": ["nhac thien 432hz", "nuoi duong tam an", "thien dinh chua lanh", "phuc hoi nang luong", "thaoduongtv"]
    },
    {
        "index": 4,
        "file": os.path.join(folder, "bai3_tinhlangtritue.mp4"),
        "title": "Âm Hưởng Kinh Điển & Tĩnh Lặng Trí Tuệ | Tiếng Chuông Chùa Thức Tỉnh Tâm Thức",
        "description": "Tiếng chuông xoay Tây Tạng và âm vang cổ truyền đưa bạn vào miền tĩnh mịch của trí tuệ, xua tan mê mờ và nuôi dưỡng chánh tri kiến theo lời Phật dạy.\n\n🌸 Kênh Thảo Dương TV - Nơi nuôi dưỡng tâm an và lan tỏa lời Phật dạy ứng dụng.\n👉 Đăng ký kênh: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n#tiengchuongchua #kinhnikaya #loiphatday #tinhlangtritue #thaoduongtv #432hz",
        "tags": ["tieng chuong chua", "am huong kinh dien", "kinh nikaya", "loi phat day", "tinh lang tri tue", "thaoduongtv"]
    },
    {
        "index": 5,
        "file": os.path.join(folder, "Bai2_muaroitinhlang.mp4"),
        "title": "Tiếng Mưa Rơi Trong Tĩnh Lặng | Xoa Dịu Bất An, Thư Giãn Thần Kinh & Ngủ Sâu",
        "description": "Thanh âm mưa rơi đều đặn kết hợp cùng tiếng đàn mộc êm dịu tạo nên liều thuốc xoa dịu tâm hồn, giúp bạn rũ bỏ âu lo và đi vào giấc ngủ dễ dàng.\n\n🌸 Kênh Thảo Dương TV - Nơi nuôi dưỡng tâm an và lan tỏa lời Phật dạy ứng dụng.\n👉 Đăng ký kênh: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n#tiengmuaroi #xoadioban #nhacthienngungon #chualanh #thaoduongtv #thugian",
        "tags": ["tieng mua roi trong tinh lang", "xoa diu bat an", "nhac ngu ngon", "thien dinh", "thaoduongtv"]
    },
    {
        "index": 6,
        "file": os.path.join(folder, "bai1_deepsleep.mp4"),
        "title": "Thiền Sâu & Buông Xả Thân Tâm | Lời Phật Dạy Về Giấc Ngủ An Lạc (Deep Sleep)",
        "description": "Bản hòa tấu mở đầu giúp buông xả mọi gánh nặng cuộc sống, đưa tâm hồn về bến đỗ bình an của chánh niệm và giấc ngủ an lành trọn vẹn.\n\n🌸 Kênh Thảo Dương TV - Nơi nuôi dưỡng tâm an và lan tỏa lời Phật dạy ứng dụng.\n👉 Đăng ký kênh: https://www.youtube.com/@1995lido?sub_confirmation=1\n\n#thiensau #buongxathantam #deepsleep #nhacthienphatgiao #thaoduongtv #loiphatday",
        "tags": ["thien sau buong xa", "deep sleep", "nhac thien phat giao", "loi phat day", "thaoduongtv"]
    }
]

log_output = "/Users/abc/Documents/KenhYTB/nhacthien_long/phan1_musicful_done/upload_6_videos_log.json"
results = []

# Upload continuously with small pause (each video is ~8-9 min in content)
for idx, v in enumerate(videos_plan, 1):
    print(f"\n=======================================================")
    print(f"▶️ BẮT ĐẦU TẢI LÊN VIDEO [{idx}/6]: {v['title'][:40]}...")
    print(f"=======================================================")
    
    vid_id = upload_private_video(
        video_path=v["file"],
        title=v["title"],
        description=v["description"],
        tags=v["tags"]
    )
    
    if vid_id:
        entry = {
            "index": idx,
            "title": v["title"],
            "video_id": vid_id,
            "edit_url": f"https://studio.youtube.com/video/{vid_id}/edit",
            "youtube_url": f"https://www.youtube.com/watch?v={vid_id}",
            "privacy": "private",
            "time": datetime.now().isoformat()
        }
        results.append(entry)
        with open(log_output, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    else:
        print(f"❌ Upload thất bại video {idx}")
        
    time.sleep(5)

print("\n🎉 ĐÃ TẢI LÊN HOÀN TẤT CẢ 6 VIDEO Ở CHẾ ĐỘ PRIVATE!")
