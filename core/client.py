from web3 import Web3

import config
from config import gas_threshold, gas_delay_range, min_balance
from constants import ZORA_ABI
from models.client_base import ClientBase
from utils import gas_delay


class ZoraMintClient(ClientBase):
    def __init__(
            self,
            w3: Web3,
            private_key: str,
            address: str,
            proxy
    ):
        super().__init__(w3, private_key=private_key, address=address)
        self.proxy = proxy

    @gas_delay(gas_threshold=gas_threshold, delay_range=gas_delay_range)
    def mint(self, nft_address: str, amount: int):
        eth_balance = self.w3.from_wei(self.w3.eth.get_balance(self.public_key), 'ether')
        if eth_balance < min_balance:
            return False, f"Insufficient balance to mint: {eth_balance} < {min_balance}\nSkipping wallet"

        nft_address = self.w3.to_checksum_address(nft_address)

        nft_contract = self.w3.eth.contract(
            address=nft_address,
            abi=ZORA_ABI
        )
        args = {
            'minter': Web3.to_checksum_address(config.minter_address),
            'tokenId': 1,
            'quantity': amount,
            'minterArguments': f'0x000000000000000000000000{self.public_key[2:]}',
            'mintReferral': Web3.to_checksum_address('0x2B8ed06cD76AD66bA9AEC19e6f760a923a949Da4')
        }
        data = nft_contract.encodeABI('mintWithRewards', args=list(args.values()))
        tx = self.send_tx(to_adr=nft_address, data=data, value=Web3.to_wei(0.000777 * amount, 'ether'))
        if self.verify_tx(tx):
            return (True, (
                f"Successfuly minted {nft_address}\n"
                f"https://explorer.zora.energy/tx/{tx.hex()}"))

        return False, f"Failed to mint {nft_address}"
