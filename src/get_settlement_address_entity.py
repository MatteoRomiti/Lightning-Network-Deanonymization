# This script fetches the entity IDs of settlement addresses from the
# GraphSense API (access token needed) starting from a list of settlement
# addresses.

from utils import read_json, write_json, fill_address_entity

input_dir = '../data/layer_1/'
input_file = input_dir + 'settlement_addresses.json'

output_dir = '../data/layer_1/'
output_file = output_dir + 'settlement_address_entity.json'

settlement_addresses = read_json(input_file)

settlement_address_entity = dict()
for sa in settlement_addresses:
    settlement_address_entity[sa] = None

settlement_address_entity = fill_address_entity(settlement_address_entity)
write_json(settlement_address_entity, output_file)
