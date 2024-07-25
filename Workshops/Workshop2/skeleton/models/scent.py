class Scent:
    LAVENDER = 'lavender'
    VANILLA = 'vanilla'
    ROSE = 'rose'

    @classmethod
    def from_string(cls, scent_string: str) -> str:
        if scent_string not in [cls.LAVENDER, cls.VANILLA, cls.ROSE]:
            raise ValueError(
                f'None of the possible scent values matches the value {scent_string}.')

        return scent_string
