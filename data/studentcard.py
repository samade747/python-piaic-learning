from PIL import Image, ImageDraw, ImageFont
from google.colab import files

# Function to create the student card image
def create_student_card(output_image_path, dummy_image_path=None):
    # Card dimensions
    width, height = 600, 350

    # Create a blank image with a light gray background
    img = Image.new("RGB", (width, height), color="#f0f0f0")
    d = ImageDraw.Draw(img)

    # Fonts: Use default font in Colab
    font_title = ImageFont.load_default()
    font_details = ImageFont.load_default()

    # Draw a border for the card
    border_thickness = 10
    d.rectangle(
        [border_thickness, border_thickness, width - border_thickness, height - border_thickness],
        outline="black",
        width=border_thickness
    )

    # Title Background
    title_bg_height = 60
    d.rectangle([0, 0, width, title_bg_height], fill="#4CAF50")  # Green background

    # Title
    d.text((width // 2 - 100, 15), "Student Card", font=font_title, fill="white")

    # Student details
    details = [
        ("Name:", "Samad"),
        ("Roll:", "2131212"),
        ("Center:", "Sindh Boys Scout Ass"),
        ("Batch:", "66"),
    ]

    y_offset = 100
    line_spacing = 40
    for label, value in details:
        d.text((50, y_offset), f"{label}", font=font_details, fill="black")
        d.text((200, y_offset), f"{value}", font=font_details, fill="gray")
        y_offset += line_spacing

    # Add dummy image or placeholder
    dummy_pic_x, dummy_pic_y = 400, 100
    dummy_pic_size = 120

    if dummy_image_path:
        try:
            dummy_pic = Image.open(dummy_image_path).resize((dummy_pic_size, dummy_pic_size))
            img.paste(dummy_pic, (dummy_pic_x, dummy_pic_y))
        except FileNotFoundError:
            print("Dummy picture not found. Skipping image addition.")
            d.rectangle(
                [dummy_pic_x, dummy_pic_y, dummy_pic_x + dummy_pic_size, dummy_pic_y + dummy_pic_size],
                outline="red",
                width=2
            )
            d.text((dummy_pic_x + 10, dummy_pic_y + 50), "No Image", font=font_details, fill="red")
    else:
        d.rectangle(
            [dummy_pic_x, dummy_pic_y, dummy_pic_x + dummy_pic_size, dummy_pic_y + dummy_pic_size],
            outline="red",
            width=2
        )
        d.text((dummy_pic_x + 10, dummy_pic_y + 50), "No Image", font=font_details, fill="red")

    # Save the card
    img.save(output_image_path)
    print(f"Student card saved as {output_image_path}")

# Paths
output_image_path = "/content/student_card_improved.png"
dummy_image_path = "/content/samad1.jpeg"  # Replace with the actual path to your dummy image

# Create the student card image
create_student_card(output_image_path, dummy_image_path)

# Display the image
img = Image.open(output_image_path)
img.show()

# Download the image
files.download(output_image_path)
