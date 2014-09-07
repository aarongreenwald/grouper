from pyramid.config import Configurator
from sqlalchemy import engine_from_config

import api.models

def main(global_config, **settings):
    
    engine = engine_from_config(settings, 'sqlalchemy.')    
    
    api.models.DBSession.configure(bind=engine)
    api.models.Base.metadata.bind = engine
    
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')        
        
     #for the main entry point to the SPA
    config.add_route('app', '/') 
        
    config.add_route('groups', '/api/groups')    

    #this sets up the ui folder to be served from the root, so things like /common/...js work    
    config.add_static_view('', 'ui', cache_max_age = 0) 
        
    config.scan()
    return config.make_wsgi_app()
