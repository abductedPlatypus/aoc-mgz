"""Player stats."""

from construct import Embedded, Float32l, If, Struct, this, Array

from mgz.util import ModVersionAdapter, Version

# pylint: disable=invalid-name


# Snapshot taken at the start of the recorded game.
player_stats = "player_stats"/Struct(
    "resources"/Struct(
        "food"/Float32l,
        "wood"/Float32l,
        "stone"/Float32l,
        "gold"/Float32l,
    ),
    "headroom"/Float32l,
    "conversion_range"/Float32l,
    "current_age"/Float32l,
    "num_relics"/Float32l,
    "trade_bonus"/Float32l,
    "trade_goods"/Float32l,
    "trade_production"/Float32l,
    "pop_current"/Float32l,
    "decay"/Float32l,
    "discovery"/Float32l,
    "ruins"/Float32l,
    "meat"/Float32l,
    "berries"/Float32l,
    "fish"/Float32l,
    "u10"/Float32l,
    "total_units_created"/Float32l,
    "num_kills"/Float32l,
    "num_items_researched"/Float32l,
    "percent_map_explored"/Float32l,
    "castle_age"/Float32l,
    "imperial_age"/Float32l,
    "feudal_age"/Float32l,
    "u14"/Float32l,
    "convert_priests"/Float32l,
    "convert_buildings"/Float32l,
    "u17"/Float32l,
    "building_limit"/Float32l,
    "food_limit"/Float32l,
    "pop_max"/Float32l,
    "maintenance"/Float32l,
    "faith"/Float32l,
    "faith_recharge_rate"/Float32l,
    "farm_food_amount"/Float32l,
    "civilian_pop"/Float32l,
    "u23"/Float32l,
    "all_techs_achieved"/Float32l,
    "military_pop"/Float32l,
    "conversions"/Float32l,
    "num_wonders"/Float32l,
    "razings"/Float32l,
    "kill_ratio"/Float32l,
    "player_killed"/Float32l,
    "tribute_inefficiency"/Float32l,
    "gold_bonus_mining_productivity"/Float32l,
    "town_center_unavailable"/Float32l,
    "total_gold_gathered_2"/Float32l,
    "has_cartography"/Float32l,
    "houses_count"/Float32l,
    "monasteries"/Float32l,
    "total_resources_tributed"/Float32l,
    "hold_ruins"/Float32l,
    "hold_relics"/Float32l,
    "ore"/Float32l,
    "captured_unit"/Float32l,
    "dark_age"/Float32l,
    "trade_good_quality"/Float32l,
    "trade_market_level"/Float32l,
    "formations"/Float32l,
    "building_housing_rate"/Float32l,
    "gather_tax_rate"/Float32l,
    "gather_accumulator"/Float32l,
    "decay_rate"/Float32l,
    "allow_formations"/Float32l,
    "can_convert"/Float32l,
    "hit_points_killed"/Float32l,
    "p1_kills"/Float32l,
    "p2_kills"/Float32l,
    "p3_kills"/Float32l,
    "p4_kills"/Float32l,
    "p5_kills"/Float32l,
    "p6_kills"/Float32l,
    "p7_kills"/Float32l,
    "p8_kills"/Float32l,
    "convert_resistance"/Float32l,
    "trade_fee"/Float32l,
    "stone_mining_productivity"/Float32l,
    "num_units_queued"/Float32l,
    "num_units_making"/Float32l,
    "raider"/Float32l,
    "boarding_recharge_rate"/Float32l,
    "starting_villagers"/Float32l,
    "research_cost_mod"/Float32l,
    "research_time_mod"/Float32l,
    "convert_boats"/Float32l,
    "fish_trap_food"/Float32l,
    "heal_rate_modifier"/Float32l,
    "heal_range"/Float32l,
    "food_bonus"/Float32l,
    "wood_bonus"/Float32l,
    "stone_bonus"/Float32l,
    "gold_bonus"/Float32l,
    "raider_ability"/Float32l,
    "berserker_heal_timer"/Float32l,
    "dominant_sheep_control"/Float32l,
    "object_cost_summation"/Float32l,
    "research_cost_summation"/Float32l,
    "relic_income_summation"/Float32l,
    "trade_income_summation"/Float32l,
    "p1_tributed_to"/Float32l,
    "p2_tributed_to"/Float32l,
    "p3_tributed_to"/Float32l,
    "p4_tributed_to"/Float32l,
    "p5_tributed_to"/Float32l,
    "p6_tributed_to"/Float32l,
    "p7_tributed_to"/Float32l,
    "p8_tributed_to"/Float32l,
    "p1_unit_kill_worth"/Float32l,
    "p2_unit_kill_worth"/Float32l,
    "p3_unit_kill_worth"/Float32l,
    "p4_unit_kill_worth"/Float32l,
    "p5_unit_kill_worth"/Float32l,
    "p6_unit_kill_worth"/Float32l,
    "p7_unit_kill_worth"/Float32l,
    "p8_unit_kill_worth"/Float32l,
    "p1_num_razes"/Float32l,
    "p2_num_razes"/Float32l,
    "p3_num_razes"/Float32l,
    "p4_num_razes"/Float32l,
    "p5_num_razes"/Float32l,
    "p6_num_razes"/Float32l,
    "p7_num_razes"/Float32l,
    "p8_num_razes"/Float32l,
    "p1_raze_worth"/Float32l,
    "p2_raze_worth"/Float32l,
    "p3_raze_worth"/Float32l,
    "p4_raze_worth"/Float32l,
    "p5_raze_worth"/Float32l,
    "p6_raze_worth"/Float32l,
    "p7_raze_worth"/Float32l,
    "p8_raze_worth"/Float32l,
    "num_castles"/Float32l,
    "num_wonders"/Float32l,
    "kills_by_p1"/Float32l,
    "kills_by_p2"/Float32l,
    "kills_by_p3"/Float32l,
    "kills_by_p4"/Float32l,
    "kills_by_p5"/Float32l,
    "kills_by_p6"/Float32l,
    "kills_by_p7"/Float32l,
    "kills_by_p8"/Float32l,
    "razings_by_p1"/Float32l,
    "razings_by_p2"/Float32l,
    "razings_by_p3"/Float32l,
    "razings_by_p4"/Float32l,
    "razings_by_p5"/Float32l,
    "razings_by_p6"/Float32l,
    "razings_by_p7"/Float32l,
    "razings_by_p8"/Float32l,
    "value_killed_by_others"/Float32l,
    "value_razed_by_others"/Float32l,
    "kills"/Float32l,
    "losses"/Float32l,
    "p1_tribute_recvd"/Float32l,
    "p2_tribute_recvd"/Float32l,
    "p3_tribute_recvd"/Float32l,
    "p4_tribute_recvd"/Float32l,
    "p5_tribute_recvd"/Float32l,
    "p6_tribute_recvd"/Float32l,
    "p7_tribute_recvd"/Float32l,
    "p8_tribute_recvd"/Float32l,
    "current_unit_worth"/Float32l,
    "current_building_worth"/Float32l,
    "total_food_gathered"/Float32l,
    "total_wood_gathered"/Float32l,
    "total_stone_gathered"/Float32l,
    "total_gold_gathered"/Float32l,
    "total_kill_and_raze_worth"/Float32l,
    "total_tribute_recvd"/Float32l,
    "total_value_of_razings"/Float32l,
    "castle_high"/Float32l,
    "wonder_high"/Float32l,
    "total_tribute_sent"/Float32l,
    "convert_min_adj"/Float32l,
    "convert_max_adj"/Float32l,
    "convert_resist_min_adj"/Float32l,
    "convert_resist_max_adj"/Float32l,
    "convert_building_min"/Float32l,
    "convert_building_max"/Float32l,
    "convert_building_chance"/Float32l,
    "spies"/Float32l,
    "value_wonders_castles"/Float32l,
    "food_score"/Float32l,
    "wood_score"/Float32l,
    "stone_score"/Float32l,
    "gold_score"/Float32l,
    Embedded(If(this._._._._.save_version >= 11.76, Struct(
        "wood_bonus0"/Float32l,
        "food_bonus0"/Float32l,
        "relic_rate"/Float32l,
        "heresy"/Float32l,
        "theocracy"/Float32l,
        "crenellations"/Float32l,
        "construction_rate_mod"/Float32l,
        "hun_wonder_bonus"/Float32l,
        "spies_discount"/Float32l,
    ))),
    Embedded(If(this._._._._.version == Version.DE, Struct(
        Array(this._._.num_header_data - 198, Float32l)
    ))),
    Embedded(If(this._._._._.version in [Version.USERPATCH15, Version.MCP], Struct(
        ModVersionAdapter("mod"/Float32l),
        Array(6, Float32l),
        "trickle_food"/Float32l,
        "trickle_wood"/Float32l,
        "trickle_stone"/Float32l,
        "trickle_gold"/Float32l,
        "reveal_enemy_tcs"/Float32l,
        "reveal_gaia_class_1"/Float32l,
        "reveal_gaia_class_2"/Float32l,
        Array(28, Float32l)
    ))),
    Embedded(If(this._._._._.version == Version.MCP, Struct(
        Array(65, Float32l)
    )))
)
