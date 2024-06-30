import random
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz
import asyncio
import os

# اطلاعات مورد نیاز
api_id = 26177429
api_hash = '672e9234b7c0013b7bdf0c856cf989e6'
string_session = '1BJWap1sBu41vUSHjVu9ajTHlRa9TZIVBB2vL_Qn_XEgDFwN8gp1zFydngsNqQ96foQTZzGlKYnSxQrozcrBx3oFzN5vc_S5-sWmf1tMJxTKNQGFj2P1Vq5_JP2IvFjk07e_4lecE3lLlivfmJ5ZHHJZbFqfC9coA5rL7DDZDlSt_8a5nyyoaq9tjf_V2GfcsE3-lw7kEWs9JHpWdA3E_2-9qIJPm-fvMll2u_hkNqIEoMUz9EddNofv3ZdTE0SehBy5IHjaq1hA-PiYgrYEqYDQSBuu9jbEPx4z47F_NM7Cf0N0wBtQUq5a5EBod_pcNDNhrZzK980c2nA7HMAtElf5bUHdCxNk='

# لیست استیکرها
stickers = ['🌁', '🌉', '🌄', '🌇', '🌆', '🏙', '🌃', '🏞', '🌅']

# ایجاد کلاینت
current_dir = os.path.dirname(os.path.abspath(__file__))  # مسیر کنونی اسکریپت
session_file = os.path.join(current_dir, 'session.sqlite')  # مسیر فایل پایگاه داده

client = TelegramClient(session_file, api_id, api_hash)

def format_time(time_str, font_numbers):
    return ''.join(font_numbers[char] if char in font_numbers else char for char in time_str)

async def update_profile_name():
    # نام اولیه را به "Amirzxr" تنظیم می‌کنیم
    initial_name = "Amirzxr"
    await client(UpdateProfileRequest(first_name=initial_name))
    
    while True:
        # دریافت زمان دقیق ایران
        iran_tz = pytz.timezone('Asia/Tehran')
        current_time = datetime.now(iran_tz).strftime('%H:%M')
        
        # اعداد با فونت دلخواه
        font_numbers = {
            '0': '𝟬',
            '1': '𝟭',
            '2': '𝟮',
            '3': '𝟯',
            '4': '𝟰',
            '5': '𝟱',
            '6': '𝟲',
            '7': '𝟳',
            '8': '𝟴',
            '9': '𝟵'
        }
        
        formatted_time = format_time(current_time, font_numbers)
        
        # انتخاب استیکر به صورت تصادفی
        sticker = random.choice(stickers)
        
        # به‌روزرسانی نام
        new_name = f"{initial_name} {formatted_time} {sticker}"
        await client(UpdateProfileRequest(first_name=new_name))
        
        # صبر به مدت ۳۰ ثانیه
        await asyncio.sleep(30)

with client:
    client.loop.run_until_complete(update_profile_name())
