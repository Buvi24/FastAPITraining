from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB_NAME:str

    #Gives the app a name
    APP_NAME: str

    #informs pydantics_settings to load values from.env file
    model_config=SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")

    #Shared settings object that all other files can import
settings=Settings()


