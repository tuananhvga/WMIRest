from django.db import models


# Create your models here.


# Agent
class Agent(models.Model):
    uniqueID = models.CharField(max_length=300)

    def __str__(self):
        return self.uniqueID


# CPU Monitor
class CPUMonitor(models.Model):
    agent = models.ForeignKey(Agent, related_name='CPUMonitors')
    Name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('agent', 'Name')
        ordering = ['agent', 'Name']

    def __str__(self):
        return self.Name


# Disk Monitor
class DiskMonitor(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='DiskMonitors')
    Name = models.CharField(max_length=30)

    class Meta:
        unique_together = ('agent', 'Name')

    def __str__(self):
        return self.Name


# Memory Monitor
class MemoryMonitor(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='MemoryMonitors')
    CommitLimit = models.BigIntegerField()

    class Meta:
        unique_together = ('agent', 'CommitLimit')

    def __str__(self):
        return str(self.CommitLimit)


# Network Monitor
class NetworkMonitor(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='NetworkMonitors')
    Name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('agent', 'Name')

    def __str__(self):
        return self.Name


# Physical Memory Monitor (no instance)
class PhysicalMemoryMonitor(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='PhysicalMonitors')
    BankLabel = models.CharField(max_length=50)
    Capacity = models.CharField(max_length=50)
    DataWidth = models.CharField(max_length=50)
    DeviceLocator = models.CharField(max_length=50)
    HotSwappable = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=50)
    SerialNumber = models.CharField(max_length=50)
    Speed = models.CharField(max_length=50)
    PartNumber = models.CharField(max_length=50)

    class Meta:
        unique_together = ('agent', 'PartNumber', 'SerialNumber')

    def __str__(self):
        return self.PartNumber


# Processor Monitor
class ProcessorMonitor(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='ProcessorMonitors')
    AddressWidth = models.CharField(max_length=50)
    Architecture = models.CharField(max_length=50)
    AssetTag = models.CharField(max_length=50)
    Availability = models.CharField(max_length=50)
    Caption = models.CharField(max_length=50)
    DataWidth = models.CharField(max_length=50)
    Family = models.CharField(max_length=50)
    L2CacheSize = models.CharField(max_length=50)
    L3CacheSize = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    NumberOfCores = models.CharField(max_length=50)
    NumberOfLogicalProcessors = models.CharField(max_length=50)
    PartNumber = models.CharField(max_length=50)
    ProcessorId = models.CharField(max_length=50)
    ProcessorType = models.CharField(max_length=50)
    Revision = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    SocketDesignation = models.CharField(max_length=50)

    class Meta:
        unique_together = ('agent', 'ProcessorId')

    def __str__(self):
        return self.Name


# CPU Instance
class CPUInstance(models.Model):
    monitor = models.ForeignKey(CPUMonitor, on_delete=models.CASCADE, related_name='CPUInstances')
    InterruptsPersec = models.BigIntegerField()
    PercentIdleTime = models.IntegerField()
    PercentInterruptTime = models.IntegerField()
    PercentPrivilegedTime = models.IntegerField()
    PercentProcessorTime = models.IntegerField()
    PercentUserTime = models.IntegerField()
    RecordTime = models.DateTimeField()


# Disk instance
class DiskInstance(models.Model):
    monitor = models.ForeignKey(DiskMonitor, on_delete=models.CASCADE, related_name='DiskInstances')
    DiskBytesPersec = models.BigIntegerField()
    DiskReadBytesPersec = models.BigIntegerField()
    DiskReadsPersec = models.BigIntegerField()
    DiskTransfersPersec = models.BigIntegerField()
    DiskWriteBytesPersec = models.BigIntegerField()
    DiskWritesPersec = models.BigIntegerField()
    PercentDiskReadTime = models.BigIntegerField()
    PercentDiskTime = models.BigIntegerField()
    PercentDiskWriteTime = models.BigIntegerField()
    RecordTime = models.DateTimeField()


# Memory Instance
class MemoryInstance(models.Model):
    monitor = models.ForeignKey(MemoryMonitor, on_delete=models.CASCADE, related_name='MemoryInstances')
    AvailableBytes = models.BigIntegerField()
    CacheBytes = models.BigIntegerField()
    CacheBytesPeak = models.BigIntegerField()
    CommittedBytes = models.BigIntegerField()
    PoolNonpagedAllocs = models.BigIntegerField()
    PoolNonpagedBytes = models.BigIntegerField()
    PoolPagedAllocs = models.BigIntegerField()
    PoolPagedBytes = models.BigIntegerField()
    PoolPagedResidentBytes = models.BigIntegerField()
    RecordTime = models.DateTimeField()


# Network Instance
class NetworkInstance(models.Model):
    monitor = models.ForeignKey(NetworkMonitor, on_delete=models.CASCADE, related_name='NetworkInstances')
    CurrentBandwidth = models.BigIntegerField()
    BytesReceivedPersec = models.BigIntegerField()
    BytesSentPersec = models.BigIntegerField()
    BytesTotalPersec = models.BigIntegerField()
    PacketsPersec = models.BigIntegerField()
    PacketsSentPersec = models.BigIntegerField()
    PacketsReceivedPersec = models.BigIntegerField()
    RecordTime = models.DateTimeField()


# Processor Instance
class ProcessorInstance(models.Model):
    monitor = models.ForeignKey(ProcessorMonitor, on_delete=models.CASCADE, related_name='ProcessorInstances')
    CurrentClockSpeed = models.BigIntegerField()
    ExtClock = models.BigIntegerField()
    LoadPercentage = models.BigIntegerField()
    MaxClockSpeed = models.BigIntegerField()
    RecordTime = models.DateTimeField()
