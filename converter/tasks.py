#pro tip: put this whole file in one big try except...
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from pydub import AudioSegment 


@shared_task
def convert_audio(path,input_file,format2):
    format1=input_file[len(input_file)-3:len(input_file)]
    print(format1)
    output_file = path+input_file[0:len(input_file)-3]+format2
    input_file = path+input_file

    if format1=="mp3":
        sound = AudioSegment.from_mp3(input_file) 

    elif format1=="wav":
        sound = AudioSegment.from_wav(input_file) 

    elif format1=="ogg":
        sound = AudioSegment.from_wav(input_file) 

    elif format1=="flv":
        sound = AudioSegment.from_flv(input_file) 

    elif format1=="aac" or format1=="mp4" or format1=="wma":
        sound = AudioSegment.from_file(input_file) 

    sound.export(output_file, format=format2)
    print('exported')


