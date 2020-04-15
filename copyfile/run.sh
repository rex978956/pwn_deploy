#!bin/sh
exec 2>/dev/null
timeout 120 ./$1
echo "\n\ntimeout"