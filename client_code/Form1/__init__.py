from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.name_box.text
    amount = self.amount_box.text
    for1 = self.for1_box.text
    open_form('Ticket', name, amount, for1)
    pdf = anvil.server.call('create_pdf',name, amount, for1)
    anvil.media.download(pdf)
