##OPEN API STUFF
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
