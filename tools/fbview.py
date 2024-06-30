from PIL import Image
import numpy as np

width = 256
height = 240
color_pallete = [ 
  0x7C7C7C, 0x0000FC, 0x0000BC, 0x4428BC, 0x940084, 0xA80020, 0xA81000, 0x881400, 
  0x503000, 0x007800, 0x006800, 0x005800, 0x004058, 0x000000, 0x000000, 0x000000, 
  0xBCBCBC, 0x0078F8, 0x0058F8, 0x6844FC, 0xD800CC, 0xE40058, 0xF83800, 0xE45C10, 
  0xAC7C00, 0x00B800, 0x00A800, 0x00A844, 0x008888, 0x000000, 0x000000, 0x000000,
  0xF8F8F8, 0x3CBCFC, 0x6888FC, 0x9878F8, 0xF878F8, 0xF85898, 0xF87858, 0xFCA044, 
  0xF8B800, 0xB8F818, 0x58D854, 0x58F898, 0x00E8D8, 0x787878, 0x000000, 0x000000, 
  0xFCFCFC, 0xA4E4FC, 0xB8B8F8, 0xD8B8F8, 0xF8B8F8, 0xF8A4C0, 0xF0D0B0, 0xFCE0A8, 
  0xF8D878, 0xD8F878, 0xB8F8B8, 0xB8F8D8, 0x00FCFC, 0xF8D8F8, 0x000000, 0x000000 
]
def make_image(file,imagename):
  image = np.zeros(height * width, dtype=np.uint32)

  for index in range(int(width*height/8)):
    num = int.from_bytes(file.read(6), "big", signed="False")
    extracted = np.zeros(8, dtype=np.uint32)
    for i in range(8):
      extracted[i] = color_pallete[((num >> i) & 0b00111111)]
    image[index*8+0] = extracted[0]
    image[index*8+1] = extracted[1]
    image[index*8+2] = extracted[2]
    image[index*8+3] = extracted[3]
    image[index*8+4] = extracted[4]
    image[index*8+5] = extracted[5]
    image[index*8+6] = extracted[6]
    image[index*8+7] = extracted[7]

  image = np.reshape(image, (height, width))
  im = Image.fromarray(image).convert('RGB')
  im.save(imagename)

offset = 0x1c

file = open('../TestBenches/fbdump_top.out','rb')
file.seek(offset)
make_image(file, "image.png")
