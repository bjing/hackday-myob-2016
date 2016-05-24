
curl -u $CONFLUENCE_USERNAME:$CONFLUENCE_PASSWORD -X POST -H 'Content-Type: application/json' -d'{"type":"page","title":"test page 1","space":{"key":"HAC"},"body":{"storage":{"value":"<p>This is a new test page</p>","representation":"storage"}}}' https://brianjing.atlassian.net/wiki/rest/api/content/ | python -mjson.tool

