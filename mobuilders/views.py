from django.shortcuts import render

class views:
    def index(request):

        if request.method == 'GET':
            print('Halo')

            return render(request,'index.html')