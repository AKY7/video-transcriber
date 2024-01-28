from pydub import AudioSegment
import os


# Directory containing the video files
video_dir = "videos"

# Directory to save the audio files
audio_dir = "audio"

# Create the audio directory if it doesn't exist
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)

# Get a list of all files in the directory
video_files = os.listdir(video_dir)

# Process each video file
for video_file in video_files:
    # Ensure the file is a .mp4 file
    if not video_file.endswith(".mp4"):
        print("Skipping " + video_file + " because it's not a .mp4 file")
        continue
    print("Processing " + video_file)
    # Load the video file
    video_path = os.path.join(video_dir, video_file)
    video = AudioSegment.from_file(video_path, format="mp4")
    audio = video.set_channels(1).set_frame_rate(16000).set_sample_width(2)

    # Create the .wav filename based on the original video filename
    wav_filename = os.path.splitext(video_file)[0] + ".wav"

    # Export the audio to the new directory
    audio.export(os.path.join(audio_dir, wav_filename), format="wav")