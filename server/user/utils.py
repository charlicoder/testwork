from decouple import config

from web3 import Web3, EthereumTesterProvider

ENV = config('ENV', 'test')


def get_eth_provider(env='test', provider_url=None):
    if env == 'test':
        w3 = Web3(EthereumTesterProvider())
    else:
        w3 = Web3(Web3.HTTPProvider(provider_url))
    
    if w3.is_connected():
        return w3
    else:
        None


def get_eth_balance(wallet_address):
    # Get balance (balance is in wei, the smallest unit of ether)
    web3 = get_eth_provider(ENV)
    if web3:
        balance_wei = web3.eth.get_balance(wallet_address)
    
        # Convert wei to ether
        balance_eth = web3.from_wei(balance_wei, 'ether')
        return balance_eth
    else:
        raise Exception('Web3 not connected')

