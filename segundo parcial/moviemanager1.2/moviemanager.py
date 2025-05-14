import speech_recognition as sr
from moviepy.editor import VideoFileClip,AudioFileClip,CompositeAudioClip
from deep_translator import GoogleTranslator
from gtts import gTTS

class MovieManager:

    def get_wav_audio(self, mp4_file, war_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(war_file, codec='pcm_s16le')
        ac.close()
        vc.close()

    def audio_to_text(self,audio_file):
        r=sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        try:
            text=r.recognize_google(audio, language='es')
            return text
        except:
            return 'unknow'

    def get_wav_audio(self, mp4_file, wav_file):
        # https://www.youtube.com/watch?v=loeq5KnZXaM


        # Carga del video
        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(wav_file, codec="pcm_s16le")
        
        audio_clip.close()
        video_clip.close()

    def remove_audio(self, mp4_file, output_mp4_file):
        video = VideoFileClip(mp4_file)
        video_without_audio = video.without_audio()
        video_without_audio.write_videofile(output_mp4_file)
        video_without_audio.close()
        video.close

    def speech_to_text(self, audio_file):
        r = sr.Recognizer()

        hellow = sr.AudioFile(audio_file)
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print("Text: "+s)
        except Exception as e:
            print("Exception: "+str(e))
        return s
    
    def text_to_speech(self, to_translate, to_lang):
        translated = GoogleTranslator(source='auto', target=to_lang).translate(to_translate)
        print(translated)
        myobj = gTTS(text=translated, lang=to_lang, slow=False)
        myobj.save("welcome.mp3")

    def add_audio_to_video(self, mp4_file, mp3_file, output_mp4_file):
        videoclip = VideoFileClip(mp4_file)
        audioclip = AudioFileClip(mp3_file)

        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        videoclip.write_videofile(output_mp4_file)
        
    
    
mm=MovieManager()
#mm.get_wav_audio('video.mp4','audio.wav')
#speech= mm.audio_to_text('audio.wav')
#print(speech)
#mm.remove_audio('video.mp4','video_sin_audio.mp4')
#mm.text_to_speech(speech, 'en')
mm.add_audio_to_video('video_sin_audio.mp4', 'welcome.mp3', 'videoEN.mp4')
