from django.http import HttpResponse

def saludo(request):
    return HttpResponse ("Hola Juan Carlos, como estás chupa pija.")

def despedida (request):
    return HttpResponse ("Nos vemos manga de chupas píjas.")




