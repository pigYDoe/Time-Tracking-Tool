from datetime import datetime
from plyer import notification
import ezodf
import json
import os


def get_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.json')

    with open(config_path, 'r') as file:
        config = json.load(file)
    return config


def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')


def convert_time_format(time_obj):
    output_format = 'PT%HH%MM%SS,0000S'
    return time_obj.strftime(output_format)


def show_notification(message):
    notification.notify(
        title='Time Tracking Tool',
        message=message,
        timeout=5,
    )


def get_index(file_path, current_date):
    doc = ezodf.opendoc(file_path)
    sheet = doc.sheets[-1]

    for index, row in enumerate(sheet.rows(), start=0):
        if index == 0:
            continue
        date_in_column = row[0].value
        if date_in_column is None:
            break

        if date_in_column == current_date:
            return index

    show_notification('\u26D4 No date index matched: check your spread sheet!')
    return None


def write_start_time():
    start_time = datetime.now()
    current_date = get_current_date()
    config = get_config()
    file_path = config['file_path']
    index = get_index(file_path, current_date)

    doc = ezodf.opendoc(file_path)
    sheet = doc.sheets[-1]

    if start_time:
        if sheet[index, 1].value == None:
            show_notification(f'\U0001F916 Clocking In: {start_time}')
            start_time_obj = convert_time_format(start_time)
            sheet[index, 1].set_value(start_time_obj, 'time')
            doc.save()
        else:
            show_notification(f'\u26D4 Already Clocked In: {sheet[index, 1].value}')


def write_end_time():
    end_time = datetime.now()
    current_date = get_current_date()
    config = get_config()
    file_path = config['file_path']
    index = get_index(file_path, current_date)

    doc = ezodf.opendoc(file_path)
    sheet = doc.sheets[-1]

    if end_time:
        if sheet[index, 2].value == None:
            show_notification(f'\U0001F916 Clocking Out: {end_time}')
            end_time_obj = convert_time_format(end_time)
            sheet[index, 2].set_value(end_time_obj, 'time')
            doc.save()
        else:
            show_notification(f'\u26D4 Already Clocked Out: {sheet[index, 2].value}')

