from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("enter_box", "pressed_enter")
  def enter_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass  # Write Code Here

CONVERSION_FACTORS = {
  'inches': 12,
  'yards': 1/3,
  'miles': 1/5280,
  'cm': 30.48
}

def convert_feet(value, to_unit):
  return value * CONVERSION_FACTORS.get(to_unit, 1)