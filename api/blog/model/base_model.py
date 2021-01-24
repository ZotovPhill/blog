from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Instance of {self.__class__.__name__}> with attributes: \n {self.__attribute_list()}"

    def __attribute_list(self):
        result = ''
        for attr in dir(self):
            if not attr.startswith('__') and not attr.endswith('__'):
                result += f"\t{attr} = {getattr(self, attr)}\n"
        return result
