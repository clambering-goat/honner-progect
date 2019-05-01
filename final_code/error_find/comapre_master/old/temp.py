

min_x=55
picels_error_margion=5


for current_x_mm in range(50,60):
    if current_x_mm > min_x - picels_error_margion and current_x_mm < min_x + picels_error_margion:
        print(current_x_mm)