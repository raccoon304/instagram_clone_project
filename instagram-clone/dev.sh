#!/bin/bash
docker network create instaclone
docker run -d -p 9999:5432 -e POSTGRES_DB=service -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=1234 --name instaclone-db --net instaclone postgres
docker build -t instaclone:test C:\Users\smon0\Desktop\인스타그램_프로젝트\instagram-clone
docker run -it -p 9998:8000 -p 9997:3000 -v C:\Users\smon0\Desktop\인스타그램_프로젝트\instagram-clone:/code --name instaclone-01 instaclone:test


