import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import numpy as np
import librosa
import time


class AudioProcessingNode(Node):
    def __init__(self):
        super().__init__('audio_processing_node')
        self.publisher = self.create_publisher(Float32, 'robot_speed', 10)

    def process_audio(self, audio, sample_rate):
        # Calculate the duration of each second
        duration_per_second = 1.0

        # Calculate the number of samples per second
        samples_per_second = int(sample_rate * duration_per_second)

        # Calculate the number of seconds in the audio
        num_seconds = int(np.ceil(len(audio) / samples_per_second))

        # Iterate over each second of the audio
        for i in range(num_seconds):
            # Extract audio for the current second
            audio_second = audio[i * samples_per_second : (i + 1) * samples_per_second]

            # Apply FFT to the audio signal
            frequencies = np.fft.fftfreq(len(audio_second), d=1/sample_rate)
            magnitudes = np.abs(np.fft.fft(audio_second))

            # Define frequency ranges and corresponding speed values
            frequency_ranges = [(3500, 3550), (3550, 3600), (3600, 3650), (3650, 3700), (3700, 3750), (3750, 3800), (3800, 3850), (3850, 3900)]
            speed_values = [0.01, 0.06, 0.11, 0.16, 0.21, 0.26, 0.31, 0.36]

            values_to_publish = []  # List to store values to be published

            for freq_range, speed in zip(frequency_ranges, speed_values):
                # Find indices corresponding to the frequency range
                indices = np.where((frequencies >= freq_range[0]) & (frequencies < freq_range[1]))[0]

                # Calculate the average magnitude within the frequency range
                avg_magnitude = np.mean(magnitudes[indices])

                # Store the speed command based on the average magnitude
                value = speed
                values_to_publish.append(value)

            # Publish the stored values
            for value in values_to_publish:
                msg = Float32()
                msg.data = value
                self.publisher.publish(msg)
                time.sleep(1)  # Sleep for 1 second

        # Publish a value of 0.0 after all values have been published
        zero_msg = Float32()
        zero_msg.data = 0.0
        self.publisher.publish(zero_msg)

    def run(self):
        audio_file_path = '/home/tiredtaurus/Downloads/audio_files/file_example_WAV_1MG.wav'
        audio, sample_rate = librosa.load(audio_file_path, sr=None)

        self.process_audio(audio, sample_rate)

        rclpy.spin(self)


def main(args=None):
    rclpy.init(args=args)
    audio_processing_node = AudioProcessingNode()
    try:
        audio_processing_node.run()
    except KeyboardInterrupt:
        pass
    finally:
        audio_processing_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
