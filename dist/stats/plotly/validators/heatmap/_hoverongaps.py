import _plotly_utils.basevalidators


class HoverongapsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="hoverongaps", parent_name="heatmap", **kwargs):
        super(HoverongapsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
