class Telegram:
  def __init__(self, sender, recipient, message, history):
    self.sender = sender
    self.recipient = recipient
    self.message = message
    self.history = history
    
    
first_message = Telegram("Thomas", "Victor", "Hi! Let's go to the park", "2026/11/5 03:43 pm")
first_reply = Telegram("Victor", "Thomas", "Hello! OKay", "2026/11/5 03:45 pm")
second_message = Telegram("Harry", "Dia", "Hi! Is your arm okay? I heard it was hurting you", "2026/5/23 10:57 am")
second_reply = Telegram("Dia", "Harry", "Hello! Yes, I went to a doctor and it's better now", "2026/5/23 02:48 pm")