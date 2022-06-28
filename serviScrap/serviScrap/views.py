from django.shortcuts import redirect


def redirect_scrap(request):
    return redirect('scrap_run_url', permanent=True)
