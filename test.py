from PIL import Image

def modify_image(filename):
  print filename
  background = Image.open(filename)
  bgw, bgh = background.size
  if not (bgw < bgh):
    background = background.rotate(-90)
  bgw, bgh = background.size
  foreground = Image.open("arcelik.png")
  resizew, resizeh = 640, 180
  resized = foreground.resize((resizew, resizeh))
  background.paste(resized, (0, bgh - resizeh), resized)
  removed_ending = filename.split('.')[0]
  background.save(removed_ending + '_modified.jpg')