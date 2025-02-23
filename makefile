migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

runserver:
	python3 manage.py runserver

runcss:
	npx @tailwindcss/cli -i ./blog/static/tailwind.css -o ./blog/static/css/blog.css --watch
