from rest_framework.response import Response

def get_response(serializer):
    if serializer.is_valid():
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors, status = 500 )

def get_request_body(request, serializerInstance):
    serializer = serializerInstance( data = request.data )
    if serializer.is_valid():
        return serializer.validated_data
    else:
        raise TypeError(serializer.errors)

def checkLoggedIn(request):
    user = request.user
    auth = user.is_authenticated
    if not auth:
        raise AssertionError("Not Authenticated")