#!/bin/sh
set -e

echo "Waiting for Cassandra..."
until cqlsh db_cassandra -e "describe keyspaces"; do
  echo "Cassandra is unavailable - sleeping"
  sleep 5
done

echo "Cassandra is ready!"
exec "$@"
