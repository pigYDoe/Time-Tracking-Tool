import spread_sheet
import time
import psutil


def monitoring_instance(program_name, active_flag):
    program_running = False

    while active_flag():
        for process in psutil.process_iter(['name']):
            if process.info['name'] == program_name:
                if not program_running:
                    program_running = True
                    spread_sheet.write_start_time()
                break
        else:
            if program_running:
                program_running = False
                spread_sheet.write_end_time()

        time.sleep(1)

