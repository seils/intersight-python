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


class FirmwareRunningFirmware(object):
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
        'component': 'str',
        'management_controller': 'MoMoRef',
        'network_elements': 'list[MoMoRef]',
        'package_version': 'str',
        'registered_device': 'MoMoRef',
        'storage_controller': 'MoMoRef',
        'type': 'str',
        'version': 'str'
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
        'component': 'Component',
        'management_controller': 'ManagementController',
        'network_elements': 'NetworkElements',
        'package_version': 'PackageVersion',
        'registered_device': 'RegisteredDevice',
        'storage_controller': 'StorageController',
        'type': 'Type',
        'version': 'Version'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, device_mo_id=None, dn=None, rn=None, component=None, management_controller=None, network_elements=None, package_version=None, registered_device=None, storage_controller=None, type=None, version=None):
        """
        FirmwareRunningFirmware - a model defined in Swagger
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
        self._component = None
        self._management_controller = None
        self._network_elements = None
        self._package_version = None
        self._registered_device = None
        self._storage_controller = None
        self._type = None
        self._version = None

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
        if component is not None:
          self.component = component
        if management_controller is not None:
          self.management_controller = management_controller
        if network_elements is not None:
          self.network_elements = network_elements
        if package_version is not None:
          self.package_version = package_version
        if registered_device is not None:
          self.registered_device = registered_device
        if storage_controller is not None:
          self.storage_controller = storage_controller
        if type is not None:
          self.type = type
        if version is not None:
          self.version = version

    @property
    def account_moid(self):
        """
        Gets the account_moid of this FirmwareRunningFirmware.
        The Account ID for this managed object.  

        :return: The account_moid of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this FirmwareRunningFirmware.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this FirmwareRunningFirmware.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this FirmwareRunningFirmware.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this FirmwareRunningFirmware.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this FirmwareRunningFirmware.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this FirmwareRunningFirmware.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this FirmwareRunningFirmware.
        The time when this managed object was created.  

        :return: The create_time of this FirmwareRunningFirmware.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this FirmwareRunningFirmware.
        The time when this managed object was created.  

        :param create_time: The create_time of this FirmwareRunningFirmware.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this FirmwareRunningFirmware.
        The time when this managed object was last modified.  

        :return: The mod_time of this FirmwareRunningFirmware.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this FirmwareRunningFirmware.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this FirmwareRunningFirmware.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this FirmwareRunningFirmware.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this FirmwareRunningFirmware.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this FirmwareRunningFirmware.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this FirmwareRunningFirmware.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this FirmwareRunningFirmware.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this FirmwareRunningFirmware.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this FirmwareRunningFirmware.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this FirmwareRunningFirmware.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this FirmwareRunningFirmware.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this FirmwareRunningFirmware.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this FirmwareRunningFirmware.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this FirmwareRunningFirmware.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this FirmwareRunningFirmware.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this FirmwareRunningFirmware.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this FirmwareRunningFirmware.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this FirmwareRunningFirmware.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this FirmwareRunningFirmware.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this FirmwareRunningFirmware.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this FirmwareRunningFirmware.
        A unique identifier of this Managed Object instance.  

        :return: The id of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FirmwareRunningFirmware.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this FirmwareRunningFirmware.
        :type: str
        """

        self._id = id

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this FirmwareRunningFirmware.

        :return: The device_mo_id of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this FirmwareRunningFirmware.

        :param device_mo_id: The device_mo_id of this FirmwareRunningFirmware.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this FirmwareRunningFirmware.

        :return: The dn of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this FirmwareRunningFirmware.

        :param dn: The dn of this FirmwareRunningFirmware.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this FirmwareRunningFirmware.

        :return: The rn of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this FirmwareRunningFirmware.

        :param rn: The rn of this FirmwareRunningFirmware.
        :type: str
        """

        self._rn = rn

    @property
    def component(self):
        """
        Gets the component of this FirmwareRunningFirmware.
        represents the kind of firmware - boot-booloader/system/kernel  

        :return: The component of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this FirmwareRunningFirmware.
        represents the kind of firmware - boot-booloader/system/kernel  

        :param component: The component of this FirmwareRunningFirmware.
        :type: str
        """

        self._component = component

    @property
    def management_controller(self):
        """
        Gets the management_controller of this FirmwareRunningFirmware.

        :return: The management_controller of this FirmwareRunningFirmware.
        :rtype: MoMoRef
        """
        return self._management_controller

    @management_controller.setter
    def management_controller(self, management_controller):
        """
        Sets the management_controller of this FirmwareRunningFirmware.

        :param management_controller: The management_controller of this FirmwareRunningFirmware.
        :type: MoMoRef
        """

        self._management_controller = management_controller

    @property
    def network_elements(self):
        """
        Gets the network_elements of this FirmwareRunningFirmware.

        :return: The network_elements of this FirmwareRunningFirmware.
        :rtype: list[MoMoRef]
        """
        return self._network_elements

    @network_elements.setter
    def network_elements(self, network_elements):
        """
        Sets the network_elements of this FirmwareRunningFirmware.

        :param network_elements: The network_elements of this FirmwareRunningFirmware.
        :type: list[MoMoRef]
        """

        self._network_elements = network_elements

    @property
    def package_version(self):
        """
        Gets the package_version of this FirmwareRunningFirmware.
        represents the packageVersion to which the firmware belongs to  

        :return: The package_version of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """
        Sets the package_version of this FirmwareRunningFirmware.
        represents the packageVersion to which the firmware belongs to  

        :param package_version: The package_version of this FirmwareRunningFirmware.
        :type: str
        """

        self._package_version = package_version

    @property
    def registered_device(self):
        """
        Gets the registered_device of this FirmwareRunningFirmware.

        :return: The registered_device of this FirmwareRunningFirmware.
        :rtype: MoMoRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this FirmwareRunningFirmware.

        :param registered_device: The registered_device of this FirmwareRunningFirmware.
        :type: MoMoRef
        """

        self._registered_device = registered_device

    @property
    def storage_controller(self):
        """
        Gets the storage_controller of this FirmwareRunningFirmware.

        :return: The storage_controller of this FirmwareRunningFirmware.
        :rtype: MoMoRef
        """
        return self._storage_controller

    @storage_controller.setter
    def storage_controller(self, storage_controller):
        """
        Sets the storage_controller of this FirmwareRunningFirmware.

        :param storage_controller: The storage_controller of this FirmwareRunningFirmware.
        :type: MoMoRef
        """

        self._storage_controller = storage_controller

    @property
    def type(self):
        """
        Gets the type of this FirmwareRunningFirmware.

        :return: The type of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FirmwareRunningFirmware.

        :param type: The type of this FirmwareRunningFirmware.
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """
        Gets the version of this FirmwareRunningFirmware.
        represents the version of the firmware   

        :return: The version of this FirmwareRunningFirmware.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FirmwareRunningFirmware.
        represents the version of the firmware   

        :param version: The version of this FirmwareRunningFirmware.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, FirmwareRunningFirmware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other