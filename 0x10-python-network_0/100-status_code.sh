#!/bin/bash
#sends a request to a URL passed as an arg, and displays the status response.
curl -s -L -X head -w "%{http_code}" "$1"
