from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializer import PatchRequestSerializer, PostRequestSerializer, EmployeeResponseSerializer
from utils.utils import get_request_body, get_response, checkLoggedIn


class manageEmployees(APIView):
    def post(self, request):
        try:
            checkLoggedIn(request)
            body = get_request_body( request, PostRequestSerializer )
            new_employee = Employee.objects.create(**body)
            new_employee.save()
            responseSerializer = EmployeeResponseSerializer( data = new_employee.__dict__ )
            return get_response(responseSerializer)
        
        except Exception as exp:
            return Response(str(exp), status = 500 )
    
    def get(self, request):
        try:
            checkLoggedIn(request)
            employees = [employee.__dict__ for employee in list(Employee.objects.all())]
            responseSerializer = EmployeeResponseSerializer( data = employees, many = True )
            return get_response(responseSerializer)
        
        except Exception as exp:
            return Response(str(exp), status = 500 )

class manageEmployee(APIView):
    def get(self, request, employeeId):
        try:
            checkLoggedIn(request)
            employee = Employee.objects.get( id = employeeId ).__dict__
            responseSerializer = EmployeeResponseSerializer( data = employee )
            return get_response(responseSerializer)

        except Exception as exp:
            return Response(str(exp), status = 500 )

    def patch(self, request, employeeId):
        try: 
            checkLoggedIn(request)
            body = get_request_body( request, PatchRequestSerializer )
            employee = Employee.objects.get( id = employeeId )
            for attr, value in body.items():
                setattr(employee, attr, value)
            employee.save()
            responseSerializer = EmployeeResponseSerializer( data = employee.__dict__ )
            return get_response( responseSerializer )

        except Exception as exp:
            return Response(str(exp), status = 500 )
    
    def delete(self, request, employeeId):
        try:
            checkLoggedIn(request)
            employee = Employee.objects.get( id = employeeId )
            response = employee.delete()
            return Response(response[0])

        except Exception as exp:
            return Response(str(exp), status = 500 )