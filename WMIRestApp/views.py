from django.http import HttpResponse
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination


def index(request):
    return HttpResponse('Lmao')


class AgentList(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        uniqueID = request.data['uniqueID']
        if Agent.objects.filter(Name=uniqueID).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            Agent.objects.create(uniqueID=uniqueID)
        return Response(status=status.HTTP_201_CREATED)


class AgentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentCPUMonitorList(generics.ListCreateAPIView):
    queryset = CPUMonitor.objects.all()
    serializer_class = CPUMonitorSerializer

    def create(self, request, *args, **kwargs):
        agent = get_object_or_404(Agent, uniqueID=self.kwargs.get('uniqueID'))
        name = request.data['Name']
        if CPUMonitor.objects.filter(Name=name).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            CPUMonitor.objects.create(agent=agent, Name=name)
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        queryset = super(AgentCPUMonitorList, self).get_queryset()
        return queryset.filter(agent__uniqueID=self.kwargs.get('uniqueID'))


class CPUMonitorInstanceList(generics.ListCreateAPIView):
    queryset = CPUInstance.objects.all()
    serializer_class = CPUInstanceSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        cpumonitor = get_object_or_404(CPUMonitor, id=self.kwargs.get('pk'))
        CPUInstance.objects.create(monitor=cpumonitor,
                                   InterruptPersec=request.data['InterruptPersec'],
                                   PercentInterruptTime=request.data['PercentInterruptTime'],
                                   PercentIdleTime=request.data['PercentIdleTime'],
                                   PercentPrivilegedTime=request.data['PercentPrivilegedTime'],
                                   PercentProcessorTime=request.data['PercentProcessorTime'],
                                   PercentUserTime=request.data['PercentUserTime'],
                                   RecordTime=request.data['RecordTime']
                                   )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super(CPUMonitorInstanceList, self).get_queryset()
        return queryset.filter(monitor__id=self.kwargs.get('pk'))


class AgentDiskMonitorList(generics.ListCreateAPIView):
    queryset = DiskMonitor.objects.all()
    serializer_class = DiskMonitorSerializer

    def create(self, request, *args, **kwargs):
        agent = get_object_or_404(Agent, uniqueID=self.kwargs.get('uniqueID'))
        DiskMonitor.objects.create(agent=agent, Name=request.data['Name'])
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        queryset = super(AgentDiskMonitorList, self).get_queryset()
        return queryset.filter(agent__uniqueID=self.kwargs.get('uniqueID'))


class DiskMonitorInstanceList(generics.ListCreateAPIView):
    queryset = DiskInstance.objects.all()
    serializer_class = DiskInstanceSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        diskmonitor = get_object_or_404(MemoryMonitor, id=self.kwargs.get('pk'))
        DiskInstance.objects.create(monitor=diskmonitor,
                                    DiskBytesPersec=request.data['DiskBytesPersec'],
                                    DiskReadBytesPersec=request.data['DiskReadBytesPersec'],
                                    DiskReadsPersec=request.data['DiskReadsPersec'],
                                    DiskTransfersPersec=request.data['DiskTransfersPersec'],
                                    DiskWriteBytesPersec=request.data['DiskWriteBytesPersec'],
                                    DiskWritesPersec=request.data['DiskWritesPersec'],
                                    PercentDiskReadTime=request.data['PercentDiskReadTime'],
                                    PercentDiskTime=request.data['PercentDiskTime'],
                                    PercentDiskWriteTime=request.data['PercentDiskWriteTime'],
                                    RecordTime=request.data['RecordTime']
                                    )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super(DiskMonitorInstanceList, self).get_queryset()
        return queryset.filter(monitor__id=self.kwargs.get('pk'))


class AgentMemoryMonitorList(generics.ListCreateAPIView):
    queryset = MemoryMonitor.objects.all()
    serializer_class = MemoryMonitorSerializer

    def create(self, request, *args, **kwargs):
        agent = get_object_or_404(Agent, uniqueID=self.kwargs.get('uniqueID'))
        MemoryMonitor.objects.create(agent=agent, CommitLimit=request.data['CommitLimit'])
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        queryset = super(AgentMemoryMonitorList, self).get_queryset()
        return queryset.filter(agent__uniqueID=self.kwargs.get('uniqueID'))


class MemoryMonitorInstanceList(generics.ListCreateAPIView):
    queryset = MemoryInstance.objects.all()
    serializer_class = MemoryInstanceSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        memorymonitor = get_object_or_404(MemoryMonitor, id=self.kwargs.get('pk'))
        MemoryInstance.objects.create(monitor=memorymonitor,
                                      AvailableBytes=request.data['AvailableBytes'],
                                      CacheBytes=request.data['CacheBytes'],
                                      CacheBytesPeak=request.data['CacheBytesPeak'],
                                      CommittedBytes=request.data['CommittedBytes'],
                                      PoolNonpagedAllocs=request.data['PoolNonpagedAllocs'],
                                      PoolNonpagedBytes=request.data['PoolNonpagedBytes'],
                                      PoolPagedAllocs=request.data['PoolPagedAllocs'],
                                      PoolPagedBytes=request.data['PoolPagedBytes'],
                                      PoolPagedResidentBytes=request.data['PoolPagedResidentBytes'],
                                      RecordTime=request.data['RecordTime'],
                                      )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super(MemoryMonitorInstanceList, self).get_queryset()
        return queryset.filter(monitor__id=self.kwargs.get('pk'))


class AgentNetworkMonitorList(generics.ListCreateAPIView):
    queryset = NetworkMonitor.objects.all()
    serializer_class = NetworkMonitorSerializer

    def create(self, request, *args, **kwargs):
        agent = get_object_or_404(Agent, uniqueID=self.kwargs.get('uniqueID'))
        NetworkMonitor.objects.create(agent=agent, Name=request.data['Name'])
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        queryset = super(AgentNetworkMonitorList, self).get_queryset()
        return queryset.filter(agent__uniqueID=self.kwargs.get('uniqueID'))


class NetworkMonitorInstanceList(generics.ListCreateAPIView):
    queryset = NetworkInstance.objects.all()
    serializer_class = NetworkInstanceSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        networkmonitor = get_object_or_404(NetworkMonitor, id=self.kwargs.get('pk'))
        NetworkInstance.objects.create(monitor=networkmonitor,
                                       CurrentBandwidth=request.data['CurrentBandwidth'],
                                       BytesReceivedPersec=request.data['BytesReceivedPersec'],
                                       BytesSentPersec=request.data['BytesSentPersec'],
                                       BytesTotalPersec=request.data['BytesTotalPersec'],
                                       PacketsPersec=request.data['PacketsPersec'],
                                       PacketsSentPersec=request.data['PacketsSentPersec'],
                                       PacketsReceivedPersec=request.data['PacketsReceivedPersec'],
                                       RecordTime=request.data['RecordTime'],
                                       )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super(NetworkMonitorInstanceList, self).get_queryset()
        return queryset.filter(monitor__id=self.kwargs.get('pk'))


class AgentPhysicalMemoryMonitorList(generics.ListCreateAPIView):
    queryset = PhysicalMemoryMonitor.objects.all()
    serializer_class = PhysicalMemoryMonitorSerializer

    def create(self, request, *args, **kwargs):
        agent = get_object_or_404(Agent, uniqueID=self.kwargs.get('uniqueID'))
        PhysicalMemoryMonitor.objects.create(agent=agent,
                                             BankLabel=request.data['BankLabel'],
                                             Capacity=request.data['Capacity'],
                                             DataWidth=request.data['DataWidth'],
                                             DeviceLocator=request.data['DeviceLocator'],
                                             HotSwappable=request.data['HotSwappable'],
                                             Manufacturer=request.data['Manufacturer'],
                                             SerialNumber=request.data['SerialNumber'],
                                             Speed=request.data['Speed'],
                                             PartNumber=request.data['PartNumber'],
                                             )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        queryset = super(AgentPhysicalMemoryMonitorList, self).get_queryset()
        return queryset.filter(agent__uniqueID=self.kwargs.get('uniqueID'))


class AgentProcessorMonitorList(generics.ListCreateAPIView):
    queryset = ProcessorMonitor.objects.all()
    serializer_class = ProcessorMonitorSerializer

    def create(self, request, *args, **kwargs):
        agent = get_object_or_404(Agent, uniqueID=self.kwargs.get('uniqueID'))
        ProcessorMonitor.objects.create(agent=agent,
                                        AddressWidth=request.data['AddressWidth'],
                                        Architecture=request.data['Architecture'],
                                        AssetTag=request.data['AssetTag'],
                                        Availability=request.data['Availability'],
                                        Caption=request.data['Caption'],
                                        DataWidth=request.data['DataWidth'],
                                        Family=request.data['Family'],
                                        L2CacheSize=request.data['L2CacheSize'],
                                        L3CacheSize=request.data['L3CacheSize'],
                                        Manufacturer=request.data['Manufacturer'],
                                        Name=request.data['Name'],
                                        NumberOfCores=request.data['NumberOfCores'],
                                        NumberOfLogicalProcessors=request.data['NumberOfLogicalProcessors'],
                                        PartNumber=request.data['PartNumber'],
                                        ProcessorId=request.data['ProcessorId'],
                                        ProcessorType=request.data['ProcessorType'],
                                        Revision=request.data['Revision'],
                                        Status=request.data['Status'],
                                        SocketDesignation=request.data['SocketDesignation'],
                                        )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        queryset = super(AgentProcessorMonitorList, self).get_queryset()
        return queryset.filter(agent__uniqueID=self.kwargs.get('uniqueID'))


class ProcessorMonitorInstanceList(generics.ListCreateAPIView):
    queryset = ProcessorInstance.objects.all()
    serializer_class = ProcessorInstanceSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        processormonitor = get_object_or_404(ProcessorMonitor, id=self.kwargs.get('pk'))
        ProcessorInstance.objects.create(monitor=processormonitor,
                                         CurrentClockSpeed=request.data['CurrentClockSpeed'],
                                         ExtClock=request.data['ExtClock'],
                                         LoadPercentage=request.data['LoadPercentage'],
                                         MaxClockSpeed=request.data['MaxClockSpeed'],
                                         RecordTime=request.data['RecordTime'],
                                         )
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super(ProcessorMonitorInstanceList, self).get_queryset()
        return queryset.filter(monitor__id=self.kwargs.get('pk'))
