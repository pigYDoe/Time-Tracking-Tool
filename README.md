# ⏲️Time-Tracking-Tool
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pigYDoe/Time-Tracking-Tool/blob/main/LICENSE)

It's a simple time tracking tool for the purpose to clock in and out your working time.

## How To ... ?

### Setup 

1. Create a `config.json` file in the same directory as the Time-Tracking-Tool.
2. Add the following configurations to the config.json file:
   * Path to the working time spread sheet ( `.ods` file format)
   * Path to the icon for the Time-Tracking-Tool
   * Name of the program to monitor for automatic clocking

Here's an example of a `config.json` file:
````json
{
    "file_path": "C:/time_tracking/working_time.ods",
    "icon_path": "C:/time_tracking/stopwatch.png",
    "program_name": "thunderbird.exe"
}

````
### Spreadsheet Design

Design the spreadsheet with the following columns:

| date [A1] | clocking in [B1] | clocking out [C1] |
|------|-------------|--------------|
| 01.04.23 |
| **.**  **.**  **.**|
| 30.04.23 |

### Usage

#### Automatic Tracking

![image](https://user-images.githubusercontent.com/103217539/232341225-869e3316-1540-42e6-b125-0b3475d090a9.png)

1. Run the Time-Tracking-Tool.
2. Activate Automatic Tracking.
3. The tool will monitor the specified program (e.g., `thunderbird.exe`).
4. When the program is active, the tool will automatically clock in and update the correspondig column in the spreadsheet
5. When the program is closed, the tool will automatically clock out and update the correspondig column in the spreadsheet

#### Manual Tracking

![image](https://user-images.githubusercontent.com/103217539/232341229-7400465c-b169-49e5-ac2a-02d60706a101.png)

1. Run the Time-Tracking-Tool.
2. Clock In/Out as you like, the tool will automatically update the correspondig column in the spreadsheet.

#### Exit

Quits the program.


<a href="https://www.flaticon.com/free-icons/time" title="time icons">Time icons created by Freepik - Flaticon</a>
