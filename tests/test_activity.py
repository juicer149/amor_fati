import unittest

from amorfati.core.activity import Activity
from amorfati.core.activity_bit import ActivityBit
from amorfati.core.catalog import ActivityCatalog


class TestActivity(unittest.TestCase):
    def test_load_unit_activity_from_yaml(self):
        activity = Activity.from_yaml(
            "config/activities/meditaion/free_breathing.yaml"
        )

        self.assertEqual(activity.name, "free_breathing")
        self.assertEqual(activity.type, "meditation")
        self.assertFalse(activity.is_bool)
        self.assertIn("minutes", activity.units)

    def test_score_unit_activity(self):
        activity = Activity.from_yaml(
            "config/activities/meditaion/free_breathing.yaml"
        )

        bit = ActivityBit(
            activity=activity,
            duration_minutes=30,
            units_data={"minutes": 30},
        )

        self.assertEqual(bit.score(), 30.0)

    def test_boolean_activity_uses_value(self):
        activity = Activity.from_yaml(
            "config/activities/cold_shower.yaml"
        )

        bit = ActivityBit(
            activity=activity,
            completed=True,
        )

        self.assertTrue(activity.is_bool)
        self.assertEqual(bit.score(), 20.0)

    def test_boolean_activity_not_completed_scores_zero(self):
        activity = Activity.from_yaml(
            "config/activities/cold_shower.yaml"
        )

        bit = ActivityBit(
            activity=activity,
            completed=False,
        )

        self.assertEqual(bit.score(), 0.0)

    def test_empty_yaml_raises_value_error(self):
        with self.assertRaises(ValueError):
            Activity.from_yaml(
                "config/activities/training/mobility.yaml"
            )

    def test_catalog_skips_invalid_yaml(self):
        catalog = ActivityCatalog()

        self.assertIn("cold_shower", catalog)
        self.assertIn("free_breathing", catalog)
        self.assertNotIn("mobility", catalog)


if __name__ == "__main__":
    unittest.main(verbosity=2)
