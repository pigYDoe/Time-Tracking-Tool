#!/usr/bin/python3.10

from PIL import Image
import pystray
import threading
import time_tracking as tt
import monitor_program as mp

monitor_state = False
monitoring_active = False

def work_start_time():
    config = tt.load_config()
    file_path = config['file_path']
    current_date = tt.get_current_date()
    matched_index = tt.compare_dates(file_path, current_date)
    tt.log_start_time(file_path, matched_index)

def work_end_time():
    config = tt.load_config()
    file_path = config['file_path']
    current_date = tt.get_current_date()
    matched_index = tt.compare_dates(file_path, current_date)
    tt.log_end_time(file_path, matched_index)

def monitoring_instance_wrapper():
    global monitoring_active
    monitoring_active = True
    config = tt.load_config()
    program_name = config['program_name']
    file_path = config['file_path']
    current_date = tt.get_current_date()
    matched_index = tt.compare_dates(file_path, current_date)
    mp.monitoring_instance(program_name, file_path, matched_index, lambda: monitoring_active)
    
def monitoring(item):
    global monitor_state, monitoring_active
    monitor_state = not monitor_state
    item.checked = monitor_state

    if monitor_state:
        monitoring_thread = threading.Thread(target=monitoring_instance_wrapper, daemon=True)
        monitoring_thread.start()
    else:
        monitoring_active = False
        
def info_program():
    tt.show_notification(
        '\U0001F4D3 Setup through a config.json within \n the same directory as the tool.'
        )
        
def exit_program(icon):
    icon.visible = False
    icon.stop()

def create_icon():
    config = tt.load_config()
    image = Image.open(config['icon_path'])

    manual_menu = pystray.Menu(
        pystray.MenuItem('\u23F3 Clocking In', work_start_time),
        pystray.MenuItem('\u231B Clocking Out', work_end_time)
        )
    
    main_menu = pystray.Menu(
        pystray.MenuItem('\U0001F5A5 Automatic Tracking', monitoring, checked=lambda item: monitor_state),
        pystray.MenuItem('\U0001F590 Manual Tracking', manual_menu),
        pystray.MenuItem('\U0001F4D3 Info', info_program),
        pystray.MenuItem('\U0001F50C Exit', exit_program)
        )
    
    icon =  pystray.Icon('name', image, 'Time Tracking Tool', main_menu)

    return icon

def run():
    icon = create_icon()
    icon.run()

if __name__ == "__main__":
    run()
