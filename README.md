# Cross-Layer Deanonymization Methods in the Lightning Protocol

This repository hosts the relevant code and the data to reproduce the results of the research paper.

------------

## Abstract

Payment channel networks (PCNs) have emerged as a promising alternative to mitigate the scalability issues inherent to cryptocurrencies like Bitcoin and are often assumed to improve privacy, as payments are not stored on chain. However, a systematic analysis of possible deanonymization attacks is still missing. In this paper, we focus on the Bitcoin Lightning Network (LN), which is the most widespread implementation of PCNs to date. We present clustering heuristics that group Bitcoin addresses, based on their interaction with the LN, and LN nodes, based on shared naming and hosting information. We also present cross-layer linking heuristics that can, with our dataset, link 43.7% of all LN nodes to 26.3% Bitcoin addresses interacting with the LN. These cross-layer links allow us to attribute information (e.g., aliases, IP addresses) to 17% of the Bitcoin addresses contributing to their deanonymization. Further, we find the security and privacy of the LN are at the mercy of as few as five actors that control 34 nodes and over 44% of the total capacity. Overall, we present the first quantitative analysis of the security and privacy issues opened up by cross-layer interactions, demonstrating their impact and proposing suitable mitigation strategies. 


## How to
