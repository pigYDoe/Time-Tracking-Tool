import time_tracking as tt
import time
import psutil

class MonitorProgram:
    def __call__(self, program_name, file_path, matched_index, active_flag):
        program_running = False

        while active_flag():
            for process in psutil.process_iter(['name', 'create_time']):
                if process.info['name'] == program_name:
                    if not program_running:
                        program_running = True
                        tt.log_start_time(file_path, matched_index)
                    break
            else:
                if program_running:
                    program_running = False
                    tt.log_end_time(file_path, matched_index)

            time.sleep(1)

monitoring_instance = MonitorProgram()
