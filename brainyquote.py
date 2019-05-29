#!/usr/bin/env python3

import feedparser
import random

#
# Sample structure of an 'entries' object:
#

# {'summary_detail': 
#  {'type': 'text/html', 
#   'language': None, 
#   'value': '"It is an ironic habit of human beings to run faster when we have lost our way."', 
#   'base': 'https://www.brainyquote.com/link/quotebr.rss'
#  }, 
#  'title_detail': 
#  {'type': 'text/plain', 
#   'language': None, 
#   'value': 'Rollo May', 
#   'base': 'https://www.brainyquote.com/link/quotebr.rss'
#  },
#  'title': 'Rollo May', 
#  'summary': '"It is an ironic habit of human beings to run faster when we have lost our way."', 
#  'links': 
#  [
#      {'type': 'text/html', 
#       'href': 'https://www.brainyquote.com/authors/rollo_may', 
#       'rel': 'alternate'
#      }
#  ], 
#  'link': 'https://www.brainyquote.com/authors/rollo_may'
# }

class BrainyQuote:
    _FEED_URL = 'https://www.brainyquote.com/link/quotebr.rss'
    def __init__( self ):
        self.quotes = [ ]
        return

    def haveQuotes( self ):
        return len( self.quotes ) > 0

    def getQuote( self ):
        self.fetchQuotes( )
        if len( self.quotes ) == 0:
            author, quote = "", ""
        else:
            i = random.randrange( len( self.quotes ) )
            author, quote = self.quotes.pop( i )
        return author, quote

    def fetchQuotes( self ):
        if len( self.quotes ) == 0:
            data = feedparser.parse( self._FEED_URL )
            for item in data[ 'entries' ]:
                self.quotes.append( ( item[ 'title' ], item[ 'summary' ] ) )
        return

def main( ):
    bq = BrainyQuote( )
    author, quote = bq.getQuote( )
    print( author, ":", quote )
    while bq.haveQuotes( ):
        author, quote = bq.getQuote( )
        print( author, ":", quote )
    return

if __name__ == "__main__":
    main( )
    
