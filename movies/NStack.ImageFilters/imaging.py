import os
import inspect
import subprocess
import math

import PIL.Image

class Image:
  def __init__(self, filename):
    self.filename = filename
    self.image = PIL.Image.open(self.filename)
    
  def make_square(self):
    pass

  def run_gm(self, command, **kwargs):
    format_params = dict(filename=self.filename, width=self.image.size[0], height=self.image.size[1])
    format_params.update(kwargs)
    command = command.format(**format_params)
    subprocess.check_call(command, shell=True, stderr=subprocess.STDOUT)

  def set_colortone(self, color, level, type = 0):
    arg0 = level
    arg1 = 100 - level
    negate = '-negate' if type == 0 else ''
    self.run_gm("convert {filename} \( -clone 0 -fill '{color}' -colorize 100% \) \( -clone 0 -colorspace gray {negate} \) -compose blend -define compose:args={arg0},{arg1} -composite {filename}",
      color=color, negate=negate, arg0=arg0, arg1=arg1)

  def add_border(self, color = 'black', width = 20):
    self.run_gm("convert {filename} -bordercolor {color} -border {bwidth}x{bwidth} {filename}",
      color=color, bwidth=width)

  def add_vignette(self, color_1 = 'none', color_2 = 'black', crop_factor = 1.5):
    crop_x = math.floor(self.image.size[0] * crop_factor)
    crop_y = math.floor(self.image.size[1] * crop_factor)
    self.run_gm("convert \( {filename} \) \( -size {crop_x}x{crop_y} radial-gradient:{color_1}-{color_2} -gravity center -crop {width}x{height}+0+0 +repage \) -compose multiply -flatten {filename}",
      crop_x=crop_x, crop_y=crop_y, color_1=color_1, color_2=color_2)

  def add_frame(self, frame):
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    self.run_gm("convert {filename} \( '{frame}' -resize {width}x{width}! -unsharp 1.5x1.0+1.5+0.02 \) -flatten {filename}",
      frame=os.path.join(path, "frames", frame)
    )

def mk_gotham(filename):
  img = Image(filename)
  img.run_gm("convert {filename} -modulate 120,10,100 -fill '#222b6d' -colorize 20 -gamma 0.5 -contrast -contrast {filename}")
  img.add_border()

def mk_kelvin(filename):
  img = Image(filename)
  img.make_square()
  img.run_gm("convert \( {filename} -auto-gamma -modulate 120,50,100 \) \( -size {width}x{height} -fill 'rgba(255,153,0,0.5)' -draw 'rectangle 0,0 {width},{height}' \) -compose multiply {filename}")
  img.add_frame("Kelvin.jpg")

def mk_lomo(filename):
  img = Image(filename)
  img.run_gm("convert {filename} -channel R -level 33% -channel G -level 33% {filename}")
  img.add_vignette()

def mk_nashville(filename):
  img = Image(filename)
  img.make_square()
  img.set_colortone('#222b6d', 50, 0);
  img.set_colortone('#f7daae', 120, 1);
  img.run_gm("convert {filename} -contrast -modulate 100,150,100 -auto-gamma {filename}");
  img.add_frame("Nashville.jpg");
  
def mk_toaster(filename):
  img = Image(filename)
  img.set_colortone('#330000', 50, 0)
  img.run_gm("convert {filename} -modulate 150,80,100 -gamma 1.2 -contrast -contrast {filename}");
  img.add_vignette('none', 'LavenderBlush3');
  img.add_vignette('#ff9966', 'none');
  img.add_border('white')

