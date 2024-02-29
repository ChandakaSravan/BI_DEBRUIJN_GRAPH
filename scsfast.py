import itertools
import time
def overlap(read_a, read_b, min_length=1):
    start = 0
    while True:
        start = read_a.find(read_b[:min_length], start)
        if start == -1:
            return 0
        if read_b.startswith(read_a[start:]):
            return len(read_a) - start
        start += 1

def shortestCommonSuperstring(string_set):
    n = len(string_set)
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i][j] = overlap(string_set[i], string_set[j], min_length=1)

    # Generating all possible permutations of the strings
    permutations = list(itertools.permutations(range(n)))
    
    # Find the shortest superstring by trying all permutations
    shortest_sup = None
    for perm in permutations:
        sup = string_set[perm[0]]
        for i in range(n - 1):
            olen = adj[perm[i]][perm[i+1]]
            sup += string_set[perm[i+1]][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup

    return shortest_sup


# Measured the execution time and compared the old and updated code by taking same input in 2 different files
# After checking i've commented below code, as it might create conflict while running grading script
#start_time = time.time()

#strings = [ 'GAC','ACG','CGA','CGC','CGT','GCG','TCG','GAG','AGA']
#result = shortestCommonSuperstring(strings)
#print(result)  

#end_time = time.time()
#elapsed_time = end_time - start_time

#print("Elapsed time: ", elapsed_time, "seconds")
