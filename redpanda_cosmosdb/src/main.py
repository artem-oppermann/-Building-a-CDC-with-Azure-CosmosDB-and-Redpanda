import datetime
import random
import uuid

import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

import config

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

def update_transaction(container, doc_id, updated_fields):

   print('\nUpdating Transaction\n')
   try:
   	item = container.read_item(item=doc_id, partition_key="Transaction")
   	print('Fetched Transaction to update: ', item)

   	for field, value in updated_fields.items():
       	item[field] = value
   	updated_item_response = container.replace_item(item=item['id'], body=item)
   	print('Updated item:', updated_item_response['id'])

   except exceptions.CosmosHttpResponseError as e:
   	print(f'An error occurred while updating the Transaction: {e.message}')

def create_transactions(container, n_transactions):

   print('\nCreating Transactions\n')

   for i in range(n_transactions):
   	transaction = {
       	'id': str(uuid.uuid4()),
       	'partitionKey' : 'Transaction',
       	'stock_symbol': random.choice(['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']),
       	'transaction_type': random.choice(['BUY', 'SELL']),
       	'transaction_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
       	'quantity': random.randint(1, 100),
       	'price_per_unit': round(random.uniform(100, 1500), 2),
       	'account_id': f"Trader{random.randint(1, 1000)}",
       	'ttl': 60 * 60 * 24 * 7  # 7 days
   	}

   	container.create_item(body=transaction)

def run():

	client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPythonQuickstart", user_agent_overwrite=True)
	try:
    	try:
        	db = client.create_database(id=DATABASE_ID)
        	print('Database with id \'{0}\' created'.format(DATABASE_ID))

    	except exceptions.CosmosResourceExistsError:
        	db = client.get_database_client(DATABASE_ID)
        	print('Database with id \'{0}\' was found'.format(DATABASE_ID))

    	try:
        	container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/partitionKey'))
        	print('Container with id \'{0}\' created'.format(CONTAINER_ID))

    	except exceptions.CosmosResourceExistsError:
        	container = db.get_container_client(CONTAINER_ID)
        	print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

    	create_transactions(container, n_transactions=2)
    
	except exceptions.CosmosHttpResponseError as e:
    	print('\n An error was caught. {0}'.format(e.message))


if __name__ == '__main__':
	run()
