class Number:

   def __init__(self, value: int):
      if not value:
         ValueError("Value cannot be Empty")
      self.value = value
   
   def __str__(self):
      return f"{self.value}"

   def __abs__(self):
      # This is my own version, written to understand absolute value.
      # It might not be the best way to write it, but it's a start.
      print("Using custom absolute value function:")
      if self.value > 0:
         return self.value
      elif self.value < 0:
         return 0 - self.value


def main():
  
  twenty_five = Number(-25)
  print(abs(twenty_five))

if __name__ == "__main__":
    main()
