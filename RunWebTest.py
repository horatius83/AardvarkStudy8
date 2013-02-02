from bottle import route, run, template, get, post, request, view
from FileManagement import OpenJsonFile, ProcessJsonObj, OutputJsonFile

file = "./Vocabulary/N3.json"
jo = ProcessJsonObj(OpenJsonFile(file))
questions = jo['vocab']
index = 0

#question = "What is red and smells like blue paint?"
#answer = "Red Paint"

@get('/test')
@view('ask_question')
def InitialQuestion():
    question = questions[index]['question']
    return {'question' : question }

@post('/test')
def AskQuestion():
    global index
    userAnswer = request.forms.answer;
    answer = questions[index]['answer']
    question = questions[index]['question']
    if userAnswer == answer:
        return template('ask_question',is_correct=True,question=question)
    elif userAnswer != '': # reply is from ask_question
        print('User Answer: {0}'.format(userAnswer))
        return template('self_check',answer=answer,user_answer=userAnswer)
    else: # reply is from self_check
        print('Is Self-Check!')
        isCorrect = request.forms.Correct
        isIncorrect = request.forms.Incorrect
        isQuit = request.forms.Quit
        isAskAgain = request.forms.AskAgain

        if isCorrect != '':
            index += 1
            question = questions[index]['question']
            return template('ask_question',is_correct=True,question=question)
        elif isQuit != '':
            return template('quit')
        elif isAskAgain != '':
            return template('ask_question',question=question)
        else:
            return template('incorrect',question=question,answer=answer)

run(host='localhost', port=8383, debug=True)
