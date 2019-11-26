class Palindrome:
  def __init__(self, s):
    self.given_str = list(s)

  def normal(self):
    for i in range(len(self.given_str)):
      if self.given_str[i] != self.given_str[len(self.given_str) - i - 1]:
        return False
    return True
