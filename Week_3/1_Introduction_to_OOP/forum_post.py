class ForumPost():
    def __init__(self, author: str, text: str, upvotes: int):
        self.author = author
        self.text = text
        self.upvotes = upvotes
        self.replies = []


    def view(self):
        if self.replies:
            reply_string = ''''''
            for reply in self.replies:
                reply_string += '- ' + reply + '\n'
            return (f'''{self.text} / by {self.author}, {self.upvotes} votes.
{reply_string}''')
        else:
            return (f'{self.text} / by {self.author}, {self.upvotes} votes.')

    def add_reply(self, reply: str):
        self.replies.append(reply)