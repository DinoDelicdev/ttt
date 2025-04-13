class PromptValidator:
  @staticmethod
  def is_valid_input(user_input):
    try:
      value = int(user_input)
      if 1 <= value <= 9:
        return True
      return False
    except ValueError:
      return False