import subprocess
import sys
filename = sys.argv[1]


vcodec = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'Codec', filename ])
width = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'Width', filename ])
height = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'Height', filename ])
DAR = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Video']", '-v', 'DisplayAspectRatio', filename ])

acodec = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='Audio']", '-v', 'Codec', filename ])

duration = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='General']", '-v', 'Duration_String4', filename ])
wrapper = subprocess.check_output(['xml','sel', '-t', '-m', "Mediainfo/File/track[@type='General']", '-v', 'FileExtension', filename ])
print '<inm:V-Codec>%s</inm:V-codec>'  % vcodec
print acodec, vcodec, duration, width, height, DAR, wrapper
