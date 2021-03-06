##################################
# vowelFormants v1.1 (17 June 2019)
# This script goes through all the files in a folder and writes in a txt informaition about formants, duration, intensity and F0.
#
#		REQUIREMENTS [INPUT]
#	A sound and a Textgrid with THE SAME filename and without spaces in the filename. For example this_is_my_sentence.wav and this_is_my_sentence.TextGrid
#	The format of the TextGrid must be: tier1 (interval) for sounds; tier2 (interval) for syllables; tier3 (interval) for words
#
#		INSTRUCTIONS 
#	1. Open the script (Open/Read from file...), click Run in the upper menu and Run again. 
#	2. Set the parameters.
#		a) Folder where the files you want to analyse are
#		b) Name of the txt where the results will be saved
#		c) Data to optimise the formantic analysis
#		d) Data to optimise the pitch (F0) detection
#
#		OUTPUT
#	The output is a tab separated txt file (can be dragged to Excel) with the following information in columns.
#		a) file name
#		b) number of the Interval
#		c) label of the interval in tier 1: vowel
#		d) label of tier2 (usually syllable, if exists)
#		e) label of tier3 (usually word, if exists)
#		f) F0
#		g) F1
#		g) F2
#		g) F3
#		g) F4
#		g) Duration of the vowel
#		g) Intensity of the vowel at its mid point
#
#		If your country uses comma as decimal separator you may want to uncomment line 132. If you are using R/Python/matlab or similar in order to do the stats don't do that. 
#		Its only for people that use Excel > SPSS
# (c) Wendy Elvira Garc챠a (2017) www.wendyelvira.ga
# Laboratori de Fon챔tica (Universitat de Barcelona) http://stel.ub.edu/labfon/en
#
#################################

#########	FORM	###############

form Pausas vowelFormants
	sentence Folder /home/eunjung/CLASSIFIER/script/asr/exp/align/text
	#sentence Folder /Users/Lab/Desktop/myfiles
	sentence txtName results.txt
	comment _
	comment Data for formant analysis
	positive Time_step 0.01
	integer Maximum_number_of_formants 5
	positive Maximum_formant_(Hz) 5500_(=adult female)
	positive Window_length_(s) 0.025
	real Preemphasis_from_(Hz) 50
	comment  _
	comment Pitch analysis data
	integer pitchFloor 75
	integer pitchCeiling 600
endform

#################################
#################################

# variables 
tier =1

#checks whether the file exists
if fileReadable(folder$ + "/" + txtName$) = 1
	pause The file already exists. If you click continue it will be overwritten.
endif

#creates the txt output with its fisrt line
writeFileLine: folder$ + "/"+ txtName$, "fileName", tab$ , "nInterval", tab$, "Label interval", tab$, "Label tier2", tab$, "Label tier3", tab$, "F0 [Hz]", tab$, "F1 [Hz]", tab$, "F2 [Hz]", tab$, "F3 [Hz]", tab$, "F4 [Hz]", tab$, "Duration[ms]", tab$, "Intensity [ms]", tab$

# index files for loop
myList = Create Strings as file list: "myList", folder$ + "/"+ "*.TextGrid"
nFiles = Get number of strings

# checks matching names
if nFiles <1
 exitScript: "No .TextGrid found in folder " + folder$
endif
#loops all files in folder

for file to nFiles
	selectObject: myList
	nameFile$ = Get string: file
	myTextGrid = Read from file: folder$ + "/"+ nameFile$
	#base name
	myTextGrid$ = selected$("TextGrid")

	#checks its a wav that matches the textgrid filename
	if fileReadable(folder$ + "/"+ myTextGrid$ + ".wav")
		mySound = Read from file: folder$ + "/"+ myTextGrid$ + ".wav"
	else
		exitScript: "No .wav matches .TextGrid name, check for spaces"
	endif


	selectObject: myTextGrid
	nOfIntervals = Get number of intervals: tier
	# converts Praat trigrphs to unicode in order to get one character for making the match
	Convert to Unicode
	
	
	#loops intervals
	nInterval=1
	for nInterval from 1 to nOfIntervals
		selectObject: myTextGrid
		labelOfInterval$ = Get label of interval: tier, nInterval
	
		#perform actions only for intervals that contain a vowel
		if index(labelOfInterval$, "ii")  <> 0 or 
		... index(labelOfInterval$, "ee") <> 0 or 
		... index(labelOfInterval$, "aa") <> 0 or 
		... index(labelOfInterval$, "oo") <> 0 or 
		... index(labelOfInterval$, "uu") <> 0 
		
			#Gets time of the interval
			endPoint = Get end point: tier, nInterval
			startPoint = Get starting point: tier, nInterval
			durInterval = endPoint- startPoint
			midInterval = startPoint +(durInterval/2)
			durIntervalms = durInterval*1000
			#fix decimals
			durIntervalms$ = fixed$(durIntervalms, tier)
			#change decimal marker for commas
			#durIntervalms$ = replace$ (durIntervalms$, ".", ",", 1)
			
			#looks for time aligned labels in other tiers
			numberOfTiers = Get number of tiers
			if numberOfTiers > 1
				intervalin2 = Get interval at time: 2, midInterval
				labelTier2$ = Get label of interval: 2, intervalin2
			else
				labelTier2$ = "no"
			endif
			
			if numberOfTiers >2
				intervalin3 = Get interval at time: 3, midInterval
				labelTier3$ = Get label of interval: 3, intervalin3
			else
				labelTier3$ = "no"
			endif
			
			#writes interval in the output
			appendFile: folder$ + "/"+ txtName$, myTextGrid$, tab$, nInterval, tab$, labelOfInterval$, tab$, labelTier2$, tab$, labelTier3$, tab$
						
			#F0
			selectObject: mySound
			myPitch = To Pitch: 0, pitchFloor, pitchCeiling
			f0 = Get value at time: midInterval, "Hertz", "Linear"
			f0$ = fixed$(f0, 0)
						
			#look for formants
			selectObject: mySound
			myFormant = To Formant (burg): time_step, maximum_number_of_formants, maximum_formant, window_length, preemphasis_from
			
			f1 = Get value at time: 1, midInterval, "Hertz", "Linear"
			f2 = Get value at time: 2, midInterval, "Hertz", "Linear"
			f3 = Get value at time: 3, midInterval, "Hertz", "Linear"
			f4 = Get value at time: 4, midInterval, "Hertz", "Linear"
			f1$ = fixed$(f1, 0)
			f2$ = fixed$(f2, 0)
			f3$ = fixed$(f3, 0)
			f4$ = fixed$(f4, 0)
			# Save result to text file:
			appendFile: folder$ + "/"+ txtName$, f0$, tab$, f1$, tab$, f2$, tab$, f3$, tab$, f4$, tab$
			removeObject: myFormant
			
			# look for intensity
			selectObject: mySound
			myIntensity = To Intensity: 500, 0, "yes"
			midInt = Get value at time: midInterval, "Cubic"
			midInt$ = fixed$(midInt,0)
			appendFileLine: folder$ + "/"+ txtName$, durIntervalms$, tab$, midInt$
			removeObject: myPitch, myIntensity
		endif
		#close interval loop
	
	endfor
	#close file loop
removeObject: myTextGrid, mySound
endfor
removeObject: myList
	echo Done.
