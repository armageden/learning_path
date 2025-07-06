def is_p1_better_than_p2(p1, p2):
  if p1['mark'] > p2['mark']:
    return True
  if p1['mark'] ==p2['mark'] and p1['id'] <p2['id']:
    return True
  return False

def manual_sort(items):
  item_count = len(items)
  result = list(items)
  for i in range(item_count):
    best_item_idx = i
    for j in range(i+1,item_count):
      if is_p1_better_than_p2(result[j], result[best_item_idx]):
        best_item_idx = j
    result[i], result[best_item_idx] = result[best_item_idx], result[i]
  return result

count = int(input())
id_list = list(map(int, input().split()))

mark_list = list(map(int, input().split()))

roster = []
for i in range(count):
  
  roster.append({"mark": mark_list[i],"id": id_list[i],"start_pos": i})

ranked_roster = manual_sort(roster)

permutation_map = [0] * count
for end_pos, person in enumerate(ranked_roster):
  
  start_pos = person["start_pos"]

  permutation_map[start_pos] = end_pos

visited = [False] * count
cycles = 0
for i in range(count):
  if not visited[i]:
    cycles += 1
    current_pos = i

#please work this time............
    while not visited[current_pos]:
      visited[current_pos] = True
      current_pos = permutation_map[current_pos]

swap_count = count - cycles
print(f"Minimum swaps: {swap_count}")

for person in ranked_roster:
  
  #please work this time............
  print(f"ID: {person['id']} Mark: {person['mark']}")