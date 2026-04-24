from ._anvil_designer import Energy_convTemplate
from anvil import *
import anvil.server


class Energy_conv(Energy_convTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.enter_box.add_event_handler('pressed_enter', self.enter_box_pressed_enter)
    self.enter_button.add_event_handler( 'click', self.enter_button_click)
    self.clear_button.add_event_handler( 'click', self.clear_button_click)
    self.link_2.add_event_handler( 'click', self.link_2_click)
  def enter_box_pressed_enter(self, **event_args):
    display_names = [self.display_0, self.display_1,self.display_2, self.display_3]
    label_names = [self.conv_label_0, self.conv_label_1,self.conv_label_2, self.conv_label_3]
    if self.conv_drop.selected_value == "Hartree":
      for i in range(4):
        display_names[i].text = convert_hartree(float(self.enter_box.text), list(CONVERSION_Hartree_FACTORS)[i])
        label_names[i].text = list(CONVERSION_Hartree_FACTORS)[i]
    elif self.conv_drop.selected_value == "eV":
      for i in range(4):
        display_names[i].text = convert_ev(float(self.enter_box.text), list(CONVERSION_ev_FACTORS)[i])
        label_names[i].text = list(CONVERSION_ev_FACTORS)[i]
    elif self.conv_drop.selected_value == "cm-1":
      for i in range(4):
        display_names[i].text = convert_cm(float(self.enter_box.text), list(CONVERSION_cm_FACTORS)[i])
        label_names[i].text = list(CONVERSION_cm_FACTORS)[i]
    elif self.conv_drop.selected_value == "kcal/mol":
      for i in range(4):
        display_names[i].text = convert_kcal(float(self.enter_box.text), list(CONVERSION_kcal_FACTORS)[i])
        label_names[i].text = list(CONVERSION_kcal_FACTORS)[i]
    elif self.conv_drop.selected_value == "nm":
      for i in range(4):
        display_names[i].text = convert_nm(float(self.enter_box.text), list(CONVERSION_nm_FACTORS)[i])
        label_names[i].text = list(CONVERSION_nm_FACTORS)[i]

  def enter_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.enter_box.raise_event('pressed_enter')

  def clear_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    display_names = [self.display_0, self.display_1,self.display_2, self.display_3]
    label_names = [self.conv_label_0, self.conv_label_1,self.conv_label_2, self.conv_label_3]
    self.enter_box.text = ""
    for i in range(4):
      display_names[i].text = ""
      label_names[i].text = ""

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Energy_conv')


CONVERSION_Hartree_FACTORS = {
  'ev': 27.2107 ,
  'cm-1': 219474.63,
  'kcal/mol': 627.503,
  'nm': 1239.84
}

def convert_hartree(value, to_unit):
  if to_unit == 'nm':
    return round(CONVERSION_Hartree_FACTORS.get(to_unit, 1)/ (value * CONVERSION_Hartree_FACTORS.get('ev', 1)),4)
  else:
   return round(value * CONVERSION_Hartree_FACTORS.get(to_unit, 1),4)


CONVERSION_ev_FACTORS = {
  'hartree': 0.0367502,
  'cm-1': 8065.73 ,
  'kcal/mol': 23.0609  ,
  'nm': 1239.84
}

def convert_ev(value, to_unit):
  if to_unit == 'nm':
    return round(CONVERSION_ev_FACTORS.get('nm', 1)/ (value),4)
  else:
    return round(value * CONVERSION_ev_FACTORS.get(to_unit, 1),4)

CONVERSION_cm_FACTORS = {
  'hartree': (4.55633 * 10**-6),
  'ev': (1.23981 * 10**-4) ,
  'kcal/mol': 0.00285911   ,
  'nm': 1239.84
}

def convert_cm(value, to_unit):
  if to_unit == 'nm':
    return round(CONVERSION_cm_FACTORS.get(to_unit, 1)/ (value * CONVERSION_cm_FACTORS.get('ev', 1)),4)
  else:
    return round(value * CONVERSION_cm_FACTORS.get(to_unit, 1),4)

CONVERSION_kcal_FACTORS = {
  'hartree': 0.00159362 ,
  'ev': 0.0433634 ,
  'cm-1': 349.757   ,
  'nm': 1239.84
}

def convert_kcal(value, to_unit):
  if to_unit == 'nm':
    return round(CONVERSION_kcal_FACTORS.get(to_unit, 1)/ (value * CONVERSION_kcal_FACTORS.get('ev', 1)),4)
  else:
    return round(value * CONVERSION_kcal_FACTORS.get(to_unit, 1),4)

CONVERSION_nm_FACTORS = {
  'hartree': 45.563 ,
  'ev': 1240 ,
  'cm-1': 10**7   ,
  'kcal/mol': 28590
}

def convert_nm(value, to_unit):
  return round(CONVERSION_nm_FACTORS.get(to_unit, 1) / value,4)