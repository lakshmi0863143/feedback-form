from ._anvil_designer import Form1Template

from anvil import *



class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)



    # Any code you write here will run before the form opens.


  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    

  def submit_Button_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    email = self.text_box_2.text
    FeedbackForm = self.text_area_1.text
    alert('Feedback submited')







