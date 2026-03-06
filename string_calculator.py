class StringCalculator:

   def calculate(self, input_string: str) -> int:
      if not input_string:
         return 0

      parsed_string: list[str] = input_string.split(",")

      if len(parsed_string) == 1:
         try:
            num = int(input_string)
            return num
         except:
            raise NotImplementedError
      elif len(parsed_string) == 2:
         try:
            return int(parsed_string[0]) + int(parsed_string[1])
         except:
            raise NotImplementedError
      else:
         raise NotImplementedError
