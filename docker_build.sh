#!/bin/sh

docker build --tag=wpeisert/dash -f dash_base/Dockerfile .
docker push wpeisert/dash

docker build --tag=wpeisert/test_dash .
docker push wpeisert/test_dash
