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


class WorkflowWorkflowTask(object):
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
        'input_params': 'object',
        'name': 'str',
        'optional': 'bool',
        'task_ref_name': 'str',
        'type': 'str',
        'workflowmeta': 'MoMoRef'
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
        'input_params': 'InputParams',
        'name': 'Name',
        'optional': 'Optional',
        'task_ref_name': 'TaskRefName',
        'type': 'Type',
        'workflowmeta': 'Workflowmeta'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, input_params=None, name=None, optional=None, task_ref_name=None, type=None, workflowmeta=None):
        """
        WorkflowWorkflowTask - a model defined in Swagger
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
        self._input_params = None
        self._name = None
        self._optional = None
        self._task_ref_name = None
        self._type = None
        self._workflowmeta = None

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
        if input_params is not None:
          self.input_params = input_params
        if name is not None:
          self.name = name
        if optional is not None:
          self.optional = optional
        if task_ref_name is not None:
          self.task_ref_name = task_ref_name
        if type is not None:
          self.type = type
        if workflowmeta is not None:
          self.workflowmeta = workflowmeta

    @property
    def account_moid(self):
        """
        Gets the account_moid of this WorkflowWorkflowTask.
        The Account ID for this managed object.  

        :return: The account_moid of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this WorkflowWorkflowTask.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this WorkflowWorkflowTask.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkflowWorkflowTask.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this WorkflowWorkflowTask.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkflowWorkflowTask.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this WorkflowWorkflowTask.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this WorkflowWorkflowTask.
        The time when this managed object was created.  

        :return: The create_time of this WorkflowWorkflowTask.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this WorkflowWorkflowTask.
        The time when this managed object was created.  

        :param create_time: The create_time of this WorkflowWorkflowTask.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this WorkflowWorkflowTask.
        The time when this managed object was last modified.  

        :return: The mod_time of this WorkflowWorkflowTask.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this WorkflowWorkflowTask.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this WorkflowWorkflowTask.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this WorkflowWorkflowTask.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this WorkflowWorkflowTask.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this WorkflowWorkflowTask.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowWorkflowTask.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowWorkflowTask.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this WorkflowWorkflowTask.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this WorkflowWorkflowTask.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this WorkflowWorkflowTask.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WorkflowWorkflowTask.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this WorkflowWorkflowTask.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this WorkflowWorkflowTask.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this WorkflowWorkflowTask.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WorkflowWorkflowTask.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this WorkflowWorkflowTask.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this WorkflowWorkflowTask.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this WorkflowWorkflowTask.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this WorkflowWorkflowTask.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this WorkflowWorkflowTask.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this WorkflowWorkflowTask.
        A unique identifier of this Managed Object instance.  

        :return: The id of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkflowWorkflowTask.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this WorkflowWorkflowTask.
        :type: str
        """

        self._id = id

    @property
    def input_params(self):
        """
        Gets the input_params of this WorkflowWorkflowTask.

        :return: The input_params of this WorkflowWorkflowTask.
        :rtype: object
        """
        return self._input_params

    @input_params.setter
    def input_params(self, input_params):
        """
        Sets the input_params of this WorkflowWorkflowTask.

        :param input_params: The input_params of this WorkflowWorkflowTask.
        :type: object
        """

        self._input_params = input_params

    @property
    def name(self):
        """
        Gets the name of this WorkflowWorkflowTask.

        :return: The name of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowWorkflowTask.

        :param name: The name of this WorkflowWorkflowTask.
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """
        Gets the optional of this WorkflowWorkflowTask.

        :return: The optional of this WorkflowWorkflowTask.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this WorkflowWorkflowTask.

        :param optional: The optional of this WorkflowWorkflowTask.
        :type: bool
        """

        self._optional = optional

    @property
    def task_ref_name(self):
        """
        Gets the task_ref_name of this WorkflowWorkflowTask.

        :return: The task_ref_name of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._task_ref_name

    @task_ref_name.setter
    def task_ref_name(self, task_ref_name):
        """
        Sets the task_ref_name of this WorkflowWorkflowTask.

        :param task_ref_name: The task_ref_name of this WorkflowWorkflowTask.
        :type: str
        """

        self._task_ref_name = task_ref_name

    @property
    def type(self):
        """
        Gets the type of this WorkflowWorkflowTask.

        :return: The type of this WorkflowWorkflowTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkflowWorkflowTask.

        :param type: The type of this WorkflowWorkflowTask.
        :type: str
        """

        self._type = type

    @property
    def workflowmeta(self):
        """
        Gets the workflowmeta of this WorkflowWorkflowTask.

        :return: The workflowmeta of this WorkflowWorkflowTask.
        :rtype: MoMoRef
        """
        return self._workflowmeta

    @workflowmeta.setter
    def workflowmeta(self, workflowmeta):
        """
        Sets the workflowmeta of this WorkflowWorkflowTask.

        :param workflowmeta: The workflowmeta of this WorkflowWorkflowTask.
        :type: MoMoRef
        """

        self._workflowmeta = workflowmeta

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
        if not isinstance(other, WorkflowWorkflowTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
