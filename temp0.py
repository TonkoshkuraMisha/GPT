with open("dataset_395528_15.txt", "r") as file:
    m, q, r = map(int, file.readline().split())
    physical_memory = {}

    for _ in range(m):
        paddr, value = map(int, file.readline().split())
        physical_memory[paddr] = value

    for _ in range(q):
        logical_address = int(file.readline())
        pte_index = (logical_address >> 12) & 0xFF
        pde_index = (logical_address >> 21) & 0xFF
        pdpte_index = (logical_address >> 30) & 0xFF
        pml4e_index = (logical_address >> 39) & 0xFF

        pml4e_entry = physical_memory.get(r + pml4e_index * 8, 0)
        pdpte_entry = physical_memory.get((pml4e_entry & 0xFFFFFFFFFFFFF000) + pdpte_index * 8, 0)
        pde_entry = physical_memory.get((pdpte_entry & 0xFFFFFFFFFFFFF000) + pde_index * 8, 0)
        pte_entry = physical_memory.get((pde_entry & 0xFFFFFFFFFFFFF000) + pte_index * 8, 0)

        if pte_entry & 0x1:
            physical_address = (pte_entry & 0xFFFFFFFFFFFFF000) + (logical_address & 0xFFF)
            print(physical_address)
        else:
            print("fault")
