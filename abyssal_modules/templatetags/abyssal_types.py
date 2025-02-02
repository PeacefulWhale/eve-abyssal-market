from django import template


register = template.Library()


@register.simple_tag
def get_abyssal_type_list():
    return [
        (
            "Microwarpdrives",
            [("5MN", 47740), ("50MN", 47408), ("500MN", 47745), ("50000MN", 56306)],
        ),
        (
            "Afterburners",
            [("1MN", 47749), ("10MN", 47753), ("100MN", 47757), ("10000MN", 56305)],
        ),
        ("Shield Extenders", [("Small", 47800), ("Medium", 47804), ("Large", 47808)]),
        ("Armor Plates", [("Small", 47812), ("Medium", 47817), ("Large", 47820)]),
        (
            "Shield Boosters",
            [
                ("Small", 47781),
                ("Medium", 47785),
                ("Large", 47789),
                ("X-Large", 47793),
                ("Capital", 56309),
            ],
        ),
        (
            "Armor Repairers",
            [("Small", 47769), ("Medium", 47773), ("Large", 47777), ("Capital", 56307)],
        ),
        (
            "Ancil. Shield Boosters",
            [
                ("Medium", 47836),
                ("Large", 47838),
                ("X-Large", 47840),
                ("Capital", 56310),
            ],
        ),
        (
            "Ancil. Armor Repairers",
            [("Small", 47842), ("Medium", 47844), ("Large", 47846), ("Capital", 56308)],
        ),
        (
            "Energy Neutralizers",
            [("Small", 47824), ("Medium", 47828), ("Heavy", 47832), ("Capital", 56312)],
        ),
        (
            "Energy Nosferatus",
            [("Small", 48419), ("Medium", 48423), ("Heavy", 48427), ("Capital", 56311)],
        ),
        ("Cap Batteries", [("Small", 48431), ("Medium", 48435), ("Large", 48439)]),
        ("Stasis Webifiers", [("Stasis Webifiers", 47702)]),
        (
            "Warp Scramblers",
            [("Warp Scramblers", 47732), ("Heavy Warp Scramblers", 56303)],
        ),
        (
            "Warp Disruptors",
            [("Warp Disruptors", 47736), ("Heavy Warp Disruptors", 56304)],
        ),
        (
            "Damage Modules",
            [
                ("Gyrostabilizer", 49730),
                ("Mag. Field Stab.", 49722),
                ("Heat Sink", 49726),
                ("Ballistic Control", 49738),
                ("Entropic Sink", 49734),
                ("Drone Amp.", 60482),
            ],
        ),
        ("Damage Control", [("Standard", 52227), ("Assault", 52230)]),
        ("Fighter Support Unit", [("Fighter Support Unit", 60483)]),
        ("Siege Module", [("Siege Module", 56313)]),
        (
            "Drones",
            [
                ("Light", 60478),
                ("Medium", 60479),
                ("Heavy", 60480),
                ("Sentry", 60481),
            ],
        ),
    ]
