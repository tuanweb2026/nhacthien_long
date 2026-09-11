import sys, os, json, time
from datetime import datetime

sys.path.insert(0, "/Users/abc/.gemini/antigravity/scratch/1995lido_youtube_management")
import youtube_api_auto_uploader as uploader

shorts = [
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_01_Nghe_Khi_Mat_Ngu.mp4",
        "title": "Mất Ngủ, Tâm Bất An? Nghe 20 Giây Này Tâm Tự Khắc Bình Yên #Shorts",
        "description": "Nếu bạn đang trằn trọc mất ngủ hoặc nhiều âu lo, hãy bấm vào nút \"Video liên quan\" ngay bên dưới để lắng nghe trọn vẹn bản hòa tấu thiền định 50 phút đưa vào giấc ngủ sâu nhé! 🙏🌿\n\n👉 Nghe trọn bộ 50 phút tại: https://www.youtube.com/watch?v=dCugzxszCJc\n#nhacthien #ngungon #chualanh #loiphatday #thaoduongtv #432hz #shorts",
        "tags": ["nhac thien", "mat ngu", "nhac ngu ngon", "thien dinh", "chua lanh", "thaoduongtv", "shorts"]
    },
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_02_Tieng_Mua_Ranh_Roi_Tam_Tri.mp4",
        "title": "Mệt Mỏi Thì Buông Xả: Tiếng Mưa Thiền Định Xoa Dịu Mọi Nỗi Đau #Shorts",
        "description": "Gột rửa mọi muộn phiền hôm nay cùng tiếng mưa rơi tĩnh lặng. Bấm vào nút \"Video liên quan\" bên dưới để nghe bản đầy đủ 50 phút giúp thư giãn và ngủ ngon trọn đêm.\n\n👉 Nghe trọn bộ 50 phút tại: https://www.youtube.com/watch?v=dCugzxszCJc\n#nhacthien #tiengmua #buongxamuonphien #chualanh #thaoduongtv #shorts",
        "tags": ["tieng mua roi", "nhac thien mua", "buong bo muon phien", "tam an", "thaoduongtv", "shorts"]
    },
    {
        "file": "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/Short_03_Chuong_Chua_Tinh_Tam.mp4",
        "title": "Tiếng Chuông Thức Tỉnh: Tâm An Thì Vạn Sự Tự Nhiên An #Shorts",
        "description": "Mỗi tiếng chuông ngân là một niệm buông bỏ. Dành 50 phút tĩnh tâm cùng lời Phật dạy và hòa tấu chuông xoay Tây Tạng tại nút \"Video liên quan\" bên dưới bạn nhé!\n\n👉 Nghe trọn bộ 50 phút tại: https://www.youtube.com/watch?v=dCugzxszCJc\n#tiengchuongchua #taman #kinhnikaya #loiphatday #thaoduongtv #shorts",
        "tags": ["tieng chuong chua", "nhac thien phat giao", "loi phat day", "tam an van su an", "thaoduongtv", "shorts"]
    }
]

results = []
log_file = "/Users/abc/Documents/KenhYTB/nhacthien_long/shorts_promo/upload_results.json"

for idx, item in enumerate(shorts, 1):
    print(f"\n==================== [TẬP {idx}/3] ====================")
    vid_id = uploader.upload_video_via_api(
        video_path=item["file"],
        title=item["title"],
        description=item["description"],
        tags=item["tags"]
    )
    if vid_id:
        url = f"https://youtube.com/shorts/{vid_id}"
        edit_url = f"https://studio.youtube.com/video/{vid_id}/edit"
        results.append({
            "index": idx,
            "title": item["title"],
            "video_id": vid_id,
            "shorts_url": url,
            "edit_url": edit_url,
            "time": datetime.now().isoformat()
        })
        print(f"✅ ĐÃ ĐĂNG THÀNH CÔNG TẬP {idx}: {url}")
    else:
        print(f"❌ THẤT BẠI TẬP {idx}")
    time.sleep(3)

with open(log_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n🎉 HOÀN TẤT ĐĂNG TẢI TRỌN BỘ 3 SHORTS!")
