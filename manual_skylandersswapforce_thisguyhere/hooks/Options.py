# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, ItemSet

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
#class TotalCharactersToWinWith(Range):
#    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
#    display_name = "Number of characters to beat the game with before victory"
#    range_start = 10
#    range_end = 50
#    default = 50

class Goal(Choice):
    """Choose your victory condition.
    Defeat Kaos: Defeat Kaos...there's not much more to it
    All Levels Perfected: 
    """
    display_name = "Goal"
    defeat_kaos = 0
    all_levels_perfected = 1

class LinearMode(Toggle):
    """Receive chapters sequentially instead of in a random order. If false, you will need an existing save with minimal progress."""
    display_name = "Linear Mode"
    default = True

class NumChaptersToBeat(Range):
    """Number of chapter completions required to challenge Kaos. Set this low for synchronous multiworlds."""
    display_name = "Chapters to Beat"
    range_start = 1
    range_end = 20
    default = 16

class CharactersAsItems(Toggle):
    """Unlock skylanders individually instead of by element."""
    display_name = "Characters as Items"
    default = True

class ChallengesAsLocations(Toggle):
    """Add locations for Cali's heroic challenges."""
    display_name = "Challenges as Locations"
    default = False

class ArenasAsLocations(Toggle):
    """Add locations for Brock's arena battles."""
    display_name = "Arenas as Locations"
    default = True

class Shopsanity(Toggle):
    """Adds shop items as locations"""
    display_name = "Shopsanity"
    default = False

class EmpireOfIceAddon(Toggle):
    """Adds checks for the Empire of Ice adventure pack."""
    display_name = "Empire of Ice Pack"
    default = False

class PirateShipAddon(Toggle):
    """Adds checks for the Pirate Ship adventure pack."""
    display_name = "Pirate Ship Pack"
    default = False

class DarklightCryptAddon(Toggle):
    """Adds checks for the Darklight Crypt adventure pack."""
    display_name = "Darklight Crypt Pack"
    default = False

class DragonsPeakAddon(Toggle):
    """Adds checks for the Dragon's Peak adventure pack."""
    display_name = "Dragon's Peak Pack"
    default = False

class ActiveItems(Toggle):
    """Adds active items to generation logic. Will only add items from enabled adventure packs."""
    display_name = "Active Items"
    default = False

class BattlePacks(Toggle):
    """Adds battle pack items to generation logic (there are only 2)."""
    display_name = "Battle Pack Items"
    default = False

class CharactersToExclude(ItemSet):
    """
    Skylanders that will not be included in generation.
    Does nothing if CharactersAsItems is false.
    Warning: if you have less than eight skylanders (and at least one from each element), some locations will be
      unreachable, which will make All Levels Perfected and some Completionist checks impossible to achieve
    """
    display_name = "Characters to Exclude"
    verify_item_name = True

class WhitelistCharacters(Toggle):
    """
    Treat CharactersToExclude as a whitelist instead of a blacklist. 
    """
    display_name = "Whitelist Characters"
    default = False

class OldGenCharacters(Toggle):
    """
    Allow skylanders from the previous game that did not get an update. 
    """
    display_name = "Old-gen Skylanders"
    default = False

class ElementLockWeight(Range):
    """Weight of Element Lock traps. Set to 0 to disable. Don't set all trap weights to 0."""
    display_name = "Element Lock trap Weight"
    range_start = 0
    range_end = 100
    default = 35

class RenameSkylanderWeight(Range):
    """Weight of Rename Skylander traps. Set to 0 to disable. Don't set all trap weights to 0."""
    display_name = "Rename Skylander trap Weight"
    range_start = 0
    range_end = 100
    default = 20

class SoloWeight(Range):
    """Weight of Solo traps. Set to 0 to disable. Don't set all trap weights to 0."""
    display_name = "Solo trap Weight"
    range_start = 0
    range_end = 100
    default = 15

class ResetCharacterWeight(Range):
    """Weight of Reset Last Skylander traps. Set to 0 to disable. Don't set all trap weights to 0."""
    display_name = "Reset Last Skylander trap Weight"
    range_start = 0
    range_end = 100
    default = 10

class HeavyHitterWeight(Range):
    """Weight of Heavy Hitter traps. Set to 0 to disable. Don't set all trap weights to 0."""
    display_name = "Heavy Hitter trap Weight"
    range_start = 0
    range_end = 100
    default = 20

class FillerTrapPercent(Range):
    """How many fillers will be replaced with traps. 0 means no traps at all, 100 means all fillers are traps."""
    display_name = "TrapPercent"
    range_end = 100
    default = 50

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["goal"] = Goal
    options["linear_mode"] = LinearMode
    options["chapters_to_beat"] = NumChaptersToBeat
    options["characters_as_items"] = CharactersAsItems
    options["challenges_as_locations"] = ChallengesAsLocations
    options["arenas_as_locations"] = ArenasAsLocations
    options["shopsanity"] = Shopsanity
    options["include_empire"] = EmpireOfIceAddon
    options["include_ship"] = PirateShipAddon
    options["include_crypt"] = DarklightCryptAddon
    options["include_peak"] = DragonsPeakAddon
    options["active_items"] = ActiveItems
    options["battle_packs"] = BattlePacks
    options["characters_to_exclude"] = CharactersToExclude
    options["whitelist_characters"] = WhitelistCharacters
    options["old_gen_skylanders"] = OldGenCharacters
    options["element_lock_trap_weight"] = ElementLockWeight
    options["rename_skylander_trap_weight"] = RenameSkylanderWeight
    options["solo_trap_weight"] = SoloWeight
    options["heavy_hitter_trap_weight"] = HeavyHitterWeight
    options["reset_last_skylander_trap_weight"] = ResetCharacterWeight
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    
    options["filler_traps"] = FillerTrapPercent

    return options