def calculate_luminance(hex_color):
    # Convert hex to RGB
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    # Calculate luminance
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return luminance

# Hex colors
gray_color = "939291"
green_color = "97988e"

# Calculate luminance for both colors
luminance_tan = calculate_luminance(gray_color)
luminance_green = calculate_luminance(green_color)

print(luminance_tan, luminance_green)
