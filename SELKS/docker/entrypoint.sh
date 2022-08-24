#!/bin/bash
# curl -X POST "http://172.16.60.10:5601/api/index_patterns/index_pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d' { "index_pattern": { "title": "tt" } } '
echo "${hostname -I}"

text="a"
text="${text} $(echo "b") c"
echo "${text}"