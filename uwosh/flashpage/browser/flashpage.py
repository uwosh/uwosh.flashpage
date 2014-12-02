from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from plone.memoize.instance import memoize
from uwosh.flashpage.adapters.flashpagerenderer import FlashPageRenderer

class View(BrowserView):
    
    template = ViewPageTemplateFile('flashpage_view.pt')
    
    def __init__(self, *args, **kwargs):
        super(BrowserView, self).__init__(*args, **kwargs)
        
        self.renderer = FlashPageRenderer(self.context)
    
    def __call__(self):
        return self.template()
        
    def getText(self):
        return self.renderer.renderText()