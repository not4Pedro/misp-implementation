from pymisp import MISPObject, InvalidMISPObject


class TaranisObject(MISPObject):
    """ Following way to handle path to custom templates work:
          misp_objects_path_custom='/home/<user>/PycharmProjects/pythonProject/docker-misp/PyMISP/pymisp/data/misp-objects/objects'
     ^^^ WRONG this is also the default path to templates for PyMISP

        - CORRECT The custom template can be saved in the venv of the pymisp site-package (example):
        misp_objects_path_custom='/home/<user>/PycharmProjects/misp-implementation/venv/lib/python3.11/site-packages/pymisp/data/misp-objects/objects'
        OR RELATIVE PATH: misp_objects_path_custom='venv/lib/python3.11/site-packages/pymisp/data/misp-objects/objects'
        - For this to work, an API key is required to authenticate to the MISP instance, create one in MISP GUI first
    """

    def __init__(self, parameters: dict, strict: bool = True, **kwargs):
        super().__init__(name='taranis-news-item', strict=strict, **kwargs)
        self._parameters = parameters
        self.generate_attributes()

    def generate_attributes(self):
        """Contains the logic where all the values of the object are gathered"""
        if hasattr(self, '_parameters'):
            for object_relation in self._definition['attributes']:
                value = self._parameters.pop(object_relation, None)
                if not value:
                    continue
                if isinstance(value, dict):
                    self.add_attribute(object_relation, **value)
                elif isinstance(value, list):
                    self.add_attributes(object_relation, *value)
                else:
                    # Assume it is the value only
                    self.add_attribute(object_relation, value=value)
            if self._strict and self._known_template and self._parameters:
                raise InvalidMISPObject(
                    'Some object relations are unknown in the template and could not be attached: {}'.format(
                        ', '.join(self._parameters)))
