init:
	pip install -r requirements.txt

test:
	nosetests tests

search_user:
	python -m automagit.automate_git search_user --param 404answernotfound

project_check:
	python -m automagit.automate_git project_check
