from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['POST'])
def push_records(request):
    uniqueID = request.data['UniqueID']
    agent = Agent.objects.filter(uniqueID=uniqueID).first()
    if agent is None:
        # create the agent
        agent = Agent.objects.create(uniqueID=uniqueID)

    monitors = request.data['Monitors']
    str = ''
    for monitor in monitors:
        if 'CPUMonitor' == monitor['Name']:
            if 'Devices' in monitor:
                str = push_cpu_monitor(agent, monitor['Devices'])

        elif 'DiskMonitor' == monitor['Name']:
            if 'Devices' in monitor:
                push_disk_monitor(agent, monitor['Devices'])

        elif 'MemoryMonitor' == monitor['Name']:
            if 'Devices' in monitor:
                push_memory_monitor(agent, monitor['Devices'])

        elif 'NetworkMonitor' == monitor['Name']:
            if 'Devices' in monitor:
                push_network_monitor(agent, monitor['Devices'])

        elif 'PhysicalMemoryMonitor' == monitor['Name']:
            if 'Devices' in monitor:
                push_physical_memory_monitor(agent, monitor['Devices'])

        elif 'ProcessorMonitor' == monitor['Name']:
            if 'Devices' in monitor:
                push_processor_monitor(agent, monitor['Devices'])

    return Response('Lmao',status=status.HTTP_200_OK)


def push_cpu_monitor(agent, cpumonitor):
    for device in cpumonitor:
        Name = None
        if 'Info' in device:
            if 'Name' in device['Info']:
                Name = device['Info']['Name']

        # create monitor if not exist
        monitor = CPUMonitor.objects.filter(Name=Name, agent=agent).first()
        if monitor is None:
            monitor = CPUMonitor.objects.create(agent=agent, Name=Name)

        # extract records
        if 'Records' in device:
            push_cpu_instance(monitor, device['Records'])


def push_disk_monitor(agent, diskmonitor):
    for device in diskmonitor:
        Name = None
        if 'Info' in device:
            if 'Name' in device['Info']:
                Name = device['Info']['Name']

        # create monitor if not exist
        monitor = DiskMonitor.objects.filter(Name=Name, agent=agent).first()
        if monitor is None:
            monitor = DiskMonitor.objects.create(agent=agent, Name=Name)

        # extract records
        if 'Records' in device:
            push_disk_instance(monitor, device['Records'])


def push_memory_monitor(agent, memorymonitor):
    for device in memorymonitor:
        CommitLimit = None
        if 'Info' in device:
            if 'CommitLimit' in device['Info']:
                CommitLimit = device['Info']['CommitLimit']

        # create monitor if not exist
        monitor = MemoryMonitor.objects.filter(CommitLimit=CommitLimit, agent=agent).first()
        if monitor is None:
            monitor = MemoryMonitor.objects.create(CommitLimit=CommitLimit, agent=agent)

        # extract records
        if 'Records' in device:
            push_memory_instance(monitor, device['Records'])


def push_network_monitor(agent, networkmonitor):
    for device in networkmonitor:
        Name = None
        if 'Info' in device:
            if 'Name' in device['Info']:
                Name = device['Info']['Name']

        # create monitor if not exist
        monitor = NetworkMonitor.objects.filter(Name=Name, agent=agent).first()
        if monitor is None:
            monitor = NetworkMonitor.objects.create(agent=agent, Name=Name)

        # extract records
        if 'Records' in device:
            push_network_instance(monitor, device['Records'])


def push_physical_memory_monitor(agent, physicalmemorymonitor):
    for device in physicalmemorymonitor:
        BankLabel = None
        Capacity = None
        DataWidth = None
        DeviceLocator = None
        HotSwappable = 'False'
        Manufacturer = None
        SerialNumber = None
        Speed = None
        PartNumber = None

        if 'Info' in device:
            if 'BankLabel' in device['Info']:
                BankLabel = device['Info']['BankLabel']
            if 'Capacity' in device['Info']:
                Capacity = device['Info']['Capacity']
            if 'DataWidth' in device['Info']:
                DataWidth = device['Info']['DataWidth']
            if 'DeviceLocator' in device['Info']:
                DeviceLocator = device['Info']['DeviceLocator']
            if 'HotSwappable' in device['Info']:
                HotSwappable = device['Info']['HotSwappable']
            if 'Manufacturer' in device['Info']:
                Manufacturer = device['Info']['Manufacturer']
            if 'SerialNumber' in device['Info']:
                SerialNumber = device['Info']['SerialNumber']
            if 'Speed' in device['Info']:
                Speed = device['Info']['Speed']
            if 'PartNumber' in device['Info']:
                PartNumber = device['Info']['PartNumber']

        # create monitor if not exist
        monitor = PhysicalMemoryMonitor.objects.filter(PartNumber=PartNumber, agent=agent,
                                                       SerialNumber=SerialNumber).first()
        if monitor is None:
            PhysicalMemoryMonitor.objects.create(agent=agent, BankLabel=BankLabel,
                                                 Capacity=Capacity, DataWidth=DataWidth,
                                                 DeviceLocator=DeviceLocator, HotSwappable=HotSwappable,
                                                 Manufacturer=Manufacturer, SerialNumber=SerialNumber,
                                                 Speed=Speed, PartNumber=PartNumber)

            # no records to extract


def push_processor_monitor(agent, processormonitor):
    for device in processormonitor:
        AddressWidth = None
        Architecture = None
        AssetTag = None
        Availability = None
        Caption = None
        DataWidth = None
        Family = None
        L2CacheSize = None
        L3CacheSize = None
        Manufacturer = None
        Name = None
        NumberOfCores = None
        NumberOfLogicalProcessors = None
        PartNumber = None
        ProcessorId = None
        ProcessorType = None
        Revision = None
        Status = None
        SocketDesignation = None
        if 'Info' in device:
            if 'AddressWidth' in device['Info']:
                AddressWidth = device['Info']['AddressWidth']
            if 'Architecture' in device['Info']:
                Architecture = device['Info']['Architecture']
            if 'AssetTag' in device['Info']:
                AssetTag = device['Info']['AssetTag']
            if 'Availability' in device['Info']:
                Availability = device['Info']['Availability']
            if 'Caption' in device['Info']:
                Caption = device['Info']['Caption']
            if 'DataWidth' in device['Info']:
                DataWidth = device['Info']['DataWidth']
            if 'Family' in device['Info']:
                Family = device['Info']['Family']
            if 'L2CacheSize' in device['Info']:
                L2CacheSize = device['Info']['L2CacheSize']
            if 'L3CacheSize' in device['Info']:
                L3CacheSize = device['Info']['L3CacheSize']
            if 'Manufacturer' in device['Info']:
                Manufacturer = device['Info']['Manufacturer']
            if 'Name' in device['Info']:
                Name = device['Info']['Name']
            if 'NumberOfCores' in device['Info']:
                NumberOfCores = device['Info']['NumberOfCores']
            if 'NumberOfLogicalProcessors' in device['Info']:
                NumberOfLogicalProcessors = device['Info']['NumberOfLogicalProcessors']
            if 'PartNumber' in device['Info']:
                PartNumber = device['Info']['PartNumber']
            if 'ProcessorId' in device['Info']:
                ProcessorId = device['Info']['ProcessorId']
            if 'ProcessorType' in device['Info']:
                ProcessorType = device['Info']['ProcessorType']
            if 'Revision' in device['Info']:
                Revision = device['Info']['Revision']
            if 'Status' in device['Info']:
                Status = device['Info']['Status']
            if 'SocketDesignation' in device['Info']:
                SocketDesignation = device['Info']['SocketDesignation']

        # create monitor if not exist
        monitor = ProcessorMonitor.objects.filter(ProcessorId=ProcessorId, agent=agent).first()
        if monitor is None:
            monitor = ProcessorMonitor.objects.create(agent=agent, AddressWidth=AddressWidth,
                                                      Architecture=Architecture, AssetTag=AssetTag,
                                                      Availability=Availability, Caption=Caption,
                                                      DataWidth=DataWidth, Family=Family,
                                                      L2CacheSize=L2CacheSize, L3CacheSize=L3CacheSize,
                                                      Manufacturer=Manufacturer, Name=Name,
                                                      NumberOfCores=NumberOfCores,
                                                      NumberOfLogicalProcessors=NumberOfLogicalProcessors,
                                                      PartNumber=PartNumber, ProcessorId=ProcessorId,
                                                      ProcessorType=ProcessorType, Revision=Revision,
                                                      Status=Status, SocketDesignation=SocketDesignation)

        # extract records
        if 'Records' in device:
            push_processor_instance(monitor, device['Records'])


def push_cpu_instance(cpumonitor, records):
    for instance in records:
        InterruptsPersec = None
        PercentProcessorTime = None
        PercentUserTime = None
        PercentIdleTime = None
        PercentPrivilegedTime = None
        PercentInterruptTime = None
        RecordTime = None
        if 'Attributes' in instance:
            attributes = instance['Attributes']
            if 'InterruptsPersec' in attributes:
                InterruptsPersec = attributes['InterruptsPersec']
            if 'PercentProcessorTime' in attributes:
                PercentProcessorTime = attributes['PercentProcessorTime']
            if 'PercentUserTime' in attributes:
                PercentUserTime = attributes['PercentUserTime']
            if 'PercentIdleTime' in attributes:
                PercentIdleTime = attributes['PercentIdleTime']
            if 'PercentPrivilegedTime' in attributes:
                PercentPrivilegedTime = attributes['PercentPrivilegedTime']
            if 'PercentInterruptTime' in attributes:
                PercentInterruptTime = attributes['PercentInterruptTime']
            if 'RecordTime' in instance:
                RecordTime = instance['RecordTime']

        CPUInstance.objects.create(monitor=cpumonitor,
                                   InterruptsPersec=InterruptsPersec,
                                   PercentIdleTime=PercentIdleTime,
                                   PercentInterruptTime=PercentInterruptTime,
                                   PercentPrivilegedTime=PercentPrivilegedTime,
                                   PercentProcessorTime=PercentProcessorTime,
                                   PercentUserTime=PercentUserTime,
                                   RecordTime=RecordTime,
                                   )


def push_disk_instance(diskmonitor, records):
    for instance in records:
        DiskBytesPersec = None
        DiskReadBytesPersec = None
        DiskReadsPersec = None
        DiskTransfersPersec = None
        DiskWriteBytesPersec = None
        DiskWritesPersec = None
        PercentDiskReadTime = None
        PercentDiskTime = None
        PercentDiskWriteTime = None
        RecordTime = None
        if 'Attributes' in instance:
            attributes = instance['Attributes']
            if 'DiskBytesPersec' in attributes:
                DiskBytesPersec = attributes['DiskBytesPersec']
            if 'DiskReadBytesPersec' in attributes:
                DiskReadBytesPersec = attributes['DiskReadBytesPersec']
            if 'DiskReadsPersec' in attributes:
                DiskReadsPersec = attributes['DiskReadsPersec']
            if 'DiskTransfersPersec' in attributes:
                DiskTransfersPersec = attributes['DiskTransfersPersec']
            if 'DiskWriteBytesPersec' in attributes:
                DiskWriteBytesPersec = attributes['DiskWriteBytesPersec']
            if 'DiskWritesPersec' in attributes:
                DiskWritesPersec = attributes['DiskWritesPersec']
            if 'PercentDiskReadTime' in attributes:
                PercentDiskReadTime = attributes['PercentDiskReadTime']
            if 'PercentDiskTime' in attributes:
                PercentDiskTime = attributes['PercentDiskTime']
            if 'PercentDiskWriteTime' in attributes:
                PercentDiskWriteTime = attributes['PercentDiskWriteTime']
            if 'RecordTime' in instance:
                RecordTime = instance['RecordTime']

        DiskInstance.objects.create(monitor=diskmonitor,
                                    DiskBytesPersec=DiskBytesPersec,
                                    DiskReadBytesPersec=DiskReadBytesPersec,
                                    DiskReadsPersec=DiskReadsPersec,
                                    DiskTransfersPersec=DiskTransfersPersec,
                                    DiskWriteBytesPersec=DiskWriteBytesPersec,
                                    DiskWritesPersec=DiskWritesPersec,
                                    PercentDiskReadTime=PercentDiskReadTime,
                                    PercentDiskTime=PercentDiskTime,
                                    PercentDiskWriteTime=PercentDiskWriteTime,
                                    RecordTime=RecordTime,
                                    )


def push_memory_instance(memorymonitor, records):
    for instance in records:
        AvailableBytes = None
        CacheBytes = None
        CacheBytesPeak = None
        CommittedBytes = None
        PoolNonpagedAllocs = None
        PoolNonpagedBytes = None
        PoolPagedAllocs = None
        PoolPagedBytes = None
        PoolPagedResidentBytes = None
        RecordTime = None
        if 'Attributes' in instance:
            attributes = instance['Attributes']
            if 'AvailableBytes' in attributes:
                AvailableBytes = attributes['AvailableBytes']
            if 'CacheBytes' in attributes:
                CacheBytes = attributes['CacheBytes']
            if 'CacheBytesPeak' in attributes:
                CacheBytesPeak = attributes['CacheBytesPeak']
            if 'CommittedBytes' in attributes:
                CommittedBytes = attributes['CommittedBytes']
            if 'PoolNonpagedAllocs' in attributes:
                PoolNonpagedAllocs = attributes['PoolNonpagedAllocs']
            if 'PoolNonpagedBytes' in attributes:
                PoolNonpagedBytes = attributes['PoolNonpagedBytes']
            if 'PoolPagedAllocs' in attributes:
                PoolPagedAllocs = attributes['PoolPagedAllocs']
            if 'PoolPagedBytes' in attributes:
                PoolPagedBytes = attributes['PoolPagedBytes']
            if 'PoolPagedResidentBytes' in attributes:
                PoolPagedResidentBytes = attributes['PoolPagedResidentBytes']
            if 'RecordTime' in instance:
                RecordTime = instance['RecordTime']

        MemoryInstance.objects.create(monitor=memorymonitor,
                                      AvailableBytes=AvailableBytes,
                                      CacheBytes=CacheBytes,
                                      CacheBytesPeak=CacheBytesPeak,
                                      CommittedBytes=CommittedBytes,
                                      PoolNonpagedAllocs=PoolNonpagedAllocs,
                                      PoolNonpagedBytes=PoolNonpagedBytes,
                                      PoolPagedAllocs=PoolPagedAllocs,
                                      PoolPagedBytes=PoolPagedBytes,
                                      PoolPagedResidentBytes=PoolPagedResidentBytes,
                                      RecordTime=RecordTime,
                                      )


def push_network_instance(networkmonitor, records):
    for instance in records:
        CurrentBandwidth = None
        BytesReceivedPersec = None
        BytesSentPersec = None
        BytesTotalPersec = None
        PacketsPersec = None
        PacketsSentPersec = None
        PacketsReceivedPersec = None
        RecordTime = None
        if 'Attributes' in instance:
            attributes = instance['Attributes']
            if 'CurrentBandwidth' in attributes:
                CurrentBandwidth = attributes['CurrentBandwidth']
            if 'BytesReceivedPersec' in attributes:
                BytesReceivedPersec = attributes['BytesReceivedPersec']
            if 'BytesSentPersec' in attributes:
                BytesSentPersec = attributes['BytesSentPersec']
            if 'BytesTotalPersec' in attributes:
                BytesTotalPersec = attributes['BytesTotalPersec']
            if 'PacketsPersec' in attributes:
                PacketsPersec = attributes['PacketsPersec']
            if 'PacketsSentPersec' in attributes:
                PacketsSentPersec = attributes['PacketsSentPersec']
            if 'PacketsReceivedPersec' in attributes:
                PacketsReceivedPersec = attributes['PacketsReceivedPersec']
            if 'RecordTime' in instance:
                RecordTime = instance['RecordTime']

        NetworkInstance.objects.create(monitor=networkmonitor,
                                       CurrentBandwidth=CurrentBandwidth,
                                       BytesReceivedPersec=BytesReceivedPersec,
                                       BytesSentPersec=BytesSentPersec,
                                       BytesTotalPersec=BytesTotalPersec,
                                       PacketsPersec=PacketsPersec,
                                       PacketsSentPersec=PacketsSentPersec,
                                       PacketsReceivedPersec=PacketsReceivedPersec,
                                       RecordTime=RecordTime,
                                       )


def push_processor_instance(processormonitor, records):
    for instance in records:
        CurrentClockSpeed = None
        ExtClock = None
        LoadPercentage = None
        MaxClockSpeed = None
        RecordTime = None
        if 'Attributes' in instance:
            attributes = instance['Attributes']
            if 'CurrentClockSpeed' in attributes:
                CurrentClockSpeed = attributes['CurrentClockSpeed']
            if 'ExtClock' in attributes:
                ExtClock = attributes['ExtClock']
            if 'LoadPercentage' in attributes:
                LoadPercentage = attributes['LoadPercentage']
            if 'MaxClockSpeed' in attributes:
                MaxClockSpeed = attributes['MaxClockSpeed']
            if 'RecordTime' in instance:
                RecordTime = instance['RecordTime']

        ProcessorInstance.objects.create(monitor=processormonitor,
                                         CurrentClockSpeed=CurrentClockSpeed,
                                         ExtClock=ExtClock,
                                         LoadPercentage=LoadPercentage,
                                         MaxClockSpeed=MaxClockSpeed,
                                         RecordTime=RecordTime,
                                         )
