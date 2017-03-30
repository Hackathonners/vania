\* Fair Distribution Problem *\
Minimize
obj: weight_diff_0 + weight_diff_1 + x00 + 2 x01 + 2 x10 + x11
Subject To
Task_0_must_be_done: x00 + x10 = 1
Task_1_must_be_done: x01 + x11 = 1
abs_negative_effort_diff_0: - weight_diff_0 - x00 - 2 x01 + 2 x10 + x11 <= 0
abs_negative_effort_diff_1: - weight_diff_1 + x00 + 2 x01 - 2 x10 - x11 <= 0
abs_positive_effort_diff_0: - weight_diff_0 + x00 + 2 x01 - 2 x10 - x11 <= 0
abs_positive_effort_diff_1: - weight_diff_1 - x00 - 2 x01 + 2 x10 + x11 <= 0
Binaries
x00
x01
x10
x11
End
