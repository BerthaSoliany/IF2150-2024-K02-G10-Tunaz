import datetime
import time
import locale
from winotify import Notification, audio

def notification(target_datetime, title, duration="long"):
    locale.setlocale(locale.LC_TIME, 'id_ID') #menggunakan bahasa indonesia
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
                icon="./img/logo_tunaz2.png"
            )
            notif.set_audio(audio.Reminder, loop=True)
            notif.show()
            break
        time.sleep(1)  # Sleep for 1 second before checking again


target_datetime = "2024-12-12 00:05:00" #format 'YYYY-MM-DD HH:MM:SS'
notification_title = "Siram Jagung 001"
notification(target_datetime, notification_title)
