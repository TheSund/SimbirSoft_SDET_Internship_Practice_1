class DataUtils:

    @staticmethod
    def get_value_closest_to_avg_by_len(values: list[str]) -> str:
        lengths = [len(v) for v in values]
        avg = sum(lengths) / len(lengths)
        return min(values, key=lambda v: abs(len(v) - avg))
