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


class FirmwareUpgrade(object):
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
        'device': 'MoMoRef',
        'direct_download': 'FirmwareDirectDownload',
        'distributable': 'MoMoRef',
        'network_share': 'FirmwareNetworkShare',
        'server': 'MoMoRef',
        'upgrade_status': 'MoMoRef',
        'upgrade_type': 'str'
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
        'device': 'Device',
        'direct_download': 'DirectDownload',
        'distributable': 'Distributable',
        'network_share': 'NetworkShare',
        'server': 'Server',
        'upgrade_status': 'UpgradeStatus',
        'upgrade_type': 'UpgradeType'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, device=None, direct_download=None, distributable=None, network_share=None, server=None, upgrade_status=None, upgrade_type='direct_upgrade'):
        """
        FirmwareUpgrade - a model defined in Swagger
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
        self._device = None
        self._direct_download = None
        self._distributable = None
        self._network_share = None
        self._server = None
        self._upgrade_status = None
        self._upgrade_type = None

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
        if device is not None:
          self.device = device
        if direct_download is not None:
          self.direct_download = direct_download
        if distributable is not None:
          self.distributable = distributable
        if network_share is not None:
          self.network_share = network_share
        if server is not None:
          self.server = server
        if upgrade_status is not None:
          self.upgrade_status = upgrade_status
        if upgrade_type is not None:
          self.upgrade_type = upgrade_type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this FirmwareUpgrade.
        The Account ID for this managed object.  

        :return: The account_moid of this FirmwareUpgrade.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this FirmwareUpgrade.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this FirmwareUpgrade.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this FirmwareUpgrade.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this FirmwareUpgrade.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this FirmwareUpgrade.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this FirmwareUpgrade.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this FirmwareUpgrade.
        The time when this managed object was created.  

        :return: The create_time of this FirmwareUpgrade.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this FirmwareUpgrade.
        The time when this managed object was created.  

        :param create_time: The create_time of this FirmwareUpgrade.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this FirmwareUpgrade.
        The time when this managed object was last modified.  

        :return: The mod_time of this FirmwareUpgrade.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this FirmwareUpgrade.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this FirmwareUpgrade.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this FirmwareUpgrade.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this FirmwareUpgrade.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this FirmwareUpgrade.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this FirmwareUpgrade.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this FirmwareUpgrade.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this FirmwareUpgrade.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this FirmwareUpgrade.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this FirmwareUpgrade.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this FirmwareUpgrade.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this FirmwareUpgrade.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this FirmwareUpgrade.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this FirmwareUpgrade.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this FirmwareUpgrade.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this FirmwareUpgrade.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this FirmwareUpgrade.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this FirmwareUpgrade.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this FirmwareUpgrade.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this FirmwareUpgrade.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this FirmwareUpgrade.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this FirmwareUpgrade.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this FirmwareUpgrade.
        A unique identifier of this Managed Object instance.  

        :return: The id of this FirmwareUpgrade.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FirmwareUpgrade.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this FirmwareUpgrade.
        :type: str
        """

        self._id = id

    @property
    def device(self):
        """
        Gets the device of this FirmwareUpgrade.

        :return: The device of this FirmwareUpgrade.
        :rtype: MoMoRef
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this FirmwareUpgrade.

        :param device: The device of this FirmwareUpgrade.
        :type: MoMoRef
        """

        self._device = device

    @property
    def direct_download(self):
        """
        Gets the direct_download of this FirmwareUpgrade.
        Customer can upgrade the setup using the image directly from Cisco.com.  

        :return: The direct_download of this FirmwareUpgrade.
        :rtype: FirmwareDirectDownload
        """
        return self._direct_download

    @direct_download.setter
    def direct_download(self, direct_download):
        """
        Sets the direct_download of this FirmwareUpgrade.
        Customer can upgrade the setup using the image directly from Cisco.com.  

        :param direct_download: The direct_download of this FirmwareUpgrade.
        :type: FirmwareDirectDownload
        """

        self._direct_download = direct_download

    @property
    def distributable(self):
        """
        Gets the distributable of this FirmwareUpgrade.

        :return: The distributable of this FirmwareUpgrade.
        :rtype: MoMoRef
        """
        return self._distributable

    @distributable.setter
    def distributable(self, distributable):
        """
        Sets the distributable of this FirmwareUpgrade.

        :param distributable: The distributable of this FirmwareUpgrade.
        :type: MoMoRef
        """

        self._distributable = distributable

    @property
    def network_share(self):
        """
        Gets the network_share of this FirmwareUpgrade.
        Customer can upgrade the setup using the already downloaded image in customer's network.  

        :return: The network_share of this FirmwareUpgrade.
        :rtype: FirmwareNetworkShare
        """
        return self._network_share

    @network_share.setter
    def network_share(self, network_share):
        """
        Sets the network_share of this FirmwareUpgrade.
        Customer can upgrade the setup using the already downloaded image in customer's network.  

        :param network_share: The network_share of this FirmwareUpgrade.
        :type: FirmwareNetworkShare
        """

        self._network_share = network_share

    @property
    def server(self):
        """
        Gets the server of this FirmwareUpgrade.

        :return: The server of this FirmwareUpgrade.
        :rtype: MoMoRef
        """
        return self._server

    @server.setter
    def server(self, server):
        """
        Sets the server of this FirmwareUpgrade.

        :param server: The server of this FirmwareUpgrade.
        :type: MoMoRef
        """

        self._server = server

    @property
    def upgrade_status(self):
        """
        Gets the upgrade_status of this FirmwareUpgrade.

        :return: The upgrade_status of this FirmwareUpgrade.
        :rtype: MoMoRef
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """
        Sets the upgrade_status of this FirmwareUpgrade.

        :param upgrade_status: The upgrade_status of this FirmwareUpgrade.
        :type: MoMoRef
        """

        self._upgrade_status = upgrade_status

    @property
    def upgrade_type(self):
        """
        Gets the upgrade_type of this FirmwareUpgrade.
        User can upgrade a server in two ways. Either can have the image locally in customer network itself and upgrade. Or can upgrade against the image directly from cisco.com.   

        :return: The upgrade_type of this FirmwareUpgrade.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """
        Sets the upgrade_type of this FirmwareUpgrade.
        User can upgrade a server in two ways. Either can have the image locally in customer network itself and upgrade. Or can upgrade against the image directly from cisco.com.   

        :param upgrade_type: The upgrade_type of this FirmwareUpgrade.
        :type: str
        """
        allowed_values = ["direct_upgrade", "network_upgrade"]
        if upgrade_type not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_type` ({0}), must be one of {1}"
                .format(upgrade_type, allowed_values)
            )

        self._upgrade_type = upgrade_type

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
        if not isinstance(other, FirmwareUpgrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
