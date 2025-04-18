#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres is not running yet..."

    # Check host and port availability
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1
    done

    echo "PostgreSQL is running"
fi

exec "$@"
