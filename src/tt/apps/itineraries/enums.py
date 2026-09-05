from tt.apps.common.enums import LabeledEnum


class ItineraryItemType( LabeledEnum ):

    FLIGHT       = ( 'Vol', '' )
    RAIL         = ( 'Train', '' )
    BUS          = ( 'Autobus/Navette', '' )
    BOAT         = ( 'Bateau', '' )
    CAR          = ( 'Voiture', '' )
    CAR_RENTAL   = ( 'Location de voiture', '' )
    CAR_SERVICE  = ( 'Service de voiture', '' )
    LODGING      = ( 'Hébergement', '' )
    ACTIVITY        = ( 'Activité', '' )
    TOUR         = ( 'Visite guidée', '' )
    OTHER        = ( 'Autre', '' )
