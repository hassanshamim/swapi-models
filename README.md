To setup:
- clone the repo
- run the migrations `python manage.py migrate api`
- load the data with the following commands (in order):
```
	python manage.py loaddata planets.json
	python manage.py loaddata people.json
	python manage.py loaddata species.json
	python manage.py loaddata transport.json
	python manage.py loaddata starships.json
	python manage.py loaddata vehicles.json
	python manage.py loaddata films.json
```
