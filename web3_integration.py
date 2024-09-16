from web3 import Web3

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # Update with your Ethereum node URL

# Load the smart contract
contract_address = '0x...'  # Address of the deployed contract
abi = [...]  # ABI of the deployed contract
contract = w3.eth.contract(address=contract_address, abi=abi)

def send_proof_to_contract(proof, input_data):
    """Send zk-SNARK proof and input data to the smart contract."""
    # Prepare transaction
    txn = contract.functions.authenticate(proof, input_data).buildTransaction({
        'chainId': 1,  # Mainnet chain ID or testnet ID
        'gas': 2000000,
        'gasPrice': w3.toWei('20', 'gwei'),
        'nonce': w3.eth.getTransactionCount('0xYourAddress')  # Replace with your address
    })

    # Sign and send transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key='0xYourPrivateKey')  # Replace with your private key
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Wait for transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return receipt

# Example usage
if __name__ == "__main__":
    proof = '...'  # Replace with your zk-SNARK proof
    input_data = [1, 2]  # Replace with your input data
    receipt = send_proof_to_contract(proof, input_data)
    print("Transaction receipt:", receipt)
