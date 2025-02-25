env:
	poetry env activate

runserver:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations $(ARG)

migrate:
	poetry run python manage.py migrate
	
superuser:
	poetry run python manage.py createsuperuser

runcss:
	npx @tailwindcss/cli -i ./blog/static/tailwind.css -o ./blog/static/css/blog.css --watch
