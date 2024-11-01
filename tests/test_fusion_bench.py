import unittest

import fusion_bench


class TestFusionBenchImports(unittest.TestCase):
    def test_imports(self):
        self.assertTrue(hasattr(fusion_bench, "BaseModelPool"))
        self.assertTrue(hasattr(fusion_bench, "BaseTaskPool"))


if __name__ == "__main__":
    unittest.main()
