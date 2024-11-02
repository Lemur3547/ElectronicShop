from rest_framework.exceptions import ValidationError


class DebtUpdateValidator:
    def __init__(self, value):
        self.value = value

    def __call__(self, value, *args, **kwargs):
        if value.get('debt') or value.get('debt') == 0:
            raise ValidationError('Нельзя изменять задолженность')
