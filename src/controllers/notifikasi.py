import sys
import os
import datetime
import time
import sqlite3
from win11toast import toast

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.controllers.jadwalperawatancontroller import JadwalPerawatanController

def notification(target_datetime, notification_message):
    icon = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../img/logo_tunaz2.png'))

    while True:
        current_datetime = datetime.datetime.now()
        current_time_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        if current_time_str == target_datetime:
            toast('Reminder Tunaz', notification_message, icon=icon)
            break
        time.sleep(1)

# Refactored main function into show_notification
def show_notification():
    connection = sqlite3.connect('src/database/tunaz.db')
    cursor = connection.cursor()

    print("Menunggu notifikasi...")
    while True:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        jadwal_perawatan_controller = JadwalPerawatanController()
        perawatan_list = jadwal_perawatan_controller.get_all_jadwal_perawatan_by_date(current_date)
        
        for row in perawatan_list:
            notif_id = row[0]
            notify_time = row[5]
            jenis_perawatan = row[6]
            jenis_tanaman = row[1]
            index_tanaman = row[2]
            pilihan_notifikasi = row[7]
            
            if pilihan_notifikasi:
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if notify_time == current_time:
                    message = f"{jenis_perawatan} {jenis_tanaman} {index_tanaman}"
                    notification(notify_time, message)
                    
                    print(f"Notifikasi '{message}' ditampilkan pada {current_time}")
        
        time.sleep(1)