import sys

sys.setrecursionlimit(2000)

def reconstruct_and_postorder(N, in_order_list, pre_order_list):
    post_order_result = []
    in_order_map = {value: index for index, value in enumerate(in_order_list)}

    def _reconstruct(in_start, in_end, pre_start, pre_end):
        if in_start > in_end or pre_start > pre_end:
            return

        root_value = pre_order_list[pre_start]
        root_index_in_in_order = in_order_map[root_value]
        num_left_nodes = root_index_in_in_order - in_start
        
        _reconstruct(in_start, root_index_in_in_order - 1, 
                     pre_start + 1, pre_start + num_left_nodes)

        _reconstruct(root_index_in_in_order + 1, in_end, 
                     pre_start + num_left_nodes + 1, pre_end)

        post_order_result.append(root_value)

    _reconstruct(0, N - 1, 0, N - 1)
    
    return post_order_result

N = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
pre_order = list(map(int, sys.stdin.readline().split()))

result = reconstruct_and_postorder(N, in_order, pre_order)
print(*result)