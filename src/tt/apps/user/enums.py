from enum import Enum

from tt.apps.common.enums import LabeledEnum


class SigninErrorType( LabeledEnum ):
    """
    Error types that can be displayed on the signin page.
    """
    INVITATION_EXPIRED = (
        'Lien d\'invitation expiré',
        'Ce lien d\'invitation a expiré ou a déjà été utilisé. Vous avez été ajouté au voyage — connectez-vous simplement ci-dessous pour y accéder.',
    )


class AccountPageType(str, Enum):
    """Enum for account-related pages."""

    PROFILE     = 'profile'
    API_TOKENS  = 'api_tokens'
    EXTENSIONS  = 'extensions'
