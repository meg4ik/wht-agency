FROM python:3.8

WORKDIR /wht-agency

ENV DJANGO_SECRET_KEY='django-insecure-w1pjm&(eomrjo*ui$y_^yq2v-6424^tot%qe5t*uz!-i0u%f%t'
ENV DJANGO_DEBUG=''

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /wht-agency/wht_test_proj

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wht_test_proj.wsgi:application"]
