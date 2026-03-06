

class StringCalculator:


    def calculate(self, input_string: str) -> int:
        if not input_string:
                return 0
        else:
            try:
                num = int(input_string)
                return num
            except:
                raise NotImplementedError