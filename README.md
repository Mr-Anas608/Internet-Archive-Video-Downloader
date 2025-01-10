# Internet Archive Video Downloader

A simple Python script to download videos from Internet Archive using web scraping.

## Features
- Automatically finds video URLs from Internet Archive pages
- Shows download progress bar
- Handles errors gracefully
- Uses random user agents for better reliability

## Requirements
```
selenium
webdriver_manager
requests
tqdm
```

## Installation
1. Clone this repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```
   python main.py
   ```
2. Enter the Internet Archive URL when prompted
3. The video will download to the current directory as 'downloaded_video.mp4'

## Notes
- Only works with Internet Archive URLs (https://archive.org/...)
- Currently supports MP4 videos only
- Requires Chrome browser to be installed

## Author
[Your Name]
[Your Contact Info/Portfolio]