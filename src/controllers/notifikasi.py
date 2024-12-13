import datetime
import time
import locale
import os
from winotify import Notification, audio

def notification(target_datetime, title, duration="long"):
    icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../img/logo_tunaz2.png'))
    locale.setlocale(locale.LC_TIME, 'id_ID')  # menggunakan bahasa Indonesia
    
    while True:
        current_datetime = datetime.datetime.now()
        current_time_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        day_of_week = current_datetime.strftime('%A')
        
        if current_time_str == target_datetime:
            notification_message = f"{day_of_week}, {current_datetime.strftime('%H:%M:%S')}."
            notif = Notification(
                app_id="Reminder Tunaz",
                title=title,
                msg=notification_message,
                duration=duration,
                icon=icon_path,
            )
            notif.set_audio(audio.Reminder, loop=True)  # Pilihan Audio: Default, Mail, NewMail, SMS, Reminder
            notif.show()
            break
        time.sleep(1)  # Tidur selama 1 detik sebelum memeriksa lagi


# Contoh penggunaan:
target_datetime = "2024-12-12 15:43:00"  # format 'YYYY-MM-DD HH:MM:SS'
notification_title = "Siram Jagung 001"
notification(target_datetime, notification_title)