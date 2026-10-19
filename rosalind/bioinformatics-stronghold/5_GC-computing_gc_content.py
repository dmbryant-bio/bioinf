from pathlib import Path

file_path = Path(__file__).parent / "rosalind_gc.txt"

seq_set = {}
current_seq_id = None

with open(file_path) as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            current_seq_id = line[1:]
            seq_set[current_seq_id] = {
                "sequence": "",
                "gc_content": 0
            }
        else:
            seq_set[current_seq_id]["sequence"] += line

for seq_id, data in seq_set.items():
    sequence = data["sequence"]
    gc_count = sequence.count('G') + sequence.count('C')
    data["gc_content"] = (gc_count / len(sequence)) * 100

# Find the sequence with the highest GC content
max_gc_id = max(seq_set, key=lambda k: seq_set[k]["gc_content"])
print(f"{max_gc_id}\n{seq_set[max_gc_id]['gc_content']:.6f}")