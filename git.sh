#!/bin/bash

echo "Start"

git init &&
git remote add origin git@github.com:jyldyzbek005/restaran.git &&
git add . &&
git commit -m "all" &&
git push origin master

echo "Finish"
