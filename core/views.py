from django.shortcuts import render, HttpResponse

html_base = """
<h1> TT ARENA </h1>
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="about/">About</a></li>
</ul>    
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """ 
        <h2>Landing page<h2> 
        <p>Welcome to TT Arena</p>
    """)

def about(request):
    return HttpResponse(html_base + """ 
            <h2>About TTArena<h2>
            <p>An online Tabletop Arena game based on WoW</p>
        """)
