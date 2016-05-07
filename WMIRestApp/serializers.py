from rest_framework import serializers
from .models import Agent
from .models import CPUMonitor, DiskMonitor, NetworkMonitor, PhysicalMemoryMonitor, MemoryMonitor, ProcessorMonitor
from .models import CPUInstance, DiskInstance, NetworkInstance, MemoryInstance, ProcessorInstance


class AgentSerializer(serializers.ModelSerializer):
    CPUMonitor_list = serializers.HyperlinkedIdentityField(
        view_name='agent-cpumonitor-list', lookup_field='uniqueID')

    DiskMonitor_list = serializers.HyperlinkedIdentityField(
        view_name='agent-diskmonitor_list', lookup_field='uniqueID')

    MemoryMonitors_list = serializers.HyperlinkedIdentityField(
        view_name='agent-memorymonitors_list', lookup_field='uniqueID')

    NetworkMonitors_list = serializers.HyperlinkedIdentityField(
        view_name='agent-networkmonitors_list', lookup_field='uniqueID')

    PhysicalMemoryMonitors_list = serializers.HyperlinkedIdentityField(
        view_name='agent-physicalmonitors_list', lookup_field='uniqueID')

    ProcessorMonitors_list = serializers.HyperlinkedIdentityField(
        view_name='agent-processormonitors_list', lookup_field='uniqueID')

    class Meta:
        model = Agent
        fields = ('uniqueID', 'CPUMonitor_list',
                  'DiskMonitor_list', 'MemoryMonitors_list',
                  'NetworkMonitors_list', 'PhysicalMemoryMonitors_list',
                  'ProcessorMonitors_list',)


class CPUMonitorSerializer(serializers.ModelSerializer):
    CPUInstances_list = serializers.HyperlinkedIdentityField(
        view_name='cpumonitorinstances_list')
    Name = serializers.CharField()

    def get_validation_exclusions(self):
        exclusions = super(CPUMonitorSerializer, self).get_validation_exclusions()
        return exclusions + ['agent']

    class Meta:
        model = CPUMonitor


class CPUInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPUInstance
        fields = ('InterruptsPersec', 'PercentIdleTime',
                  'PercentInterruptTime', 'PercentPrivilegedTime',
                  'PercentProcessorTime', 'PercentUserTime',
                  'RecordTime',)


class DiskMonitorSerializer(serializers.ModelSerializer):
    DiskInstances_list = serializers.HyperlinkedIdentityField(
        view_name='diskmonitorinstances_list')
    Name = serializers.CharField()

    def get_validation_exclusions(self):
        exclusions = super(DiskMonitorSerializer, self).get_validation_exclusions()
        return exclusions + ['agent']

    class Meta:
        model = DiskMonitor


class DiskInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskInstance
        fields = ('DiskBytesPersec', 'DiskReadBytesPersec',
                  'DiskReadsPersec', 'DiskTransfersPersec',
                  'DiskWriteBytesPersec', 'DiskWritesPersec',
                  'PercentDiskReadTime', 'PercentDiskTime',
                  'PercentDiskWriteTime', 'RecordTime',)


class MemoryMonitorSerializer(serializers.ModelSerializer):
    MemoryInstances_list = serializers.HyperlinkedIdentityField(
        view_name='memorymonitorinstances_list')
    CommitLimit = serializers.IntegerField()

    def get_validation_exclusions(self):
        exclusions = super(MemoryMonitorSerializer, self).get_validation_exclusions()
        return exclusions + ['agent']

    class Meta:
        model = MemoryMonitor


class MemoryInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryInstance
        fields = ('AvailableBytes', 'CacheBytes',
                  'CacheBytesPeak', 'CommittedBytes',
                  'PoolNonpagedAllocs', 'PoolNonpagedBytes',
                  'PoolPagedAllocs', 'PoolPagedBytes',
                  'PoolPagedResidentBytes', 'RecordTime',)


class NetworkMonitorSerializer(serializers.ModelSerializer):
    NetworkInstances_list = serializers.HyperlinkedIdentityField(
        view_name='networkmonitorinstances_list')
    Name = serializers.CharField()

    def get_validation_exclusions(self):
        exclusions = super(NetworkMonitorSerializer, self).get_validation_exclusions()
        return exclusions + ['agent']

    class Meta:
        model = NetworkMonitor


class NetworkInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkInstance
        fields = ('CurrentBandwidth', 'BytesReceivedPersec',
                  'BytesSentPersec', 'BytesTotalPersec',
                  'PacketsPersec', 'PacketsSentPersec',
                  'PacketsReceivedPersec', 'RecordTime',)


class PhysicalMemoryMonitorSerializer(serializers.ModelSerializer):
    BankLabel = serializers.CharField()
    Capacity = serializers.CharField()
    DataWidth = serializers.CharField()
    DeviceLocator = serializers.CharField()
    HotSwappable = serializers.CharField()
    Manufacturer = serializers.CharField()
    SerialNumber = serializers.CharField()
    Speed = serializers.CharField()
    PartNumber = serializers.CharField()

    def get_validation_exclusions(self):
        exclusions = super(PhysicalMemoryMonitorSerializer, self).get_validation_exclusions()
        return exclusions + ['agent']

    class Meta:
        model = PhysicalMemoryMonitor


class ProcessorMonitorSerializer(serializers.ModelSerializer):
    CPUInstances_list = serializers.HyperlinkedIdentityField(
        view_name='processormonitorinstances_list')

    AddressWidth = serializers.CharField()
    Architecture = serializers.CharField()
    AssetTag = serializers.CharField()
    Availability = serializers.CharField()
    Caption = serializers.CharField()
    DataWidth = serializers.CharField()
    Family = serializers.CharField()
    L2CacheSize = serializers.CharField()
    L3CacheSize = serializers.CharField()
    Manufacturer = serializers.CharField()
    Name = serializers.CharField()
    NumberOfCores = serializers.CharField()
    NumberOfLogicalProcessors = serializers.CharField()
    PartNumber = serializers.CharField()
    ProcessorId = serializers.CharField()
    ProcessorType = serializers.CharField()
    Revision = serializers.CharField()
    Status = serializers.CharField()
    SocketDesignation = serializers.CharField()

    def get_validation_exclusions(self):
        exclusions = super(ProcessorMonitorSerializer, self).get_validation_exclusions()
        return exclusions + ['agent']

    class Meta:
        model = ProcessorMonitor


class ProcessorInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessorInstance
        fields = ('CurrentClockSpeed', 'ExtClock',
                  'LoadPercentage', 'MaxClockSpeed',
                  'RecordTime',)
