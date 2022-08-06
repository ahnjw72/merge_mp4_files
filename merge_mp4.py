#####################################################################################################
#
# ref site: https://stackoverflow.com/questions/7333232/how-to-concatenate-two-mp4-files-using-ffmpeg
#
# This script assume merging intro.mp4, some mp4 in a specific folder, and out.mp4 into an mkv file.
#
#####################################################################################################

import subprocess, glob, os

filenames = sorted(os.listdir('.'))
print(filenames)
for filename in filenames:
    if os.path.isdir(filename):
        if "ipynb" in filename:
            continue
        #print(filename)
        files = sorted(os.listdir(filename))
        #print(files)

        for file in files:
            if 'mp4' in file:
                #print(file)
                pre, ext = os.path.splitext(file)
                output_mkv = os.path.join(filename, pre+'.mkv')
                #print(output_mkv)
                input_mp4 = os.path.join(filename, file)

                ffmpeg_command = f'ffmpeg -y -i intro.mp4 -i "{input_mp4}" -i out.mp4 -filter_complex "[0:v] [0:a] [1:v] [1:a] [2:v] [2:a] concat=n=3:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" "{output_mkv}"'
                print(ffmpeg_command)
                subprocess.call(ffmpeg_command, shell=True, stdout=stdout_file)
                #!{ffmpeg_command}
