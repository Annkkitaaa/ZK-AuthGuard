// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVerifier {
    function verifyProof(
        bytes memory proof,
        uint[] memory input
    ) external view returns (bool);
}

contract ZkSnarkVerifier {
    IVerifier public verifier;

    constructor(address _verifierAddress) {
        verifier = IVerifier(_verifierAddress);
    }

    function authenticate(bytes memory proof, uint[] memory input) public view returns (bool) {
        return verifier.verifyProof(proof, input);
    }
}
