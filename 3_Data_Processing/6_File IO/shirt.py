import sys
from PIL import Image, ImageOps


# Valid extensions set
valid_extensions = {".jpg", ".jpeg", ".png"}

# Check for correct number of arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Get extensions of input and output
input_ext = '.' + sys.argv[1].split('.')[-1].lower()
output_ext = '.' + sys.argv[2].split('.')[-1].lower()

# Check if input extension is valid
if input_ext not in valid_extensions:
    sys.exit("Invalid input")

# Check if output extension is valid
if output_ext not in valid_extensions:
    sys.exit("Invalid output")

# Check if extensions match
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    muppet = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    # Resize input(muppet) to shirt size
    muppet_resized = ImageOps.fit(muppet, shirt.size)

    # Paste shirt on input
    muppet_resized.paste(shirt, mask=shirt)

    muppet_resized.save(sys.argv[2])

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


