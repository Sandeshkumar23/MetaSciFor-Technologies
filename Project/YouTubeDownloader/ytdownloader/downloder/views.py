from django.shortcuts import render, redirect
from django.http import HttpResponse
import yt_dlp as youtube_dl
import os

def index(request):
    # Get success message from the request
    success_message = request.GET.get('success')
    return render(request, 'youtube.html', {'success_message': success_message})

def download(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        ydl_opts = {
            'format': 'best',  # Download the best available format directly
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,  # Download single video
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = f"{info_dict['title']}.mp4"

            # Check if the file exists and return it
            if os.path.isfile(filename):
                with open(filename, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='video/mp4')
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                # Remove the file after sending
                os.remove(filename)
                
                # Redirect to the index page with a success message
                return redirect('/?success=Video%20%27' + info_dict['title'] + '%27%20successfully%20downloaded.')
    return HttpResponse("Successfully Downloaded.")
