\* Fair Distribution Problem *\
Minimize
obj: weight_diff_0 + weight_diff_1 + weight_diff_2 + x00 + 2 x01 + 3 x02
 + 3 x10 + x11 + 2 x12 + 2 x20 + 3 x21 + x22
Subject To
Task_0_must_be_done: x00 + x10 + x20 = 1
Task_1_must_be_done: x01 + x11 = 1
Task_2_must_be_done: x02 = 1
abs_negative_effort_diff_0: - weight_diff_0 - 2 x00 - 4 x01 - 6 x02 + 3 x10
 + x11 + 2 x12 + 2 x20 + 3 x21 + x22 <= 0
abs_negative_effort_diff_1: - weight_diff_1 + x00 + 2 x01 + 3 x02 - 6 x10
 - 2 x11 - 4 x12 + 2 x20 + 3 x21 + x22 <= 0
abs_negative_effort_diff_2: - weight_diff_2 + x00 + 2 x01 + 3 x02 + 3 x10
 + x11 + 2 x12 - 4 x20 - 6 x21 - 2 x22 <= 0
abs_positive_effort_diff_0: - weight_diff_0 + 2 x00 + 4 x01 + 6 x02 - 3 x10
 - x11 - 2 x12 - 2 x20 - 3 x21 - x22 <= 0
abs_positive_effort_diff_1: - weight_diff_1 - x00 - 2 x01 - 3 x02 + 6 x10
 + 2 x11 + 4 x12 - 2 x20 - 3 x21 - x22 <= 0
abs_positive_effort_diff_2: - weight_diff_2 - x00 - 2 x01 - 3 x02 - 3 x10
 - x11 - 2 x12 + 4 x20 + 6 x21 + 2 x22 <= 0
Binaries
x00
x01
x02
x10
x11
x12
x20
x21
x22
End
