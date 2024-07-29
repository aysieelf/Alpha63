from models.validation_helpers import valid_str_len


class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    def __init__(self,
                 content: str,
                 author: str):

        self.content = content
        self.author = author

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        valid_str_len(value,
                      Comment.CONTENT_LEN_MIN,
                      Comment.CONTENT_LEN_MAX,
                      Comment.CONTENT_LEN_ERR)

        self._content = value

    def __str__(self):
        return '\n'.join([
            f'----------',
            f'{self.content}',
            f'User: {self.author}',
            '----------'])

