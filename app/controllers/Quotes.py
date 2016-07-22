"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Quote')
        self.load_model('User')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        all_quotes = self.models['Quote'].get_all_quotes()
        return self.load_view('quotes/index.html' , quotes = all_quotes)

    def show(self, id):
        quote = self.models['Quote'].view_quote(id)
        return self.load_view('quotes/display_quote.html', quote=quote[0])


    def create(self):
       
        self.models['Quote'].add_quote(request.form)
        return redirect('/')

    



    
