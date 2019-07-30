class Config:  # Configuraciones globales
    SECRET_KEY = 'Admin123'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
