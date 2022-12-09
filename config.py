##OPEN API STUFF
# OPENAI_API_KEY = 'sk-yourkey'
OPENAI_API_KEY = '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'


## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
