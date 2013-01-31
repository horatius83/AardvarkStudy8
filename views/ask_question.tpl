% if defined('is_correct'):
<h2>Correct</h2>
% end
<p>
Question: <br/>
<b>{{question}}</b>
</p>
<form method="POST" action="/test">
	<input name="answer" type="text" />
	<input type="submit" value="Submit" />
</form>
%rebase test_layout title="Correct"