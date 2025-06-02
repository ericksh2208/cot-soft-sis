import speech_recognition as sr
from moviepy.editor import VideoFileClip,AudioFileClip
class MovieManager:
    def get_wav_audio(self, mp4_file, war_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(war_file, codec='pcm_s16le')
        ac.close()
        vc.close

    def audio_to_text(self,audio_file):
        r=sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        try:
            text=r.recognize_google(audio, language='es')
            return text
        except:
            return 'unknow'

mm=MovieManager()
#mm.get_wav_audio('video.mp4','audio.wav')
speech= mm.audio_to_text('audio.wav')
print(speech)
