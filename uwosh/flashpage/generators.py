import random

def generate_flashvideo(url, options):
    id = str(random.randint(0, 1000000))
    return \
"""
<div id="%s"><a href="http://www.macromedia.com/go/getflashplayer">Get the Flash Player</a> to see this player.</div>
<script type="text/javascript">
	var s1 = new SWFObject("++resource++player.swf","player","%s","%s","9","%s");
	s1.addParam("allowfullscreen","true");
	s1.addParam("allowscriptaccess","always");
	s1.addParam("flashvars","file=%s");
	s1.write("%s");
</script>

""" % (
    id,
    options['width'],
    options['height'],
    options['bgcolor'],
    url,
    id
)