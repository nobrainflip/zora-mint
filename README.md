# Software for automated Mint of free NFTs on Zora network

### Installation

In the project folder, open the terminal and run pip install -r requirements.txt

### Configuration

Settings can be found in config.py:
* private_keys_file — the path to the file containing private keys
* proxies_file — the path to the file containing proxies
* database_file — the path to the database file
* nfts_to_mint — a dictionary in the format address: quantity, where address — is NFT address in Zora network, quantity — is the amount required for free minting
* database_autocreate — a parameter that controls automatic database creation when the script is launched. It takes values:
* * True — auto-creation is enabled
* * False — auto-creation is disabled (the database stored at the path specified in database_file parameter will be used when launching)
* use_proxy — a parameter that determines whether proxies are used. It takes values:
* * True — proxies are used (the number of proxies should be equal to the number of wallets)
* * False — proxies are not used (in this case, the contents of the proxy file are ignored)
* min_balance —  the minimum wallet balance (if the balance is below this value, NFTs will not be minted)
* sleep_time — the waiting time between mints (in seconds; a random number is chosen within this interval)
* gas_multiplier — a multiplier for calculating gas prices for transactions
* gas_threshold — The maximum gas price in Gwei, at which a bridge will be used (if the price is higher, the script will wait until the gas price reaches the specified threshold)
* `gas_delay_range`— the range of time delay between checking the current gas price in seconds (a random number is chosen within this interval)
* zora_rpc — the RPC used for Zora
* eth_rpc — the RPC used for Ethereum mainnet

### Running

Before running, make sure all the required private keys for wallets are added to the data/private_keys.txt file

Please note that Zora does not allow IP addresses from the CIS region, so you will need proxies to use the software (only if you are in the mentioned countries). For this purpose, there is a proxies.txt file in the data folder, where proxies are specified in the format username:password@ip:port (1 proxy = 1 account)

To run the script, open the console and type: python main.py

Built by @sybil-v-zakone