color_list1 = ["red", "green", "blue", "white", "black"]
color_list2 = ["green", "white", "orange"]
diff = [color for color in color_list1 if color not in color_list2]
print("Colors in color_list1 not in color_list2:", diff)
