# from typing import Dict, Any
# from django.test import TestCase

# class TestExpectedSettings(TestCase):
#     def _get_settings(settings_module: object) -> Dict[str, Any]:
#         """
#         Load Django settings from a given module.

#         Args:
#             settings_module (object): Django settings module.

#         Returns:
#             dict: Django settings.
#         """
#         _vars: Dict[str, Any] = vars(settings_module)
#         result = {
#             name: value for (name, value) in _vars.items() if name.isupper()
#         } 
#         # return result
    
#     def compare_settings(self, result):
#         expected_settings = {
#             'DEBUG': False,
#             'SECRET_KEY': 'secret_key',
#             }

#         assert expected_settings == _get_settings(settings_env)
