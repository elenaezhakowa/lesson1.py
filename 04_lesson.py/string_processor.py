import unittest


class TestStringProcessor:
    @staticmethod
    def process(text: str) -> str:
        if not text:
            return "."
        processed_text = text[0].upper() + text[1:]
        if not processed_text.endswith("."):
            processed_text += "."
        return processed_text


class TestStringProcessor(unittest.TestCase):
    def test_empty_string(self):
        result = TestStringProcessor.process("")
        self.assertEqual(result, ".")

    def test_string_without_period(self):
        result = TestStringProcessor.process("hello")
        self.assertEqual(result, "Hello.")

    def test_string_with_period(self):
        result = TestStringProcessor.process("hello.")
        self.assertEqual(result, "Hello.")

    def test_string_starting_with_digit(self):
        result = TestStringProcessor.process("1hello")
        self.assertEqual(result, "1hello.")

    def test_string_only_period(self):
        result = TestStringProcessor.process(".")
        self.assertEqual(result, ".")


if __name__ == "__main__":
    unittest.main()
