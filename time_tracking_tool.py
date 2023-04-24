#!/usr/bin/python3.10

from PIL import Image
from pystray import Icon, Menu, MenuItem
import threading
import spread_sheet
import monitor


monitor_state = False


def monitoring():
    global monitor_state
    monitor_state = not monitor_state

    config = spread_sheet.get_config()
    program_name = config['program_name']

    if monitor_state:
        monitoring_thread = threading.Thread(
            target=monitor.monitoring_instance,
            args =[program_name, lambda: monitor_state]
        )
        monitoring_thread.start()


def show_info():
    spread_sheet.show_notification(
        'For more information visit:\n'
        'https://github.com/pigYDoe/Time-Tracking-Tool'
    )


def exit_program(icon):
    icon.visible = False
    icon.stop()


def create_icon():
    manual_menu = Menu(
        MenuItem(
            '\u23F3 Clocking In',
            spread_sheet.write_start_time
        ),
        MenuItem(
            '\u231B Clocking Out',
            spread_sheet.write_end_time
        ),
    )

    main_menu = Menu(
        MenuItem(
            '\U0001F5A5 Automatic Tracking',
              monitoring,
              checked=lambda item: monitor_state
        ),
        MenuItem(
            '\U0001F590 Manual Tracking',
            manual_menu
        ),
        MenuItem(
            '\U0001F4D3 Info',
            show_info
        ),
        MenuItem(
            '\U0001F50C Exit',
            exit_program
        )
    )

    config = spread_sheet.get_config()
    image = Image.open(config['icon_path'])

    icon = Icon(
        'name',
        image,
        'Time Tracking Tool',
        main_menu
    )

    return icon


def run():
    icon = create_icon()
    icon.run()


if __name__ == "__main__":
    run()
