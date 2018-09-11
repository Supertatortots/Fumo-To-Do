import datetime

class Note:
  def __init__(self, title, content):
    self.title = title
    self.content = content

testNote = Note("Hello", "I like shorts!")

print(testNote.title)