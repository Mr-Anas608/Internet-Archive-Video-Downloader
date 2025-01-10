from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import subprocess
import time

def download_video(url):
    try:
        # Setup Chrome options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        
        # Initialize browser
        service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=options)
        driver = webdriver.Chrome(options=options)
        
        print("\nSearching for video...")
        driver.get(url)
        time.sleep(3)

        # Get all network requests
        network_requests = driver.execute_script("""
            var resources = window.performance.getEntriesByType("resource");
            return resources.map(function(r) { return r.name; });
        """)
        
        # Find video links
        video_links = [link for link in network_requests if link.endswith("mp4")]
        driver.quit()

        if not video_links:
            print("\nNo MP4 video found at this URL")
            return False

        video_link = video_links[0]
        print("Video found! Starting download...")

        # Download using yt-dlp through subprocess
        try:
            subprocess.run(['yt-dlp', video_link], check=True)
            print("\nVideo downloaded successfully!")
            return True
        except subprocess.CalledProcessError:
            print("\nFailed to download with yt-dlp. Make sure yt-dlp is installed.")
            print("Install it using: pip install yt-dlp")
            return False

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    url = input("\nEnter Internet Archive URL: ").strip()
    if not url.startswith("https://archive.org"):
        print("Please enter a valid Internet Archive URL (https://archive.org/...)")
    else:
        download_video(url)