import sys

sys.setrecursionlimit(2000)

def reconstruct_and_preorder(N, in_order_list, post_order_list):
    pre_order_result = []
    in_order_map = {value: index for index, value in enumerate(in_order_list)}

    def _reconstruct(in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return

        root_value = post_order_list[post_end]
        pre_order_result.append(root_value)
        root_index_in_in_order = in_order_map[root_value]
        num_left_nodes = root_index_in_in_order - in_start
        
        _reconstruct(in_start, root_index_in_in_order - 1, 
                     post_start, post_start + num_left_nodes - 1)

        _reconstruct(root_index_in_in_order + 1, in_end, 
                     post_start + num_left_nodes, post_end - 1)

    _reconstruct(0, N - 1, 0, N - 1)
    
    return pre_order_result

N = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))

result = reconstruct_and_preorder(N, in_order, post_order)
print(*result)