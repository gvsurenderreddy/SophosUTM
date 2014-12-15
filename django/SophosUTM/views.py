from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('SophosUTM:home.html')
@login_required
def home(request):
    return {
        "message": "Hello World from SophosUTM!",
        "app_name": "SophosUTM"
    }