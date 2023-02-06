#!/bin/sh

echo "-- Start Migrations --"
manage migrate
manage showmigrations -l

echo "-- Collect Static --"
manage collectstatic --noinput

exec "$@"
