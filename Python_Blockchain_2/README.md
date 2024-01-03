# Blockchain with Transaction, Block and Chain Validation

Building a Blockchain in Python with Validation Checking

Description: This program builds a functioning Blockchain in Python with functional validation checking for transactions, blocks and the entire chain.

Concepts:
- Validation
- Blocks
- Transactions
- State
- Chain

Environemnt:
- Anaconda is used to manage the environment.

Blockchain:
- Our blockchain consists of several blocks which link back to previous blocks via an internal hash.
- A genesis block is generated to act as the initial block to instantiate the block chain, assigned an arbitrary value that will return as an invalid transaction expectantly.
- The rules for this system are: 1. The sum of deposits and withdrawals must be 0 (tokens are neither created nor destroyed) 2. A user's account must have sufficient funds to cover any withdrawals.
- Methods are utilized to check for validation across the blockchain.
- Block contents are checked to ensure a match against the hash, a block's parent and current system state are checked and returned as an updated state if valid, then the entire chain's system state is computed beginning at the genesis block and returned if the chain is valid.
