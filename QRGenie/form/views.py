import qrcode
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def generate_qr_code(request):

    if request.method == 'POST':
        
        text = request.POST.get('text', '')

        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)

        
        img = qr.make_image(fill_color="black", back_color="white")

        
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        return response

    return render(request, 'form.html')


    
