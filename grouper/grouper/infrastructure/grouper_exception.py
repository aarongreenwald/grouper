class GrouperException(Exception):
    
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message

    def __json__(self, request):
        return self.message        

