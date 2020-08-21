import _plotly_utils.basevalidators


class BoxmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(self, plotly_name="boxmode", parent_name="layout", **kwargs):
        super(BoxmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["group", "overlay"]),
            **kwargs
        )
