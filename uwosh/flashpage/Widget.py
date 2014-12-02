from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Archetypes.Widget import RichWidget
from Products.Archetypes.Registry import registerWidget

class FlashEmbeddableRichWidget(RichWidget):
    _properties = RichWidget._properties.copy()
    _properties.update({
        'macro' : "widgets/rich",
        'rows'  : 5,
        'cols'  : 40,
        'format': 1,
        'allow_file_upload': True,
        })
    
    
    def __call__(self, instance, context, *args, **kwargs):
        self.instance = instance
        self.context = context
        return ViewPageTemplateFile('richflashwidget.pt')()
        
registerWidget(FlashEmbeddableRichWidget,
               title='FlashEmbeddableRichWidget',
               description='Renders rich text with embedded flash',
               used_for=('Products.Archetypes.Field.TextField',)
               )