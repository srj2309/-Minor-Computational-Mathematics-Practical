# Short Python implementation: Northwest Corner method for Transportation Problem

def northwest_corner(costs, supply, demand):
    """Return allocation matrix and total cost using NW-corner method.
    costs: list of rows (m x n), supply: list length m, demand: list length n"""
    m, n = len(supply), len(demand)
    sup = supply.copy()
    dem = demand.copy()
    alloc = [[0]*n for _ in range(m)]
    i = j = 0
    while i < m and j < n:
        qty = min(sup[i], dem[j])
        alloc[i][j] = qty
        sup[i] -= qty
        dem[j] -= qty
        # move to next row/column when exhausted
        if sup[i] == 0 and i+1 < m and dem[j] == 0 and j+1 < n:
            # both zero -> advance column then row (common convention)
            j += 1
            i += 1
        elif sup[i] == 0:
            i += 1
        elif dem[j] == 0:
            j += 1
        else:
            # should not happen because qty = min(...) forces one to zero
            break
    # compute total cost
    total_cost = sum(alloc[r][c] * costs[r][c] for r in range(m) for c in range(n))
    return alloc, total_cost

# Example usage (from your screenshots)
if __name__ == "__main__":
    costs = [
        [8, 6, 10],   # O1 -> D1,D2,D3
        [10, 4, 9]    # O2 -> D1,D2,D3
    ]
    supply = [2000, 2500]      # supplies for O1,O2
    demand = [1500, 2000, 1000]# demands for D1,D2,D3

    allocation, cost = northwest_corner(costs, supply, demand)
    print("Allocation matrix (rows = origins, cols = destinations):")
    for row in allocation:
        print(row)
    print(f"\nTotal transportation cost (NW-corner): {cost:,}")
