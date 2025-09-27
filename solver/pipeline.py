from solver import solver
from test import graph as test_graph, n as test_n
from test_series_parallel import graph as test_graph_sp, n as test_n_sp
from test_wheat_stone import graph as test_graph_ws, n as test_n_ws
from multi_volt_source import graph as test_graph_mv, n as test_n_mv


# ans=solver(test_n,test_graph)
# print(ans)

# ans=solver(test_n_sp,test_graph_sp)
# print(ans)  

# ans=solver(test_n_ws,test_graph_ws)
# print(ans)

ans=solver(test_n_mv,test_graph_mv)
print(ans)
