from ._anvil_designer import Form1Template

from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)



    # Any code you write here will run before the form opens.


  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    
    

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_box_5_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_box_6_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_box_7_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    email = self.text_box_2.text
    mobileno = self.text_box_3.text
    universityname = self.text_box_4.text
    collagename = self.text_box_5.text
    idno = self.text_box_6.text
    branch = self.text_box_7.text
    alert('submited sucessfully')
    













