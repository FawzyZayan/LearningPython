class Profile:
  def __init__(self, username, email, language):
    self.username = username
    self.email = email
    self.language = language
    
    
first_profile = Profile("Thomas Jan", "thomas@gmail.com", "German")
second_profile = Profile("Victor Dia", "victor@hotmail.com", "Spanish")
third_profile = Profile("Harry Kane", "harry@yahoo.com", "English")