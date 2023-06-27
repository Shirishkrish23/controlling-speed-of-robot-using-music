import rclpy
from rclpy.node import Node
import sounddevice as sd
import librosa

class AudioPlaybackNode(Node):
    def __init__(self):
        super().__init__('audio_playback_node')

    def play_audio(self):
        audio_file_path = '/home/tiredtaurus/Downloads/audio_files/file_example_WAV_1MG.wav'
        audio, sample_rate = librosa.load(audio_file_path, sr=None)

        # Play the audio
        sd.play(audio, sample_rate)
        sd.wait()

    def run(self):
        self.play_audio()


def main(args=None):
    rclpy.init(args=args)
    audio_playback_node = AudioPlaybackNode()
    try:
        audio_playback_node.run()
    except KeyboardInterrupt:
        pass
    finally:
        audio_playback_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
