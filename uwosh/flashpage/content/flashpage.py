from Products.ATContentTypes.content.document import ATDocumentBase, ATDocument, ATDocumentSchema
from uwosh.flashpage.interfaces import IFlashPage
from Products.Archetypes.atapi import *
from uwosh.flashpage.config import PROJECT_NAME
from zope.interface import implements
from AccessControl import ClassSecurityInfo
from uwosh.flashpage.Widget import FlashEmbeddableRichWidget
from Products.ATContentTypes.configuration import zconf
from uwosh.flashpage.config import mf as _


copied_fields = {}
copied_fields['text'] = ATDocumentSchema['text'].copy()

copied_fields['text'].widget.description = \
"""
To add video into the page, just insert the url inbetween the tags ###flashvideo### and ###/flashvideo###.
For example, ###flashvideo###www.example.com/someflashvideo.flv###/flashvideo###
"""

#FlashEmbeddableRichWidget(
#    description = \
#"""
#To add video into the page, just insert the url inbetween the tags ###flashvideo### and ###/flashvideo###.
#For example, ###flashvideo###www.example.com/someflashvideo.flv###/flashvideo###
#""",
#    label = _(u'label_body_text', default=u'Body Text'),
#    rows = 20,
#    allow_file_upload = zconf.ATDocument.allow_document_upload
#)

schema = Schema((

    copied_fields['text'],
    
    

))

FlashPageSchema = ATDocumentSchema.copy() + schema.copy()

class FlashPage(ATDocument):
    
    implements(IFlashPage)
    
    security = ClassSecurityInfo()
    schema = FlashPageSchema
    portal_type = "FlashPage"
    archetype_name = "FlashPage"
    meta_type = "FlashPage"

    
registerType(FlashPage, PROJECT_NAME)