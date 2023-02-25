from django.http import HttpResponse
def handler404(request,exception):
    return HttpResponse("404 Page Not Found")
    # here we are returning a HttpResponse object which is a response object.
    # here request parameter is the request object which is sent by the client.
    # and exception parameter is the exception object which is raised by the server.