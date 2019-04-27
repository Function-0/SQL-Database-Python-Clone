# k and smallest_index were swapped in key i
# perform that swap in all keys after i.
def propagate(t, keys, future, k, smallest_index):
  for i in range(future, len(keys)):
    lst = t[keys[i]]
    lst[smallest_index], lst[k] = lst[k], lst[smallest_index]

def find_min(L, i, j):
  '''(list, int, int) -> int
  Return the index of the smallest item in L[i:j].
  '''
  smallest_index = i
  for k in range(i + 1, j):
      if L[k] < L[smallest_index]:
        smallest_index = k
  return smallest_index

def selection_sort(L, i, j, t, keys, future):
  '''(list, int, int) -> NoneType
  Sort the elements of L[i:j] in non-descending order.
  Also update remaining keys.
  '''
  for k in range(i, j):
    smallest_index = find_min(L, k, j)
    L[smallest_index], L[k] = L[k], L[smallest_index]
    propagate(t, keys, future, k, smallest_index)

def sort_part(t, keys, lower, upper, i):
  selection_sort(t[keys[i]], lower, upper, t, keys, i + 1)

def sort_key(t, keys, buckets, i):
  lower = 0
  for bucket in buckets:
    upper = bucket
    sort_part(t, keys, lower, upper, i)
    lower = upper
    

def sort_table(t, keys):
  '''Sort a table by its first column, then further sort 
  on second column etc.'''
  
  num_rows = len(t[keys[0]])
  buckets = [num_rows]
  for i in range(len(keys)):
    sort_key(t, keys, buckets, i)
    newbuckets = []
    lst = t[keys[i]]
    lower = 0
    for bucket in buckets:
      upper = bucket
      for i in range(lower, upper - 1):
        if lst[i] != lst[i + 1]:
          newbuckets.append(i + 1)
      newbuckets.append(upper)
      lower = upper
    buckets = newbuckets

def equiv_tables(t1, t2):
  '''Return True if tables t1 and t2 are equivalent.'''
  
  keys1 = list(t1.keys())
  keys2 = list(t2.keys())
  keys1.sort()
  keys2.sort()
  if keys1 != keys2:
    return False
  # tables have the same keys...
  sort_table(t1, keys1)
  sort_table(t2, keys1)
  #print(keys1)
  #print(t1)
  #print(t2)
  for k in keys1:
    if t1[k] != t2[k]:
      return False
  return True



t1 = {'a': ['b', 'c', 'q', 'b', 'c', 'q'], 'x': ['y', 'z', 'r', 'y', 'z', 'r'],
       'd': ['e', 'e', 'e', 'f', 'f', 'f'], 'u': ['v', 'v', 'v', 'w', 'w', 'w']}   
t1keys = list(t1.keys())
sort_table(t1, t1keys)
