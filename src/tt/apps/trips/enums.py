from enum import Enum

from tt.apps.common.enums import LabeledEnum


class TripPage(str, Enum):
    """Enum for trip-related pages."""

    OVERVIEW   = 'trip_overview'
    PLANNING   = 'planning'
    ITINERARY  = 'itinerary'
    LOCATIONS  = 'locations'
    BOOKINGS   = 'bookings'
    REVIEWS    = 'reviews'
    JOURNAL    = 'journal'
    IMAGES     = 'images'
    MEMBERS    = 'members'


class TripPermissionLevel( LabeledEnum ):
    """
    Permission levels for trip sharing.
    """
    OWNER   = ( 'Propriétaire', 'Contrôle total, incluant la suppression et le partage' , 4 )
    ADMIN   = ( 'Admin', 'Peut modifier et gérer la plupart des aspects'                , 3 )
    EDITOR  = ( 'Éditeur', 'Peut modifier le contenu du voyage'                         , 2 )
    VIEWER  = ( 'Lecteur', 'Peut consulter le contenu du voyage'                        , 1 )

    def __init__( self, label, description, priority ):
        super().__init__( label, description )
        self.priority = priority
        return

    def __lt__( self, other ):
        if not isinstance( other, TripPermissionLevel ):
            return NotImplemented
        return bool( self.priority < other.priority )

    def __le__( self, other ):
        if not isinstance( other, TripPermissionLevel ):
            return NotImplemented
        return bool( self.priority <= other.priority )

    def __gt__( self, other ):
        if not isinstance( other, TripPermissionLevel ):
            return NotImplemented
        return bool( self.priority > other.priority )

    def __ge__( self, other ):
        if not isinstance( other, TripPermissionLevel ):
            return NotImplemented
        return bool( self.priority >= other.priority )

    def __eq__( self, other ):
        if not isinstance( other, TripPermissionLevel ):
            return False
        return bool( self.priority == other.priority )

    def __hash__( self ):
        return hash( self.priority )

    @property
    def is_owner(self):
        return bool( self in [ TripPermissionLevel.OWNER ])

    @property
    def is_admin(self):
        return bool( self in [ TripPermissionLevel.OWNER,
                               TripPermissionLevel.ADMIN ])

    @property
    def is_editor(self):
        return bool( self in [ TripPermissionLevel.OWNER,
                               TripPermissionLevel.ADMIN,
                               TripPermissionLevel.EDITOR ])

    
class TripStatus( LabeledEnum ):

    UPCOMING  = ( 'À venir', '' )
    CURRENT   = ( 'En cours', '' )
    PAST      = ( 'Passé', '' )
