<p>
The answer was:<br />
<b>{{answer}}</b><br />
Your answer was:<br />
<b>{{user_answer}}</b><br />
<form method="POST" action="/test">
	<input name="Correct" value="Correct" type="submit" />
	<input name="Incorrect" value="Incorrect" type="submit" />
	<input name="Quit" value="Quit" type="submit" />
</form>
%rebase test_layout title="Self Check"