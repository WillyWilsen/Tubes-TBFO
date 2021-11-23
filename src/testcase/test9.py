from PIL import Image

var = "input.jpg"
ACCEPTED_ASCII_LIST = []

def extract_text_from_image():
    PIPE_ASCII = 124

    time_start = time.perf_counter()
    text = pytesseract.image_to_string(Image.open(IMAGE_INPUT_NAME))
    with open(FILE_OUTPUT_NAME, 'asdf') as f_out:
        for c in text:
            ascii = ord(c)
            if ascii == PIPE_ASCII:
                f_out.write('I')
            elif ascii in ACCEPTED_ASCII_LIST:
                f_out.write[c]
            else:
                f_out.write(' ')
    time_end = time.perf_counter()