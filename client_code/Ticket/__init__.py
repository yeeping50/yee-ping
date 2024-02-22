from ._anvil_designer import TicketTemplate
from anvil import *
import anvil.server
from datetime import date
from datetime import datetime
today = date.today()
date = today.strftime("%d %B %Y")
now = datetime.now()

class Ticket(TicketTemplate):
  def __init__(self, name, amount, for1,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.text = name
    self.amount_label.text = amount
    self.for1_label.text = for1
    self.date_label.text = date
    self.unique_label.text = now
