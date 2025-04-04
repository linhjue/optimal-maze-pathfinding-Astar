
def get_cell_properties(cell_type):
    cell_properties = {
        0: {"time_cost" : 1, "score" : 0},
        1: {"time_cost" : float('inf'), "score" : None},
        2: {"time_cost" : 3, "score" : -1},
        3: {"time_cost" : 5, "score" : -3},
        4: {"time_cost" : 0.5, "score" : 2},
        5: {"time_cost" : 0.1, "score" : 1},
    }
    return cell_properties[cell_type]



print  ("Đường: ", get_cell_properties(0))
print  ("Tường: ", get_cell_properties(1))
print  ("Bãi Lầy: ", get_cell_properties(2))
print  ("Quái Vật: ", get_cell_properties(3))
print  ("Đá Quý: ", get_cell_properties(4))
print  ("Vùng Tăng Cường: ", get_cell_properties(5))
