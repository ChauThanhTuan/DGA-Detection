#!/bin/bash

IP=$(head -n 1 config.py)
curl -X POST "http://${IP:12:-1}:5601/api/index_patterns/index_pattern" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d' { "index_pattern": { "title": "classifyDomain" } } ' || echo SELKS_DGA
./selks_dga.py
