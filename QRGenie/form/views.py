import qrcode
import base64
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def generate_qr_code(request):

    if request.method == 'POST':
        
        text = request.POST.get('text', '')

        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        # qr.add_data(text)
        image = qrcode.make(text)
        # print(image)  
        
        # qr.make(fit=True)
        # img = qr.make_image(fill_color="black", back_color="white")
        # response = HttpResponse(content_type="image/png")
        image.save("code.png")
        with open("code.png", "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
            converted_string=str(converted_string)
            fstr=converted_string[2:-1]
            fstr="data:image/png;base64,"+fstr
        print(fstr)
        img = {"img":fstr}
        return render(request, 'form copy.html', img)

    return render(request, 'form.html')

def form1(request):
    return render(request, 'form copy.html')

    
