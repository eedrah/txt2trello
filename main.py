from trello import TrelloClient
import os

class MultipleBoardError(LookupError):
    '''Error when there is more than one board matching that name.'''

class Card():
    def __init__(self, trello_card):
        self.trello_card = trello_card

    def print(self):
        return self.trello_card.name

class List():
    def __init__(self, trello_list):
        self.trello_list = trello_list

    def print(self):
        return '\n'.join([
                self.print_name(),
                self.print_cards(),
                ''
            ])

    def print_cards(self):
        cards = self.trello_list.list_cards('open')
        return '\n'.join([Card(card).print() for card in cards])

    def print_name(self):
        return '\n'.join([
                self.trello_list.name,
                '===='
            ])

class Board():
    def __init__(self, trello_board):
        self.trello_board = trello_board

    def print(self):
        return '\n'.join([
                self.print_name(),
                self.print_lists(),
            ])

    def print_lists(self):
        lists = self.trello_board.get_lists('open')
        return '\n'.join([List(list).print() for list in lists])

    def print_name(self):
        return self.trello_board.name

def main():
    api_key = os.environ['API_KEY'],
    api_secret = os.environ['API_SECRET'],

    client = TrelloClient(
            api_key=api_key,
            api_secret=api_secret,
            # token='your-oauth-token-key', # Perhaps this will make it faster?
            # token_secret='your-oauth-token-secret'
        )

    matching_boards = [x for x in client.list_boards('open') if x.name == 'trello2txt']
    if len(matching_boards) > 1:
        raise MultipleBoardError('There is more than one board with that name.')
    board = Board(matching_boards[0])
    print(board.print())

if __name__ == '__main__':
    main()
