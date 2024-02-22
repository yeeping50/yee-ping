import anvil.pdf
from anvil.pdf import PDFRenderer

@anvil.server.callable
def create_pdf(name, amount, for1):
  pdf = anvil.pdf.render_form('Ticket', name, amount, for1)
  pdf = PDFRenderer(filename=f'{name} Ticket.pdf').render_form('Ticket', name, amount, for1)
  return pdf
