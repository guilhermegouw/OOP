from fileinput import filename


class AudioFile:
    def __init__(self, filename) -> None:
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format.")

        self.filename = filename


class Mp3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"Playing {self.filename} as mp3")


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"Playing {self.filename} as wav")


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print(f"Playing {self.filename} as ogg")
