import azure.cognitiveservices.speech as speechsdk

speech_key = "5256043bad8e4c7a861ed6428e714302"
service_region = "eastus"


speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename='d:/text2speech.wav')

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name="zh-CN-YunxiNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
text = "总有一双眼睛盯着你网上一言一行;总有一块硬盘记录你网上蛛丝马迹;总有一个时刻追究你网上违规行为"

speech_synthesis_result = speech_synthesizer.speak_text_async(text)

# if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized for text [{}]".format(text))
# elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = speech_synthesis_result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")