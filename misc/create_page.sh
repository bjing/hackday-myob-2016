#!/bin/bash
TITLE="Test page 2"

curl -X POST -H 'Authorization:Basic TOKEN' -H 'Content-Type: application/json' -d'{"type":"page","title":"${TITLE}","space":{"key":"HAC"},"body":{"storage":{"value":"<p>This is a new test page</p>","representation":"storage"}}}' https://brianjing.atlassian.net/wiki/rest/api/content/
