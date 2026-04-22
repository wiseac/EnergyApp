from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("enter_box", "pressed_enter")
  def enter_box_pressed_enter(self, **event_args):
    for i in range(4):
      display_names = [self.display_0, self.display_1,self.display_2, self.display_3]
      label_names = [self.conv_label_0, self.conv_label_1,self.conv_label_2, self.conv_label_3]
      display_names[i].text = convert_hartree(float(self.enter_box.text), list(CONVERSION_Hartree_FACTORS)[i])
      label_names[i].text = list(CONVERSION_Hartree_FACTORS)[i]

CONVERSION_Hartree_FACTORS = {
  'ev': 27.2107 ,
  'cm-1': 219474.63,
  'kcal/mol': 627.503,
  'nm': 1239.84
}

def convert_hartree(value, to_unit):
  if to_unit == 'nm':
    return round(CONVERSION_Hartree_FACTORS.get(to_unit, 1)/ (value * CONVERSION_Hartree_FACTORS.get('ev', 1)),2)
  else:
    return round(value * CONVERSION_Hartree_FACTORS.get(to_unit, 1),2)
