COLOUR_TO_CODE = {"aliceblue": "#f0f8ff", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "aqua": "#00ffff", "beige": "#f5f5dc", "bistre": "#3d2b1f", "bittersweet": "#fe6f5e", "black": "#000000"}
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_TO_CODE.get(colour_name)}")
    colour_name = input("Enter colour name: ").lower()