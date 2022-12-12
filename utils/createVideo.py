import ffmpeg
import pathlib
import tempfile
from ffprobe import FFProbe

def create_video(image_path, audio_bytes, format='mp4'):
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create the output video file in the temporary directory
        output_path = pathlib.Path(temp_dir) / 'output.mp4'

        # Create the FFmpeg object
        ff = ffmpeg

        audio_path = pathlib.Path(temp_dir) / 'audio.mp3'
        with open(audio_path, 'wb') as f:
            f.write(audio_bytes)

        # Specify the input files
        input_still = ff.input(image_path)
        input_audio = ff.input(audio_path)
        duration = FFProbe(str(audio_path)).streams[0].duration_seconds()
        # Specify the output file and the format and duration of the video

        run = (
            ff
            .concat(input_still, input_audio, v=1, a=1)
            .output(filename=output_path, format=format, t=duration, loop=1, vcodec='libx264', shortest=False)
           )
        result = run.run(overwrite_output=True)

        # Return the byte array
        return pathlib.Path(output_path).read_bytes()


if __name__ == '__main__':
    # add image and audio from arguments
    cwd = pathlib.Path.cwd()
    image_path = cwd / 'img' / 'altryne.jpeg'
    audio_path = cwd / 'audio' / 'sam-altman.mp3'
    # Create a video from the image and audio files
    video_bytes = create_video(image_path, audio_path.read_bytes(), 'mp4')

    # Write the video to a file
    with open('output.mp4', 'wb') as f:
        f.write(video_bytes)