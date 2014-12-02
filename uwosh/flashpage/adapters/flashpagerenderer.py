from zope.interface import implements
from zope.component import adapts
from uwosh.flashpage.interfaces import IFlashPageRenderer, IFlashPage
from uwosh.flashpage.content.flashpage import FlashPage
import re
from uwosh.flashpage.generators import *

TAG_SIGNIFIER = "###"
CLOSE_SIGNIFIER = "/"

BASE_TAGS = {
    'flashvideo':{
		'width': 320,
		'height': 280,
		'quality': 'high',
		'align': 'middle',
		'play': 'true',
		'loop': 'false',
		'scale': 'showall',
		'wmode': 'window',
		'devicefont': 'false',
		'bgcolor': '#ffffff',
		'menu': 'true',
		'allowScriptAccess': 'sameDomain',
		'allowFullScreen': 'true',
		'salign': ''
    }
}

TAG_REPLACERS = {
    'flashvideo': generate_flashvideo
}

class FlashPageRenderer(object):
    implements(IFlashPageRenderer)
    adapts(FlashPage)
    
    def __init__(self, flashpage):
        self.flashpage = flashpage
        self.text = self.flashpage.getText()
        self.possible_tags = BASE_TAGS.copy()
        
    def getTag(self, start):
        found_tag = None
        
        for tag in self.possible_tags.keys():
            the_tag = self.text[start + len(TAG_SIGNIFIER) : start + len(TAG_SIGNIFIER) + len(tag)]
            
            if the_tag.lower() == tag:
                found_tag = tag
                break
                
        return found_tag
        
    def getOptions(self, start, found_tag):

        this_tags_options = self.possible_tags[found_tag].copy()
        open_tag_end = self.text.find(TAG_SIGNIFIER, start + len(found_tag))
    
        text_options = self.text[start + len(TAG_SIGNIFIER) + len(found_tag) : open_tag_end]
    
        if len(text_options) > 0:
        
            for option in text_options.strip(" ").split(" "):
                key, value = option.split("=")
                value = value.strip("'").strip('"').strip(" ")
                key = key.lower().strip(" ")
            
                if this_tags_options.has_key(key):
                    this_tags_options[key] = value
                    
        return this_tags_options, open_tag_end
    
    def getCloseTagEnd(self, start, tag):
        the_tag = self.text[start + len(TAG_SIGNIFIER) + len(CLOSE_SIGNIFIER) : start + len(TAG_SIGNIFIER) + len(CLOSE_SIGNIFIER) + len(tag)]

        if the_tag.lower() == tag:
            return start + len(TAG_SIGNIFIER) + len(CLOSE_SIGNIFIER) + len(the_tag)
            
    def getGeneratedFromTag(self, tag, url, options):
        return TAG_REPLACERS[tag](url, options)
        
    def applyTag(self, start, end, tag, url, options):
        self.text = self.text[:start] + self.getGeneratedFromTag(tag, url, options) + self.text[end:]
        
    def renderText(self):
        possible_tags = BASE_TAGS.copy()
        
        open_tag_start = self.text.find(TAG_SIGNIFIER)
        open_tag_end = None
        while open_tag_start != -1:
            open_tag_end = 0
            this_tags_options = None
            
            found_tag = self.getTag(open_tag_start)
            
            if found_tag:
                options, open_tag_end = self.getOptions(open_tag_start, found_tag)
            
                close_tag_start = self.text.find(TAG_SIGNIFIER, open_tag_end + len(TAG_SIGNIFIER) + len(CLOSE_SIGNIFIER))
            
                url = self.text[open_tag_end + len(TAG_SIGNIFIER) : close_tag_start].strip(" ")
                
                close_tag_end = self.getCloseTagEnd(close_tag_start, found_tag)
                
                if self.text[close_tag_end:close_tag_end + len(TAG_SIGNIFIER)] == TAG_SIGNIFIER:
                    self.applyTag(open_tag_start, close_tag_end + len(TAG_SIGNIFIER), found_tag, url, options)
                
            
            open_tag_start = self.text.find(TAG_SIGNIFIER)
        
                
        return self.text