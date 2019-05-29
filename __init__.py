from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from . import brainyquote

__author__ = 'fractal13'
LOGGER = LOG.create_logger( __name__ )

class BrainyQuoteSkill( MycroftSkill ):

    def __init__( self ):
        super( BrainyQuoteSkill, self ).__init__( name="BrainyQuoteSkill" )
        self.brainyquote = brainyquote.BrainyQuote( )
        return

    @intent_handler(IntentBuilder("").optionally("Tell").require("BrainyQuote"))
    def handle_tell_quote_intent(self, message):
        author, quote = self.brainyquote.getQuote( )
        self.speak_dialog("author.quote",
                          data={"author": author,
                                "quote": quote})
        return
    
def create_skill():
    return BrainyQuoteSkill()

