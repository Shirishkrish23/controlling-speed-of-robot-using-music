import rclpy
from rclpy.node import Node
import sounddevice as sd
import librosa

class AudioPlaybackNode(Node):
    def __init__(self):
        super().__init__('audio_playback_node')

    def play_audio(self):
        # Path to the audio file to be played
        audio_file_path = '/home/tiredtaurus/Downloads/audio_files/file_example_WAV_1MG.wav'

        # Load the audio file using librosa
        audio, sample_rate = librosa.load(audio_file_path, sr=None)

        # Play the audio using sounddevice
        sd.play(audio, sample_rate)
        sd.wait()

    def run(self):
        # Entry point of the node
        self.play_audio()


def main(args=None):
    # Initialize the ROS 2 system
    rclpy.init(args=args)

    # Create an instance of the AudioPlaybackNode class
    audio_playback_node = AudioPlaybackNode()

    try:
        # Run the audio playback node
        audio_playback_node.run()
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up the node
        audio_playback_node.destroy_node()

        # Shutdown the ROS 2 communication
        rclpy.shutdown()


if __name__ == '__main__':
    main()
