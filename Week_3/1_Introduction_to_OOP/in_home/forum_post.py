class ForumPost():
    def __init__(self, author: str, text: str, upvotes: int):
        self.author = author
        self.text = text
        self.upvotes = upvotes
        self.replies = []

    def view(self) -> str:
        if self.replies:
            reply_string = '\n- '.join(self.replies)
            return f'{self.text} / by {self.author}, {self.upvotes} votes. \n- {reply_string}'
        else:
            return f'{self.text} / by {self.author}, {self.upvotes} votes.'

    def add_reply(self, reply: str) -> None:
        self.replies.append(reply)