#!/bin/bash
echo Content-type: text/plain
echo

export PATH=~/bin/:$PATH

git pull

composer.phar install

echo I HAVE COMPLETED THE AUTO UPLOAD

