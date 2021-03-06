# COSI configuration

passive(screentype = "8:5") # e.g., MBP (1680x1050)
# passive(screentype = "4:3") # e.g., D458 (1028x768)

expName = 'COSI2'

# Number of sessions per subject
numSessions = 2

isEEG = True
#isEEG = False
playAudio = True
#playAudio = False

# for talking to the NetStation computer over ethernet
#isNS = True
isNS = False
ns_port = 55513
# D464
#ns_ip = '128.138.223.26'
# D458
ns_ip = '128.138.223.251'
# my G4
#ns_ip = '128.138.223.154'

#############################
# Exp organization
#############################

# Number of trials/lists per session
numLists = 4
# Number of target stimuli per trial/list
study_listLen = 100
# number of buffer stimuli to add to start and end of lists
study_bufferStart = 2
study_bufferEnd = 2
# Recognition & Source task
test_numLures = 50
# targ that were presented on L and R; should be half of the study
# list length
test_numTargets_Left = 50
test_numTargets_Right = 50

# Do a practice trial?
practiceList = True
#practiceList = False
prac_testblocks = ['color', 'side']
prac_numLists = 2
pracstudy_listLen = 10
pracstudy_bufferStart = 2
pracstudy_bufferEnd = 2
practest_numLures = 6

#############################
# Display setup
#############################

# Stim setup
PICTURE_SIZE = 0.3
mid_coord = 0.5
top_coord = 0.05
bot_coord = 0.95
fback_coord = 0.25

if screentype == "8:5":
    # Widescreen (1680x1050): 15" MBP, office display
    left_coord = 0.31
    right_coord = 0.69
elif screentype == "4:3":
    # Squarescreen (1280x1024): D458/D464 linux EEG
    left_coord = 0.28
    right_coord = 0.72

# old configurations
# 15" PowerBook (1280x800); E013 iMac (1440x900)
#left_coord = 0.31
#right_coord = 0.69
# Square (1024x768): D458? linux EEG
#left_coord = 0.28
#right_coord = 0.72
# 1024x768?
#left_coord = 0.25
#right_coord = 0.75

#KEYIMAGE_SIZE = (0.96,0.12)

# Word Font size (proportion of vertical screen)
test_wordHeight = .05
instruct_wordHeight = .05
fixation_wordHeight = .05

# Orienting Stimulus text
orientText = '+'

# frame for the stimuli during 'side'
side_color_name = ('White')
side_color_rgb = (255,255,255,255)

# color frame info
#color_rgbs = ((229,0,0,255),(3,67,225,255))
#color_names = ('Red','Blue')
color_rgbs = ((3,67,225,255),(255,255,20,255))
color_names = ('Blue','Yellow')
#colors_rgb = [(126,30,156,255),(21,176,26,255),(3,67,223,255),(255,129,192,255),(229,0,0,255),(249,115,6,255),(255,255,20,255),(101,55,0,255)]
#color_names = ('Purple','Green','Blue','Pink','Red','Orange','Yellow','Brown')
#(2,147,134,255),(0,255,255,255)
# color_names = ('Teal','Cyan')

color_frame_side_prop = 0.2 # proportion of image size
color_frame_top_prop = 0.2 # proportion of image size

test_rect_side_prop = 0.15 # proportion of image size
test_rect_top_prop = 0.15 # proportion of image size

#################################
# EEG setup
#################################

# initial resting period duration
restEEGDuration = 200

# this is the key that the experimenter has to hit to continue after
# impedance check
endImpedanceKey = "G"
# choose a huge number for the impedance countdown
#minImpedanceTime = 300000 # 300000ms=5min
minImpedanceTime = 1000 # 240000ms=4min
maxImpedanceTime = 3600000 # 3600000ms=60min

# number of blink breaks
#doBlinkBreaks = True
doBlinkBreaks = False
study_blinkBreaksPerList = 6
test_blinkBreaksPerList = 10
# EEG: Pause after a blinking period to subject can finish blinking
pauseAfterBlink = 2000
textAfterBlink = "Get ready..."

# BEHAVIORAL ONLY: amount of time to break between study and test (isEEG == False)
breakTime = 300000 # 300000ms=5min

################################
# Study period parameters
################################

# Pause+Jitter after orienting cross before first study stim; only
# happens once on each list
study_preStimDelay = 20
study_preStimJitter = 5
# Duration that the study stim is on the screen
study_sourcePreview = 5
study_stimDuration = 10
study_stimJitter = None
# ISI+Jitter after study stim is cleared from the screen
study_ISI = 5
study_ISIJitter = 3

############################################################
# Test period parameters
############################################################

# keys for the test period
leftKeys_test = ('Z','X')
rightKeys_test = ('.','/')

redoKey_test = ('LEFT SHIFT', 'RIGHT SHIFT')

sourceLeftText_test = "L"
sourceRightText_test = "R"

newText_test = "N"
rememSideText_test = "RS"
rememColorText_test = "RC"
rememOtherText_test = "RO"
knowText_test = "F"
sureText_test = "Sure"
maybeText_test = "Maybe"

if screentype == "8:5":
    # Widescreen
    test_source_left_x = (0.53, 0.43)
    test_source_right_x = (0.57, 0.47)
    test_new_x = (0.47, 0.53)
    test_rs_x = (0.6, 0.4)
    test_ro_x = (0.54, 0.46)
    test_k_x = (0.47, 0.53)
    test_sure_x = (0.445, 0.555)
    test_maybe_x = (0.57, 0.425)
elif screentype == "4:3":
    # Squarescreen
    test_source_left_x = (0.54, 0.41)
    test_source_right_x = (0.59, 0.46)
    test_new_x = (0.46, 0.54)
    test_rs_x = (0.62, 0.38)
    test_ro_x = (0.55, 0.45)
    test_k_x = (0.46, 0.54)
    test_sure_x = (0.43, 0.57)
    test_maybe_x = (0.59, 0.405)

# Pause+Jitter before test period begins; happens once per list
test_preStimDelay = 20
test_preStimJitter = 5

# amount of time to show test stimulus
test_stimDuration = 8
test_stimJitter = None
# delay after each stim before response period
test_preRespOrientDelay = 15
test_preRespOrientJitter = None
#test_preRespBlankDelay = 900
# min and max response duration
test_minRespDuration = 1
test_maxRespDuration = 300
# delay after response period
test_ISI = 5
test_ISIJitter = 3

#############################################
# Other experiment parameters
#############################################

# countdown timer between lists
ILI_timer = True
ILI_dur = 1000
ILI_key = 'SPACE'

# make the stimulus pools
objectStimuli = 'images/object_stims'
#objectStimuliTxt = 'images/object_stims.txt'
objectBuffers = 'images/object_buffers'
#objectBuffersTxt = 'images/object_buffers.txt'
noiseStimuli = 'images/noise_stim'
#noiseStim = 'images/noise/noise1.png'
presentationType = 'image'  # image, sound, text
presentationAttribute = 'name'  # attribute to use to create the text
                                # description

# Trial text
sesBeginText = "Press any key for Session #%d."
trialBeginText = "Press any key for Trial #%d."
studyBeginText = "Blink now.\nPress SPACE to begin Study #%d."
testBeginText = "Blink now.\nPress SPACE to begin Test #%d."
studyPracBeginText = "Blink now.\nPress SPACE to begin Study Practice."
testPracBeginText = "Blink now.\nPress SPACE to begin Test Practice."
restEEGPrep = "Press any key to record resting data."
restEEGText = "Recording resting data. Please sit still..."
blinkRestText_study = "Blink now.\nPress any key to continue study period."
blinkRestText_test = "Blink now.\nPress any key to continue test period."

# Set up the beeps
hiBeepFreq = 800
hiBeepDur = 500
hiBeepRiseFall = 100
loBeepFreq = 400
loBeepDur = 500
loBeepRiseFall = 100

# Instructions text file
instruct_getready = 'text/instruct_getready.txt'
# BEH
#instruct_intro = 'text/beh/instruct_intro.txt'
#instruct_study_practice = 'text/beh/instruct_study_practice.txt'
#instruct_test_practice = 'text/beh/instruct_test_practice.txt'
#instruct_study = 'text/beh/instruct_study.txt'
#instruct_test = 'text/beh/instruct_test.txt'
#midSessionBreak = 'text/beh/midSessionBreak.txt'
# EEG
instruct_intro = 'text/eeg/instruct_intro_eeg.txt'
instruct_study_color_practice = 'text/eeg/instruct_study_color_practice_eeg.txt'
instruct_study_side_practice = 'text/eeg/instruct_study_side_practice_eeg.txt'
instruct_test_color_practice = 'text/eeg/instruct_test_color_practice_eeg.txt'
instruct_test_side_practice = 'text/eeg/instruct_test_side_practice_eeg.txt'
instruct_study_color = 'text/eeg/instruct_study_color_eeg.txt'
instruct_study_side = 'text/eeg/instruct_study_side_eeg.txt'
instruct_test_color = 'text/eeg/instruct_test_color_eeg.txt'
instruct_test_side = 'text/eeg/instruct_test_side_eeg.txt'
midSessionBreak = 'text/eeg/midSessionBreak.txt'

# Default font
defaultFont = 'fonts/Verdana.ttf'
