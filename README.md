##Для запуску проекту

```sh
docker build -t wht-agency . 

docker run -it -p 8000:8000 wht-agency
```

або 

```sh
python manage.py migrate

python manage.py runserver
```