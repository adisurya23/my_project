""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()
   
    def get_all_quotes(self):
        return self.db.query_db("SELECT * FROM quotes")
    
    def add_quote(self, quote):
        
        query = 'INSERT INTO quotes (content, created_at, updated_at) VALUES (:message, NOW(), NOW())'
        data = {'content':quote['content']}
        return self.db.query_db(query,data)

    def view_quote(self, quote_id):
        query = "SELECT * FROM quotes WHERE quotes.id = :id"
        data = {'id' : quote_id}
        return self.db.query_db(query,data)


       

