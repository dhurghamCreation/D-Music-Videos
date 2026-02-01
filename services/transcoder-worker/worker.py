import os
import subprocess

def start_transcode(input_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # This creates HLS chunks (Adaptive Bitrate ready)
    command = [
        'ffmpeg', '-i', input_path,
        '-profile:v', 'baseline', '-level', '3.0',
        '-s', '640x360', '-start_number', '0',
        '-hls_time', '10', '-hls_list_size', '0',
        '-f', 'hls', f'{output_dir}/index.m3u8'
    ]
    subprocess.run(command)

if __name__ == "__main__":
    # Check if video exists before starting
    if os.path.exists('/app/uploads/video.mp4'):
        start_transcode('/app/uploads/video.mp4', '/app/video_output/stream')
    else:
        print("Waiting for video.mp4 in uploads folder...")
