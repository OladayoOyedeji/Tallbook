.ONESHELL:
run:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	export FLASK_APP=flask_app.py
	export FLASK_ENV=development
	firefox localhost:5000 &
	flask --app flask_app.py --debug run
init_sql:
	mysql --user=root --password=root < app/init.sql

git g:
	git add .
	git commit -m 'sync'
	git push
