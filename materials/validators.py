import re
from rest_framework.serializers import ValidationError


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pattern = r'^https://www.youtube.com/watch\?v='
        tmp_val = dict(value).get(self.field)
        result = re.match(pattern, tmp_val)
        if not result:
            raise ValidationError('Не является YouTube ссылкой')
