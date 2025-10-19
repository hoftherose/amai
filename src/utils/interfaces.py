from typing import TypeVar

AmaiType = TypeVar("AmaiType", bound="AmaiBase")


class AmaiBase:
    def setup(self):
        pass

    def shutdown(self):
        pass

    @classmethod
    def mult_parse_from_json(cls: type[AmaiType]) -> list[AmaiType]:
        raise NotImplementedError("mult_parse_from_json not implemented")

    @classmethod
    def parse_from_json(cls: type[AmaiType]) -> AmaiType:
        raise NotImplementedError("parse_from_json not implemented")
