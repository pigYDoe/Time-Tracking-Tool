# ⏲️Time-Tracking-Tool
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pigYDoe/Time-Tracking-Tool/blob/main/LICENSE)

It's a simple time tracking tool for the purpose to clock in and out your working time.

## How To ... ?

### Setup

1. Clone the repository or download it as archive
2. Install the required Python packages with:

        pip install -r requirements.txt

3. Adjust the configuration in the `config.json` file:
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
| `%Y-%m-%d` |

### Usage

#### Automatic Tracking

![time_tracking_tool_autojpeg](https://user-images.githubusercontent.com/103217539/235324180-cdeda263-e6d6-4fe3-8849-49def6ab4661.jpeg)

1. Run the Time-Tracking-Tool.
2. Activate Automatic Tracking.
3. Upon detecting the specified program (e.g., `thunderbird.exe`), the tool begins monitoring.
4. The tool will automatically clock in when the program is active and clock out when closed.
5. During clock-in and clock-out events, the corresponding column/row in the spreadsheet will be updated.

#### Manual Tracking

![time_tracking_tool_man](https://user-images.githubusercontent.com/103217539/235324219-d5e5d1c7-44a5-4304-b99e-70cea1623e69.jpeg)

1. Run the Time-Tracking-Tool.
2. Clock in/out as you like, the tool will automatically update the correspondig column/row in the spreadsheet.

#### Info

Link to repository.

#### Exit

Quits the program.


<a href="https://www.flaticon.com/free-icons/time" title="time icons">Time icons created by Freepik - Flaticon</a>
