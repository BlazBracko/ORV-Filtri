#!/bin/bash

DOCKER_USERNAME="blazbracko"
REPO_NAME="orv-filtri"
IMAGE_TAG="2024-04-09--12-43-44"

# Prenesi Docker sliko
docker pull $DOCKER_USERNAME/$REPO_NAME:$IMAGE_TAG

# Zaženi Docker vsebnik
docker run -d $DOCKER_USERNAME/$REPO_NAME:$IMAGE_TAG
