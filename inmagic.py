import subprocess
import sys
filename = sys.argv[1]
inputxml = filename + ".xml"

vcodec = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'Codec', filename ])
width = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'Width', filename ])
height = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'Height', filename ])
DAR = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'DisplayAspectRatio', filename ])

acodec = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Audio']", '-v', 'Codec', filename ])

duration = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='General']", '-v', 'Duration_String4', filename ])
wrapper = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='General']", '-v', 'FileExtension', filename ])
filesize = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='General']", '-v', 'FileSize_String4', filename ])


print '<inm:V-Codec>%s</inm:V-codec>'  % vcodec
print acodec, vcodec, duration, width, height, DAR, wrapper

fo = open(inputxml, "w+")
fo.write('<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>\n')
fo.write('<inm:Results productTitle="Inmagic DB/TextWorks for SQL" productVersion="13.00" xmlns:inm="http://www.inmagic.com/webpublisher/query">\n')
fo.write('<inm:Recordset setCount="1">\n')
fo.write('<inm:Record setEntry="0">\n')	
fo.write('<inm:Video-codec>%s</inm:Video-codec>\n' % vcodec) 
fo.write('<inm:D-Audio-codec>%s</inm:D-Audio-codec>\n' % acodec)
fo.write('<inm:D-Duration>%s</inm:D-Duration>\n' % duration)
fo.write('<inm:D-video-width >%s</inm:D-video-width >\n' % width)
fo.write('<inm:D-video-height >%s</inm:D-video-height >\n' % height)
fo.write('<inm:Display-Aspect-ratio >%s</inm:Display-Aspect-ratio >\n' % DAR)
fo.write('<inm:Wrapper>%s</inm:Wrapper>\n' % wrapper)
fo.write('<inm:D-File-Size >%s</inm:D-File-Size >\n' % filesize)
fo.write('</inm:Record>\n')	
fo.write('</inm:Recordset>\n')	
fo.write('</inm:Results>\n')	
fo.close
