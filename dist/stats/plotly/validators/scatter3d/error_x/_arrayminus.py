import _plotly_utils.basevalidators


class ArrayminusValidator(_plotly_utils.basevalidators.DataArrayValidator):
    def __init__(
        self, plotly_name="arrayminus", parent_name="scatter3d.error_x", **kwargs
    ):
        super(ArrayminusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "data"),
            **kwargs
        )
