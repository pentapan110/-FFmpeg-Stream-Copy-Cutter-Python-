# FFmpeg Stream Copy Cutter (Python)

A simple Python script that automates cutting long videos using FFmpeg stream copy (`-c copy`).

Instead of manually rewriting FFmpeg commands every time, you only need to provide timestamps, and the script will generate and execute the correct commands to export multiple video segments quickly.

This tool is useful for cutting long recordings, livestream videos, and raw footage without re-encoding.

---

## Features

- Cut videos by timestamps automatically
- Uses FFmpeg stream copy (`-c copy`) for fast cutting (no re-encoding)
- No quality loss (original video/audio streams are copied)
- Automatically inserts `00:00:00` if the first timestamp is missing
- Outputs multiple segments in order

---

## Requirements

- Python 3.8+
- FFmpeg installed and added to PATH

Check your installation:

```bash
python --version
ffmpeg -version

Installation

Clone this repository:
git clone https://github.com/yourname/yourrepo.git
cd yourrepo

(Optional) Create a virtual environment:
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows

Usage
Run the script:
python main.py

You will be asked to input:
Input video path (must include extension, e.g. .mp4)
Output name prefix
Timestamps (HH:MM:SS)
The script will automatically generate FFmpeg commands and export multiple segments.

Example
Input
Example timestamps:
00:10:00
00:25:30
00:40:12
Even if you do not provide 00:00:00, the script will automatically insert it.

Output
The script will export:
output_0.mp4 (00:00:00 ~ 00:10:00)
output_1.mp4 (00:10:00 ~ 00:25:30)
output_2.mp4 (00:25:30 ~ 00:40:12)
output_3.mp4 (00:40:12 ~ end of video)

Notes / Important Information
1. Stream Copy Cutting Is Not Frame Accurate
This tool uses FFmpeg stream copy mode:
-c copy
That means cutting is usually fast, but the output may not be frame-perfect, because FFmpeg may cut at the nearest keyframe.
If you need frame-accurate cutting, you must re-encode.




2. Input Timestamp Format
Timestamps must follow this format:
HH:MM:SS
Example:
02:15:30

3. Output File Naming
Output files are generated automatically in order, for example:
output_0.mp4
output_1.mp4
output_2.mp4

4. Large Files
This script is designed for long videos and large files, where manual command editing is time-consuming.


How It Works

This script builds FFmpeg commands like:
ffmpeg -i input.mp4 -ss 00:10:00 -to 00:25:30 -c copy output_1.mp4
Each segment is exported one by one until the last timestamp, and the last segment is automatically cut until the end of the video.

Roadmap / Future Improvements

Possible future features:

Load timestamps from a .txt file
Batch processing for multiple videos
Add GUI interface (Tkinter / PyQt)
Add better input validation and error handling
Add --dry-run mode (print FFmpeg commands without executing)
