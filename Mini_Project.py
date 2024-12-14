# MP_621428679_EEX5563_Worst Fit Implementation

def worst_fit_allocation(memory_blocks, processes):
    allocation = [-1] * len(processes)  # Track allocated block for each process

    for i in range(len(processes)):
        # Find the block with the largest size that can fit the process
        worst_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i]:
                if worst_idx == -1 or memory_blocks[j] > memory_blocks[worst_idx]:
                    worst_idx = j

        # If a suitable block was found, allocate it
        if worst_idx != -1:
            allocation[i] = worst_idx
            memory_blocks[worst_idx] -= processes[i]

    return allocation, memory_blocks


def user_input_block(memory_blocks, processes):
    print("\nInitial Memory Blocks:")
    for i, size in enumerate(memory_blocks):
        print(f"Block {i + 1}: {size} KB")

    print("\nProcesses to be Allocated:")
    for i, size in enumerate(processes):
        print(f"Process {chr(65 + i)} requires {size} KB")


def allocate_process(allocation, memory_blocks, processes):
    print("\nAllocation Process:")
    for i, block in enumerate(allocation):
        if block != -1:
            print(f"Process {chr(65 + i)} is allocated to Block {block + 1}")
        else:
            print(f"Process {chr(65 + i)} could not be allocated.")

    print("\nUpdated Memory Blocks:")
    for i, size in enumerate(memory_blocks):
        print(f"Block {i + 1}: {size} KB")

    print("\nFinal Memory State:")
    for i, size in enumerate(memory_blocks):
        status = "fully allocated" if size == 0 else "free"
        print(f"Block {i + 1}: {size} KB ({status})")

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Invalid input. Please enter a positive integer block size")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer block size")


def main():
    # Input memory blocks
    print("Enter the sizes of three memory blocks.")
    memory_blocks = []
    for i in range(3):
        size = get_valid_input(f"Block {i + 1} (KB): ")
        memory_blocks.append(size)

    # Input processes
    print("Enter the sizes of three processes.")
    processes = []
    for i in range(3):
        size = get_valid_input(f"Process {chr(65 + i)} (KB): ")
        processes.append(size)

    # Display initial state which user input
    user_input_block(memory_blocks, processes)

    # Perform allocation
    allocation, updated_memory_blocks = worst_fit_allocation(memory_blocks, processes)

    # Display allocation and final state
    allocate_process(allocation, updated_memory_blocks, processes)
    # allocated or not into blocks

if __name__ == "__main__":
    main()
