from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CohortViewSet():
    pass


class NativeViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['get'])
    def call_myself(self, request):
        return Response({})
