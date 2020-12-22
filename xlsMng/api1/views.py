from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
import pandas as pd
import numpy as np
from .models import File

class FileView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = request.FILES['file']
        #f1 = FileSerializer(data=request.FILES['file'])
        if file_serializer != None:
            #print(f1)
            #print(file_serializer)
            df = pd.read_excel(file_serializer)
            df.dropna()
            #print(df.head())
            df_pc = df.loc[df['Accepted Compound ID'].str.endswith('PC', na=False)]
            df_lpc = df.loc[df['Accepted Compound ID'].str.endswith('LPC', na=False)]
            df_plasma = df.loc[df['Accepted Compound ID'].str.endswith('plasmalogen', na=False)]
            #print(df_pc.head())
            #print(df_pc.shape)
            #file_serializer.save()
            writer = pd.ExcelWriter('media/task1.xlsx', engine='openpyxl')
            df_pc.to_excel(writer, sheet_name='PC')
            df_lpc.to_excel(writer, sheet_name='LPC')
            df_plasma.to_excel(writer, sheet_name='Plasmalogen')
            writer.save()
            #output = open("media/task1.xlsx")
            #f2.save()
            return Response("Success",status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ColumnView(APIView):
    def post(self, request, *args, **kwargs):
        file_copy = request.FILES['file']
        if file_copy != None:
            df = pd.read_excel(file_copy)
            df.dropna()
            #print(df.shape)
            df["Retention Time Roundoff (in mins)"] = round(df["Retention time (min)"]).astype(np.int64)
            #print(df.head())
            #print(df.shape)
            df.to_excel('media/task2.xlsx',index=False)
            return Response("Success",status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MeanView(APIView):
    def post(self, request, *args, **kwargs):
        file_copy = request.FILES['file']
        if file_copy != None:
            df = pd.read_excel(file_copy)
            df.dropna()
            df["Retention Time Roundoff"] = round(df["Retention time (min)"]).astype(np.int64)
            unique_val = df['Retention Time Roundoff'].unique()
            sum_initialised = { unique_val[i]:0 for i in range(len(unique_val))}
            count = df['Retention Time Roundoff'].value_counts()
            for i in range(df.shape[0]):
                sum_initialised[df['Retention Time Roundoff'].iloc[i]] = sum_initialised[df['Retention Time Roundoff'].iloc[i]] + df['m/z'].iloc[i]
            for i in sum_initialised.keys():
                sum_initialised[i] = sum_initialised[i]/count[i]
            df_2 =[ sum_initialised[df['Retention Time Roundoff'].iloc[i]] for i in range(df.shape[0])]
            df["Mean m/z"] = df_2
            df = df.drop(['m/z','Accepted Compound ID', 'Retention time (min)'],axis=1)
            df.to_excel('media/task3.xlsx',index=False)
            return Response("Success",status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)