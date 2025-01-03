import unittest
from app.models import Package

class TestPackageModel(unittest.TestCase):
    def test_package_creation(self):
        package = Package(origin="Location A", destination="Location B")
        self.assertEqual(package.origin, "Location A")
        self.assertEqual(package.status, "pending")