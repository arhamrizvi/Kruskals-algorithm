def swap(array, i, j):
    array[i], array[j] = array[j],array[i]


def quicksort(array):
    start = 0
    end = len(array)-1
    quicksort_aux(array, start, end)


def quicksort_aux(array, start, end):
    if start < end :
        boundary = partition(array, start, end)
        quicksort_aux(array, start, boundary)
        quicksort_aux(array, boundary+1, end)


def partition(array, start, end):
    mid = (start + end) // 2
    pivot = array[mid][2]
    swap(array, start, mid)
    index = start  # keep track of border
    for k in range(start+1, end+1):
        if array[k][2] < pivot:
            index += 1
            swap(array, k, index)
    swap(array, start, index)  # put pivot in correct position
    return index


"""""
Reference: ADS(FIT2004) supplementary notes
"""""
def find(x):  # time complexity: O(log(N))
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


arr = []
name = 'inputgraphfile.txt'
file = open(name)  # opens file and reads it
file = file.read()
var = file.splitlines()

for i in range(len(var)):
    line = var[i].split(' ')

    u = int(line[0])
    v = int(line[1])
    w = int(line[2])

    arr.append([u,v,w])
    if u>=v:
        N = u
    else:
        N = v


N+=1

parent = []

for j in range(N):
    parent.append(j)


rank = [0] * N

finalized = []

quicksort(arr)


i = 0

for edge in arr:
    u, v, weight = arr[i]
    i = i + 1

    if find(u) != find(v):
        finalized.append([u, v, weight])
        union(u, v)


file = open('output_kruskal.txt', 'w')
for u,v,w in finalized:
    file.write(str(u) + " ")
    file.write(str(v) + " ")
    file.write(str(w) + " "+ "\n")
file.close()