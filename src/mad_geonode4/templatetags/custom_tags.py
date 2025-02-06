from django import template

register = template.Library()


@register.simple_tag
def get_base_left_topbar_menu_custom():
    return [
        {
            "type": "link",
            "href": "/catalogue/#/all",
            "label": "All resources",
        },
        {
            "type": "link",
            "href": "/catalogue/#/datasets",
            "label": "Datasets",
        },
        {
            "type": "link", 
            "href": "/catalogue/#/maps", 
            "label": "Maps"
        },
        {
            "type": "link",
            "href": "/catalogue/#/documents",
            "label": "Documents",
        },
    ]