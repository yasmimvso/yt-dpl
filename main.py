import os
import subprocess

path = "c:\yt-dpl\dowloads\list.txt"

# Função principal
def main():
    try:
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()  

                if "youtube.com" in line or "youtu.be" in line:
                    print(f"Baixando o vídeo: {line}")

                    # Comando para baixar o vídeo utilizando o ffmpeg como downloader externo
                    download_command = [
                        "yt-dlp",
                        "--format", "(bestvideo+bestaudio/best)[protocol!*=dash]",
                        "--external-downloader", "ffmpeg",
                        "--external-downloader-args", "-ss 00:00:00.00 -to 00:30:00.00", 
                        "--remux-video", "mp4", 
                        "--output", "%(id)s.mp4",  
                        f"{line}"
                    ]

                    
                    subprocess.run(download_command)

                 
    except FileNotFoundError:
        print(f"arquivo não encontrado")

if __name__ == "__main__":
    main()

