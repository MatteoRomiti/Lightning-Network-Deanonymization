# This script fetches the entity IDs of funding addresses
# from the GraphSense API (access token needed)
# starting from a list funding txs.

from utils import read_json, write_json, fill_address_entity

input_dir = '../data/joined/level_1/'
input_file = input_dir + 'funding_txs.json'

output_dir = '../data/joined/level_1/'
output_file = output_dir + 'funding_address_entity_test.json'

funding_txs = read_json(input_file)

funding_address_entity = dict()
for tx in funding_txs.values():
	for i in tx['inputs']:
		funding_address_entity[i['address']] = None

funding_address_entity = fill_address_entity(funding_address_entity)
write_json(funding_address_entity, output_file)
