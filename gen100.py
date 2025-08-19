import os
from concurrent.futures import ThreadPoolExecutor

csmith_path = "/home/huangnengchao/csmith/Release"
output_path = "/home/huangnengchao/csmith/output"

def generate(seed):

    # gcc random1.c -I/home/huangnengchao/csmith/Release/include -o random1
    print(f"Generating with seed {seed:04d}")
    os.system(f"{csmith_path}/bin/csmith -s {seed} > {output_path}/src/c{seed:04d}.c")

    print(f"Compiling with c{seed:04d}.c")
    os.system(f"gcc {output_path}/src/c{seed:04d}.c -I{csmith_path}/include -o {output_path}/bin/c{seed:04d}.out")

if __name__ == "__main__":
    os.system("mkdir -p " + output_path + "/src")
    os.system("mkdir -p " + output_path + "/bin")
    os.system("rm -f " + output_path + "/src/c*.c")
    os.system("rm -f " + output_path + "/bin/c*.out")
    # Define the range of seeds to generate
    # Adjust the range as needed    
    seeds = range(1, 20)
    # Set the number of threads (adjust as needed)
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(generate, seeds)

