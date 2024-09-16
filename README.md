

# ZK-AuthGuard

## Overview

ZK-AuthGuard is a privacy-preserving authentication system that leverages zk-SNARKs (Zero-Knowledge Succinct Non-Interactive Arguments of Knowledge) for authentication verification without revealing any sensitive information. This project consists of both Python scripts and Solidity smart contracts, allowing users to generate proofs via ZoKrates and interact with the Ethereum blockchain.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup ZoKrates](#setup-zokrates)
- [Python Scripts](#python-scripts)
  - [Generate and Verify Proof](#generate-and-verify-proof)
  - [Integrate with Smart Contract](#integrate-with-smart-contract)
- [Solidity Smart Contract](#solidity-smart-contract)
  - [Deploy the Smart Contract](#deploy-the-smart-contract)
- [Summary of Execution Steps](#summary-of-execution-steps)
- [License](#license)

## Prerequisites

To get started with the **ZK-AuthGuard** project, ensure that you have the following installed:

- **Python 3.8+**
- **ZoKrates** (for zk-SNARK proof generation)
- **Node.js** and **npm**
- **Hardhat** (for deploying Solidity contracts)
- **Web3.py** (for Ethereum integration)
- **An Ethereum node** (for smart contract interactions, e.g., via Infura or Ganache)

## Setup ZoKrates

Before running the Python scripts, you need to set up ZoKrates, which is used to generate zk-SNARK proofs.

1. Install ZoKrates by following the official [ZoKrates Installation Guide](https://zokrates.github.io/gettingstarted.html).
2. Ensure that ZoKrates is accessible via the system path as it will be invoked by the Python scripts.

## Python Scripts

The Python scripts are responsible for generating zk-SNARK proofs and interacting with the Ethereum smart contract.

### 1. Generate and Verify Proof

File: `zk_authguard.py`

This script generates a zk-SNARK proof using ZoKrates and verifies the proof locally.

```bash
python zk_authguard.py
```

Make sure to update the script with the correct ZoKrates file paths and other required parameters.

### 2. Integrate with Smart Contract

File: `web3_integration.py`

This script interacts with the deployed Ethereum smart contract to send the zk-SNARK proof and the input data for verification on-chain.

```bash
python web3_integration.py
```

In this script, you'll need to replace the placeholder values, such as:
- Ethereum contract address
- Private key
- Infura/Alchemy URL or local node URL

## Solidity Smart Contract

The project includes a Solidity smart contract for verifying zk-SNARK proofs on the Ethereum blockchain.

### 1. Deploy the Smart Contract

File: `deploy.js`

This file is a Hardhat script used to deploy the smart contract to an Ethereum network. 

First, ensure that Hardhat is installed:

```bash
npm install --save-dev hardhat
```

Then initialize Hardhat in your project directory:

```bash
npx hardhat
```

To deploy the contract, run:

```bash
npx hardhat run scripts/deploy.js --network <network>
```

Replace `<network>` with the desired target, such as `localhost` for a local blockchain or `ropsten` for an Ethereum testnet. Make sure the `hardhat.config.js` file is properly configured with network details.

## Summary of Execution Steps

1. **Generate and Verify Proof**:  
   Run `zk_authguard.py` to generate and verify zk-SNARK proofs locally.

   ```bash
   python zk_authguard.py
   ```

2. **Deploy the Smart Contract**:  
   Deploy the smart contract to the Ethereum network by running:

   ```bash
   npx hardhat run scripts/deploy.js --network <network>
   ```

3. **Integrate with the Smart Contract**:  
   Interact with the deployed smart contract and send the zk-SNARK proofs using:

   ```bash
   python web3_integration.py
   ```


---

Feel free to update the project to add new features or modify existing functionality. Contributions are welcome!

