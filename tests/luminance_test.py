from physycs.electromagnetism import calculate_luminance

# Hex colors
gray_color = "939291"
green_color = "97988e"

# Calculate luminance for both colors
luminance_tan = calculate_luminance(gray_color)
luminance_green = calculate_luminance(green_color)

print(luminance_tan, luminance_green)
