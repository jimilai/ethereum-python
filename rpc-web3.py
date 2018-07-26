from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
print('version => {0}'.format(w3.manager.request_blocking('web3_clientVersion',[])))
print('keccak hash => {0}'.format(w3.manager.request_blocking('web3_sha3',['hello,ethereum'])))
