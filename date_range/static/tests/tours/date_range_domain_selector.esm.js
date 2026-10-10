import {registry} from "@web/core/registry";

registry.category("web_tour.tours").add("date_range_domain_selector", {
    steps: () => [
        {
            content: "Unfold the domain editor of the filter",
            trigger: ".o_field_widget[name=domain] .d-flex.align-items-center",
            run: "click",
        },
        {
            content: "The date range operator is offered for a date field",
            trigger: ".o_tree_editor select:has(option[value='\"daterange\"'])",
        },
        {
            content: "The matching date range is selected as value",
            trigger: ".o_tree_editor select:has(option:checked:contains(DR Tour 2026))",
        },
    ],
});
