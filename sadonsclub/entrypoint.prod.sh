#!/bin/sh

if [ "$POSTGRES_DB" = "sadonsclub_db" ]
then
    echo "Ждём postgres..."

    while ! nc -z "db" $POSTGRES_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL запущен"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"