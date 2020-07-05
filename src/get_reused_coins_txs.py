# This script fetches txs from Blockstream API (useful to link a tx input to
# the previous tx) starting from a subset of funding txs where coins are
# reused.

from utils import get_blockstream_tx, write_json, on_chain_heuristics_list
from load_data import funding_address_entity, settlement_address_entity, \
    funding_txs, set_mapping

output_dir = '../data/layer_1/'
output_file = output_dir + 'blockstream_funding_txs.json'

# use all on-chain clustering heuristics to have a wider overlap
# then the linking heuristics will decide which triplets to use
och = {h: (True if h != 'none' else False) for h in on_chain_heuristics_list}

funding_address_entity, settlement_address_entity, = \
    set_mapping(funding_address_entity, settlement_address_entity, och)

fes = set(funding_address_entity.values())
ses = set(settlement_address_entity.values())
overlap_entities = fes.intersection(ses)

print('len overlap entities', len(overlap_entities))

useful_funding_txs = set()
settlement_entities = settlement_address_entity.values()
for ftx in funding_txs.values():
    for inp in ftx['inputs']:
        e = funding_address_entity[inp['address']]
        if e in overlap_entities and e in settlement_entities:
            useful_funding_txs.add(ftx['tx_hash'])
            break

print('len useful_funding_txs', len(useful_funding_txs))

blockstream_funding_txs = dict()
for i, ftx in enumerate(useful_funding_txs):
    print(i, end='\r')
    if ftx not in blockstream_funding_txs:
        blockstream_funding_txs[ftx] = get_blockstream_tx(ftx)

write_json(blockstream_funding_txs, output_file)
