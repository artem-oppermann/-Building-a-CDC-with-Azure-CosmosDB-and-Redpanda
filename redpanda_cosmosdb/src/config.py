import os

settings = {
	'host': os.environ.get('ACCOUNT_HOST', 'https://<cosmosinstance-name>.documents.azure.com:443/'),
	'master_key': os.environ.get('ACCOUNT_KEY', '<cosmosdbprimarykey>'),
	'database_id': os.environ.get('COSMOS_DATABASE', '<cosmosdb-name>'),
	'container_id': os.environ.get('COSMOS_CONTAINER', '<cosmosdb-container>'),
}
