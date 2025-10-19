from typing import Self


class AmaiBase:
    def setup(self):
        pass

    def shutdown(self):
        pass

    @classmethod
    def mult_parse_from_json(cls) -> list[Self]:
        raise NotImplementedError("mult_parse_from_json not implemented")

    @classmethod
    def parse_from_json(cls) -> Self:
        raise NotImplementedError("parse_from_json not implemented")
