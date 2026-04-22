#!/usr/bin/env python3
"""
YouTube Playlist to MP3 Downloader
Downloads all songs from a YouTube playlist as MP3 files
"""

import os
import sys
import subprocess
from yt_dlp import YoutubeDL

def get_ffmpeg_path():
    """Get FFmpeg path - bundled (PyInstaller) or system"""
    # When bundled with PyInstaller, binaries are in sys._MEIPASS
    if hasattr(sys, '_MEIPASS'):
        bundle_dir = sys._MEIPASS
        ffmpeg_name = 'ffmpeg.exe' if sys.platform == 'win32' else 'ffmpeg'
        bundled_path = os.path.join(bundle_dir, ffmpeg_name)
        if os.path.exists(bundled_path):
            return bundled_path
    # Fall back to system FFmpeg
    return 'ffmpeg'

def check_ffmpeg():
    """Check if ffmpeg is available (bundled or system)"""
    ffmpeg_path = get_ffmpeg_path()
    try:
        subprocess.run([ffmpeg_path, '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def download_playlist_as_mp3(playlist_url, output_path="downloads"):
    """
    Download all songs from a YouTube playlist as MP3 files.

    Args:
        playlist_url: The full YouTube playlist URL
        output_path: Directory where MP3 files will be saved (default: "downloads")
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"[✓] Created output directory: {output_path}")

    ffmpeg_path = get_ffmpeg_path()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'quiet': False,
        'no_warnings': False,
        'extract_flat': False,
        'progress_hooks': [progress_hook],
        'ffmpeg_location': os.path.dirname(ffmpeg_path) if ffmpeg_path != 'ffmpeg' else None,
    }

    # Remove None values
    ydl_opts = {k: v for k, v in ydl_opts.items() if v is not None}

    try:
        print(f"\n[✓] Starting download from playlist")
        print(f"[✓] Saving MP3 files to: {output_path}")
        print("-" * 60)

        with YoutubeDL(ydl_opts) as ydl:
            print("[INFO] Fetching playlist information...")
            playlist_info = ydl.extract_info(playlist_url, download=False)

            if 'entries' in playlist_info:
                video_count = len(playlist_info['entries'])
                print(f"[INFO] Found {video_count} videos in playlist")
                print(f"[INFO] Playlist: {playlist_info.get('title', 'Unknown')}")

            print("\n[INFO] Downloading...\n")
            ydl.download([playlist_url])

        print("-" * 60)
        print(f"[✓] Download completed successfully!")
        print(f"[✓] Files saved in: {os.path.abspath(output_path)}")

    except Exception as e:
        print(f"[✗] An error occurred: {str(e)}")
        sys.exit(1)

def progress_hook(d):
    """Show download progress"""
    if d['status'] == 'downloading':
        if '_percent_str' in d:
            print(f"\r[DOWNLOADING] {d['_percent_str']} complete at {d.get('_speed_str', 'N/A')}", end='')
    elif d['status'] == 'finished':
        print(f"\n[✓] Finished downloading, now converting to MP3...")

def main():
    print("=" * 60)
    print(" YouTube Playlist to MP3 Downloader")
    print("=" * 60)

    if not check_ffmpeg():
        print("\n[✗] FFmpeg not found!")
        print("\nPlease install FFmpeg:")
        print("  • Ubuntu/Debian: sudo apt-get install ffmpeg")
        print("  • Mac: brew install ffmpeg")
        print("  • Windows: Download from https://ffmpeg.org")
        sys.exit(1)
    else:
        ffmpeg_path = get_ffmpeg_path()
        if hasattr(sys, '_MEIPASS'):
            print("[✓] Using bundled FFmpeg")
        else:
            print(f"[✓] FFmpeg found: {ffmpeg_path}")

    print("\n[?] Enter your YouTube playlist URL:")
    playlist_url = input("> ").strip()

    if not playlist_url:
        print("[✗] No URL provided. Exiting.")
        sys.exit(1)

    print("\n[?] Enter output directory name (press Enter for 'downloads'):")
    custom_path = input("> ").strip()

    if custom_path:
        download_playlist_as_mp3(playlist_url, custom_path)
    else:
        download_playlist_as_mp3(playlist_url)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Download cancelled by user.")
        sys.exit(0)