







def x_pixel_to_mm(distance_to_object_mm,number_of_pixels):
    mm_size = (distance_to_object_mm / 1000) * 1.7 * number_of_pixels
    return mm_size


def x_mm_to_pixel(distance_to_object_mm, size_in_mm):
    pixels_size = size_in_mm / (1.7 * (distance_to_object_mm / 1000))
    return pixels_size




def y_pixel_to_mm(distance_to_object_mm, number_of_pixels):
    mm_size=(distance_to_object_mm / 1000)*1.64*number_of_pixels
    return mm_size



def y_mm_to_pixel(distance_to_object_mm, size_in_mm):
    pixels_size = size_in_mm / (1.64 * (distance_to_object_mm / 1000))
    return pixels_size




#assuming costancet distance
vaule=x_mm_to_pixel(100,50)

print("constant distance",vaule)


vaule_2=x_mm_to_pixel(150,50)


print("varible disytance ",vaule_2)