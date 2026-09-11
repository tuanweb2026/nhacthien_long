# 🌿 HỆ THỐNG TỰ ĐỘNG HÓA SẢN XUẤT & TỐI ƯU KÊNH YOUTUBE NHẠC THIỀN TRIỆU VIEW
### Kênh: Thảo Dương TV (@1995lido) · Mục tiêu: Bật Kiếm Tiền (4.000 Giờ Xem & 1.000 Subscribers)

---

## 📖 GIỚI THIỆU DỰ ÁN
Dự án được xây dựng dựa trên phân tích chuyên sâu từ video hướng dẫn phát triển kênh YouTube mới ([CkHXh59lkyc](https://www.youtube.com/watch?v=CkHXh59lkyc)). Hệ thống giải quyết bài toán:
* **Tạo "Nam Châm Giờ Xem" (Pillar Video):** Sản xuất chuỗi video hòa tấu thiền định Phật giáo dài 50 phút với âm nhạc độc quyền từ Musful AI, tối ưu hóa theo chu kỳ sinh học giấc ngủ để thính giả bật nghe qua đêm.
* **Xây Dựng Phễu Chuyển Đổi Shorts $\rightarrow$ Video Dài:** Tự động cắt trích đoạn cao trào hay nhất (~20s), phủ nền mờ 9:16 (1080x1920) kèm chữ kêu gọi hành động để kéo traffic từ Shorts Feed trực tiếp vào video dài thông qua tính năng *Video liên quan (Related Video)*.
* **Tự Động Hóa Xuất Bản & Lên Lịch Giờ Vàng (Drip Release):** Tự động tải lên, tối ưu SEO On-Page và hẹn giờ công khai tự động trên YouTube Data API v3.

---

## 📂 CẤU TRÚC DỰ ÁN

```text
nhacthien_long/
├── CAM_NANG_SAN_XUAT_VIDEO_THIEN_TRIEU_VIEW.md   # Quy trình chuẩn SOP toàn diện từ A-Z
├── BAO_CAO_LICH_DANG_6_VIDEO.md                  # Báo cáo tiến trình 6 video phát hành nhỏ giọt
├── METADATA_VIDEO_DAO_NGUOC_50PHUT.md            # Bộ siêu dữ liệu SEO cho video 50p đảo ngược
│
├── 🛠️ BỘ CÔNG CỤ TỰ ĐỘNG HÓA (PYTHON):
│   ├── render_long_video.py                      # Ghép nối video 50 phút thuận (Bài 1 -> Bài 3)
│   ├── render_reverse_50min.py                   # Ghép nối video 50 phút nghịch (Bài 6 -> Bài 1)
│   ├── render_3_shorts_pil.py                    # Dựng 3 video Shorts promo 20s (9:16 Full HD)
│   ├── render_5_shorts.py                        # Dựng 5 video Shorts promo khung giờ vàng
│   ├── create_thumb_bai4.py                      # Thiết kế Thumbnail nổi khối chuẩn Mobile qua PIL
│   ├── upload_3_shorts.py                        # Tự động upload 3 Shorts + tự động comment link
│   ├── upload_5_scheduled_shorts.py              # Tự động upload & đặt lịch phát 5 khung giờ vàng
│   ├── upload_6_standalone_videos.py             # Tự động upload 6 video hòa tấu riêng lẻ (Private)
│   └── schedule_6_videos.py                      # Đặt lịch công khai tự động cách nhau 10 phút
│
├── 🎨 THUMBNAILS & DỮ LIỆU ĐỒ HỌA:
│   ├── Thumbnail_TamAn_NguNgon.jpg               # Thumbnail video 50 phút đầu tiên
│   ├── Thumbnail_Thien_Dao_Nguoc_50Phut.jpg      # Thumbnail video 50 phút đảo ngược
│   ├── Thumbnail_Bai4_432Hz_TamAn.jpg            # Thumbnail bài 4 (432Hz Chữa Lành)
│   └── shorts_promo/                             # Thư mục chứa video Shorts & metadata đăng tải
│
└── .gitignore                                    # Loại trừ các file video/audio nặng (>100MB)
```

---

## 🎵 THƯ VIỆN PROMPT MUSFUL AI (CHU KỲ SINH HỌC 6 GIAI ĐOẠN)

Hệ thống âm nhạc được thiết kế dựa trên chu trình thư giãn tự nhiên của não bộ:
1. **Bài 1 (00:00):** *Thiền Sâu & Giấc Ngủ (Deep Sleep)* — Sáo trúc Shakuhachi & Chuông xoay Tây Tạng.
2. **Bài 2 (08:47):** *Chánh Niệm & Chữa Lành Lo Âu* — Tiếng mưa rơi tĩnh lặng & Piano 528Hz.
3. **Bài 3 (17:16):** *Kinh Điển & Tĩnh Lặng Trí Tuệ* — Chuông chùa ngân nga & Đàn tranh tối giản.
4. **Bài 4 (25:02):** *Hòa Tấu Nuôi Dưỡng Tâm An* — Tần số 432Hz xoa dịu thần kinh, phục hồi năng lượng.
5. **Bài 5 (33:49):** *Mưa Đêm Thanh Lọc Năng Lượng Tiêu Cực* — Mưa đêm trên mái ngói cổ & chuông đồng.
6. **Bài 6 (42:19):** *Bình Yên Tự Tại & Chìm Sâu Vào Giấc Ngủ* — Sóng não Delta đưa vào giấc ngủ say.

*(Xem chi tiết prompt tiếng Anh trong file [CAM_NANG_SAN_XUAT_VIDEO_THIEN_TRIEU_VIEW.md](./CAM_NANG_SAN_XUAT_VIDEO_THIEN_TRIEU_VIEW.md)).*

---

## 🚀 HƯỚNG DẪN VẬN HÀNH NHANH

### 1. Dựng video dài 50 phút từ các file mp4 con:
```bash
python3 render_reverse_50min.py
```

### 2. Trích xuất video Shorts quảng cáo (20s) chuẩn 9:16:
```bash
python3 render_5_shorts.py
```

### 3. Tự động tải lên & lên lịch phát sóng tự động:
```bash
# Upload 5 Shorts theo khung giờ vàng trong ngày
python3 upload_5_scheduled_shorts.py

# Đặt lịch phát sóng nhỏ giọt cách nhau 10 phút
python3 schedule_6_videos.py
```

---

## 📈 CHIẾN LƯỢC ĐẠT 4.000 GIỜ XEM & 1.000 SUBSCRIBERS
* **Shorts làm phễu:** Dùng để kéo subscriber và tạo luồng xem tò mò nhờ tỷ lệ giữ chân cao (>120%).
* **Tính năng "Related Video":** Gắn link video dài 50 phút trực tiếp vào các video Shorts triệu view để chuyển đổi người lướt ngắn thành người nghe dài.
* **Thời điểm xuất bản vàng:** Tập trung các video dài vào **20:30 - 21:00 tối** để đón trọn lượng khán giả nghe nhạc đi ngủ, tích lũy hàng ngàn giờ xem tự động mỗi đêm.

---
© 2026 **Thảo Dương TV (@1995lido)**. All rights reserved.
