# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ComputeRackUnit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_moid': 'str',
        'ancestors': 'list[MoMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoMoRef',
        'tags': 'list[MoTag]',
        'id': 'str',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'admin_power_state': 'str',
        'available_memory': 'int',
        'fault_summary': 'int',
        'kvm_ip_addresses': 'list[ComputeIpAddress]',
        'memory_speed': 'str',
        'num_adaptors': 'int',
        'num_cpu_cores': 'int',
        'num_cpu_cores_enabled': 'int',
        'num_cpus': 'int',
        'num_eth_host_interfaces': 'int',
        'num_fc_host_interfaces': 'int',
        'num_threads': 'int',
        'oper_power_state': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'platform_type': 'str',
        'presence': 'str',
        'service_profile': 'str',
        'total_memory': 'int',
        'uuid': 'str',
        'adapters': 'list[MoMoRef]',
        'bmc': 'MoMoRef',
        'board': 'MoMoRef',
        'fanmodules': 'list[MoMoRef]',
        'generic_inventory_holders': 'list[MoMoRef]',
        'locator_led': 'MoMoRef',
        'psus': 'list[MoMoRef]',
        'registered_device': 'MoMoRef',
        'server_id': 'int',
        'top_system': 'MoMoRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'id': 'Id',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'admin_power_state': 'AdminPowerState',
        'available_memory': 'AvailableMemory',
        'fault_summary': 'FaultSummary',
        'kvm_ip_addresses': 'KvmIpAddresses',
        'memory_speed': 'MemorySpeed',
        'num_adaptors': 'NumAdaptors',
        'num_cpu_cores': 'NumCpuCores',
        'num_cpu_cores_enabled': 'NumCpuCoresEnabled',
        'num_cpus': 'NumCpus',
        'num_eth_host_interfaces': 'NumEthHostInterfaces',
        'num_fc_host_interfaces': 'NumFcHostInterfaces',
        'num_threads': 'NumThreads',
        'oper_power_state': 'OperPowerState',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'platform_type': 'PlatformType',
        'presence': 'Presence',
        'service_profile': 'ServiceProfile',
        'total_memory': 'TotalMemory',
        'uuid': 'Uuid',
        'adapters': 'Adapters',
        'bmc': 'Bmc',
        'board': 'Board',
        'fanmodules': 'Fanmodules',
        'generic_inventory_holders': 'GenericInventoryHolders',
        'locator_led': 'LocatorLed',
        'psus': 'Psus',
        'registered_device': 'RegisteredDevice',
        'server_id': 'ServerId',
        'top_system': 'TopSystem'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, admin_power_state=None, available_memory=None, fault_summary=None, kvm_ip_addresses=None, memory_speed=None, num_adaptors=None, num_cpu_cores=None, num_cpu_cores_enabled=None, num_cpus=None, num_eth_host_interfaces=None, num_fc_host_interfaces=None, num_threads=None, oper_power_state=None, oper_state=None, operability=None, platform_type=None, presence=None, service_profile=None, total_memory=None, uuid=None, adapters=None, bmc=None, board=None, fanmodules=None, generic_inventory_holders=None, locator_led=None, psus=None, registered_device=None, server_id=None, top_system=None):
        """
        ComputeRackUnit - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._id = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._admin_power_state = None
        self._available_memory = None
        self._fault_summary = None
        self._kvm_ip_addresses = None
        self._memory_speed = None
        self._num_adaptors = None
        self._num_cpu_cores = None
        self._num_cpu_cores_enabled = None
        self._num_cpus = None
        self._num_eth_host_interfaces = None
        self._num_fc_host_interfaces = None
        self._num_threads = None
        self._oper_power_state = None
        self._oper_state = None
        self._operability = None
        self._platform_type = None
        self._presence = None
        self._service_profile = None
        self._total_memory = None
        self._uuid = None
        self._adapters = None
        self._bmc = None
        self._board = None
        self._fanmodules = None
        self._generic_inventory_holders = None
        self._locator_led = None
        self._psus = None
        self._registered_device = None
        self._server_id = None
        self._top_system = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if id is not None:
          self.id = id
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if admin_power_state is not None:
          self.admin_power_state = admin_power_state
        if available_memory is not None:
          self.available_memory = available_memory
        if fault_summary is not None:
          self.fault_summary = fault_summary
        if kvm_ip_addresses is not None:
          self.kvm_ip_addresses = kvm_ip_addresses
        if memory_speed is not None:
          self.memory_speed = memory_speed
        if num_adaptors is not None:
          self.num_adaptors = num_adaptors
        if num_cpu_cores is not None:
          self.num_cpu_cores = num_cpu_cores
        if num_cpu_cores_enabled is not None:
          self.num_cpu_cores_enabled = num_cpu_cores_enabled
        if num_cpus is not None:
          self.num_cpus = num_cpus
        if num_eth_host_interfaces is not None:
          self.num_eth_host_interfaces = num_eth_host_interfaces
        if num_fc_host_interfaces is not None:
          self.num_fc_host_interfaces = num_fc_host_interfaces
        if num_threads is not None:
          self.num_threads = num_threads
        if oper_power_state is not None:
          self.oper_power_state = oper_power_state
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if platform_type is not None:
          self.platform_type = platform_type
        if presence is not None:
          self.presence = presence
        if service_profile is not None:
          self.service_profile = service_profile
        if total_memory is not None:
          self.total_memory = total_memory
        if uuid is not None:
          self.uuid = uuid
        if adapters is not None:
          self.adapters = adapters
        if bmc is not None:
          self.bmc = bmc
        if board is not None:
          self.board = board
        if fanmodules is not None:
          self.fanmodules = fanmodules
        if generic_inventory_holders is not None:
          self.generic_inventory_holders = generic_inventory_holders
        if locator_led is not None:
          self.locator_led = locator_led
        if psus is not None:
          self.psus = psus
        if registered_device is not None:
          self.registered_device = registered_device
        if server_id is not None:
          self.server_id = server_id
        if top_system is not None:
          self.top_system = top_system

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ComputeRackUnit.
        The Account ID for this managed object.  

        :return: The account_moid of this ComputeRackUnit.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ComputeRackUnit.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ComputeRackUnit.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ComputeRackUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ComputeRackUnit.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ComputeRackUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ComputeRackUnit.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ComputeRackUnit.
        The time when this managed object was created.  

        :return: The create_time of this ComputeRackUnit.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ComputeRackUnit.
        The time when this managed object was created.  

        :param create_time: The create_time of this ComputeRackUnit.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ComputeRackUnit.
        The time when this managed object was last modified.  

        :return: The mod_time of this ComputeRackUnit.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ComputeRackUnit.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ComputeRackUnit.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ComputeRackUnit.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this ComputeRackUnit.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ComputeRackUnit.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this ComputeRackUnit.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ComputeRackUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ComputeRackUnit.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ComputeRackUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ComputeRackUnit.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ComputeRackUnit.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this ComputeRackUnit.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ComputeRackUnit.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ComputeRackUnit.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ComputeRackUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ComputeRackUnit.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ComputeRackUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ComputeRackUnit.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this ComputeRackUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this ComputeRackUnit.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ComputeRackUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this ComputeRackUnit.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this ComputeRackUnit.
        A unique identifier of this Managed Object instance.  

        :return: The id of this ComputeRackUnit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ComputeRackUnit.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this ComputeRackUnit.
        :type: str
        """

        self._id = id

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this ComputeRackUnit.

        :return: The device_mo_id of this ComputeRackUnit.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this ComputeRackUnit.

        :param device_mo_id: The device_mo_id of this ComputeRackUnit.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this ComputeRackUnit.

        :return: The dn of this ComputeRackUnit.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ComputeRackUnit.

        :param dn: The dn of this ComputeRackUnit.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this ComputeRackUnit.

        :return: The rn of this ComputeRackUnit.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this ComputeRackUnit.

        :param rn: The rn of this ComputeRackUnit.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this ComputeRackUnit.

        :return: The model of this ComputeRackUnit.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this ComputeRackUnit.

        :param model: The model of this ComputeRackUnit.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this ComputeRackUnit.

        :return: The revision of this ComputeRackUnit.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ComputeRackUnit.

        :param revision: The revision of this ComputeRackUnit.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this ComputeRackUnit.

        :return: The serial of this ComputeRackUnit.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this ComputeRackUnit.

        :param serial: The serial of this ComputeRackUnit.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this ComputeRackUnit.

        :return: The vendor of this ComputeRackUnit.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this ComputeRackUnit.

        :param vendor: The vendor of this ComputeRackUnit.
        :type: str
        """

        self._vendor = vendor

    @property
    def admin_power_state(self):
        """
        Gets the admin_power_state of this ComputeRackUnit.

        :return: The admin_power_state of this ComputeRackUnit.
        :rtype: str
        """
        return self._admin_power_state

    @admin_power_state.setter
    def admin_power_state(self, admin_power_state):
        """
        Sets the admin_power_state of this ComputeRackUnit.

        :param admin_power_state: The admin_power_state of this ComputeRackUnit.
        :type: str
        """

        self._admin_power_state = admin_power_state

    @property
    def available_memory(self):
        """
        Gets the available_memory of this ComputeRackUnit.

        :return: The available_memory of this ComputeRackUnit.
        :rtype: int
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        """
        Sets the available_memory of this ComputeRackUnit.

        :param available_memory: The available_memory of this ComputeRackUnit.
        :type: int
        """

        self._available_memory = available_memory

    @property
    def fault_summary(self):
        """
        Gets the fault_summary of this ComputeRackUnit.

        :return: The fault_summary of this ComputeRackUnit.
        :rtype: int
        """
        return self._fault_summary

    @fault_summary.setter
    def fault_summary(self, fault_summary):
        """
        Sets the fault_summary of this ComputeRackUnit.

        :param fault_summary: The fault_summary of this ComputeRackUnit.
        :type: int
        """

        self._fault_summary = fault_summary

    @property
    def kvm_ip_addresses(self):
        """
        Gets the kvm_ip_addresses of this ComputeRackUnit.

        :return: The kvm_ip_addresses of this ComputeRackUnit.
        :rtype: list[ComputeIpAddress]
        """
        return self._kvm_ip_addresses

    @kvm_ip_addresses.setter
    def kvm_ip_addresses(self, kvm_ip_addresses):
        """
        Sets the kvm_ip_addresses of this ComputeRackUnit.

        :param kvm_ip_addresses: The kvm_ip_addresses of this ComputeRackUnit.
        :type: list[ComputeIpAddress]
        """

        self._kvm_ip_addresses = kvm_ip_addresses

    @property
    def memory_speed(self):
        """
        Gets the memory_speed of this ComputeRackUnit.

        :return: The memory_speed of this ComputeRackUnit.
        :rtype: str
        """
        return self._memory_speed

    @memory_speed.setter
    def memory_speed(self, memory_speed):
        """
        Sets the memory_speed of this ComputeRackUnit.

        :param memory_speed: The memory_speed of this ComputeRackUnit.
        :type: str
        """

        self._memory_speed = memory_speed

    @property
    def num_adaptors(self):
        """
        Gets the num_adaptors of this ComputeRackUnit.

        :return: The num_adaptors of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_adaptors

    @num_adaptors.setter
    def num_adaptors(self, num_adaptors):
        """
        Sets the num_adaptors of this ComputeRackUnit.

        :param num_adaptors: The num_adaptors of this ComputeRackUnit.
        :type: int
        """

        self._num_adaptors = num_adaptors

    @property
    def num_cpu_cores(self):
        """
        Gets the num_cpu_cores of this ComputeRackUnit.

        :return: The num_cpu_cores of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores):
        """
        Sets the num_cpu_cores of this ComputeRackUnit.

        :param num_cpu_cores: The num_cpu_cores of this ComputeRackUnit.
        :type: int
        """

        self._num_cpu_cores = num_cpu_cores

    @property
    def num_cpu_cores_enabled(self):
        """
        Gets the num_cpu_cores_enabled of this ComputeRackUnit.

        :return: The num_cpu_cores_enabled of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_cpu_cores_enabled

    @num_cpu_cores_enabled.setter
    def num_cpu_cores_enabled(self, num_cpu_cores_enabled):
        """
        Sets the num_cpu_cores_enabled of this ComputeRackUnit.

        :param num_cpu_cores_enabled: The num_cpu_cores_enabled of this ComputeRackUnit.
        :type: int
        """

        self._num_cpu_cores_enabled = num_cpu_cores_enabled

    @property
    def num_cpus(self):
        """
        Gets the num_cpus of this ComputeRackUnit.

        :return: The num_cpus of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        """
        Sets the num_cpus of this ComputeRackUnit.

        :param num_cpus: The num_cpus of this ComputeRackUnit.
        :type: int
        """

        self._num_cpus = num_cpus

    @property
    def num_eth_host_interfaces(self):
        """
        Gets the num_eth_host_interfaces of this ComputeRackUnit.

        :return: The num_eth_host_interfaces of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_eth_host_interfaces

    @num_eth_host_interfaces.setter
    def num_eth_host_interfaces(self, num_eth_host_interfaces):
        """
        Sets the num_eth_host_interfaces of this ComputeRackUnit.

        :param num_eth_host_interfaces: The num_eth_host_interfaces of this ComputeRackUnit.
        :type: int
        """

        self._num_eth_host_interfaces = num_eth_host_interfaces

    @property
    def num_fc_host_interfaces(self):
        """
        Gets the num_fc_host_interfaces of this ComputeRackUnit.

        :return: The num_fc_host_interfaces of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_fc_host_interfaces

    @num_fc_host_interfaces.setter
    def num_fc_host_interfaces(self, num_fc_host_interfaces):
        """
        Sets the num_fc_host_interfaces of this ComputeRackUnit.

        :param num_fc_host_interfaces: The num_fc_host_interfaces of this ComputeRackUnit.
        :type: int
        """

        self._num_fc_host_interfaces = num_fc_host_interfaces

    @property
    def num_threads(self):
        """
        Gets the num_threads of this ComputeRackUnit.

        :return: The num_threads of this ComputeRackUnit.
        :rtype: int
        """
        return self._num_threads

    @num_threads.setter
    def num_threads(self, num_threads):
        """
        Sets the num_threads of this ComputeRackUnit.

        :param num_threads: The num_threads of this ComputeRackUnit.
        :type: int
        """

        self._num_threads = num_threads

    @property
    def oper_power_state(self):
        """
        Gets the oper_power_state of this ComputeRackUnit.

        :return: The oper_power_state of this ComputeRackUnit.
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """
        Sets the oper_power_state of this ComputeRackUnit.

        :param oper_power_state: The oper_power_state of this ComputeRackUnit.
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def oper_state(self):
        """
        Gets the oper_state of this ComputeRackUnit.

        :return: The oper_state of this ComputeRackUnit.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this ComputeRackUnit.

        :param oper_state: The oper_state of this ComputeRackUnit.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this ComputeRackUnit.

        :return: The operability of this ComputeRackUnit.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this ComputeRackUnit.

        :param operability: The operability of this ComputeRackUnit.
        :type: str
        """

        self._operability = operability

    @property
    def platform_type(self):
        """
        Gets the platform_type of this ComputeRackUnit.

        :return: The platform_type of this ComputeRackUnit.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this ComputeRackUnit.

        :param platform_type: The platform_type of this ComputeRackUnit.
        :type: str
        """

        self._platform_type = platform_type

    @property
    def presence(self):
        """
        Gets the presence of this ComputeRackUnit.

        :return: The presence of this ComputeRackUnit.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this ComputeRackUnit.

        :param presence: The presence of this ComputeRackUnit.
        :type: str
        """

        self._presence = presence

    @property
    def service_profile(self):
        """
        Gets the service_profile of this ComputeRackUnit.

        :return: The service_profile of this ComputeRackUnit.
        :rtype: str
        """
        return self._service_profile

    @service_profile.setter
    def service_profile(self, service_profile):
        """
        Sets the service_profile of this ComputeRackUnit.

        :param service_profile: The service_profile of this ComputeRackUnit.
        :type: str
        """

        self._service_profile = service_profile

    @property
    def total_memory(self):
        """
        Gets the total_memory of this ComputeRackUnit.

        :return: The total_memory of this ComputeRackUnit.
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """
        Sets the total_memory of this ComputeRackUnit.

        :param total_memory: The total_memory of this ComputeRackUnit.
        :type: int
        """

        self._total_memory = total_memory

    @property
    def uuid(self):
        """
        Gets the uuid of this ComputeRackUnit.

        :return: The uuid of this ComputeRackUnit.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this ComputeRackUnit.

        :param uuid: The uuid of this ComputeRackUnit.
        :type: str
        """

        self._uuid = uuid

    @property
    def adapters(self):
        """
        Gets the adapters of this ComputeRackUnit.

        :return: The adapters of this ComputeRackUnit.
        :rtype: list[MoMoRef]
        """
        return self._adapters

    @adapters.setter
    def adapters(self, adapters):
        """
        Sets the adapters of this ComputeRackUnit.

        :param adapters: The adapters of this ComputeRackUnit.
        :type: list[MoMoRef]
        """

        self._adapters = adapters

    @property
    def bmc(self):
        """
        Gets the bmc of this ComputeRackUnit.

        :return: The bmc of this ComputeRackUnit.
        :rtype: MoMoRef
        """
        return self._bmc

    @bmc.setter
    def bmc(self, bmc):
        """
        Sets the bmc of this ComputeRackUnit.

        :param bmc: The bmc of this ComputeRackUnit.
        :type: MoMoRef
        """

        self._bmc = bmc

    @property
    def board(self):
        """
        Gets the board of this ComputeRackUnit.

        :return: The board of this ComputeRackUnit.
        :rtype: MoMoRef
        """
        return self._board

    @board.setter
    def board(self, board):
        """
        Sets the board of this ComputeRackUnit.

        :param board: The board of this ComputeRackUnit.
        :type: MoMoRef
        """

        self._board = board

    @property
    def fanmodules(self):
        """
        Gets the fanmodules of this ComputeRackUnit.

        :return: The fanmodules of this ComputeRackUnit.
        :rtype: list[MoMoRef]
        """
        return self._fanmodules

    @fanmodules.setter
    def fanmodules(self, fanmodules):
        """
        Sets the fanmodules of this ComputeRackUnit.

        :param fanmodules: The fanmodules of this ComputeRackUnit.
        :type: list[MoMoRef]
        """

        self._fanmodules = fanmodules

    @property
    def generic_inventory_holders(self):
        """
        Gets the generic_inventory_holders of this ComputeRackUnit.

        :return: The generic_inventory_holders of this ComputeRackUnit.
        :rtype: list[MoMoRef]
        """
        return self._generic_inventory_holders

    @generic_inventory_holders.setter
    def generic_inventory_holders(self, generic_inventory_holders):
        """
        Sets the generic_inventory_holders of this ComputeRackUnit.

        :param generic_inventory_holders: The generic_inventory_holders of this ComputeRackUnit.
        :type: list[MoMoRef]
        """

        self._generic_inventory_holders = generic_inventory_holders

    @property
    def locator_led(self):
        """
        Gets the locator_led of this ComputeRackUnit.

        :return: The locator_led of this ComputeRackUnit.
        :rtype: MoMoRef
        """
        return self._locator_led

    @locator_led.setter
    def locator_led(self, locator_led):
        """
        Sets the locator_led of this ComputeRackUnit.

        :param locator_led: The locator_led of this ComputeRackUnit.
        :type: MoMoRef
        """

        self._locator_led = locator_led

    @property
    def psus(self):
        """
        Gets the psus of this ComputeRackUnit.

        :return: The psus of this ComputeRackUnit.
        :rtype: list[MoMoRef]
        """
        return self._psus

    @psus.setter
    def psus(self, psus):
        """
        Sets the psus of this ComputeRackUnit.

        :param psus: The psus of this ComputeRackUnit.
        :type: list[MoMoRef]
        """

        self._psus = psus

    @property
    def registered_device(self):
        """
        Gets the registered_device of this ComputeRackUnit.

        :return: The registered_device of this ComputeRackUnit.
        :rtype: MoMoRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this ComputeRackUnit.

        :param registered_device: The registered_device of this ComputeRackUnit.
        :type: MoMoRef
        """

        self._registered_device = registered_device

    @property
    def server_id(self):
        """
        Gets the server_id of this ComputeRackUnit.

        :return: The server_id of this ComputeRackUnit.
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """
        Sets the server_id of this ComputeRackUnit.

        :param server_id: The server_id of this ComputeRackUnit.
        :type: int
        """

        self._server_id = server_id

    @property
    def top_system(self):
        """
        Gets the top_system of this ComputeRackUnit.

        :return: The top_system of this ComputeRackUnit.
        :rtype: MoMoRef
        """
        return self._top_system

    @top_system.setter
    def top_system(self, top_system):
        """
        Sets the top_system of this ComputeRackUnit.

        :param top_system: The top_system of this ComputeRackUnit.
        :type: MoMoRef
        """

        self._top_system = top_system

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ComputeRackUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
