from bottle import route, run, template, get, post, request, view

question = "What is red and smells like blue paint?"
answer = "Red Paint"

@get('/test')
@view('ask_question')
def InitialQuestion():
    return {'question' : question }

@post('/test')
def AskQuestion():
    userAnswer = request.forms.answer;
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
        print(', '.join(['{0}: {1}'.format(x,y) for (x,y) in zip(['isCorrect','isIncorrect','isQuit','isAskAgain'],[isCorrect,isIncorrect,isQuit,isAskAgain])]))
        if isCorrect != '':
            return template('ask_question',is_correct=True,question=question)
        elif isQuit != '':
            return template('quit')
        elif isAskAgain != '':
            return template('ask_question',question=question)
        else:
            return template('incorrect',question=question,answer=answer)

run(host='localhost', port=8383, debug=True)
