from trello import TrelloClient, Board, List, Card, Checklist, Label
import os

class MultipleBoardError(LookupError):
    '''Error when there is more than one board matching that name.'''

def Checklist__str__(self):
    def __str__(self):
        return '### A checklist exists!!' # Finish when needed

Checklist.__str__ = Checklist__str__

def Card__str__(self):
    def str_name(self, fmt):
        if fmt == 'short':
            return '## {}'.format(self.name)
        return '\n'.join([
                self.name,
                '----'
            ])

    def str_description(self):
        return self.description

    def str_checklists(self):
        return '\n\n'.join([str(checklist) for checklist in self.checklists])

    description = str_description(self)
    if description:
        return '\n'.join([
                str_name(self, 'long'),
                str_description(self),
                '',
            ])
    return str_name(self, 'short')

Card.__str__ = Card__str__

def List__str__(self):
    def str_cards(self):
        open_cards = self.list_cards('open')
        return '\n'.join([str(card) for card in open_cards])

    def str_name(self):
        return '\n'.join([
                self.name,
                '===='
            ])

    return '\n'.join([
            str_name(self),
            str_cards(self),
            ''
        ])

List.__str__ = List__str__

class Labels():
    def __init__(self, labels):
        self.labels = labels

    def __str__(self):
        str_labels = ['- ({}) {}'.format(label.color,label.name) for label in self.labels if label.name]
        if str_labels:
            return '\n'.join([
                    'Labels',
                    '----',
                    *str_labels,
                    '',
                ])
        return ''

def Board__str__(self):
    def str_lists(self):
        open_lists = self.get_lists('open')
        return '\n'.join([str(list) for list in open_lists])

    def str_name(self):
        return self.name

    def str_labels(self):
        return str(Labels(self.get_labels()))

    return '\n'.join([
            str_name(self),
            str_labels(self),
            str_lists(self),
        ])

Board.__str__ = Board__str__

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
    board = (matching_boards[0])
    print(str(board))

if __name__ == '__main__':
    main()
