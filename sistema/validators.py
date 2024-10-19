from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator

class NoRestrictionsValidator:
    def validate(self, password, user=None):
        pass  # Não faz validações

    def get_help_text(self):
        return "Esta senha não possui restrições."
