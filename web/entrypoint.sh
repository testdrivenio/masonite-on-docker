#!/bin/sh

if [ "$DB_CONNECTION" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

craft migrate:refresh  # you may want to remove this
craft migrate

exec "$@"
