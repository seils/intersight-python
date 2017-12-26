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


class StorageVdMemberEp(object):
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
        'oper_qualifier_reason': 'str',
        'presence': 'str',
        'registered_device': 'MoMoRef',
        'role': 'str',
        'span_id': 'str',
        'storage_virtual_drive': 'MoMoRef',
        'vd_member_ep_id': 'int'
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
        'oper_qualifier_reason': 'OperQualifierReason',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'role': 'Role',
        'span_id': 'SpanId',
        'storage_virtual_drive': 'StorageVirtualDrive',
        'vd_member_ep_id': 'VdMemberEpId'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, device_mo_id=None, dn=None, rn=None, oper_qualifier_reason=None, presence=None, registered_device=None, role=None, span_id=None, storage_virtual_drive=None, vd_member_ep_id=None):
        """
        StorageVdMemberEp - a model defined in Swagger
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
        self._oper_qualifier_reason = None
        self._presence = None
        self._registered_device = None
        self._role = None
        self._span_id = None
        self._storage_virtual_drive = None
        self._vd_member_ep_id = None

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
        if oper_qualifier_reason is not None:
          self.oper_qualifier_reason = oper_qualifier_reason
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if role is not None:
          self.role = role
        if span_id is not None:
          self.span_id = span_id
        if storage_virtual_drive is not None:
          self.storage_virtual_drive = storage_virtual_drive
        if vd_member_ep_id is not None:
          self.vd_member_ep_id = vd_member_ep_id

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageVdMemberEp.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageVdMemberEp.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageVdMemberEp.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageVdMemberEp.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageVdMemberEp.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageVdMemberEp.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageVdMemberEp.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageVdMemberEp.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageVdMemberEp.
        The time when this managed object was created.  

        :return: The create_time of this StorageVdMemberEp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageVdMemberEp.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageVdMemberEp.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageVdMemberEp.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageVdMemberEp.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageVdMemberEp.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageVdMemberEp.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageVdMemberEp.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this StorageVdMemberEp.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageVdMemberEp.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageVdMemberEp.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageVdMemberEp.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageVdMemberEp.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageVdMemberEp.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageVdMemberEp.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageVdMemberEp.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageVdMemberEp.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageVdMemberEp.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageVdMemberEp.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageVdMemberEp.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageVdMemberEp.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageVdMemberEp.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageVdMemberEp.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this StorageVdMemberEp.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StorageVdMemberEp.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageVdMemberEp.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StorageVdMemberEp.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this StorageVdMemberEp.
        A unique identifier of this Managed Object instance.  

        :return: The id of this StorageVdMemberEp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StorageVdMemberEp.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this StorageVdMemberEp.
        :type: str
        """

        self._id = id

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageVdMemberEp.

        :return: The device_mo_id of this StorageVdMemberEp.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageVdMemberEp.

        :param device_mo_id: The device_mo_id of this StorageVdMemberEp.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageVdMemberEp.

        :return: The dn of this StorageVdMemberEp.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageVdMemberEp.

        :param dn: The dn of this StorageVdMemberEp.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageVdMemberEp.

        :return: The rn of this StorageVdMemberEp.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageVdMemberEp.

        :param rn: The rn of this StorageVdMemberEp.
        :type: str
        """

        self._rn = rn

    @property
    def oper_qualifier_reason(self):
        """
        Gets the oper_qualifier_reason of this StorageVdMemberEp.

        :return: The oper_qualifier_reason of this StorageVdMemberEp.
        :rtype: str
        """
        return self._oper_qualifier_reason

    @oper_qualifier_reason.setter
    def oper_qualifier_reason(self, oper_qualifier_reason):
        """
        Sets the oper_qualifier_reason of this StorageVdMemberEp.

        :param oper_qualifier_reason: The oper_qualifier_reason of this StorageVdMemberEp.
        :type: str
        """

        self._oper_qualifier_reason = oper_qualifier_reason

    @property
    def presence(self):
        """
        Gets the presence of this StorageVdMemberEp.

        :return: The presence of this StorageVdMemberEp.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this StorageVdMemberEp.

        :param presence: The presence of this StorageVdMemberEp.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageVdMemberEp.

        :return: The registered_device of this StorageVdMemberEp.
        :rtype: MoMoRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageVdMemberEp.

        :param registered_device: The registered_device of this StorageVdMemberEp.
        :type: MoMoRef
        """

        self._registered_device = registered_device

    @property
    def role(self):
        """
        Gets the role of this StorageVdMemberEp.

        :return: The role of this StorageVdMemberEp.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this StorageVdMemberEp.

        :param role: The role of this StorageVdMemberEp.
        :type: str
        """

        self._role = role

    @property
    def span_id(self):
        """
        Gets the span_id of this StorageVdMemberEp.

        :return: The span_id of this StorageVdMemberEp.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        """
        Sets the span_id of this StorageVdMemberEp.

        :param span_id: The span_id of this StorageVdMemberEp.
        :type: str
        """

        self._span_id = span_id

    @property
    def storage_virtual_drive(self):
        """
        Gets the storage_virtual_drive of this StorageVdMemberEp.

        :return: The storage_virtual_drive of this StorageVdMemberEp.
        :rtype: MoMoRef
        """
        return self._storage_virtual_drive

    @storage_virtual_drive.setter
    def storage_virtual_drive(self, storage_virtual_drive):
        """
        Sets the storage_virtual_drive of this StorageVdMemberEp.

        :param storage_virtual_drive: The storage_virtual_drive of this StorageVdMemberEp.
        :type: MoMoRef
        """

        self._storage_virtual_drive = storage_virtual_drive

    @property
    def vd_member_ep_id(self):
        """
        Gets the vd_member_ep_id of this StorageVdMemberEp.

        :return: The vd_member_ep_id of this StorageVdMemberEp.
        :rtype: int
        """
        return self._vd_member_ep_id

    @vd_member_ep_id.setter
    def vd_member_ep_id(self, vd_member_ep_id):
        """
        Sets the vd_member_ep_id of this StorageVdMemberEp.

        :param vd_member_ep_id: The vd_member_ep_id of this StorageVdMemberEp.
        :type: int
        """

        self._vd_member_ep_id = vd_member_ep_id

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
        if not isinstance(other, StorageVdMemberEp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other