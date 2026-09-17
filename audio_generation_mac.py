import subprocess
import shutil

# ========= INSTRUCTIONS ==========
# Before running this script fluidsynth installation is required
# run the following command by command line to install Homebrew:
#   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# 
# install then fluidsynth using the following command line:
#   brew install fluidsynth
# 
# You can check fluidsynth installation using the following command:
#   fluidsynth --version
#
# ---------------------------------------------------------------------------------------
#
# On Mac, Homebrew usually installs to:
# /opt/homebrew/bin/fluidsynth (Apple Silicon M1/M2/M3/M4)
# or /usr/local/bin/fluidsynth (Intel)
# shutil.which locates it automatically:
FLUIDSYNTH_CMD = shutil.which("fluidsynth") or "fluidsynth"

# ================= PATH CONFIGURATION =================
# Insert the path to the file SoundFont .sf2
SOUNDFONT_PATH = r"GeneralUser-GS\GeneralUser-GS.sf2"

MIDI_PATH = "output.mid"
WAV_PATH = "output.wav"
# ===========================================================

cmd = [
    FLUIDSYNTH_CMD,
    "-ni",
    "-F", WAV_PATH,
    "-r", "44100",
    SOUNDFONT_PATH,
    MIDI_PATH
]

result = subprocess.run(cmd, capture_output=True, text=True, check=True)
print("Audio file successfully generated on Mac!")