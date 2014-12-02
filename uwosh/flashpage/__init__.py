from uwosh.flashpage import content
from Products.Archetypes import atapi
from Products.CMFCore import utils as cmfutils
ADD_CONTENT_PERMISSION = "Add portal content"
from uwosh.flashpage import Widget

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    import content
    import Widget

    content_types, constructors, ftis = atapi.process_types(atapi.listTypes('uwosh.flashpage'), 'uwosh.flashpage')

    cmfutils.ContentInit(
        'uwosh.flashpage Content',
        content_types = content_types,
        permission = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti = ftis,
        ).initialize(context)