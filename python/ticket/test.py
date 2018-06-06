from PIL import Image
import pytesseract as pt

print(pt.image_to_string(Image.open('./iii.png'), lang='chi_sim', config=''))