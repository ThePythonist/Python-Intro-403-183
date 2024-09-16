people = {
    "09305541012": "3 mahe 20 gig",
    "09101881984": "1 mahe 10 gig",
    "09305541012": "1 rooze 1 gig",
    "09108843332": "7 rooze 7 gig",
}

msg = """
Moshtarake gerami {} hajm ya zamane basteye {} shoma
roo be etmam ast. Lotfan nesbat tamdid ya kharid basteye jadid
eghdam namayid.
"""

for k, v in people.items():
    print(msg.format(k, v))
