#!/bin/sh

CONTAINER=$1

if [ "x$CONTAINER" = "x" ]; then
  CONTAINER=web
fi

docker-compose exec --user $(id -u):$(id -g) $CONTAINER bash
