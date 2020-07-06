# Cross-Layer Deanonymization Methods in the Lightning Protocol

## [Work in progress]
This repository is going to host the relevant code and the data to reproduce 
the results of the [research paper][arxiv].

## Abstract

Payment channel networks (PCNs) have emerged as a promising alternative to 
mitigate the scalability issues inherent to cryptocurrencies like Bitcoin and 
are often assumed to improve privacy, as payments are not stored on chain. 
However, a systematic analysis of possible deanonymization attacks is still 
missing. In this paper, we focus on the Bitcoin Lightning Network (LN), which 
is the most widespread implementation of PCNs to date. We present clustering 
heuristics that group Bitcoin addresses, based on their interaction with the 
LN, and LN nodes, based on shared naming and hosting information. We also 
present cross-layer linking heuristics that can, with our dataset, link 43.7% 
of all LN nodes to 26.3% Bitcoin addresses interacting with the LN. These 
cross-layer links allow us to attribute information (e.g., aliases, IP 
addresses) to 17% of the Bitcoin addresses contributing to their 
deanonymization. Further, we find the security and privacy of the LN are at the
mercy of as few as five actors that control 34 nodes and over 44% of the total
capacity. Overall, we present the first quantitative analysis of the security
and privacy issues opened up by cross-layer interactions, demonstrating 
their impact and proposing suitable mitigation strategies. 


## How to

In what follows, we present the steps we took in order to produce the results
in the paper. Some steps rely on the [GraphSense API][GS API]. You may choose 
to get an API token to query on-chain data running our scripts or use the data 
we already fetched and stored in `data/layer_1` and `data/layer_2`.

#### Requirements

- python3
- [`git lfs`][git lfs]
- `pip install -r requirements.txt`
- [optional] an API token for [GraphSense][GS API]

Below the steps needed to reproduce the results.

#### Get LN data

Run an [LND][LND] node and export the LN graph using the `describegraph` 
command every 30 minutes.

Split data into `channel.csv`, `ip_address.csv` and `node.csv` and place them 
in `data/layer_2`.

#### Get funding and settlement txs

Use the channel points in `channel.csv` to get the details of the funding 
transactions by querying the [GraphSense API][GS API] and store the 
results in `data/layer_1/funding_txs.json`:

    python3 get_funding_txs.py

Use the funding transactions and the channel points to get the details of the
 settlement transactions and the settlement addresses by querying the 
 [GraphSense API][GS API] and store the results in 
 `data/layer_1/funded_address_settlement_txs.json` and 
 `data/layer_1/settlement_addresses.json`:

    python3 get_funded_address_settlement_txs.py

#### Get mapping of funding and settlement address to entities

Map funding and settlement addresses to funding and settlement entities by 
querying the [GraphSense API][GS API] and store the results in 
`data/layer_1/funding_address_entity.json` and 
`data/layer_1/settlement_address_entity.json`:

    python3 get_funding_address_entity.json
    python3 get_settlement_address_entity.json

#### Perform on-chain clustering heuristics

Use the funding and settlement entities to retrieve source and destination 
entities by querying the [GraphSense API][GS API]:

    ...

Cluster source, funding, settlement and destination entities into components 
(star, snake, collector and proxy).

    ...

#### Perform off-chain clustering heuristics

Use aliases and IP addresses to cluster nodes:

    ...

#### Perform cross-layer linking heuristics

Retrieve from the [Blockstream API][BS API] the funding transactions that use 
coins from settlement transactions:

    python3 get_reused_coins_txs.py

Sort stars, snakes and proxies and assign them unique IDs:

    python3 sort_mapping_entities.py
    
Use results from on-chain clustering heuristics to link Bitcoin entities to LN 
nodes. Two linking heuristics are available. 

    python3 LN_BTC_heuristic_1.py
    python3 LN_BTC_heuristic_2.py

The results are stored in `data/results/`. In particular, 
`filtered_heuristic_2_results.json` and `filtered_heuristic_2_results.json` 
report absolute and relative numbers of linked entities and nodes, while 
`*_entity_node.json` and `*_node_entity.json` contain the actual links (from 
entity to node and vice versa). On-chain patterns used before the linking 
heuristics are mentioned in the file name, e.g., 
`star_heuristic_1_entity_node.json` contains the mapping from entity to node 
using the star-pattern on top of the standard multi-input clustering heuristic.
When `filtered_` is prepended to the file name, it means that, to the best of 
our knowledge, no exchanges or similar services are in the dataset (please, 
refer to the paper for further details).


#### Perform attacks on the LN

Use the results of the LN node clustering heuristic to evaluate the security 
and privacy of the LN:

    ...
    
---

### Notes
- last block height (for computing multi-input clustering): 618857


[arxiv]: https://arxiv.org/abs/2007.00764
[git lfs]: https://git-lfs.github.com/
[LND]: https://github.com/lightningnetwork/lnd
[GS API]: https://api.graphsense.info/
[BS API]: https://github.com/Blockstream/esplora/blob/master/API.md