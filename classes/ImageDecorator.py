from PIL import Image, ImageDraw, ImageFont
import textwrap


class ImageDecorator:

    def decorate_image(self, input_img, output_img, text_bottom, text_center):

        font_path_center = 'fonts/True North Inline W01 Regular/True North Inline W01 Regular.ttf'
        font_size_center = 100
        font_path_bottom = 'fonts/PacificRough/pacific-northwest-rough-letters.ttf'
        font_size_bottom = 120

        try:
            self.__create_image_with_text_hq(input_img,
                                             output_img,
                                             text_center,
                                             text_bottom,
                                             font_path_center,
                                             font_size_center,
                                             font_path_bottom,
                                             font_size_bottom,
                                             False,
                                             False)
        except Exception as e:
            print("Error creating image {}".format(str(e)))

    def __create_image_with_text_hq(self, image_path, output_path, text1, text2, font_path_center, font_size_center, font_path_bottom, font_size_bottom, footer_gradient=False, header_gradient=False):

        # Load the image
        image = Image.open(image_path).convert("RGBA")
        image = image.resize((1080, 1080))
        width, height = image.size

        text_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        draw.fontmode = "L"

        if header_gradient or footer_gradient:
            # Create a new transparent image with the same dimensions
            gradient = Image.new("RGBA", image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(gradient)

            # Define gradient sizes and colors
            gradient_height = int(height * 0.1)

            # Opacity level means transparency
            opacity = 150
            gradient_top = (0, 0, 0, opacity)
            gradient_bottom = (0, 0, 0, opacity)

            if header_gradient:
                for y in range(gradient_height):
                    alpha = int(((gradient_height - y) /
                                gradient_height) * gradient_top[3])
                    draw.line([(0, y), (width, y)],
                              fill=gradient_top[:3] + (alpha,))

            if footer_gradient:
                for y in range(height - gradient_height, height):
                    alpha = int((y - (height - gradient_height)) /
                                gradient_height * gradient_bottom[3])
                    draw.line([(0, y), (width, y)],
                              fill=gradient_bottom[:3] + (alpha,))

            image = Image.alpha_composite(image, gradient)

            # Apply the gradient to the bottom of the original image
            image = Image.alpha_composite(image, gradient)
            draw = ImageDraw.Draw(image)

        # Load the font
        font_center = ImageFont.truetype(font_path_center, font_size_center)
        font_bottom = ImageFont.truetype(font_path_bottom, font_size_bottom)

        wrapped, lines = self.__multiline_text(
            text1, font_center, max_width=width - 40)
        text1 = wrapped

        final_height = font_size_center * (len(lines))
        final_width = 0
        for line in lines:
            line_width = draw.textlength(text=line, font=font_center)
            if line_width > final_width:
                final_width = line_width

        if len(lines) <= 1:
            space = 100
        if len(lines) == 2:
            space = 125
        if len(lines) >= 3:
            space = 150

        # Calculate the text dimensions
        text1_width = final_width
        text1_height = final_height
        text2_width = draw.textlength(text=text2, font=font_bottom)
        text2_height = 0

        # Define the positions of the texts
        image_width, image_height = image.size
        # margin = 20
        text1_x = (image_width - text1_width) // 2
        text1_y = (image_height - text1_height - space) // 2
        text2_x = (image_width - text2_width) // 2
        text2_y = (image_height - font_size_center) - 100

        # Draw the texts on the image
        draw.multiline_text((text1_x, text1_y), text1, font=font_center, fill=(
            255, 255, 255), align="center")
        draw.text((text2_x, text2_y), text2,
                  font=font_bottom, fill=(255, 255, 255))

        image_with_text = Image.alpha_composite(image, text_layer)

        image_with_text.show()

        # Save the image as JPEG
        image_with_text.save(output_path, format="PNG",
                             optimize=True, quality=100)

    def __multiline_text(self, text, font, max_width):
        wrapped_text = textwrap.wrap(text, width=max_width)
        # print(wrapped_text)

        lines = []
        for line in wrapped_text:
            if font.getlength(line) <= max_width:
                lines.append(line)
            else:
                words = line.split()
                new_line = words[0]
                for word in words[1:]:
                    if font.getlength(new_line + ' ' + word) <= max_width:
                        new_line += ' ' + word
                    else:
                        lines.append(new_line)
                        new_line = word
                if new_line:
                    lines.append(new_line)

        multiline_text = '\n'.join(lines)
        return multiline_text, lines
