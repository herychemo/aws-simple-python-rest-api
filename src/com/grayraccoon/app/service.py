# service.py

from .db import get_db

class ResourcesService:
    def find_all(self):
        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute('SELECT * FROM resources;')
        results = cursor.fetchall()

        return results

    def find_by_id(self, id):
        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(f'SELECT * FROM resources WHERE ID={id};')
        result = cursor.fetchone()

        return result

    def save(self, resource):
        if self.find_by_id(resource['ID']) is None:
            self.__create(resource)
        else:
            self.__update(resource)

        return self.find_by_id(resource['ID'])

    def __create(self, resource):
        db = get_db()
        cursor = db.cursor()

        cursor.execute(f"INSERT INTO resources(ID, VAL) VALUES ('{resource['ID']}', '{resource['VAL']}')")
        db.commit()

    def __update(self, resource):
        db = get_db()
        cursor = db.cursor()

        cursor.execute(f"UPDATE resources SET VAL='{resource['VAL']}' WHERE ID={resource['ID']}")
        db.commit()

    def delete(self, id):
        db = get_db()
        cursor = db.cursor()

        cursor.execute(f"DELETE FROM resources WHERE id={id}")
        db.commit()
