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


class SecurityUnit(object):
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
        'compute_board': 'MoMoRef',
        'oper_state': 'str',
        'operability': 'str',
        'part_number': 'str',
        'pci_slot': 'str',
        'power': 'str',
        'presence': 'str',
        'registered_device': 'MoMoRef',
        'thermal': 'str',
        'unit_id': 'int',
        'vid': 'str',
        'voltage': 'str'
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
        'compute_board': 'ComputeBoard',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'part_number': 'PartNumber',
        'pci_slot': 'PciSlot',
        'power': 'Power',
        'presence': 'Presence',
        'registered_device': 'RegisteredDevice',
        'thermal': 'Thermal',
        'unit_id': 'UnitId',
        'vid': 'Vid',
        'voltage': 'Voltage'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, compute_board=None, oper_state=None, operability=None, part_number=None, pci_slot=None, power=None, presence=None, registered_device=None, thermal=None, unit_id=None, vid=None, voltage=None):
        """
        SecurityUnit - a model defined in Swagger
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
        self._compute_board = None
        self._oper_state = None
        self._operability = None
        self._part_number = None
        self._pci_slot = None
        self._power = None
        self._presence = None
        self._registered_device = None
        self._thermal = None
        self._unit_id = None
        self._vid = None
        self._voltage = None

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
        if compute_board is not None:
          self.compute_board = compute_board
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if part_number is not None:
          self.part_number = part_number
        if pci_slot is not None:
          self.pci_slot = pci_slot
        if power is not None:
          self.power = power
        if presence is not None:
          self.presence = presence
        if registered_device is not None:
          self.registered_device = registered_device
        if thermal is not None:
          self.thermal = thermal
        if unit_id is not None:
          self.unit_id = unit_id
        if vid is not None:
          self.vid = vid
        if voltage is not None:
          self.voltage = voltage

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SecurityUnit.
        The Account ID for this managed object.  

        :return: The account_moid of this SecurityUnit.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SecurityUnit.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SecurityUnit.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SecurityUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SecurityUnit.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SecurityUnit.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SecurityUnit.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this SecurityUnit.
        The time when this managed object was created.  

        :return: The create_time of this SecurityUnit.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SecurityUnit.
        The time when this managed object was created.  

        :param create_time: The create_time of this SecurityUnit.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SecurityUnit.
        The time when this managed object was last modified.  

        :return: The mod_time of this SecurityUnit.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SecurityUnit.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SecurityUnit.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SecurityUnit.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this SecurityUnit.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SecurityUnit.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this SecurityUnit.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SecurityUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this SecurityUnit.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SecurityUnit.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this SecurityUnit.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SecurityUnit.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this SecurityUnit.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SecurityUnit.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SecurityUnit.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this SecurityUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SecurityUnit.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SecurityUnit.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SecurityUnit.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this SecurityUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this SecurityUnit.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SecurityUnit.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this SecurityUnit.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this SecurityUnit.
        A unique identifier of this Managed Object instance.  

        :return: The id of this SecurityUnit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityUnit.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this SecurityUnit.
        :type: str
        """

        self._id = id

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this SecurityUnit.

        :return: The device_mo_id of this SecurityUnit.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this SecurityUnit.

        :param device_mo_id: The device_mo_id of this SecurityUnit.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this SecurityUnit.

        :return: The dn of this SecurityUnit.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this SecurityUnit.

        :param dn: The dn of this SecurityUnit.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this SecurityUnit.

        :return: The rn of this SecurityUnit.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this SecurityUnit.

        :param rn: The rn of this SecurityUnit.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this SecurityUnit.

        :return: The model of this SecurityUnit.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this SecurityUnit.

        :param model: The model of this SecurityUnit.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this SecurityUnit.

        :return: The revision of this SecurityUnit.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this SecurityUnit.

        :param revision: The revision of this SecurityUnit.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this SecurityUnit.

        :return: The serial of this SecurityUnit.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this SecurityUnit.

        :param serial: The serial of this SecurityUnit.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this SecurityUnit.

        :return: The vendor of this SecurityUnit.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this SecurityUnit.

        :param vendor: The vendor of this SecurityUnit.
        :type: str
        """

        self._vendor = vendor

    @property
    def compute_board(self):
        """
        Gets the compute_board of this SecurityUnit.

        :return: The compute_board of this SecurityUnit.
        :rtype: MoMoRef
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """
        Sets the compute_board of this SecurityUnit.

        :param compute_board: The compute_board of this SecurityUnit.
        :type: MoMoRef
        """

        self._compute_board = compute_board

    @property
    def oper_state(self):
        """
        Gets the oper_state of this SecurityUnit.

        :return: The oper_state of this SecurityUnit.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this SecurityUnit.

        :param oper_state: The oper_state of this SecurityUnit.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this SecurityUnit.

        :return: The operability of this SecurityUnit.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this SecurityUnit.

        :param operability: The operability of this SecurityUnit.
        :type: str
        """

        self._operability = operability

    @property
    def part_number(self):
        """
        Gets the part_number of this SecurityUnit.

        :return: The part_number of this SecurityUnit.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this SecurityUnit.

        :param part_number: The part_number of this SecurityUnit.
        :type: str
        """

        self._part_number = part_number

    @property
    def pci_slot(self):
        """
        Gets the pci_slot of this SecurityUnit.

        :return: The pci_slot of this SecurityUnit.
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """
        Sets the pci_slot of this SecurityUnit.

        :param pci_slot: The pci_slot of this SecurityUnit.
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def power(self):
        """
        Gets the power of this SecurityUnit.

        :return: The power of this SecurityUnit.
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        """
        Sets the power of this SecurityUnit.

        :param power: The power of this SecurityUnit.
        :type: str
        """

        self._power = power

    @property
    def presence(self):
        """
        Gets the presence of this SecurityUnit.

        :return: The presence of this SecurityUnit.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this SecurityUnit.

        :param presence: The presence of this SecurityUnit.
        :type: str
        """

        self._presence = presence

    @property
    def registered_device(self):
        """
        Gets the registered_device of this SecurityUnit.

        :return: The registered_device of this SecurityUnit.
        :rtype: MoMoRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this SecurityUnit.

        :param registered_device: The registered_device of this SecurityUnit.
        :type: MoMoRef
        """

        self._registered_device = registered_device

    @property
    def thermal(self):
        """
        Gets the thermal of this SecurityUnit.

        :return: The thermal of this SecurityUnit.
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """
        Sets the thermal of this SecurityUnit.

        :param thermal: The thermal of this SecurityUnit.
        :type: str
        """

        self._thermal = thermal

    @property
    def unit_id(self):
        """
        Gets the unit_id of this SecurityUnit.

        :return: The unit_id of this SecurityUnit.
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """
        Sets the unit_id of this SecurityUnit.

        :param unit_id: The unit_id of this SecurityUnit.
        :type: int
        """

        self._unit_id = unit_id

    @property
    def vid(self):
        """
        Gets the vid of this SecurityUnit.

        :return: The vid of this SecurityUnit.
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """
        Sets the vid of this SecurityUnit.

        :param vid: The vid of this SecurityUnit.
        :type: str
        """

        self._vid = vid

    @property
    def voltage(self):
        """
        Gets the voltage of this SecurityUnit.

        :return: The voltage of this SecurityUnit.
        :rtype: str
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """
        Sets the voltage of this SecurityUnit.

        :param voltage: The voltage of this SecurityUnit.
        :type: str
        """

        self._voltage = voltage

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
        if not isinstance(other, SecurityUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
