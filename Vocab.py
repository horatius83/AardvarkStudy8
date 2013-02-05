#!/usr/bin/python

from FileManagement import OutputJsonFile, ProcessJsonObj, OpenJsonFile
from Utility import GetTime, CutIntoLengths, ShuffleList, Clear
from itertools import islice

def AskQuestion(question,answer):
    """Ask the question, compare to answer, if doesn't match ask for verification"""
    userAnswer = input("Question: {0} ".format(question))
    exitTokens = ['X', 'EXIT', 'Q', 'QUIT']
    if(userAnswer.upper() in exitTokens and userAnswer not in exitTokens):
        return None
    if(userAnswer != answer):
        if userAnswer == '':
            print('Answer was: {0}'.format(answer))
            _ = input('Press any key to continue...')
            return False
        check = input("Answer was     : {0}\nYour answer was: {1}\nIs this correct? ".format(answer,userAnswer))
        if(check.upper() not in ['Y','YES', 'T', 'TRUE']):
            return False
    return True

def EightsQuizFunction(vocabWords):
    """Cut the quiz into eights, then quiz over each section until 100% accuracy"""
    session = dict()
    vocabWords = ShuffleList(vocabWords)
    def sortingFunction(x):
        if x['tried'] != 0:
            return x['failed'] / x['tried']
        else:
            return 1
    vocabWords.sort(key=sortingFunction,reverse=True)
    sections = [x for x in CutIntoLengths(vocabWords,8)]
    lengthOfSections = len(sections)
    for count,section in enumerate(sections):
        wrongWords = [x for x in section]
        while(wrongWords != []):
            lastWrongWord = wrongWords[-1]
            wrongWords = ShuffleList(wrongWords)
            if wrongWords[0] == lastWrongWord:
                wrongWords = wrongWords[1:] + [lastWrongWord]
            Clear()
            print('{1} of {2} {0}%'.format(100.0 * count / lengthOfSections, count, lengthOfSections))
            futureWrongWords = []
            for word in wrongWords:
                question, answer = word['question'], word['answer']
                result = AskQuestion(question,answer)
                if question not in session.keys():
                    session[question] = {'tried' : 0, 'failed' : 0}
                if result == None:
                    return (session, vocabWords)
                elif result == False:
                    word['failed'] += 1
                    session[question]['failed'] += 1
                    futureWrongWords.append(word)
                    while result == False:
                        if result != "":
                            Clear()
                        result = AskQuestion(question,answer)
                word['tried'] += 1
                session[question]['tried'] += 1
                word['lastAsked'] = GetTime()
            wrongWords = futureWrongWords    
    return (session, vocabWords)
            
def StandardQuizFunction(vocabWords):
    """Randomize list and iterate through the entire thing"""
    vocabWords = ShuffleList(vocabWords)
    for word in vocabWords:
        question = word['question']
        answer = word['answer']
        word['tried'] += 1
        userAnswer = input("Question: {0} ".format(question))
        if(userAnswer.upper() in ['X', 'EXIT', 'Q', 'QUIT']):
            break
        if(userAnswer != answer):
            check = input("Answer was: {0}\nYour answer was: {1}\nIs this correct? ".format(answer,userAnswer))
            if(check.upper() in ['Y','YES', 'T', 'TRUE']):
                pass
            else:
                word['failed'] += 1
    return (vocabWords, vocabWords)

def Quiz(quizObj, quizFunction):
    session, quizObj['vocab'] = quizFunction(quizObj['vocab'])
    attempted = [x for x in session.keys() if session[x]['tried'] > 0]
    for question in attempted:
        tried = session[question]['tried']
        succeeded = tried - session[question]['failed']
        print('"{0}": {1} of {2} ({3:.2%})'.format(question, succeeded, tried, succeeded * 1.0 / tried))
    totalAttempted = sum([session[x]['tried'] for x in attempted])
    totalFailed = sum([session[x]['failed'] for x in attempted])
    totalSucceeded = 0.0
    successPercentage = 0.0
    if totalAttempted > 0.0:
        if totalFailed > 0.0:
            totalSucceeded = totalAttempted - totalFailed
        successPercentage = totalSucceeded / totalAttempted
    totalTried = sum([session[x]['tried'] for x in attempted])
    totalWords = len(quizObj['vocab'])
    print('Total tried: {0} of {2} Percentage Success: {1:.2%}'.format(totalAttempted, successPercentage, totalWords))
    return quizObj
