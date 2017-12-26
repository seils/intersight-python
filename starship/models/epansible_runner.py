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


class EpansibleRunner(object):
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
        'account': 'MoMoRef',
        'exit_code': 'int',
        'extra_vars': 'str',
        'oper_state': 'str',
        'playbook': 'str',
        'stderr': 'str',
        'stdout': 'str'
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
        'account': 'Account',
        'exit_code': 'ExitCode',
        'extra_vars': 'ExtraVars',
        'oper_state': 'OperState',
        'playbook': 'Playbook',
        'stderr': 'Stderr',
        'stdout': 'Stdout'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, account=None, exit_code=None, extra_vars=None, oper_state=None, playbook=None, stderr=None, stdout=None):
        """
        EpansibleRunner - a model defined in Swagger
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
        self._account = None
        self._exit_code = None
        self._extra_vars = None
        self._oper_state = None
        self._playbook = None
        self._stderr = None
        self._stdout = None

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
        if account is not None:
          self.account = account
        if exit_code is not None:
          self.exit_code = exit_code
        if extra_vars is not None:
          self.extra_vars = extra_vars
        if oper_state is not None:
          self.oper_state = oper_state
        if playbook is not None:
          self.playbook = playbook
        if stderr is not None:
          self.stderr = stderr
        if stdout is not None:
          self.stdout = stdout

    @property
    def account_moid(self):
        """
        Gets the account_moid of this EpansibleRunner.
        The Account ID for this managed object.  

        :return: The account_moid of this EpansibleRunner.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EpansibleRunner.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this EpansibleRunner.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EpansibleRunner.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this EpansibleRunner.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EpansibleRunner.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this EpansibleRunner.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this EpansibleRunner.
        The time when this managed object was created.  

        :return: The create_time of this EpansibleRunner.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EpansibleRunner.
        The time when this managed object was created.  

        :param create_time: The create_time of this EpansibleRunner.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EpansibleRunner.
        The time when this managed object was last modified.  

        :return: The mod_time of this EpansibleRunner.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EpansibleRunner.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this EpansibleRunner.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EpansibleRunner.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this EpansibleRunner.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EpansibleRunner.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this EpansibleRunner.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EpansibleRunner.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this EpansibleRunner.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EpansibleRunner.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this EpansibleRunner.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EpansibleRunner.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this EpansibleRunner.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EpansibleRunner.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this EpansibleRunner.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this EpansibleRunner.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this EpansibleRunner.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EpansibleRunner.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this EpansibleRunner.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this EpansibleRunner.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this EpansibleRunner.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EpansibleRunner.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this EpansibleRunner.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this EpansibleRunner.
        A unique identifier of this Managed Object instance.  

        :return: The id of this EpansibleRunner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EpansibleRunner.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this EpansibleRunner.
        :type: str
        """

        self._id = id

    @property
    def account(self):
        """
        Gets the account of this EpansibleRunner.
        Delete this object when the account is deleted. 

        :return: The account of this EpansibleRunner.
        :rtype: MoMoRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this EpansibleRunner.
        Delete this object when the account is deleted. 

        :param account: The account of this EpansibleRunner.
        :type: MoMoRef
        """

        self._account = account

    @property
    def exit_code(self):
        """
        Gets the exit_code of this EpansibleRunner.
        Exit code of the workflow task  

        :return: The exit_code of this EpansibleRunner.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this EpansibleRunner.
        Exit code of the workflow task  

        :param exit_code: The exit_code of this EpansibleRunner.
        :type: int
        """

        self._exit_code = exit_code

    @property
    def extra_vars(self):
        """
        Gets the extra_vars of this EpansibleRunner.
        Extra variables for the ansible playbook.  

        :return: The extra_vars of this EpansibleRunner.
        :rtype: str
        """
        return self._extra_vars

    @extra_vars.setter
    def extra_vars(self, extra_vars):
        """
        Sets the extra_vars of this EpansibleRunner.
        Extra variables for the ansible playbook.  

        :param extra_vars: The extra_vars of this EpansibleRunner.
        :type: str
        """

        self._extra_vars = extra_vars

    @property
    def oper_state(self):
        """
        Gets the oper_state of this EpansibleRunner.
        Denotes if the task is pending, in_progress, completed_ok, completed_error  

        :return: The oper_state of this EpansibleRunner.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this EpansibleRunner.
        Denotes if the task is pending, in_progress, completed_ok, completed_error  

        :param oper_state: The oper_state of this EpansibleRunner.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def playbook(self):
        """
        Gets the playbook of this EpansibleRunner.
        Name of the ansible playbook to execute.  

        :return: The playbook of this EpansibleRunner.
        :rtype: str
        """
        return self._playbook

    @playbook.setter
    def playbook(self, playbook):
        """
        Sets the playbook of this EpansibleRunner.
        Name of the ansible playbook to execute.  

        :param playbook: The playbook of this EpansibleRunner.
        :type: str
        """

        self._playbook = playbook

    @property
    def stderr(self):
        """
        Gets the stderr of this EpansibleRunner.
        Standard error from the task execution  

        :return: The stderr of this EpansibleRunner.
        :rtype: str
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        """
        Sets the stderr of this EpansibleRunner.
        Standard error from the task execution  

        :param stderr: The stderr of this EpansibleRunner.
        :type: str
        """

        self._stderr = stderr

    @property
    def stdout(self):
        """
        Gets the stdout of this EpansibleRunner.
        Standard output from the task execution   

        :return: The stdout of this EpansibleRunner.
        :rtype: str
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """
        Sets the stdout of this EpansibleRunner.
        Standard output from the task execution   

        :param stdout: The stdout of this EpansibleRunner.
        :type: str
        """

        self._stdout = stdout

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
        if not isinstance(other, EpansibleRunner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
