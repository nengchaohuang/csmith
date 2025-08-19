import os
from concurrent.futures import ThreadPoolExecutor
import subprocess

gen100_script = "/home/huangnengchao/csmith/gen100.py"
output_bin_path = "/home/huangnengchao/csmith/output/bin"

def run_test(seed):
    # Generate the output using gen100.py
    # print(f"Running gen100.py for seed {seed:04d}")
    # subprocess.run(["python3", gen100_script, str(seed)], check=True)

    # Test the generated binary
    binary_path = f"{output_bin_path}/c{seed:04d}.out"
    if os.path.exists(binary_path):
        print(f"Testing {binary_path}")
        try:
            result = subprocess.run([binary_path], capture_output=True, text=True, timeout=20)
            # Get exit code and output
            print(f"Exit code for c{seed:04d}.out: {result.returncode}")
            print(f"Output for c{seed:04d}.out:\n{result.stdout}")
        except subprocess.TimeoutExpired:
            print(f"Testing {binary_path}------------------------ timed out!")
    else:
        print(f"Binary {binary_path} not found!")

if __name__ == "__main__":
    # Define the range of seeds to test
    seeds = range(1, 20)

    # Set the number of threads for parallel execution
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_test, seeds)
