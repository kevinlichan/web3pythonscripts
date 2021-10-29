from web3 import Web3
import pandas as pd
import numpy as np

infura_url = <INSERT INFURA URL HERE>
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

## Generating an array of random intergers (block numbers) since the Homestead network upgrade to the current block
randomBlock = np.random.randint(1150000, web3.eth.get_block_number(), size = 5000)

## Setting up the dataframe to capture the block, txn, address, and balance
df = pd.DataFrame(columns=['block','transaction','to_address', 'eth_balance'])

for i in randomBlock:
  txnCount = web3.eth.get_block_transaction_count(int(i)) - 1
  if txnCount > 0:
      txn = web3.eth.get_transaction_by_block(int(i), txnCount) ## Getting txn 0 for each random block
      if isinstance(txn['to'], str):
        balance = web3.eth.getBalance(txn['to']) ## Balance returned in Wei
        df2 = pd.DataFrame([(int(i), txnCount, txn['to'], balance)], columns=['block','transaction','to_address', 'eth_balance'])
        df = df.append(df2)

print("complete")
df.to_csv('eth_balances.csv')