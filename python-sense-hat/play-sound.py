import subprocess
# p = subprocess.Popen(['omxplayer', '/home/pi/sound/105345__sandyrb__sonar-ping-pong-eb.wav'], stdout=subprocess.PIPE.communicate()[0]


p = subprocess.Popen (['omxplayer', '/home/pi/sound/105345__sandyrb__sonar-ping-pong-eb.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p.communicate()
print out

