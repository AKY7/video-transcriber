# Video Transcriber

## Overview
Video Transcriber is a tool designed to convert spoken language in videos into written text. It's an excellent resource for generating subtitles, understanding content in a foreign language, or enhancing accessibility.

## Prerequisites

To use Video Transcriber, you need to have the following installed:

1. Python 3: Install it using `pip install python3`
2. PyDub: A Python library for audio file manipulation. Install it using `pip install pydub`
3. OpenAI Whisper: An automatic speech recognition (ASR) system. Install it using `pip install -U openai-whisper`

Note: OpenAI Whisper requires additional dependencies, including `ffmpeg`. You can find detailed installation instructions in the [official OpenAI Whisper documentation](https://github.com/openai/whisper).

## Installation and Usage

Follow these steps to install and use Video Transcriber:

1. Clone the repository.
2. Navigate into the project directory: `cd video-transcriber`
3. Create a 'videos' folder and add the .mp4 files you want to transcribe.
4. Grant execute permissions to the script: `chmod +x transcript.sh`
5. Run the script: `./transcript.sh`
6. You can find the transcript for each video in the 'transcript' folder.

## Customization

The Whisper command is currently configured for long videos and MacOS. You can customize it to your needs by modifying line 31 in `transcript.sh`.

## Contributing

We welcome contributions! If you want to make major changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).