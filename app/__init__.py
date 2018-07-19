from app.routes import app
from app.extensions import AppJSONEncoder

app.json_encoder = AppJSONEncoder
