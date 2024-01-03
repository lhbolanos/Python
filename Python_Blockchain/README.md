# Blockchain with PoW

Building a Blockchain in Python

Description: This program builds a functioning Blockchain in Python.

Concepts:
- Proof of Work
- Blocks
- Transactions
- Endpoints
- Consensus

Environemnt:
- Anaconda is used to manage the environment.

Blockchain:
- Our blockchain consists of several blocks which link back to previous blocks via an internal hash.
- A genesis block is generated to act as the initial block to instantiate the block chain.
- A proof of work algorithm is utilized to generated new blocks or mine on the blockchain.
- PoW algorithm aims to generate proof that produces a hash with four leading zeroes.
- Generated Blockchain is treated as API and communicated with via HTTP requests using the Flask framework.
- The Mining Endpoint is responsible for the PoW calculations, transaction/reward assignment, and new Block generation.
- Consensus Algorithm is implemented via establishment of an auhtoritative chain across all nodes in a network. 
