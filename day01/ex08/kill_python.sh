kill -9 $(ps -eo comm,pid,etimes | awk '/^python3/ {if ($3 > 3) { print $2}}')