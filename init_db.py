from estudo import app, db
from estudo import models
from sqlalchemy import inspect


with app.app_context():
    db.create_all()
    print("Banco criado com sucesso!")

    inspector = inspect(db.engine)
    print("Tabelas criadas:", inspector.get_table_names())