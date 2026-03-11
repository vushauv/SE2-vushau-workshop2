class StringCalculator:

   def calculate(self, input_string: str) -> int:
      if not input_string:
         return 0
      
      delimiter=","
      
      if input_string.startswith("//"):
         try:
               header, input_string = input_string.split("\n", 1)
               delimiter = header[3]
               if delimiter == "":
                  raise ValueError
         except Exception:
               raise ValueError

      input_string = input_string.replace(delimiter, "\n")
      input_string = input_string.replace(",", "\n")

      input_string = input_string.replace(",","\n")
      numbers: list[str] = input_string.split("\n")

      if len(numbers) > 3:
         raise ValueError

      sum: int = 0
      for n in numbers:
         try:
            if int(n) < 0:
               raise ValueError
            elif int(n) <= 1000:
               sum += int(n)
         except:
            raise ValueError
      return sum



