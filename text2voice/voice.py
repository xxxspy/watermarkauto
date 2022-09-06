import pysrt
import azure.cognitiveservices.speech as speechsdk
from moviepy.editor import AudioFileClip, CompositeAudioClip
from pathlib import Path
import time 

speech_key = "5256043bad8e4c7a861ed6428e714302"
service_region = "eastus"


speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)


# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name="zh-CN-YunxiNeural"



def to_secondes(sub):
    s = sub.start
    return s.hours * 60 * 60 + s.minutes * 60 + s.seconds + s.milliseconds / 1000


def voice(outputdir: str, strfile: str):
    for sub in pysrt.open(strfile):
        if not sub.text.strip():
            continue
        outputpath = '{}/{}.wav'.format(outputdir, str(sub.start).replace(':', '-'))
        if Path(outputpath).exists():
            continue
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename=outputpath)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        speech_synthesis_result = speech_synthesizer.speak_text(sub.text)
        print(outputpath)


def merge(datadir):
    audios = []
    for path in Path(datadir).iterdir():
        if path.suffix == '.wav':
            audios.append(AudioFileClip(str(path)).set_start(path.stem.replace('-', ':')))
    cac = CompositeAudioClip(audios)
    cac.fps = audios[0].fps
    cac.write_audiofile('d:/output.wav')

if __name__ == '__main__':
    # voice(r'D:\mysites\watermarkauto\output', r"D:\mysites\watermarkauto\text2voice\Introduction to Stata.zh-Hans.srt")
    merge(r'D:\mysites\watermarkauto\output')