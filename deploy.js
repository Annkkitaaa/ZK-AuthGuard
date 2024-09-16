const hre = require("hardhat");

async function main() {
    const ZkSnarkVerifier = await hre.ethers.getContractFactory("ZkSnarkVerifier");
    const verifierAddress = "0x...";  // Replace with the address of your zk-SNARK verifier contract
    const zkSnarkVerifier = await ZkSnarkVerifier.deploy(verifierAddress);

    await zkSnarkVerifier.deployed();

    console.log("ZkSnarkVerifier deployed to:", zkSnarkVerifier.address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
