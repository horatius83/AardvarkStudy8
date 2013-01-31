# automatic kanji lookup
# answer returned from user and answer displayed can be different
# ui

from FileManagement import OpenJsonFile, ProcessJsonObj, OutputJsonFile
from Vocab import Quiz, EightsQuizFunction

def RunTest(filename):
    print("Opening file: {0}".format(file))
    jo = OpenJsonFile(file)
    print("Processing file...")
    joPrime = ProcessJsonObj(jo)
    print("Making backup of the file to {0}.old".format(file))
    OutputJsonFile(joPrime,file + '.old')
    print("Starting test...")
    newWords = Quiz(joPrime, EightsQuizFunction)
    print("Recording results...")
    OutputJsonFile(newWords,file)
    print("Done.")    

#file = "./KanjiByOldLevel/KanjiQuizLevel3.json"
file = "./Vocabulary/N3.json"
RunTest(file)
