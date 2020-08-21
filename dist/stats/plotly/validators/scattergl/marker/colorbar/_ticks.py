import _plotly_utils.basevalidators


class TicksValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="ticks", parent_name="scattergl.marker.colorbar", **kwargs
    ):
        super(TicksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["outside", "inside", ""]),
            **kwargs
        )
