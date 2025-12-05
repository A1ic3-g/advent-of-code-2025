from itertools import chain

class FreshItems:
    def __init__(self, fresh_ranges: list[str]):
        fresh_ranges = [    
            (int(r.split("-")[0]), int(r.split("-")[1]))
            for r in fresh_ranges
        ]
        self.fresh_ranges = fresh_ranges
        self.remove_overlapping_fresh_ranges()
    def is_fresh(self, item_id: int) -> bool:
        for start, end in self.fresh_ranges:
            if start <= item_id <= end:
                return True
        return False
    
    def get_fresh_items_from_list(self, item_ids: list) -> list[int]:
        return [int(item_id) for item_id in item_ids if self.is_fresh(int(item_id))]
    
    def count_fresh_items(self) -> set[int]:
        return sum([(e - s) + 1 for s, e in self.fresh_ranges])

    def remove_overlapping_fresh_ranges(self):
        self.fresh_ranges.sort()
        merged_ranges = []
        for current_start, current_end in self.fresh_ranges:
            if not merged_ranges or merged_ranges[-1][1] < current_start:
                merged_ranges.append((current_start, current_end))
            else:
                merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], current_end))
        self.fresh_ranges = merged_ranges

if __name__ == "__main__":
    with open("inputs/05.txt") as f:
        lines = [l.strip("\n") for l in f.readlines()]
    
    split_index = next(i for i, line in enumerate(lines) if not line)

    fresh_items = FreshItems(lines[:split_index])
    items_lines = lines[split_index + 1:]
    
    print("Part 1:")
    print(len(fresh_items.get_fresh_items_from_list(items_lines)))
    print("Part 2:")
    print(fresh_items.count_fresh_items())

    