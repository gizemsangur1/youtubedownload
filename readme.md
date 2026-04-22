# YouTube Playlist to MP3 Downloader

A simple and efficient command-line tool to download entire YouTube playlists as high-quality MP3 files.

> **FFmpeg is bundled** — no extra installation needed. Just download and run.

---

## ⬇ Download

<!-- Replace YOUR_USERNAME and YOUR_REPO with your GitHub info -->

| Platform | Download |
|----------|----------|
|  Windows | [![Windows](https://img.shields.io/badge/Download-Windows%20.exe-0078D6?style=for-the-badge&logo=windows)](https://github.com/https://github.com/gizemsangur1/youtubedownload.git/releases/latest/download/yt-playlist-downloader-windows.exe) |
|  Linux | [![Linux](https://img.shields.io/badge/Download-Linux%20Binary-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://github.com/gizemsangur1/youtubedownload.git/releases/latest/download/yt-playlist-downloader-linux) |

---

##  Features

- Downloads all videos from a YouTube playlist and converts them to MP3
- 192kbps audio quality
- FFmpeg bundled — no separate installation required
- Real-time download progress display
- Auto-creates output directory if it doesn't exist
- Skips unavailable or private videos without stopping
- Custom output directory support

---

##  Quick Start

###  Windows

1. Download `yt-playlist-downloader-windows.exe` above
2. Double-click to run (or run from terminal)
3. Paste your playlist URL when prompted

###  Linux

```bash
# Download
wget https://github.com/https://github.com/gizemsangur1/youtubedownload.git/releases/latest/download/yt-playlist-downloader-linux

# Make executable
chmod +x yt-playlist-downloader-linux

# Run
./yt-playlist-downloader-linux
```

---

##  Run from Source

### Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg (if not using the bundled binary)

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/youtubedownload.git
cd youtubedownload
pip install yt-dlp
python downloader.py
```

---

## Example Session

```
============================================================
 YouTube Playlist to MP3 Downloader
============================================================
[✓] Using bundled FFmpeg

[?] Enter your YouTube playlist URL:
> https://www.youtube.com/playlist?list=PLxxxxxxxxxxxxxxxx

[?] Enter output directory name (press Enter for 'downloads'):
> my_music

[✓] Created output directory: my_music
[✓] Starting download from playlist
[✓] Saving MP3 files to: my_music
------------------------------------------------------------
[INFO] Fetching playlist information...
[INFO] Found 25 videos in playlist
[INFO] Playlist: My Favorite Songs

[INFO] Downloading...

[DOWNLOADING]  45.2% complete at 1.23MiB/s
[✓] Finished downloading, now converting to MP3...
------------------------------------------------------------
[✓] Download completed successfully!
[✓] Files saved in: /home/user/my_music
```

---

## Output

```
downloads/
├── Song Title One.mp3
├── Song Title Two.mp3
└── Song Title Three.mp3
```

---

## Configuration

Edit these values in `downloader.py`:

| Option | Default | Description |
|--------|---------|-------------|
| `preferredquality` | `192` | MP3 bitrate (kbps) |
| `output_path` | `downloads` | Default output folder |
| `ignoreerrors` | `True` | Skip unavailable videos |

---

## Build from Source

Builds are automated via GitHub Actions. To trigger a new release:

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions will automatically build both Windows `.exe` and Linux binary with bundled FFmpeg, then publish them as a GitHub Release.

---

## Troubleshooting

**Download fails for some videos**  
Some videos may be region-locked, age-restricted, or private. The script skips these automatically.

**Permission denied on Linux**  
```bash
chmod +x yt-playlist-downloader-linux
```

**Windows Defender warning**  
PyInstaller-built executables sometimes trigger false positives. The source code is fully open — you can inspect it and build it yourself.

---


## Disclaimer

This tool is intended for personal use only. Please respect YouTube's [Terms of Service](https://www.youtube.com/t/terms) and applicable copyright laws.