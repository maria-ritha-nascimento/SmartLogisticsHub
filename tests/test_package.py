import unittest
from main import app, db, Package

class TestPackageAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_package(self):
        response = self.app.post("/packages", json={
            "origin": "Location A",
            "destination": "Location B"
        })
        self.assertEqual(response.status_code, 201)

    def test_list_packages(self):
        response = self.app.get("/packages")
        self.assertEqual(response.status_code, 200)

    def test_update_package_status(self):
        # Create package
        self.app.post("/packages", json={
            "origin": "Location A",
            "destination": "Location B"
        })
        response = self.app.patch("/packages/1", json={"status": "delivered"})
        self.assertEqual(response.status_code, 200)
