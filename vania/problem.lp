\* Fair Distribution Problem *\
Minimize
obj: effort_diff_0 + effort_diff_1 + effort_diff_2 + 3 x00 + 3 x01 + 3 x02
 + 3 x10 + 3 x11 + 3 x12 + 3 x20 + 3 x21 + 3 x22
Subject To
Task_0_must_be_done: x00 + x10 + x20 = 1
Task_1_must_be_done: x01 + x11 + x21 = 1
Task_2_must_be_done: x02 + x12 + x22 = 1
abs_negative_effort_diff_0: - effort_diff_0 - 6 x00 - 6 x01 - 6 x02 + 3 x10
 + 3 x11 + 3 x12 + 3 x20 + 3 x21 + 3 x22 <= 0
abs_negative_effort_diff_1: - effort_diff_1 + 3 x00 + 3 x01 + 3 x02 - 6 x10
 - 6 x11 - 6 x12 + 3 x20 + 3 x21 + 3 x22 <= 0
abs_negative_effort_diff_2: - effort_diff_2 + 3 x00 + 3 x01 + 3 x02 + 3 x10
 + 3 x11 + 3 x12 - 6 x20 - 6 x21 - 6 x22 <= 0
abs_positive_effort_diff_0: - effort_diff_0 + 6 x00 + 6 x01 + 6 x02 - 3 x10
 - 3 x11 - 3 x12 - 3 x20 - 3 x21 - 3 x22 <= 0
abs_positive_effort_diff_1: - effort_diff_1 - 3 x00 - 3 x01 - 3 x02 + 6 x10
 + 6 x11 + 6 x12 - 3 x20 - 3 x21 - 3 x22 <= 0
abs_positive_effort_diff_2: - effort_diff_2 - 3 x00 - 3 x01 - 3 x02 - 3 x10
 - 3 x11 - 3 x12 + 6 x20 + 6 x21 + 6 x22 <= 0
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
