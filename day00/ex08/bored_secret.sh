curl --insecure -vvI https://www.boredapi.com/api/activity 2>&1 | awk 'BEGIN { cert=0 } /^\* SSL connection/ { cert=1 } /^\*/ { if (cert) print }'
