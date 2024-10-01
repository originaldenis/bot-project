from botdir.database.utils.CRUD import CRUDInterface
from botdir.database.common.models import db, History

db.connect()
db.create_tables([History])

while History.select().count() > 20:
    CRUDInterface.delete(db, History, History.id < 11)
    History.update({History.id: History.id - 10}).execute()

if __name__ == "__main__":
    CRUDInterface()
