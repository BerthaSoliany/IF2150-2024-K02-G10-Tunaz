import datetime
import time
import os
import sqlite3
from win11toast import toast

def notification(target_datetime, notification_message):
    icon = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../img/logo_tunaz2.png'))

    while True:
        current_datetime = datetime.datetime.now()
        current_time_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        if current_time_str == target_datetime:
            toast('Reminder Tunaz', notification_message, icon=icon)
            break
        time.sleep(1)

# Fungsi untuk mendapatkan notifikasi yang waktunya sudah tiba
def get_notifications_to_trigger(cursor):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = "SELECT id, notify_time, message FROM notifications WHERE notify_time <= ? AND notify_time != 'triggered'"
    cursor.execute(query, (current_time,))
    return cursor.fetchall()

# Fungsi untuk menandai notifikasi yang sudah ditampilkan
def mark_notification_as_triggered(cursor, notification_id):
    query = "UPDATE notifications SET notify_time = 'triggered' WHERE id = ?"
    cursor.execute(query, (notification_id,))

# Main function
def main():
    # Koneksi ke database
    connection = sqlite3.connect('notifications.db')
    cursor = connection.cursor()

    print("Menunggu notifikasi...")
    while True:
        # Periksa notifikasi yang waktunya sudah tiba
        notifications = get_notifications_to_trigger(cursor)
        
        for notif_id, notify_time, message in notifications:
            # Tampilkan notifikasi menggunakan fungsi notification
            notification(notify_time, message)
            
            # Tandai sebagai ditampilkan
            mark_notification_as_triggered(cursor, notif_id)
        
        # Simpan perubahan ke database
        connection.commit()

        # Tunggu sebelum memeriksa lagi (dalam detik)
        time.sleep(5)

if __name__ == "__main__":
    main()