#!/bin/sh

docker-compose down
docker pull wpeisert/test_dash
docker-compose -f docker-compose.prod.yml up -d

