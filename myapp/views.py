# views.py
from django.shortcuts import render
import replicate

def run_replicate_model(request):
    # Your Replicate model code goes here
    result = replicate.run(
        "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
        input={"prompt": "a 19th century portrait of a wombat gentleman"},
        
    )
    result_url = result[0] if result and isinstance(result, list) else None

    # Process the result or pass it to the template
    context = {"result_url": result_url}
    return render(request, 'your_template.html', context)
