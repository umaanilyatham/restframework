from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeAPIView(APIView):

    def get(self, request, pk=None):

        if pk:

            employee = Employee.objects.get(id=pk)

            serializer = EmployeeSerializer(employee)

            return Response(serializer.data)

        employees = Employee.objects.all()

        serializer = EmployeeSerializer(
            employees,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = EmployeeSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    def put(self, request, pk=None):

        employee = Employee.objects.get(id=pk)

        serializer = EmployeeSerializer(
            employee,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)
    

    def delete(self, request, pk=None):

        employee = Employee.objects.get(id=pk)

        employee.delete()

        return Response({
            "message": "Employee Deleted Successfully"
        })