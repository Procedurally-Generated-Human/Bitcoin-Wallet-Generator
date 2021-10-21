from bitcoin import *


class wallet_gen():
    def genrate (self, data):
        private_key = sha256(data)
        public_key = privkey_to_pubkey(private_key)
        address = pubkey_to_address(public_key)
        return private_key, public_key, address

