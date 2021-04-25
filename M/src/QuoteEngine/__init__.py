""" Create Quote Model Class for body and author"""


class QuoteModel:
    """Create self objects"""
    def __init__(self, body, author):
        self.body = body
        self.author = author
    """Return self objects together"""
    def __repr__(self):
        return f"{self.body} - {self.author}"
