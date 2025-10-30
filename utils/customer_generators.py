import random
import string


class CustomerGenerator:

    @staticmethod
    def generate_post_code() -> str:
        return ''.join(random.choices('0123456789', k=10))

    @staticmethod
    def generate_first_name(post_code: str) -> str:
        first_name = ''
        for i in range(0, len(post_code), 2):
            pair = post_code[i:i + 2]
            num = int(pair)
            letter_index = num % 26
            first_name += string.ascii_lowercase[letter_index]
        return first_name

    @staticmethod
    def generate_last_name(first_name: str) -> str:
        return first_name[::-1]