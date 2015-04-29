from PIL import Image, ImageDraw, ImageFont

def modify_image(filename, word, color):
  print filename
  background = Image.open(filename)
  bgw, bgh = background.size
  if not (bgw < bgh):
    background = background.rotate(-90)
  background = background.resize((960, 1280))
  bgw, bgh = background.size
  frame = Image.open(color + "Frame.png")
  frame.paste(background, (74, 138))
  draw = ImageDraw.Draw(frame)
  font = ImageFont.truetype("BebasNeueRegular.ttf", 225)
  draw.text((325, 1490),word.upper(),(255,255,255),font=font)
  removed_ending = filename.split('.')[0]
  frame.save(removed_ending + '_modified.jpg')
