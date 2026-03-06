class StringCalculator:

   def calculate(self, input_string: str) -> int:
      if not input_string:
         return 0

      input_string = input_string.replace(",","\n")
      numbers: list[str] = input_string.split("\n")

      if len(numbers) > 3:
         raise ValueError

      return sum(int(n) for n in numbers)

