import os
from PIL import Image, ImageDraw, ImageFont

bg_path = "/Users/abc/.gemini/antigravity/brain/5cc44281-930c-4493-be5b-fc6b34ea201d/bg_bai4_432hz_1789147577569.jpg"
out_path = "/Users/abc/Documents/KenhYTB/nhacthien_long/Thumbnail_Bai4_432Hz_TamAn.jpg"
font_path = "/Library/Fonts/Arial Unicode.ttf"

img = Image.open(bg_path).convert("RGBA")
W, H = img.size

# Subtle dark gradient on left
gradient = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_grad = ImageDraw.Draw(gradient)
for x in range(int(W * 0.52)):
    alpha = int(130 * (1 - x / (W * 0.52)))
    draw_grad.line([(x, 0), (x, H)], fill=(0, 0, 0, alpha))

img = Image.alpha_composite(img, gradient)

text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(text_layer)

font_main = ImageFont.truetype(font_path, int(H * 0.13))
font_badge = ImageFont.truetype(font_path, int(H * 0.08))

text1 = "TÂM AN"
text2 = "PHỤC HỒI"
badge = "432Hz CHỮA LÀNH"

x = int(W * 0.08)
y1 = int(H * 0.18)
y2 = y1 + int(H * 0.13 * 1.15)
y_badge = y2 + int(H * 0.13 * 1.25)

def draw_styled(draw_c, pos, text, font, fill, shadow=(0, 0, 0, 240)):
    px, py = pos
    for dx in range(-4, 5):
        for dy in range(-4, 5):
            if dx != 0 or dy != 0:
                draw_c.text((px + dx, py + dy), text, font=font, fill=shadow)
    draw_c.text((px, py), text, font=font, fill=fill)

# TÂM AN (Vàng hoàng kim dịu mắt)
draw_styled(draw, (x, y1), text1, font_main, (255, 240, 160, 255))
# PHỤC HỒI (Trắng tinh khôi)
draw_styled(draw, (x, y2), text2, font_main, (255, 255, 255, 255))

# 432Hz Badge Box
bbox = draw.textbbox((0, 0), badge, font=font_badge)
bw = bbox[2] - bbox[0]
bh = bbox[3] - bbox[1]
draw.rounded_rectangle([x - 15, y_badge - 10, x + bw + 20, y_badge + bh + 15], radius=12, fill=(180, 130, 20, 220), outline=(255, 240, 180, 255), width=3)
draw.text((x, y_badge), badge, font=font_badge, fill=(255, 255, 255, 255))

final_img = Image.alpha_composite(img, text_layer).convert("RGB")
final_img.save(out_path, "JPEG", quality=95)
print("Saved custom thumbnail to:", out_path)
