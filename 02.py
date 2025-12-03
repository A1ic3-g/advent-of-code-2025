from itertools import chain
from functools import reduce, lru_cache

@lru_cache(None)
def factors(n):   
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_valid_id_01(id: int) -> bool:
    idStr = str(id)
    lenId = len(idStr)
    if idStr[0] == "0":
        return False

    if lenId % 2 != 0:
        return True

    midpoint = lenId//2
    h0 = idStr[:midpoint]
    h1 = idStr[midpoint:]

    if h0 == h1:
        return False
    
    return True

def is_valid_id_02(id: int) -> bool:
    idStr = str(id)
    lenId = len(idStr)

    if idStr[0] == "0":
        return False
    
    lenFactors = factors(lenId)
    lenFactors.discard(lenId)
    for f in lenFactors:
        co_f = lenId // f

        if idStr[:f] * co_f == idStr:
            return False
    
    return True
 

class IdRange:
    def __init__(self, rangeStr: str):
        r = rangeStr.split("-")
        self.start = int(r[0])
        self.end = int(r[1]) + 1
    def get_invalid(self, task: int):
        if task == 1:
            is_valid = is_valid_id_01
        else:
            is_valid = is_valid_id_02

        ids = range(self.start, self.end)
        return [id for id in ids if not is_valid(id)]

            
    

if __name__ == "__main__":
    with open("inputs/02.txt", "r") as f:
        ranges = [IdRange(r) for r in f.read().split(",")]
    
    task1 = sum(list(chain(*[r.get_invalid(1) for r in ranges])))

    #print([r.get_invalid(2) for r in ranges])
    invalid_ids_02 = list(chain(*[r.get_invalid(2) for r in ranges]))
    #print(invalid_ids_02)
    task2 = sum(invalid_ids_02)
    print(task2)