# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestDateRangeDomainSelectorTour(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        date_range_type = cls.env["date.range.type"].create({"name": "DR Tour Type"})
        cls.env["date.range"].create(
            {
                "name": "DR Tour 2026",
                "type_id": date_range_type.id,
                "date_start": "2026-01-01",
                "date_end": "2026-12-31",
            }
        )
        cls.ir_filter = cls.env["ir.filters"].create(
            {
                "name": "DR Tour Filter",
                "model_id": "date.range",
                "domain": "[('date_start', '<=', '2026-12-31'), "
                "('date_start', '>=', '2026-01-01')]",
            }
        )

    def test_domain_selector_date_range(self):
        """The domain editor loads with date_range's patches and shows the
        date range operator and value for a matching domain."""
        self.start_tour(
            f"/odoo/action-base.actions_ir_filters_view/{self.ir_filter.id}",
            "date_range_domain_selector",
            login="admin",
        )
