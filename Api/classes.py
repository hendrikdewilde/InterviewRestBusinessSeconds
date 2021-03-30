from rest_framework import permissions
from rest_framework.metadata import BaseMetadata


class APIRootMetadata(BaseMetadata):
    """
    Don't include field and other information for `OPTIONS` requests.
    Just return the name and description.
    """
    def determine_metadata(self, request, view):

        if view.get_view_name() == "Business Seconds List":
            actions = {
                "GET": {
                    "read_only": False,
                    "parameters required": True,
                    "parameters": {
                        "start_time": "Please enter Start Time",
                        "end_time": "Please enter End Time",
                    },
                },
            }
        else:
            actions = {}
        return {
            'name': view.get_view_name(),
            'description': view.get_view_description(),
            'renders': [renderer.media_type for renderer in
                        view.renderer_classes],
            'parses': [parser.media_type for parser in view.parser_classes],
            'actions': actions,
        }
