import subprocess
from music21 import converter, midi

# ========= INSTRUCTIONS ==========
# 
# To run the script download and extract fluidsynth program .zip file from his github page:
#   https://github.com/fluidsynth/fluidsynth/releases
#
# Download also a SounfFont .sf2 file like GeneralUser-GS:
#   https://www.schristiancollins.com/generaluser
#
# Extract the files and parse the correct address paths in the following fields 
#

# ================= PATH CONFIGURATION =================
# Insert the path to the fluidsynth.exe file
FLUIDSYNTH_EXE = r"fluidsynth-v2.6.0-win10-x64-cpp11\bin\fluidsynth.exe"

# Insert the path to the file SoundFont .sf2
SOUNDFONT_PATH = r"GeneralUser-GS\GeneralUser-GS.sf2"

MIDI_PATH = "output.mid"
WAV_PATH = "output.wav"
# ===========================================================

abc_string = """X:1
L:1/8
M:3/4
K:D
|: A3 D3 F3 | A2 B2 c2 d2 | A3 D3 F3 | G2 F2 E2 d2 | A3 D3 F3 | E2 F2 D2 c2 | d2 B2 A2 g2 | 
 f2 g2 f2 e2 | d2 c2 B2 A2 | G2 D2 A2 G2 | A2 G2 G2 G2 | f2 e2 d2 B2 | f2 g2 f2 e2 | 
 d2 c2 B2 A2 | G2 D2 A2 G2 | A2 F2 F2 F2 :|"""

# 1. Parsing ABC
print("1. Parsing ABC string...")
score = converter.parse(abc_string, format="abc")

# 2. exporting MIDI output file
print("2. Wrinting MIDI file...")
try:
    score.write("midi", fp=MIDI_PATH)
except Exception:
    mf = midi.translate.streamHierarchyToMidiTracks(score)
    midi_file = midi.MidiFile()
    midi_file.tracks = mf
    midi_file.open(MIDI_PATH, 'wb')
    midi_file.write()
    midi_file.close()

print(f"MIDI file succesfully created: {MIDI_PATH}")

# 3. Converting MIDI file to WAV
print("3. Synthesizing audio WAV file with FluidSynth...")

cmd = [
    FLUIDSYNTH_EXE,
    "-ni",               # not-interactive
    "-F", WAV_PATH,      # output file
    "-r", "44100",       # sampling frequency
    SOUNDFONT_PATH,      # SoundFont path
    MIDI_PATH            # MIDI file path
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(f"File audio WAV succesfully created: {WAV_PATH}")
except subprocess.CalledProcessError as e:
    print(f"Error during FluidSynth execution:\n{e.stderr}")
except FileNotFoundError:
    print(f"ERROR: fluidsynth.exe not foundat the given path \n({FLUIDSYNTH_EXE})")