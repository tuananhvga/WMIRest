from django.conf.urls import url, include
from . import views
from . import push_record

agent_urls = [
    url(r'^$', views.AgentList.as_view(), name='agent-list'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/$', views.AgentList.as_view(),
        name='agent-detail'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/cpumonitors$', views.AgentCPUMonitorList.as_view(),
        name='agent-cpumonitor-list'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/diskmonitors$', views.AgentDiskMonitorList.as_view(),
        name='agent-diskmonitor_list'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/memorymonitors$', views.AgentMemoryMonitorList.as_view(),
        name='agent-memorymonitors_list'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/networkmonitors$', views.AgentNetworkMonitorList.as_view(),
        name='agent-networkmonitors_list'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/physicalmemorymonitors$', views.AgentPhysicalMemoryMonitorList.as_view(),
        name='agent-physicalmonitors_list'),
    url(r'^(?P<uniqueID>[0-9A-Za-z]+)/processormonitors$', views.AgentProcessorMonitorList.as_view(),
        name='agent-processormonitors_list'),
]

cpumonitors_urls = [
    url(r'^(?P<pk>[0-9]+)/cpuinstances/$', views.CPUMonitorInstanceList.as_view(), name='cpumonitorinstances_list'),
]

diskmonitors_urls = [
    url(r'^(?P<pk>[0-9]+)/diskinstances/$', views.DiskMonitorInstanceList.as_view(), name='diskmonitorinstances_list'),
]

memorymonitors_urls = [
    url(r'^(?P<pk>[0-9]+)/memoryinstances/$', views.MemoryMonitorInstanceList.as_view(),
        name='memorymonitorinstances_list'),
]

networkmonitors_urls = [
    url(r'^(?P<pk>[0-9]+)/networkinstances/$', views.NetworkMonitorInstanceList.as_view(),
        name='networkmonitorinstances_list')
]

physicalmemorymonitors_url = [

]

processormonitors_url = [
    url(r'^(?P<pk>[0-9]+)/processorinstances/$', views.ProcessorMonitorInstanceList.as_view(),
        name='processormonitorinstances_list')
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cpumonitors/', include(cpumonitors_urls)),
    url(r'^diskmonitors/', include(diskmonitors_urls)),
    url(r'^memorymonitors/', include(memorymonitors_urls)),
    url(r'^networkmonitors/', include(networkmonitors_urls)),
    url(r'^processormonitors/', include(processormonitors_url)),
    url(r'^agents/', include(agent_urls)),
    url(r'^pushrecords/', push_record.push_records, name='push-record-view')
]
