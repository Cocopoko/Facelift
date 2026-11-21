# Faces go here (on the Pi: /root/coco2-faces)

One PNG per face state, named after the state:

LOOK_R, LOOK_L, LOOK_R_HAPPY, LOOK_L_HAPPY, AWAKE, HAPPY, EXCITED, COOL,
GRATEFUL, FRIEND, MOTIVATED, SMART, SLEEP, SLEEP2, BORED, LONELY, SAD,
DEMOTIVATED, ANGRY, INTENSE, BROKEN, DEBUG, UPLOAD, UPLOAD1, UPLOAD2

Format: 108x108, 1-bit (mode "1") PNG. Any picture works — crop it square,
convert to greyscale, resize to 108x108 and dither to black & white.
Bold, high-contrast images read best at this size. Missing states fall
back to the classic text face automatically.
