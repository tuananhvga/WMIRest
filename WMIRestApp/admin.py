from django.contrib import admin
from .models import *


# Register your models here.
class CPUMonitorsInline(admin.StackedInline):
    model = CPUMonitor
    extra = 1


class DiskMonitorsInline(admin.StackedInline):
    model = DiskMonitor
    extra = 1


class MemoryMonitorsInline(admin.StackedInline):
    model = MemoryMonitor
    extra = 1


class NetworkMonitorsInline(admin.StackedInline):
    model = NetworkMonitor
    extra = 1


class PhysicalMemoryMonitorsInline(admin.StackedInline):
    model = PhysicalMemoryMonitor
    extra = 1


class ProcessorMonitorsInline(admin.StackedInline):
    model = ProcessorMonitor
    extra = 1


class CPUInstancesInline(admin.StackedInline):
    model = CPUInstance
    extra = 1


class DiskInstancesInline(admin.StackedInline):
    model = DiskInstance
    extra = 1


class MemoryInstancesInline(admin.StackedInline):
    model = MemoryInstance
    extra = 1


class NetworkInstancesInline(admin.StackedInline):
    model = NetworkInstance
    extra = 1


class ProcessorInstancesInline(admin.StackedInline):
    model = ProcessorInstance
    extra = 1


class AgentAdmin(admin.ModelAdmin):
    fields = ['uniqueID']
    inlines = [CPUMonitorsInline, DiskMonitorsInline,
               MemoryMonitorsInline, NetworkMonitorsInline,
               ProcessorMonitorsInline, PhysicalMemoryMonitorsInline]


class CPUMonitorAdmin(admin.ModelAdmin):
    fields = ['Name']
    inlines = [CPUInstancesInline]


class DiskMonitorAdmin(admin.ModelAdmin):
    fields = ['Name']
    inlines = [DiskInstancesInline]


class MemoryMonitorAdmin(admin.ModelAdmin):
    fields = ['CommitLimit']
    inlines = [MemoryInstancesInline]


class NetworkMonitorAdmin(admin.ModelAdmin):
    fields = ['Name']
    inlines = [NetworkInstancesInline]


class PhysicalMemoryMonitorAdmin(admin.ModelAdmin):
    fields = ['BankLabel', 'Capacity', 'DataWidth',
              'DeviceLocator', 'HotSwappable', 'Manufacturer',
              'SerialNumber', 'Speed', 'PartNumber', ]


class ProcessorMonitorAdmin(admin.ModelAdmin):
    fields = ['AddressWidth', 'Architecture', 'AssetTag',
              'Availability', 'Caption', 'DataWidth',
              'Family', 'L2CacheSize', 'L3CacheSize',
              'Manufacturer', 'Name', 'NumberOfCores',
              'NumberOfLogicalProcessors', 'PartNumber',
              'ProcessorId', 'ProcessorType', 'Revision',
              'Status', 'SocketDesignation',
              ]
    inlines = [ProcessorInstancesInline]


admin.site.register(Agent, AgentAdmin)
admin.site.register(CPUMonitor, CPUMonitorAdmin)
admin.site.register(DiskMonitor, DiskMonitorAdmin)
admin.site.register(NetworkMonitor, NetworkMonitorAdmin)
admin.site.register(PhysicalMemoryMonitor, PhysicalMemoryMonitorAdmin)
admin.site.register(ProcessorMonitor, ProcessorMonitorAdmin)
