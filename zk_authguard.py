import subprocess
import os

# Define the path where ZoKrates is installed
ZOKRATES_PATH = '/path/to/zokrates'  # Update this path to your ZoKrates installation directory

def run_zokrates_command(command):
    """Run a ZoKrates command and return the output."""
    result = subprocess.run([os.path.join(ZOKRATES_PATH, command)], capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"Error running command '{command}': {result.stderr}")
    return result.stdout

def generate_proof(inputs):
    """Generate a zk-SNARK proof."""
    # Compile the ZoKrates program
    run_zokrates_command("compile -i my_program.zok")
    
    # Setup the trusted setup
    run_zokrates_command("setup")
    
    # Compute witness
    input_str = ' '.join(map(str, inputs))
    run_zokrates_command(f"compute-witness -a {input_str}")
    
    # Generate proof
    proof_output = run_zokrates_command("generate-proof")
    print("Proof generated successfully.")
    return proof_output

def verify_proof():
    """Verify a zk-SNARK proof."""
    verify_output = run_zokrates_command("verify")
    return "Proof is valid" in verify_output

# Example usage
if __name__ == "__main__":
    # Define inputs for proof generation
    inputs = [1, 2]  # Replace with actual inputs for your program

    # Generate proof
    proof = generate_proof(inputs)
    print("Proof:", proof)
    
    # Verify proof
    if verify_proof():
        print("Proof is valid.")
    else:
        print("Proof is not valid.")
