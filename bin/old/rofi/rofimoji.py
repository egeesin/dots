#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

emojis="""
⛑🏻 Helmet With White Cross, Type-1-2
⛑🏼 Helmet With White Cross, Type-3
⛑🏽 Helmet With White Cross, Type-4
⛑🏾 Helmet With White Cross, Type-5
⛑🏿 Helmet With White Cross, Type-6
💏🏻 Kiss, Type-1-2
💏🏼 Kiss, Type-3
💏🏽 Kiss, Type-4
💏🏾 Kiss, Type-5
💏🏿 Kiss, Type-6
💑🏻 Couple With Heart, Type-1-2
💑🏼 Couple With Heart, Type-3
💑🏽 Couple With Heart, Type-4
💑🏾 Couple With Heart, Type-5
💑🏿 Couple With Heart, Type-6
⛷🏻 Skier, Type-1-2
⛷🏼 Skier, Type-3
⛷🏽 Skier, Type-4
⛷🏾 Skier, Type-5
⛷🏿 Skier, Type-6
😀 Grinning Face
😁 Beaming Face With Smiling Eyes
😂 Face With Tears of Joy
🤣 Rolling on the Floor Laughing
😃 Grinning Face With Big Eyes
😄 Grinning Face With Smiling Eyes
😅 Grinning Face With Sweat
😆 Grinning Squinting Face
😉 Winking Face
😊 Smiling Face With Smiling Eyes
😋 Face Savoring Food
😎 Smiling Face With Sunglasses
😍 Smiling Face With Heart-Eyes
😘 Face Blowing a Kiss
😗 Kissing Face
😙 Kissing Face With Smiling Eyes
😚 Kissing Face With Closed Eyes
☺ Smiling Face
🙂 Slightly Smiling Face
🤗 Hugging Face
🤩 Star-Struck
🤔 Thinking Face
🤨 Face With Raised Eyebrow
😐 Neutral Face
😑 Expressionless Face
😶 Face Without Mouth
🙄 Face With Rolling Eyes
😏 Smirking Face
😣 Persevering Face
😥 Sad but Relieved Face
😮 Face With Open Mouth
🤐 Zipper-Mouth Face
😯 Hushed Face
😪 Sleepy Face
😫 Tired Face
😴 Sleeping Face
😌 Relieved Face
😛 Face With Tongue
😜 Winking Face With Tongue
😝 Squinting Face With Tongue
🤤 Drooling Face
😒 Unamused Face
😓 Downcast Face With Sweat
😔 Pensive Face
😕 Confused Face
🙃 Upside-Down Face
🤑 Money-Mouth Face
😲 Astonished Face
☹ Frowning Face
🙁 Slightly Frowning Face
😖 Confounded Face
😞 Disappointed Face
😟 Worried Face
😤 Face With Steam From Nose
😢 Crying Face
😭 Loudly Crying Face
😦 Frowning Face With Open Mouth
😧 Anguished Face
😨 Fearful Face
😩 Weary Face
🤯 Exploding Head
😬 Grimacing Face
😰 Anxious Face With Sweat
😱 Face Screaming in Fear
😳 Flushed Face
🤪 Zany Face
😵 Dizzy Face
😡 Pouting Face
😠 Angry Face
🤬 Face With Symbols on Mouth
😷 Face With Medical Mask
🤒 Face With Thermometer
🤕 Face With Head-Bandage
🤢 Nauseated Face
🤮 Face Vomiting
🤧 Sneezing Face
😇 Smiling Face With Halo
🤠 Cowboy Hat Face
🤡 Clown Face
🤥 Lying Face
🤫 Shushing Face
🤭 Face With Hand Over Mouth
🧐 Face With Monocle
🤓 Nerd Face
😈 Smiling Face With Horns
👿 Angry Face With Horns
👹 Ogre
👺 Goblin
💀 Skull
☠ Skull and Crossbones
👻 Ghost
👽 Alien
👾 Alien Monster
🤖 Robot Face
💩 Pile of Poo
😺 Grinning Cat Face
😸 Grinning Cat Face With Smiling Eyes
😹 Cat Face With Tears of Joy
😻 Smiling Cat Face With Heart-Eyes
😼 Cat Face With Wry Smile
😽 Kissing Cat Face
🙀 Weary Cat Face
😿 Crying Cat Face
😾 Pouting Cat Face
🙈 See-No-Evil Monkey
🙉 Hear-No-Evil Monkey
🙊 Speak-No-Evil Monkey
🏻 Light Skin Tone
🏼 Medium-Light Skin Tone
🏽 Medium Skin Tone
🏾 Medium-Dark Skin Tone
🏿 Dark Skin Tone
👶 Baby
👶🏻 Baby: Light Skin Tone
👶🏼 Baby: Medium-Light Skin Tone
👶🏽 Baby: Medium Skin Tone
👶🏾 Baby: Medium-Dark Skin Tone
👶🏿 Baby: Dark Skin Tone
🧒 Child
🧒🏻 Child: Light Skin Tone
🧒🏼 Child: Medium-Light Skin Tone
🧒🏽 Child: Medium Skin Tone
🧒🏾 Child: Medium-Dark Skin Tone
🧒🏿 Child: Dark Skin Tone
👦 Boy
👦🏻 Boy: Light Skin Tone
👦🏼 Boy: Medium-Light Skin Tone
👦🏽 Boy: Medium Skin Tone
👦🏾 Boy: Medium-Dark Skin Tone
👦🏿 Boy: Dark Skin Tone
👧 Girl
👧🏻 Girl: Light Skin Tone
👧🏼 Girl: Medium-Light Skin Tone
👧🏽 Girl: Medium Skin Tone
👧🏾 Girl: Medium-Dark Skin Tone
👧🏿 Girl: Dark Skin Tone
🧑 Adult
🧑🏻 Adult: Light Skin Tone
🧑🏼 Adult: Medium-Light Skin Tone
🧑🏽 Adult: Medium Skin Tone
🧑🏾 Adult: Medium-Dark Skin Tone
🧑🏿 Adult: Dark Skin Tone
👨 Man
👨🏻 Man: Light Skin Tone
👨🏼 Man: Medium-Light Skin Tone
👨🏽 Man: Medium Skin Tone
👨🏾 Man: Medium-Dark Skin Tone
👨🏿 Man: Dark Skin Tone
👩 Woman
👩🏻 Woman: Light Skin Tone
👩🏼 Woman: Medium-Light Skin Tone
👩🏽 Woman: Medium Skin Tone
👩🏾 Woman: Medium-Dark Skin Tone
👩🏿 Woman: Dark Skin Tone
🧓 Older Adult
🧓🏻 Older Adult: Light Skin Tone
🧓🏼 Older Adult: Medium-Light Skin Tone
🧓🏽 Older Adult: Medium Skin Tone
🧓🏾 Older Adult: Medium-Dark Skin Tone
🧓🏿 Older Adult: Dark Skin Tone
👴 Old Man
👴🏻 Old Man: Light Skin Tone
👴🏼 Old Man: Medium-Light Skin Tone
👴🏽 Old Man: Medium Skin Tone
👴🏾 Old Man: Medium-Dark Skin Tone
👴🏿 Old Man: Dark Skin Tone
👵 Old Woman
👵🏻 Old Woman: Light Skin Tone
👵🏼 Old Woman: Medium-Light Skin Tone
👵🏽 Old Woman: Medium Skin Tone
👵🏾 Old Woman: Medium-Dark Skin Tone
👵🏿 Old Woman: Dark Skin Tone
👨‍⚕️ Man Health Worker
👨🏻‍⚕️ Man Health Worker: Light Skin Tone
👨🏼‍⚕️ Man Health Worker: Medium-Light Skin Tone
👨🏽‍⚕️ Man Health Worker: Medium Skin Tone
👨🏾‍⚕️ Man Health Worker: Medium-Dark Skin Tone
👨🏿‍⚕️ Man Health Worker: Dark Skin Tone
👩‍⚕️ Woman Health Worker
👩🏻‍⚕️ Woman Health Worker: Light Skin Tone
👩🏼‍⚕️ Woman Health Worker: Medium-Light Skin Tone
👩🏽‍⚕️ Woman Health Worker: Medium Skin Tone
👩🏾‍⚕️ Woman Health Worker: Medium-Dark Skin Tone
👩🏿‍⚕️ Woman Health Worker: Dark Skin Tone
👨‍🎓 Man Student
👨🏻‍🎓 Man Student: Light Skin Tone
👨🏼‍🎓 Man Student: Medium-Light Skin Tone
👨🏽‍🎓 Man Student: Medium Skin Tone
👨🏾‍🎓 Man Student: Medium-Dark Skin Tone
👨🏿‍🎓 Man Student: Dark Skin Tone
👩‍🎓 Woman Student
👩🏻‍🎓 Woman Student: Light Skin Tone
👩🏼‍🎓 Woman Student: Medium-Light Skin Tone
👩🏽‍🎓 Woman Student: Medium Skin Tone
👩🏾‍🎓 Woman Student: Medium-Dark Skin Tone
👩🏿‍🎓 Woman Student: Dark Skin Tone
👨‍🏫 Man Teacher
👨🏻‍🏫 Man Teacher: Light Skin Tone
👨🏼‍🏫 Man Teacher: Medium-Light Skin Tone
👨🏽‍🏫 Man Teacher: Medium Skin Tone
👨🏾‍🏫 Man Teacher: Medium-Dark Skin Tone
👨🏿‍🏫 Man Teacher: Dark Skin Tone
👩‍🏫 Woman Teacher
👩🏻‍🏫 Woman Teacher: Light Skin Tone
👩🏼‍🏫 Woman Teacher: Medium-Light Skin Tone
👩🏽‍🏫 Woman Teacher: Medium Skin Tone
👩🏾‍🏫 Woman Teacher: Medium-Dark Skin Tone
👩🏿‍🏫 Woman Teacher: Dark Skin Tone
👨‍⚖️ Man Judge
👨🏻‍⚖️ Man Judge: Light Skin Tone
👨🏼‍⚖️ Man Judge: Medium-Light Skin Tone
👨🏽‍⚖️ Man Judge: Medium Skin Tone
👨🏾‍⚖️ Man Judge: Medium-Dark Skin Tone
👨🏿‍⚖️ Man Judge: Dark Skin Tone
👩‍⚖️ Woman Judge
👩🏻‍⚖️ Woman Judge: Light Skin Tone
👩🏼‍⚖️ Woman Judge: Medium-Light Skin Tone
👩🏽‍⚖️ Woman Judge: Medium Skin Tone
👩🏾‍⚖️ Woman Judge: Medium-Dark Skin Tone
👩🏿‍⚖️ Woman Judge: Dark Skin Tone
👨‍🌾 Man Farmer
👨🏻‍🌾 Man Farmer: Light Skin Tone
👨🏼‍🌾 Man Farmer: Medium-Light Skin Tone
👨🏽‍🌾 Man Farmer: Medium Skin Tone
👨🏾‍🌾 Man Farmer: Medium-Dark Skin Tone
👨🏿‍🌾 Man Farmer: Dark Skin Tone
👩‍🌾 Woman Farmer
👩🏻‍🌾 Woman Farmer: Light Skin Tone
👩🏼‍🌾 Woman Farmer: Medium-Light Skin Tone
👩🏽‍🌾 Woman Farmer: Medium Skin Tone
👩🏾‍🌾 Woman Farmer: Medium-Dark Skin Tone
👩🏿‍🌾 Woman Farmer: Dark Skin Tone
👨‍🍳 Man Cook
👨🏻‍🍳 Man Cook: Light Skin Tone
👨🏼‍🍳 Man Cook: Medium-Light Skin Tone
👨🏽‍🍳 Man Cook: Medium Skin Tone
👨🏾‍🍳 Man Cook: Medium-Dark Skin Tone
👨🏿‍🍳 Man Cook: Dark Skin Tone
👩‍🍳 Woman Cook
👩🏻‍🍳 Woman Cook: Light Skin Tone
👩🏼‍🍳 Woman Cook: Medium-Light Skin Tone
👩🏽‍🍳 Woman Cook: Medium Skin Tone
👩🏾‍🍳 Woman Cook: Medium-Dark Skin Tone
👩🏿‍🍳 Woman Cook: Dark Skin Tone
👨‍🔧 Man Mechanic
👨🏻‍🔧 Man Mechanic: Light Skin Tone
👨🏼‍🔧 Man Mechanic: Medium-Light Skin Tone
👨🏽‍🔧 Man Mechanic: Medium Skin Tone
👨🏾‍🔧 Man Mechanic: Medium-Dark Skin Tone
👨🏿‍🔧 Man Mechanic: Dark Skin Tone
👩‍🔧 Woman Mechanic
👩🏻‍🔧 Woman Mechanic: Light Skin Tone
👩🏼‍🔧 Woman Mechanic: Medium-Light Skin Tone
👩🏽‍🔧 Woman Mechanic: Medium Skin Tone
👩🏾‍🔧 Woman Mechanic: Medium-Dark Skin Tone
👩🏿‍🔧 Woman Mechanic: Dark Skin Tone
👨‍🏭 Man Factory Worker
👨🏻‍🏭 Man Factory Worker: Light Skin Tone
👨🏼‍🏭 Man Factory Worker: Medium-Light Skin Tone
👨🏽‍🏭 Man Factory Worker: Medium Skin Tone
👨🏾‍🏭 Man Factory Worker: Medium-Dark Skin Tone
👨🏿‍🏭 Man Factory Worker: Dark Skin Tone
👩‍🏭 Woman Factory Worker
👩🏻‍🏭 Woman Factory Worker: Light Skin Tone
👩🏼‍🏭 Woman Factory Worker: Medium-Light Skin Tone
👩🏽‍🏭 Woman Factory Worker: Medium Skin Tone
👩🏾‍🏭 Woman Factory Worker: Medium-Dark Skin Tone
👩🏿‍🏭 Woman Factory Worker: Dark Skin Tone
👨‍💼 Man Office Worker
👨🏻‍💼 Man Office Worker: Light Skin Tone
👨🏼‍💼 Man Office Worker: Medium-Light Skin Tone
👨🏽‍💼 Man Office Worker: Medium Skin Tone
👨🏾‍💼 Man Office Worker: Medium-Dark Skin Tone
👨🏿‍💼 Man Office Worker: Dark Skin Tone
👩‍💼 Woman Office Worker
👩🏻‍💼 Woman Office Worker: Light Skin Tone
👩🏼‍💼 Woman Office Worker: Medium-Light Skin Tone
👩🏽‍💼 Woman Office Worker: Medium Skin Tone
👩🏾‍💼 Woman Office Worker: Medium-Dark Skin Tone
👩🏿‍💼 Woman Office Worker: Dark Skin Tone
👨‍🔬 Man Scientist
👨🏻‍🔬 Man Scientist: Light Skin Tone
👨🏼‍🔬 Man Scientist: Medium-Light Skin Tone
👨🏽‍🔬 Man Scientist: Medium Skin Tone
👨🏾‍🔬 Man Scientist: Medium-Dark Skin Tone
👨🏿‍🔬 Man Scientist: Dark Skin Tone
👩‍🔬 Woman Scientist
👩🏻‍🔬 Woman Scientist: Light Skin Tone
👩🏼‍🔬 Woman Scientist: Medium-Light Skin Tone
👩🏽‍🔬 Woman Scientist: Medium Skin Tone
👩🏾‍🔬 Woman Scientist: Medium-Dark Skin Tone
👩🏿‍🔬 Woman Scientist: Dark Skin Tone
👨‍💻 Man Technologist
👨🏻‍💻 Man Technologist: Light Skin Tone
👨🏼‍💻 Man Technologist: Medium-Light Skin Tone
👨🏽‍💻 Man Technologist: Medium Skin Tone
👨🏾‍💻 Man Technologist: Medium-Dark Skin Tone
👨🏿‍💻 Man Technologist: Dark Skin Tone
👩‍💻 Woman Technologist
👩🏻‍💻 Woman Technologist: Light Skin Tone
👩🏼‍💻 Woman Technologist: Medium-Light Skin Tone
👩🏽‍💻 Woman Technologist: Medium Skin Tone
👩🏾‍💻 Woman Technologist: Medium-Dark Skin Tone
👩🏿‍💻 Woman Technologist: Dark Skin Tone
👨‍🎤 Man Singer
👨🏻‍🎤 Man Singer: Light Skin Tone
👨🏼‍🎤 Man Singer: Medium-Light Skin Tone
👨🏽‍🎤 Man Singer: Medium Skin Tone
👨🏾‍🎤 Man Singer: Medium-Dark Skin Tone
👨🏿‍🎤 Man Singer: Dark Skin Tone
👩‍🎤 Woman Singer
👩🏻‍🎤 Woman Singer: Light Skin Tone
👩🏼‍🎤 Woman Singer: Medium-Light Skin Tone
👩🏽‍🎤 Woman Singer: Medium Skin Tone
👩🏾‍🎤 Woman Singer: Medium-Dark Skin Tone
👩🏿‍🎤 Woman Singer: Dark Skin Tone
👨‍🎨 Man Artist
👨🏻‍🎨 Man Artist: Light Skin Tone
👨🏼‍🎨 Man Artist: Medium-Light Skin Tone
👨🏽‍🎨 Man Artist: Medium Skin Tone
👨🏾‍🎨 Man Artist: Medium-Dark Skin Tone
👨🏿‍🎨 Man Artist: Dark Skin Tone
👩‍🎨 Woman Artist
👩🏻‍🎨 Woman Artist: Light Skin Tone
👩🏼‍🎨 Woman Artist: Medium-Light Skin Tone
👩🏽‍🎨 Woman Artist: Medium Skin Tone
👩🏾‍🎨 Woman Artist: Medium-Dark Skin Tone
👩🏿‍🎨 Woman Artist: Dark Skin Tone
👨‍✈️ Man Pilot
👨🏻‍✈️ Man Pilot: Light Skin Tone
👨🏼‍✈️ Man Pilot: Medium-Light Skin Tone
👨🏽‍✈️ Man Pilot: Medium Skin Tone
👨🏾‍✈️ Man Pilot: Medium-Dark Skin Tone
👨🏿‍✈️ Man Pilot: Dark Skin Tone
👩‍✈️ Woman Pilot
👩🏻‍✈️ Woman Pilot: Light Skin Tone
👩🏼‍✈️ Woman Pilot: Medium-Light Skin Tone
👩🏽‍✈️ Woman Pilot: Medium Skin Tone
👩🏾‍✈️ Woman Pilot: Medium-Dark Skin Tone
👩🏿‍✈️ Woman Pilot: Dark Skin Tone
👨‍🚀 Man Astronaut
👨🏻‍🚀 Man Astronaut: Light Skin Tone
👨🏼‍🚀 Man Astronaut: Medium-Light Skin Tone
👨🏽‍🚀 Man Astronaut: Medium Skin Tone
👨🏾‍🚀 Man Astronaut: Medium-Dark Skin Tone
👨🏿‍🚀 Man Astronaut: Dark Skin Tone
👩‍🚀 Woman Astronaut
👩🏻‍🚀 Woman Astronaut: Light Skin Tone
👩🏼‍🚀 Woman Astronaut: Medium-Light Skin Tone
👩🏽‍🚀 Woman Astronaut: Medium Skin Tone
👩🏾‍🚀 Woman Astronaut: Medium-Dark Skin Tone
👩🏿‍🚀 Woman Astronaut: Dark Skin Tone
👨‍🚒 Man Firefighter
👨🏻‍🚒 Man Firefighter: Light Skin Tone
👨🏼‍🚒 Man Firefighter: Medium-Light Skin Tone
👨🏽‍🚒 Man Firefighter: Medium Skin Tone
👨🏾‍🚒 Man Firefighter: Medium-Dark Skin Tone
👨🏿‍🚒 Man Firefighter: Dark Skin Tone
👩‍🚒 Woman Firefighter
👩🏻‍🚒 Woman Firefighter: Light Skin Tone
👩🏼‍🚒 Woman Firefighter: Medium-Light Skin Tone
👩🏽‍🚒 Woman Firefighter: Medium Skin Tone
👩🏾‍🚒 Woman Firefighter: Medium-Dark Skin Tone
👩🏿‍🚒 Woman Firefighter: Dark Skin Tone
👮 Police Officer
👮🏻 Police Officer: Light Skin Tone
👮🏼 Police Officer: Medium-Light Skin Tone
👮🏽 Police Officer: Medium Skin Tone
👮🏾 Police Officer: Medium-Dark Skin Tone
👮🏿 Police Officer: Dark Skin Tone
👮‍♂️ Man Police Officer
👮🏻‍♂️ Man Police Officer: Light Skin Tone
👮🏼‍♂️ Man Police Officer: Medium-Light Skin Tone
👮🏽‍♂️ Man Police Officer: Medium Skin Tone
👮🏾‍♂️ Man Police Officer: Medium-Dark Skin Tone
👮🏿‍♂️ Man Police Officer: Dark Skin Tone
👮‍♀️ Woman Police Officer
👮🏻‍♀️ Woman Police Officer: Light Skin Tone
👮🏼‍♀️ Woman Police Officer: Medium-Light Skin Tone
👮🏽‍♀️ Woman Police Officer: Medium Skin Tone
👮🏾‍♀️ Woman Police Officer: Medium-Dark Skin Tone
👮🏿‍♀️ Woman Police Officer: Dark Skin Tone
🕵 Detective
🕵🏻 Detective: Light Skin Tone
🕵🏼 Detective: Medium-Light Skin Tone
🕵🏽 Detective: Medium Skin Tone
🕵🏾 Detective: Medium-Dark Skin Tone
🕵🏿 Detective: Dark Skin Tone
🕵️‍♂️ Man Detective
🕵🏻‍♂️ Man Detective: Light Skin Tone
🕵🏼‍♂️ Man Detective: Medium-Light Skin Tone
🕵🏽‍♂️ Man Detective: Medium Skin Tone
🕵🏾‍♂️ Man Detective: Medium-Dark Skin Tone
🕵🏿‍♂️ Man Detective: Dark Skin Tone
🕵️‍♀️ Woman Detective
🕵🏻‍♀️ Woman Detective: Light Skin Tone
🕵🏼‍♀️ Woman Detective: Medium-Light Skin Tone
🕵🏽‍♀️ Woman Detective: Medium Skin Tone
🕵🏾‍♀️ Woman Detective: Medium-Dark Skin Tone
🕵🏿‍♀️ Woman Detective: Dark Skin Tone
🦸‍♀️ Woman Superhero
🦸‍♂️ Man Superhero
🦹‍♀️ Woman Supervillain
🦹‍♂️ Man Supervillain
💂 Guard
💂🏻 Guard: Light Skin Tone
💂🏼 Guard: Medium-Light Skin Tone
💂🏽 Guard: Medium Skin Tone
💂🏾 Guard: Medium-Dark Skin Tone
💂🏿 Guard: Dark Skin Tone
💂‍♂️ Man Guard
💂🏻‍♂️ Man Guard: Light Skin Tone
💂🏼‍♂️ Man Guard: Medium-Light Skin Tone
💂🏽‍♂️ Man Guard: Medium Skin Tone
💂🏾‍♂️ Man Guard: Medium-Dark Skin Tone
💂🏿‍♂️ Man Guard: Dark Skin Tone
💂‍♀️ Woman Guard
💂🏻‍♀️ Woman Guard: Light Skin Tone
💂🏼‍♀️ Woman Guard: Medium-Light Skin Tone
💂🏽‍♀️ Woman Guard: Medium Skin Tone
💂🏾‍♀️ Woman Guard: Medium-Dark Skin Tone
💂🏿‍♀️ Woman Guard: Dark Skin Tone
👷 Construction Worker
👷🏻 Construction Worker: Light Skin Tone
👷🏼 Construction Worker: Medium-Light Skin Tone
👷🏽 Construction Worker: Medium Skin Tone
👷🏾 Construction Worker: Medium-Dark Skin Tone
👷🏿 Construction Worker: Dark Skin Tone
👷‍♂️ Man Construction Worker
👷🏻‍♂️ Man Construction Worker: Light Skin Tone
👷🏼‍♂️ Man Construction Worker: Medium-Light Skin Tone
👷🏽‍♂️ Man Construction Worker: Medium Skin Tone
👷🏾‍♂️ Man Construction Worker: Medium-Dark Skin Tone
👷🏿‍♂️ Man Construction Worker: Dark Skin Tone
👷‍♀️ Woman Construction Worker
👷🏻‍♀️ Woman Construction Worker: Light Skin Tone
👷🏼‍♀️ Woman Construction Worker: Medium-Light Skin Tone
👷🏽‍♀️ Woman Construction Worker: Medium Skin Tone
👷🏾‍♀️ Woman Construction Worker: Medium-Dark Skin Tone
👷🏿‍♀️ Woman Construction Worker: Dark Skin Tone
🤴 Prince
🤴🏻 Prince: Light Skin Tone
🤴🏼 Prince: Medium-Light Skin Tone
🤴🏽 Prince: Medium Skin Tone
🤴🏾 Prince: Medium-Dark Skin Tone
🤴🏿 Prince: Dark Skin Tone
👸 Princess
👸🏻 Princess: Light Skin Tone
👸🏼 Princess: Medium-Light Skin Tone
👸🏽 Princess: Medium Skin Tone
👸🏾 Princess: Medium-Dark Skin Tone
👸🏿 Princess: Dark Skin Tone
👳 Person Wearing Turban
👳🏻 Person Wearing Turban: Light Skin Tone
👳🏼 Person Wearing Turban: Medium-Light Skin Tone
👳🏽 Person Wearing Turban: Medium Skin Tone
👳🏾 Person Wearing Turban: Medium-Dark Skin Tone
👳🏿 Person Wearing Turban: Dark Skin Tone
👳‍♂️ Man Wearing Turban
👳🏻‍♂️ Man Wearing Turban: Light Skin Tone
👳🏼‍♂️ Man Wearing Turban: Medium-Light Skin Tone
👳🏽‍♂️ Man Wearing Turban: Medium Skin Tone
👳🏾‍♂️ Man Wearing Turban: Medium-Dark Skin Tone
👳🏿‍♂️ Man Wearing Turban: Dark Skin Tone
👳‍♀️ Woman Wearing Turban
👳🏻‍♀️ Woman Wearing Turban: Light Skin Tone
👳🏼‍♀️ Woman Wearing Turban: Medium-Light Skin Tone
👳🏽‍♀️ Woman Wearing Turban: Medium Skin Tone
👳🏾‍♀️ Woman Wearing Turban: Medium-Dark Skin Tone
👳🏿‍♀️ Woman Wearing Turban: Dark Skin Tone
👲 Man With Chinese Cap
👲🏻 Man With Chinese Cap: Light Skin Tone
👲🏼 Man With Chinese Cap: Medium-Light Skin Tone
👲🏽 Man With Chinese Cap: Medium Skin Tone
👲🏾 Man With Chinese Cap: Medium-Dark Skin Tone
👲🏿 Man With Chinese Cap: Dark Skin Tone
🧕 Woman With Headscarf
🧕🏻 Person With Headscarf: Light Skin Tone
🧕🏼 Person With Headscarf: Medium-Light Skin Tone
🧕🏽 Person With Headscarf: Medium Skin Tone
🧕🏾 Person With Headscarf: Medium-Dark Skin Tone
🧕🏿 Person With Headscarf: Dark Skin Tone
🧔 Bearded Person
🧔🏻 Bearded Person: Light Skin Tone
🧔🏼 Bearded Person: Medium-Light Skin Tone
🧔🏽 Bearded Person: Medium Skin Tone
🧔🏾 Bearded Person: Medium-Dark Skin Tone
🧔🏿 Bearded Person: Dark Skin Tone
👱 Blond-Haired Person
👱🏻 Blond-Haired Person: Light Skin Tone
👱🏼 Blond-Haired Person: Medium-Light Skin Tone
👱🏽 Blond-Haired Person: Medium Skin Tone
👱🏾 Blond-Haired Person: Medium-Dark Skin Tone
👱🏿 Blond-Haired Person: Dark Skin Tone
👱‍♂️ Blond-Haired Man
👱🏻‍♂️ Blond-Haired Man: Light Skin Tone
👱🏼‍♂️ Blond-Haired Man: Medium-Light Skin Tone
👱🏽‍♂️ Blond-Haired Man: Medium Skin Tone
👱🏾‍♂️ Blond-Haired Man: Medium-Dark Skin Tone
👱🏿‍♂️ Blond-Haired Man: Dark Skin Tone
👱‍♀️ Blond-Haired Woman
👱🏻‍♀️ Blond-Haired Woman: Light Skin Tone
👱🏼‍♀️ Blond-Haired Woman: Medium-Light Skin Tone
👱🏽‍♀️ Blond-Haired Woman: Medium Skin Tone
👱🏾‍♀️ Blond-Haired Woman: Medium-Dark Skin Tone
👱🏿‍♀️ Blond-Haired Woman: Dark Skin Tone
👨‍🦰 Man, Red Haired
👨🏻‍🦰 Man, Red Haired: Light Skin Tone
👨🏼‍🦰 Man, Red Haired: Medium-Light Skin Tone
👨🏽‍🦰 Man, Red Haired: Medium Skin Tone
👨🏾‍🦰 Man, Red Haired: Medium-Dark Skin Tone
👨🏿‍🦰 Man, Red Haired: Dark Skin Tone
👨‍🦱 Man, Curly Haired
👨🏻‍🦱 Man, Curly Haired: Light Skin Tone
👨🏼‍🦱 Man, Curly Haired: Medium-Light Skin Tone
👨🏽‍🦱 Man, Curly Haired: Medium Skin Tone
👨🏾‍🦱 Man, Curly Haired: Medium-Dark Skin Tone
👨🏿‍🦱 Man, Curly Haired: Dark Skin Tone
👨‍🦲 Man, Bald
👨🏻‍🦲 Man, Bald: Light Skin Tone
👨🏼‍🦲 Man, Bald: Medium-Light Skin Tone
👨🏽‍🦲 Man, Bald: Medium Skin Tone
👨🏾‍🦲 Man, Bald: Medium-Dark Skin Tone
👨🏿‍🦲 Man, Bald: Dark Skin Tone
👨‍🦳 Man, White Haired
👨🏻‍🦳 Man, White Haired: Light Skin Tone
👨🏼‍🦳 Man, White Haired: Medium-Light Skin Tone
👨🏽‍🦳 Man, White Haired: Medium Skin Tone
👨🏾‍🦳 Man, White Haired: Medium-Dark Skin Tone
👨🏿‍🦳 Man, White Haired: Dark Skin Tone
👩‍🦰 Woman, Red Haired
👩🏻‍🦰 Woman, Red Haired: Light Skin Tone
👩🏼‍🦰 Woman, Red Haired: Medium-Light Skin Tone
👩🏽‍🦰 Woman, Red Haired: Medium Skin Tone
👩🏾‍🦰 Woman, Red Haired: Medium-Dark Skin Tone
👩🏿‍🦰 Woman, Red Haired: Dark Skin Tone
👩‍🦱 Woman, Curly Haired
👩🏻‍🦱 Woman, Curly Haired: Light Skin Tone
👩🏼‍🦱 Woman, Curly Haired: Medium-Light Skin Tone
👩🏽‍🦱 Woman, Curly Haired: Medium Skin Tone
👩🏾‍🦱 Woman, Curly Haired: Medium-Dark Skin Tone
👩🏿‍🦱 Woman, Curly Haired: Dark Skin Tone
👩‍🦲 Woman, Bald
👩🏻‍🦲 Woman, Bald: Light Skin Tone
👩🏼‍🦲 Woman, Bald: Medium-Light Skin Tone
👩🏽‍🦲 Woman, Bald: Medium Skin Tone
👩🏾‍🦲 Woman, Bald: Medium-Dark Skin Tone
👩🏿‍🦲 Woman, Bald: Dark Skin Tone
👩‍🦳 Woman, White Haired
👩🏻‍🦳 Woman, White Haired: Light Skin Tone
👩🏼‍🦳 Woman, White Haired: Medium-Light Skin Tone
👩🏽‍🦳 Woman, White Haired: Medium Skin Tone
👩🏾‍🦳 Woman, White Haired: Medium-Dark Skin Tone
👩🏿‍🦳 Woman, White Haired: Dark Skin Tone
🤵 Man in Tuxedo
🤵🏻 Man in Tuxedo: Light Skin Tone
🤵🏼 Man in Tuxedo: Medium-Light Skin Tone
🤵🏽 Man in Tuxedo: Medium Skin Tone
🤵🏾 Man in Tuxedo: Medium-Dark Skin Tone
🤵🏿 Man in Tuxedo: Dark Skin Tone
👰 Bride With Veil
👰🏻 Bride With Veil: Light Skin Tone
👰🏼 Bride With Veil: Medium-Light Skin Tone
👰🏽 Bride With Veil: Medium Skin Tone
👰🏾 Bride With Veil: Medium-Dark Skin Tone
👰🏿 Bride With Veil: Dark Skin Tone
🤰 Pregnant Woman
🤰🏻 Pregnant Woman: Light Skin Tone
🤰🏼 Pregnant Woman: Medium-Light Skin Tone
🤰🏽 Pregnant Woman: Medium Skin Tone
🤰🏾 Pregnant Woman: Medium-Dark Skin Tone
🤰🏿 Pregnant Woman: Dark Skin Tone
🤱 Breast-Feeding
🤱🏻 Breast-Feeding: Light Skin Tone
🤱🏼 Breast-Feeding: Medium-Light Skin Tone
🤱🏽 Breast-Feeding: Medium Skin Tone
🤱🏾 Breast-Feeding: Medium-Dark Skin Tone
🤱🏿 Breast-Feeding: Dark Skin Tone
👼 Baby Angel
👼🏻 Baby Angel: Light Skin Tone
👼🏼 Baby Angel: Medium-Light Skin Tone
👼🏽 Baby Angel: Medium Skin Tone
👼🏾 Baby Angel: Medium-Dark Skin Tone
👼🏿 Baby Angel: Dark Skin Tone
🎅 Santa Claus
🎅🏻 Santa Claus: Light Skin Tone
🎅🏼 Santa Claus: Medium-Light Skin Tone
🎅🏽 Santa Claus: Medium Skin Tone
🎅🏾 Santa Claus: Medium-Dark Skin Tone
🎅🏿 Santa Claus: Dark Skin Tone
🤶 Mrs. Claus
🤶🏻 Mrs. Claus: Light Skin Tone
🤶🏼 Mrs. Claus: Medium-Light Skin Tone
🤶🏽 Mrs. Claus: Medium Skin Tone
🤶🏾 Mrs. Claus: Medium-Dark Skin Tone
🤶🏿 Mrs. Claus: Dark Skin Tone
🧙 Mage
🧙🏻 Mage: Light Skin Tone
🧙🏼 Mage: Medium-Light Skin Tone
🧙🏽 Mage: Medium Skin Tone
🧙🏾 Mage: Medium-Dark Skin Tone
🧙🏿 Mage: Dark Skin Tone
🧙‍♀️ Woman Mage
🧙🏻‍♀️ Woman Mage: Light Skin Tone
🧙🏼‍♀️ Woman Mage: Medium-Light Skin Tone
🧙🏽‍♀️ Woman Mage: Medium Skin Tone
🧙🏾‍♀️ Woman Mage: Medium-Dark Skin Tone
🧙🏿‍♀️ Woman Mage: Dark Skin Tone
👯🏻 Woman With Bunny Ears, Type-1-2
🧙‍♂️ Man Mage
👯🏼 Woman With Bunny Ears, Type-3
👯🏽 Woman With Bunny Ears, Type-4
🧙🏻‍♂️ Man Mage: Light Skin Tone
👯🏾 Woman With Bunny Ears, Type-5
👯🏿 Woman With Bunny Ears, Type-6
🧙🏼‍♂️ Man Mage: Medium-Light Skin Tone
👯🏻‍♂️ Men With Bunny Ears Partying, Type-1-2
👯🏼‍♂️ Men With Bunny Ears Partying, Type-3
🧙🏽‍♂️ Man Mage: Medium Skin Tone
👯🏽‍♂️ Men With Bunny Ears Partying, Type-4
👯🏾‍♂️ Men With Bunny Ears Partying, Type-5
🧙🏾‍♂️ Man Mage: Medium-Dark Skin Tone
👯🏿‍♂️ Men With Bunny Ears Partying, Type-6
🧙🏿‍♂️ Man Mage: Dark Skin Tone
👯🏻‍♀️ Women With Bunny Ears Partying, Type-1-2
🧚 Fairy
👯🏼‍♀️ Women With Bunny Ears Partying, Type-3
👯🏽‍♀️ Women With Bunny Ears Partying, Type-4
🧚🏻 Fairy: Light Skin Tone
👯🏾‍♀️ Women With Bunny Ears Partying, Type-5
🧚🏼 Fairy: Medium-Light Skin Tone
👯🏿‍♀️ Women With Bunny Ears Partying, Type-6
🧚🏽 Fairy: Medium Skin Tone
🧚🏾 Fairy: Medium-Dark Skin Tone
🧚🏿 Fairy: Dark Skin Tone
🧚‍♀️ Woman Fairy
🧚🏻‍♀️ Woman Fairy: Light Skin Tone
🧚🏼‍♀️ Woman Fairy: Medium-Light Skin Tone
🧚🏽‍♀️ Woman Fairy: Medium Skin Tone
🧚🏾‍♀️ Woman Fairy: Medium-Dark Skin Tone
👫🏻 Man and Woman Holding Hands, Type-1-2
👫🏼 Man and Woman Holding Hands, Type-3
🧚🏿‍♀️ Woman Fairy: Dark Skin Tone
👫🏽 Man and Woman Holding Hands, Type-4
👫🏾 Man and Woman Holding Hands, Type-5
🧚‍♂️ Man Fairy
👫🏿 Man and Woman Holding Hands, Type-6
🧚🏻‍♂️ Man Fairy: Light Skin Tone
👬🏻 Two Men Holding Hands, Type-1-2
👬🏼 Two Men Holding Hands, Type-3
🧚🏼‍♂️ Man Fairy: Medium-Light Skin Tone
👬🏽 Two Men Holding Hands, Type-4
👬🏾 Two Men Holding Hands, Type-5
🧚🏽‍♂️ Man Fairy: Medium Skin Tone
👬🏿 Two Men Holding Hands, Type-6
🧚🏾‍♂️ Man Fairy: Medium-Dark Skin Tone
👭🏻 Two Women Holding Hands, Type-1-2
👭🏼 Two Women Holding Hands, Type-3
🧚🏿‍♂️ Man Fairy: Dark Skin Tone
👭🏽 Two Women Holding Hands, Type-4
👭🏾 Two Women Holding Hands, Type-5
🧛 Vampire
👭🏿 Two Women Holding Hands, Type-6
🧛🏻 Vampire: Light Skin Tone
🧛🏼 Vampire: Medium-Light Skin Tone
🧛🏽 Vampire: Medium Skin Tone
🧛🏾 Vampire: Medium-Dark Skin Tone
🧛🏿 Vampire: Dark Skin Tone
🧛‍♀️ Woman Vampire
🧛🏻‍♀️ Woman Vampire: Light Skin Tone
🧛🏼‍♀️ Woman Vampire: Medium-Light Skin Tone
👪🏻 Family, Type-1-2
👪🏼 Family, Type-3
🧛🏽‍♀️ Woman Vampire: Medium Skin Tone
👪🏽 Family, Type-4
👪🏾 Family, Type-5
🧛🏾‍♀️ Woman Vampire: Medium-Dark Skin Tone
👪🏿 Family, Type-6
🧛🏿‍♀️ Woman Vampire: Dark Skin Tone
🧛‍♂️ Man Vampire
🧛🏻‍♂️ Man Vampire: Light Skin Tone
🧛🏼‍♂️ Man Vampire: Medium-Light Skin Tone
🧛🏽‍♂️ Man Vampire: Medium Skin Tone
🧛🏾‍♂️ Man Vampire: Medium-Dark Skin Tone
🧛🏿‍♂️ Man Vampire: Dark Skin Tone
🧜 Merperson
🧜🏻 Merperson: Light Skin Tone
🧜🏼 Merperson: Medium-Light Skin Tone
🧜🏽 Merperson: Medium Skin Tone
🧜🏾 Merperson: Medium-Dark Skin Tone
🧜🏿 Merperson: Dark Skin Tone
🧜‍♀️ Mermaid
🧜🏻‍♀️ Mermaid: Light Skin Tone
🧜🏼‍♀️ Mermaid: Medium-Light Skin Tone
🧜🏽‍♀️ Mermaid: Medium Skin Tone
🧜🏾‍♀️ Mermaid: Medium-Dark Skin Tone
🧜🏿‍♀️ Mermaid: Dark Skin Tone
🧜‍♂️ Merman
🧜🏻‍♂️ Merman: Light Skin Tone
🧜🏼‍♂️ Merman: Medium-Light Skin Tone
🧜🏽‍♂️ Merman: Medium Skin Tone
🧜🏾‍♂️ Merman: Medium-Dark Skin Tone
🧜🏿‍♂️ Merman: Dark Skin Tone
🧝 Elf
🧝🏻 Elf: Light Skin Tone
🧝🏼 Elf: Medium-Light Skin Tone
🧝🏽 Elf: Medium Skin Tone
🧝🏾 Elf: Medium-Dark Skin Tone
🧝🏿 Elf: Dark Skin Tone
🧝‍♀️ Woman Elf
🧝🏻‍♀️ Woman Elf: Light Skin Tone
🧝🏼‍♀️ Woman Elf: Medium-Light Skin Tone
🧝🏽‍♀️ Woman Elf: Medium Skin Tone
🧝🏾‍♀️ Woman Elf: Medium-Dark Skin Tone
🧝🏿‍♀️ Woman Elf: Dark Skin Tone
🧝‍♂️ Man Elf
🧝🏻‍♂️ Man Elf: Light Skin Tone
🧝🏼‍♂️ Man Elf: Medium-Light Skin Tone
🧝🏽‍♂️ Man Elf: Medium Skin Tone
🧝🏾‍♂️ Man Elf: Medium-Dark Skin Tone
🧝🏿‍♂️ Man Elf: Dark Skin Tone
🧞 Genie
🧞‍♀️ Woman Genie
🧞‍♂️ Man Genie
🧟 Zombie
🧟‍♀️ Woman Zombie
🧟‍♂️ Man Zombie
🙍 Person Frowning
🙍🏻 Person Frowning: Light Skin Tone
🙍🏼 Person Frowning: Medium-Light Skin Tone
🙍🏽 Person Frowning: Medium Skin Tone
🙍🏾 Person Frowning: Medium-Dark Skin Tone
🙍🏿 Person Frowning: Dark Skin Tone
🙍‍♂️ Man Frowning
🙍🏻‍♂️ Man Frowning: Light Skin Tone
🙍🏼‍♂️ Man Frowning: Medium-Light Skin Tone
🙍🏽‍♂️ Man Frowning: Medium Skin Tone
🙍🏾‍♂️ Man Frowning: Medium-Dark Skin Tone
🙍🏿‍♂️ Man Frowning: Dark Skin Tone
🙍‍♀️ Woman Frowning
🙍🏻‍♀️ Woman Frowning: Light Skin Tone
🙍🏼‍♀️ Woman Frowning: Medium-Light Skin Tone
🙍🏽‍♀️ Woman Frowning: Medium Skin Tone
🙍🏾‍♀️ Woman Frowning: Medium-Dark Skin Tone
🙍🏿‍♀️ Woman Frowning: Dark Skin Tone
🙎 Person Pouting
🙎🏻 Person Pouting: Light Skin Tone
🙎🏼 Person Pouting: Medium-Light Skin Tone
🙎🏽 Person Pouting: Medium Skin Tone
🙎🏾 Person Pouting: Medium-Dark Skin Tone
🙎🏿 Person Pouting: Dark Skin Tone
🙎‍♂️ Man Pouting
🙎🏻‍♂️ Man Pouting: Light Skin Tone
🙎🏼‍♂️ Man Pouting: Medium-Light Skin Tone
🙎🏽‍♂️ Man Pouting: Medium Skin Tone
🙎🏾‍♂️ Man Pouting: Medium-Dark Skin Tone
🙎🏿‍♂️ Man Pouting: Dark Skin Tone
🙎‍♀️ Woman Pouting
🙎🏻‍♀️ Woman Pouting: Light Skin Tone
🙎🏼‍♀️ Woman Pouting: Medium-Light Skin Tone
🙎🏽‍♀️ Woman Pouting: Medium Skin Tone
🙎🏾‍♀️ Woman Pouting: Medium-Dark Skin Tone
🙎🏿‍♀️ Woman Pouting: Dark Skin Tone
🙅 Person Gesturing No
🙅🏻 Person Gesturing No: Light Skin Tone
🙅🏼 Person Gesturing No: Medium-Light Skin Tone
🙅🏽 Person Gesturing No: Medium Skin Tone
🙅🏾 Person Gesturing No: Medium-Dark Skin Tone
🙅🏿 Person Gesturing No: Dark Skin Tone
🙅‍♂️ Man Gesturing No
🙅🏻‍♂️ Man Gesturing No: Light Skin Tone
🙅🏼‍♂️ Man Gesturing No: Medium-Light Skin Tone
🙅🏽‍♂️ Man Gesturing No: Medium Skin Tone
🙅🏾‍♂️ Man Gesturing No: Medium-Dark Skin Tone
🙅🏿‍♂️ Man Gesturing No: Dark Skin Tone
🙅‍♀️ Woman Gesturing No
🙅🏻‍♀️ Woman Gesturing No: Light Skin Tone
🙅🏼‍♀️ Woman Gesturing No: Medium-Light Skin Tone
🙅🏽‍♀️ Woman Gesturing No: Medium Skin Tone
🙅🏾‍♀️ Woman Gesturing No: Medium-Dark Skin Tone
🙅🏿‍♀️ Woman Gesturing No: Dark Skin Tone
🙆 Person Gesturing OK
🙆🏻 Person Gesturing OK: Light Skin Tone
🙆🏼 Person Gesturing OK: Medium-Light Skin Tone
🙆🏽 Person Gesturing OK: Medium Skin Tone
🙆🏾 Person Gesturing OK: Medium-Dark Skin Tone
🙆🏿 Person Gesturing OK: Dark Skin Tone
🙆‍♂️ Man Gesturing OK
🙆🏻‍♂️ Man Gesturing OK: Light Skin Tone
🙆🏼‍♂️ Man Gesturing OK: Medium-Light Skin Tone
🙆🏽‍♂️ Man Gesturing OK: Medium Skin Tone
🙆🏾‍♂️ Man Gesturing OK: Medium-Dark Skin Tone
🙆🏿‍♂️ Man Gesturing OK: Dark Skin Tone
🙆‍♀️ Woman Gesturing OK
🙆🏻‍♀️ Woman Gesturing OK: Light Skin Tone
🙆🏼‍♀️ Woman Gesturing OK: Medium-Light Skin Tone
🙆🏽‍♀️ Woman Gesturing OK: Medium Skin Tone
🙆🏾‍♀️ Woman Gesturing OK: Medium-Dark Skin Tone
🙆🏿‍♀️ Woman Gesturing OK: Dark Skin Tone
💁 Person Tipping Hand
🤝🏻 Handshake, Type-1-2
🤝🏼 Handshake, Type-3
💁🏻 Person Tipping Hand: Light Skin Tone
🤝🏽 Handshake, Type-4
💁🏼 Person Tipping Hand: Medium-Light Skin Tone
🤝🏾 Handshake, Type-5
💁🏽 Person Tipping Hand: Medium Skin Tone
🤝🏿 Handshake, Type-6
💁🏾 Person Tipping Hand: Medium-Dark Skin Tone
💁🏿 Person Tipping Hand: Dark Skin Tone
💁‍♂️ Man Tipping Hand
💁🏻‍♂️ Man Tipping Hand: Light Skin Tone
💁🏼‍♂️ Man Tipping Hand: Medium-Light Skin Tone
💁🏽‍♂️ Man Tipping Hand: Medium Skin Tone
💁🏾‍♂️ Man Tipping Hand: Medium-Dark Skin Tone
💁🏿‍♂️ Man Tipping Hand: Dark Skin Tone
💁‍♀️ Woman Tipping Hand
💁🏻‍♀️ Woman Tipping Hand: Light Skin Tone
💁🏼‍♀️ Woman Tipping Hand: Medium-Light Skin Tone
💁🏽‍♀️ Woman Tipping Hand: Medium Skin Tone
💁🏾‍♀️ Woman Tipping Hand: Medium-Dark Skin Tone
💁🏿‍♀️ Woman Tipping Hand: Dark Skin Tone
🙋 Person Raising Hand
🙋🏻 Person Raising Hand: Light Skin Tone
🙋🏼 Person Raising Hand: Medium-Light Skin Tone
🙋🏽 Person Raising Hand: Medium Skin Tone
🙋🏾 Person Raising Hand: Medium-Dark Skin Tone
🙋🏿 Person Raising Hand: Dark Skin Tone
🙋‍♂️ Man Raising Hand
🙋🏻‍♂️ Man Raising Hand: Light Skin Tone
🙋🏼‍♂️ Man Raising Hand: Medium-Light Skin Tone
🙋🏽‍♂️ Man Raising Hand: Medium Skin Tone
🙋🏾‍♂️ Man Raising Hand: Medium-Dark Skin Tone
🙋🏿‍♂️ Man Raising Hand: Dark Skin Tone
🙋‍♀️ Woman Raising Hand
🙋🏻‍♀️ Woman Raising Hand: Light Skin Tone
🙋🏼‍♀️ Woman Raising Hand: Medium-Light Skin Tone
🙋🏽‍♀️ Woman Raising Hand: Medium Skin Tone
🙋🏾‍♀️ Woman Raising Hand: Medium-Dark Skin Tone
🙋🏿‍♀️ Woman Raising Hand: Dark Skin Tone
🙇 Person Bowing
🙇🏻 Person Bowing: Light Skin Tone
🙇🏼 Person Bowing: Medium-Light Skin Tone
🙇🏽 Person Bowing: Medium Skin Tone
🙇🏾 Person Bowing: Medium-Dark Skin Tone
🙇🏿 Person Bowing: Dark Skin Tone
🙇‍♂️ Man Bowing
🙇🏻‍♂️ Man Bowing: Light Skin Tone
🙇🏼‍♂️ Man Bowing: Medium-Light Skin Tone
🙇🏽‍♂️ Man Bowing: Medium Skin Tone
🙇🏾‍♂️ Man Bowing: Medium-Dark Skin Tone
🙇🏿‍♂️ Man Bowing: Dark Skin Tone
🙇‍♀️ Woman Bowing
🙇🏻‍♀️ Woman Bowing: Light Skin Tone
🙇🏼‍♀️ Woman Bowing: Medium-Light Skin Tone
🙇🏽‍♀️ Woman Bowing: Medium Skin Tone
🙇🏾‍♀️ Woman Bowing: Medium-Dark Skin Tone
🙇🏿‍♀️ Woman Bowing: Dark Skin Tone
🤦 Person Facepalming
🤦🏻 Person Facepalming: Light Skin Tone
🤦🏼 Person Facepalming: Medium-Light Skin Tone
🤦🏽 Person Facepalming: Medium Skin Tone
🤦🏾 Person Facepalming: Medium-Dark Skin Tone
🤦🏿 Person Facepalming: Dark Skin Tone
🤦‍♂️ Man Facepalming
🤦🏻‍♂️ Man Facepalming: Light Skin Tone
🤦🏼‍♂️ Man Facepalming: Medium-Light Skin Tone
🤦🏽‍♂️ Man Facepalming: Medium Skin Tone
🤦🏾‍♂️ Man Facepalming: Medium-Dark Skin Tone
🤦🏿‍♂️ Man Facepalming: Dark Skin Tone
🤦‍♀️ Woman Facepalming
🤦🏻‍♀️ Woman Facepalming: Light Skin Tone
🤦🏼‍♀️ Woman Facepalming: Medium-Light Skin Tone
🤦🏽‍♀️ Woman Facepalming: Medium Skin Tone
🤦🏾‍♀️ Woman Facepalming: Medium-Dark Skin Tone
🤦🏿‍♀️ Woman Facepalming: Dark Skin Tone
🤷 Person Shrugging
🤷🏻 Person Shrugging: Light Skin Tone
🤷🏼 Person Shrugging: Medium-Light Skin Tone
🤷🏽 Person Shrugging: Medium Skin Tone
🤷🏾 Person Shrugging: Medium-Dark Skin Tone
🤷🏿 Person Shrugging: Dark Skin Tone
🤷‍♂️ Man Shrugging
🤷🏻‍♂️ Man Shrugging: Light Skin Tone
🤷🏼‍♂️ Man Shrugging: Medium-Light Skin Tone
🤷🏽‍♂️ Man Shrugging: Medium Skin Tone
🤷🏾‍♂️ Man Shrugging: Medium-Dark Skin Tone
🤷🏿‍♂️ Man Shrugging: Dark Skin Tone
🤷‍♀️ Woman Shrugging
🤷🏻‍♀️ Woman Shrugging: Light Skin Tone
🤷🏼‍♀️ Woman Shrugging: Medium-Light Skin Tone
🤷🏽‍♀️ Woman Shrugging: Medium Skin Tone
🤷🏾‍♀️ Woman Shrugging: Medium-Dark Skin Tone
🤷🏿‍♀️ Woman Shrugging: Dark Skin Tone
💆 Person Getting Massage
💆🏻 Person Getting Massage: Light Skin Tone
💆🏼 Person Getting Massage: Medium-Light Skin Tone
💆🏽 Person Getting Massage: Medium Skin Tone
💆🏾 Person Getting Massage: Medium-Dark Skin Tone
💆🏿 Person Getting Massage: Dark Skin Tone
💆‍♂️ Man Getting Massage
💆🏻‍♂️ Man Getting Massage: Light Skin Tone
💆🏼‍♂️ Man Getting Massage: Medium-Light Skin Tone
💆🏽‍♂️ Man Getting Massage: Medium Skin Tone
💆🏾‍♂️ Man Getting Massage: Medium-Dark Skin Tone
💆🏿‍♂️ Man Getting Massage: Dark Skin Tone
💆‍♀️ Woman Getting Massage
💆🏻‍♀️ Woman Getting Massage: Light Skin Tone
💆🏼‍♀️ Woman Getting Massage: Medium-Light Skin Tone
💆🏽‍♀️ Woman Getting Massage: Medium Skin Tone
💆🏾‍♀️ Woman Getting Massage: Medium-Dark Skin Tone
💆🏿‍♀️ Woman Getting Massage: Dark Skin Tone
💇 Person Getting Haircut
💇🏻 Person Getting Haircut: Light Skin Tone
💇🏼 Person Getting Haircut: Medium-Light Skin Tone
💇🏽 Person Getting Haircut: Medium Skin Tone
💇🏾 Person Getting Haircut: Medium-Dark Skin Tone
💇🏿 Person Getting Haircut: Dark Skin Tone
💇‍♂️ Man Getting Haircut
💇🏻‍♂️ Man Getting Haircut: Light Skin Tone
💇🏼‍♂️ Man Getting Haircut: Medium-Light Skin Tone
💇🏽‍♂️ Man Getting Haircut: Medium Skin Tone
💇🏾‍♂️ Man Getting Haircut: Medium-Dark Skin Tone
💇🏿‍♂️ Man Getting Haircut: Dark Skin Tone
💇‍♀️ Woman Getting Haircut
💇🏻‍♀️ Woman Getting Haircut: Light Skin Tone
💇🏼‍♀️ Woman Getting Haircut: Medium-Light Skin Tone
💇🏽‍♀️ Woman Getting Haircut: Medium Skin Tone
💇🏾‍♀️ Woman Getting Haircut: Medium-Dark Skin Tone
💇🏿‍♀️ Woman Getting Haircut: Dark Skin Tone
🚶 Person Walking
🚶🏻 Person Walking: Light Skin Tone
🚶🏼 Person Walking: Medium-Light Skin Tone
🚶🏽 Person Walking: Medium Skin Tone
🚶🏾 Person Walking: Medium-Dark Skin Tone
🚶🏿 Person Walking: Dark Skin Tone
🚶‍♂️ Man Walking
🚶🏻‍♂️ Man Walking: Light Skin Tone
🚶🏼‍♂️ Man Walking: Medium-Light Skin Tone
🚶🏽‍♂️ Man Walking: Medium Skin Tone
🚶🏾‍♂️ Man Walking: Medium-Dark Skin Tone
🚶🏿‍♂️ Man Walking: Dark Skin Tone
🚶‍♀️ Woman Walking
🚶🏻‍♀️ Woman Walking: Light Skin Tone
🚶🏼‍♀️ Woman Walking: Medium-Light Skin Tone
🚶🏽‍♀️ Woman Walking: Medium Skin Tone
🚶🏾‍♀️ Woman Walking: Medium-Dark Skin Tone
🚶🏿‍♀️ Woman Walking: Dark Skin Tone
🏃 Person Running
🏃🏻 Person Running: Light Skin Tone
🏃🏼 Person Running: Medium-Light Skin Tone
🏃🏽 Person Running: Medium Skin Tone
🏃🏾 Person Running: Medium-Dark Skin Tone
🏃🏿 Person Running: Dark Skin Tone
🏃‍♂️ Man Running
🏃🏻‍♂️ Man Running: Light Skin Tone
🏃🏼‍♂️ Man Running: Medium-Light Skin Tone
🏃🏽‍♂️ Man Running: Medium Skin Tone
🏃🏾‍♂️ Man Running: Medium-Dark Skin Tone
🏃🏿‍♂️ Man Running: Dark Skin Tone
🏃‍♀️ Woman Running
🏃🏻‍♀️ Woman Running: Light Skin Tone
🏃🏼‍♀️ Woman Running: Medium-Light Skin Tone
🏃🏽‍♀️ Woman Running: Medium Skin Tone
🏃🏾‍♀️ Woman Running: Medium-Dark Skin Tone
🏃🏿‍♀️ Woman Running: Dark Skin Tone
💃 Woman Dancing
💃🏻 Woman Dancing: Light Skin Tone
💃🏼 Woman Dancing: Medium-Light Skin Tone
💃🏽 Woman Dancing: Medium Skin Tone
💃🏾 Woman Dancing: Medium-Dark Skin Tone
💃🏿 Woman Dancing: Dark Skin Tone
🕺 Man Dancing
🕺🏻 Man Dancing: Light Skin Tone
🕺🏼 Man Dancing: Medium-Light Skin Tone
🕺🏽 Man Dancing: Medium Skin Tone
🕺🏾 Man Dancing: Medium-Dark Skin Tone
🕺🏿 Man Dancing: Dark Skin Tone
👯 People With Bunny Ears
👯‍♂️ Men With Bunny Ears
👯‍♀️ Women With Bunny Ears
🧖 Person in Steamy Room
🧖🏻 Person in Steamy Room: Light Skin Tone
🧖🏼 Person in Steamy Room: Medium-Light Skin Tone
🧖🏽 Person in Steamy Room: Medium Skin Tone
🧖🏾 Person in Steamy Room: Medium-Dark Skin Tone
🧖🏿 Person in Steamy Room: Dark Skin Tone
🧖‍♀️ Woman in Steamy Room
🧖🏻‍♀️ Woman in Steamy Room: Light Skin Tone
🧖🏼‍♀️ Woman in Steamy Room: Medium-Light Skin Tone
🧖🏽‍♀️ Woman in Steamy Room: Medium Skin Tone
🧖🏾‍♀️ Woman in Steamy Room: Medium-Dark Skin Tone
🧖🏿‍♀️ Woman in Steamy Room: Dark Skin Tone
🧖‍♂️ Man in Steamy Room
🧖🏻‍♂️ Man in Steamy Room: Light Skin Tone
🧖🏼‍♂️ Man in Steamy Room: Medium-Light Skin Tone
🧖🏽‍♂️ Man in Steamy Room: Medium Skin Tone
🧖🏾‍♂️ Man in Steamy Room: Medium-Dark Skin Tone
🧖🏿‍♂️ Man in Steamy Room: Dark Skin Tone
🧗 Person Climbing
🧗🏻 Person Climbing: Light Skin Tone
🧗🏼 Person Climbing: Medium-Light Skin Tone
🧗🏽 Person Climbing: Medium Skin Tone
🧗🏾 Person Climbing: Medium-Dark Skin Tone
🧗🏿 Person Climbing: Dark Skin Tone
🧗‍♀️ Woman Climbing
🧗🏻‍♀️ Woman Climbing: Light Skin Tone
🧗🏼‍♀️ Woman Climbing: Medium-Light Skin Tone
🧗🏽‍♀️ Woman Climbing: Medium Skin Tone
🧗🏾‍♀️ Woman Climbing: Medium-Dark Skin Tone
🧗🏿‍♀️ Woman Climbing: Dark Skin Tone
🧗‍♂️ Man Climbing
🧗🏻‍♂️ Man Climbing: Light Skin Tone
🧗🏼‍♂️ Man Climbing: Medium-Light Skin Tone
🧗🏽‍♂️ Man Climbing: Medium Skin Tone
🧗🏾‍♂️ Man Climbing: Medium-Dark Skin Tone
🧗🏿‍♂️ Man Climbing: Dark Skin Tone
🧘 Person in Lotus Position
🧘🏻 Person in Lotus Position: Light Skin Tone
🧘🏼 Person in Lotus Position: Medium-Light Skin Tone
🧘🏽 Person in Lotus Position: Medium Skin Tone
🧘🏾 Person in Lotus Position: Medium-Dark Skin Tone
🧘🏿 Person in Lotus Position: Dark Skin Tone
🧘‍♀️ Woman in Lotus Position
🧘🏻‍♀️ Woman in Lotus Position: Light Skin Tone
🧘🏼‍♀️ Woman in Lotus Position: Medium-Light Skin Tone
🧘🏽‍♀️ Woman in Lotus Position: Medium Skin Tone
🧘🏾‍♀️ Woman in Lotus Position: Medium-Dark Skin Tone
🧘🏿‍♀️ Woman in Lotus Position: Dark Skin Tone
🧘‍♂️ Man in Lotus Position
🧘🏻‍♂️ Man in Lotus Position: Light Skin Tone
🧘🏼‍♂️ Man in Lotus Position: Medium-Light Skin Tone
🧘🏽‍♂️ Man in Lotus Position: Medium Skin Tone
🧘🏾‍♂️ Man in Lotus Position: Medium-Dark Skin Tone
🧘🏿‍♂️ Man in Lotus Position: Dark Skin Tone
🛀 Person Taking Bath
🛀🏻 Person Taking Bath: Light Skin Tone
🛀🏼 Person Taking Bath: Medium-Light Skin Tone
🛀🏽 Person Taking Bath: Medium Skin Tone
🛀🏾 Person Taking Bath: Medium-Dark Skin Tone
🛀🏿 Person Taking Bath: Dark Skin Tone
🛌 Person in Bed
🛌🏻 Person in Bed: Light Skin Tone
🛌🏼 Person in Bed: Medium-Light Skin Tone
🛌🏽 Person in Bed: Medium Skin Tone
🛌🏾 Person in Bed: Medium-Dark Skin Tone
🛌🏿 Person in Bed: Dark Skin Tone
🕴 Man in Suit Levitating
🕴🏻 Man in Suit Levitating: Light Skin Tone
🕴🏼 Man in Suit Levitating: Medium-Light Skin Tone
🕴🏽 Man in Suit Levitating: Medium Skin Tone
🕴🏾 Man in Suit Levitating: Medium-Dark Skin Tone
🕴🏿 Man in Suit Levitating: Dark Skin Tone
🗣 Speaking Head
👤 Bust in Silhouette
👥 Busts in Silhouette
🤺 Person Fencing
🏇 Horse Racing
🏇🏻 Horse Racing: Light Skin Tone
🏇🏼 Horse Racing: Medium-Light Skin Tone
🏇🏽 Horse Racing: Medium Skin Tone
🏇🏾 Horse Racing: Medium-Dark Skin Tone
🏇🏿 Horse Racing: Dark Skin Tone
⛷ Skier
🏂 Snowboarder
🏂🏻 Snowboarder: Light Skin Tone
🏂🏼 Snowboarder: Medium-Light Skin Tone
🏂🏽 Snowboarder: Medium Skin Tone
🏂🏾 Snowboarder: Medium-Dark Skin Tone
🏂🏿 Snowboarder: Dark Skin Tone
🏌 Person Golfing
🏌🏻 Person Golfing: Light Skin Tone
🏌🏼 Person Golfing: Medium-Light Skin Tone
🏌🏽 Person Golfing: Medium Skin Tone
🏌🏾 Person Golfing: Medium-Dark Skin Tone
🏌🏿 Person Golfing: Dark Skin Tone
🏌️‍♂️ Man Golfing
🏌🏻‍♂️ Man Golfing: Light Skin Tone
🏌🏼‍♂️ Man Golfing: Medium-Light Skin Tone
🏌🏽‍♂️ Man Golfing: Medium Skin Tone
🏌🏾‍♂️ Man Golfing: Medium-Dark Skin Tone
🏌🏿‍♂️ Man Golfing: Dark Skin Tone
🏌️‍♀️ Woman Golfing
🏌🏻‍♀️ Woman Golfing: Light Skin Tone
🏌🏼‍♀️ Woman Golfing: Medium-Light Skin Tone
🏌🏽‍♀️ Woman Golfing: Medium Skin Tone
🏌🏾‍♀️ Woman Golfing: Medium-Dark Skin Tone
🏌🏿‍♀️ Woman Golfing: Dark Skin Tone
🏄 Person Surfing
🏄🏻 Person Surfing: Light Skin Tone
🏄🏼 Person Surfing: Medium-Light Skin Tone
🏄🏽 Person Surfing: Medium Skin Tone
🏄🏾 Person Surfing: Medium-Dark Skin Tone
🏄🏿 Person Surfing: Dark Skin Tone
🏄‍♂️ Man Surfing
🏄🏻‍♂️ Man Surfing: Light Skin Tone
🏄🏼‍♂️ Man Surfing: Medium-Light Skin Tone
🏄🏽‍♂️ Man Surfing: Medium Skin Tone
🏄🏾‍♂️ Man Surfing: Medium-Dark Skin Tone
🏄🏿‍♂️ Man Surfing: Dark Skin Tone
🏄‍♀️ Woman Surfing
🏄🏻‍♀️ Woman Surfing: Light Skin Tone
🏄🏼‍♀️ Woman Surfing: Medium-Light Skin Tone
🏄🏽‍♀️ Woman Surfing: Medium Skin Tone
🏄🏾‍♀️ Woman Surfing: Medium-Dark Skin Tone
🏄🏿‍♀️ Woman Surfing: Dark Skin Tone
🚣 Person Rowing Boat
🚣🏻 Person Rowing Boat: Light Skin Tone
🚣🏼 Person Rowing Boat: Medium-Light Skin Tone
🚣🏽 Person Rowing Boat: Medium Skin Tone
🚣🏾 Person Rowing Boat: Medium-Dark Skin Tone
🚣🏿 Person Rowing Boat: Dark Skin Tone
🚣‍♂️ Man Rowing Boat
🚣🏻‍♂️ Man Rowing Boat: Light Skin Tone
🚣🏼‍♂️ Man Rowing Boat: Medium-Light Skin Tone
🚣🏽‍♂️ Man Rowing Boat: Medium Skin Tone
🚣🏾‍♂️ Man Rowing Boat: Medium-Dark Skin Tone
🚣🏿‍♂️ Man Rowing Boat: Dark Skin Tone
🚣‍♀️ Woman Rowing Boat
🚣🏻‍♀️ Woman Rowing Boat: Light Skin Tone
🚣🏼‍♀️ Woman Rowing Boat: Medium-Light Skin Tone
🚣🏽‍♀️ Woman Rowing Boat: Medium Skin Tone
🚣🏾‍♀️ Woman Rowing Boat: Medium-Dark Skin Tone
🚣🏿‍♀️ Woman Rowing Boat: Dark Skin Tone
🏊 Person Swimming
🏊🏻 Person Swimming: Light Skin Tone
🏊🏼 Person Swimming: Medium-Light Skin Tone
🏊🏽 Person Swimming: Medium Skin Tone
🏊🏾 Person Swimming: Medium-Dark Skin Tone
🏊🏿 Person Swimming: Dark Skin Tone
🏊‍♂️ Man Swimming
🏊🏻‍♂️ Man Swimming: Light Skin Tone
🏊🏼‍♂️ Man Swimming: Medium-Light Skin Tone
🏊🏽‍♂️ Man Swimming: Medium Skin Tone
🏊🏾‍♂️ Man Swimming: Medium-Dark Skin Tone
🏊🏿‍♂️ Man Swimming: Dark Skin Tone
🏊‍♀️ Woman Swimming
🏊🏻‍♀️ Woman Swimming: Light Skin Tone
🏊🏼‍♀️ Woman Swimming: Medium-Light Skin Tone
🏊🏽‍♀️ Woman Swimming: Medium Skin Tone
🏊🏾‍♀️ Woman Swimming: Medium-Dark Skin Tone
🏊🏿‍♀️ Woman Swimming: Dark Skin Tone
⛹ Person Bouncing Ball
⛹🏻 Person Bouncing Ball: Light Skin Tone
⛹🏼 Person Bouncing Ball: Medium-Light Skin Tone
⛹🏽 Person Bouncing Ball: Medium Skin Tone
⛹🏾 Person Bouncing Ball: Medium-Dark Skin Tone
⛹🏿 Person Bouncing Ball: Dark Skin Tone
⛹️‍♂️ Man Bouncing Ball
⛹🏻‍♂️ Man Bouncing Ball: Light Skin Tone
⛹🏼‍♂️ Man Bouncing Ball: Medium-Light Skin Tone
⛹🏽‍♂️ Man Bouncing Ball: Medium Skin Tone
⛹🏾‍♂️ Man Bouncing Ball: Medium-Dark Skin Tone
⛹🏿‍♂️ Man Bouncing Ball: Dark Skin Tone
⛹️‍♀️ Woman Bouncing Ball
⛹🏻‍♀️ Woman Bouncing Ball: Light Skin Tone
⛹🏼‍♀️ Woman Bouncing Ball: Medium-Light Skin Tone
⛹🏽‍♀️ Woman Bouncing Ball: Medium Skin Tone
⛹🏾‍♀️ Woman Bouncing Ball: Medium-Dark Skin Tone
⛹🏿‍♀️ Woman Bouncing Ball: Dark Skin Tone
🏋 Person Lifting Weights
🏋🏻 Person Lifting Weights: Light Skin Tone
🏋🏼 Person Lifting Weights: Medium-Light Skin Tone
🏋🏽 Person Lifting Weights: Medium Skin Tone
🏋🏾 Person Lifting Weights: Medium-Dark Skin Tone
🏋🏿 Person Lifting Weights: Dark Skin Tone
🏋️‍♂️ Man Lifting Weights
🏋🏻‍♂️ Man Lifting Weights: Light Skin Tone
🏋🏼‍♂️ Man Lifting Weights: Medium-Light Skin Tone
🏋🏽‍♂️ Man Lifting Weights: Medium Skin Tone
🏋🏾‍♂️ Man Lifting Weights: Medium-Dark Skin Tone
🏋🏿‍♂️ Man Lifting Weights: Dark Skin Tone
🏋️‍♀️ Woman Lifting Weights
🏋🏻‍♀️ Woman Lifting Weights: Light Skin Tone
🏋🏼‍♀️ Woman Lifting Weights: Medium-Light Skin Tone
🏋🏽‍♀️ Woman Lifting Weights: Medium Skin Tone
🏋🏾‍♀️ Woman Lifting Weights: Medium-Dark Skin Tone
🏋🏿‍♀️ Woman Lifting Weights: Dark Skin Tone
🚴 Person Biking
🚴🏻 Person Biking: Light Skin Tone
🚴🏼 Person Biking: Medium-Light Skin Tone
🚴🏽 Person Biking: Medium Skin Tone
🚴🏾 Person Biking: Medium-Dark Skin Tone
🚴🏿 Person Biking: Dark Skin Tone
🚴‍♂️ Man Biking
🚴🏻‍♂️ Man Biking: Light Skin Tone
🚴🏼‍♂️ Man Biking: Medium-Light Skin Tone
🚴🏽‍♂️ Man Biking: Medium Skin Tone
🚴🏾‍♂️ Man Biking: Medium-Dark Skin Tone
🚴🏿‍♂️ Man Biking: Dark Skin Tone
🚴‍♀️ Woman Biking
🚴🏻‍♀️ Woman Biking: Light Skin Tone
🚴🏼‍♀️ Woman Biking: Medium-Light Skin Tone
🚴🏽‍♀️ Woman Biking: Medium Skin Tone
🚴🏾‍♀️ Woman Biking: Medium-Dark Skin Tone
🚴🏿‍♀️ Woman Biking: Dark Skin Tone
🚵 Person Mountain Biking
🚵🏻 Person Mountain Biking: Light Skin Tone
🚵🏼 Person Mountain Biking: Medium-Light Skin Tone
🚵🏽 Person Mountain Biking: Medium Skin Tone
🚵🏾 Person Mountain Biking: Medium-Dark Skin Tone
🚵🏿 Person Mountain Biking: Dark Skin Tone
🚵‍♂️ Man Mountain Biking
🚵🏻‍♂️ Man Mountain Biking: Light Skin Tone
🚵🏼‍♂️ Man Mountain Biking: Medium-Light Skin Tone
🚵🏽‍♂️ Man Mountain Biking: Medium Skin Tone
🚵🏾‍♂️ Man Mountain Biking: Medium-Dark Skin Tone
🚵🏿‍♂️ Man Mountain Biking: Dark Skin Tone
🚵‍♀️ Woman Mountain Biking
🚵🏻‍♀️ Woman Mountain Biking: Light Skin Tone
🚵🏼‍♀️ Woman Mountain Biking: Medium-Light Skin Tone
🚵🏽‍♀️ Woman Mountain Biking: Medium Skin Tone
🚵🏾‍♀️ Woman Mountain Biking: Medium-Dark Skin Tone
🚵🏿‍♀️ Woman Mountain Biking: Dark Skin Tone
🏎 Racing Car
🏍 Motorcycle
🤸 Person Cartwheeling
🤸🏻 Person Cartwheeling: Light Skin Tone
🤸🏼 Person Cartwheeling: Medium-Light Skin Tone
🤸🏽 Person Cartwheeling: Medium Skin Tone
🤸🏾 Person Cartwheeling: Medium-Dark Skin Tone
🤸🏿 Person Cartwheeling: Dark Skin Tone
🤸‍♂️ Man Cartwheeling
🤸🏻‍♂️ Man Cartwheeling: Light Skin Tone
🤸🏼‍♂️ Man Cartwheeling: Medium-Light Skin Tone
🤸🏽‍♂️ Man Cartwheeling: Medium Skin Tone
🤸🏾‍♂️ Man Cartwheeling: Medium-Dark Skin Tone
🤸🏿‍♂️ Man Cartwheeling: Dark Skin Tone
🤸‍♀️ Woman Cartwheeling
🤸🏻‍♀️ Woman Cartwheeling: Light Skin Tone
🤸🏼‍♀️ Woman Cartwheeling: Medium-Light Skin Tone
🤸🏽‍♀️ Woman Cartwheeling: Medium Skin Tone
🤸🏾‍♀️ Woman Cartwheeling: Medium-Dark Skin Tone
🤸🏿‍♀️ Woman Cartwheeling: Dark Skin Tone
🤼 People Wrestling
🤼‍♂️ Men Wrestling
🤼‍♀️ Women Wrestling
🤽 Person Playing Water Polo
🤽🏻 Person Playing Water Polo: Light Skin Tone
🤽🏼 Person Playing Water Polo: Medium-Light Skin Tone
🤽🏽 Person Playing Water Polo: Medium Skin Tone
🤽🏾 Person Playing Water Polo: Medium-Dark Skin Tone
🤽🏿 Person Playing Water Polo: Dark Skin Tone
🤽‍♂️ Man Playing Water Polo
🤽🏻‍♂️ Man Playing Water Polo: Light Skin Tone
🤽🏼‍♂️ Man Playing Water Polo: Medium-Light Skin Tone
🤽🏽‍♂️ Man Playing Water Polo: Medium Skin Tone
🤽🏾‍♂️ Man Playing Water Polo: Medium-Dark Skin Tone
🤽🏿‍♂️ Man Playing Water Polo: Dark Skin Tone
🤽‍♀️ Woman Playing Water Polo
🤼🏻 Wrestlers, Type-1-2
🤽🏻‍♀️ Woman Playing Water Polo: Light Skin Tone
🤼🏼 Wrestlers, Type-3
🤼🏽 Wrestlers, Type-4
🤽🏼‍♀️ Woman Playing Water Polo: Medium-Light Skin Tone
🤼🏾 Wrestlers, Type-5
🤼🏿 Wrestlers, Type-6
🤽🏽‍♀️ Woman Playing Water Polo: Medium Skin Tone
🤼🏻‍♂️ Men Wrestling, Type-1-2
🤽🏾‍♀️ Woman Playing Water Polo: Medium-Dark Skin Tone
🤼🏼‍♂️ Men Wrestling, Type-3
🤼🏽‍♂️ Men Wrestling, Type-4
🤼🏾‍♂️ Men Wrestling, Type-5
🤽🏿‍♀️ Woman Playing Water Polo: Dark Skin Tone
🤼🏿‍♂️ Men Wrestling, Type-6
🤾 Person Playing Handball
🤼🏻‍♀️ Women Wrestling, Type-1-2
🤾🏻 Person Playing Handball: Light Skin Tone
🤼🏼‍♀️ Women Wrestling, Type-3
🤾🏼 Person Playing Handball: Medium-Light Skin Tone
🤼🏽‍♀️ Women Wrestling, Type-4
🤾🏽 Person Playing Handball: Medium Skin Tone
🤼🏾‍♀️ Women Wrestling, Type-5
🤾🏾 Person Playing Handball: Medium-Dark Skin Tone
🤼🏿‍♀️ Women Wrestling, Type-6
🤾🏿 Person Playing Handball: Dark Skin Tone
🤾‍♂️ Man Playing Handball
🤾🏻‍♂️ Man Playing Handball: Light Skin Tone
🤾🏼‍♂️ Man Playing Handball: Medium-Light Skin Tone
🤾🏽‍♂️ Man Playing Handball: Medium Skin Tone
🤾🏾‍♂️ Man Playing Handball: Medium-Dark Skin Tone
🤾🏿‍♂️ Man Playing Handball: Dark Skin Tone
🤾‍♀️ Woman Playing Handball
🤾🏻‍♀️ Woman Playing Handball: Light Skin Tone
🤾🏼‍♀️ Woman Playing Handball: Medium-Light Skin Tone
🤾🏽‍♀️ Woman Playing Handball: Medium Skin Tone
🤾🏾‍♀️ Woman Playing Handball: Medium-Dark Skin Tone
🤾🏿‍♀️ Woman Playing Handball: Dark Skin Tone
🤹 Person Juggling
🤹🏻 Person Juggling: Light Skin Tone
🤹🏼 Person Juggling: Medium-Light Skin Tone
🤹🏽 Person Juggling: Medium Skin Tone
🤹🏾 Person Juggling: Medium-Dark Skin Tone
🤹🏿 Person Juggling: Dark Skin Tone
🤹‍♂️ Man Juggling
🤹🏻‍♂️ Man Juggling: Light Skin Tone
🤹🏼‍♂️ Man Juggling: Medium-Light Skin Tone
🤹🏽‍♂️ Man Juggling: Medium Skin Tone
🤹🏾‍♂️ Man Juggling: Medium-Dark Skin Tone
🤹🏿‍♂️ Man Juggling: Dark Skin Tone
🤹‍♀️ Woman Juggling
🤹🏻‍♀️ Woman Juggling: Light Skin Tone
🤹🏼‍♀️ Woman Juggling: Medium-Light Skin Tone
🤹🏽‍♀️ Woman Juggling: Medium Skin Tone
🤹🏾‍♀️ Woman Juggling: Medium-Dark Skin Tone
🤹🏿‍♀️ Woman Juggling: Dark Skin Tone
👫 Man and Woman Holding Hands
👬 Two Men Holding Hands
👭 Two Women Holding Hands
💏 Kiss
👩‍❤️‍💋‍👨 Kiss: Woman, Man
👨‍❤️‍💋‍👨 Kiss: Man, Man
👩‍❤️‍💋‍👩 Kiss: Woman, Woman
💑 Couple With Heart
👩‍❤️‍👨 Couple With Heart: Woman, Man
👨‍❤️‍👨 Couple With Heart: Man, Man
👩‍❤️‍👩 Couple With Heart: Woman, Woman
👪 Family
👨‍👩‍👦 Family: Man, Woman, Boy
👨‍👩‍👧 Family: Man, Woman, Girl
👨‍👩‍👧‍👦 Family: Man, Woman, Girl, Boy
👨‍👩‍👦‍👦 Family: Man, Woman, Boy, Boy
👨‍👩‍👧‍👧 Family: Man, Woman, Girl, Girl
👨‍👨‍👦 Family: Man, Man, Boy
👨‍👨‍👧 Family: Man, Man, Girl
👨‍👨‍👧‍👦 Family: Man, Man, Girl, Boy
👨‍👨‍👦‍👦 Family: Man, Man, Boy, Boy
👨‍👨‍👧‍👧 Family: Man, Man, Girl, Girl
👩‍👩‍👦 Family: Woman, Woman, Boy
👩‍👩‍👧 Family: Woman, Woman, Girl
👩‍👩‍👧‍👦 Family: Woman, Woman, Girl, Boy
👩‍👩‍👦‍👦 Family: Woman, Woman, Boy, Boy
👩‍👩‍👧‍👧 Family: Woman, Woman, Girl, Girl
👨‍👦 Family: Man, Boy
👨‍👦‍👦 Family: Man, Boy, Boy
👨‍👧 Family: Man, Girl
👨‍👧‍👦 Family: Man, Girl, Boy
👨‍👧‍👧 Family: Man, Girl, Girl
👩‍👦 Family: Woman, Boy
👩‍👦‍👦 Family: Woman, Boy, Boy
👩‍👧 Family: Woman, Girl
👩‍👧‍👦 Family: Woman, Girl, Boy
👩‍👧‍👧 Family: Woman, Girl, Girl
🤳 Selfie
🤳🏻 Selfie: Light Skin Tone
🤳🏼 Selfie: Medium-Light Skin Tone
🤳🏽 Selfie: Medium Skin Tone
🤳🏾 Selfie: Medium-Dark Skin Tone
🤳🏿 Selfie: Dark Skin Tone
💪 Flexed Biceps
💪🏻 Flexed Biceps: Light Skin Tone
💪🏼 Flexed Biceps: Medium-Light Skin Tone
💪🏽 Flexed Biceps: Medium Skin Tone
💪🏾 Flexed Biceps: Medium-Dark Skin Tone
💪🏿 Flexed Biceps: Dark Skin Tone
👈 Backhand Index Pointing Left
👈🏻 Backhand Index Pointing Left: Light Skin Tone
👈🏼 Backhand Index Pointing Left: Medium-Light Skin Tone
👈🏽 Backhand Index Pointing Left: Medium Skin Tone
👈🏾 Backhand Index Pointing Left: Medium-Dark Skin Tone
👈🏿 Backhand Index Pointing Left: Dark Skin Tone
👉 Backhand Index Pointing Right
👉🏻 Backhand Index Pointing Right: Light Skin Tone
👉🏼 Backhand Index Pointing Right: Medium-Light Skin Tone
👉🏽 Backhand Index Pointing Right: Medium Skin Tone
👉🏾 Backhand Index Pointing Right: Medium-Dark Skin Tone
👉🏿 Backhand Index Pointing Right: Dark Skin Tone
☝ Index Pointing Up
☝🏻 Index Pointing Up: Light Skin Tone
☝🏼 Index Pointing Up: Medium-Light Skin Tone
☝🏽 Index Pointing Up: Medium Skin Tone
☝🏾 Index Pointing Up: Medium-Dark Skin Tone
☝🏿 Index Pointing Up: Dark Skin Tone
👆 Backhand Index Pointing Up
👆🏻 Backhand Index Pointing Up: Light Skin Tone
👆🏼 Backhand Index Pointing Up: Medium-Light Skin Tone
👆🏽 Backhand Index Pointing Up: Medium Skin Tone
👆🏾 Backhand Index Pointing Up: Medium-Dark Skin Tone
👆🏿 Backhand Index Pointing Up: Dark Skin Tone
🖕 Middle Finger
🖕🏻 Middle Finger: Light Skin Tone
🖕🏼 Middle Finger: Medium-Light Skin Tone
🖕🏽 Middle Finger: Medium Skin Tone
🖕🏾 Middle Finger: Medium-Dark Skin Tone
🖕🏿 Middle Finger: Dark Skin Tone
👇 Backhand Index Pointing Down
👇🏻 Backhand Index Pointing Down: Light Skin Tone
👇🏼 Backhand Index Pointing Down: Medium-Light Skin Tone
👇🏽 Backhand Index Pointing Down: Medium Skin Tone
👇🏾 Backhand Index Pointing Down: Medium-Dark Skin Tone
👇🏿 Backhand Index Pointing Down: Dark Skin Tone
✌ Victory Hand
✌🏻 Victory Hand: Light Skin Tone
✌🏼 Victory Hand: Medium-Light Skin Tone
✌🏽 Victory Hand: Medium Skin Tone
✌🏾 Victory Hand: Medium-Dark Skin Tone
✌🏿 Victory Hand: Dark Skin Tone
🤞 Crossed Fingers
🤞🏻 Crossed Fingers: Light Skin Tone
🤞🏼 Crossed Fingers: Medium-Light Skin Tone
🤞🏽 Crossed Fingers: Medium Skin Tone
🤞🏾 Crossed Fingers: Medium-Dark Skin Tone
🤞🏿 Crossed Fingers: Dark Skin Tone
🖖 Vulcan Salute
🖖🏻 Vulcan Salute: Light Skin Tone
🖖🏼 Vulcan Salute: Medium-Light Skin Tone
🖖🏽 Vulcan Salute: Medium Skin Tone
🖖🏾 Vulcan Salute: Medium-Dark Skin Tone
🖖🏿 Vulcan Salute: Dark Skin Tone
🤘 Sign of the Horns
🤘🏻 Sign of the Horns: Light Skin Tone
🤘🏼 Sign of the Horns: Medium-Light Skin Tone
🤘🏽 Sign of the Horns: Medium Skin Tone
🤘🏾 Sign of the Horns: Medium-Dark Skin Tone
🤘🏿 Sign of the Horns: Dark Skin Tone
🤙 Call Me Hand
🤙🏻 Call Me Hand: Light Skin Tone
🤙🏼 Call Me Hand: Medium-Light Skin Tone
🤙🏽 Call Me Hand: Medium Skin Tone
🤙🏾 Call Me Hand: Medium-Dark Skin Tone
🤙🏿 Call Me Hand: Dark Skin Tone
🖐 Hand With Fingers Splayed
🖐🏻 Hand With Fingers Splayed: Light Skin Tone
🖐🏼 Hand With Fingers Splayed: Medium-Light Skin Tone
🖐🏽 Hand With Fingers Splayed: Medium Skin Tone
🖐🏾 Hand With Fingers Splayed: Medium-Dark Skin Tone
🖐🏿 Hand With Fingers Splayed: Dark Skin Tone
✋ Raised Hand
✋🏻 Raised Hand: Light Skin Tone
✋🏼 Raised Hand: Medium-Light Skin Tone
✋🏽 Raised Hand: Medium Skin Tone
✋🏾 Raised Hand: Medium-Dark Skin Tone
✋🏿 Raised Hand: Dark Skin Tone
👌 OK Hand
👌🏻 OK Hand: Light Skin Tone
👌🏼 OK Hand: Medium-Light Skin Tone
👌🏽 OK Hand: Medium Skin Tone
👌🏾 OK Hand: Medium-Dark Skin Tone
👌🏿 OK Hand: Dark Skin Tone
👍 Thumbs Up
👍🏻 Thumbs Up: Light Skin Tone
👍🏼 Thumbs Up: Medium-Light Skin Tone
👍🏽 Thumbs Up: Medium Skin Tone
👍🏾 Thumbs Up: Medium-Dark Skin Tone
👍🏿 Thumbs Up: Dark Skin Tone
👎 Thumbs Down
👎🏻 Thumbs Down: Light Skin Tone
👎🏼 Thumbs Down: Medium-Light Skin Tone
👎🏽 Thumbs Down: Medium Skin Tone
👎🏾 Thumbs Down: Medium-Dark Skin Tone
👎🏿 Thumbs Down: Dark Skin Tone
✊ Raised Fist
✊🏻 Raised Fist: Light Skin Tone
✊🏼 Raised Fist: Medium-Light Skin Tone
✊🏽 Raised Fist: Medium Skin Tone
✊🏾 Raised Fist: Medium-Dark Skin Tone
✊🏿 Raised Fist: Dark Skin Tone
👊 Oncoming Fist
👊🏻 Oncoming Fist: Light Skin Tone
👊🏼 Oncoming Fist: Medium-Light Skin Tone
👊🏽 Oncoming Fist: Medium Skin Tone
👊🏾 Oncoming Fist: Medium-Dark Skin Tone
👊🏿 Oncoming Fist: Dark Skin Tone
🤛 Left-Facing Fist
🤛🏻 Left-Facing Fist: Light Skin Tone
🤛🏼 Left-Facing Fist: Medium-Light Skin Tone
🤛🏽 Left-Facing Fist: Medium Skin Tone
🤛🏾 Left-Facing Fist: Medium-Dark Skin Tone
🤛🏿 Left-Facing Fist: Dark Skin Tone
🤜 Right-Facing Fist
🤜🏻 Right-Facing Fist: Light Skin Tone
🤜🏼 Right-Facing Fist: Medium-Light Skin Tone
🤜🏽 Right-Facing Fist: Medium Skin Tone
🤜🏾 Right-Facing Fist: Medium-Dark Skin Tone
🤜🏿 Right-Facing Fist: Dark Skin Tone
🤚 Raised Back of Hand
🤚🏻 Raised Back of Hand: Light Skin Tone
🤚🏼 Raised Back of Hand: Medium-Light Skin Tone
🤚🏽 Raised Back of Hand: Medium Skin Tone
🤚🏾 Raised Back of Hand: Medium-Dark Skin Tone
🤚🏿 Raised Back of Hand: Dark Skin Tone
👋 Waving Hand
👋🏻 Waving Hand: Light Skin Tone
👋🏼 Waving Hand: Medium-Light Skin Tone
👋🏽 Waving Hand: Medium Skin Tone
👋🏾 Waving Hand: Medium-Dark Skin Tone
👋🏿 Waving Hand: Dark Skin Tone
🤟 Love-You Gesture
🤟🏻 Love-You Gesture: Light Skin Tone
🤟🏼 Love-You Gesture: Medium-Light Skin Tone
🤟🏽 Love-You Gesture: Medium Skin Tone
🤟🏾 Love-You Gesture: Medium-Dark Skin Tone
🤟🏿 Love-You Gesture: Dark Skin Tone
✍ Writing Hand
✍🏻 Writing Hand: Light Skin Tone
✍🏼 Writing Hand: Medium-Light Skin Tone
✍🏽 Writing Hand: Medium Skin Tone
✍🏾 Writing Hand: Medium-Dark Skin Tone
✍🏿 Writing Hand: Dark Skin Tone
👏 Clapping Hands
👏🏻 Clapping Hands: Light Skin Tone
👏🏼 Clapping Hands: Medium-Light Skin Tone
👏🏽 Clapping Hands: Medium Skin Tone
👏🏾 Clapping Hands: Medium-Dark Skin Tone
👏🏿 Clapping Hands: Dark Skin Tone
👐 Open Hands
👐🏻 Open Hands: Light Skin Tone
👐🏼 Open Hands: Medium-Light Skin Tone
👐🏽 Open Hands: Medium Skin Tone
👐🏾 Open Hands: Medium-Dark Skin Tone
👐🏿 Open Hands: Dark Skin Tone
🙌 Raising Hands
🙌🏻 Raising Hands: Light Skin Tone
🙌🏼 Raising Hands: Medium-Light Skin Tone
🙌🏽 Raising Hands: Medium Skin Tone
🙌🏾 Raising Hands: Medium-Dark Skin Tone
🙌🏿 Raising Hands: Dark Skin Tone
🤲 Palms Up Together
🤲🏻 Palms Up Together: Light Skin Tone
🤲🏼 Palms Up Together: Medium-Light Skin Tone
🤲🏽 Palms Up Together: Medium Skin Tone
🤲🏾 Palms Up Together: Medium-Dark Skin Tone
🤲🏿 Palms Up Together: Dark Skin Tone
🙏 Folded Hands
🙏🏻 Folded Hands: Light Skin Tone
🙏🏼 Folded Hands: Medium-Light Skin Tone
🙏🏽 Folded Hands: Medium Skin Tone
🙏🏾 Folded Hands: Medium-Dark Skin Tone
🙏🏿 Folded Hands: Dark Skin Tone
🤝 Handshake
💅 Nail Polish
💅🏻 Nail Polish: Light Skin Tone
💅🏼 Nail Polish: Medium-Light Skin Tone
💅🏽 Nail Polish: Medium Skin Tone
💅🏾 Nail Polish: Medium-Dark Skin Tone
💅🏿 Nail Polish: Dark Skin Tone
👂 Ear
👂🏻 Ear: Light Skin Tone
👂🏼 Ear: Medium-Light Skin Tone
👂🏽 Ear: Medium Skin Tone
👂🏾 Ear: Medium-Dark Skin Tone
👂🏿 Ear: Dark Skin Tone
👃 Nose
👃🏻 Nose: Light Skin Tone
👃🏼 Nose: Medium-Light Skin Tone
👃🏽 Nose: Medium Skin Tone
👃🏾 Nose: Medium-Dark Skin Tone
👃🏿 Nose: Dark Skin Tone
👣 Footprints
👀 Eyes
👁 Eye
👁️‍🗨️ Eye in Speech Bubble
🧠 Brain
👅 Tongue
👄 Mouth
💋 Kiss Mark
💘 Heart With Arrow
❤ Red Heart
💓 Beating Heart
💔 Broken Heart
💕 Two Hearts
💖 Sparkling Heart
💗 Growing Heart
💙 Blue Heart
💚 Green Heart
💛 Yellow Heart
🧡 Orange Heart
💜 Purple Heart
🖤 Black Heart
💝 Heart With Ribbon
💞 Revolving Hearts
💟 Heart Decoration
❣ Heavy Heart Exclamation
💌 Love Letter
💤 Zzz
💢 Anger Symbol
💣 Bomb
💥 Collision
💦 Sweat Droplets
💨 Dashing Away
💫 Dizzy
💬 Speech Balloon
🗨 Left Speech Bubble
🗯 Right Anger Bubble
💭 Thought Balloon
🕳 Hole
👓 Glasses
🕶 Sunglasses
👔 Necktie
👕 T-Shirt
👖 Jeans
🧣 Scarf
🧤 Gloves
🧥 Coat
🧦 Socks
👗 Dress
👘 Kimono
👙 Bikini
👚 Woman’s Clothes
👛 Purse
👜 Handbag
👝 Clutch Bag
🛍 Shopping Bags
🎒 School Backpack
👞 Man’s Shoe
👟 Running Shoe
👠 High-Heeled Shoe
👡 Woman’s Sandal
👢 Woman’s Boot
👑 Crown
👒 Woman’s Hat
🎩 Top Hat
🎓 Graduation Cap
🧢 Billed Cap
⛑ Rescue Worker’s Helmet
📿 Prayer Beads
💄 Lipstick
💍 Ring
💎 Gem Stone
🐵 Monkey Face
🐒 Monkey
🦍 Gorilla
🐶 Dog Face
🐕 Dog
🐩 Poodle
🐺 Wolf Face
🦊 Fox Face
🐱 Cat Face
🐈 Cat
🦁 Lion Face
🐯 Tiger Face
🐅 Tiger
🐆 Leopard
🐴 Horse Face
🐎 Horse
🦄 Unicorn Face
🦓 Zebra
🦌 Deer
🐮 Cow Face
🐂 Ox
🐃 Water Buffalo
🐄 Cow
🐷 Pig Face
🐖 Pig
🐗 Boar
🐽 Pig Nose
🐏 Ram
🐑 Ewe
🐐 Goat
🐪 Camel
🐫 Two-Hump Camel
🦒 Giraffe
🐘 Elephant
🦏 Rhinoceros
🐭 Mouse Face
🐁 Mouse
🐀 Rat
🐹 Hamster Face
🐰 Rabbit Face
🐇 Rabbit
🐿 Chipmunk
🦔 Hedgehog
🦇 Bat
🐻 Bear Face
🐨 Koala
🐼 Panda Face
🐾 Paw Prints
🦃 Turkey
🐔 Chicken
🐓 Rooster
🐣 Hatching Chick
🐤 Baby Chick
🐥 Front-Facing Baby Chick
🐦 Bird
🐧 Penguin
🕊 Dove
🦅 Eagle
🦆 Duck
🦉 Owl
🐸 Frog Face
🐊 Crocodile
🐢 Turtle
🦎 Lizard
🐍 Snake
🐲 Dragon Face
🐉 Dragon
🦕 Sauropod
🦖 T-Rex
🐳 Spouting Whale
🐋 Whale
🐬 Dolphin
🐟 Fish
🐠 Tropical Fish
🐡 Blowfish
🦈 Shark
🐙 Octopus
🐚 Spiral Shell
🦀 Crab
🦐 Shrimp
🦑 Squid
🐌 Snail
🦋 Butterfly
🐛 Bug
🐜 Ant
🐝 Honeybee
🐞 Lady Beetle
🦗 Cricket
🕷 Spider
🕸 Spider Web
🦂 Scorpion
💐 Bouquet
🌸 Cherry Blossom
💮 White Flower
🏵 Rosette
🌹 Rose
🥀 Wilted Flower
🌺 Hibiscus
🌻 Sunflower
🌼 Blossom
🌷 Tulip
🌱 Seedling
🌲 Evergreen Tree
🌳 Deciduous Tree
🌴 Palm Tree
🌵 Cactus
🌾 Sheaf of Rice
🌿 Herb
☘ Shamrock
🍀 Four Leaf Clover
🍁 Maple Leaf
🍂 Fallen Leaf
🍃 Leaf Fluttering in Wind
🍇 Grapes
🍈 Melon
🍉 Watermelon
🍊 Tangerine
🍋 Lemon
🍌 Banana
🍍 Pineapple
🍎 Red Apple
🍏 Green Apple
🍐 Pear
🍑 Peach
🍒 Cherries
🍓 Strawberry
🥝 Kiwi Fruit
🍅 Tomato
🥥 Coconut
🥑 Avocado
🍆 Eggplant
🥔 Potato
🥕 Carrot
🌽 Ear of Corn
🌶 Hot Pepper
🥒 Cucumber
🥦 Broccoli
🍄 Mushroom
🥜 Peanuts
🌰 Chestnut
🍞 Bread
🥐 Croissant
🥖 Baguette Bread
🥨 Pretzel
🥞 Pancakes
🧀 Cheese Wedge
🍖 Meat on Bone
🍗 Poultry Leg
🥩 Cut of Meat
🥓 Bacon
🍔 Hamburger
🍟 French Fries
🍕 Pizza
🌭 Hot Dog
🥪 Sandwich
🌮 Taco
🌯 Burrito
🥙 Stuffed Flatbread
🥚 Egg
🍳 Cooking
🥘 Shallow Pan of Food
🍲 Pot of Food
🥣 Bowl With Spoon
🥗 Green Salad
🍿 Popcorn
🥫 Canned Food
🍱 Bento Box
🍘 Rice Cracker
🍙 Rice Ball
🍚 Cooked Rice
🍛 Curry Rice
🍜 Steaming Bowl
🍝 Spaghetti
🍠 Roasted Sweet Potato
🍢 Oden
🍣 Sushi
🍤 Fried Shrimp
🍥 Fish Cake With Swirl
🍡 Dango
🥟 Dumpling
🥠 Fortune Cookie
🥡 Takeout Box
🍦 Soft Ice Cream
🍧 Shaved Ice
🍨 Ice Cream
🍩 Doughnut
🍪 Cookie
🎂 Birthday Cake
🍰 Shortcake
🥧 Pie
🍫 Chocolate Bar
🍬 Candy
🍭 Lollipop
🍮 Custard
🍯 Honey Pot
🍼 Baby Bottle
🥛 Glass of Milk
☕ Hot Beverage
🍵 Teacup Without Handle
🍶 Sake
🍾 Bottle With Popping Cork
🍷 Wine Glass
🍸 Cocktail Glass
🍹 Tropical Drink
🍺 Beer Mug
🍻 Clinking Beer Mugs
🥂 Clinking Glasses
🥃 Tumbler Glass
🥤 Cup With Straw
🥢 Chopsticks
🍽 Fork and Knife With Plate
🍴 Fork and Knife
🥄 Spoon
🔪 Kitchen Knife
🏺 Amphora
🌍 Globe Showing Europe-Africa
🌎 Globe Showing Americas
🌏 Globe Showing Asia-Australia
🌐 Globe With Meridians
🗺 World Map
🗾 Map of Japan
🏔 Snow-Capped Mountain
⛰ Mountain
🌋 Volcano
🗻 Mount Fuji
🏕 Camping
🏖 Beach With Umbrella
🏜 Desert
🏝 Desert Island
🏞 National Park
🏟 Stadium
🏛 Classical Building
🏗 Building Construction
🏘 Houses
🏚 Derelict House
🏠 House
🏡 House With Garden
🏢 Office Building
🏣 Japanese Post Office
🏤 Post Office
🏥 Hospital
🏦 Bank
🏨 Hotel
🏩 Love Hotel
🏪 Convenience Store
🏫 School
🏬 Department Store
🏭 Factory
🏯 Japanese Castle
🏰 Castle
💒 Wedding
🗼 Tokyo Tower
🗽 Statue of Liberty
⛪ Church
🕌 Mosque
🕍 Synagogue
⛩ Shinto Shrine
🕋 Kaaba
⛲ Fountain
⛺ Tent
🌁 Foggy
🌃 Night With Stars
🏙 Cityscape
🌄 Sunrise Over Mountains
🌅 Sunrise
🌆 Cityscape at Dusk
🌇 Sunset
🌉 Bridge at Night
♨ Hot Springs
🌌 Milky Way
🎠 Carousel Horse
🎡 Ferris Wheel
🎢 Roller Coaster
💈 Barber Pole
🎪 Circus Tent
🚂 Locomotive
🚃 Railway Car
🚄 High-Speed Train
🚅 Bullet Train
🚆 Train
🚇 Metro
🚈 Light Rail
🚉 Station
🚊 Tram
🚝 Monorail
🚞 Mountain Railway
🚋 Tram Car
🚌 Bus
🚍 Oncoming Bus
🚎 Trolleybus
🚐 Minibus
🚑 Ambulance
🚒 Fire Engine
🚓 Police Car
🚔 Oncoming Police Car
🚕 Taxi
🚖 Oncoming Taxi
🚗 Automobile
🚘 Oncoming Automobile
🚙 Sport Utility Vehicle
🚚 Delivery Truck
🚛 Articulated Lorry
🚜 Tractor
🚲 Bicycle
🛴 Kick Scooter
🛵 Motor Scooter
🚏 Bus Stop
🛣 Motorway
🛤 Railway Track
🛢 Oil Drum
⛽ Fuel Pump
🚨 Police Car Light
🚥 Horizontal Traffic Light
🚦 Vertical Traffic Light
🛑 Stop Sign
🚧 Construction
⚓ Anchor
⛵ Sailboat
🛶 Canoe
🚤 Speedboat
🛳 Passenger Ship
⛴ Ferry
🛥 Motor Boat
🚢 Ship
✈ Airplane
🛩 Small Airplane
🛫 Airplane Departure
🛬 Airplane Arrival
💺 Seat
🚁 Helicopter
🚟 Suspension Railway
🚠 Mountain Cableway
🚡 Aerial Tramway
🛰 Satellite
🚀 Rocket
🛸 Flying Saucer
🛎 Bellhop Bell
⌛ Hourglass Done
⏳ Hourglass Not Done
⌚ Watch
⏰ Alarm Clock
⏱ Stopwatch
⏲ Timer Clock
🕰 Mantelpiece Clock
🕛 Twelve O’clock
🕧 Twelve-Thirty
🕐 One O’clock
🕜 One-Thirty
🕑 Two O’clock
🕝 Two-Thirty
🕒 Three O’clock
🕞 Three-Thirty
🕓 Four O’clock
🕟 Four-Thirty
🕔 Five O’clock
🕠 Five-Thirty
🕕 Six O’clock
🕡 Six-Thirty
🕖 Seven O’clock
🕢 Seven-Thirty
🕗 Eight O’clock
🕣 Eight-Thirty
🕘 Nine O’clock
🕤 Nine-Thirty
🕙 Ten O’clock
🕥 Ten-Thirty
🕚 Eleven O’clock
🕦 Eleven-Thirty
🌑 New Moon
🌒 Waxing Crescent Moon
🌓 First Quarter Moon
🌔 Waxing Gibbous Moon
🌕 Full Moon
🌖 Waning Gibbous Moon
🌗 Last Quarter Moon
🌘 Waning Crescent Moon
🌙 Crescent Moon
🌚 New Moon Face
🌛 First Quarter Moon Face
🌜 Last Quarter Moon Face
🌡 Thermometer
☀ Sun
🌝 Full Moon Face
🌞 Sun With Face
⭐ White Medium Star
🌟 Glowing Star
🌠 Shooting Star
☁ Cloud
⛅ Sun Behind Cloud
⛈ Cloud With Lightning and Rain
🌤 Sun Behind Small Cloud
🌥 Sun Behind Large Cloud
🌦 Sun Behind Rain Cloud
🌧 Cloud With Rain
🌨 Cloud With Snow
🌩 Cloud With Lightning
🌪 Tornado
🌫 Fog
🌬 Wind Face
🌀 Cyclone
🌈 Rainbow
🌂 Closed Umbrella
☂ Umbrella
☔ Umbrella With Rain Drops
⛱ Umbrella on Ground
⚡ High Voltage
❄ Snowflake
☃ Snowman
⛄ Snowman Without Snow
☄ Comet
🔥 Fire
💧 Droplet
🌊 Water Wave
🎃 Jack-O-Lantern
🎄 Christmas Tree
🎆 Fireworks
🎇 Sparkler
✨ Sparkles
🎈 Balloon
🎉 Party Popper
🎊 Confetti Ball
🎋 Tanabata Tree
🎍 Pine Decoration
🎎 Japanese Dolls
🎏 Carp Streamer
🎐 Wind Chime
🎑 Moon Viewing Ceremony
🎀 Ribbon
🎁 Wrapped Gift
🎗 Reminder Ribbon
🎟 Admission Tickets
🎫 Ticket
🎖 Military Medal
🏆 Trophy
🏅 Sports Medal
🥇 1st Place Medal
🥈 2nd Place Medal
🥉 3rd Place Medal
⚽ Soccer Ball
⚾ Baseball
🏀 Basketball
🏐 Volleyball
🏈 American Football
🏉 Rugby Football
🎾 Tennis
🎳 Bowling
🏏 Cricket Game
🏑 Field Hockey
🏒 Ice Hockey
🏓 Ping Pong
🏸 Badminton
🥊 Boxing Glove
🥋 Martial Arts Uniform
🥅 Goal Net
⛳ Flag in Hole
⛸ Ice Skate
🎣 Fishing Pole
🎽 Running Shirt
🎿 Skis
🛷 Sled
🥌 Curling Stone
🎯 Direct Hit
🎱 Pool 8 Ball
🔮 Crystal Ball
🎮 Video Game
🕹 Joystick
🎰 Slot Machine
🎲 Game Die
♠ Spade Suit
♥ Heart Suit
♦ Diamond Suit
♣ Club Suit
🃏 Joker
🀄 Mahjong Red Dragon
🎴 Flower Playing Cards
🎭 Performing Arts
🖼 Framed Picture
🎨 Artist Palette
🔇 Muted Speaker
🔈 Speaker Low Volume
🔉 Speaker Medium Volume
🔊 Speaker High Volume
📢 Loudspeaker
📣 Megaphone
📯 Postal Horn
🔔 Bell
🔕 Bell With Slash
🎼 Musical Score
🎵 Musical Note
🎶 Musical Notes
🎙 Studio Microphone
🎚 Level Slider
🎛 Control Knobs
🎤 Microphone
🎧 Headphone
📻 Radio
🎷 Saxophone
🎸 Guitar
🎹 Musical Keyboard
🎺 Trumpet
🎻 Violin
🥁 Drum
📱 Mobile Phone
📲 Mobile Phone With Arrow
☎ Telephone
📞 Telephone Receiver
📟 Pager
📠 Fax Machine
🔋 Battery
🔌 Electric Plug
💻 Laptop Computer
🖥 Desktop Computer
🖨 Printer
⌨ Keyboard
🖱 Computer Mouse
🖲 Trackball
💽 Computer Disk
💾 Floppy Disk
💿 Optical Disk
📀 DVD
🎥 Movie Camera
🎞 Film Frames
📽 Film Projector
🎬 Clapper Board
📺 Television
📷 Camera
📸 Camera With Flash
📹 Video Camera
📼 Videocassette
🔍 Magnifying Glass Tilted Left
🔎 Magnifying Glass Tilted Right
🕯 Candle
💡 Light Bulb
🔦 Flashlight
🏮 Red Paper Lantern
📔 Notebook With Decorative Cover
📕 Closed Book
📖 Open Book
📗 Green Book
📘 Blue Book
📙 Orange Book
📚 Books
📓 Notebook
📒 Ledger
📃 Page With Curl
📜 Scroll
📄 Page Facing Up
📰 Newspaper
🗞 Rolled-Up Newspaper
📑 Bookmark Tabs
🔖 Bookmark
🏷 Label
💰 Money Bag
💴 Yen Banknote
💵 Dollar Banknote
💶 Euro Banknote
💷 Pound Banknote
💸 Money With Wings
💳 Credit Card
💹 Chart Increasing With Yen
💱 Currency Exchange
💲 Heavy Dollar Sign
✉ Envelope
📧 E-Mail
📨 Incoming Envelope
📩 Envelope With Arrow
📤 Outbox Tray
📥 Inbox Tray
📦 Package
📫 Closed Mailbox With Raised Flag
📪 Closed Mailbox With Lowered Flag
📬 Open Mailbox With Raised Flag
📭 Open Mailbox With Lowered Flag
📮 Postbox
🗳 Ballot Box With Ballot
✏ Pencil
✒ Black Nib
🖋 Fountain Pen
🖊 Pen
🖌 Paintbrush
🖍 Crayon
📝 Memo
💼 Briefcase
📁 File Folder
📂 Open File Folder
🗂 Card Index Dividers
📅 Calendar
📆 Tear-Off Calendar
🗒 Spiral Notepad
🗓 Spiral Calendar
📇 Card Index
📈 Chart Increasing
📉 Chart Decreasing
📊 Bar Chart
📋 Clipboard
📌 Pushpin
📍 Round Pushpin
📎 Paperclip
🖇 Linked Paperclips
📏 Straight Ruler
📐 Triangular Ruler
✂ Scissors
🗃 Card File Box
🗄 File Cabinet
🗑 Wastebasket
🔒 Locked
🔓 Unlocked
🔏 Locked With Pen
🔐 Locked With Key
🔑 Key
🗝 Old Key
🔨 Hammer
⛏ Pick
⚒ Hammer and Pick
🛠 Hammer and Wrench
🗡 Dagger
⚔ Crossed Swords
🔫 Pistol
🏹 Bow and Arrow
🛡 Shield
🔧 Wrench
🔩 Nut and Bolt
⚙ Gear
🗜 Clamp
⚖ Balance Scale
🔗 Link
⛓ Chains
⚗ Alembic
🔬 Microscope
🔭 Telescope
📡 Satellite Antenna
💉 Syringe
💊 Pill
🚪 Door
🛏 Bed
🛋 Couch and Lamp
🚽 Toilet
🚿 Shower
🛁 Bathtub
🛒 Shopping Cart
🚬 Cigarette
⚰ Coffin
⚱ Funeral Urn
🗿 Moai
🏧 Atm Sign
🚮 Litter in Bin Sign
🚰 Potable Water
♿ Wheelchair Symbol
🚹 Men’s Room
🚺 Women’s Room
🚻 Restroom
🚼 Baby Symbol
🚾 Water Closet
🛂 Passport Control
🛃 Customs
🛄 Baggage Claim
🛅 Left Luggage
⚠ Warning
🚸 Children Crossing
⛔ No Entry
🚫 Prohibited
🚳 No Bicycles
🚭 No Smoking
🚯 No Littering
🚱 Non-Potable Water
🚷 No Pedestrians
📵 No Mobile Phones
🔞 No One Under Eighteen
☢ Radioactive
☣ Biohazard
⬆ Up Arrow
↗ Up-Right Arrow
➡ Right Arrow
↘ Down-Right Arrow
⬇ Down Arrow
↙ Down-Left Arrow
⬅ Left Arrow
↖ Up-Left Arrow
↕ Up-Down Arrow
↔ Left-Right Arrow
↩ Right Arrow Curving Left
↪ Left Arrow Curving Right
⤴ Right Arrow Curving Up
⤵ Right Arrow Curving Down
🔃 Clockwise Vertical Arrows
🔄 Counterclockwise Arrows Button
🔙 Back Arrow
🔚 End Arrow
🔛 On! Arrow
🔜 Soon Arrow
🔝 Top Arrow
🛐 Place of Worship
⚛ Atom Symbol
♾ Permanent Paper Sign
🕉 Om
✡ Star of David
☸ Wheel of Dharma
☯ Yin Yang
✝ Latin Cross
☦ Orthodox Cross
☪ Star and Crescent
☮ Peace Symbol
🕎 Menorah
🔯 Dotted Six-Pointed Star
♈ Aries
♉ Taurus
♊ Gemini
♋ Cancer
♌ Leo
♍ Virgo
♎ Libra
♏ Scorpio
♐ Sagittarius
♑ Capricorn
♒ Aquarius
♓ Pisces
⛎ Ophiuchus
🔀 Shuffle Tracks Button
🔁 Repeat Button
🔂 Repeat Single Button
▶ Play Button
⏩ Fast-Forward Button
⏭ Next Track Button
⏯ Play or Pause Button
◀ Reverse Button
⏪ Fast Reverse Button
⏮ Last Track Button
🔼 Upwards Button
⏫ Fast Up Button
🔽 Downwards Button
⏬ Fast Down Button
⏸ Pause Button
⏹ Stop Button
⏺ Record Button
⏏ Eject Button
🎦 Cinema
🔅 Dim Button
🔆 Bright Button
📶 Antenna Bars
📳 Vibration Mode
📴 Mobile Phone Off
♀ Female Sign
♂ Male Sign
⚕ Medical Symbol
♻ Recycling Symbol
⚜ Fleur-De-Lis
🔱 Trident Emblem
📛 Name Badge
🔰 Japanese Symbol for Beginner
⭕ Heavy Large Circle
✅ White Heavy Check Mark
☑ Ballot Box With Check
✔ Heavy Check Mark
✖ Heavy Multiplication X
❌ Cross Mark
❎ Cross Mark Button
➕ Heavy Plus Sign
➖ Heavy Minus Sign
➗ Heavy Division Sign
➰ Curly Loop
➿ Double Curly Loop
〽 Part Alternation Mark
✳ Eight-Spoked Asterisk
✴ Eight-Pointed Star
❇ Sparkle
‼ Double Exclamation Mark
⁉ Exclamation Question Mark
❓ Question Mark
❔ White Question Mark
❕ White Exclamation Mark
❗ Exclamation Mark
〰 Wavy Dash
© Copyright
® Registered
™ Trade Mark
#️⃣ Keycap Number Sign
*️⃣ Keycap Asterisk
0️⃣ Keycap Digit Zero
1️⃣ Keycap Digit One
2️⃣ Keycap Digit Two
3️⃣ Keycap Digit Three
4️⃣ Keycap Digit Four
5️⃣ Keycap Digit Five
6️⃣ Keycap Digit Six
7️⃣ Keycap Digit Seven
8️⃣ Keycap Digit Eight
9️⃣ Keycap Digit Nine
🔟 Keycap 10
💯 Hundred Points
🔠 Input Latin Uppercase
🔡 Input Latin Lowercase
🔢 Input Numbers
🔣 Input Symbols
🔤 Input Latin Letters
🅰 A Button (blood Type)
🆎 Ab Button (blood Type)
🅱 B Button (blood Type)
🆑 CL Button
🆒 Cool Button
🆓 Free Button
ℹ Information
🆔 ID Button
Ⓜ Circled M
🆕 New Button
🆖 NG Button
🅾 O Button (blood Type)
🆗 OK Button
🅿 P Button
🆘 SOS Button
🆙 Up! Button
🆚 Vs Button
🈁 Japanese “here” Button
🈂 Japanese “service Charge” Button
🈷 Japanese “monthly Amount” Button
🈶 Japanese “not Free of Charge” Button
🈯 Japanese “reserved” Button
🉐 Japanese “bargain” Button
🈹 Japanese “discount” Button
🈚 Japanese “free of Charge” Button
🈲 Japanese “prohibited” Button
🉑 Japanese “acceptable” Button
🈸 Japanese “application” Button
🈴 Japanese “passing Grade” Button
🈳 Japanese “vacancy” Button
㊗ Japanese “congratulations” Button
㊙ Japanese “secret” Button
🈺 Japanese “open for Business” Button
🈵 Japanese “no Vacancy” Button
▪ Black Small Square
▫ White Small Square
◻ White Medium Square
◼ Black Medium Square
◽ White Medium-Small Square
◾ Black Medium-Small Square
⬛ Black Large Square
⬜ White Large Square
🔶 Large Orange Diamond
🔷 Large Blue Diamond
🔸 Small Orange Diamond
🔹 Small Blue Diamond
🔺 Red Triangle Pointed Up
🔻 Red Triangle Pointed Down
💠 Diamond With a Dot
🔘 Radio Button
🔲 Black Square Button
🔳 White Square Button
⚪ White Circle
⚫ Black Circle
🔴 Red Circle
🔵 Blue Circle
🏁 Chequered Flag
🚩 Triangular Flag
🎌 Crossed Flags
🏴 Black Flag
🏳 White Flag
🏳️‍🌈 Rainbow Flag
🏴‍☠️ Pirate Flag
🇦🇨 Ascension Island
🇦🇩 Andorra
🇦🇪 United Arab Emirates
🇦🇫 Afghanistan
🇦🇬 Antigua & Barbuda
🇦🇮 Anguilla
🇦🇱 Albania
🇦🇲 Armenia
🇦🇴 Angola
🇦🇶 Antarctica
🇦🇷 Argentina
🇦🇸 American Samoa
🇦🇹 Austria
🇦🇺 Australia
🇦🇼 Aruba
🇦🇽 Åland Islands
🇦🇿 Azerbaijan
🇧🇦 Bosnia & Herzegovina
🇧🇧 Barbados
🇧🇩 Bangladesh
🇧🇪 Belgium
🇧🇫 Burkina Faso
🇧🇬 Bulgaria
🇧🇭 Bahrain
🇧🇮 Burundi
🇧🇯 Benin
🇧🇱 St. Barthélemy
🇧🇲 Bermuda
🇧🇳 Brunei
🇧🇴 Bolivia
🇧🇶 Caribbean Netherlands
🇧🇷 Brazil
🇧🇸 Bahamas
🇧🇹 Bhutan
🇧🇻 Bouvet Island
🇧🇼 Botswana
🇧🇾 Belarus
🇧🇿 Belize
🇨🇦 Canada
🇨🇨 Cocos (Keeling) Islands
🇨🇩 Congo - Kinshasa
🇨🇫 Central African Republic
🇨🇬 Congo - Brazzaville
🇨🇭 Switzerland
🇨🇮 Côte D’Ivoire
🇨🇰 Cook Islands
🇨🇱 Chile
🇨🇲 Cameroon
🇨🇳 China
🇨🇴 Colombia
🇨🇵 Clipperton Island
🇨🇷 Costa Rica
🇨🇺 Cuba
🇨🇻 Cape Verde
🇨🇼 Curaçao
🇨🇽 Christmas Island
🇨🇾 Cyprus
🇨🇿 Czechia
🇩🇪 Germany
🇩🇬 Diego Garcia
🇩🇯 Djibouti
🇩🇰 Denmark
🇩🇲 Dominica
🇩🇴 Dominican Republic
🇩🇿 Algeria
🇪🇦 Ceuta & Melilla
🇪🇨 Ecuador
🇪🇪 Estonia
🇪🇬 Egypt
🇪🇭 Western Sahara
🇪🇷 Eritrea
🇪🇸 Spain
🇪🇹 Ethiopia
🇪🇺 European Union
🇫🇮 Finland
🇫🇯 Fiji
🇫🇰 Falkland Islands
🇫🇲 Micronesia
🇫🇴 Faroe Islands
🇫🇷 France
🇬🇦 Gabon
🇬🇧 United Kingdom
🇬🇩 Grenada
🇬🇪 Georgia
🇬🇫 French Guiana
🇬🇬 Guernsey
🇬🇭 Ghana
🇬🇮 Gibraltar
🇬🇱 Greenland
🇬🇲 Gambia
🇬🇳 Guinea
🇬🇵 Guadeloupe
🇬🇶 Equatorial Guinea
🇬🇷 Greece
🇬🇸 South Georgia & South Sandwich Islands
🇬🇹 Guatemala
🇬🇺 Guam
🇬🇼 Guinea-Bissau
🇬🇾 Guyana
🇭🇰 Hong Kong Sar China
🇭🇲 Heard & Mcdonald Islands
🇭🇳 Honduras
🇭🇷 Croatia
🇭🇹 Haiti
🇭🇺 Hungary
🇮🇨 Canary Islands
🇮🇩 Indonesia
🇮🇪 Ireland
🇮🇱 Israel
🇮🇲 Isle of Man
🇮🇳 India
🇮🇴 British Indian Ocean Territory
🇮🇶 Iraq
🇮🇷 Iran
🇮🇸 Iceland
🇮🇹 Italy
🇯🇪 Jersey
🇯🇲 Jamaica
🇯🇴 Jordan
🇯🇵 Japan
🇰🇪 Kenya
🇰🇬 Kyrgyzstan
🇰🇭 Cambodia
🇰🇮 Kiribati
🇰🇲 Comoros
🇰🇳 St. Kitts & Nevis
🇰🇵 North Korea
🇰🇷 South Korea
🇰🇼 Kuwait
🇰🇾 Cayman Islands
🇰🇿 Kazakhstan
🇱🇦 Laos
🇱🇧 Lebanon
🇱🇨 St. Lucia
🇱🇮 Liechtenstein
🇱🇰 Sri Lanka
🇱🇷 Liberia
🇱🇸 Lesotho
🇱🇹 Lithuania
🇱🇺 Luxembourg
🇱🇻 Latvia
🇱🇾 Libya
🇲🇦 Morocco
🇲🇨 Monaco
🇲🇩 Moldova
🇲🇪 Montenegro
🇲🇫 St. Martin
🇲🇬 Madagascar
🇲🇭 Marshall Islands
🇲🇰 Macedonia
🇲🇱 Mali
🇲🇲 Myanmar (Burma)
🇲🇳 Mongolia
🇲🇴 Macau Sar China
🇲🇵 Northern Mariana Islands
🇲🇶 Martinique
🇲🇷 Mauritania
🇲🇸 Montserrat
🇲🇹 Malta
🇲🇺 Mauritius
🇲🇻 Maldives
🇲🇼 Malawi
🇲🇽 Mexico
🇲🇾 Malaysia
🇲🇿 Mozambique
🇳🇦 Namibia
🇳🇨 New Caledonia
🇳🇪 Niger
🇳🇫 Norfolk Island
🇳🇬 Nigeria
🇳🇮 Nicaragua
🇳🇱 Netherlands
🇳🇴 Norway
🇳🇵 Nepal
🇳🇷 Nauru
🇳🇺 Niue
🇳🇿 New Zealand
🇴🇲 Oman
🇵🇦 Panama
🇵🇪 Peru
🇵🇫 French Polynesia
🇵🇬 Papua New Guinea
🇵🇭 Philippines
🇵🇰 Pakistan
🇵🇱 Poland
🇵🇲 St. Pierre & Miquelon
🇵🇳 Pitcairn Islands
🇵🇷 Puerto Rico
🇵🇸 Palestinian Territories
🇵🇹 Portugal
🇵🇼 Palau
🇵🇾 Paraguay
🇶🇦 Qatar
🇷🇪 Réunion
🇷🇴 Romania
🇷🇸 Serbia
🇷🇺 Russia
🇷🇼 Rwanda
🇸🇦 Saudi Arabia
🇸🇧 Solomon Islands
🇸🇨 Seychelles
🇸🇩 Sudan
🇸🇪 Sweden
🇸🇬 Singapore
🇸🇭 St. Helena
🇸🇮 Slovenia
🇸🇯 Svalbard & Jan Mayen
🇸🇰 Slovakia
🇸🇱 Sierra Leone
🇸🇲 San Marino
🇸🇳 Senegal
🇸🇴 Somalia
🇸🇷 Suriname
🇸🇸 South Sudan
🇸🇹 São Tomé & Príncipe
🇸🇻 El Salvador
🇸🇽 Sint Maarten
🇸🇾 Syria
🇸🇿 Swaziland
🇹🇦 Tristan Da Cunha
🇹🇨 Turks & Caicos Islands
🇹🇩 Chad
🇹🇫 French Southern Territories
🇹🇬 Togo
🇹🇭 Thailand
🇹🇯 Tajikistan
🇹🇰 Tokelau
🇹🇱 Timor-Leste
🇹🇲 Turkmenistan
🇹🇳 Tunisia
🇹🇴 Tonga
🇹🇷 Turkey
🇹🇹 Trinidad & Tobago
🇹🇻 Tuvalu
🇹🇼 Taiwan
🇹🇿 Tanzania
🇺🇦 Ukraine
🇺🇬 Uganda
🇺🇲 U.S. Outlying Islands
🇺🇳 United Nations
🇺🇸 United States
🇺🇾 Uruguay
🇺🇿 Uzbekistan
🇻🇦 Vatican City
🇻🇨 St. Vincent & Grenadines
🇻🇪 Venezuela
🇻🇬 British Virgin Islands
🇻🇮 U.S. Virgin Islands
🇻🇳 Vietnam
🇻🇺 Vanuatu
🇼🇫 Wallis & Futuna
🇼🇸 Samoa
🇽🇰 Kosovo
🇾🇪 Yemen
🇾🇹 Mayotte
🇿🇦 South Africa
🇿🇲 Zambia
🇿🇼 Zimbabwe
🏴󠁧󠁢󠁥󠁮󠁧󠁿 England
🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland
🏴󠁧󠁢󠁷󠁬󠁳󠁿 Wales
🥆 Rifle
🤻 Modern Pentathlon
🇦 Regional Indicator Symbol Letter A
🇧 Regional Indicator Symbol Letter B
🇨 Regional Indicator Symbol Letter C
🇩 Regional Indicator Symbol Letter D
🇪 Regional Indicator Symbol Letter E
🇫 Regional Indicator Symbol Letter F
🇬 Regional Indicator Symbol Letter G
🇭 Regional Indicator Symbol Letter H
🇮 Regional Indicator Symbol Letter I
🇯 Regional Indicator Symbol Letter J
🇰 Regional Indicator Symbol Letter K
🇱 Regional Indicator Symbol Letter L
🇲 Regional Indicator Symbol Letter M
🇳 Regional Indicator Symbol Letter N
🇴 Regional Indicator Symbol Letter O
🇵 Regional Indicator Symbol Letter P
🇶 Regional Indicator Symbol Letter Q
🇷 Regional Indicator Symbol Letter R
🇸 Regional Indicator Symbol Letter S
🇹 Regional Indicator Symbol Letter T
🇺 Regional Indicator Symbol Letter U
🇻 Regional Indicator Symbol Letter V
🇼 Regional Indicator Symbol Letter W
🇽 Regional Indicator Symbol Letter X
🇾 Regional Indicator Symbol Letter Y
🇿 Regional Indicator Symbol Letter Z
🐱‍🏍 Stunt Cat
🐱‍🐉 Dino Cat
🐱‍💻 Hacker Cat
🐱‍🚀 Astro Cat
🐱‍👓 Hipster Cat
🐱‍👤 Ninja Cat
◯‍◯‍◯‍◯‍◯ Olympic Rings
🏴󠁭󠁹󠀰󠀱󠁿 Flag for Johor (MY-01)
🏴󠁮󠁥󠀸󠁿 Flag for Niamey (NE-8)
🏴󠁮󠁧󠁡󠁮󠁿 Flag for Anambra (NG-AN)
🏴󠁮󠁡󠁫󠁵󠁿 Flag for Kunene (NA-KU)
🏴󠁮󠁧󠁩󠁭󠁿 Flag for Imo (NG-IM)
🏴󠁮󠁡󠁫󠁨󠁿 Flag for Khomas (NA-KH)
🏴󠁮󠁥󠀲󠁿 Flag for Diffa (NE-2)
🏴󠁮󠁧󠁡󠁫󠁿 Flag for Akwa Ibom (NG-AK)
🏴󠁮󠁡󠁯󠁳󠁿 Flag for Omusati (NA-OS)
🏴󠁮󠁧󠁫󠁮󠁿 Flag for Kano (NG-KN)
🏴󠁮󠁧󠁧󠁯󠁿 Flag for Gombe (NG-GO)
🏴󠁮󠁧󠁡󠁢󠁿 Flag for Abia (NG-AB)
🏴󠁮󠁡󠁯󠁴󠁿 Flag for Oshikoto (NA-OT)
🏴󠁮󠁡󠁫󠁷󠁿 Flag for Kavango West (NA-KW)
🏴󠁮󠁩󠁪󠁩󠁿 Flag for Jinotega (NI-JI)
🏴󠁮󠁧󠁮󠁡󠁿 Flag for Nasarawa (NG-NA)
🏴󠁮󠁩󠁲󠁩󠁿 Flag for Rivas (NI-RI)
🏴󠁮󠁩󠁮󠁳󠁿 Flag for Nueva Segovia (NI-NS)
🏴󠁮󠁬󠁦󠁬󠁿 Flag for Flevoland (NL-FL)
🏴󠁮󠁧󠁹󠁯󠁿 Flag for Yobe (NG-YO)
🏴󠁮󠁩󠁡󠁮󠁿 Flag for Atlántico Norte (NI-AN)
🏴󠁩󠁲󠀲󠀴󠁿 Flag for Hamadan (IR-24)
🏴󠁮󠁬󠁣󠁷󠁿 Flag for Curaçao (NL-CW)
🏴󠁮󠁧󠁺󠁡󠁿 Flag for Zamfara (NG-ZA)
🏴󠁮󠁬󠁧󠁥󠁿 Flag for Gelderland (NL-GE)
🏴󠁮󠁧󠁯󠁹󠁿 Flag for Oyo (NG-OY)
🏴󠁮󠁩󠁭󠁤󠁿 Flag for Madriz (NI-MD)
🏴󠁮󠁧󠁰󠁬󠁿 Flag for Plateau (NG-PL)
🏴󠁮󠁩󠁣󠁩󠁿 Flag for Chinandega (NI-CI)
🏴󠁮󠁧󠁯󠁮󠁿 Flag for Ondo (NG-ON)
🏴󠁮󠁧󠁯󠁳󠁿 Flag for Osun (NG-OS)
🏴󠁮󠁩󠁭󠁮󠁿 Flag for Managua (NI-MN)
🏴󠁮󠁧󠁬󠁡󠁿 Flag for Lagos (NG-LA)
󠀻 Tag Semicolon
🏴󠁮󠁩󠁡󠁳󠁿 Flag for Atlántico Sur (NI-AS)
🏴󠁮󠁩󠁳󠁪󠁿 Flag for Río San Juan (NI-SJ)
󠀾 Tag Greater-Than Sign
🏴󠁮󠁩󠁢󠁯󠁿 Flag for Boaco (NI-BO)
🏴󠁮󠁩󠁧󠁲󠁿 Flag for Granada (NI-GR)
🏴󠁮󠁩󠁣󠁯󠁿 Flag for Chontales (NI-CO)
🏴󠁮󠁬󠁢󠁱󠀳󠁿 Flag for Sint Eustatius (NL-BQ3)
🏴󠁮󠁧󠁴󠁡󠁿 Flag for Taraba (NG-TA)
🏴󠁮󠁬󠁤󠁲󠁿 Flag for Drenthe (NL-DR)
🏴󠁮󠁩󠁭󠁴󠁿 Flag for Matagalpa (NI-MT)
🏴󠁮󠁬󠁧󠁲󠁿 Flag for Groningen (NL-GR)
🏴󠁮󠁩󠁣󠁡󠁿 Flag for Carazo (NI-CA)
🏴󠁮󠁬󠁦󠁲󠁿 Flag for Friesland (NL-FR)
🏴󠁮󠁧󠁫󠁷󠁿 Flag for Kwara (NG-KW)
🏴󠁮󠁩󠁥󠁳󠁿 Flag for Estelí (NI-ES)
🏴󠁮󠁬󠁵󠁴󠁿 Flag for Utrecht (NL-UT)
🏴󠁮󠁲󠀰󠀵󠁿 Flag for Baiti (NR-05)
🏴󠁮󠁬󠁺󠁨󠁿 Flag for South Holland (NL-ZH)
🏴󠁮󠁲󠀰󠀶󠁿 Flag for Boe (NR-06)
🏴󠁮󠁯󠀰󠀲󠁿 Flag for Akershus (NO-02)
🏴󠁮󠁯󠀱󠀶󠁿 Flag for Sør-Trøndelag (NO-16)
🏴󠁮󠁯󠀱󠀹󠁿 Flag for Troms (NO-19)
🏴󠁮󠁯󠀱󠀲󠁿 Flag for Hordaland (NO-12)
🏴󠁮󠁯󠀱󠀵󠁿 Flag for Møre og Romsdal (NO-15)
🏴󠁮󠁬󠁺󠁥󠁿 Flag for Zeeland (NL-ZE)
🏴󠁮󠁯󠀱󠀸󠁿 Flag for Nordland (NO-18)
🏴󠁮󠁯󠀰󠀱󠁿 Flag for Østfold (NO-01)
🏴󠁮󠁰󠀴󠁿 Flag for Purwanchal (NP-4)
🏴󠁮󠁰󠀱󠁿 Flag for Central (NP-1)
🏴󠁤󠁪󠁤󠁩󠁿 Flag for Dikhil (DJ-DI)
🏴󠁮󠁯󠀱󠀱󠁿 Flag for Rogaland (NO-11)
🏴󠁮󠁯󠀰󠀵󠁿 Flag for Oppland (NO-05)
🏴󠁮󠁯󠀰󠀸󠁿 Flag for Telemark (NO-08)
🏴󠁮󠁯󠀰󠀹󠁿 Flag for Aust-Agder (NO-09)
🏴󠁮󠁲󠀰󠀲󠁿 Flag for Anabar (NR-02)
🏴󠁮󠁯󠀰󠀶󠁿 Flag for Buskerud (NO-06)
🏴󠁮󠁯󠀰󠀴󠁿 Flag for Hedmark (NO-04)
🏴󠁮󠁯󠀰󠀷󠁿 Flag for Vestfold (NO-07)
🏴󠁮󠁲󠀰󠀴󠁿 Flag for Anibare (NR-04)
🏴󠁮󠁬󠁯󠁶󠁿 Flag for Overijssel (NL-OV)
🏴󠁮󠁯󠀰󠀳󠁿 Flag for Oslo (NO-03)
🏴󠁮󠁬󠁬󠁩󠁿 Flag for Limburg (NL-LI)
🏴󠁮󠁲󠀰󠀱󠁿 Flag for Aiwo (NR-01)
🏴󠁮󠁯󠀲󠀱󠁿 Flag for Svalbard (NO-21)
🏴󠁮󠁲󠀰󠀷󠁿 Flag for Buada (NR-07)
🏴󠁮󠁯󠀲󠀰󠁿 Flag for Finnmark (NO-20)
🏴󠁮󠁯󠀱󠀷󠁿 Flag for Nord-Trøndelag (NO-17)
🏴󠁮󠁰󠀲󠁿 Flag for Madhya Pashchimanchal (NP-2)
🏴󠁮󠁲󠀰󠀳󠁿 Flag for Anetan (NR-03)
🏴󠁮󠁰󠀳󠁿 Flag for Western (NP-3)
🏴󠁮󠁯󠀲󠀲󠁿 Flag for Jan Mayen (NO-22)
🏴󠁮󠁺󠁮󠁴󠁬󠁿 Flag for Northland (NZ-NTL)
🏴󠁯󠁭󠁤󠁡󠁿 Flag for Ad Dakhiliyah (OM-DA)
🏴󠁮󠁲󠀰󠀹󠁿 Flag for Ewa (NR-09)
🏴󠁮󠁬󠁮󠁢󠁿 Flag for North Brabant (NL-NB)
🏴󠁮󠁲󠀱󠀰󠁿 Flag for Ijuw (NR-10)
🏴󠁮󠁺󠁴󠁡󠁳󠁿 Flag for Tasman (NZ-TAS)
🏴󠁮󠁺󠁢󠁯󠁰󠁿 Flag for Bay of Plenty (NZ-BOP)
🏴󠁮󠁺󠁨󠁫󠁢󠁿 Flag for Hawke’s Bay (NZ-HKB)
🏴󠁮󠁲󠀰󠀸󠁿 Flag for Denigomodu (NR-08)
🏴󠁮󠁺󠁭󠁷󠁴󠁿 Flag for Manawatu-Wanganui (NZ-MWT)
🏴󠁮󠁺󠁷󠁫󠁯󠁿 Flag for Waikato (NZ-WKO)
🏴󠁮󠁺󠁷󠁴󠁣󠁿 Flag for West Coast (NZ-WTC)
🏴󠁯󠁭󠁳󠁪󠁿 Flag for Janub ash Sharqiyah (OM-SJ)
🏴󠁮󠁺󠁭󠁢󠁨󠁿 Flag for Marl (NZ-MBH)
🏴󠁯󠁭󠁭󠁡󠁿 Flag for Muscat (OM-MA)
🏴󠁯󠁭󠁢󠁵󠁿 Flag for Al Buraimi (OM-BU)
🏴󠁮󠁲󠀱󠀳󠁿 Flag for Uaboe (NR-13)
🏴󠁮󠁺󠁴󠁫󠁩󠁿 Flag for Taranaki (NZ-TKI)
🏴󠁯󠁭󠁳󠁳󠁿 Flag for Shamal ash Sharqiyah (OM-SS)
🏴󠁰󠁡󠀲󠁿 Flag for Coclé (PA-2)
🏴󠁮󠁲󠀱󠀱󠁿 Flag for Meneng (NR-11)
🏴󠁮󠁺󠁳󠁴󠁬󠁿 Flag for Southland (NZ-STL)
🏴󠁯󠁭󠁺󠁡󠁿 Flag for Ad Dhahirah (OM-ZA)
🏴󠁮󠁲󠀱󠀲󠁿 Flag for Nibok (NR-12)
🏴󠁮󠁺󠁣󠁡󠁮󠁿 Flag for Canterbury (NZ-CAN)
🏴󠁮󠁺󠁧󠁩󠁳󠁿 Flag for Gisborne (NZ-GIS)
🏴󠁰󠁡󠀳󠁿 Flag for Colón (PA-3)
🏴󠁯󠁭󠁭󠁵󠁿 Flag for Musandam (OM-MU)
🏴󠁯󠁭󠁢󠁳󠁿 Flag for Shamal al Batinah (OM-BS)
🏴󠁮󠁺󠁣󠁩󠁴󠁿 Flag for Chatham Islands (NZ-CIT)
🏴󠁮󠁺󠁯󠁴󠁡󠁿 Flag for Otago (NZ-OTA)
🏴󠁯󠁭󠁢󠁪󠁿 Flag for Janub al Batinah (OM-BJ)
🏴󠁯󠁭󠁺󠁵󠁿 Flag for Dhofar (OM-ZU)
🏴󠁰󠁡󠀵󠁿 Flag for Darién (PA-5)
🏴󠁰󠁥󠁣󠁡󠁬󠁿 Flag for El Callao (PE-CAL)
🏴󠁰󠁡󠀶󠁿 Flag for Herrera (PA-6)
🏴󠁰󠁡󠁫󠁹󠁿 Flag for Guna Yala (PA-KY)
🏴󠁰󠁡󠁥󠁭󠁿 Flag for Emberá (PA-EM)
🏴󠁰󠁡󠁮󠁢󠁿 Flag for Ngöbe-Buglé (PA-NB)
🏴󠁰󠁡󠀹󠁿 Flag for Veraguas (PA-9)
🏴󠁰󠁧󠁣󠁰󠁭󠁿 Flag for Central (PG-CPM)
🏴󠁰󠁥󠁬󠁯󠁲󠁿 Flag for Loreto (PE-LOR)
🏴󠁰󠁥󠁡󠁭󠁡󠁿 Flag for Amazonas (PE-AMA)
🏴󠁰󠁧󠁣󠁰󠁫󠁿 Flag for Chimbu (PG-CPK)
🏴󠁰󠁥󠁴󠁵󠁭󠁿 Flag for Tumbes (PE-TUM)
🏴󠁰󠁥󠁳󠁡󠁭󠁿 Flag for San Martín (PE-SAM)
🏴󠁰󠁥󠁪󠁵󠁮󠁿 Flag for Junín (PE-JUN)
🏴󠁰󠁡󠀱󠁿 Flag for Bocas del Toro (PA-1)
🏴󠁰󠁥󠁰󠁡󠁳󠁿 Flag for Pasco (PE-PAS)
🏴󠁰󠁥󠁬󠁭󠁡󠁿 Flag for Lima (PE-LMA)
🏴󠁰󠁡󠀴󠁿 Flag for Chiriquí (PA-4)
🏴󠁰󠁥󠁣󠁡󠁪󠁿 Flag for Cajamarca (PE-CAJ)
🏴󠁰󠁥󠁩󠁣󠁡󠁿 Flag for Ica (PE-ICA)
🏴󠁰󠁥󠁭󠁯󠁱󠁿 Flag for Moquegua (PE-MOQ)
🏴󠁰󠁥󠁬󠁡󠁬󠁿 Flag for La Libertad (PE-LAL)
🏴󠁰󠁡󠀸󠁿 Flag for Panamá (PA-8)
🏴󠁰󠁥󠁵󠁣󠁡󠁿 Flag for Ucayali (PE-UCA)
󠀨 Tag Left Parenthesis
🏴󠁰󠁥󠁰󠁩󠁵󠁿 Flag for Piura (PE-PIU)
🏴󠁰󠁥󠁰󠁵󠁮󠁿 Flag for Puno (PE-PUN)
🏴󠁰󠁥󠁣󠁵󠁳󠁿 Flag for Cusco (PE-CUS)
🏴󠁰󠁥󠁨󠁵󠁣󠁿 Flag for Huánuco (PE-HUC)
🏴󠁰󠁥󠁴󠁡󠁣󠁿 Flag for Tacna (PE-TAC)
🏴󠁰󠁡󠀷󠁿 Flag for Los Santos (PA-7)
🏴󠁰󠁥󠁬󠁡󠁭󠁿 Flag for Lambayeque (PE-LAM)
🏴󠁰󠁥󠁨󠁵󠁶󠁿 Flag for Huancavelica (PE-HUV)
🏴󠁰󠁥󠁡󠁮󠁣󠁿 Flag for Ancash (PE-ANC)
🏴󠁰󠁧󠁭󠁢󠁡󠁿 Flag for Milne Bay (PG-MBA)
🏴󠁰󠁫󠁩󠁳󠁿 Flag for Islamabad (PK-IS)
🏴󠁰󠁫󠁧󠁢󠁿 Flag for Gilgit-Baltistan (PK-GB)
🏴󠁰󠁨󠀱󠀲󠁿 Flag for Soccsksargen (PH-12)
🏴󠁰󠁧󠁧󠁰󠁫󠁿 Flag for Gulf (PG-GPK)
🏴󠁰󠁧󠁷󠁰󠁤󠁿 Flag for Western (PG-WPD)
🏴󠁰󠁨󠀰󠀲󠁿 Flag for Cagayan Valley (PH-02)
🏴󠁰󠁨󠀰󠀰󠁿 Flag for Metro Manila (PH-00)
🕴🏻‍♀️ Woman in Business Suit Levitating: Light Skin Tone
🏴󠁰󠁧󠁮󠁣󠁤󠁿 Flag for Port Moresby (PG-NCD)
🏴󠁰󠁧󠁭󠁰󠁭󠁿 Flag for Madang (PG-MPM)
🏴󠁰󠁧󠁨󠁬󠁡󠁿 Flag for Hela (PG-HLA)
🏴󠁰󠁨󠀱󠀴󠁿 Flag for Muslim Mindanao (PH-14)
🏴󠁰󠁨󠀰󠀸󠁿 Flag for Eastern Visayas (PH-08)
🏴󠁰󠁧󠁮󠁳󠁢󠁿 Flag for Bougainville (PG-NSB)
🏴󠁰󠁧󠁥󠁰󠁷󠁿 Flag for Enga (PG-EPW)
🏴󠁰󠁨󠀴󠀰󠁿 Flag for Calabarzon (PH-40)
👨🏿‍👨🏿‍👦🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁰󠁧󠁭󠁰󠁬󠁿 Flag for Morobe (PG-MPL)
🏴󠁰󠁨󠀱󠀰󠁿 Flag for Northern Mindanao (PH-10)
🏴󠁰󠁧󠁮󠁩󠁫󠁿 Flag for New Ireland (PG-NIK)
🏴󠁰󠁨󠀴󠀱󠁿 Flag for Mimaropa (PH-41)
🏴󠁭󠁹󠀰󠀶󠁿 Flag for Pahang (MY-06)
🏴󠁰󠁨󠀱󠀳󠁿 Flag for Caraga (PH-13)
🏴󠁰󠁧󠁥󠁳󠁷󠁿 Flag for East Sepik (PG-ESW)
🏴󠁰󠁨󠀰󠀶󠁿 Flag for Western Visayas (PH-06)
🏴󠁰󠁨󠀰󠀳󠁿 Flag for Central Luzon (PH-03)
🏴󠁰󠁧󠁳󠁨󠁭󠁿 Flag for Southern Highlands (PG-SHM)
🏴󠁰󠁨󠀰󠀹󠁿 Flag for Zamboanga Peninsula (PH-09)
🏴󠁰󠁧󠁳󠁡󠁮󠁿 Flag for Sandaun (PG-SAN)
🏴󠁦󠁪󠁷󠁿 Flag for Western (FJ-W)
🏴󠁰󠁧󠁪󠁷󠁫󠁿 Flag for Jiwaka (PG-JWK)
🏴󠁰󠁧󠁭󠁲󠁬󠁿 Flag for Manus (PG-MRL)
🏴󠁰󠁫󠁢󠁡󠁿 Flag for Balochistan (PK-BA)
🏴󠁰󠁨󠀱󠀱󠁿 Flag for Davao (PH-11)
🏴󠁰󠁧󠁮󠁰󠁰󠁿 Flag for Oro (PG-NPP)
🏴󠁰󠁬󠁬󠁵󠁿 Flag for Lublin (PL-LU)
🏴󠁰󠁬󠁰󠁭󠁿 Flag for Federal Capital Territory (PL-PM)
🏴󠁰󠁬󠁭󠁺󠁿 Flag for Mazovia (PL-MZ)
🏴󠁰󠁫󠁫󠁰󠁿 Flag for Khyber Pakhtunkhwa (PK-KP)
󠁝 Tag Right Square Bracket
🏴󠁰󠁬󠁫󠁰󠁿 Flag for Kuyavian-Pomerania (PL-KP)
🏴󠁰󠁫󠁪󠁫󠁿 Flag for Azad Kashmir (PK-JK)
🏴󠁰󠁫󠁳󠁤󠁿 Flag for Sindh (PK-SD)
🏴󠁰󠁳󠁲󠁢󠁨󠁿 Flag for Ramallah and al-Bireh (PS-RBH)
🏴󠁰󠁳󠁧󠁺󠁡󠁿 Flag for Gaza (PS-GZA)
🏴󠁰󠁳󠁴󠁢󠁳󠁿 Flag for Tubas (PS-TBS)
🏴󠁰󠁳󠁲󠁦󠁨󠁿 Flag for Rafah (PS-RFH)
🏴󠁰󠁳󠁨󠁢󠁮󠁿 Flag for Hebron (PS-HBN)
🏴󠁰󠁬󠁰󠁫󠁿 Flag for Subcarpathia (PL-PK)
🏴󠁰󠁬󠁳󠁬󠁿 Flag for Silesia (PL-SL)
🏴󠁰󠁬󠁷󠁰󠁿 Flag for Greater Poland (PL-WP)
🏴󠁰󠁬󠁤󠁳󠁿 Flag for Lower Silesian (PL-DS)
🏴󠁰󠁬󠁺󠁰󠁿 Flag for West Pomerania (PL-ZP)
🏴󠁰󠁳󠁫󠁹󠁳󠁿 Flag for Khan Yunis (PS-KYS)
🏴󠁰󠁬󠁬󠁤󠁿 Flag for Łódź (PL-LD)
🏴󠁰󠁳󠁪󠁥󠁮󠁿 Flag for Jenin (PS-JEN)
🏴󠁰󠁳󠁪󠁥󠁭󠁿 Flag for Jerusalem (PS-JEM)
🏴󠁰󠁳󠁳󠁬󠁴󠁿 Flag for Salfit (PS-SLT)
🏴󠁰󠁨󠀰󠀵󠁿 Flag for Bicol (PH-05)
🏴󠁰󠁳󠁴󠁫󠁭󠁿 Flag for Tulkarm (PS-TKM)
🏴󠁰󠁳󠁱󠁱󠁡󠁿 Flag for Qalqilya (PS-QQA)
🏴󠁰󠁴󠀰󠀱󠁿 Flag for Aveiro (PT-01)
🏴󠁰󠁬󠁯󠁰󠁿 Flag for Opole (PL-OP)
🏴󠁰󠁬󠁭󠁡󠁿 Flag for Lesser Poland (PL-MA)
🏴󠁰󠁳󠁮󠁢󠁳󠁿 Flag for Nablus (PS-NBS)
🏴󠁰󠁬󠁷󠁮󠁿 Flag for Warmian-Masuria (PL-WN)
🏴󠁰󠁳󠁪󠁲󠁨󠁿 Flag for Jericho (PS-JRH)
🏴󠁰󠁬󠁰󠁤󠁿 Flag for Podlaskie (PL-PD)
🏴󠁰󠁫󠁰󠁢󠁿 Flag for Punjab (PK-PB)
🏴󠁰󠁬󠁳󠁫󠁿 Flag for Świętokrzyskie (PL-SK)
🏴󠁰󠁬󠁬󠁢󠁿 Flag for Lubusz (PL-LB)
🏴󠁰󠁳󠁮󠁧󠁺󠁿 Flag for North Gaza (PS-NGZ)
🏴󠁰󠁷󠀲󠀱󠀲󠁿 Flag for Melekeok (PW-212)
🏴󠁰󠁷󠀰󠀰󠀲󠁿 Flag for Aimeliik (PW-002)
🏴󠁰󠁹󠀱󠀱󠁿 Flag for Central (PY-11)
🏴󠁰󠁴󠀰󠀷󠁿 Flag for Évora (PT-07)
🏴󠁰󠁷󠀲󠀱󠀴󠁿 Flag for Ngaraard (PW-214)
🏴󠁰󠁹󠀱󠀲󠁿 Flag for Ñeembucú (PY-12)
🏴󠁰󠁴󠀱󠀷󠁿 Flag for Vila Real (PT-17)
🏴󠁰󠁴󠀱󠀱󠁿 Flag for Lisbon (PT-11)
🏴󠁰󠁷󠀰󠀰󠀴󠁿 Flag for Airai (PW-004)
🏴󠁰󠁹󠀱󠀳󠁿 Flag for Amambay (PY-13)
🏴󠁰󠁷󠀲󠀲󠀴󠁿 Flag for Ngatpang (PW-224)
🏴󠁰󠁴󠀱󠀲󠁿 Flag for Portalegre (PT-12)
🏴󠁰󠁷󠀳󠀷󠀰󠁿 Flag for Sonsorol (PW-370)
🏴󠁰󠁴󠀱󠀳󠁿 Flag for Porto (PT-13)
🏴󠁰󠁴󠀰󠀶󠁿 Flag for Coimbra (PT-06)
🏴󠁰󠁷󠀲󠀲󠀲󠁿 Flag for Ngardmau (PW-222)
🏴󠁰󠁴󠀰󠀸󠁿 Flag for Faro (PT-08)
🏴󠁰󠁴󠀰󠀳󠁿 Flag for Braga (PT-03)
🏴󠁰󠁴󠀱󠀶󠁿 Flag for Viana do Castelo (PT-16)
🏴󠁰󠁹󠀱󠀴󠁿 Flag for Canindeyú (PY-14)
🏴󠁰󠁴󠀱󠀰󠁿 Flag for Leiria (PT-10)
🏴󠁰󠁴󠀰󠀴󠁿 Flag for Bragança (PT-04)
🏴󠁰󠁴󠀰󠀵󠁿 Flag for Castelo Branco (PT-05)
🏴󠁰󠁴󠀱󠀴󠁿 Flag for Santarém (PT-14)
🏴󠁰󠁷󠀲󠀲󠀷󠁿 Flag for Ngeremlengui (PW-227)
🏴󠁰󠁷󠀳󠀵󠀰󠁿 Flag for Peleliu (PW-350)
🏴󠁰󠁷󠀱󠀵󠀰󠁿 Flag for Koror (PW-150)
🏴󠁰󠁹󠀱󠀰󠁿 Flag for Alto Paraná (PY-10)
🏴󠁰󠁷󠀰󠀱󠀰󠁿 Flag for Angaur (PW-010)
🏴󠁰󠁷󠀰󠀵󠀰󠁿 Flag for Hatohobei (PW-050)
🏴󠁰󠁹󠀱󠀵󠁿 Flag for Presidente Hayes (PY-15)
🏴󠁰󠁴󠀱󠀵󠁿 Flag for Setúbal (PT-15)
🏴󠁰󠁷󠀲󠀲󠀶󠁿 Flag for Ngchesar (PW-226)
🏴󠁰󠁴󠀰󠀹󠁿 Flag for Guarda (PT-09)
🏴󠁲󠁯󠁢󠁺󠁿 Flag for Buzău (RO-BZ)
🏴󠁰󠁹󠀲󠁿 Flag for San Pedro (PY-2)
🏴󠁰󠁹󠀵󠁿 Flag for Caaguazú (PY-5)
🏴󠁰󠁹󠀴󠁿 Flag for Guairá (PY-4)
🏴󠁲󠁯󠁣󠁴󠁿 Flag for Constanța (RO-CT)
🏴󠁰󠁹󠀷󠁿 Flag for Itapúa (PY-7)
🏴󠁲󠁯󠁢󠁲󠁿 Flag for Brăila (RO-BR)
🏴󠁰󠁹󠀶󠁿 Flag for Caazapá (PY-6)
🏴󠁱󠁡󠁫󠁨󠁿 Flag for Al Khor (QA-KH)
🏴󠁲󠁯󠁢󠁨󠁿 Flag for Bihor (RO-BH)
🏴󠁲󠁯󠁨󠁤󠁿 Flag for Hunedoara (RO-HD)
🏴󠁲󠁯󠁣󠁪󠁿 Flag for Cluj (RO-CJ)
🏴󠁲󠁯󠁢󠁿 Flag for Bucharest (RO-B)
🏴󠁰󠁹󠀳󠁿 Flag for Cordillera (PY-3)
🏴󠁱󠁡󠁭󠁳󠁿 Flag for Madinat ash Shamal (QA-MS)
🏴󠁰󠁹󠁡󠁳󠁵󠁿 Flag for Asunción (PY-ASU)
🏴󠁲󠁯󠁨󠁲󠁿 Flag for Harghita (RO-HR)
🏴󠁲󠁯󠁢󠁣󠁿 Flag for Bacău (RO-BC)
🏴󠁲󠁯󠁤󠁪󠁿 Flag for Dolj (RO-DJ)
🏴󠁱󠁡󠁺󠁡󠁿 Flag for Al Daayen (QA-ZA)
🏴󠁲󠁯󠁢󠁮󠁿 Flag for Bistriţa-Năsăud (RO-BN)
🏴󠁲󠁯󠁡󠁢󠁿 Flag for Alba (RO-AB)
🏴󠁭󠁸󠁣󠁨󠁰󠁿 Flag for Chiapas (MX-CHP)
🏴󠁰󠁹󠀱󠁿 Flag for Concepción (PY-1)
🏴󠁲󠁯󠁧󠁬󠁿 Flag for Galați (RO-GL)
🏴󠁲󠁯󠁧󠁲󠁿 Flag for Giurgiu (RO-GR)
🏴󠁰󠁹󠀱󠀹󠁿 Flag for Boquerón (PY-19)
🏴󠁰󠁹󠀸󠁿 Flag for Misiones (PY-8)
🏴󠁰󠁹󠀹󠁿 Flag for Paraguarí (PY-9)
🏴󠁱󠁡󠁲󠁡󠁿 Flag for Al Rayyan (QA-RA)
🏴󠁲󠁯󠁣󠁶󠁿 Flag for Covasna (RO-CV)
🏴󠁲󠁯󠁤󠁢󠁿 Flag for Dâmbovița (RO-DB)
🏴󠁲󠁯󠁣󠁳󠁿 Flag for Caraș-Severin (RO-CS)
🏴󠁲󠁯󠁡󠁲󠁿 Flag for Arad (RO-AR)
🏴󠁲󠁯󠁢󠁴󠁿 Flag for Botoşani (RO-BT)
🏴󠁱󠁡󠁷󠁡󠁿 Flag for Al Wakrah (QA-WA)
🏴󠁲󠁯󠁡󠁧󠁿 Flag for Argeș (RO-AG)
🏴󠁢󠁲󠁧󠁯󠁿 Flag for Goiás (BR-GO)
🏴󠁲󠁯󠁶󠁬󠁿 Flag for Vâlcea (RO-VL)
🏴󠁲󠁯󠁩󠁳󠁿 Flag for Iași (RO-IS)
🏴󠁲󠁳󠀱󠀲󠁿 Flag for Šumadija (RS-12)
🏴󠁲󠁳󠀱󠀴󠁿 Flag for Bor (RS-14)
🏴󠁲󠁯󠁴󠁲󠁿 Flag for Teleorman (RO-TR)
🏴󠁲󠁯󠁶󠁮󠁿 Flag for Vrancea (RO-VN)
🏴󠁲󠁯󠁳󠁶󠁿 Flag for Suceava (RO-SV)
🏴󠁲󠁳󠀲󠀰󠁿 Flag for Nišava (RS-20)
🏴󠁲󠁳󠀱󠀸󠁿 Flag for Raška (RS-18)
🏴󠁲󠁯󠁭󠁨󠁿 Flag for Mehedinți (RO-MH)
🏴󠁲󠁳󠀰󠀸󠁿 Flag for Mačva (RS-08)
🏴󠁲󠁯󠁩󠁬󠁿 Flag for Ialomița (RO-IL)
🏴󠁲󠁯󠁰󠁨󠁿 Flag for Prahova (RO-PH)
🏴󠁲󠁳󠀱󠀱󠁿 Flag for Braničevo (RS-11)
🏴󠁲󠁯󠁩󠁦󠁿 Flag for Ilfov (RO-IF)
🏴󠁲󠁳󠀱󠀵󠁿 Flag for Zaječar (RS-15)
🏴󠁲󠁳󠁶󠁯󠁿 Flag for Vojvodina (RS-VO)
🏴󠁲󠁳󠀱󠀳󠁿 Flag for Pomoravlje (RS-13)
🏴󠁲󠁯󠁮󠁴󠁿 Flag for Neamţ (RO-NT)
🏴󠁲󠁵󠁡󠁤󠁿 Flag for Adygea (RU-AD)
🏴󠁲󠁳󠀲󠀱󠁿 Flag for Toplica (RS-21)
🏴󠁲󠁯󠁳󠁪󠁿 Flag for Sălaj (RO-SJ)
🏴󠁲󠁯󠁭󠁳󠁿 Flag for Mureş (RO-MS)
🏴󠁲󠁯󠁯󠁴󠁿 Flag for Olt (RO-OT)
🏴󠁲󠁳󠀲󠀲󠁿 Flag for Pirot (RS-22)
🏴󠁲󠁳󠀱󠀹󠁿 Flag for Rasina (RS-19)
🏴󠁲󠁯󠁭󠁭󠁿 Flag for Maramureş (RO-MM)
🏴󠁲󠁯󠁳󠁭󠁿 Flag for Satu Mare (RO-SM)
🏴󠁲󠁳󠀲󠀴󠁿 Flag for Pčinja (RS-24)
🏴󠁲󠁯󠁶󠁳󠁿 Flag for Vaslui (RO-VS)
🏴󠁲󠁵󠁡󠁬󠁿 Flag for Altai (RU-AL)
🏴󠁲󠁳󠁫󠁭󠁿 Flag for Kosovo-Metohija (RS-KM)
🏴󠁲󠁳󠀱󠀰󠁿 Flag for Podunavlje (RS-10)
🏴󠁲󠁳󠀱󠀶󠁿 Flag for Zlatibor (RS-16)
🏴󠁲󠁳󠀱󠀷󠁿 Flag for Moravica (RS-17)
🏴󠁲󠁳󠀲󠀳󠁿 Flag for Jablanica (RS-23)
🏴󠁲󠁯󠁴󠁬󠁿 Flag for Tulcea (RO-TL)
🏴󠁲󠁳󠀰󠀰󠁿 Flag for Beograd (RS-00)
🏴󠁲󠁯󠁴󠁭󠁿 Flag for Timiș (RO-TM)
🏴󠁲󠁳󠀰󠀹󠁿 Flag for Kolubara (RS-09)
🏴󠁲󠁵󠁩󠁶󠁡󠁿 Flag for Ivanovo (RU-IVA)
👩🏼‍👦🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁲󠁵󠁬󠁩󠁰󠁿 Flag for Lipetsk (RU-LIP)
🏴󠁲󠁵󠁢󠁥󠁬󠁿 Flag for Belgorod (RU-BEL)
🏴󠁲󠁵󠁫󠁯󠁿 Flag for Komi (RU-KO)
🏴󠁲󠁵󠁫󠁢󠁿 Flag for Kabardino-Balkar (RU-KB)
🏴󠁲󠁵󠁫󠁬󠁿 Flag for Kalmykia (RU-KL)
🏴󠁲󠁵󠁫󠁩󠁲󠁿 Flag for Kirov (RU-KIR)
🏴󠁲󠁵󠁫󠁧󠁮󠁿 Flag for Kurgan (RU-KGN)
🏴󠁲󠁵󠁩󠁮󠁿 Flag for Ingushetia (RU-IN)
🏴󠁲󠁵󠁫󠁣󠁿 Flag for Karachay-Cherkess (RU-KC)
🏴󠁲󠁵󠁫󠁧󠁤󠁿 Flag for Kaliningrad (RU-KGD)
🏴󠁲󠁵󠁫󠁡󠁭󠁿 Flag for Kamchatka Krai (RU-KAM)
🏴󠁲󠁵󠁣󠁨󠁥󠁿 Flag for Chelyabinsk (RU-CHE)
🏴󠁲󠁵󠁫󠁨󠁭󠁿 Flag for Khanty-Mansi (RU-KHM)
🏴󠁲󠁵󠁫󠁲󠁿 Flag for Karelia (RU-KR)
🏴󠁲󠁵󠁫󠁥󠁭󠁿 Flag for Kemerovo (RU-KEM)
🏴󠁲󠁵󠁡󠁳󠁴󠁿 Flag for Astrakhan (RU-AST)
🏴󠁲󠁵󠁫󠁫󠁿 Flag for Khakassia (RU-KK)
🏴󠁲󠁵󠁭󠁯󠁿 Flag for Mordovia (RU-MO)
🏴󠁲󠁵󠁣󠁵󠁿 Flag for Chuvash (RU-CU)
🏴󠁲󠁵󠁫󠁤󠁡󠁿 Flag for Krasnodar Krai (RU-KDA)
🏴󠁲󠁵󠁫󠁨󠁡󠁿 Flag for Khabarovsk Krai (RU-KHA)
🏴󠁲󠁵󠁫󠁲󠁳󠁿 Flag for Kursk (RU-KRS)
🏴󠁲󠁵󠁭󠁥󠁿 Flag for Mari El (RU-ME)
🏴󠁲󠁵󠁩󠁲󠁫󠁿 Flag for Irkutsk (RU-IRK)
🏴󠁲󠁵󠁣󠁨󠁵󠁿 Flag for Chukotka Okrug (RU-CHU)
🏴󠁲󠁵󠁡󠁭󠁵󠁿 Flag for Amur (RU-AMU)
🏴󠁲󠁵󠁢󠁡󠁿 Flag for Bashkortostan (RU-BA)
🏴󠁲󠁵󠁫󠁬󠁵󠁿 Flag for Kaluga (RU-KLU)
🏴󠁲󠁵󠁫󠁹󠁡󠁿 Flag for Krasnoyarsk Krai (RU-KYA)
🏴󠁲󠁵󠁭󠁡󠁧󠁿 Flag for Magadan (RU-MAG)
🏴󠁲󠁵󠁫󠁯󠁳󠁿 Flag for Kostroma (RU-KOS)
🏴󠁲󠁵󠁳󠁡󠁫󠁿 Flag for Sakhalin (RU-SAK)
🏴󠁲󠁵󠁴󠁶󠁥󠁿 Flag for Tver (RU-TVE)
🏴󠁲󠁵󠁮󠁶󠁳󠁿 Flag for Novosibirsk (RU-NVS)
🏴󠁲󠁵󠁭󠁯󠁷󠁿 Flag for Moscow (RU-MOW)
🏴󠁲󠁵󠁶󠁬󠁡󠁿 Flag for Vladimir (RU-VLA)
🏴󠁲󠁵󠁯󠁲󠁬󠁿 Flag for Oryol (RU-ORL)
🏴󠁲󠁵󠁳󠁴󠁡󠁿 Flag for Stavropol Krai (RU-STA)
🏴󠁲󠁵󠁮󠁩󠁺󠁿 Flag for Nizhny Novgorod (RU-NIZ)
🏴󠁲󠁵󠁳󠁡󠁲󠁿 Flag for Saratov (RU-SAR)
🏴󠁲󠁵󠁮󠁥󠁮󠁿 Flag for Nenets (RU-NEN)
🏴󠁲󠁵󠁴󠁡󠁿 Flag for Tatarstan (RU-TA)
🏴󠁲󠁵󠁯󠁭󠁳󠁿 Flag for Omsk (RU-OMS)
🏴󠁲󠁵󠁳󠁶󠁥󠁿 Flag for Sverdlovsk (RU-SVE)
🏴󠁲󠁵󠁭󠁵󠁲󠁿 Flag for Murmansk (RU-MUR)
🏴󠁲󠁵󠁹󠁡󠁮󠁿 Flag for Yamalo-Nenets Okrug (RU-YAN)
🏴󠁲󠁵󠁵󠁬󠁹󠁿 Flag for Ulyanovsk (RU-ULY)
🏴󠁲󠁵󠁰󠁮󠁺󠁿 Flag for Penza (RU-PNZ)
🏴󠁲󠁵󠁳󠁭󠁯󠁿 Flag for Smolensk (RU-SMO)
🏴󠁲󠁵󠁯󠁲󠁥󠁿 Flag for Orenburg (RU-ORE)
🏴󠁲󠁵󠁴󠁵󠁬󠁿 Flag for Tula (RU-TUL)
🏴󠁲󠁵󠁹󠁡󠁲󠁿 Flag for Yaroslavl (RU-YAR)
🏴󠁲󠁵󠁴󠁹󠁵󠁿 Flag for Tyumen (RU-TYU)
🏴󠁲󠁵󠁰󠁳󠁫󠁿 Flag for Pskov (RU-PSK)
🏴󠁲󠁵󠁳󠁡󠁭󠁿 Flag for Samara (RU-SAM)
🏴󠁲󠁵󠁵󠁤󠁿 Flag for Udmurt (RU-UD)
🏴󠁲󠁵󠁲󠁹󠁡󠁿 Flag for Ryazan (RU-RYA)
🏴󠁲󠁵󠁴󠁹󠁿 Flag for Tuva (RU-TY)
🏴󠁲󠁵󠁰󠁥󠁲󠁿 Flag for Perm Krai (RU-PER)
🏴󠁲󠁵󠁶󠁯󠁲󠁿 Flag for Voronezh (RU-VOR)
🏴󠁲󠁵󠁮󠁧󠁲󠁿 Flag for Novgorod (RU-NGR)
🏴󠁲󠁵󠁴󠁡󠁭󠁿 Flag for Tambov (RU-TAM)
🏴󠁲󠁵󠁳󠁡󠁿 Flag for Sakha (RU-SA)
🏴󠁲󠁵󠁲󠁯󠁳󠁿 Flag for Rostov (RU-ROS)
🏴󠁲󠁵󠁶󠁬󠁧󠁿 Flag for Vologda (RU-VLG)
🏴󠁲󠁵󠁳󠁰󠁥󠁿 Flag for Saint Petersburg (RU-SPE)
🏴󠁲󠁵󠁶󠁧󠁧󠁿 Flag for Volgograd (RU-VGG)
🏴󠁲󠁵󠁴󠁯󠁭󠁿 Flag for Tomsk (RU-TOM)
🏴󠁲󠁷󠀰󠀱󠁿 Flag for Kigali (RW-01)
🏴󠁳󠁣󠀰󠀱󠁿 Flag for Anse aux Pins (SC-01)
🏴󠁳󠁢󠁩󠁳󠁿 Flag for Isabel (SB-IS)
🏴󠁳󠁣󠀰󠀲󠁿 Flag for Anse Boileau (SC-02)
🏴󠁳󠁡󠀰󠀷󠁿 Flag for Tabuk (SA-07)
🏴󠁳󠁢󠁧󠁵󠁿 Flag for Guadalcanal (SB-GU)
🏴󠁲󠁷󠀰󠀳󠁿 Flag for Northern (RW-03)
🏴󠁲󠁷󠀰󠀵󠁿 Flag for Southern (RW-05)
🏴󠁳󠁢󠁲󠁢󠁿 Flag for Rennell and Bellona (SB-RB)
🏴󠁳󠁡󠀰󠀶󠁿 Flag for Ha’il (SA-06)
🏴󠁳󠁡󠀰󠀵󠁿 Flag for Al-Qassim (SA-05)
🏴󠁳󠁢󠁭󠁬󠁿 Flag for Malaita (SB-ML)
🏴󠁳󠁢󠁣󠁴󠁿 Flag for Honiara (SB-CT)
🏴󠁳󠁡󠀰󠀸󠁿 Flag for Northern Borders (SA-08)
🏴󠁳󠁡󠀰󠀲󠁿 Flag for Makkah (SA-02)
🏴󠁳󠁡󠀰󠀹󠁿 Flag for Jizan (SA-09)
🏴󠁲󠁷󠀰󠀲󠁿 Flag for Eastern (RW-02)
🏴󠁳󠁣󠀰󠀷󠁿 Flag for Baie Sainte Anne (SC-07)
🏴󠁳󠁡󠀰󠀳󠁿 Flag for Al Madinah (SA-03)
🏴󠁳󠁢󠁣󠁥󠁿 Flag for Central (SB-CE)
🏴󠁳󠁣󠀱󠀰󠁿 Flag for Bel Ombre (SC-10)
🏴󠁳󠁢󠁴󠁥󠁿 Flag for Temotu (SB-TE)
🏴󠁳󠁡󠀱󠀰󠁿 Flag for Najran (SA-10)
🏴󠁳󠁣󠀰󠀳󠁿 Flag for Anse Etoile (SC-03)
🏴󠁲󠁵󠁹󠁥󠁶󠁿 Flag for Jewish (RU-YEV)
🏴󠁳󠁢󠁣󠁨󠁿 Flag for Choiseul (SB-CH)
🏴󠁲󠁷󠀰󠀴󠁿 Flag for Western (RW-04)
🏴󠁳󠁢󠁭󠁫󠁿 Flag for Makira-Ulawa (SB-MK)
🏴󠁳󠁣󠀰󠀹󠁿 Flag for Bel Air (SC-09)
🏴󠁳󠁡󠀰󠀱󠁿 Flag for Riyadh (SA-01)
🏴󠁳󠁡󠀰󠀴󠁿 Flag for Eastern (SA-04)
🏴󠁳󠁡󠀱󠀴󠁿 Flag for Asir (SA-14)
🏴󠁲󠁵󠁺󠁡󠁢󠁿 Flag for Zabaykalsky Krai (RU-ZAB)
🏴󠁳󠁣󠀰󠀸󠁿 Flag for Beau Vallon (SC-08)
🏴󠁳󠁣󠀰󠀶󠁿 Flag for Baie Lazare (SC-06)
🏴󠁳󠁡󠀱󠀲󠁿 Flag for Al Jawf (SA-12)
🏴󠁳󠁢󠁷󠁥󠁿 Flag for Western (SB-WE)
🏴󠁳󠁣󠀰󠀴󠁿 Flag for Au Cap (SC-04)
🏴󠁳󠁣󠀱󠀹󠁿 Flag for Plaisance (SC-19)
🏴󠁳󠁥󠁤󠁿 Flag for Södermanland (SE-D)
🏴󠁳󠁣󠀱󠀶󠁿 Flag for La Rivière Anglaise (SC-16)
🏴󠁳󠁤󠁮󠁷󠁿 Flag for White Nile (SD-NW)
🏴󠁳󠁣󠀱󠀸󠁿 Flag for Mont Fleuri (SC-18)
🏴󠁳󠁤󠁮󠁯󠁿 Flag for Northern (SD-NO)
🏴󠁳󠁣󠀱󠀳󠁿 Flag for Grand’Anse Mahé (SC-13)
🏴󠁳󠁣󠀲󠀳󠁿 Flag for Takamaka (SC-23)
🏴󠁳󠁤󠁧󠁤󠁿 Flag for Al Qadarif (SD-GD)
🏴󠁳󠁤󠁤󠁳󠁿 Flag for South Darfur (SD-DS)
🏴󠁳󠁤󠁧󠁫󠁿 Flag for West Kurdufan (SD-GK)
🏴󠁳󠁤󠁮󠁲󠁿 Flag for River Nile (SD-NR)
🏴󠁳󠁤󠁫󠁡󠁿 Flag for Kassala (SD-KA)
🏴󠁳󠁤󠁫󠁨󠁿 Flag for Khartoum (SD-KH)
🏴󠁳󠁣󠀱󠀵󠁿 Flag for La Digue (SC-15)
🏴󠁳󠁤󠁫󠁮󠁿 Flag for North Kurdufan (SD-KN)
🏴󠁳󠁣󠀲󠀴󠁿 Flag for Les Mamelles (SC-24)
🏴󠁳󠁣󠀲󠀰󠁿 Flag for Pointe La Rue (SC-20)
🏴󠁳󠁥󠁡󠁣󠁿 Flag for Västerbotten (SE-AC)
🏴󠁳󠁥󠁦󠁿 Flag for Jönköping (SE-F)
🏴󠁳󠁥󠁡󠁢󠁿 Flag for Stockholm (SE-AB)
🏴󠁳󠁤󠁳󠁩󠁿 Flag for Sennar (SD-SI)
🏴󠁳󠁣󠀲󠀲󠁿 Flag for Saint Louis (SC-22)
🏴󠁳󠁣󠀲󠀱󠁿 Flag for Port Glaud (SC-21)
🏴󠁳󠁤󠁧󠁺󠁿 Flag for Al Jazirah (SD-GZ)
🏴󠁳󠁥󠁥󠁿 Flag for Östergötland (SE-E)
🏴󠁳󠁣󠀱󠀲󠁿 Flag for Glacis (SC-12)
🏴󠁳󠁥󠁣󠁿 Flag for Uppsala (SE-C)
🏴󠁳󠁣󠀱󠀷󠁿 Flag for Mont Buxton (SC-17)
🏴󠁳󠁣󠀱󠀴󠁿 Flag for Grand’Anse Praslin (SC-14)
🏴󠁳󠁤󠁤󠁷󠁿 Flag for West Darfur (SD-DW)
🏴󠁳󠁤󠁫󠁳󠁿 Flag for South Kurdufan (SD-KS)
🏴󠁳󠁣󠀱󠀱󠁿 Flag for Cascade (SC-11)
🏴󠁳󠁤󠁮󠁢󠁿 Flag for Blue Nile (SD-NB)
🏴󠁳󠁤󠁤󠁥󠁿 Flag for East Darfur (SD-DE)
🏴󠁳󠁤󠁤󠁮󠁿 Flag for North Darfur (SD-DN)
🏴󠁳󠁤󠁤󠁣󠁿 Flag for Central Darfur (SD-DC)
🏴󠁳󠁥󠁢󠁤󠁿 Flag for Norrbotten (SE-BD)
🏴󠁳󠁥󠁵󠁿 Flag for Västmanland (SE-U)
🏴󠁳󠁩󠀰󠀱󠀷󠁿 Flag for Črnomelj (SI-017)
🏴󠁳󠁩󠀰󠀰󠀵󠁿 Flag for Borovnica (SI-005)
🏴󠁳󠁩󠀰󠀰󠀷󠁿 Flag for Brda (SI-007)
🏴󠁳󠁧󠀰󠀵󠁿 Flag for South West (SG-05)
🏴󠁳󠁩󠀰󠀱󠀶󠁿 Flag for Črna na Koroškem (SI-016)
🏴󠁳󠁥󠁳󠁿 Flag for Värmland (SE-S)
🏴󠁳󠁥󠁩󠁿 Flag for Gotland (SE-I)
🏴󠁳󠁧󠀰󠀲󠁿 Flag for North East (SG-02)
🏴󠁳󠁩󠀰󠀱󠀸󠁿 Flag for Destrnik (SI-018)
🏴󠁳󠁩󠀰󠀰󠀲󠁿 Flag for Beltinci (SI-002)
🏴󠁳󠁩󠀰󠀰󠀴󠁿 Flag for Bohinj (SI-004)
🏴󠁳󠁩󠀰󠀰󠀹󠁿 Flag for Brežice (SI-009)
🏴󠁳󠁨󠁡󠁣󠁿 Flag for Ascension Island (SH-AC)
🏴󠁳󠁧󠀰󠀳󠁿 Flag for North West (SG-03)
👩🏽‍👦🏽‍👶🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁳󠁩󠀰󠀱󠀳󠁿 Flag for Cerknica (SI-013)
🏴󠁳󠁩󠀰󠀰󠀶󠁿 Flag for Bovec (SI-006)
🏴󠁳󠁩󠀰󠀱󠀵󠁿 Flag for Črenšovci (SI-015)
🏴󠁳󠁥󠁧󠁿 Flag for Kronoberg (SE-G)
🏴󠁳󠁩󠀰󠀰󠀱󠁿 Flag for Ajdovščina (SI-001)
🏴󠁳󠁥󠁫󠁿 Flag for Blekinge (SE-K)
🏴󠁳󠁩󠀰󠀱󠀰󠁿 Flag for Tišina (SI-010)
🏴󠁳󠁧󠀰󠀴󠁿 Flag for South East (SG-04)
🏴󠁳󠁩󠀰󠀰󠀸󠁿 Flag for Brezovica (SI-008)
🏴󠁳󠁥󠁹󠁿 Flag for Västernorrland (SE-Y)
🏴󠁳󠁥󠁺󠁿 Flag for Jämtland (SE-Z)
🏴󠁳󠁥󠁷󠁿 Flag for Dalarna (SE-W)
🏴󠁳󠁩󠀰󠀰󠀳󠁿 Flag for Bled (SI-003)
🏴󠁳󠁥󠁴󠁿 Flag for Örebro (SE-T)
🏴󠁳󠁨󠁨󠁬󠁿 Flag for Saint Helena (SH-HL)
🏴󠁳󠁩󠀰󠀱󠀲󠁿 Flag for Cerklje na Gorenjskem (SI-012)
🏴󠁳󠁨󠁴󠁡󠁿 Flag for Tristan da Cunha (SH-TA)
🏴󠁳󠁩󠀰󠀱󠀴󠁿 Flag for Cerkno (SI-014)
🏴󠁳󠁥󠁯󠁿 Flag for Västra Götaland (SE-O)
🏴󠁳󠁥󠁨󠁿 Flag for Kalmar (SE-H)
🏴󠁳󠁩󠀰󠀲󠀳󠁿 Flag for Domžale (SI-023)
🏴󠁳󠁩󠀰󠀴󠀰󠁿 Flag for Izola (SI-040)
🏴󠁳󠁩󠀰󠀵󠀶󠁿 Flag for Kuzma (SI-056)
🏴󠁳󠁩󠀰󠀲󠀵󠁿 Flag for Dravograd (SI-025)
🏴󠁳󠁩󠀰󠀲󠀶󠁿 Flag for Duplek (SI-026)
🏴󠁳󠁩󠀰󠀴󠀱󠁿 Flag for Jesenice (SI-041)
🏴󠁳󠁩󠀰󠀲󠀸󠁿 Flag for Gorišnica (SI-028)
🏴󠁳󠁩󠀰󠀲󠀹󠁿 Flag for Gornja Radgona (SI-029)
🏴󠁳󠁩󠀰󠀳󠀱󠁿 Flag for Gornji Petrovci (SI-031)
🏴󠁳󠁩󠀰󠀲󠀴󠁿 Flag for Dornava (SI-024)
🏴󠁳󠁩󠀰󠀳󠀴󠁿 Flag for Hrastnik (SI-034)
🏴󠁳󠁩󠀰󠀴󠀹󠁿 Flag for Komen (SI-049)
🏴󠁳󠁩󠀰󠀵󠀱󠁿 Flag for Kozje (SI-051)
🏴󠁳󠁩󠀰󠀱󠀹󠁿 Flag for Divača (SI-019)
🏴󠁳󠁩󠀰󠀳󠀶󠁿 Flag for Idrija (SI-036)
🏴󠁳󠁩󠀰󠀴󠀵󠁿 Flag for Kidričevo (SI-045)
🏴󠁳󠁩󠀰󠀴󠀶󠁿 Flag for Kobarid (SI-046)
🏴󠁳󠁩󠀰󠀴󠀷󠁿 Flag for Kobilje (SI-047)
🏴󠁳󠁩󠀰󠀳󠀷󠁿 Flag for Ig (SI-037)
🏴󠁳󠁩󠀰󠀵󠀰󠁿 Flag for Koper (SI-050)
🏴󠁳󠁩󠀰󠀳󠀹󠁿 Flag for Ivančna Gorica (SI-039)
🏴󠁳󠁩󠀰󠀵󠀳󠁿 Flag for Kranjska Gora (SI-053)
🏴󠁳󠁩󠀰󠀵󠀵󠁿 Flag for Kungota (SI-055)
🏴󠁳󠁩󠀰󠀳󠀲󠁿 Flag for Grosuplje (SI-032)
🏴󠁳󠁩󠀰󠀲󠀱󠁿 Flag for Dobrova–Polhov Gradec (SI-021)
🏴󠁳󠁩󠀰󠀴󠀲󠁿 Flag for Juršinci (SI-042)
🏴󠁳󠁩󠀰󠀵󠀴󠁿 Flag for Krško (SI-054)
🏴󠁳󠁩󠀰󠀳󠀳󠁿 Flag for Šalovci (SI-033)
🏴󠁳󠁩󠀰󠀴󠀴󠁿 Flag for Kanal (SI-044)
🏴󠁳󠁩󠀰󠀴󠀸󠁿 Flag for Kočevje (SI-048)
🏴󠁳󠁩󠀰󠀳󠀸󠁿 Flag for Ilirska Bistrica (SI-038)
🏴󠁳󠁩󠀰󠀴󠀳󠁿 Flag for Kamnik (SI-043)
🏴󠁳󠁩󠀰󠀳󠀵󠁿 Flag for Hrpelje–Kozina (SI-035)
🏴󠁳󠁩󠀰󠀳󠀰󠁿 Flag for Gornji Grad (SI-030)
🏴󠁳󠁩󠀰󠀲󠀰󠁿 Flag for Dobrepolje (SI-020)
🏴󠁳󠁩󠀰󠀲󠀲󠁿 Flag for Dol pri Ljubljani (SI-022)
🏴󠁳󠁩󠀰󠀸󠀹󠁿 Flag for Pesnica (SI-089)
🏴󠁳󠁩󠀰󠀹󠀰󠁿 Flag for Piran (SI-090)
🏴󠁳󠁩󠀰󠀷󠀴󠁿 Flag for Mežica (SI-074)
🏴󠁳󠁩󠀰󠀸󠀱󠁿 Flag for Muta (SI-081)
🏴󠁳󠁩󠀰󠀶󠀲󠁿 Flag for Ljubno (SI-062)
🏴󠁳󠁩󠀰󠀸󠀷󠁿 Flag for Ormož (SI-087)
🏴󠁳󠁩󠀰󠀶󠀶󠁿 Flag for Loški Potok (SI-066)
🏴󠁳󠁩󠀰󠀷󠀶󠁿 Flag for Mislinja (SI-076)
👩🏾‍👦🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁳󠁩󠀰󠀶󠀹󠁿 Flag for Majšperk (SI-069)
🏴󠁳󠁩󠀰󠀷󠀲󠁿 Flag for Mengeš (SI-072)
🏴󠁳󠁩󠀰󠀷󠀳󠁿 Flag for Metlika (SI-073)
🏴󠁳󠁩󠀰󠀷󠀷󠁿 Flag for Moravče (SI-077)
🏴󠁳󠁩󠀰󠀷󠀸󠁿 Flag for Moravske Toplice (SI-078)
🏴󠁳󠁩󠀰󠀹󠀴󠁿 Flag for Postojna (SI-094)
🏴󠁳󠁩󠀰󠀸󠀰󠁿 Flag for Murska Sobota (SI-080)
🏴󠁳󠁩󠀰󠀸󠀲󠁿 Flag for Naklo (SI-082)
🏴󠁳󠁩󠀰󠀸󠀸󠁿 Flag for Osilnica (SI-088)
🏴󠁳󠁩󠀰󠀶󠀱󠁿 Flag for Ljubljana (SI-061)
🏴󠁳󠁩󠀰󠀹󠀱󠁿 Flag for Pivka (SI-091)
🏴󠁳󠁩󠀰󠀸󠀳󠁿 Flag for Nazarje (SI-083)
🏴󠁳󠁩󠀰󠀷󠀵󠁿 Flag for Miren–Kostanjevica (SI-075)
🏴󠁳󠁩󠀰󠀶󠀴󠁿 Flag for Logatec (SI-064)
🏴󠁳󠁩󠀰󠀸󠀴󠁿 Flag for Nova Gorica (SI-084)
🏴󠁳󠁩󠀰󠀶󠀰󠁿 Flag for Litija (SI-060)
🏴󠁳󠁩󠀰󠀷󠀰󠁿 Flag for Maribor (SI-070)
🏴󠁳󠁩󠀰󠀶󠀳󠁿 Flag for Ljutomer (SI-063)
🏴󠁳󠁩󠀰󠀶󠀷󠁿 Flag for Luče (SI-067)
🏴󠁳󠁩󠀰󠀹󠀲󠁿 Flag for Podčetrtek (SI-092)
🏴󠁳󠁩󠀰󠀹󠀳󠁿 Flag for Podvelka (SI-093)
🏴󠁳󠁩󠀰󠀷󠀱󠁿 Flag for Medvode (SI-071)
🏴󠁳󠁩󠀰󠀶󠀵󠁿 Flag for Loška Dolina (SI-065)
🏴󠁳󠁩󠀰󠀵󠀷󠁿 Flag for Laško (SI-057)
🏴󠁳󠁩󠀰󠀵󠀹󠁿 Flag for Lendava (SI-059)
🏴󠁳󠁩󠀰󠀷󠀹󠁿 Flag for Mozirje (SI-079)
🏴󠁳󠁩󠀰󠀶󠀸󠁿 Flag for Lukovica (SI-068)
🏴󠁳󠁩󠀱󠀳󠀱󠁿 Flag for Tržič (SI-131)
🏴󠁳󠁩󠀱󠀱󠀸󠁿 Flag for Šentilj (SI-118)
🏴󠁳󠁩󠀰󠀹󠀷󠁿 Flag for Puconci (SI-097)
👩🏿‍👦🏿‍👶🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁳󠁩󠀱󠀰󠀵󠁿 Flag for Rogašovci (SI-105)
🏴󠁳󠁩󠀱󠀱󠀳󠁿 Flag for Slovenska Bistrica (SI-113)
🏴󠁳󠁩󠀱󠀰󠀷󠁿 Flag for Rogatec (SI-107)
🏴󠁳󠁩󠀰󠀹󠀶󠁿 Flag for Ptuj (SI-096)
🏴󠁳󠁩󠀱󠀱󠀹󠁿 Flag for Šentjernej (SI-119)
🏴󠁳󠁩󠀱󠀱󠀱󠁿 Flag for Sežana (SI-111)
🏴󠁳󠁩󠀰󠀹󠀸󠁿 Flag for Rače–Fram (SI-098)
🏴󠁳󠁩󠀱󠀱󠀲󠁿 Flag for Slovenj Gradec (SI-112)
🏴󠁳󠁩󠀱󠀱󠀵󠁿 Flag for Starše (SI-115)
🏴󠁳󠁩󠀱󠀱󠀶󠁿 Flag for Sveti Jurij (SI-116)
🏴󠁳󠁩󠀱󠀳󠀰󠁿 Flag for Trebnje (SI-130)
🏴󠁳󠁩󠀱󠀱󠀰󠁿 Flag for Sevnica (SI-110)
🏴󠁳󠁩󠀰󠀹󠀹󠁿 Flag for Radeče (SI-099)
🏴󠁳󠁩󠀱󠀲󠀱󠁿 Flag for Škocjan (SI-121)
🏴󠁳󠁩󠀱󠀲󠀴󠁿 Flag for Šmarje pri Jelšah (SI-124)
🏴󠁳󠁩󠀱󠀲󠀶󠁿 Flag for Šoštanj (SI-126)
🏴󠁳󠁩󠀱󠀲󠀷󠁿 Flag for Štore (SI-127)
🏴󠁳󠁩󠀱󠀲󠀳󠁿 Flag for Škofljica (SI-123)
🏴󠁳󠁩󠀱󠀰󠀶󠁿 Flag for Rogaška Slatina (SI-106)
🏴󠁳󠁩󠀰󠀹󠀵󠁿 Flag for Preddvor (SI-095)
🏴󠁳󠁩󠀱󠀳󠀲󠁿 Flag for Turnišče (SI-132)
🏴󠁳󠁩󠀱󠀰󠀲󠁿 Flag for Radovljica (SI-102)
🏴󠁳󠁩󠀱󠀱󠀴󠁿 Flag for Slovenske Konjice (SI-114)
🏴󠁳󠁩󠀱󠀲󠀰󠁿 Flag for Šentjur (SI-120)
🏴󠁳󠁩󠀱󠀲󠀸󠁿 Flag for Tolmin (SI-128)
🏴󠁳󠁩󠀱󠀰󠀴󠁿 Flag for Ribnica (SI-104)
🏴󠁳󠁩󠀱󠀰󠀱󠁿 Flag for Radlje ob Dravi (SI-101)
🏴󠁳󠁩󠀱󠀰󠀸󠁿 Flag for Ruše (SI-108)
🏴󠁳󠁩󠀱󠀲󠀹󠁿 Flag for Trbovlje (SI-129)
🏴󠁳󠁩󠀱󠀰󠀹󠁿 Flag for Semič (SI-109)
🏴󠁳󠁩󠀱󠀱󠀷󠁿 Flag for Šenčur (SI-117)
🏴󠁳󠁩󠀱󠀰󠀳󠁿 Flag for Ravne na Koroškem (SI-103)
🏴󠁳󠁩󠀱󠀶󠀹󠁿 Flag for Miklavž na Dravskem Polju (SI-169)
🏴󠁳󠁩󠀱󠀴󠀱󠁿 Flag for Vuzenica (SI-141)
🏴󠁳󠁩󠀱󠀴󠀲󠁿 Flag for Zagorje ob Savi (SI-142)
🏴󠁳󠁩󠀱󠀳󠀸󠁿 Flag for Vodice (SI-138)
🏴󠁳󠁩󠀱󠀴󠀰󠁿 Flag for Vrhnika (SI-140)
🏴󠁳󠁩󠀱󠀶󠀴󠁿 Flag for Komenda (SI-164)
🏴󠁳󠁩󠀱󠀴󠀶󠁿 Flag for Železniki (SI-146)
🏴󠁳󠁩󠀱󠀴󠀷󠁿 Flag for Žiri (SI-147)
🏴󠁳󠁩󠀱󠀴󠀸󠁿 Flag for Benedikt (SI-148)
🏴󠁳󠁩󠀱󠀳󠀴󠁿 Flag for Velike Lašče (SI-134)
🏴󠁳󠁩󠀱󠀳󠀷󠁿 Flag for Vitanje (SI-137)
🏴󠁳󠁩󠀱󠀵󠀸󠁿 Flag for Grad (SI-158)
🏴󠁳󠁩󠀱󠀵󠀵󠁿 Flag for Dobrna (SI-155)
🏴󠁳󠁩󠀱󠀵󠀶󠁿 Flag for Dobrovnik (SI-156)
🏴󠁳󠁩󠀱󠀵󠀷󠁿 Flag for Dolenjske Toplice (SI-157)
🏴󠁳󠁩󠀱󠀵󠀹󠁿 Flag for Hajdina (SI-159)
🏴󠁳󠁩󠀱󠀷󠀱󠁿 Flag for Oplotnica (SI-171)
🏴󠁳󠁩󠀱󠀳󠀵󠁿 Flag for Videm (SI-135)
🏴󠁳󠁩󠀱󠀶󠀳󠁿 Flag for Jezersko (SI-163)
🏴󠁳󠁩󠀱󠀵󠀲󠁿 Flag for Cankova (SI-152)
🏴󠁳󠁩󠀱󠀶󠀵󠁿 Flag for Kostel (SI-165)
🏴󠁳󠁩󠀱󠀶󠀶󠁿 Flag for Križevci (SI-166)
🏴󠁳󠁩󠀱󠀳󠀹󠁿 Flag for Vojnik (SI-139)
🏴󠁳󠁩󠀱󠀶󠀸󠁿 Flag for Markovci (SI-168)
👩🏻‍👧🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone
🏴󠁳󠁩󠀱󠀷󠀰󠁿 Flag for Mirna Peč (SI-170)
🏴󠁳󠁩󠀱󠀳󠀶󠁿 Flag for Vipava (SI-136)
🏴󠁳󠁩󠀱󠀶󠀲󠁿 Flag for Horjul (SI-162)
🏴󠁳󠁩󠀱󠀵󠀳󠁿 Flag for Cerkvenjak (SI-153)
🏴󠁳󠁩󠀱󠀵󠀰󠁿 Flag for Bloke (SI-150)
🏴󠁳󠁩󠀱󠀴󠀳󠁿 Flag for Zavrč (SI-143)
🏴󠁳󠁩󠀱󠀴󠀹󠁿 Flag for Bistrica ob Sotli (SI-149)
🏴󠁳󠁩󠀱󠀴󠀴󠁿 Flag for Zreče (SI-144)
🏴󠁳󠁩󠀱󠀶󠀱󠁿 Flag for Hodoš (SI-161)
🏴󠁳󠁩󠀱󠀶󠀰󠁿 Flag for Hoče–Slivnica (SI-160)
🏴󠁳󠁩󠀱󠀷󠀲󠁿 Flag for Podlehnik (SI-172)
🏴󠁳󠁩󠀱󠀹󠀶󠁿 Flag for Cirkulane (SI-196)
🏴󠁳󠁩󠀱󠀷󠀴󠁿 Flag for Prebold (SI-174)
🏴󠁳󠁩󠀱󠀷󠀶󠁿 Flag for Razkrižje (SI-176)
🏴󠁳󠁩󠀱󠀸󠀸󠁿 Flag for Veržej (SI-188)
🏴󠁳󠁩󠀱󠀹󠀰󠁿 Flag for Žalec (SI-190)
🏴󠁳󠁩󠀱󠀸󠀰󠁿 Flag for Solčava (SI-180)
🏴󠁳󠁩󠀱󠀸󠀱󠁿 Flag for Sveta Ana (SI-181)
🏴󠁳󠁩󠀱󠀸󠀳󠁿 Flag for Šempeter–Vrtojba (SI-183)
🏴󠁳󠁩󠀱󠀸󠀵󠁿 Flag for Trnovska Vas (SI-185)
🏴󠁳󠁩󠀱󠀷󠀹󠁿 Flag for Sodražica (SI-179)
🏴󠁳󠁩󠀱󠀹󠀸󠁿 Flag for Makole (SI-198)
🏴󠁳󠁩󠀲󠀰󠀳󠁿 Flag for Straža (SI-203)
🏴󠁳󠁩󠀱󠀷󠀸󠁿 Flag for Selnica ob Dravi (SI-178)
🏴󠁳󠁩󠀱󠀹󠀳󠁿 Flag for Žužemberk (SI-193)
🏴󠁳󠁩󠀱󠀹󠀷󠁿 Flag for Kostanjevica na Krki (SI-197)
🏴󠁳󠁩󠀱󠀷󠀵󠁿 Flag for Prevalje (SI-175)
🏴󠁳󠁩󠀱󠀹󠀴󠁿 Flag for Šmartno pri Litiji (SI-194)
🏴󠁳󠁩󠀱󠀹󠀱󠁿 Flag for Žetale (SI-191)
🏴󠁳󠁩󠀱󠀸󠀹󠁿 Flag for Vransko (SI-189)
🏴󠁳󠁩󠀲󠀰󠀱󠁿 Flag for Renče–Vogrsko (SI-201)
🏴󠁳󠁩󠀱󠀸󠀶󠁿 Flag for Trzin (SI-186)
🏴󠁳󠁩󠀲󠀰󠀴󠁿 Flag for Sveta Trojica v Slovenskih Goricah (SI-204)
🏴󠁳󠁩󠀲󠀰󠀵󠁿 Flag for Sveti Tomaž (SI-205)
🏴󠁳󠁩󠀱󠀷󠀷󠁿 Flag for Ribnica na Pohorju (SI-177)
🏴󠁳󠁩󠀲󠀰󠀷󠁿 Flag for Gorje (SI-207)
󠁒 Tag Latin Capital Letter R
🏴󠁳󠁩󠀱󠀸󠀴󠁿 Flag for Tabor (SI-184)
🏴󠁳󠁩󠀱󠀹󠀹󠁿 Flag for Mokronog–Trebelno (SI-199)
🏴󠁳󠁩󠀱󠀷󠀳󠁿 Flag for Polzela (SI-173)
🏴󠁳󠁩󠀲󠀰󠀰󠁿 Flag for Poljčane (SI-200)
🏴󠁳󠁩󠀱󠀹󠀵󠁿 Flag for Apače (SI-195)
🏴󠁳󠁩󠀱󠀸󠀷󠁿 Flag for Velika Polana (SI-187)
🏴󠁳󠁫󠁴󠁡󠁿 Flag for Trnava (SK-TA)
🏴󠁳󠁩󠀲󠀰󠀹󠁿 Flag for Rečica ob Savinji (SI-209)
🏴󠁳󠁭󠀰󠀹󠁿 Flag for Serravalle (SM-09)
🏴󠁳󠁫󠁫󠁩󠁿 Flag for Košice (SK-KI)
🏴󠁳󠁭󠀰󠀲󠁿 Flag for Chiesanuova (SM-02)
🏴󠁳󠁫󠁮󠁩󠁿 Flag for Nitra (SK-NI)
🏴󠁳󠁭󠀰󠀷󠁿 Flag for San Marino (SM-07)
🏴󠁳󠁩󠀲󠀱󠀱󠁿 Flag for Šentrupert (SI-211)
🏴󠁳󠁫󠁢󠁬󠁿 Flag for Bratislava (SK-BL)
🏴󠁳󠁮󠁫󠁬󠁿 Flag for Kaolack (SN-KL)
🏴󠁳󠁫󠁢󠁣󠁿 Flag for Banská Bystrica (SK-BC)
🏴󠁳󠁭󠀰󠀸󠁿 Flag for Montegiardino (SM-08)
🏴󠁳󠁩󠀲󠀱󠀲󠁿 Flag for Mirna (SI-212)
🏴󠁧󠁲󠁧󠁿 Flag for West Greece (GR-G)
🏴󠁳󠁭󠀰󠀵󠁿 Flag for Fiorentino (SM-05)
🏴󠁳󠁮󠁴󠁨󠁿 Flag for Thiès (SN-TH)
🏴󠁩󠁮󠁲󠁪󠁿 Flag for Rajasthan (IN-RJ)
🏴󠁳󠁮󠁬󠁧󠁿 Flag for Louga (SN-LG)
🏴󠁳󠁫󠁴󠁣󠁿 Flag for Trenčín (SK-TC)
🏴󠁳󠁭󠀰󠀳󠁿 Flag for Domagnano (SM-03)
🏴󠁳󠁭󠀰󠀴󠁿 Flag for Faetano (SM-04)
🏴󠁳󠁫󠁺󠁩󠁿 Flag for Žilina (SK-ZI)
🏴󠁳󠁬󠁳󠁿 Flag for Southern (SL-S)
🏴󠁳󠁮󠁫󠁡󠁿 Flag for Kaffrine (SN-KA)
🏴󠁳󠁮󠁦󠁫󠁿 Flag for Fatick (SN-FK)
🏴󠁳󠁮󠁳󠁥󠁿 Flag for Sédhiou (SN-SE)
🏴󠁳󠁬󠁷󠁿 Flag for Western Area (SL-W)
🏴󠁳󠁮󠁫󠁥󠁿 Flag for Kédougou (SN-KE)
🏴󠁳󠁬󠁮󠁿 Flag for Northern (SL-N)
🏴󠁳󠁮󠁫󠁤󠁿 Flag for Kolda (SN-KD)
🏴󠁳󠁮󠁭󠁴󠁿 Flag for Matam (SN-MT)
🏴󠁩󠁴󠀷󠀸󠁿 Flag for Calabria (IT-78)
🏴󠁳󠁭󠀰󠀱󠁿 Flag for Acquaviva (SM-01)
󠀿 Tag Question Mark
🏴󠁳󠁮󠁤󠁢󠁿 Flag for Diourbel (SN-DB)
🏴󠁳󠁮󠁴󠁣󠁿 Flag for Tambacounda (SN-TC)
🏴󠁳󠁭󠀰󠀶󠁿 Flag for Borgo Maggiore (SM-06)
🏴󠁳󠁫󠁰󠁶󠁿 Flag for Prešov (SK-PV)
🏴󠁳󠁯󠁨󠁩󠁿 Flag for Hiran (SO-HI)
🏴󠁭󠁮󠀰󠀶󠀴󠁿 Flag for Govisümber (MN-064)
🏴󠁳󠁲󠁳󠁡󠁿 Flag for Saramacca (SR-SA)
🏴󠁳󠁳󠁥󠁥󠁿 Flag for Eastern Equatoria (SS-EE)
🏴󠁳󠁯󠁴󠁯󠁿 Flag for Togdheer (SO-TO)
🏴󠁳󠁯󠁡󠁷󠁿 Flag for Awdal (SO-AW)
🏴󠁳󠁲󠁭󠁡󠁿 Flag for Marowijne (SR-MA)
🏴󠁳󠁯󠁪󠁤󠁿 Flag for Middle Juba (SO-JD)
🏴󠁳󠁯󠁭󠁵󠁿 Flag for Mudug (SO-MU)
🏴󠁳󠁯󠁳󠁨󠁿 Flag for Lower Shebelle (SO-SH)
🏴󠁳󠁳󠁥󠁣󠁿 Flag for Central Equatoria (SS-EC)
󠀬 Tag Comma
🏴󠁳󠁮󠁺󠁧󠁿 Flag for Ziguinchor (SN-ZG)
🏴󠁳󠁯󠁳󠁤󠁿 Flag for Middle Shebelle (SO-SD)
🏴󠁳󠁳󠁮󠁵󠁿 Flag for Upper Nile (SS-NU)
🏴󠁳󠁲󠁷󠁡󠁿 Flag for Wanica (SR-WA)
🏴󠁳󠁳󠁥󠁷󠁿 Flag for Western Equatoria (SS-EW)
🏴󠁳󠁯󠁳󠁡󠁿 Flag for Sanaag (SO-SA)
🏴󠁳󠁯󠁷󠁯󠁿 Flag for Woqooyi Galbeed (SO-WO)
🏴󠁳󠁯󠁪󠁨󠁿 Flag for Lower Juba (SO-JH)
🏴󠁳󠁳󠁷󠁲󠁿 Flag for Warrap (SS-WR)
🏴󠁳󠁴󠁰󠁿 Flag for Príncipe (ST-P)
🏴󠁳󠁲󠁳󠁩󠁿 Flag for Sipaliwini (SR-SI)
🏴󠁳󠁳󠁢󠁷󠁿 Flag for Western Bahr el Ghazal (SS-BW)
🏴󠁳󠁳󠁪󠁧󠁿 Flag for Jonglei (SS-JG)
🏴󠁳󠁯󠁳󠁯󠁿 Flag for Sool (SO-SO)
🏴󠁳󠁯󠁢󠁫󠁿 Flag for Bakool (SO-BK)
🏴󠁳󠁲󠁰󠁲󠁿 Flag for Para (SR-PR)
🏴󠁳󠁲󠁣󠁭󠁿 Flag for Commewijne (SR-CM)
🏴󠁳󠁯󠁧󠁡󠁿 Flag for Galguduud (SO-GA)
🏴󠁳󠁲󠁮󠁩󠁿 Flag for Nickerie (SR-NI)
🏴󠁳󠁯󠁢󠁲󠁿 Flag for Bari (SO-BR)
🏴󠁳󠁯󠁧󠁥󠁿 Flag for Gedo (SO-GE)
🏴󠁳󠁲󠁰󠁭󠁿 Flag for Paramaribo (SR-PM)
🏴󠁳󠁲󠁢󠁲󠁿 Flag for Brokopondo (SR-BR)
🏴󠁳󠁯󠁮󠁵󠁿 Flag for Nugal (SO-NU)
🏴󠁳󠁲󠁣󠁲󠁿 Flag for Coronie (SR-CR)
👩🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
󠀺 Tag Colon
🏴󠁴󠁤󠁥󠁯󠁿 Flag for Ennedi-Ouest (TD-EO)
🏴󠁳󠁶󠁣󠁵󠁿 Flag for Cuscatlán (SV-CU)
🏴󠁳󠁺󠁳󠁨󠁿 Flag for Shiselweni (SZ-SH)
🏴󠁳󠁹󠁤󠁲󠁿 Flag for Daraa (SY-DR)
🏴󠁳󠁹󠁤󠁩󠁿 Flag for Damascus (SY-DI)
🏴󠁳󠁹󠁨󠁬󠁿 Flag for Aleppo (SY-HL)
🏴󠁳󠁶󠁳󠁯󠁿 Flag for Sonsonate (SV-SO)
🏴󠁳󠁶󠁳󠁳󠁿 Flag for San Salvador (SV-SS)
🏴󠁳󠁶󠁰󠁡󠁿 Flag for La Paz (SV-PA)
🏴󠁳󠁶󠁳󠁭󠁿 Flag for San Miguel (SV-SM)
🏴󠁳󠁶󠁭󠁯󠁿 Flag for Morazán (SV-MO)
🏴󠁳󠁹󠁨󠁭󠁿 Flag for Hama (SY-HM)
🏴󠁴󠁤󠁧󠁲󠁿 Flag for Guéra (TD-GR)
🏴󠁳󠁶󠁣󠁡󠁿 Flag for Cabañas (SV-CA)
🏴󠁳󠁺󠁬󠁵󠁿 Flag for Lubombo (SZ-LU)
🏴󠁳󠁶󠁣󠁨󠁿 Flag for Chalatenango (SV-CH)
🏴󠁴󠁤󠁢󠁧󠁿 Flag for Bahr el Gazel (TD-BG)
🏴󠁳󠁹󠁴󠁡󠁿 Flag for Tartus (SY-TA)
🏴󠁳󠁹󠁨󠁩󠁿 Flag for Homs (SY-HI)
🏴󠁳󠁺󠁭󠁡󠁿 Flag for Manzini (SZ-MA)
🏴󠁴󠁤󠁢󠁡󠁿 Flag for Batha (TD-BA)
🏴󠁴󠁤󠁥󠁥󠁿 Flag for Ennedi-Est (TD-EE)
🏴󠁳󠁺󠁨󠁨󠁿 Flag for Hhohho (SZ-HH)
🏴󠁴󠁤󠁫󠁡󠁿 Flag for Kanem (TD-KA)
🏴󠁳󠁹󠁬󠁡󠁿 Flag for Latakia (SY-LA)
🏴󠁳󠁹󠁩󠁤󠁿 Flag for Idlib (SY-ID)
🏴󠁳󠁶󠁬󠁩󠁿 Flag for La Libertad (SV-LI)
🏴󠁳󠁶󠁵󠁮󠁿 Flag for La Unión (SV-UN)
🏴󠁴󠁤󠁢󠁯󠁿 Flag for Borkou (TD-BO)
🏴󠁳󠁶󠁡󠁨󠁿 Flag for Ahuachapán (SV-AH)
🏴󠁴󠁤󠁣󠁢󠁿 Flag for Chari-Baguirmi (TD-CB)
🏴󠁳󠁹󠁲󠁤󠁿 Flag for Rif Dimashq (SY-RD)
🏴󠁳󠁹󠁳󠁵󠁿 Flag for As-Suwayda (SY-SU)
🏴󠁳󠁹󠁱󠁵󠁿 Flag for Quneitra (SY-QU)
🏴󠁳󠁹󠁲󠁡󠁿 Flag for Ar-Raqqah (SY-RA)
🏴󠁳󠁹󠁨󠁡󠁿 Flag for Al-Hasakah (SY-HA)
🏴󠁳󠁶󠁳󠁡󠁿 Flag for Santa Ana (SV-SA)
🏴󠁴󠁤󠁬󠁯󠁿 Flag for Logone Occidental (TD-LO)
🏴󠁴󠁨󠀲󠀲󠁿 Flag for Chanthaburi (TH-22)
🏴󠁴󠁤󠁭󠁥󠁿 Flag for Mayo-Kebbi Est (TD-ME)
🏴󠁴󠁤󠁭󠁣󠁿 Flag for Moyen-Chari (TD-MC)
🏴󠁴󠁤󠁴󠁡󠁿 Flag for Tandjilé (TD-TA)
🏴󠁴󠁤󠁭󠁯󠁿 Flag for Mayo-Kebbi Ouest (TD-MO)
󠁌 Tag Latin Capital Letter L
🏴󠁴󠁧󠁳󠁿 Flag for Savanes (TG-S)
🏴󠁴󠁤󠁳󠁩󠁿 Flag for Sila (TD-SI)
🏴󠁴󠁨󠀱󠀴󠁿 Flag for Phra Nakhon Si Ayutthaya (TH-14)
🏴󠁴󠁧󠁣󠁿 Flag for Centrale (TG-C)
🏴󠁴󠁨󠀱󠀱󠁿 Flag for Samut Prakan (TH-11)
🏴󠁴󠁨󠀱󠀲󠁿 Flag for Nonthaburi (TH-12)
🏴󠁴󠁨󠀱󠀰󠁿 Flag for Bangkok (TH-10)
🏴󠁴󠁨󠀲󠀰󠁿 Flag for Chon Buri (TH-20)
🏴󠁴󠁤󠁬󠁲󠁿 Flag for Logone Oriental (TD-LR)
🏴󠁴󠁨󠀱󠀳󠁿 Flag for Pathum Thani (TH-13)
🏴󠁴󠁤󠁬󠁣󠁿 Flag for Lac (TD-LC)
🏴󠁴󠁨󠀲󠀱󠁿 Flag for Rayong (TH-21)
🏴󠁴󠁨󠀲󠀵󠁿 Flag for Prachin Buri (TH-25)
🏴󠁴󠁨󠀳󠀰󠁿 Flag for Nakhon Ratchasima (TH-30)
🏴󠁴󠁨󠀳󠀱󠁿 Flag for Buri Ram (TH-31)
🏴󠁴󠁤󠁴󠁩󠁿 Flag for Tibesti (TD-TI)
🏴󠁴󠁤󠁭󠁡󠁿 Flag for Mandoul (TD-MA)
🏴󠁴󠁨󠀲󠀴󠁿 Flag for Chachoengsao (TH-24)
🏴󠁴󠁤󠁯󠁤󠁿 Flag for Ouaddaï (TD-OD)
🏴󠁴󠁨󠀱󠀵󠁿 Flag for Ang Thong (TH-15)
🏴󠁴󠁨󠀳󠀲󠁿 Flag for Surin (TH-32)
🏴󠁴󠁨󠀲󠀶󠁿 Flag for Nakhon Nayok (TH-26)
🏴󠁴󠁤󠁳󠁡󠁿 Flag for Salamat (TD-SA)
🏴󠁴󠁤󠁷󠁦󠁿 Flag for Wadi Fira (TD-WF)
🏴󠁴󠁨󠀱󠀹󠁿 Flag for Saraburi (TH-19)
🏴󠁴󠁨󠀱󠀷󠁿 Flag for Sing Buri (TH-17)
🏴󠁴󠁧󠁰󠁿 Flag for Plateaux (TG-P)
🏴󠁴󠁤󠁮󠁤󠁿 Flag for N’Djamena (TD-ND)
🏴󠁴󠁨󠀲󠀷󠁿 Flag for Sa Kaeo (TH-27)
󠁄 Tag Latin Capital Letter D
🏴󠁴󠁨󠀱󠀸󠁿 Flag for Chai Nat (TH-18)
🏴󠁴󠁨󠀶󠀲󠁿 Flag for Kamphaeng Phet (TH-62)
🏴󠁴󠁨󠀳󠀴󠁿 Flag for Ubon Ratchathani (TH-34)
🏴󠁴󠁨󠀷󠀲󠁿 Flag for Suphanburi (TH-72)
🏴󠁴󠁨󠀷󠀴󠁿 Flag for Samut Sakhon (TH-74)
🏴󠁴󠁨󠀶󠀷󠁿 Flag for Phetchabun (TH-67)
🏴󠁴󠁨󠀷󠀱󠁿 Flag for Kanchanaburi (TH-71)
🏴󠁴󠁨󠀵󠀴󠁿 Flag for Phrae (TH-54)
🏴󠁴󠁨󠀶󠀳󠁿 Flag for Tak (TH-63)
🏴󠁴󠁨󠀶󠀴󠁿 Flag for Sukhothai (TH-64)
🏴󠁴󠁨󠀴󠀸󠁿 Flag for Nakhon Phanom (TH-48)
🏴󠁴󠁨󠀵󠀱󠁿 Flag for Lamphun (TH-51)
🏴󠁴󠁨󠀵󠀸󠁿 Flag for Mae Hong Son (TH-58)
🏴󠁴󠁨󠀴󠀷󠁿 Flag for Sakon Nakhon (TH-47)
🏴󠁴󠁨󠀵󠀶󠁿 Flag for Phayao (TH-56)
🏴󠁴󠁨󠀴󠀱󠁿 Flag for Udon Thani (TH-41)
🏴󠁴󠁨󠀳󠀷󠁿 Flag for Amnat Charoen (TH-37)
🏴󠁴󠁨󠀵󠀲󠁿 Flag for Lampang (TH-52)
🏴󠁴󠁨󠀴󠀹󠁿 Flag for Mukdahan (TH-49)
🏴󠁴󠁨󠀷󠀳󠁿 Flag for Nakhon Pathom (TH-73)
🏴󠁴󠁨󠀵󠀷󠁿 Flag for Chiang Rai (TH-57)
🏴󠁴󠁨󠀴󠀰󠁿 Flag for Khon Kaen (TH-40)
🏴󠁴󠁨󠀷󠀰󠁿 Flag for Ratchaburi (TH-70)
🏴󠁴󠁨󠀳󠀵󠁿 Flag for Yasothon (TH-35)
🏴󠁴󠁨󠀶󠀰󠁿 Flag for Nakhon Sawan (TH-60)
🏴󠁴󠁨󠀴󠀴󠁿 Flag for Maha Sarakham (TH-44)
🏴󠁴󠁨󠀴󠀵󠁿 Flag for Roi Et (TH-45)
🏴󠁴󠁨󠀴󠀶󠁿 Flag for Kalasin (TH-46)
🏴󠁴󠁨󠀴󠀲󠁿 Flag for Loei (TH-42)
🏴󠁴󠁨󠀳󠀳󠁿 Flag for Si Sa Ket (TH-33)
🏴󠁴󠁨󠀶󠀱󠁿 Flag for Uthai Thani (TH-61)
🏴󠁴󠁨󠀳󠀸󠁿 Flag for Bueng Kan (TH-38)
🏴󠁴󠁨󠀵󠀵󠁿 Flag for Nan (TH-55)
🏴󠁴󠁨󠀳󠀹󠁿 Flag for Nong Bua Lam Phu (TH-39)
🏴󠁴󠁨󠀵󠀳󠁿 Flag for Uttaradit (TH-53)
🏴󠁴󠁨󠀶󠀶󠁿 Flag for Phichit (TH-66)
🏴󠁴󠁨󠀴󠀳󠁿 Flag for Nong Khai (TH-43)
🏴󠁴󠁨󠀶󠀵󠁿 Flag for Phitsanulok (TH-65)
🏴󠁴󠁨󠀵󠀰󠁿 Flag for Chiang Mai (TH-50)
🏴󠁴󠁬󠁥󠁲󠁿 Flag for Ermera (TL-ER)
🏴󠁴󠁬󠁬󠁩󠁿 Flag for Liquiçá (TL-LI)
🏴󠁴󠁬󠁭󠁦󠁿 Flag for Manufahi (TL-MF)
🏴󠁴󠁪󠁤󠁵󠁿 Flag for Dushanbe (TJ-DU)
🏴󠁴󠁨󠀷󠀶󠁿 Flag for Phetchaburi (TH-76)
🏴󠁴󠁬󠁢󠁯󠁿 Flag for Bobonaro (TL-BO)
🏴󠁴󠁬󠁭󠁴󠁿 Flag for Manatuto (TL-MT)
🏴󠁴󠁪󠁫󠁴󠁿 Flag for Khatlon (TJ-KT)
🏴󠁴󠁬󠁡󠁮󠁿 Flag for Ainaro (TL-AN)
🏴󠁴󠁨󠀸󠀲󠁿 Flag for Phang Nga (TH-82)
🏴󠁴󠁬󠁣󠁯󠁿 Flag for Cova Lima (TL-CO)
🏴󠁴󠁬󠁡󠁬󠁿 Flag for Aileu (TL-AL)
🏴󠁴󠁨󠀸󠀵󠁿 Flag for Ranong (TH-85)
🏴󠁴󠁨󠀸󠀰󠁿 Flag for Nakhon Si Thammarat (TH-80)
🏴󠁴󠁨󠀷󠀷󠁿 Flag for Prachuap Khiri Khan (TH-77)
🏴󠁴󠁨󠀹󠀵󠁿 Flag for Yala (TH-95)
🏴󠁴󠁭󠁬󠁿 Flag for Lebap (TM-L)
🏴󠁴󠁨󠀸󠀴󠁿 Flag for Surat Thani (TH-84)
🏴󠁴󠁨󠀹󠀶󠁿 Flag for Narathiwat (TH-96)
🏴󠁴󠁭󠁡󠁿 Flag for Ahal (TM-A)
🏴󠁴󠁨󠀹󠀲󠁿 Flag for Trang (TH-92)
👨🏼‍👨🏼‍👦🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁴󠁬󠁢󠁡󠁿 Flag for Baucau (TL-BA)
🏴󠁴󠁮󠀱󠀱󠁿 Flag for Tunis (TN-11)
🏴󠁴󠁨󠁳󠁿 Flag for Pattaya (TH-S)
🏴󠁴󠁪󠁳󠁵󠁿 Flag for Sughd (TJ-SU)
🏴󠁴󠁬󠁶󠁩󠁿 Flag for Viqueque (TL-VI)
🏴󠁴󠁨󠀹󠀴󠁿 Flag for Pattani (TH-94)
🏴󠁴󠁨󠀸󠀱󠁿 Flag for Krabi (TH-81)
🏴󠁴󠁭󠁢󠁿 Flag for Balkan (TM-B)
🏴󠁴󠁬󠁤󠁩󠁿 Flag for Dili (TL-DI)
🏴󠁴󠁬󠁯󠁥󠁿 Flag for Oecusse (TL-OE)
🏴󠁴󠁨󠀸󠀳󠁿 Flag for Phuket (TH-83)
🏴󠁴󠁨󠀹󠀱󠁿 Flag for Satun (TH-91)
🏴󠁴󠁨󠀹󠀰󠁿 Flag for Songkhla (TH-90)
🏴󠁴󠁪󠁲󠁡󠁿 Flag for Nohiyahoi Tobei Jumhurí (TJ-RA)
🏴󠁴󠁭󠁭󠁿 Flag for Mary (TM-M)
🏴󠁴󠁭󠁤󠁿 Flag for Daşoguz (TM-D)
🏴󠁴󠁮󠀴󠀱󠁿 Flag for Kairouan (TN-41)
🏴󠁴󠁮󠀳󠀱󠁿 Flag for Béja (TN-31)
🏴󠁴󠁮󠀸󠀲󠁿 Flag for Medenine (TN-82)
🏴󠁴󠁮󠀲󠀱󠁿 Flag for Nabeul (TN-21)
🏴󠁴󠁮󠀵󠀳󠁿 Flag for Mahdia (TN-53)
🏴󠁴󠁯󠀰󠀲󠁿 Flag for Haʻapai (TO-02)
🏴󠁴󠁲󠀰󠀵󠁿 Flag for Amasya (TR-05)
🏴󠁴󠁲󠀱󠀳󠁿 Flag for Bitlis (TR-13)
🏴󠁴󠁲󠀰󠀹󠁿 Flag for Aydın (TR-09)
🏴󠁴󠁮󠀷󠀳󠁿 Flag for Kebili (TN-73)
🏴󠁴󠁲󠀱󠀰󠁿 Flag for Balıkesir (TR-10)
🏴󠁴󠁯󠀰󠀱󠁿 Flag for ʻEua (TO-01)
🏴󠁴󠁮󠀸󠀳󠁿 Flag for Tataouine (TN-83)
🏴󠁴󠁮󠀱󠀲󠁿 Flag for Ariana (TN-12)
🏴󠁴󠁲󠀰󠀶󠁿 Flag for Ankara (TR-06)
🏴󠁴󠁮󠀲󠀳󠁿 Flag for Bizerte (TN-23)
🏴󠁴󠁲󠀱󠀴󠁿 Flag for Bolu (TR-14)
🏴󠁴󠁮󠀸󠀱󠁿 Flag for Gabès (TN-81)
🏴󠁴󠁲󠀰󠀴󠁿 Flag for Ağrı (TR-04)
🏴󠁴󠁲󠀱󠀱󠁿 Flag for Bilecik (TR-11)
🏴󠁴󠁮󠀳󠀲󠁿 Flag for Jendouba (TN-32)
🏴󠁴󠁮󠀵󠀲󠁿 Flag for Monastir (TN-52)
🏴󠁴󠁯󠀰󠀴󠁿 Flag for Tongatapu (TO-04)
🏴󠁴󠁲󠀰󠀲󠁿 Flag for Adıyaman (TR-02)
🏴󠁴󠁮󠀵󠀱󠁿 Flag for Sousse (TN-51)
🏴󠁴󠁮󠀳󠀳󠁿 Flag for Kef (TN-33)
🏴󠁴󠁮󠀲󠀲󠁿 Flag for Zaghouan (TN-22)
🏴󠁴󠁲󠀰󠀱󠁿 Flag for Adana (TR-01)
🏴󠁴󠁯󠀰󠀳󠁿 Flag for Niuas (TO-03)
🏴󠁴󠁮󠀷󠀲󠁿 Flag for Tozeur (TN-72)
🏴󠁴󠁲󠀰󠀸󠁿 Flag for Artvin (TR-08)
🏴󠁴󠁮󠀱󠀴󠁿 Flag for Manouba (TN-14)
🏴󠁴󠁮󠀴󠀲󠁿 Flag for Kasserine (TN-42)
🏴󠁴󠁮󠀱󠀳󠁿 Flag for Ben Arous (TN-13)
🏴󠁴󠁮󠀳󠀴󠁿 Flag for Siliana (TN-34)
🏴󠁴󠁯󠀰󠀵󠁿 Flag for Vavaʻu (TO-05)
🏴󠁴󠁮󠀶󠀱󠁿 Flag for Sfax (TN-61)
🏴󠁴󠁮󠀴󠀳󠁿 Flag for Sidi Bouzid (TN-43)
🏴󠁴󠁲󠀰󠀷󠁿 Flag for Antalya (TR-07)
🏴󠁴󠁲󠀱󠀲󠁿 Flag for Bingöl (TR-12)
🏴󠁴󠁲󠀲󠀴󠁿 Flag for Erzincan (TR-24)
🏴󠁴󠁲󠀴󠀶󠁿 Flag for Kahramanmaraş (TR-46)
🏴󠁴󠁲󠀳󠀶󠁿 Flag for Kars (TR-36)
🏴󠁴󠁲󠀵󠀳󠁿 Flag for Rize (TR-53)
🏴󠁴󠁲󠀵󠀵󠁿 Flag for Samsun (TR-55)
🏴󠁴󠁲󠀴󠀱󠁿 Flag for Kocaeli (TR-41)
🏴󠁴󠁲󠀱󠀸󠁿 Flag for Çankırı (TR-18)
🏴󠁴󠁲󠀴󠀸󠁿 Flag for Muğla (TR-48)
🏴󠁴󠁲󠀵󠀱󠁿 Flag for Niğde (TR-51)
🏴󠁴󠁲󠀳󠀸󠁿 Flag for Kayseri (TR-38)
🏴󠁴󠁲󠀴󠀲󠁿 Flag for Konya (TR-42)
🏴󠁴󠁲󠀲󠀲󠁿 Flag for Edirne (TR-22)
🏴󠁴󠁲󠀲󠀹󠁿 Flag for Gümüşhane (TR-29)
🏴󠁴󠁲󠀲󠀱󠁿 Flag for Diyarbakır (TR-21)
🏴󠁴󠁲󠀳󠀴󠁿 Flag for Istanbul (TR-34)
🏴󠁴󠁲󠀵󠀲󠁿 Flag for Ordu (TR-52)
🏴󠁴󠁲󠀱󠀵󠁿 Flag for Burdur (TR-15)
🏴󠁴󠁲󠀴󠀵󠁿 Flag for Manisa (TR-45)
🏴󠁴󠁲󠀲󠀵󠁿 Flag for Erzurum (TR-25)
🏴󠁴󠁲󠀳󠀲󠁿 Flag for Isparta (TR-32)
🏴󠁴󠁲󠀳󠀰󠁿 Flag for Hakkâri (TR-30)
🏴󠁴󠁲󠀱󠀶󠁿 Flag for Bursa (TR-16)
🏴󠁴󠁲󠀴󠀹󠁿 Flag for Muş (TR-49)
🏴󠁴󠁲󠀵󠀴󠁿 Flag for Sakarya (TR-54)
🏴󠁴󠁲󠀵󠀰󠁿 Flag for Nevşehir (TR-50)
🏴󠁴󠁲󠀳󠀳󠁿 Flag for Mersin (TR-33)
🏴󠁴󠁲󠀵󠀶󠁿 Flag for Siirt (TR-56)
🏴󠁴󠁲󠀴󠀷󠁿 Flag for Mardin (TR-47)
🏴󠁴󠁲󠀲󠀳󠁿 Flag for Elazığ (TR-23)
🏴󠁴󠁲󠀲󠀸󠁿 Flag for Giresun (TR-28)
🏴󠁴󠁲󠀲󠀶󠁿 Flag for Eskişehir (TR-26)
🏴󠁴󠁲󠀲󠀰󠁿 Flag for Denizli (TR-20)
🏴󠁴󠁲󠀱󠀹󠁿 Flag for Çorum (TR-19)
🏴󠁴󠁲󠀳󠀷󠁿 Flag for Kastamonu (TR-37)
🏴󠁴󠁲󠀲󠀷󠁿 Flag for Gaziantep (TR-27)
🏴󠁴󠁲󠀳󠀱󠁿 Flag for Hatay (TR-31)
🏴󠁴󠁲󠀴󠀰󠁿 Flag for Kırşehir (TR-40)
🏴󠁴󠁲󠀱󠀷󠁿 Flag for Çanakkale (TR-17)
🏴󠁴󠁲󠀴󠀴󠁿 Flag for Malatya (TR-44)
🏴󠁴󠁲󠀳󠀹󠁿 Flag for Kırklareli (TR-39)
🏴󠁴󠁲󠀶󠀳󠁿 Flag for Şanlıurfa (TR-63)
🏴󠁴󠁲󠀵󠀸󠁿 Flag for Sivas (TR-58)
🏴󠁴󠁴󠁣󠁴󠁴󠁿 Flag for Couva-Tabaquite-Talparo (TT-CTT)
🏴󠁴󠁴󠁴󠁯󠁢󠁿 Flag for Tobago (TT-TOB)
🏴󠁴󠁲󠀵󠀷󠁿 Flag for Sinop (TR-57)
🏴󠁴󠁴󠁡󠁲󠁩󠁿 Flag for Arima (TT-ARI)
🏴󠁴󠁴󠁭󠁲󠁣󠁿 Flag for Mayaro-Rio Claro (TT-MRC)
🏴󠁴󠁲󠀶󠀷󠁿 Flag for Zonguldak (TR-67)
🏴󠁴󠁲󠀷󠀲󠁿 Flag for Batman (TR-72)
🏴󠁴󠁲󠀷󠀹󠁿 Flag for Kilis (TR-79)
🏴󠁴󠁲󠀶󠀸󠁿 Flag for Aksaray (TR-68)
🏴󠁴󠁴󠁤󠁭󠁮󠁿 Flag for Diego Martin (TT-DMN)
🏴󠁴󠁴󠁰󠁥󠁤󠁿 Flag for Penal-Debe (TT-PED)
🏴󠁴󠁴󠁣󠁨󠁡󠁿 Flag for Chaguanas (TT-CHA)
🏴󠁴󠁲󠀸󠀰󠁿 Flag for Osmaniye (TR-80)
🏴󠁴󠁲󠀷󠀷󠁿 Flag for Yalova (TR-77)
🏴󠁴󠁴󠁳󠁪󠁬󠁿 Flag for San Juan-Laventille (TT-SJL)
🏴󠁴󠁲󠀷󠀸󠁿 Flag for Karabük (TR-78)
🏴󠁴󠁲󠀶󠀶󠁿 Flag for Yozgat (TR-66)
🏴󠁴󠁲󠀶󠀱󠁿 Flag for Trabzon (TR-61)
🏴󠁴󠁴󠁰󠁲󠁴󠁿 Flag for Princes Town (TT-PRT)
🏴󠁴󠁲󠀶󠀴󠁿 Flag for Uşak (TR-64)
🏴󠁴󠁴󠁴󠁵󠁰󠁿 Flag for Tunapuna-Piarco (TT-TUP)
🏴󠁴󠁲󠀶󠀹󠁿 Flag for Bayburt (TR-69)
🏴󠁴󠁲󠀷󠀴󠁿 Flag for Bartın (TR-74)
🏴󠁴󠁲󠀷󠀱󠁿 Flag for Kırıkkale (TR-71)
🏴󠁴󠁴󠁳󠁦󠁯󠁿 Flag for San Fernando (TT-SFO)
🏴󠁴󠁲󠀷󠀶󠁿 Flag for Iğdır (TR-76)
🏴󠁴󠁲󠀷󠀵󠁿 Flag for Ardahan (TR-75)
🏴󠁴󠁲󠀷󠀳󠁿 Flag for Şırnak (TR-73)
🏴󠁴󠁴󠁰󠁴󠁦󠁿 Flag for Point Fortin (TT-PTF)
🏴󠁴󠁲󠀶󠀲󠁿 Flag for Tunceli (TR-62)
🏴󠁴󠁲󠀵󠀹󠁿 Flag for Tekirdağ (TR-59)
🏴󠁴󠁲󠀶󠀰󠁿 Flag for Tokat (TR-60)
🏴󠁴󠁴󠁰󠁯󠁳󠁿 Flag for Port of Spain (TT-POS)
🏴󠁴󠁲󠀷󠀰󠁿 Flag for Karaman (TR-70)
🏴󠁴󠁴󠁳󠁩󠁰󠁿 Flag for Siparia (TT-SIP)
🏴󠁴󠁲󠀶󠀵󠁿 Flag for Van (TR-65)
🏴󠁴󠁷󠁴󠁴󠁴󠁿 Flag for Taitung (TW-TTT)
🏴󠁴󠁺󠀰󠀲󠁿 Flag for Dar es Salaam (TZ-02)
🏴󠁴󠁶󠁶󠁡󠁩󠁿 Flag for Vaitupu (TV-VAI)
🏴󠁴󠁷󠁮󠁷󠁴󠁿 Flag for New Taipei (TW-NWT)
🏴󠁴󠁺󠀰󠀹󠁿 Flag for Kilimanjaro (TZ-09)
🏴󠁴󠁺󠀰󠀸󠁿 Flag for Kigoma (TZ-08)
🏴󠁴󠁷󠁫󠁩󠁮󠁿 Flag for Kinmen (TW-KIN)
🏴󠁴󠁷󠁴󠁮󠁮󠁿 Flag for Tainan (TW-TNN)
🏴󠁴󠁶󠁮󠁫󠁦󠁿 Flag for Nukufetau (TV-NKF)
🏴󠁴󠁺󠀰󠀷󠁿 Flag for Zanzibar North (TZ-07)
🏴󠁴󠁷󠁫󠁨󠁨󠁿 Flag for Kaohsiung (TW-KHH)
🏴󠁴󠁷󠁰󠁩󠁦󠁿 Flag for Pingtung (TW-PIF)
🏴󠁴󠁷󠁩󠁬󠁡󠁿 Flag for Yilan (TW-ILA)
🏴󠁴󠁷󠁴󠁡󠁯󠁿 Flag for Taoyuan (TW-TAO)
🏴󠁴󠁺󠀰󠀳󠁿 Flag for Dodoma (TZ-03)
🏴󠁴󠁶󠁮󠁭󠁡󠁿 Flag for Nanumea (TV-NMA)
🏴󠁴󠁺󠀰󠀶󠁿 Flag for North Pemba (TZ-06)
🏴󠁴󠁺󠀰󠀴󠁿 Flag for Iringa (TZ-04)
🏴󠁴󠁷󠁹󠁵󠁮󠁿 Flag for Yunlin (TW-YUN)
🏴󠁴󠁷󠁴󠁰󠁥󠁿 Flag for Taipei (TW-TPE)
🏴󠁴󠁶󠁮󠁭󠁧󠁿 Flag for Nanumanga (TV-NMG)
🏴󠁴󠁷󠁬󠁩󠁥󠁿 Flag for Lienchiang (TW-LIE)
🏴󠁴󠁷󠁣󠁨󠁡󠁿 Flag for Changhua (TW-CHA)
🏴󠁴󠁺󠀰󠀵󠁿 Flag for Kagera (TZ-05)
🏴󠁴󠁶󠁮󠁵󠁩󠁿 Flag for Nui (TV-NUI)
🏴󠁴󠁷󠁣󠁹󠁩󠁿 Flag for Chiayi County (TW-CYI)
🏴󠁴󠁷󠁰󠁥󠁮󠁿 Flag for Penghu (TW-PEN)
🏴󠁴󠁷󠁮󠁡󠁮󠁿 Flag for Nantou (TW-NAN)
🏴󠁴󠁷󠁣󠁹󠁱󠁿 Flag for Chiayi (TW-CYQ)
🏴󠁴󠁺󠀰󠀱󠁿 Flag for Arusha (TZ-01)
🏴󠁴󠁷󠁨󠁵󠁡󠁿 Flag for Hualien (TW-HUA)
🏴󠁴󠁷󠁴󠁸󠁧󠁿 Flag for Taichung (TW-TXG)
🏴󠁴󠁷󠁫󠁥󠁥󠁿 Flag for Keelung (TW-KEE)
🏴󠁴󠁷󠁭󠁩󠁡󠁿 Flag for Miaoli (TW-MIA)
🏴󠁴󠁺󠀱󠀹󠁿 Flag for Pwani (TZ-19)
🏴󠁴󠁺󠀱󠀲󠁿 Flag for Lindi (TZ-12)
🏴󠁴󠁺󠀲󠀶󠁿 Flag for Manyara (TZ-26)
🏴󠁵󠁡󠀰󠀹󠁿 Flag for Luhanshchyna (UA-09)
🏴󠁴󠁺󠀲󠀰󠁿 Flag for Rukwa (TZ-20)
🏴󠁵󠁡󠀱󠀲󠁿 Flag for Dnipropetrovshchyna (UA-12)
🏴󠁵󠁡󠀰󠀷󠁿 Flag for Volyn (UA-07)
🏴󠁴󠁺󠀲󠀲󠁿 Flag for Shinyanga (TZ-22)
🏴󠁴󠁺󠀱󠀵󠁿 Flag for Zanzibar Urban/West (TZ-15)
🏴󠁴󠁺󠀲󠀱󠁿 Flag for Ruvuma (TZ-21)
🏴󠁴󠁺󠀲󠀸󠁿 Flag for Katavi (TZ-28)
🏴󠁵󠁡󠀳󠀲󠁿 Flag for Kyivshchyna (UA-32)
🏴󠁴󠁺󠀲󠀳󠁿 Flag for Singida (TZ-23)
🏴󠁴󠁺󠀲󠀴󠁿 Flag for Tabora (TZ-24)
🏴󠁵󠁡󠀲󠀶󠁿 Flag for Prykarpattia (UA-26)
🏴󠁴󠁺󠀲󠀷󠁿 Flag for Geita (TZ-27)
🏴󠁴󠁺󠀳󠀰󠁿 Flag for Simiyu (TZ-30)
🏴󠁵󠁡󠀴󠀸󠁿 Flag for Mykolayivschyna (UA-48)
🏴󠁳󠁮󠁳󠁬󠁿 Flag for Saint-Louis (SN-SL)
🏴󠁵󠁡󠀵󠀶󠁿 Flag for Rivnenshchyna (UA-56)
🏴󠁵󠁡󠀵󠀳󠁿 Flag for Poltavshchyna (UA-53)
🏴󠁴󠁺󠀱󠀴󠁿 Flag for Mbeya (TZ-14)
🏴󠁴󠁺󠀱󠀸󠁿 Flag for Mwanza (TZ-18)
🏴󠁴󠁺󠀱󠀳󠁿 Flag for Mara (TZ-13)
🏴󠁵󠁡󠀲󠀱󠁿 Flag for Zakarpattia (UA-21)
🏴󠁴󠁺󠀱󠀰󠁿 Flag for South Pemba (TZ-10)
🏴󠁵󠁡󠀲󠀳󠁿 Flag for Zaporizhzhya (UA-23)
🏴󠁴󠁺󠀱󠀷󠁿 Flag for Mtwara (TZ-17)
🏴󠁵󠁡󠀴󠀰󠁿 Flag for Sevastopol (UA-40)
🏴󠁵󠁡󠀰󠀵󠁿 Flag for Vinnychchyna (UA-05)
🏴󠁵󠁡󠀵󠀱󠁿 Flag for Odeshchyna (UA-51)
🏴󠁵󠁡󠀴󠀶󠁿 Flag for Lvivshchyna (UA-46)
🏴󠁵󠁡󠀳󠀵󠁿 Flag for Kirovohradschyna (UA-35)
🏴󠁵󠁡󠀱󠀴󠁿 Flag for Donechchyna (UA-14)
🏴󠁴󠁺󠀱󠀶󠁿 Flag for Morogoro (TZ-16)
🏴󠁴󠁺󠀲󠀹󠁿 Flag for Njombe (TZ-29)
🏴󠁵󠁡󠀴󠀳󠁿 Flag for Crimea (UA-43)
🏴󠁵󠁡󠀷󠀷󠁿 Flag for Chernivtsi Oblast (UA-77)
🏴󠁵󠁭󠀹󠀵󠁿 Flag for Palmyra Atoll (UM-95)
👨🏽‍👨🏽‍👦🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁵󠁳󠁩󠁡󠁿 Flag for Iowa (US-IA)
🏴󠁵󠁭󠀸󠀴󠁿 Flag for Howland Island (UM-84)
🏴󠁵󠁳󠁡󠁲󠁿 Flag for Arkansas (US-AR)
🏴󠁵󠁡󠀶󠀳󠁿 Flag for Kharkivshchyna (UA-63)
🏴󠁵󠁡󠀵󠀹󠁿 Flag for Sumshchyna (UA-59)
🏴󠁵󠁭󠀸󠀱󠁿 Flag for Baker Island (UM-81)
🏴󠁵󠁳󠁧󠁵󠁿 Flag for Guam (US-GU)
🏴󠁵󠁡󠀶󠀱󠁿 Flag for Ternopilshchyna (UA-61)
🏴󠁵󠁳󠁦󠁬󠁿 Flag for Florida (US-FL)
🏴󠁵󠁧󠁥󠁿 Flag for Eastern (UG-E)
🏴󠁵󠁭󠀷󠀹󠁿 Flag for Wake Island (UM-79)
🏴󠁵󠁭󠀸󠀹󠁿 Flag for Kingman Reef (UM-89)
🏴󠁵󠁡󠀶󠀵󠁿 Flag for Khersonshchyna (UA-65)
🏴󠁵󠁳󠁡󠁬󠁿 Flag for Alabama (US-AL)
🏴󠁵󠁭󠀷󠀱󠁿 Flag for Midway Atoll (UM-71)
🏴󠁵󠁳󠁡󠁳󠁿 Flag for American Samoa (US-AS)
🏴󠁵󠁳󠁩󠁤󠁿 Flag for Idaho (US-ID)
🏴󠁵󠁧󠁮󠁿 Flag for Northern (UG-N)
🏴󠁵󠁳󠁣󠁴󠁿 Flag for Connecticut (US-CT)
🏴󠁵󠁧󠁷󠁿 Flag for Western (UG-W)
🏴󠁵󠁡󠀶󠀸󠁿 Flag for Khmelnychchyna (UA-68)
🏴󠁵󠁭󠀸󠀶󠁿 Flag for Jarvis Island (UM-86)
🏴󠁵󠁭󠀷󠀶󠁿 Flag for Navassa Island (UM-76)
🏴󠁵󠁳󠁨󠁩󠁿 Flag for Hawaii (US-HI)
🏴󠁵󠁳󠁡󠁺󠁿 Flag for Arizona (US-AZ)
🏴󠁵󠁳󠁩󠁬󠁿 Flag for Illinois (US-IL)
🏴󠁵󠁡󠀷󠀴󠁿 Flag for Chernihivshchyna (UA-74)
🏴󠁵󠁳󠁤󠁥󠁿 Flag for Delaware (US-DE)
🏴󠁵󠁳󠁧󠁡󠁿 Flag for Georgia (US-GA)
🏴󠁵󠁳󠁤󠁣󠁿 Flag for Washington DC (US-DC)
🏴󠁵󠁭󠀶󠀷󠁿 Flag for Johnston Atoll (UM-67)
🏴󠁵󠁳󠁩󠁮󠁿 Flag for Indiana (US-IN)
🏴󠁵󠁡󠀷󠀱󠁿 Flag for Cherkashchyna (UA-71)
🏴󠁵󠁳󠁶󠁩󠁿 Flag for U.S. Virgin Islands (US-VI)
🏴󠁵󠁳󠁶󠁡󠁿 Flag for Virginia (US-VA)
🏴󠁵󠁳󠁰󠁡󠁿 Flag for Pennsylvania (US-PA)
🏴󠁵󠁳󠁷󠁩󠁿 Flag for Wisconsin (US-WI)
🏴󠁵󠁳󠁵󠁭󠁿 Flag for U.S. Outlying Islands (US-UM)
🏴󠁵󠁳󠁯󠁨󠁿 Flag for Ohio (US-OH)
🏴󠁵󠁳󠁯󠁫󠁿 Flag for Oklahoma (US-OK)
🏴󠁵󠁳󠁮󠁹󠁿 Flag for New York (US-NY)
🏴󠁵󠁳󠁮󠁨󠁿 Flag for New Hampshire (US-NH)
🏴󠁵󠁳󠁭󠁮󠁿 Flag for Minnesota (US-MN)
🏴󠁵󠁳󠁮󠁣󠁿 Flag for North Carolina (US-NC)
🏴󠁵󠁳󠁷󠁶󠁿 Flag for West Virginia (US-WV)
👨🏾‍👨🏾‍👦🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁵󠁹󠁡󠁲󠁿 Flag for Artigas (UY-AR)
🏴󠁵󠁳󠁰󠁲󠁿 Flag for Puerto Rico (US-PR)
🏴󠁵󠁳󠁵󠁴󠁿 Flag for Utah (US-UT)
🏴󠁵󠁳󠁭󠁥󠁿 Flag for Maine (US-ME)
🏴󠁵󠁹󠁣󠁡󠁿 Flag for Canelones (UY-CA)
🏴󠁵󠁳󠁮󠁭󠁿 Flag for New Mexico (US-NM)
🏴󠁵󠁳󠁷󠁡󠁿 Flag for Washington (US-WA)
🏴󠁵󠁳󠁴󠁸󠁿 Flag for Texas (US-TX)
🏴󠁵󠁳󠁬󠁡󠁿 Flag for Louisiana (US-LA)
🏴󠁵󠁳󠁭󠁳󠁿 Flag for Mississippi (US-MS)
🏴󠁵󠁳󠁮󠁶󠁿 Flag for Nevada (US-NV)
🏴󠁵󠁳󠁷󠁹󠁿 Flag for Wyoming (US-WY)
🏴󠁵󠁳󠁭󠁤󠁿 Flag for Maryland (US-MD)
🏴󠁵󠁳󠁭󠁯󠁿 Flag for Missouri (US-MO)
🏴󠁵󠁳󠁲󠁩󠁿 Flag for Rhode Island (US-RI)
🏴󠁵󠁳󠁭󠁩󠁿 Flag for Michigan (US-MI)
🏴󠁵󠁳󠁯󠁲󠁿 Flag for Oregon (US-OR)
🏴󠁵󠁳󠁳󠁣󠁿 Flag for South Carolina (US-SC)
🏴󠁵󠁳󠁮󠁪󠁿 Flag for New Jersey (US-NJ)
🏴󠁵󠁺󠁳󠁡󠁿 Flag for Samarqand (UZ-SA)
🏴󠁵󠁹󠁭󠁡󠁿 Flag for Maldonado (UY-MA)
🏴󠁵󠁺󠁮󠁧󠁿 Flag for Namangan (UZ-NG)
🏴󠁵󠁹󠁴󠁡󠁿 Flag for Tacuarembó (UY-TA)
🏴󠁵󠁺󠁳󠁩󠁿 Flag for Sirdaryo (UZ-SI)
🏴󠁵󠁹󠁳󠁡󠁿 Flag for Salto (UY-SA)
🏴󠁵󠁹󠁣󠁬󠁿 Flag for Cerro Largo (UY-CL)
🏴󠁵󠁺󠁸󠁯󠁿 Flag for Xorazm (UZ-XO)
🏴󠁶󠁣󠀰󠀵󠁿 Flag for Saint Patrick (VC-05)
🏴󠁶󠁥󠁢󠁿 Flag for Anzoátegui (VE-B)
🏴󠁶󠁣󠀰󠀲󠁿 Flag for Saint Andrew (VC-02)
🏴󠁵󠁹󠁳󠁯󠁿 Flag for Soriano (UY-SO)
🏴󠁵󠁹󠁲󠁮󠁿 Flag for Río Negro (UY-RN)
🏴󠁶󠁥󠁡󠁿 Flag for Capital (VE-A)
🏴󠁵󠁹󠁤󠁵󠁿 Flag for Durazno (UY-DU)
🏴󠁵󠁹󠁭󠁯󠁿 Flag for Montevideo (UY-MO)
🏴󠁶󠁣󠀰󠀶󠁿 Flag for Grenadines (VC-06)
🏴󠁵󠁹󠁦󠁳󠁿 Flag for Flores (UY-FS)
🏴󠁶󠁥󠁤󠁿 Flag for Aragua (VE-D)
🏴󠁵󠁺󠁡󠁮󠁿 Flag for Andijan (UZ-AN)
🏴󠁵󠁹󠁦󠁤󠁿 Flag for Florida (UY-FD)
🏴󠁵󠁹󠁰󠁡󠁿 Flag for Paysandú (UY-PA)
🏴󠁵󠁺󠁱󠁲󠁿 Flag for Karakalpakstan (UZ-QR)
🏴󠁵󠁹󠁴󠁴󠁿 Flag for Treinta y Tres (UY-TT)
🏴󠁵󠁹󠁬󠁡󠁿 Flag for Lavalleja (UY-LA)
🏴󠁶󠁣󠀰󠀳󠁿 Flag for Saint David (VC-03)
🏴󠁵󠁺󠁳󠁵󠁿 Flag for Surxondaryo (UZ-SU)
🏴󠁵󠁹󠁣󠁯󠁿 Flag for Colonia (UY-CO)
🏴󠁵󠁺󠁴󠁯󠁿 Flag for Tashkent Province (UZ-TO)
🏴󠁵󠁺󠁱󠁡󠁿 Flag for Qashqadaryo (UZ-QA)
🏴󠁵󠁹󠁳󠁪󠁿 Flag for San José (UY-SJ)
🏴󠁶󠁣󠀰󠀱󠁿 Flag for Charlotte (VC-01)
🏴󠁵󠁹󠁲󠁯󠁿 Flag for Rocha (UY-RO)
🏴󠁵󠁺󠁦󠁡󠁿 Flag for Fergana (UZ-FA)
🏴󠁵󠁺󠁪󠁩󠁿 Flag for Jizzakh (UZ-JI)
🏴󠁵󠁺󠁴󠁫󠁿 Flag for Tashkent (UZ-TK)
🏴󠁵󠁺󠁢󠁵󠁿 Flag for Bukhara (UZ-BU)
🏴󠁵󠁺󠁮󠁷󠁿 Flag for Navoiy (UZ-NW)
🏴󠁶󠁮󠀲󠀱󠁿 Flag for Thanh Hóa (VN-21)
🏴󠁶󠁥󠁯󠁿 Flag for Nueva Esparta (VE-O)
🏴󠁶󠁥󠁺󠁿 Flag for Amazonas (VE-Z)
🏴󠁶󠁥󠁸󠁿 Flag for Vargas (VE-X)
🏴󠁶󠁮󠀱󠀴󠁿 Flag for Hòa Bình (VN-14)
🏴󠁶󠁮󠀲󠀴󠁿 Flag for Quảng Bình (VN-24)
🏴󠁶󠁥󠁨󠁿 Flag for Cojedes (VE-H)
🏴󠁶󠁮󠀲󠀶󠁿 Flag for Thừa Thiên–Huế (VN-26)
🏴󠁶󠁥󠁬󠁿 Flag for Mérida (VE-L)
🏴󠁶󠁮󠀲󠀹󠁿 Flag for Quảng Ngãi (VN-29)
🏴󠁶󠁮󠀰󠀱󠁿 Flag for Lai Châu (VN-01)
🏴󠁶󠁮󠀰󠀹󠁿 Flag for Lạng Sơn (VN-09)
🏴󠁶󠁮󠀰󠀲󠁿 Flag for Lào Cai (VN-02)
🏴󠁶󠁥󠁩󠁿 Flag for Falcón (VE-I)
🏴󠁶󠁥󠁴󠁿 Flag for Trujillo (VE-T)
🏴󠁶󠁥󠁥󠁿 Flag for Barinas (VE-E)
🏴󠁶󠁥󠁮󠁿 Flag for Monagas (VE-N)
🏴󠁶󠁮󠀲󠀲󠁿 Flag for Nghệ An (VN-22)
🏴󠁶󠁮󠀲󠀸󠁿 Flag for Kon Tum (VN-28)
🏴󠁶󠁥󠁦󠁿 Flag for Bolívar (VE-F)
🏴󠁶󠁮󠀰󠀷󠁿 Flag for Tuyên Quang (VN-07)
🏴󠁶󠁮󠀰󠀵󠁿 Flag for Sơn La (VN-05)
🏴󠁶󠁮󠀲󠀰󠁿 Flag for Thái Bình (VN-20)
🏴󠁶󠁥󠁷󠁿 Flag for Federal Dependencies (VE-W)
🏴󠁶󠁥󠁪󠁿 Flag for Guárico (VE-J)
🏴󠁶󠁮󠀱󠀸󠁿 Flag for Ninh Bình (VN-18)
🏴󠁶󠁮󠀰󠀴󠁿 Flag for Cao Bằng (VN-04)
🏴󠁶󠁮󠀰󠀶󠁿 Flag for Yên Bái (VN-06)
🏴󠁶󠁮󠀲󠀳󠁿 Flag for Hà Tĩnh (VN-23)
🏴󠁶󠁥󠁳󠁿 Flag for Táchira (VE-S)
🏴󠁶󠁥󠁰󠁿 Flag for Portuguesa (VE-P)
🏴󠁶󠁥󠁵󠁿 Flag for Yaracuy (VE-U)
🏴󠁶󠁥󠁲󠁿 Flag for Sucre (VE-R)
🏴󠁶󠁮󠀱󠀳󠁿 Flag for Quảng Ninh (VN-13)
🏴󠁶󠁮󠀰󠀳󠁿 Flag for Hà Giang (VN-03)
🏴󠁶󠁮󠀲󠀷󠁿 Flag for Quảng Nam (VN-27)
🏴󠁶󠁥󠁭󠁿 Flag for Miranda (VE-M)
🏴󠁶󠁥󠁫󠁿 Flag for Lara (VE-K)
🏴󠁶󠁮󠁣󠁴󠁿 Flag for Can Tho (VN-CT)
🏴󠁶󠁮󠀳󠀶󠁿 Flag for Ninh Thuận (VN-36)
🏴󠁶󠁮󠀶󠀷󠁿 Flag for Nam Định (VN-67)
🏴󠁶󠁮󠀳󠀵󠁿 Flag for Lâm Đồng (VN-35)
🏴󠁶󠁮󠀶󠀱󠁿 Flag for Hải Dương (VN-61)
🏴󠁶󠁮󠀵󠀲󠁿 Flag for Sóc Trăng (VN-52)
🏴󠁶󠁮󠀷󠀳󠁿 Flag for Hậu Giang (VN-73)
🏴󠁶󠁮󠀷󠀰󠁿 Flag for Vĩnh Phúc (VN-70)
🏴󠁶󠁮󠀵󠀰󠁿 Flag for Bến Tre (VN-50)
🏴󠁶󠁮󠀵󠀴󠁿 Flag for Bắc Giang (VN-54)
🏴󠁶󠁮󠀳󠀳󠁿 Flag for Đắk Lắk (VN-33)
🏴󠁶󠁮󠀵󠀷󠁿 Flag for Bình Dương (VN-57)
🏴󠁶󠁮󠀴󠀹󠁿 Flag for Vĩnh Long (VN-49)
🏴󠁶󠁮󠀴󠀶󠁿 Flag for Tiền Giang (VN-46)
🏴󠁶󠁮󠀴󠀳󠁿 Flag for Bà Rịa–Vũng Tàu (VN-43)
🏴󠁶󠁮󠀷󠀱󠁿 Flag for Điện Biên (VN-71)
🏴󠁶󠁮󠀵󠀸󠁿 Flag for Bình Phước (VN-58)
🏴󠁶󠁮󠁤󠁮󠁿 Flag for Da Nang (VN-DN)
🏴󠁶󠁮󠀳󠀷󠁿 Flag for Tây Ninh (VN-37)
🏴󠁶󠁮󠀵󠀵󠁿 Flag for Bạc Liêu (VN-55)
🏴󠁶󠁮󠀳󠀲󠁿 Flag for Phú Yên (VN-32)
🏴󠁶󠁮󠀴󠀴󠁿 Flag for An Giang (VN-44)
🏴󠁶󠁮󠀶󠀳󠁿 Flag for Hà Nam (VN-63)
🏴󠁶󠁮󠀵󠀹󠁿 Flag for Cà Mau (VN-59)
🏴󠁶󠁮󠀴󠀷󠁿 Flag for Kiên Giang (VN-47)
🏴󠁶󠁮󠀳󠀴󠁿 Flag for Khánh Hòa (VN-34)
🏴󠁶󠁮󠀴󠀵󠁿 Flag for Đồng Tháp (VN-45)
🏴󠁶󠁮󠀳󠀹󠁿 Flag for Đồng Nai (VN-39)
🏴󠁶󠁮󠀶󠀸󠁿 Flag for Phú Thọ (VN-68)
🏴󠁶󠁮󠀵󠀶󠁿 Flag for Bắc Ninh (VN-56)
🏴󠁶󠁮󠀳󠀰󠁿 Flag for Gia Lai (VN-30)
🏴󠁶󠁮󠀷󠀲󠁿 Flag for Đắk Nông (VN-72)
🏴󠁶󠁮󠀴󠀰󠁿 Flag for Bình Thuận (VN-40)
🏴󠁶󠁮󠀴󠀱󠁿 Flag for Long An (VN-41)
🏴󠁶󠁮󠀳󠀱󠁿 Flag for Bình Định (VN-31)
🏴󠁶󠁮󠁨󠁮󠁿 Flag for Hanoi (VN-HN)
🏴󠁶󠁮󠀵󠀳󠁿 Flag for Bắc Kạn (VN-53)
🏴󠁶󠁮󠀶󠀹󠁿 Flag for Thái Nguyên (VN-69)
🏴󠁹󠁥󠁳󠁤󠁿 Flag for Sa’dah (YE-SD)
🏴󠁷󠁳󠁡󠁡󠁿 Flag for A’ana (WS-AA)
🏴󠁹󠁥󠁨󠁪󠁿 Flag for Hajjah (YE-HJ)
🏴󠁷󠁳󠁡󠁴󠁿 Flag for Atua (WS-AT)
🏴󠁷󠁦󠁳󠁧󠁿 Flag for Sigave (WF-SG)
🏴󠁷󠁳󠁶󠁦󠁿 Flag for Va’a-o-Fonoti (WS-VF)
🏴󠁹󠁥󠁨󠁵󠁿 Flag for Al Hudaydah (YE-HU)
🏴󠁷󠁳󠁡󠁬󠁿 Flag for Aiga-i-le-Tai (WS-AL)
🏴󠁷󠁳󠁳󠁡󠁿 Flag for Satupa’itea (WS-SA)
🏴󠁹󠁥󠁲󠁡󠁿 Flag for Raymah (YE-RA)
🏴󠁷󠁳󠁧󠁩󠁿 Flag for Gaga’ifomauga (WS-GI)
🏴󠁶󠁵󠁳󠁡󠁭󠁿 Flag for Sanma (VU-SAM)
🏴󠁷󠁦󠁡󠁬󠁿 Flag for Alo (WF-AL)
🏴󠁹󠁥󠁭󠁲󠁿 Flag for Al Mahrah (YE-MR)
🏴󠁹󠁥󠁡󠁤󠁿 Flag for ’Adan (YE-AD)
🏴󠁶󠁵󠁴󠁡󠁥󠁿 Flag for Tafea (VU-TAE)
🏴󠁹󠁥󠁡󠁭󠁿 Flag for Amran (YE-AM)
🏴󠁶󠁵󠁰󠁡󠁭󠁿 Flag for Penama (VU-PAM)
🏴󠁹󠁥󠁭󠁷󠁿 Flag for Al Mahwit (YE-MW)
🏴󠁹󠁥󠁤󠁡󠁿 Flag for Dhale (YE-DA)
🏴󠁷󠁳󠁧󠁥󠁿 Flag for Gaga’emauga (WS-GE)
🏴󠁹󠁥󠁪󠁡󠁿 Flag for Al Jawf (YE-JA)
👨🏻‍👨🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone
🏴󠁹󠁥󠁭󠁡󠁿 Flag for Ma’rib (YE-MA)
🏴󠁹󠁥󠁩󠁢󠁿 Flag for Ibb (YE-IB)
🏴󠁹󠁥󠁡󠁢󠁿 Flag for Abyan (YE-AB)
🏴󠁹󠁥󠁢󠁡󠁿 Flag for Al Bayda (YE-BA)
🏴󠁹󠁥󠁨󠁤󠁿 Flag for Hadramaut (YE-HD)
🏴󠁶󠁵󠁭󠁡󠁰󠁿 Flag for Malampa (VU-MAP)
🏴󠁶󠁮󠁨󠁰󠁿 Flag for Haiphong (VN-HP)
🏴󠁹󠁥󠁬󠁡󠁿 Flag for Lahij (YE-LA)
🏴󠁶󠁵󠁳󠁥󠁥󠁿 Flag for Shefa (VU-SEE)
🏴󠁶󠁵󠁴󠁯󠁢󠁿 Flag for Torba (VU-TOB)
🏴󠁹󠁥󠁳󠁨󠁿 Flag for Shabwah (YE-SH)
🏴󠁷󠁦󠁵󠁶󠁿 Flag for Uvea (WF-UV)
🏴󠁷󠁳󠁴󠁵󠁿 Flag for Tuamasaga (WS-TU)
🏴󠁹󠁥󠁤󠁨󠁿 Flag for Dhamar (YE-DH)
🏴󠁷󠁳󠁰󠁡󠁿 Flag for Palauli (WS-PA)
🏴󠁺󠁷󠁭󠁶󠁿 Flag for Masvingo (ZW-MV)
🏴󠁹󠁥󠁳󠁵󠁿 Flag for Arkhabil Suqutra (YE-SU)
🏴󠁺󠁡󠁦󠁳󠁿 Flag for Free (ZA-FS)
🏴󠁺󠁭󠀰󠀶󠁿 Flag for North-Western (ZM-06)
🏴󠁺󠁭󠀰󠀹󠁿 Flag for Lusaka (ZM-09)
👨🏼‍👨🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁺󠁷󠁭󠁮󠁿 Flag for Matabeleland North (ZW-MN)
🏴󠁺󠁡󠁬󠁰󠁿 Flag for Limpopo (ZA-LP)
🏴󠁺󠁭󠀰󠀳󠁿 Flag for Eastern (ZM-03)
🏴󠁺󠁷󠁭󠁷󠁿 Flag for Mashonaland West (ZW-MW)
🏴󠁺󠁷󠁢󠁵󠁿 Flag for Bulawayo (ZW-BU)
🏴󠁺󠁭󠀰󠀵󠁿 Flag for Northern (ZM-05)
🏴󠁺󠁭󠀰󠀱󠁿 Flag for Western (ZM-01)
🏴󠁺󠁡󠁥󠁣󠁿 Flag for Eastern Cape (ZA-EC)
🏴󠁺󠁷󠁨󠁡󠁿 Flag for Harare (ZW-HA)
🏴󠁺󠁷󠁭󠁥󠁿 Flag for Mashonaland East (ZW-ME)
🏴󠁺󠁭󠀰󠀷󠁿 Flag for Southern (ZM-07)
🏴󠁹󠁥󠁴󠁡󠁿 Flag for Taiz (YE-TA)
🏴󠁺󠁷󠁭󠁳󠁿 Flag for Matabeleland South (ZW-MS)
🏴󠁺󠁭󠀰󠀸󠁿 Flag for Copperbelt (ZM-08)
🏴󠁹󠁥󠁳󠁮󠁿 Flag for Sana’a (YE-SN)
🏴󠁺󠁭󠀱󠀰󠁿 Flag for Muchinga (ZM-10)
🏴󠁺󠁡󠁷󠁣󠁿 Flag for Western Cape (ZA-WC)
🏴󠁺󠁡󠁧󠁴󠁿 Flag for Gauteng (ZA-GT)
🏴󠁺󠁭󠀰󠀲󠁿 Flag for Central (ZM-02)
🏴󠁺󠁡󠁮󠁣󠁿 Flag for Northern Cape (ZA-NC)
🏴󠁺󠁡󠁭󠁰󠁿 Flag for Mpumalanga (ZA-MP)
🏴󠁺󠁡󠁮󠁬󠁿 Flag for KwaZulu-Natal (ZA-NL)
🏴󠁺󠁡󠁮󠁷󠁿 Flag for North West (ZA-NW)
🏴󠁺󠁷󠁭󠁡󠁿 Flag for Manicaland (ZW-MA)
🏴󠁺󠁷󠁭󠁩󠁿 Flag for Midlands (ZW-MI)
🏴󠁺󠁭󠀰󠀴󠁿 Flag for Luapula (ZM-04)
👨🏽‍👨🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁩󠁲󠀲󠀱󠁿 Flag for Mazandaran (IR-21)
👨🏾‍👨🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁬󠁴󠀲󠀰󠁿 Flag for Klaipėdos Municipality (LT-20)
🏴󠁣󠁡󠁭󠁢󠁿 Flag for Manitoba (CA-MB)
󠁸 Tag Latin Small Letter X
🏴󠁰󠁧󠁥󠁨󠁧󠁿 Flag for Eastern Highlands (PG-EHG)
🏴󠁤󠁪󠁡󠁲󠁿 Flag for Arta (DJ-AR)
🏴󠁲󠁵󠁰󠁲󠁩󠁿 Flag for Primorsky Krai (RU-PRI)
🏴󠁪󠁰󠀰󠀷󠁿 Flag for Fukushima (JP-07)
🏴󠁤󠁪󠁤󠁪󠁿 Flag for Djibouti (DJ-DJ)
🏴󠁧󠁲󠁭󠁿 Flag for Crete (GR-M)
🏴󠁴󠁶󠁮󠁩󠁴󠁿 Flag for Niutao (TV-NIT)
🏴󠁦󠁲󠁰󠁤󠁬󠁿 Flag for Pays-de-la-Loire (FR-PDL)
🏴󠁭󠁸󠁧󠁲󠁯󠁿 Flag for Guerrero (MX-GRO)
🏴󠁪󠁭󠀰󠀳󠁿 Flag for Saint Thomas (JM-03)
👩🏻‍❤️‍👩🏻 Couple With Heart - Woman: Light Skin Tone, Woman: Light Skin Tone
👩‍👨‍👦 Family: Woman, Man, Boy
🏴󠁭󠁸󠁳󠁬󠁰󠁿 Flag for San Luis Potosí (MX-SLP)
👨‍👩‍👶 Family: Man, Woman, Baby
👩‍❤️‍👩🏿 Couple With Heart - Woman, Woman: Dark Skin Tone
🏴󠁰󠁷󠀱󠀰󠀰󠁿 Flag for Kayangel (PW-100)
🏴󠁰󠁳󠁤󠁥󠁢󠁿 Flag for Deir al-Balah (PS-DEB)
🏴󠁦󠁩󠀱󠀸󠁿 Flag for Uusimaa (FI-18)
👨‍❤️‍👨🏾 Couple With Heart - Man, Man: Medium-Dark Skin Tone
🏴󠁥󠁥󠀵󠀹󠁿 Flag for Lääne-Viru (EE-59)
👨🏿‍👨🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁣󠁧󠀱󠀲󠁿 Flag for Pool (CG-12)
🏴󠁥󠁳󠁩󠁢󠁿 Flag for Balearic Islands (ES-IB)
🏴󠁮󠁡󠁫󠁥󠁿 Flag for Kavango East (NA-KE)
🏴󠁮󠁲󠀱󠀴󠁿 Flag for Yaren (NR-14)
👨🏻‍👨🏻‍👶🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁣󠁬󠁡󠁮󠁿 Flag for Antofagasta (CL-AN)
👨🏻‍👩🏻‍👦🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
👩🏻‍👦🏻‍👦🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
🏴󠁭󠁫󠀲󠀵󠁿 Flag for Demir Hisar (MK-25)
👨‍👩‍👦‍👶 Family: Man, Woman, Boy, Baby
🏴󠁥󠁥󠀳󠀷󠁿 Flag for Harju (EE-37)
🏴󠁢󠁲󠁣󠁥󠁿 Flag for Ceará (BR-CE)
🏴󠁬󠁲󠁢󠁧󠁿 Flag for Bong (LR-BG)
👨🏿‍❤️‍💋‍👩🏽 Kiss - Man: Dark Skin Tone, Woman: Medium Skin Tone
👩‍❤️‍👩🏻 Couple With Heart - Woman, Woman: Light Skin Tone
🏴󠁢󠁢󠀰󠀱󠁿 Flag for Christ Church (BB-01)
🏴󠁭󠁲󠀰󠀷󠁿 Flag for Adrar (MR-07)
🏴󠁰󠁥󠁡󠁰󠁵󠁿 Flag for Apurímac (PE-APU)
🏴󠁫󠁥󠀱󠀷󠁿 Flag for Kisumu (KE-17)
🏴󠁭󠁸󠁳󠁯󠁮󠁿 Flag for Sonora (MX-SON)
🏴󠁭󠁹󠀱󠀰󠁿 Flag for Selangor (MY-10)
🏴󠁬󠁩󠀰󠀸󠁿 Flag for Schellenberg (LI-08)
🏴󠁢󠁺󠁯󠁷󠁿 Flag for Orange Walk (BZ-OW)
👩‍👨‍👶‍👦 Family: Woman, Man, Baby, Boy
🏴󠁴󠁲󠀸󠀱󠁿 Flag for Düzce (TR-81)
👨🏿‍👩🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁧󠁥󠁡󠁢󠁿 Flag for Abkhazia (GE-AB)
🏴󠁣󠁩󠁳󠁭󠁿 Flag for Sassandra-Marahoué (CI-SM)
👩🏽‍❤️‍👩🏼 Couple With Heart - Woman: Medium Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁭󠁸󠁭󠁥󠁸󠁿 Flag for Mexico State (MX-MEX)
🏴󠁮󠁧󠁳󠁯󠁿 Flag for Sokoto (NG-SO)
🏴󠁣󠁧󠀱󠀱󠁿 Flag for Bouenza (CG-11)
🏴󠁪󠁭󠀱󠀴󠁿 Flag for Saint Catherine (JM-14)
🏴󠁰󠁥󠁡󠁲󠁥󠁿 Flag for Arequipa (PE-ARE)
🏴󠁳󠁩󠀱󠀲󠀲󠁿 Flag for Škofja Loka (SI-122)
🏴󠁬󠁡󠁢󠁫󠁿 Flag for Bokeo (LA-BK)
👩🏻‍❤️‍💋‍👨🏼 Kiss - Woman: Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁣󠁡󠁱󠁣󠁿 Flag for Quebec (CA-QC)
🏴󠁴󠁷󠁨󠁳󠁺󠁿 Flag for Hsinchu (TW-HSZ)
👨‍❤️‍💋‍👨🏼 Kiss - Man, Man: Medium-Light Skin Tone
👨🏽‍👨🏽‍👧🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁨󠁲󠀰󠀵󠁿 Flag for Varaždin (HR-05)
🏴󠁭󠁣󠁳󠁤󠁿 Flag for Sainte-Dévote Chapel (MC-SD)
👨🏻‍👨🏻‍👦🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
🏴󠁣󠁯󠁡󠁮󠁴󠁿 Flag for Antioquia (CO-ANT)
🏴󠁭󠁫󠀶󠀱󠁿 Flag for Plasnica (MK-61)
👨🏾‍❤️‍👨🏻 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Light Skin Tone
🏴󠁬󠁫󠀳󠁿 Flag for Southern (LK-3)
🏴󠁭󠁶󠁮󠁯󠁿 Flag for North Province (MV-NO)
👨‍❤️‍👩🏻 Couple With Heart - Man, Woman: Light Skin Tone
🏴󠁮󠁩󠁬󠁥󠁿 Flag for León (NI-LE)
🏴󠁳󠁤󠁲󠁳󠁿 Flag for Red Sea (SD-RS)
🏴󠁶󠁥󠁣󠁿 Flag for Apure (VE-C)
🕴🏾‍♀️ Woman in Business Suit Levitating: Medium-Dark Skin Tone
👩🏼‍❤️‍👨🏾 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁮󠁺󠁡󠁵󠁫󠁿 Flag for Auckland (NZ-AUK)
🏴󠁭󠁸󠁴󠁡󠁢󠁿 Flag for Tabasco (MX-TAB)
🏴󠁲󠁵󠁳󠁥󠁿 Flag for North Ossetia-Alania (RU-SE)
🏴󠁳󠁩󠀱󠀳󠀳󠁿 Flag for Velenje (SI-133)
🏴󠁣󠁦󠁵󠁫󠁿 Flag for Ouaka (CF-UK)
👨🏾‍👨🏾‍👧🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁤󠁺󠀰󠀸󠁿 Flag for Béchar (DZ-08)
🏴󠁣󠁮󠀹󠀲󠁿 Flag for Macau SAR China (CN-92)
🏴󠁥󠁣󠁥󠁿 Flag for Esmeraldas (EC-E)
🏴󠁦󠁲󠁢󠁬󠁿 Flag for St. Barthélemy (FR-BL)
🏴󠁨󠁵󠁥󠁧󠁿 Flag for Eger (HU-EG)
🏴󠁮󠁬󠁮󠁨󠁿 Flag for North Holland (NL-NH)
🏴󠁣󠁤󠁥󠁱󠁿 Flag for Équateur (CD-EQ)
🏴󠁵󠁳󠁭󠁴󠁿 Flag for Montana (US-MT)
🏴󠁩󠁲󠀰󠀲󠁿 Flag for West Azarbaijan (IR-02)
🏴󠁳󠁩󠀲󠀱󠀳󠁿 Flag for Ankaran (SI-213)
🏴󠁳󠁩󠀱󠀵󠀴󠁿 Flag for Dobje (SI-154)
🏴󠁣󠁯󠁮󠁡󠁲󠁿 Flag for Nariño (CO-NAR)
👨🏽‍❤️‍💋‍👨🏻 Kiss - Man: Medium Skin Tone, Man: Light Skin Tone
🏴󠁥󠁳󠁰󠁶󠁿 Flag for Basque Country (ES-PV)
🏴󠁦󠁩󠀰󠀶󠁿 Flag for Tavastia Proper (FI-06)
👨🏽‍👨🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁫󠁩󠁬󠁿 Flag for Line Islands (KI-L)
👨🏼‍❤️‍💋‍👨🏻 Kiss - Man: Medium-Light Skin Tone, Man: Light Skin Tone
👨🏿‍👨🏿‍👧🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁧󠁴󠁲󠁥󠁿 Flag for Retalhuleu (GT-RE)
🏴󠁥󠁲󠁤󠁫󠁿 Flag for Southern Red Sea (ER-DK)
🏴󠁴󠁮󠀷󠀱󠁿 Flag for Gafsa (TN-71)
🏴󠁺󠁷󠁭󠁣󠁿 Flag for Mashonaland Central (ZW-MC)
👨🏻‍👩🏻‍👶🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
🏴󠁩󠁲󠀳󠀰󠁿 Flag for Razavi Khorasan (IR-30)
👨🏻‍❤️‍👨🏻 Couple With Heart - Man: Light Skin Tone, Man: Light Skin Tone
🏴󠁩󠁴󠀴󠀵󠁿 Flag for Emilia-Romagna (IT-45)
🏴󠁥󠁳󠁶󠁣󠁿 Flag for Valencian Community (ES-VC)
👨🏻‍👨🏻‍👧🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
🏴󠁣󠁤󠁮󠁵󠁿 Flag for Nord-Ubangi (CD-NU)
🏴󠁴󠁨󠀷󠀵󠁿 Flag for Samut Songkhram (TH-75)
🏴󠁬󠁳󠁡󠁿 Flag for Maseru (LS-A)
🏴󠁫󠁥󠀲󠀵󠁿 Flag for Marsabit (KE-25)
🏴󠁤󠁺󠀰󠀱󠁿 Flag for Adrar (DZ-01)
👩🏻‍❤️‍💋‍👩🏾 Kiss - Woman: Light Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁥󠁳󠁣󠁬󠁿 Flag for Castile and León (ES-CL)
🏴󠁬󠁶󠀰󠀶󠀰󠁿 Flag for Mazsalaca (LV-060)
🏴󠁰󠁨󠀰󠀷󠁿 Flag for Central Visayas (PH-07)
🏴󠁴󠁨󠀳󠀶󠁿 Flag for Chaiyaphum (TH-36)
🏴󠁣󠁩󠁺󠁺󠁿 Flag for Zanzan (CI-ZZ)
🏴󠁳󠁶󠁵󠁳󠁿 Flag for Usulután (SV-US)
👨🏾‍👦🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁴󠁨󠀸󠀶󠁿 Flag for Chumphon (TH-86)
☿️ Mercury
🏴󠁭󠁸󠁣󠁭󠁸󠁿 Flag for Ciudad de Mexico (MX-CMX)
👨🏻‍👩🏻‍👧🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁶󠁥󠁶󠁿 Flag for Zulia (VE-V)
👨🏾‍👩🏾‍👦🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁳󠁡󠀱󠀱󠁿 Flag for Al Bahah (SA-11)
🏴󠁷󠁳󠁶󠁳󠁿 Flag for Vaisigano (WS-VS)
🏴󠁢󠁱󠁳󠁥󠁿 Flag for Sint Eustatius (BQ-SE)
🏴󠁴󠁲󠀴󠀳󠁿 Flag for Kütahya (TR-43)
🏴󠁫󠁲󠀲󠀹󠁿 Flag for Gwangju City (KR-29)
👨🏿‍❤️‍💋‍👩🏼 Kiss - Man: Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁳󠁩󠀰󠀵󠀲󠁿 Flag for Kranj (SI-052)
🏴󠁣󠁲󠁨󠁿 Flag for Heredia (CR-H)
🏴󠁦󠁩󠀰󠀱󠁿 Flag for Åland Islands (FI-01)
👩🏽‍❤️‍💋‍👨🏼 Kiss - Woman: Medium Skin Tone, Man: Medium-Light Skin Tone
🏴󠁬󠁵󠁣󠁡󠁿 Flag for Capellen (LU-CA)
🏴󠁩󠁮󠁨󠁰󠁿 Flag for Himachal Pradesh (IN-HP)
👩🏽‍❤️‍👩🏾 Couple With Heart - Woman: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁴󠁺󠀲󠀵󠁿 Flag for Tanga (TZ-25)
🏴󠁥󠁧󠁳󠁩󠁮󠁿 Flag for North Sinai (EG-SIN)
🏴󠁧󠁹󠁥󠁢󠁿 Flag for East Berbice-Corentyne (GY-EB)
🏴󠁭󠁡󠀰󠀴󠁿 Flag for Oriental (MA-04)
👨🏻‍❤️‍👨🏼 Couple With Heart - Man: Light Skin Tone, Man: Medium-Light Skin Tone
👨🏼‍👨🏼‍👧🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏻‍❤️‍👩🏽 Couple With Heart - Woman: Light Skin Tone, Woman: Medium Skin Tone
🏴󠁴󠁧󠁫󠁿 Flag for Kara (TG-K)
🏴󠁥󠁧󠁢󠁮󠁳󠁿 Flag for Beni Suef (EG-BNS)
🏴󠁴󠁨󠀹󠀳󠁿 Flag for Phatthalung (TH-93)
🏴󠁭󠁴󠀲󠀵󠁿 Flag for Luqa (MT-25)
👨🏾‍👨🏾‍👧🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👨🏿‍👩🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁳󠁩󠀰󠀲󠀷󠁿 Flag for Gorenja Vas–Poljane (SI-027)
🏴󠁮󠁧󠁤󠁥󠁿 Flag for Delta (NG-DE)
🏴󠁴󠁴󠁳󠁧󠁥󠁿 Flag for Sangre Grande (TT-SGE)
🏴󠁬󠁶󠀰󠀴󠀶󠁿 Flag for Koknese (LV-046)
🏴󠁳󠁩󠀰󠀸󠀶󠁿 Flag for Odranci (SI-086)
👩🏾‍❤️‍💋‍👨🏽 Kiss - Woman: Medium-Dark Skin Tone, Man: Medium Skin Tone
🏴󠁳󠁩󠀲󠀱󠀰󠁿 Flag for Sveti Jurij v Slovenskih Goricah (SI-210)
👩‍👨‍👦‍👧 Family: Woman, Man, Boy, Girl
🏴󠁨󠁵󠁳󠁺󠁿 Flag for Szabolcs-Szatmár-Bereg (HU-SZ)
🏴󠁭󠁤󠁣󠁳󠁿 Flag for Căușeni (MD-CS)
👩🏽‍👧🏽‍👦🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁲󠁵󠁢󠁵󠁿 Flag for Buryat (RU-BU)
߷ NKo Symbol Gbakurunen
🏴󠁫󠁨󠀲󠀰󠁿 Flag for Svay Rieng (KH-20)
🏴󠁦󠁩󠀱󠀹󠁿 Flag for Southwest Finland (FI-19)
🏴󠁭󠁫󠀰󠀲󠁿 Flag for Aračinovo (MK-02)
👩🏼‍👧🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁴󠁤󠁨󠁬󠁿 Flag for Hadjer-Lamis (TD-HL)
🏴󠁳󠁩󠀲󠀰󠀸󠁿 Flag for Log–Dragomer (SI-208)
🏴󠁪󠁰󠀲󠀱󠁿 Flag for Gifu (JP-21)
🏴󠁬󠁶󠀰󠀴󠀱󠁿 Flag for Jelgava Municipality (LV-041)
🏴󠁩󠁴󠀳󠀶󠁿 Flag for Friuli–Venezia Giulia (IT-36)
🏴󠁰󠁫󠁴󠁡󠁿 Flag for Federally Administered Tribal Areas (PK-TA)
🏴󠁭󠁴󠀶󠀲󠁿 Flag for Xewkija (MT-62)
🏴󠁭󠁲󠀱󠀰󠁿 Flag for Guidimaka (MR-10)
🏴󠁪󠁰󠀱󠀱󠁿 Flag for Saitama (JP-11)
🏴󠁣󠁵󠀹󠀹󠁿 Flag for Isla de la Juventud (CU-99)
🏴󠁳󠁩󠀱󠀲󠀵󠁿 Flag for Šmartno ob Paki (SI-125)
🏴󠁣󠁯󠁤󠁣󠁿 Flag for Capital District (CO-DC)
🏴󠁡󠁺󠁸󠁶󠁤󠁿 Flag for Khojavend (AZ-XVD)
🏴󠁬󠁶󠀱󠀰󠀶󠁿 Flag for Ventspils Municipality (LV-106)
🏴󠁭󠁶󠁳󠁣󠁿 Flag for South Central Province (MV-SC)
🏴󠁩󠁮󠁡󠁳󠁿 Flag for Assam (IN-AS)
🏴󠁬󠁴󠀰󠀲󠁿 Flag for Alytus Municipality (LT-02)
👨🏾‍❤️‍👩🏾 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
👩🏼‍❤️‍👩🏼 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁶󠁮󠀶󠀶󠁿 Flag for Hưng Yên (VN-66)
🏴󠁤󠁥󠁳󠁨󠁿 Flag for Schleswig-Holstein (DE-SH)
👨🏻‍👨🏻‍👧🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
👨🏼‍👨🏼‍👧🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁵󠁴󠁡󠁳󠁿 Flag for Tasmania (AU-TAS)
🏴󠁧󠁴󠁳󠁭󠁿 Flag for San Marcos (GT-SM)
👨🏼‍👨🏼‍👦🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁰󠁳󠁢󠁴󠁨󠁿 Flag for Bethlehem (PS-BTH)
👨🏽‍👨🏽‍👧🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
👨🏾‍👨🏾‍👧🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨🏿‍👨🏿‍👧🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
👨🏻‍👨🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone
🏴󠁤󠁥󠁮󠁷󠁿 Flag for North Rhine-Westphalia (DE-NW)
👨🏼‍👧🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁳󠁩󠀲󠀰󠀲󠁿 Flag for Središče ob Dravi (SI-202)
👨🏽‍👨🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone
👨🏼‍👩🏼‍👦🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁩󠁮󠁴󠁮󠁿 Flag for Tamil Nadu (IN-TN)
👨🏼‍👨🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👨🏾‍👨🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨🏿‍👨🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁳󠁳󠁵󠁹󠁿 Flag for Unity (SS-UY)
👨🏿‍👩🏿‍👧🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
👩‍❤️‍👨🏿 Couple With Heart - Woman, Man: Dark Skin Tone
🏴󠁥󠁳󠁣󠁢󠁿 Flag for Cantabria (ES-CB)
👩🏽‍👶🏽‍👦🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
👩🏼‍👶🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏿‍👶🏿‍👦🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
👩🏻‍👶🏻‍👧🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
👩🏼‍👶🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏽‍👶🏽‍👧🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👩🏾‍👶🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏽‍👶🏽‍👶🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👶🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👶🏿‍👶🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
👩🏼‍👨🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏽‍👨🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone
👩🏾‍👨🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏻‍👨🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone
👩🏻‍👨🏻‍👦🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
👩🏾‍👶🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏿‍👨🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone
👩🏽‍👨🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone
👩🏽‍👨🏽‍👦🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👩🏾‍👨🏾‍👦🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏿‍👨🏿‍👦🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
👩🏾‍👨🏾‍👦🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👨🏿‍👦🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
👩🏽‍👨🏽‍👦🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
👩🏼‍👨🏼‍👦🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👨🏽‍👦🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
👩🏻‍👨🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone
👩🏼‍👨🏼‍👦🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏻‍👨🏻‍👦🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👨🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏼‍👨🏼‍👦🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏻‍👨🏻‍👧🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
👩🏾‍👨🏾‍👧🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏾‍👨🏾‍👧🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏼‍👨🏼‍👧🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏿‍👨🏿‍👧🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
👩🏽‍👨🏽‍👧🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
👩🏿‍👨🏿‍👧🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
👩🏻‍👨🏻‍👧🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👨🏼‍👧🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👨🏽‍👧🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
👩🏻‍👨🏻‍👧🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
👩🏿‍👨🏿‍👧🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
👩🏻‍👨🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👨🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👨🏽‍👧🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
👩🏻‍👨🏻‍👶🏻‍👦🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
👩🏼‍👨🏼‍👶🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏾‍👨🏾‍👶🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏿‍👨🏿‍👶🏿‍👦🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
👩🏻‍👨🏻‍👶🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
👩🏼‍👨🏼‍👶🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨‍👨‍👶‍👧 Family: Man, Man, Baby, Girl
👩🏿‍👨🏿‍👶🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
👩🏽‍👨🏽‍👶🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👨🏾‍👶🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👨🏿‍👶🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
👩🏼‍👩🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏽‍👨🏽‍👶🏽‍👧🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👩🏻‍👨🏻‍👶🏻‍👶🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
👩🏻‍👩🏻‍👦🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
👩🏾‍👩🏾‍👦🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏽‍👩🏽‍👦🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👩🏽‍👩🏽‍👦🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
👩🏾‍👩🏾‍👦🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👦🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
👩🏻‍👩🏻‍👦🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👩🏼‍👦🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👩🏽‍👦🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👩🏾‍👦🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👦🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
👩🏻‍👩🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone
👩🏿‍👩🏿‍👦🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
👩🏼‍👩🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏽‍👩🏽‍👧🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
👩🏾‍👩🏾‍👧🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏻‍👩🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone
👩🏽‍👩🏽‍👧🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
👩🏻‍👩🏻‍👧🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👩🏼‍👧🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👩🏽‍👧🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👩🏾‍👧🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👧🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
👩🏿‍👩🏿‍👧🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
👨🏾‍👩🏾‍👧🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁤󠁫󠀸󠀱󠁿 Flag for Northern Denmark (DK-81)
👩🏻‍👩🏻‍👧🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
👩🏼‍👩🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👩🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👩🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone
👩🏻‍👩🏻‍👶🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
👩🏼‍👩🏼‍👶🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏽‍👩🏽‍👶🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
👩🏾‍👩🏾‍👶🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👶🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
👩🏻‍👩🏻‍👶🏻‍👧🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
👩🏽‍👩🏽‍👶🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👩🏾‍👩🏾‍👶🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩🏿‍👩🏿‍👶🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
👩🏻‍👩🏻‍👶🏻‍👶🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
👩🏼‍👩🏼‍👶🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏽‍👩🏽‍👶🏽‍👶🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👩🏿‍👶🏿‍👧🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
👩🏿‍👩🏿‍👶🏿‍👶🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁩󠁤󠁭󠁬󠁿 Flag for Maluku Islands (ID-ML)
👩🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁵󠁳󠁫󠁹󠁿 Flag for Kentucky (US-KY)
👩🏾‍👩🏾‍👶🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁤󠁫󠀸󠀳󠁿 Flag for Southern Denmark (DK-83)
🏴󠁭󠁫󠀸󠀵󠁿 Flag for Skopje (MK-85)
🏴󠁣󠁭󠁥󠁮󠁿 Flag for Far North (CM-EN)
👨🏿‍👨🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁣󠁮󠀱󠀵󠁿 Flag for Inner Mongolia (CN-15)
👨🏼‍❤️‍💋‍👩 Kiss - Man: Medium-Light Skin Tone, Woman
🏴󠁰󠁴󠀰󠀲󠁿 Flag for Beja (PT-02)
🏴󠁴󠁶󠁦󠁵󠁮󠁿 Flag for Funafuti (TV-FUN)
🏴󠁤󠁥󠁢󠁹󠁿 Flag for Bavaria (DE-BY)
🏴󠁴󠁪󠁧󠁢󠁿 Flag for Gorno-Badakhshan (TJ-GB)
🏴󠁩󠁴󠀳󠀲󠁿 Flag for Trentino-South Tyrol (IT-32)
🏴󠁳󠁯󠁢󠁮󠁿 Flag for Banaadir (SO-BN)
🏴󠁩󠁴󠀸󠀸󠁿 Flag for Sardinia (IT-88)
🏴󠁰󠁧󠁥󠁢󠁲󠁿 Flag for East New Britain (PG-EBR)
🏴󠁳󠁩󠀱󠀰󠀰󠁿 Flag for Radenci (SI-100)
🏴󠁵󠁳󠁴󠁮󠁿 Flag for Tennessee (US-TN)
👩🏿‍👧🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁤󠁥󠁢󠁷󠁿 Flag for Baden-Württemberg (DE-BW)
🏴󠁴󠁧󠁭󠁿 Flag for Maritime (TG-M)
🏴󠁫󠁥󠀳󠀱󠁿 Flag for Nakuru (KE-31)
🏴󠁶󠁥󠁧󠁿 Flag for Carabobo (VE-G)
‍ Zero Width Joiner
🏴󠁮󠁧󠁢󠁯󠁿 Flag for Borno (NG-BO)
🏴󠁭󠁹󠀱󠀴󠁿 Flag for Kuala Lumpur (MY-14)
🏴󠁭󠁤󠁳󠁮󠁿 Flag for Transnistria (MD-SN)
🏴󠁩󠁲󠀰󠀷󠁿 Flag for Tehran (IR-07)
👩🏽‍👧🏽‍👶🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁲󠁵󠁤󠁡󠁿 Flag for Dagestan (RU-DA)
🏴󠁣󠁺󠀴󠀲󠁿 Flag for Ústecký kraj (CZ-42)
🏴󠁯󠁭󠁷󠁵󠁿 Flag for Al Wusta (OM-WU)
🏴󠁰󠁥󠁡󠁹󠁡󠁿 Flag for Ayacucho (PE-AYA)
🏴󠁭󠁸󠁤󠁵󠁲󠁿 Flag for Durango (MX-DUR)
🏴󠁭󠁴󠀲󠀹󠁿 Flag for Mdina (MT-29)
🏴󠁡󠁧󠀰󠀸󠁿 Flag for Saint Philip (AG-08)
🏴󠁵󠁡󠀳󠀰󠁿 Flag for Kiev (UA-30)
🏴󠁦󠁲󠁡󠁲󠁡󠁿 Flag for Auvergne-Rhône-Alpes (FR-ARA)
🏴󠁬󠁫󠀵󠁿 Flag for Eastern (LK-5)
🏴󠁮󠁧󠁯󠁧󠁿 Flag for Ogun (NG-OG)
👨🏼‍👨🏼‍👧🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁬󠁹󠁪󠁩󠁿 Flag for Jafara (LY-JI)
🏴󠁧󠁴󠁳󠁲󠁿 Flag for Santa Rosa (GT-SR)
👩🏾‍👩🏾‍👧🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁢󠁲󠁭󠁳󠁿 Flag for Mato Grosso do Sul (BR-MS)
🏴󠁳󠁥󠁭󠁿 Flag for Skåne (SE-M)
🏴󠁳󠁩󠀱󠀵󠀱󠁿 Flag for Braslovče (SI-151)
🏴󠁣󠁮󠀱󠀳󠁿 Flag for Hebei (CN-13)
🏴󠁩󠁲󠀳󠀲󠁿 Flag for Alborz (IR-32)
🏴󠁳󠁶󠁳󠁶󠁿 Flag for San Vicente (SV-SV)
🏴󠁷󠁳󠁦󠁡󠁿 Flag for Fa’asaleleaga (WS-FA)
🏴󠁮󠁬󠁳󠁸󠁿 Flag for Sint Maarten (NL-SX)
👩🏿‍👩🏿‍👧🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
👨🏼‍👨🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁭󠁴󠀴󠀸󠁿 Flag for St. Julian’s (MT-48)
🏴󠁧󠁲󠁪󠁿 Flag for Peloponnese (GR-J)
🏴󠁮󠁧󠁡󠁤󠁿 Flag for Adamawa (NG-AD)
🏴󠁣󠁡󠁮󠁬󠁿 Flag for Newfoundland and Labrador (CA-NL)
👩🏻‍👩🏻‍👧🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁬󠁶󠀰󠀱󠀰󠁿 Flag for Auce (LV-010)
🏴󠁰󠁨󠀱󠀵󠁿 Flag for Cordillera Administrative (PH-15)
🏴󠁳󠁴󠁳󠁿 Flag for São Tomé (ST-S)
👨🏿‍👩🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁪󠁰󠀱󠀸󠁿 Flag for Fukui (JP-18)
🏴󠁭󠁡󠀱󠀳󠁿 Flag for Souss-Massa-Drâa (MA-13)
🏴󠁧󠁥󠁫󠁡󠁿 Flag for Kakheti (GE-KA)
🏴󠁦󠁲󠁴󠁦󠁿 Flag for French Southern Territories (FR-TF)
🏴󠁫󠁲󠀴󠀹󠁿 Flag for Jeju (KR-49)
🏴󠁬󠁶󠀰󠀳󠀷󠁿 Flag for Inčukalns (LV-037)
🏴󠁭󠁸󠁲󠁯󠁯󠁿 Flag for Quintana Roo (MX-ROO)
👨🏾‍👨🏾‍👦🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏻‍👶🏻‍👶🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁨󠁵󠁧󠁳󠁿 Flag for Győr-Moson-Sopron (HU-GS)
👩🏿‍👩🏿‍👧🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone
👩🏻‍👩🏻‍👦🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
👩‍❤️‍👨🏽 Couple With Heart - Woman, Man: Medium Skin Tone
👩🏼‍👩🏼‍👧🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏽‍👨🏽‍👦🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁣󠁡󠁡󠁢󠁿 Flag for Alberta (CA-AB)
👨‍👶‍👶 Family: Man, Baby, Baby
🏴󠁬󠁶󠀰󠀹󠀰󠁿 Flag for Sēja (LV-090)
🏴󠁵󠁳󠁭󠁰󠁿 Flag for Northern Mariana Islands (US-MP)
🏴󠁣󠁤󠁢󠁵󠁿 Flag for Bas-Uélé (CD-BU)
👩🏻‍❤️‍💋‍👩 Kiss - Woman: Light Skin Tone, Woman
🏴󠁨󠁴󠁮󠁥󠁿 Flag for Nord-Est (HT-NE)
🏴󠁥󠁣󠁴󠁿 Flag for Tungurahua (EC-T)
👨🏻‍👨🏻‍👶🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
🏴󠁣󠁡󠁳󠁫󠁿 Flag for Saskatchewan (CA-SK)
🏴󠁢󠁯󠁴󠁿 Flag for Tarija (BO-T)
🏴󠁵󠁹󠁲󠁶󠁿 Flag for Rivera (UY-RV)
🏴󠁭󠁶󠁵󠁳󠁿 Flag for Upper South Province (MV-US)
🏴󠁢󠁩󠁣󠁩󠁿 Flag for Cibitoke (BI-CI)
🏴󠁧󠁥󠁡󠁪󠁿 Flag for Adjara (GE-AJ)
🏴󠁡󠁤󠀰󠀲󠁿 Flag for Canillo (AD-02)
🏴󠁢󠁲󠁳󠁰󠁿 Flag for São Paulo (BR-SP)
🏴󠁡󠁤󠀰󠀳󠁿 Flag for Encamp (AD-03)
🦛 Hippopotamus
🦢 Swan
🏴󠁧󠁡󠀱󠁿 Flag for Estuaire (GA-1)
🥰 Smiling Face With Smiling Eyes And Three Hearts
🏴󠁡󠁦󠁢󠁡󠁭󠁿 Flag for Bamyan (AF-BAM)
* Asterisk
🏴󠁡󠁤󠀰󠀴󠁿 Flag for La Massana (AD-04)
🦰 Emoji Component Red Hair
🧨 Firecracker
🦳 Emoji Component White Hair
🏴󠁬󠁶󠀰󠀱󠀲󠁿 Flag for Babīte (LV-012)
🏴󠁭󠁶󠁮󠁣󠁿 Flag for North Central Province (MV-NC)
🏴󠁳󠁯󠁢󠁹󠁿 Flag for Bay, Somalia (SO-BY)
🏴󠁣󠁺󠀳󠀱󠁿 Flag for Jihočeský kraj (CZ-31)
# Number Sign
󠁺 Tag Latin Small Letter Z
🏴󠁢󠁲󠁰󠁡󠁿 Flag for Pará (BR-PA)
🥵 Overheated Face
🏴󠁧󠁡󠀴󠁿 Flag for Ngounié (GA-4)
🏴󠁭󠁥󠀰󠀳󠁿 Flag for Berane (ME-03)
🦡 Badger
🏴󠁭󠁭󠀱󠀷󠁿 Flag for Shan (MM-17)
1 Digit One
👨🏿‍❤️‍💋‍👨🏽 Kiss - Man: Dark Skin Tone, Man: Medium Skin Tone
🏴󠁰󠁴󠀳󠀰󠁿 Flag for Madeira (PT-30)
🏴󠁤󠁯󠀳󠀷󠁿 Flag for El Valle (DO-37)
󠀩 Tag Right Parenthesis
🏴󠁫󠁥󠀰󠀱󠁿 Flag for Baringo (KE-01)
🏴󠁹󠁥󠁳󠁡󠁿 Flag for Amanat Al Asimah (YE-SA)
👨🏼‍👨🏼‍👶🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁭󠁴󠀲󠀰󠁿 Flag for Senglea (MT-20)
󠀲 Tag Digit Two
🏴󠁣󠁦󠁨󠁭󠁿 Flag for Haut-Mbomou (CF-HM)
🕴️‍♀️ Woman in Business Suit Levitating
6 Digit Six
🏴󠁥󠁣󠁸󠁿 Flag for Cotopaxi (EC-X)
🥶 Freezing Face
🏴󠁭󠁫󠀷󠀵󠁿 Flag for Tearce (MK-75)
󠀳 Tag Digit Three
🏴󠁡󠁺󠁡󠁢󠁳󠁿 Flag for Absheron (AZ-ABS)
🏴󠁳󠁮󠁤󠁫󠁿 Flag for Dakar (SN-DK)
👨‍❤️‍💋‍👨🏽 Kiss - Man, Man: Medium Skin Tone
🏴󠁬󠁡󠁳󠁶󠁿 Flag for Savannakhet (LA-SV)
🏴󠁭󠁬󠀱󠁿 Flag for Kayes (ML-1)
🏴󠁩󠁱󠁢󠁢󠁿 Flag for Babylon (IQ-BB)
8 Digit Eight
🏴󠁡󠁥󠁡󠁪󠁿 Flag for Ajman (AE-AJ)
🏴󠁤󠁥󠁢󠁥󠁿 Flag for Berlin (DE-BE)
👨🏻‍❤️‍💋‍👩 Kiss - Man: Light Skin Tone, Woman
🏴󠁣󠁮󠀶󠀴󠁿 Flag for Ningxia (CN-64)
󠁻 Tag Left Curly Bracket
🏴󠁡󠁤󠀰󠀸󠁿 Flag for Escaldes-Engordany (AD-08)
🏴󠁥󠁣󠁦󠁿 Flag for Cañar (EC-F)
🥴 Face With Uneven Eyes And Wavy Mouth
🏴󠁲󠁵󠁣󠁥󠁿 Flag for Chechen (RU-CE)
🏴󠁮󠁺󠁮󠁳󠁮󠁿 Flag for Nelson (NZ-NSN)
🥺 Face With Pleading Eyes
🏴󠁨󠁲󠀱󠀰󠁿 Flag for Virovitica-Podravina (HR-10)
👩🏿‍❤️‍👩🏿 Couple With Heart - Woman: Dark Skin Tone, Woman: Dark Skin Tone
󠀷 Tag Digit Seven
7 Digit Seven
🏴󠁡󠁥󠁦󠁵󠁿 Flag for Fujairah (AE-FU)
👨🏼‍👦🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
󠀱 Tag Digit One
🦲 Emoji Component Bald
🏴󠁭󠁨󠁴󠁿 Flag for Ratak Chain (MH-T)
4 Digit Four
󠀸 Tag Digit Eight
👨🏽‍👩🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁬󠁴󠀵󠀷󠁿 Flag for Vilniaus Municipality (LT-57)
🏴󠁩󠁳󠀴󠁿 Flag for Westfjords (IS-4)
🏴󠁡󠁦󠁢󠁡󠁬󠁿 Flag for Balkh (AF-BAL)
󠀴 Tag Digit Four
👨‍👶‍👦 Family: Man, Baby, Boy
🏴󠁰󠁧󠁷󠁨󠁭󠁿 Flag for Western Highlands (PG-WHM)
👩‍👶‍👧 Family: Woman, Baby, Girl
󠁩 Tag Latin Small Letter I
🏴󠁴󠁷󠁨󠁳󠁱󠁿 Flag for Hsinchu County (TW-HSQ)
🦸 Superhero
🏴󠁡󠁥󠁳󠁨󠁿 Flag for Sharjah (AE-SH)
🏴󠁤󠁺󠀱󠀹󠁿 Flag for Sétif (DZ-19)
🏴󠁭󠁹󠀰󠀷󠁿 Flag for Penang (MY-07)
🏴󠁣󠁮󠀶󠀱󠁿 Flag for Shaanxi (CN-61)
🏴󠁳󠁬󠁥󠁿 Flag for Eastern (SL-E)
🏴󠁰󠁴󠀲󠀰󠁿 Flag for Azores (PT-20)
🏴󠁡󠁦󠁢󠁧󠁬󠁿 Flag for Baghlan (AF-BGL)
🏴󠁩󠁮󠁭󠁮󠁿 Flag for Manipur (IN-MN)
🏴󠁭󠁹󠀱󠀲󠁿 Flag for Sabah (MY-12)
👩‍👧‍👶 Family: Woman, Girl, Baby
🏴󠁰󠁷󠀲󠀲󠀸󠁿 Flag for Ngiwal (PW-228)
🏴󠁡󠁤󠀰󠀵󠁿 Flag for Ordino (AD-05)
🦹 Supervillain
🏴󠁫󠁥󠀱󠀸󠁿 Flag for Kitui (KE-18)
🏴󠁥󠁳󠁡󠁳󠁿 Flag for Asturias (ES-AS)
🏴󠁳󠁥󠁸󠁿 Flag for Gävleborg (SE-X)
👩🏻‍❤️‍👩🏼 Couple With Heart - Woman: Light Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁡󠁦󠁢󠁤󠁳󠁿 Flag for Badakhshan (AF-BDS)
🏴󠁣󠁡󠁮󠁴󠁿 Flag for Northwest Territories (CA-NT)
󠁦 Tag Latin Small Letter F
🏴󠁩󠁲󠀱󠀴󠁿 Flag for Fars (IR-14)
󠁱 Tag Latin Small Letter Q
👨🏽‍👨🏽‍👶🏽‍👦🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🦠 Microbe
󠁳 Tag Latin Small Letter S
🏴󠁮󠁺󠁷󠁧󠁮󠁿 Flag for Wellington (NZ-WGN)
🧧 Red Gift Envelope
󠁴 Tag Latin Small Letter T
👨🏽‍❤️‍💋‍👨🏿 Kiss - Man: Medium Skin Tone, Man: Dark Skin Tone
👨🏻‍👩🏻‍👦🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
👩‍👶‍👶 Family: Woman, Baby, Baby
👨🏻‍❤️‍💋‍👨🏾 Kiss - Man: Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁡󠁦󠁦󠁲󠁡󠁿 Flag for Farah (AF-FRA)
🏴󠁭󠁫󠀶󠀴󠁿 Flag for Radoviš (MK-64)
🏴󠁡󠁦󠁤󠁡󠁹󠁿 Flag for Daykundi (AF-DAY)
🏴󠁣󠁨󠁴󠁧󠁿 Flag for Thurgau (CH-TG)
󠁿 Cancel Tag
🏴󠁡󠁴󠀹󠁿 Flag for Vienna (AT-9)
🧬 DNA
🏴󠁤󠁯󠀴󠀰󠁿 Flag for Ozama (DO-40)
🏴󠁧󠁴󠁧󠁵󠁿 Flag for Guatemala (GT-GU)
🧫 Petri Dish
󠁵 Tag Latin Small Letter U
🧂 Salt Shaker
🏴󠁢󠁳󠁢󠁹󠁿 Flag for Berry Islands (BS-BY)
󠁷 Tag Latin Small Letter W
🏴󠁩󠁱󠁫󠁩󠁿 Flag for Kirkuk (IQ-KI)
🏴󠁡󠁦󠁧󠁨󠁡󠁿 Flag for Ghazni (AF-GHA)
🏴󠁢󠁷󠁧󠁡󠁿 Flag for Gaborone (BW-GA)
󠀵 Tag Digit Five
🏴󠁡󠁦󠁧󠁨󠁯󠁿 Flag for Ghōr (AF-GHO)
󠁹 Tag Latin Small Letter Y
👩🏽‍❤️‍👩🏿 Couple With Heart - Woman: Medium Skin Tone, Woman: Dark Skin Tone
👨🏼‍👩🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁣󠁯󠁡󠁭󠁡󠁿 Flag for Amazonas (CO-AMA)
👩‍❤️‍💋‍👩🏽 Kiss - Woman, Woman: Medium Skin Tone
󠁮 Tag Latin Small Letter N
🏴󠁣󠁨󠁪󠁵󠁿 Flag for Jura (CH-JU)
🏴󠁡󠁴󠀱󠁿 Flag for Burgenland (AT-1)
🏴󠁳󠁳󠁬󠁫󠁿 Flag for Lakes (SS-LK)
󠀰 Tag Digit Zero
🏴󠁭󠁬󠀸󠁿 Flag for Kidal (ML-8)
🏴󠁡󠁦󠁪󠁯󠁷󠁿 Flag for Jowzjan (AF-JOW)
🏴󠁡󠁦󠁨󠁥󠁲󠁿 Flag for Herat (AF-HER)
🏴󠁡󠁦󠁨󠁥󠁬󠁿 Flag for Helmand (AF-HEL)
󠁥 Tag Latin Small Letter E
🏴󠁡󠁦󠁫󠁡󠁢󠁿 Flag for Kabul (AF-KAB)
🧕‍♀️ Woman With Headscarf
🏴󠁧󠁤󠀰󠀵󠁿 Flag for Saint Mark (GD-05)
👩🏽‍❤️‍💋‍👨🏽 Kiss - Woman: Medium Skin Tone, Man: Medium Skin Tone
3 Digit Three
󠁲 Tag Latin Small Letter R
🧕‍♂️ Man With Headscarf
🧮 Abacus
🏴󠁴󠁬󠁬󠁡󠁿 Flag for Lautém (TL-LA)
👩🏿‍👩🏿‍👦🏿 Family - Woman: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁵󠁳󠁡󠁫󠁿 Flag for Alaska (US-AK)
👨‍❤️‍💋‍👨🏿 Kiss - Man, Man: Dark Skin Tone
🏴󠁣󠁮󠀱󠀱󠁿 Flag for Beijing (CN-11)
🏴󠁡󠁦󠁫󠁡󠁰󠁿 Flag for Kapisa (AF-KAP)
󠁭 Tag Latin Small Letter M
󠁤 Tag Latin Small Letter D
🏴󠁡󠁦󠁫󠁡󠁮󠁿 Flag for Kandahar (AF-KAN)
󠁧 Tag Latin Small Letter G
🧕🏻‍♂️ Man With Headscarf: Light Skin Tone
🧯 Fire Extinguisher
🏴󠁭󠁣󠁳󠁲󠁿 Flag for Saint Roman (MC-SR)
🧿 Nazar Amulet
󠁶 Tag Latin Small Letter V
🏴󠁥󠁥󠀳󠀹󠁿 Flag for Hiiu (EE-39)
🏴󠁡󠁦󠁫󠁤󠁺󠁿 Flag for Kunduz (AF-KDZ)
🏴󠁪󠁰󠀱󠀳󠁿 Flag for Tokyo (JP-13)
🏴󠁵󠁳󠁳󠁤󠁿 Flag for South Dakota (US-SD)
👩🏾‍👨🏾‍👦🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🥽 Goggles
🏴󠁡󠁦󠁢󠁤󠁧󠁿 Flag for Badghis (AF-BDG)
 Shibuya
👨‍👨‍👶‍👶 Family: Man, Man, Baby, Baby
👩‍👨‍👦‍👦 Family: Woman, Man, Boy, Boy
🏴󠁩󠁳󠀸󠁿 Flag for Southern (IS-8)
🏴󠁡󠁦󠁫󠁮󠁲󠁿 Flag for Kunar (AF-KNR)
🏴󠁡󠁦󠁬󠁡󠁧󠁿 Flag for Laghman (AF-LAG)
🏴󠁭󠁸󠁮󠁡󠁹󠁿 Flag for Nayarit (MX-NAY)
󠀦 Tag Ampersand
󠀹 Tag Digit Nine
🏴󠁡󠁦󠁦󠁹󠁢󠁿 Flag for Faryab (AF-FYB)
🏴󠁡󠁦󠁮󠁡󠁮󠁿 Flag for Nangarhar (AF-NAN)
🏴󠁡󠁦󠁬󠁯󠁧󠁿 Flag for Logar (AF-LOG)
🧕🏽‍♂️ Man With Headscarf: Medium Skin Tone
🏴󠁢󠁲󠁰󠁥󠁿 Flag for Pernambuco (BR-PE)
󠁍 Tag Latin Capital Letter M
🏴󠁰󠁧󠁷󠁢󠁫󠁿 Flag for West New Britain (PG-WBK)
👩🏽‍❤️‍💋‍👩🏾 Kiss - Woman: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁩󠁴󠀷󠀲󠁿 Flag for Campania (IT-72)
5 Digit Five
󠁰 Tag Latin Small Letter P
🏴󠁡󠁦󠁮󠁵󠁲󠁿 Flag for Nuristan (AF-NUR)
👨‍👨‍👧‍👶 Family: Man, Man, Girl, Baby
🏴󠁡󠁦󠁮󠁩󠁭󠁿 Flag for Nimruz (AF-NIM)
🏴󠁧󠁹󠁵󠁤󠁿 Flag for Upper Demerara-Berbice (GY-UD)
🧕🏾‍♂️ Man With Headscarf: Medium-Dark Skin Tone
👨‍👦‍👧 Family: Man, Boy, Girl
👨‍❤️‍💋‍👩 Kiss - Man, Woman
🏴󠁦󠁲󠁩󠁤󠁦󠁿 Flag for Île-de-France (FR-IDF)
🏴󠁡󠁦󠁰󠁡󠁲󠁿 Flag for Parwan (AF-PAR)
🏴󠁨󠁲󠀰󠀴󠁿 Flag for Karlovac (HR-04)
🏴󠁥󠁴󠁡󠁦󠁿 Flag for Afar (ET-AF)
🏴󠁡󠁦󠁫󠁨󠁯󠁿 Flag for Khost (AF-KHO)
󠁯 Tag Latin Small Letter O
󠁞 Tag Circumflex Accent
🧕🏿‍♂️ Man With Headscarf: Dark Skin Tone
🧕🏼‍♂️ Man With Headscarf: Medium-Light Skin Tone
🏴󠁫󠁩󠁰󠁿 Flag for Phoenix Islands (KI-P)
󠁊 Tag Latin Capital Letter J
🏴󠁣󠁨󠁴󠁩󠁿 Flag for Ticino (CH-TI)
🏴󠁡󠁦󠁰󠁫󠁡󠁿 Flag for Paktika (AF-PKA)
∞ Infinity
🏴󠁡󠁦󠁰󠁩󠁡󠁿 Flag for Paktia (AF-PIA)
󠁐 Tag Latin Capital Letter P
🏴󠁤󠁥󠁲󠁰󠁿 Flag for Rhineland-Palatinate (DE-RP)
🏴󠁡󠁦󠁰󠁡󠁮󠁿 Flag for Panjshir (AF-PAN)
🏴󠁳󠁩󠀱󠀹󠀲󠁿 Flag for Žirovnica (SI-192)
🏴󠁳󠁥󠁮󠁿 Flag for Halland (SE-N)
🏴󠁳󠁳󠁢󠁮󠁿 Flag for Northern Bahr el Ghazal (SS-BN)
👨🏾‍👨🏾‍👶🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👨🏿‍👨🏿‍👶🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁡󠁥󠁲󠁫󠁿 Flag for Ras al-Khaimah (AE-RK)
🏴󠁥󠁳󠁣󠁥󠁿 Flag for Ceuta (ES-CE)
👨🏽‍❤️‍💋‍👩 Kiss - Man: Medium Skin Tone, Woman
🏴󠁴󠁶󠁮󠁫󠁬󠁿 Flag for Nukulaelae (TV-NKL)
👩🏽‍❤️‍💋‍👩🏻 Kiss - Woman: Medium Skin Tone, Woman: Light Skin Tone
🏴󠁣󠁦󠁢󠁫󠁿 Flag for Basse-Kotto (CF-BK)
👨‍❤️‍👨🏻 Couple With Heart - Man, Man: Light Skin Tone
🦴 Bone
🏴󠁬󠁫󠀹󠁿 Flag for Sabaragamuwa (LK-9)
🏴󠁴󠁺󠀱󠀱󠁿 Flag for Zanzibar Central/South (TZ-11)
🏴󠁬󠁹󠁢󠁵󠁿 Flag for Butnan (LY-BU)
󠁪 Tag Latin Small Letter J
🏴󠁡󠁦󠁳󠁡󠁭󠁿 Flag for Samangan (AF-SAM)
👨🏻‍👨🏻‍👶🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
🏴󠁰󠁥󠁬󠁩󠁭󠁿 Flag for Lima Region (PE-LIM)
👨‍👶 Family: Man, Baby
🏴󠁡󠁥󠁤󠁵󠁿 Flag for Dubai (AE-DU)
🦵 Leg
👨🏾‍👩🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁡󠁥󠁡󠁺󠁿 Flag for Abu Dhabi (AE-AZ)
󠀡 Tag Exclamation Mark
🏴󠁪󠁰󠀴󠀷󠁿 Flag for Okinawa (JP-47)
🏴󠁡󠁦󠁳󠁡󠁲󠁿 Flag for Sar-e Pol (AF-SAR)
9 Digit Nine
👩🏼‍👩🏼‍👦🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🦶 Foot
🏴󠁡󠁦󠁵󠁲󠁵󠁿 Flag for Urozgan (AF-URU)
󠁬 Tag Latin Small Letter L
🏴󠁩󠁴󠀲󠀵󠁿 Flag for Lombardy (IT-25)
🏴󠁣󠁯󠁶󠁩󠁤󠁿 Flag for Vichada (CO-VID)
🏴󠁰󠁷󠀲󠀱󠀸󠁿 Flag for Ngarchelong (PW-218)
🏴󠁡󠁦󠁺󠁡󠁢󠁿 Flag for Zabul (AF-ZAB)
🦷 Tooth
🏴󠁡󠁧󠀰󠀴󠁿 Flag for Saint John (AG-04)
👩🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁤󠁭󠀰󠀶󠁿 Flag for Saint Joseph (DM-06)
🏴󠁡󠁧󠀰󠀳󠁿 Flag for Saint George (AG-03)
🏴󠁥󠁣󠁺󠁿 Flag for Zamora-Chinchipe (EC-Z)
🏴󠁧󠁲󠁫󠁿 Flag for North Aegean (GR-K)
🏴󠁡󠁧󠀰󠀵󠁿 Flag for Saint Mary (AG-05)
🏴󠁫󠁩󠁧󠁿 Flag for Gilbert Islands (KI-G)
🥾 Hiking Boot
🏴󠁡󠁧󠀰󠀶󠁿 Flag for Saint Paul (AG-06)
🏴󠁶󠁮󠀵󠀱󠁿 Flag for Trà Vinh (VN-51)
👩‍👩‍👶‍👧 Family: Woman, Woman, Baby, Girl
🏴󠁣󠁺󠀵󠀳󠁿 Flag for Pardubický kraj (CZ-53)
👩‍👨‍👶‍👧 Family: Woman, Man, Baby, Girl
🏴󠁮󠁩󠁭󠁳󠁿 Flag for Masaya (NI-MS)
🏴󠁫󠁲󠀴󠀸󠁿 Flag for South Gyeongsang (KR-48)
🏴󠁭󠁸󠁣󠁨󠁨󠁿 Flag for Chihuahua (MX-CHH)
👨🏼‍👨🏼‍👶🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁭󠁸󠁢󠁣󠁮󠁿 Flag for Baja California (MX-BCN)
👨🏽‍👨🏽‍👶🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
󠁣 Tag Latin Small Letter C
🏴󠁡󠁧󠀱󠀱󠁿 Flag for Redonda (AG-11)
🥼 Lab Coat
👨🏼‍👩🏼‍👧🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁡󠁬󠀰󠀱󠁿 Flag for Berat County (AL-01)
👩‍👩‍👶 Family: Woman, Woman, Baby
🏴󠁩󠁲󠀰󠀳󠁿 Flag for Ardabil (IR-03)
👩🏽‍❤️‍💋‍👩 Kiss - Woman: Medium Skin Tone, Woman
🏴󠁩󠁮󠁪󠁫󠁿 Flag for Jammu and Kashmir (IN-JK)
🏴󠁣󠁯󠁳󠁡󠁰󠁿 Flag for San Andrés & Providencia (CO-SAP)
🥿 Flat Shoe
👨🏾‍👨🏾‍👶🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🦘 Kangaroo
🏴󠁪󠁰󠀰󠀱󠁿 Flag for Hokkaidō (JP-01)
👨🏿‍👨🏿‍👦🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
󠁡 Tag Latin Small Letter a
🏴󠁰󠁡󠀱󠀰󠁿 Flag for West Panamá (PA-10)
🏴󠁡󠁬󠀰󠀳󠁿 Flag for Elbasan County (AL-03)
👩🏾‍👨🏾‍👶🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁮󠁧󠁣󠁲󠁿 Flag for Cross River (NG-CR)
👨🏼‍❤️‍💋‍👨 Kiss - Man: Medium-Light Skin Tone, Man
🏴󠁡󠁬󠀰󠀲󠁿 Flag for Durrës County (AL-02)
🏴󠁡󠁬󠀰󠀴󠁿 Flag for Fier County (AL-04)
🏴󠁡󠁬󠀰󠀶󠁿 Flag for Korçë County (AL-06)
🏴󠁡󠁬󠀰󠀷󠁿 Flag for Kukës County (AL-07)
🏴󠁭󠁴󠀶󠀵󠁿 Flag for Żebbuġ Gozo (MT-65)
👨🏿‍❤️‍💋‍👨 Kiss - Man: Dark Skin Tone, Man
🏴󠁧󠁹󠁵󠁴󠁿 Flag for Upper Takutu-Upper Essequibo (GY-UT)
󠁇 Tag Latin Capital Letter G
👨🏾‍👶🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
󠀶 Tag Digit Six
👨🏿‍👨🏿‍👶🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🦚 Peacock
🦙 Llama
󠁂 Tag Latin Capital Letter B
🏴󠁡󠁬󠀰󠀹󠁿 Flag for Dibër County (AL-09)
🏴󠁡󠁬󠀰󠀸󠁿 Flag for Lezhë County (AL-08)
👨🏼‍👨🏼‍👶🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩‍👨‍👶‍👶 Family: Woman, Man, Baby, Baby
🧪 Test Tube
🏴󠁡󠁬󠀱󠀱󠁿 Flag for Tirana County (AL-11)
🏴󠁡󠁬󠀱󠀰󠁿 Flag for Shkodër County (AL-10)
👩‍❤️‍💋‍👨🏽 Kiss - Woman, Man: Medium Skin Tone
👨🏽‍👨🏽‍👶🏽‍👶🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👨🏾‍👨🏾‍👶🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁢󠁲󠁢󠁡󠁿 Flag for Bahia (BR-BA)
🏴󠁤󠁥󠁳󠁮󠁿 Flag for Saxony (DE-SN)
🏴󠁡󠁬󠀱󠀲󠁿 Flag for Vlorë County (AL-12)
󠁢 Tag Latin Small Letter B
🏴󠁴󠁨󠀲󠀳󠁿 Flag for Trat (TH-23)
👩‍❤️‍💋‍👨🏿 Kiss - Woman, Man: Dark Skin Tone
👨🏿‍👨🏿‍👶🏿‍👶🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁡󠁧󠀱󠀰󠁿 Flag for Barbuda (AG-10)
🏴󠁡󠁭󠁧󠁲󠁿 Flag for Gegharkunik (AM-GR)
🏴󠁡󠁭󠁡󠁧󠁿 Flag for Aragatsotn (AM-AG)
👨🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁡󠁭󠁡󠁲󠁿 Flag for Ararat (AM-AR)
👩‍❤️‍👩🏽 Couple With Heart - Woman, Woman: Medium Skin Tone
🏴󠁡󠁭󠁥󠁲󠁿 Flag for Yerevan (AM-ER)
🏴󠁮󠁧󠁥󠁮󠁿 Flag for Enugu (NG-EN)
🏴󠁡󠁭󠁫󠁴󠁿 Flag for Kotayk (AM-KT)
🏴󠁤󠁺󠀲󠀱󠁿 Flag for Skikda (DZ-21)
🏴󠁡󠁭󠁳󠁨󠁿 Flag for Shirak (AM-SH)
🏴󠁣󠁧󠀱󠀶󠁿 Flag for Pointe-Noire (CG-16)
👩‍❤️‍💋‍👩🏿 Kiss - Woman, Woman: Dark Skin Tone
🏴󠁡󠁭󠁡󠁶󠁿 Flag for Armavir (AM-AV)
🏴󠁡󠁭󠁬󠁯󠁿 Flag for Lori (AM-LO)
🦝 Raccoon
🏴󠁦󠁲󠁣󠁯󠁲󠁿 Flag for Corse (FR-COR)
🏴󠁰󠁹󠀱󠀶󠁿 Flag for Alto Paraguay (PY-16)
👩‍❤️‍💋‍👩🏾 Kiss - Woman, Woman: Medium-Dark Skin Tone
🏴󠁡󠁤󠀰󠀷󠁿 Flag for Andorra la Vella (AD-07)
🏴󠁢󠁲󠁭󠁧󠁿 Flag for Minas Gerais (BR-MG)
👩‍❤️‍💋‍👩🏼 Kiss - Woman, Woman: Medium-Light Skin Tone
🏴󠁳󠁩󠀱󠀶󠀷󠁿 Flag for Lovrenc na Pohorju (SI-167)
🏴󠁭󠁸󠁡󠁧󠁵󠁿 Flag for Aguascalientes (MX-AGU)
🏴󠁭󠁸󠁪󠁡󠁬󠁿 Flag for Jalisco (MX-JAL)
🦞 Lobster
👨🏿‍❤️‍💋‍👩🏻 Kiss - Man: Dark Skin Tone, Woman: Light Skin Tone
🏴󠁬󠁴󠁰󠁮󠁿 Flag for Panevėžys County (LT-PN)
🏴󠁥󠁧󠁧󠁺󠁿 Flag for Giza (EG-GZ)
🏴󠁪󠁭󠀰󠀵󠁿 Flag for Saint Mary (JM-05)
👨‍❤️‍💋‍👩🏿 Kiss - Man, Woman: Dark Skin Tone
👨🏾‍👨🏾‍👦🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👩‍👨‍👶 Family: Woman, Man, Baby
🏴󠁡󠁭󠁶󠁤󠁿 Flag for Vayots Dzor (AM-VD)
👩🏻‍❤️‍💋‍👩🏻 Kiss - Woman: Light Skin Tone, Woman: Light Skin Tone
🦱 Emoji Component Curly Hair
🏴󠁵󠁳󠁫󠁳󠁿 Flag for Kansas (US-KS)
󠀥 Tag Percent Sign
🏴󠁣󠁯󠁭󠁥󠁴󠁿 Flag for Meta (CO-MET)
👨🏽‍❤️‍💋‍👨 Kiss - Man: Medium Skin Tone, Man
🏴󠁵󠁧󠁣󠁿 Flag for Central (UG-C)
👩🏼‍❤️‍💋‍👩🏻 Kiss - Woman: Medium-Light Skin Tone, Woman: Light Skin Tone
🏴󠁡󠁯󠁢󠁧󠁯󠁿 Flag for Bengo (AO-BGO)
🏴󠁮󠁬󠁢󠁱󠀲󠁿 Flag for Saba (NL-BQ2)
🏴󠁲󠁵󠁡󠁬󠁴󠁿 Flag for Altai Krai (RU-ALT)
👨🏽‍👨🏽‍👧🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
👩🏽‍❤️‍💋‍👩🏼 Kiss - Woman: Medium Skin Tone, Woman: Medium-Light Skin Tone
󠁙 Tag Latin Capital Letter Y
👨🏽‍👩🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone
🦜 Parrot
🏴󠁡󠁯󠁢󠁧󠁵󠁿 Flag for Benguela (AO-BGU)
🏴󠁰󠁥󠁭󠁤󠁤󠁿 Flag for Madre de Dios (PE-MDD)
🏴󠁡󠁤󠀰󠀶󠁿 Flag for Sant Julià de Lòria (AD-06)
🏴󠁤󠁥󠁨󠁢󠁿 Flag for Bremen (DE-HB)
🏴󠁪󠁭󠀰󠀴󠁿 Flag for Portland (JM-04)
🏴󠁣󠁯󠁳󠁵󠁣󠁿 Flag for Sucre (CO-SUC)
🏴󠁡󠁯󠁢󠁩󠁥󠁿 Flag for Bié (AO-BIE)
🦟 Mosquito
🏴󠁣󠁨󠁶󠁤󠁿 Flag for Vaud (CH-VD)
🥬 Leafy Green
🏴󠁩󠁴󠀲󠀳󠁿 Flag for Aosta Valley (IT-23)
🏴󠁡󠁯󠁣󠁡󠁢󠁿 Flag for Cabinda (AO-CAB)
🏴󠁡󠁯󠁨󠁵󠁩󠁿 Flag for Huíla (AO-HUI)
👨🏼‍❤️‍👩🏾 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁡󠁯󠁣󠁵󠁳󠁿 Flag for Cuanza Sul (AO-CUS)
👨‍❤️‍💋‍👩🏽 Kiss - Man, Woman: Medium Skin Tone
🏴󠁵󠁳󠁶󠁴󠁿 Flag for Vermont (US-VT)
👩‍👩‍👦‍👶 Family: Woman, Woman, Boy, Baby
👩‍👶 Family: Woman, Baby
🏴󠁡󠁯󠁨󠁵󠁡󠁿 Flag for Huambo (AO-HUA)
👨‍❤️‍💋‍👨🏾 Kiss - Man, Man: Medium-Dark Skin Tone
🏴󠁣󠁹󠀰󠀶󠁿 Flag for Kyrenia (CY-06)
👩🏼‍❤️‍💋‍👨🏻 Kiss - Woman: Medium-Light Skin Tone, Man: Light Skin Tone
🥯 Bagel
🏴󠁡󠁯󠁬󠁳󠁵󠁿 Flag for Lunda Sul (AO-LSU)
🏴󠁡󠁥󠁵󠁱󠁿 Flag for Umm al-Quwain (AE-UQ)
👩🏽‍❤️‍👨🏿 Couple With Heart - Woman: Medium Skin Tone, Man: Dark Skin Tone
🏴󠁬󠁲󠁣󠁭󠁿 Flag for Grand Cape Mount (LR-CM)
🏴󠁡󠁯󠁬󠁮󠁯󠁿 Flag for Lunda Norte (AO-LNO)
👩🏼‍❤️‍💋‍👩 Kiss - Woman: Medium-Light Skin Tone, Woman
󠁽 Tag Right Curly Bracket
🏴󠁡󠁯󠁣󠁮󠁯󠁿 Flag for Cuanza Norte (AO-CNO)
🏴󠁲󠁵󠁡󠁲󠁫󠁿 Flag for Arkhangelsk (RU-ARK)
🏴󠁮󠁧󠁮󠁩󠁿 Flag for Niger (NG-NI)
👩🏼‍👩🏼‍👦🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁡󠁯󠁭󠁡󠁬󠁿 Flag for Malanje (AO-MAL)
🏴󠁲󠁯󠁣󠁬󠁿 Flag for Călărași (RO-CL)
🏴󠁡󠁯󠁭󠁯󠁸󠁿 Flag for Moxico (AO-MOX)
󠁓 Tag Latin Capital Letter S
󠁑 Tag Latin Capital Letter Q
󠁟 Tag Low Line
🏴󠁣󠁮󠀷󠀱󠁿 Flag for Taiwan (CN-71)
🥍 Lacrosse Stick And Ball
🏴󠁡󠁯󠁮󠁡󠁭󠁿 Flag for Namibe (AO-NAM)
🏴󠁧󠁤󠀰󠀳󠁿 Flag for Saint George (GD-03)
🏴󠁡󠁲󠁢󠁿 Flag for Buenos Aires Province (AR-B)
🥮 Moon Cake
👨🏾‍👩🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🥎 Softball
🏴󠁡󠁲󠁡󠁿 Flag for Salta (AR-A)
🕴🏼‍♀️ Woman in Business Suit Levitating: Medium-Light Skin Tone
󠁫 Tag Latin Small Letter K
🏴󠁣󠁤󠁬󠁵󠁿 Flag for Lualaba (CD-LU)
🏴󠁦󠁩󠀱󠀰󠁿 Flag for Lapland (FI-10)
🛹 Skateboard
👨🏿‍👩🏿‍👦🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁫󠁺󠁺󠁡󠁰󠁿 Flag for West Kazakhstan (KZ-ZAP)
🏴󠁡󠁯󠁺󠁡󠁩󠁿 Flag for Zaire (AO-ZAI)
0 Digit Zero
🏴󠁴󠁲󠀰󠀳󠁿 Flag for Afyonkarahisar (TR-03)
🏴󠁡󠁯󠁣󠁣󠁵󠁿 Flag for Cuando Cubango (AO-CCU)
🏴󠁶󠁮󠀲󠀵󠁿 Flag for Quảng Trị (VN-25)
🕴🏿‍♀️ Woman in Business Suit Levitating: Dark Skin Tone
🏴󠁵󠁡󠀱󠀸󠁿 Flag for Zhytomyrshchyna (UA-18)
🏴󠁡󠁯󠁵󠁩󠁧󠁿 Flag for Uíge (AO-UIG)
🏴󠁡󠁲󠁤󠁿 Flag for San Luis (AR-D)
🏴󠁮󠁧󠁲󠁩󠁿 Flag for Rivers (NG-RI)
👨🏾‍❤️‍💋‍👨🏽 Kiss - Man: Medium-Dark Skin Tone, Man: Medium Skin Tone
🥏 Flying Disc
🏴󠁣󠁯󠁣󠁥󠁳󠁿 Flag for Cesar (CO-CES)
🏴󠁡󠁲󠁥󠁿 Flag for Entre Ríos (AR-E)
👨🏿‍❤️‍💋‍👩 Kiss - Man: Dark Skin Tone, Woman
󠁼 Tag Vertical Line
🏴󠁫󠁺󠁶󠁯󠁳󠁿 Flag for East Kazakhstan (KZ-VOS)
🏴󠁡󠁭󠁳󠁵󠁿 Flag for Syunik (AM-SU)
🏴󠁡󠁲󠁦󠁿 Flag for La Rioja (AR-F)
󠁃 Tag Latin Capital Letter C
👨🏽‍👩🏽‍👦🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁡󠁲󠁪󠁿 Flag for San Juan (AR-J)
🏴󠁡󠁲󠁬󠁿 Flag for La Pampa (AR-L)
🏴󠁣󠁡󠁮󠁵󠁿 Flag for Nunavut (CA-NU)
🏴󠁡󠁯󠁬󠁵󠁡󠁿 Flag for Luanda (AO-LUA)
👩🏼‍❤️‍💋‍👩🏽 Kiss - Woman: Medium-Light Skin Tone, Woman: Medium Skin Tone
🏴󠁡󠁲󠁫󠁿 Flag for Catamarca (AR-K)
🧩 Jigsaw Puzzle Piece
🏴󠁡󠁲󠁰󠁿 Flag for Formosa (AR-P)
🏴󠁳󠁹󠁤󠁹󠁿 Flag for Deir ez-Zor (SY-DY)
🧱 Bricks
🏴󠁡󠁲󠁲󠁿 Flag for Río Negro (AR-R)
🏴󠁡󠁲󠁨󠁿 Flag for Chaco (AR-H)
🏴󠁡󠁲󠁮󠁿 Flag for Misiones (AR-N)
🏴󠁡󠁲󠁱󠁿 Flag for Neuquén (AR-Q)
🏴󠁳󠁣󠀰󠀵󠁿 Flag for Anse Royale (SC-05)
🧲 Magnet
🏴󠁡󠁲󠁳󠁿 Flag for Santa Fe (AR-S)
🏴󠁡󠁲󠁴󠁿 Flag for Tucumán (AR-T)
󠁅 Tag Latin Capital Letter E
🏴󠁡󠁲󠁭󠁿 Flag for Mendoza (AR-M)
🏴󠁡󠁲󠁺󠁿 Flag for Santa Cruz (AR-Z)
🏴󠁤󠁯󠀳󠀵󠁿 Flag for Cibao Norte (DO-35)
🏴󠁡󠁲󠁶󠁿 Flag for Tierra del Fuego (AR-V)
🏴󠁡󠁲󠁵󠁿 Flag for Chubut (AR-U)
🏴󠁡󠁲󠁹󠁿 Flag for Jujuy (AR-Y)
🏴󠁡󠁲󠁸󠁿 Flag for Córdoba (AR-X)
🏴󠁡󠁲󠁷󠁿 Flag for Corrientes (AR-W)
🏴󠁡󠁲󠁧󠁿 Flag for Santiago del Estero (AR-G)
👩🏿‍👧🏿‍👧🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁣󠁡󠁢󠁣󠁿 Flag for British Columbia (CA-BC)
👨🏼‍👦🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁴󠀲󠁿 Flag for Carinthia (AT-2)
🏴󠁣󠁨󠁢󠁬󠁿 Flag for Basel-Landschaft (CH-BL)
🧳 Luggage
👩‍👶‍👦 Family: Woman, Baby, Boy
🏴󠁡󠁴󠀳󠁿 Flag for Lower Austria (AT-3)
🧵 Spool Of Thread
🏴󠁭󠁲󠀱󠀳󠁿 Flag for Nouakchott Ouest (MR-13)
󠀠 Tag Space
👨‍👨‍👦‍👧 Family: Man, Man, Boy, Girl
🏴󠁰󠁴󠀱󠀸󠁿 Flag for Viseu (PT-18)
🏴󠁣󠁦󠁭󠁢󠁿 Flag for Mbomou (CF-MB)
🧶 Ball Of Yarn
🏴󠁰󠁨󠀰󠀱󠁿 Flag for Ilocos (PH-01)
👨🏿‍❤️‍👨🏿 Couple With Heart - Man: Dark Skin Tone, Man: Dark Skin Tone
🏴󠁡󠁴󠀷󠁿 Flag for Tyrol (AT-7)
👨🏿‍👩🏿‍👦🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁣󠁮󠀵󠀲󠁿 Flag for Guizhou (CN-52)
🏴󠁬󠁡󠁸󠁳󠁿 Flag for Xaisomboun (LA-XS)
👨🏼‍👨🏼‍👦🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁡󠁴󠀶󠁿 Flag for Styria (AT-6)
🧷 Safety Pin
🏴󠁡󠁴󠀸󠁿 Flag for Vorarlberg (AT-8)
🏴󠁡󠁴󠀵󠁿 Flag for Salzburg (AT-5)
👩‍👦‍👶 Family: Woman, Boy, Baby
👩‍👨‍👧‍👦 Family: Woman, Man, Girl, Boy
👩‍👨‍👧‍👶 Family: Woman, Man, Girl, Baby
🏴󠁥󠁣󠁭󠁿 Flag for Manabí (EC-M)
🧸 Teddy Bear
🧹 Broom
👩‍👩‍👶‍👶 Family: Woman, Woman, Baby, Baby
👩‍👨‍👧 Family: Woman, Man, Girl
🏴󠁡󠁵󠁱󠁬󠁤󠁿 Flag for Queensland (AU-QLD)
🏴󠁩󠁴󠀳󠀴󠁿 Flag for Veneto (IT-34)
🧁 Cupcake
🧰 Toolbox
👩🏼‍👧🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁡󠁴󠀴󠁿 Flag for Upper Austria (AT-4)
👨🏽‍👩🏽‍👦🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
👨🏾‍👩🏾‍👦🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁱󠁡󠁤󠁡󠁿 Flag for Doha (QA-DA)
🏴󠁩󠁮󠁫󠁡󠁿 Flag for Karnataka (IN-KA)
🧺 Basket
🏴󠁧󠁲󠁡󠁿 Flag for East Macedonia and Thrace (GR-A)
🏴󠁥󠁴󠁳󠁮󠁿 Flag for Southern Nations, Nationalities, and Peoples (ET-SN)
󠁁 Tag Latin Capital Letter a
👨🏿‍👩🏿‍👦🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
2 Digit Two
🧻 Roll Of Toilet Paper
🏴󠁵󠁳󠁮󠁥󠁿 Flag for Nebraska (US-NE)
󠀢 Tag Quotation Mark
🏴󠁡󠁵󠁮󠁳󠁷󠁿 Flag for New South Wales (AU-NSW)
🏴󠁡󠁺󠁡󠁧󠁡󠁿 Flag for Agstafa (AZ-AGA)
🏴󠁡󠁦󠁴󠁡󠁫󠁿 Flag for Takhar (AF-TAK)
🏴󠁡󠁺󠁡󠁧󠁣󠁿 Flag for Aghjabadi (AZ-AGC)
🧼 Bar Of Soap
👩‍❤️‍💋‍👨🏼 Kiss - Woman, Man: Medium-Light Skin Tone
🏴󠁡󠁺󠁢󠁡󠁬󠁿 Flag for Balakan (AZ-BAL)
👩🏾‍👩🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
󠀪 Tag Asterisk
🏴󠁡󠁺󠁡󠁧󠁳󠁿 Flag for Agdash (AZ-AGS)
👨🏻‍❤️‍💋‍👩🏿 Kiss - Man: Light Skin Tone, Woman: Dark Skin Tone
🏴󠁡󠁺󠁡󠁧󠁭󠁿 Flag for Agdam (AZ-AGM)
🏴󠁵󠁳󠁣󠁯󠁿 Flag for Colorado (US-CO)
🏴󠁡󠁺󠁡󠁳󠁴󠁿 Flag for Astara (AZ-AST)
🏴󠁮󠁬󠁢󠁱󠀱󠁿 Flag for Bonaire (NL-BQ1)
🏴󠁮󠁯󠀱󠀰󠁿 Flag for Vest-Agder (NO-10)
󠁉 Tag Latin Capital Letter I
🏴󠁡󠁺󠁢󠁡󠁿 Flag for Baku (AZ-BA)
👩🏾‍👧🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁡󠁺󠁡󠁧󠁵󠁿 Flag for Agsu (AZ-AGU)
🏴󠁣󠁤󠁴󠁡󠁿 Flag for Tanganyika (CD-TA)
🥭 Mango
🧽 Sponge
🏴󠁤󠁺󠀱󠀶󠁿 Flag for Algiers (DZ-16)
👨🏻‍👩🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone
🏴󠁳󠁩󠀰󠀸󠀵󠁿 Flag for Novo Mesto (SI-085)
🏴󠁡󠁺󠁣󠁡󠁬󠁿 Flag for Jalilabad (AZ-CAL)
🏴󠁡󠁺󠁢󠁡󠁲󠁿 Flag for Barda (AZ-BAR)
👩🏼‍👶🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁡󠁺󠁣󠁡󠁢󠁿 Flag for Jabrayil (AZ-CAB)
🏴󠁡󠁺󠁤󠁡󠁳󠁿 Flag for Dashkasan (AZ-DAS)
👩🏻‍❤️‍👨🏼 Couple With Heart - Woman: Light Skin Tone, Man: Medium-Light Skin Tone
👨🏻‍👧🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone
👨🏼‍👩🏼‍👧🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁡󠁺󠁢󠁥󠁹󠁿 Flag for Beylagan (AZ-BEY)
🧾 Receipt
🏴󠁡󠁺󠁢󠁩󠁬󠁿 Flag for Bilasuvar (AZ-BIL)
🏴󠁣󠁧󠀹󠁿 Flag for Niari (CG-9)
🏴󠁡󠁺󠁦󠁵󠁺󠁿 Flag for Fizuli (AZ-FUZ)
🏴󠁱󠁡󠁵󠁳󠁿 Flag for Umm Salal (QA-US)
👩🏿‍❤️‍💋‍👨🏽 Kiss - Woman: Dark Skin Tone, Man: Medium Skin Tone
👨🏿‍❤️‍👨🏾 Couple With Heart - Man: Dark Skin Tone, Man: Medium-Dark Skin Tone
󠁛 Tag Left Square Bracket
🏴󠁡󠁺󠁧󠁯󠁹󠁿 Flag for Goychay (AZ-GOY)
🏴󠁩󠁲󠀱󠀳󠁿 Flag for Sistan and Baluchestan (IR-13)
🏴󠁡󠁺󠁧󠁯󠁲󠁿 Flag for Goranboy (AZ-GOR)
🏴󠁦󠁪󠁥󠁿 Flag for Eastern (FJ-E)
🏴󠁡󠁺󠁧󠁹󠁧󠁿 Flag for Goygol (AZ-GYG)
🏴󠁡󠁺󠁨󠁡󠁣󠁿 Flag for Hajigabul (AZ-HAC)
🏴󠁡󠁭󠁴󠁶󠁿 Flag for Tavush (AM-TV)
🏴󠁬󠁶󠀰󠀷󠀷󠁿 Flag for Rēzekne Municipality (LV-077)
👩🏿‍❤️‍💋‍👩 Kiss - Woman: Dark Skin Tone, Woman
👨🏽‍❤️‍💋‍👩🏾 Kiss - Man: Medium Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁮󠁧󠁦󠁣󠁿 Flag for Federal Capital Territory (NG-FC)
🏴󠁲󠁵󠁢󠁲󠁹󠁿 Flag for Bryansk (RU-BRY)
🏴󠁥󠁣󠁳󠁤󠁿 Flag for Santo Domingo de los Tsáchilas (EC-SD)
🏴󠁴󠁨󠀱󠀶󠁿 Flag for Lopburi (TH-16)
🏴󠁡󠁵󠁶󠁩󠁣󠁿 Flag for Victoria (AU-VIC)
🏴󠁲󠁵󠁬󠁥󠁮󠁿 Flag for Leningrad (RU-LEN)
👨🏻‍👩🏻‍👦🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
👩🏼‍❤️‍👩 Couple With Heart - Woman: Medium-Light Skin Tone, Woman
🏴󠁡󠁺󠁩󠁭󠁩󠁿 Flag for Imishli (AZ-IMI)
🏴󠁬󠁡󠁸󠁥󠁿 Flag for Sekong (LA-XE)
🏴󠁲󠁯󠁧󠁪󠁿 Flag for Gorj (RO-GJ)
🏴󠁭󠁸󠁢󠁣󠁳󠁿 Flag for Baja California Sur (MX-BCS)
🏴󠁡󠁺󠁫󠁵󠁲󠁿 Flag for Kurdamir (AZ-KUR)
👩🏻‍👨🏻‍👦🏻‍👧🏻 Family - Woman: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
🏴󠁡󠁺󠁬󠁡󠁿 Flag for Lankaran (AZ-LA)
🏴󠁶󠁮󠁳󠁧󠁿 Flag for Ho Chi Minh City (VN-SG)
🏴󠁡󠁺󠁧󠁡󠁤󠁿 Flag for Gadabay (AZ-GAD)
🏴󠁵󠁳󠁭󠁡󠁿 Flag for Massachusetts (US-MA)
🏴󠁡󠁺󠁬󠁡󠁣󠁿 Flag for Lachin (AZ-LAC)
🏴󠁡󠁺󠁫󠁡󠁬󠁿 Flag for Kalbajar (AZ-KAL)
🏴󠁡󠁺󠁬󠁥󠁲󠁿 Flag for Lerik (AZ-LER)
👨🏻‍❤️‍👨 Couple With Heart - Man: Light Skin Tone, Man
🏴󠁡󠁺󠁭󠁩󠁿 Flag for Mingachevir (AZ-MI)
🏴󠁡󠁺󠁮󠁡󠁿 Flag for Naftalan (AZ-NA)
󠀫 Tag Plus Sign
🏴󠁡󠁺󠁭󠁡󠁳󠁿 Flag for Masally (AZ-MAS)
👨‍❤️‍👩 Couple With Heart - Man, Woman
🏴󠁡󠁺󠁬󠁡󠁮󠁿 Flag for Lankaran District (AZ-LAN)
👩🏼‍👨🏼‍👧🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩🏽‍❤️‍💋‍👨🏾 Kiss - Woman: Medium Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁡󠁵󠁡󠁣󠁴󠁿 Flag for Australian Capital Territory (AU-ACT)
🏴󠁥󠁳󠁮󠁣󠁿 Flag for Navarra Chartered Community (ES-NC)
👩🏿‍👧🏿‍👶🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁡󠁺󠁮󠁥󠁦󠁿 Flag for Neftchala (AZ-NEF)
🏴󠁡󠁺󠁮󠁸󠁿 Flag for Nakhchivan AR (AZ-NX)
🏴󠁳󠁩󠀰󠀱󠀱󠁿 Flag for Celje (SI-011)
🏴󠁬󠁴󠀳󠀲󠁿 Flag for Panevėžio Municipality (LT-32)
👩🏻‍👧🏻‍👶🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
󠁨 Tag Latin Small Letter H
🏴󠁡󠁺󠁩󠁳󠁭󠁿 Flag for Ismailli (AZ-ISM)
👩🏾‍❤️‍👨🏻 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Light Skin Tone
👨🏻‍❤️‍👩🏿 Couple With Heart - Man: Light Skin Tone, Woman: Dark Skin Tone
🏴󠁡󠁺󠁱󠁯󠁢󠁿 Flag for Gobustan (AZ-QOB)
👩🏿‍❤️‍💋‍👩🏿 Kiss - Woman: Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁲󠁯󠁢󠁶󠁿 Flag for Braşov (RO-BV)
🏴󠁡󠁺󠁱󠁢󠁩󠁿 Flag for Qubadli (AZ-QBI)
👩🏿‍❤️‍💋‍👨🏻 Kiss - Woman: Dark Skin Tone, Man: Light Skin Tone
🏴󠁣󠁨󠁵󠁲󠁿 Flag for Uri (CH-UR)
🏴󠁡󠁺󠁱󠁡󠁺󠁿 Flag for Qazakh (AZ-QAZ)
👨‍👩‍👧‍👶 Family: Man, Woman, Girl, Baby
🏴󠁣󠁦󠁮󠁭󠁿 Flag for Nana-Mambéré (CF-NM)
🏴󠁡󠁺󠁱󠁢󠁡󠁿 Flag for Quba (AZ-QBA)
🏴󠁡󠁺󠁱󠁡󠁢󠁿 Flag for Qabala (AZ-QAB)
🏴󠁡󠁺󠁯󠁧󠁵󠁿 Flag for Oghuz (AZ-OGU)
🏴󠁡󠁺󠁱󠁡󠁸󠁿 Flag for Qakh (AZ-QAX)
🏴󠁳󠁩󠀲󠀰󠀶󠁿 Flag for Šmarješke Toplice (SI-206)
👨🏾‍❤️‍💋‍👩🏿 Kiss - Man: Medium-Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁴󠁭󠁳󠁿 Flag for Aşgabat (TM-S)
🏴󠁬󠁲󠁭󠁹󠁿 Flag for Maryland (LR-MY)
🏴󠁡󠁺󠁱󠁵󠁳󠁿 Flag for Qusar (AZ-QUS)
👨‍❤️‍💋‍👩🏻 Kiss - Man, Woman: Light Skin Tone
🏴󠁡󠁺󠁳󠁡󠁢󠁿 Flag for Sabirabad (AZ-SAB)
🏴󠁡󠁧󠀰󠀷󠁿 Flag for Saint Peter (AG-07)
🏴󠁡󠁺󠁳󠁡󠁴󠁿 Flag for Saatly (AZ-SAT)
👨🏼‍❤️‍👩🏽 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Medium Skin Tone
👨‍👩‍👶‍👶 Family: Man, Woman, Baby, Baby
🏴󠁡󠁺󠁳󠁢󠁮󠁿 Flag for Shabran (AZ-SBN)
🏴󠁡󠁺󠁳󠁡󠁫󠁿 Flag for Shaki District (AZ-SAK)
👩‍👨‍👧‍👧 Family: Woman, Man, Girl, Girl
🏴󠁣󠁯󠁣󠁡󠁳󠁿 Flag for Casanare (CO-CAS)
󠁗 Tag Latin Capital Letter W
👩🏻‍👶🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone
🏴󠁡󠁵󠁷󠁡󠁿 Flag for Western Australia (AU-WA)
🏴󠁦󠁲󠁭󠁱󠁿 Flag for Martinique (FR-MQ)
🏴󠁡󠁺󠁳󠁭󠁸󠁿 Flag for Samukh (AZ-SMX)
🏴󠁡󠁺󠁳󠁭󠁩󠁿 Flag for Shamakhi (AZ-SMI)
👩🏽‍👶🏽 Family - Woman: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁡󠁺󠁳󠁭󠁿 Flag for Sumqayit (AZ-SM)
🏴󠁡󠁺󠁳󠁡󠁿 Flag for Shaki (AZ-SA)
🏴󠁡󠁺󠁳󠁩󠁹󠁿 Flag for Siazan (AZ-SIY)
🏴󠁡󠁺󠁳󠁲󠁿 Flag for Shirvan (AZ-SR)
🏴󠁡󠁺󠁳󠁵󠁳󠁿 Flag for Shusha (AZ-SUS)
🏴󠁣󠁨󠁶󠁳󠁿 Flag for Valais (CH-VS)
👩🏻‍❤️‍💋‍👨🏿 Kiss - Woman: Light Skin Tone, Man: Dark Skin Tone
👩🏿‍❤️‍💋‍👨 Kiss - Woman: Dark Skin Tone, Man
🏴󠁡󠁺󠁴󠁡󠁲󠁿 Flag for Tartar (AZ-TAR)
🏴󠁡󠁦󠁷󠁡󠁲󠁿 Flag for Maidan Wardak (AF-WAR)
👨🏻‍👩🏻‍👧🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁡󠁺󠁴󠁯󠁶󠁿 Flag for Tovuz (AZ-TOV)
🏴󠁡󠁺󠁸󠁡󠁣󠁿 Flag for Khachmaz (AZ-XAC)
🏴󠁡󠁺󠁵󠁣󠁡󠁿 Flag for Ujar (AZ-UCA)
🏴󠁭󠁹󠀰󠀳󠁿 Flag for Kelantan (MY-03)
👨🏿‍❤️‍💋‍👨🏻 Kiss - Man: Dark Skin Tone, Man: Light Skin Tone
󠀼 Tag Less-Than Sign
👨🏽‍👩🏽‍👧🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁶󠁥󠁹󠁿 Flag for Delta Amacuro (VE-Y)
🏴󠁡󠁺󠁸󠁩󠁺󠁿 Flag for Khizi (AZ-XIZ)
󠁘 Tag Latin Capital Letter X
🏴󠁡󠁺󠁸󠁣󠁩󠁿 Flag for Khojali (AZ-XCI)
🏴󠁡󠁺󠁸󠁡󠁿 Flag for Stepanakert (AZ-XA)
👨🏽‍❤️‍👨🏼 Couple With Heart - Man: Medium Skin Tone, Man: Medium-Light Skin Tone
🏴󠁡󠁺󠁹󠁡󠁲󠁿 Flag for Yardymli (AZ-YAR)
🏴󠁡󠁺󠁹󠁥󠁿 Flag for Yevlakh (AZ-YE)
🏴󠁡󠁺󠁹󠁥󠁶󠁿 Flag for Yevlakh District (AZ-YEV)
🏴󠁡󠁺󠁺󠁡󠁱󠁿 Flag for Zaqatala (AZ-ZAQ)
👩🏽‍👧🏽‍👧🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
👩🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁡󠁺󠁺󠁡󠁲󠁿 Flag for Zardab (AZ-ZAR)
🏴󠁡󠁺󠁳󠁡󠁬󠁿 Flag for Salyan (AZ-SAL)
🏴󠁣󠁨󠁺󠁧󠁿 Flag for Zug (CH-ZG)
🧴 Lotion Bottle
👨🏾‍👩🏾‍👧🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👨🏿‍👩🏿‍👧🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
👩🏿‍👶🏿 Family - Woman: Dark Skin Tone, Baby: Dark Skin Tone
👨🏼‍👩🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👨‍❤️‍👩🏼 Couple With Heart - Man, Woman: Medium-Light Skin Tone
👨🏼‍👩🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👩🏾‍👧🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👨🏽‍❤️‍👩 Couple With Heart - Man: Medium Skin Tone, Woman
🏴󠁢󠁡󠁳󠁲󠁰󠁿 Flag for Republika Srpska (BA-SRP)
👨🏻‍👩🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone
👨‍❤️‍👩🏽 Couple With Heart - Man, Woman: Medium Skin Tone
🏴󠁥󠁳󠁡󠁮󠁿 Flag for Andalusia (ES-AN)
🏴󠁡󠁵󠁮󠁴󠁿 Flag for Northern Territory (AU-NT)
👩🏼‍👩🏼‍👧🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👨🏾‍❤️‍👩🏼 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
👨‍👩‍👶‍👦 Family: Man, Woman, Baby, Boy
🏴󠁣󠁯󠁱󠁵󠁩󠁿 Flag for Quindío (CO-QUI)
🏴󠁢󠁢󠀰󠀲󠁿 Flag for Saint Andrew (BB-02)
🏴󠁢󠁢󠀰󠀴󠁿 Flag for Saint James (BB-04)
🏴󠁢󠁢󠀰󠀳󠁿 Flag for Saint George (BB-03)
👨🏾‍👩🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁢󠁡󠁢󠁩󠁨󠁿 Flag for Federation of Bosnia and Herzegovina (BA-BIH)
🏴󠁢󠁹󠁢󠁲󠁿 Flag for Brest (BY-BR)
🏴󠁢󠁢󠀰󠀵󠁿 Flag for Saint John (BB-05)
🏴󠁡󠁺󠁳󠁫󠁲󠁿 Flag for Shamkir (AZ-SKR)
🏴󠁢󠁢󠀰󠀷󠁿 Flag for Saint Lucy (BB-07)
👨🏽‍👩🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁬󠁫󠀱󠁿 Flag for Western (LK-1)
🏴󠁢󠁢󠀰󠀶󠁿 Flag for Saint Joseph (BB-06)
👩🏻‍👶🏻‍👦🏻 Family - Woman: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
🏴󠁶󠁣󠀰󠀴󠁿 Flag for Saint George (VC-04)
🏴󠁢󠁢󠀱󠀰󠁿 Flag for Saint Philip (BB-10)
🏴󠁥󠁳󠁣󠁭󠁿 Flag for Castile-La Mancha (ES-CM)
👨🏻‍👩🏻‍👶🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
👩🏻‍👧🏻‍👧🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
🏴󠁢󠁤󠁡󠁿 Flag for Barisal (BD-A)
🏴󠁡󠁺󠁺󠁡󠁮󠁿 Flag for Zangilan (AZ-ZAN)
🏴󠁵󠁳󠁣󠁡󠁿 Flag for California (US-CA)
🏴󠁪󠁭󠀰󠀱󠁿 Flag for Kingston (JM-01)
🏴󠁢󠁤󠁦󠁿 Flag for Rangpur Division (BD-F)
🏴󠁢󠁤󠁣󠁿 Flag for Dhaka Division (BD-C)
🏴󠁢󠁤󠁥󠁿 Flag for Rajshahi Division (BD-E)
🏴󠁢󠁤󠁤󠁿 Flag for Khulna Division (BD-D)
🏴󠁢󠁢󠀰󠀹󠁿 Flag for Saint Peter (BB-09)
🏴󠁢󠁦󠀰󠀴󠁿 Flag for Centre-Est (BF-04)
🏴󠁣󠁮󠀹󠀱󠁿 Flag for Hong Kong SAR China (CN-91)
👩🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁭󠁵󠁢󠁲󠁿 Flag for Beau-Bassin Rose-Hill (MU-BR)
🏴󠁳󠁩󠀰󠀵󠀸󠁿 Flag for Lenart (SI-058)
🏴󠁢󠁤󠁨󠁿 Flag for Mymensingh Division (BD-H)
🏴󠁢󠁦󠀰󠀱󠁿 Flag for Boucle du Mouhoun (BF-01)
🏴󠁤󠁫󠀸󠀲󠁿 Flag for Central Denmark (DK-82)
🏴󠁢󠁦󠀰󠀳󠁿 Flag for Centre (BF-03)
🏴󠁢󠁥󠁷󠁡󠁬󠁿 Flag for Wallonia (BE-WAL)
🏴󠁢󠁦󠀰󠀲󠁿 Flag for Cascades (BF-02)
👨🏿‍❤️‍👨 Couple With Heart - Man: Dark Skin Tone, Man
🏴󠁢󠁦󠀰󠀷󠁿 Flag for Centre-Sud (BF-07)
👨🏽‍👩🏽‍👶🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁢󠁦󠀰󠀶󠁿 Flag for Centre-Ouest (BF-06)
🏴󠁢󠁦󠀰󠀸󠁿 Flag for Est (BF-08)
🏴󠁢󠁤󠁧󠁿 Flag for Sylhet Division (BD-G)
🏴󠁢󠁦󠀰󠀵󠁿 Flag for Centre-Nord (BF-05)
🏴󠁢󠁢󠀱󠀱󠁿 Flag for Saint Thomas (BB-11)
🏴󠁢󠁥󠁢󠁲󠁵󠁿 Flag for Brussels (BE-BRU)
👨🏽‍👩🏽‍👧🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
👨🏽‍❤️‍👩🏿 Couple With Heart - Man: Medium Skin Tone, Woman: Dark Skin Tone
🏴󠁥󠁳󠁭󠁤󠁿 Flag for Madrid Autonomous Community (ES-MD)
🏴󠁢󠁢󠀰󠀸󠁿 Flag for Saint Michael (BB-08)
👨🏼‍👩🏼‍👦🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👨🏾‍👩🏾‍👶🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁢󠁧󠀰󠀵󠁿 Flag for Vidin (BG-05)
🏴󠁢󠁧󠀰󠀲󠁿 Flag for Burgas (BG-02)
🏴󠁢󠁧󠀰󠀳󠁿 Flag for Varna (BG-03)
👩🏾‍❤️‍👩🏻 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Light Skin Tone
🏴󠁢󠁦󠀱󠀳󠁿 Flag for Sud-Ouest (BF-13)
🏴󠁢󠁤󠁢󠁿 Flag for Chittagong Division (BD-B)
👨🏿‍❤️‍👩🏽 Couple With Heart - Man: Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁢󠁦󠀱󠀱󠁿 Flag for Plateau-Central (BF-11)
🏴󠁢󠁦󠀱󠀰󠁿 Flag for Nord (BF-10)
👨🏿‍👩🏿‍👶🏿‍👦🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁦󠀱󠀲󠁿 Flag for Sahel (BF-12)
🏴󠁢󠁧󠀰󠀸󠁿 Flag for Dobrich (BG-08)
👨🏿‍❤️‍👩🏻 Couple With Heart - Man: Dark Skin Tone, Woman: Light Skin Tone
👨🏽‍👩🏽‍👧🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
🧭 Compass
🏴󠁩󠁲󠀱󠀶󠁿 Flag for Kurdistan (IR-16)
󠁖 Tag Latin Capital Letter V
🏴󠁢󠁧󠀰󠀷󠁿 Flag for Gabrovo (BG-07)
👩🏻‍👧🏻‍👦🏻 Family - Woman: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
👨🏼‍👩🏼‍👶🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏾‍❤️‍💋‍👩🏾 Kiss - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁣󠁬󠁬󠁩󠁿 Flag for Libertador General Bernardo O’Higgins (CL-LI)
🏴󠁢󠁧󠀱󠀱󠁿 Flag for Lovech (BG-11)
🏴󠁢󠁧󠀱󠀳󠁿 Flag for Pazardzhik (BG-13)
👨🏿‍❤️‍👩🏿 Couple With Heart - Man: Dark Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁧󠀱󠀴󠁿 Flag for Pernik (BG-14)
🏴󠁢󠁧󠀱󠀰󠁿 Flag for Kyustendil (BG-10)
󠀣 Tag Number Sign
🏴󠁢󠁧󠀱󠀵󠁿 Flag for Pleven (BG-15)
🏴󠁥󠁧󠁢󠁡󠁿 Flag for Red Sea (EG-BA)
👨🏽‍👩🏽‍👶🏽‍👧🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
👩‍❤️‍👨🏼 Couple With Heart - Woman, Man: Medium-Light Skin Tone
🏴󠁢󠁧󠀲󠀱󠁿 Flag for Smolyan (BG-21)
🏴󠁤󠁺󠀳󠀴󠁿 Flag for Bordj Bou Arréridj (DZ-34)
🏴󠁢󠁧󠀱󠀶󠁿 Flag for Plovdiv (BG-16)
🏴󠁣󠁩󠁶󠁢󠁿 Flag for Vallée du Bandama (CI-VB)
󠀯 Tag Solidus
🏴󠁢󠁧󠀱󠀹󠁿 Flag for Silistra (BG-19)
🏴󠁢󠁧󠀱󠀷󠁿 Flag for Razgrad (BG-17)
👨🏾‍❤️‍👨 Couple With Heart - Man: Medium-Dark Skin Tone, Man
🏴󠁢󠁧󠀲󠀰󠁿 Flag for Sliven (BG-20)
🏴󠁡󠁯󠁣󠁮󠁮󠁿 Flag for Cunene (AO-CNN)
🏴󠁢󠁧󠀰󠀱󠁿 Flag for Blagoevgrad (BG-01)
🏴󠁢󠁧󠀲󠀵󠁿 Flag for Targovishte (BG-25)
👨🏾‍👩🏾‍👶🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
󠁎 Tag Latin Capital Letter N
👩🏼‍👩🏼‍👶🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁦󠁲󠁰󠁡󠁣󠁿 Flag for Provence-Alpes-Côte-d’Azur (FR-PAC)
🧕🏻‍♀️ Woman With Headscarf: Light Skin Tone
🏴󠁢󠁧󠀲󠀲󠁿 Flag for Sofia (BG-22)
🏴󠁢󠁧󠀲󠀳󠁿 Flag for Sofia District (BG-23)
󠁜 Tag Reverse Solidus
👨🏻‍❤️‍💋‍👩🏾 Kiss - Man: Light Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁢󠁧󠀲󠀸󠁿 Flag for Yambol (BG-28)
🧕🏽‍♀️ Woman With Headscarf: Medium Skin Tone
🏴󠁢󠁨󠀱󠀳󠁿 Flag for Capital (BH-13)
🏴󠁢󠁧󠀲󠀶󠁿 Flag for Haskovo (BG-26)
🏴󠁬󠁩󠀰󠀷󠁿 Flag for Schaan (LI-07)
👨🏿‍👩🏿‍👶🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁢󠁨󠀱󠀵󠁿 Flag for Muharraq (BH-15)
🏴󠁲󠁯󠁳󠁢󠁿 Flag for Sibiu (RO-SB)
👩🏻‍❤️‍👩 Couple With Heart - Woman: Light Skin Tone, Woman
🏴󠁢󠁨󠀱󠀴󠁿 Flag for Southern (BH-14)
👩🏻‍❤️‍👨🏿 Couple With Heart - Woman: Light Skin Tone, Man: Dark Skin Tone
👨🏿‍👨🏿‍👦🏿‍👦🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁨󠀱󠀷󠁿 Flag for Northern (BH-17)
🧕🏾‍♀️ Woman With Headscarf: Medium-Dark Skin Tone
🏴󠁢󠁩󠁢󠁢󠁿 Flag for Bubanza (BI-BB)
🏴󠁡󠁵󠁳󠁡󠁿 Flag for South Australia (AU-SA)
🏴󠁢󠁩󠁢󠁭󠁿 Flag for Bujumbura (BI-BM)
🧕🏿‍♀️ Woman With Headscarf: Dark Skin Tone
👨🏿‍👩🏿‍👧🏿‍👧🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
👩🏽‍👧🏽 Family - Woman: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁢󠁩󠁢󠁬󠁿 Flag for Bujumbura Rural (BI-BL)
👨🏻‍👩🏻‍👶🏻‍👶🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🧕🏼‍♀️ Woman With Headscarf: Medium-Light Skin Tone
👨🏾‍❤️‍💋‍👩🏽 Kiss - Man: Medium-Dark Skin Tone, Woman: Medium Skin Tone
👨🏻‍👨🏻‍👦🏻‍👶🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁢󠁩󠁣󠁡󠁿 Flag for Cankuzo (BI-CA)
🏴󠁬󠁶󠀰󠀸󠀵󠁿 Flag for Sala (LV-085)
👩🏼‍❤️‍👨🏽 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁧󠀱󠀲󠁿 Flag for Montana (BG-12)
🏴󠁢󠁩󠁢󠁲󠁿 Flag for Bururi (BI-BR)
🏴󠁢󠁧󠀰󠀹󠁿 Flag for Kardzhali (BG-09)
🏴󠁢󠁥󠁶󠁬󠁧󠁿 Flag for Flanders (BE-VLG)
🏴󠁢󠁩󠁲󠁭󠁿 Flag for Rumonge (BI-RM)
👩🏼‍👧🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁢󠁩󠁭󠁹󠁿 Flag for Muyinga (BI-MY)
🏴󠁬󠁲󠁲󠁧󠁿 Flag for River Gee (LR-RG)
🏴󠁮󠁬󠁡󠁷󠁿 Flag for Aruba (NL-AW)
🏴󠁢󠁩󠁲󠁹󠁿 Flag for Ruyigi (BI-RY)
🏴󠁢󠁩󠁮󠁧󠁿 Flag for Ngozi (BI-NG)
🏴󠁢󠁩󠁫󠁩󠁿 Flag for Kirundo (BI-KI)
🏴󠁢󠁩󠁫󠁹󠁿 Flag for Kayanza (BI-KY)
🏴󠁢󠁧󠀲󠀷󠁿 Flag for Shumen (BG-27)
🏴󠁢󠁩󠁭󠁷󠁿 Flag for Mwaro (BI-MW)
🏴󠁢󠁩󠁭󠁵󠁿 Flag for Muramvya (BI-MU)
👩🏼‍👦🏼‍👧🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
🏴󠁭󠁡󠀱󠀵󠁿 Flag for Laâyoune-Boujdour-Sakia El Hamra (MA-15)
🏴󠁢󠁩󠁫󠁲󠁿 Flag for Karuzi (BI-KR)
👨🏽‍👩🏽‍👶🏽‍👶🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
👩🏾‍👨🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁢󠁩󠁲󠁴󠁿 Flag for Rutana (BI-RT)
👨🏾‍👩🏾‍👶🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
👩🏽‍👨🏽‍👶🏽‍👦🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁢󠁪󠁤󠁯󠁿 Flag for Donga (BJ-DO)
🏴󠁦󠁲󠁨󠁤󠁦󠁿 Flag for Hauts-de-France (FR-HDF)
⃣ Combining Enclosing Keycap
🏴󠁢󠁪󠁡󠁬󠁿 Flag for Alibori (BJ-AL)
🏴󠁢󠁪󠁡󠁫󠁿 Flag for Atakora (BJ-AK)
👨🏽‍❤️‍💋‍👩🏼 Kiss - Man: Medium Skin Tone, Woman: Medium-Light Skin Tone
👨🏿‍👩🏿‍👶🏿‍👶🏿 Family - Man: Dark Skin Tone, Woman: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁢󠁪󠁬󠁩󠁿 Flag for Littoral (BJ-LI)
🏴󠁢󠁪󠁫󠁯󠁿 Flag for Kouffo (BJ-KO)
🏴󠁢󠁪󠁢󠁯󠁿 Flag for Borgou (BJ-BO)
👩‍👩‍👧‍👶 Family: Woman, Woman, Girl, Baby
👨🏼‍❤️‍💋‍👨🏾 Kiss - Man: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁢󠁪󠁺󠁯󠁿 Flag for Zou (BJ-ZO)
🏴󠁢󠁪󠁰󠁬󠁿 Flag for Plateau (BJ-PL)
🏴󠁵󠁳󠁮󠁤󠁿 Flag for North Dakota (US-ND)
🏴󠁡󠁬󠀰󠀵󠁿 Flag for Gjirokastër County (AL-05)
🏴󠁧󠁤󠀱󠀰󠁿 Flag for Carriacou and Petite Martinique (GD-10)
👩🏽‍❤️‍👨🏻 Couple With Heart - Woman: Medium Skin Tone, Man: Light Skin Tone
👩🏻‍👦🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone
👩🏽‍❤️‍👨🏽 Couple With Heart - Woman: Medium Skin Tone, Man: Medium Skin Tone
👨🏽‍❤️‍👩🏼 Couple With Heart - Man: Medium Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁢󠁯󠁢󠁿 Flag for Beni (BO-B)
🏴󠁢󠁮󠁢󠁭󠁿 Flag for Brunei-Muara (BN-BM)
🏴󠁢󠁮󠁴󠁥󠁿 Flag for Temburong (BN-TE)
🏴󠁢󠁮󠁴󠁵󠁿 Flag for Tutong (BN-TU)
👩🏽‍❤️‍👨🏼 Couple With Heart - Woman: Medium Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁮󠁢󠁥󠁿 Flag for Belait (BN-BE)
👩🏼‍❤️‍👨🏻 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Light Skin Tone
👩🏼‍❤️‍👨 Couple With Heart - Woman: Medium-Light Skin Tone, Man
🏴󠁢󠁪󠁯󠁵󠁿 Flag for Ouémé (BJ-OU)
🏴󠁢󠁧󠀰󠀶󠁿 Flag for Vratsa (BG-06)
🏴󠁬󠁢󠁢󠁩󠁿 Flag for Beqaa (LB-BI)
🕴🏽‍♀️ Woman in Business Suit Levitating: Medium Skin Tone
👩🏽‍👦🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone
👨🏾‍👩🏾‍👧🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁢󠁯󠁣󠁿 Flag for Cochabamba (BO-C)
👩🏻‍❤️‍👨🏾 Couple With Heart - Woman: Light Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁢󠁯󠁮󠁿 Flag for Pando (BO-N)
👩🏽‍❤️‍👩🏻 Couple With Heart - Woman: Medium Skin Tone, Woman: Light Skin Tone
👩🏾‍❤️‍👨🏽 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁯󠁨󠁿 Flag for Chuquisaca (BO-H)
👩🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁭󠁮󠀰󠀳󠀹󠁿 Flag for Khentii (MN-039)
🏴󠁢󠁯󠁬󠁿 Flag for La Paz (BO-L)
🏴󠁭󠁫󠀲󠀷󠁿 Flag for Dolneni (MK-27)
🏴󠁳󠁣󠀲󠀵󠁿 Flag for Roche Caiman (SC-25)
🏴󠁢󠁧󠀲󠀴󠁿 Flag for Stara Zagora (BG-24)
🥳 Face With Smiling Eyes And Party Horn And Party Hat
👩‍❤️‍💋‍👨🏻 Kiss - Woman, Man: Light Skin Tone
🏴󠁢󠁲󠁡󠁣󠁿 Flag for Acre (BR-AC)
🏴󠁢󠁱󠁳󠁡󠁿 Flag for Saba (BQ-SA)
🏴󠁢󠁯󠁰󠁿 Flag for Potosí (BO-P)
🏴󠁢󠁱󠁢󠁯󠁿 Flag for Bonaire (BQ-BO)
🏴󠁢󠁩󠁧󠁩󠁿 Flag for Gitega (BI-GI)
👩🏿‍❤️‍👨🏻 Couple With Heart - Woman: Dark Skin Tone, Man: Light Skin Tone
👩🏿‍👦🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone
👩🏾‍❤️‍👨 Couple With Heart - Woman: Medium-Dark Skin Tone, Man
👩🏼‍👦🏼‍👦🏼 Family - Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁢󠁡󠁢󠁲󠁣󠁿 Flag for Brčko District (BA-BRC)
👩🏽‍❤️‍👨🏾 Couple With Heart - Woman: Medium Skin Tone, Man: Medium-Dark Skin Tone
👩🏾‍❤️‍👨🏿 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Dark Skin Tone
👩🏾‍❤️‍👨🏼 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
👨🏼‍👩🏼‍👧🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👨🏼‍❤️‍💋‍👨🏼 Kiss - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
👨🏿‍❤️‍💋‍👨🏾 Kiss - Man: Dark Skin Tone, Man: Medium-Dark Skin Tone
👨🏼‍❤️‍💋‍👨🏽 Kiss - Man: Medium-Light Skin Tone, Man: Medium Skin Tone
🏴󠁳󠁧󠀰󠀱󠁿 Flag for Central Singapore (SG-01)
🏴󠁢󠁲󠁥󠁳󠁿 Flag for Espírito Santo (BR-ES)
👨🏿‍❤️‍💋‍👩🏾 Kiss - Man: Dark Skin Tone, Woman: Medium-Dark Skin Tone
👩🏻‍❤️‍💋‍👩🏽 Kiss - Woman: Light Skin Tone, Woman: Medium Skin Tone
👨🏼‍❤️‍💋‍👨🏿 Kiss - Man: Medium-Light Skin Tone, Man: Dark Skin Tone
🏴󠁡󠁲󠁣󠁿 Flag for Buenos Aires (AR-C)
🏴󠁢󠁲󠁡󠁰󠁿 Flag for Amapá (BR-AP)
👩🏾‍👦🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👩🏿‍❤️‍👩🏼 Couple With Heart - Woman: Dark Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁢󠁲󠁡󠁭󠁿 Flag for Amazonas (BR-AM)
🏴󠁢󠁲󠁭󠁡󠁿 Flag for Maranhão (BR-MA)
👩🏿‍❤️‍👩🏽 Couple With Heart - Woman: Dark Skin Tone, Woman: Medium Skin Tone
👨🏽‍❤️‍👨🏻 Couple With Heart - Man: Medium Skin Tone, Man: Light Skin Tone
👨🏽‍❤️‍💋‍👨🏽 Kiss - Man: Medium Skin Tone, Man: Medium Skin Tone
👨🏿‍❤️‍💋‍👨🏼 Kiss - Man: Dark Skin Tone, Man: Medium-Light Skin Tone
👩🏿‍❤️‍💋‍👩🏻 Kiss - Woman: Dark Skin Tone, Woman: Light Skin Tone
👨🏽‍❤️‍💋‍👩🏿 Kiss - Man: Medium Skin Tone, Woman: Dark Skin Tone
👩🏽‍❤️‍💋‍👩🏿 Kiss - Woman: Medium Skin Tone, Woman: Dark Skin Tone
👩🏼‍❤️‍💋‍👨🏾 Kiss - Woman: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
👩‍❤️‍💋‍👨🏾 Kiss - Woman, Man: Medium-Dark Skin Tone
👩🏻‍❤️‍💋‍👩🏼 Kiss - Woman: Light Skin Tone, Woman: Medium-Light Skin Tone
👨🏾‍❤️‍💋‍👨🏿 Kiss - Man: Medium-Dark Skin Tone, Man: Dark Skin Tone
👩🏼‍❤️‍💋‍👨🏿 Kiss - Woman: Medium-Light Skin Tone, Man: Dark Skin Tone
👨🏽‍❤️‍💋‍👩🏽 Kiss - Man: Medium Skin Tone, Woman: Medium Skin Tone
👨🏾‍❤️‍💋‍👨🏼 Kiss - Man: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
👨🏽‍❤️‍💋‍👩🏻 Kiss - Man: Medium Skin Tone, Woman: Light Skin Tone
👨🏾‍❤️‍💋‍👨 Kiss - Man: Medium-Dark Skin Tone, Man
👨🏾‍❤️‍💋‍👨🏾 Kiss - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
👩🏽‍❤️‍💋‍👨🏻 Kiss - Woman: Medium Skin Tone, Man: Light Skin Tone
👩🏿‍❤️‍💋‍👨🏿 Kiss - Woman: Dark Skin Tone, Man: Dark Skin Tone
👩🏻‍❤️‍💋‍👩🏿 Kiss - Woman: Light Skin Tone, Woman: Dark Skin Tone
👩🏾‍❤️‍💋‍👩🏿 Kiss - Woman: Medium-Dark Skin Tone, Woman: Dark Skin Tone
👩🏾‍❤️‍💋‍👩🏻 Kiss - Woman: Medium-Dark Skin Tone, Woman: Light Skin Tone
👨🏻‍👩🏻‍👧🏻‍👧🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
👩🏻‍👩🏻‍👦🏻 Family - Woman: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone
🏴󠁢󠁯󠁳󠁿 Flag for Santa Cruz (BO-S)
👩🏾‍❤️‍💋‍👨🏾 Kiss - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
👨‍❤️‍👨🏿 Couple With Heart - Man, Man: Dark Skin Tone
👨🏻‍❤️‍👨🏽 Couple With Heart - Man: Light Skin Tone, Man: Medium Skin Tone
👨🏽‍❤️‍👩🏻 Couple With Heart - Man: Medium Skin Tone, Woman: Light Skin Tone
👩🏿‍❤️‍💋‍👨🏼 Kiss - Woman: Dark Skin Tone, Man: Medium-Light Skin Tone
👩🏿‍❤️‍💋‍👩🏾 Kiss - Woman: Dark Skin Tone, Woman: Medium-Dark Skin Tone
👩🏻‍👦🏻‍👧🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
👩🏻‍❤️‍👨 Couple With Heart - Woman: Light Skin Tone, Man
👨🏻‍❤️‍👩🏽 Couple With Heart - Man: Light Skin Tone, Woman: Medium Skin Tone
👨🏽‍❤️‍👩🏽 Couple With Heart - Man: Medium Skin Tone, Woman: Medium Skin Tone
👩🏾‍❤️‍💋‍👩 Kiss - Woman: Medium-Dark Skin Tone, Woman
👩🏾‍❤️‍💋‍👩🏽 Kiss - Woman: Medium-Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁢󠁪󠁣󠁯󠁿 Flag for Collines (BJ-CO)
👩🏿‍❤️‍💋‍👩🏽 Kiss - Woman: Dark Skin Tone, Woman: Medium Skin Tone
👨‍❤️‍👨🏽 Couple With Heart - Man, Man: Medium Skin Tone
🏴󠁢󠁲󠁭󠁴󠁿 Flag for Mato Grosso (BR-MT)
👨🏼‍👩🏼‍👦🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
👨🏾‍❤️‍👨🏼 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
👨🏾‍❤️‍👩🏽 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Medium Skin Tone
👩🏽‍👦🏽‍👧🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
👨🏼‍❤️‍👨🏼 Couple With Heart - Man: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
👨🏿‍❤️‍👨🏻 Couple With Heart - Man: Dark Skin Tone, Man: Light Skin Tone
👩🏽‍❤️‍👩🏽 Couple With Heart - Woman: Medium Skin Tone, Woman: Medium Skin Tone
👨🏾‍❤️‍👨🏽 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Medium Skin Tone
👨🏽‍❤️‍👨🏽 Couple With Heart - Man: Medium Skin Tone, Man: Medium Skin Tone
👨🏾‍❤️‍👩🏿 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Dark Skin Tone
👩🏼‍❤️‍👩🏻 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Light Skin Tone
👨🏻‍❤️‍👩🏼 Couple With Heart - Man: Light Skin Tone, Woman: Medium-Light Skin Tone
👨🏿‍❤️‍👩🏼 Couple With Heart - Man: Dark Skin Tone, Woman: Medium-Light Skin Tone
👨🏼‍❤️‍👨🏾 Couple With Heart - Man: Medium-Light Skin Tone, Man: Medium-Dark Skin Tone
👨🏽‍❤️‍👨🏾 Couple With Heart - Man: Medium Skin Tone, Man: Medium-Dark Skin Tone
👩‍❤️‍👨🏾 Couple With Heart - Woman, Man: Medium-Dark Skin Tone
👩🏻‍❤️‍👨🏻 Couple With Heart - Woman: Light Skin Tone, Man: Light Skin Tone
👩🏾‍❤️‍💋‍👩🏾 Kiss - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
👨🏽‍👦🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone
👩🏾‍❤️‍👩🏾 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁢󠁲󠁲󠁪󠁿 Flag for Rio de Janeiro (BR-RJ)
👨🏾‍❤️‍💋‍👩🏻 Kiss - Man: Medium-Dark Skin Tone, Woman: Light Skin Tone
👩‍❤️‍👨🏻 Couple With Heart - Woman, Man: Light Skin Tone
👨🏾‍❤️‍👨🏿 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Dark Skin Tone
👨🏻‍👦🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone
👩🏼‍❤️‍👩🏾 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
🏴󠁢󠁲󠁲󠁮󠁿 Flag for Rio Grande do Norte (BR-RN)
🏴󠁢󠁦󠀰󠀹󠁿 Flag for Hauts-Bassins (BF-09)
👨🏼‍❤️‍👨🏽 Couple With Heart - Man: Medium-Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁲󠁰󠁩󠁿 Flag for Piauí (BR-PI)
👨🏻‍❤️‍👩 Couple With Heart - Man: Light Skin Tone, Woman
🏴󠁢󠁲󠁲󠁯󠁿 Flag for Rondônia (BR-RO)
🏴󠁢󠁲󠁡󠁬󠁿 Flag for Alagoas (BR-AL)
👨🏿‍❤️‍👩🏾 Couple With Heart - Man: Dark Skin Tone, Woman: Medium-Dark Skin Tone
👨🏽‍👩🏽‍👦🏽‍👦🏽 Family - Man: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👩🏽‍❤️‍💋‍👩🏽 Kiss - Woman: Medium Skin Tone, Woman: Medium Skin Tone
🏴󠁢󠁲󠁰󠁲󠁿 Flag for Paraná (BR-PR)
👨🏿‍👦🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁲󠁳󠁥󠁿 Flag for Sergipe (BR-SE)
👩🏼‍❤️‍👩🏽 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Medium Skin Tone
👩🏾‍❤️‍👩🏼 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
👩🏿‍👦🏿‍👦🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁲󠁲󠁳󠁿 Flag for Rio Grande do Sul (BR-RS)
🏴󠁮󠁯󠀱󠀴󠁿 Flag for Sogn og Fjordane (NO-14)
👩🏼‍❤️‍👨🏿 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Dark Skin Tone
👨🏽‍👦🏽‍👦🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
👨🏼‍❤️‍👩🏻 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Light Skin Tone
👨🏿‍❤️‍👨🏽 Couple With Heart - Man: Dark Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁳󠁢󠁩󠁿 Flag for Bimini (BS-BI)
👨🏻‍❤️‍💋‍👨🏻 Kiss - Man: Light Skin Tone, Man: Light Skin Tone
🏴󠁢󠁲󠁴󠁯󠁿 Flag for Tocantins (BR-TO)
👨🏻‍👨🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone
👨🏿‍❤️‍👩 Couple With Heart - Man: Dark Skin Tone, Woman
👨🏿‍👦🏿‍👦🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁲󠁲󠁲󠁿 Flag for Roraima (BR-RR)
🏴󠁳󠁩󠀱󠀸󠀲󠁿 Flag for Sveti Andraž v Slovenskih Goricah (SI-182)
🏴󠁢󠁯󠁯󠁿 Flag for Oruro (BO-O)
🏴󠁢󠁳󠁣󠁫󠁿 Flag for Crooked Island (BS-CK)
🏴󠁢󠁳󠁣󠁥󠁿 Flag for Central Eleuthera (BS-CE)
👩🏽‍❤️‍👨 Couple With Heart - Woman: Medium Skin Tone, Man
🏴󠁢󠁩󠁭󠁡󠁿 Flag for Makamba (BI-MA)
🏴󠁢󠁳󠁥󠁧󠁿 Flag for East Grand Bahama (BS-EG)
🏴󠁢󠁳󠁣󠁳󠁿 Flag for Central Andros (BS-CS)
🏴󠁢󠁳󠁥󠁸󠁿 Flag for Exuma (BS-EX)
👨🏼‍❤️‍💋‍👩🏼 Kiss - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
🏴󠁢󠁲󠁤󠁦󠁿 Flag for Federal District (BR-DF)
🏴󠁢󠁳󠁣󠁯󠁿 Flag for Central Abaco (BS-CO)
👩🏻‍❤️‍👩🏾 Couple With Heart - Woman: Light Skin Tone, Woman: Medium-Dark Skin Tone
👨🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁢󠁳󠁮󠁯󠁿 Flag for North Abaco (BS-NO)
👨🏼‍👦🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏽‍👦🏽‍👧🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁢󠁳󠁬󠁩󠁿 Flag for Long Island (BS-LI)
👩🏾‍❤️‍💋‍👨🏼 Kiss - Woman: Medium-Dark Skin Tone, Man: Medium-Light Skin Tone
👩🏾‍❤️‍👩🏿 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Dark Skin Tone
👩🏿‍❤️‍👨🏾 Couple With Heart - Woman: Dark Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁩󠁲󠀰󠀱󠁿 Flag for East Azerbaijan (IR-01)
🏴󠁢󠁳󠁭󠁧󠁿 Flag for Mayaguana (BS-MG)
👨🏾‍👦🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁢󠁳󠁮󠁥󠁿 Flag for North Eleuthera (BS-NE)
🏴󠁢󠁳󠁧󠁣󠁿 Flag for Grand Cay (BS-GC)
🏴󠁢󠁳󠁦󠁰󠁿 Flag for Freeport (BS-FP)
🏴󠁢󠁳󠁩󠁮󠁿 Flag for Inagua (BS-IN)
👨🏽‍👨🏽‍👦🏽‍👧🏽 Family - Man: Medium Skin Tone, Man: Medium Skin Tone, Boy: Medium Skin Tone, Girl: Medium Skin Tone
👨🏿‍👦🏿‍👧🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
👨🏾‍❤️‍👩 Couple With Heart - Man: Medium-Dark Skin Tone, Woman
👩🏿‍❤️‍👨🏿 Couple With Heart - Woman: Dark Skin Tone, Man: Dark Skin Tone
👨🏻‍👦🏻‍👶🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
👩🏿‍❤️‍👩🏻 Couple With Heart - Woman: Dark Skin Tone, Woman: Light Skin Tone
👨‍👨‍👶 Family: Man, Man, Baby
👩🏿‍❤️‍👨 Couple With Heart - Woman: Dark Skin Tone, Man
👩🏿‍❤️‍👨🏽 Couple With Heart - Woman: Dark Skin Tone, Man: Medium Skin Tone
🏴󠁡󠁺󠁧󠁡󠁿 Flag for Ganja (AZ-GA)
🏴󠁢󠁳󠁲󠁩󠁿 Flag for Ragged Island (BS-RI)
👨‍👦‍👶 Family: Man, Boy, Baby
🏴󠁢󠁳󠁮󠁳󠁿 Flag for North Andros (BS-NS)
👨‍👶‍👧 Family: Man, Baby, Girl
👩🏼‍❤️‍👨🏼 Couple With Heart - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
👨🏻‍👦🏻‍👧🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
👨‍👨‍👶‍👦 Family: Man, Man, Baby, Boy
👨🏻‍❤️‍💋‍👨 Kiss - Man: Light Skin Tone, Man
👨🏻‍❤️‍💋‍👨🏼 Kiss - Man: Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁳󠁳󠁥󠁿 Flag for South Eleuthera (BS-SE)
👨🏻‍❤️‍💋‍👩🏻 Kiss - Man: Light Skin Tone, Woman: Light Skin Tone
👨🏼‍❤️‍💋‍👩🏾 Kiss - Man: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
👨🏾‍❤️‍💋‍👨🏻 Kiss - Man: Medium-Dark Skin Tone, Man: Light Skin Tone
👩‍❤️‍💋‍👩🏻 Kiss - Woman, Woman: Light Skin Tone
👩‍👨‍👦‍👶 Family: Woman, Man, Boy, Baby
👨🏾‍❤️‍💋‍👩 Kiss - Man: Medium-Dark Skin Tone, Woman
👨🏻‍❤️‍💋‍👨🏿 Kiss - Man: Light Skin Tone, Man: Dark Skin Tone
👩‍👩‍👦‍👧 Family: Woman, Woman, Boy, Girl
👩‍👩‍👶‍👦 Family: Woman, Woman, Baby, Boy
👨🏾‍❤️‍💋‍👩🏼 Kiss - Man: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
👨🏻‍❤️‍💋‍👩🏽 Kiss - Man: Light Skin Tone, Woman: Medium Skin Tone
👨🏽‍👦🏽‍👶🏽 Family - Man: Medium Skin Tone, Boy: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁢󠁳󠁲󠁣󠁿 Flag for Rum Cay (BS-RC)
🏴󠁢󠁲󠁳󠁣󠁿 Flag for Santa Catarina (BR-SC)
👨‍❤️‍💋‍👩🏾 Kiss - Man, Woman: Medium-Dark Skin Tone
👨‍❤️‍💋‍👨🏻 Kiss - Man, Man: Light Skin Tone
🏴󠁢󠁳󠁳󠁡󠁿 Flag for South Andros (BS-SA)
👨🏼‍❤️‍💋‍👩🏽 Kiss - Man: Medium-Light Skin Tone, Woman: Medium Skin Tone
👨🏾‍👦🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁣󠁩󠁡󠁢󠁿 Flag for Abidjan (CI-AB)
👩🏾‍❤️‍💋‍👩🏼 Kiss - Woman: Medium-Dark Skin Tone, Woman: Medium-Light Skin Tone
👨🏻‍❤️‍👨🏿 Couple With Heart - Man: Light Skin Tone, Man: Dark Skin Tone
🏴󠁢󠁳󠁳󠁯󠁿 Flag for South Abaco (BS-SO)
👩🏾‍❤️‍💋‍👨🏿 Kiss - Woman: Medium-Dark Skin Tone, Man: Dark Skin Tone
👩🏼‍❤️‍💋‍👨🏽 Kiss - Woman: Medium-Light Skin Tone, Man: Medium Skin Tone
👩🏾‍❤️‍💋‍👨🏻 Kiss - Woman: Medium-Dark Skin Tone, Man: Light Skin Tone
👨🏿‍❤️‍💋‍👩🏿 Kiss - Man: Dark Skin Tone, Woman: Dark Skin Tone
👩🏻‍❤️‍💋‍👨🏾 Kiss - Woman: Light Skin Tone, Man: Medium-Dark Skin Tone
👨‍❤️‍👨🏼 Couple With Heart - Man, Man: Medium-Light Skin Tone
👨🏿‍❤️‍💋‍👨🏿 Kiss - Man: Dark Skin Tone, Man: Dark Skin Tone
👩🏼‍❤️‍💋‍👩🏼 Kiss - Woman: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
👩🏽‍❤️‍💋‍👨🏿 Kiss - Woman: Medium Skin Tone, Man: Dark Skin Tone
👩🏽‍❤️‍💋‍👨 Kiss - Woman: Medium Skin Tone, Man
👨🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👩🏻‍❤️‍💋‍👨 Kiss - Woman: Light Skin Tone, Man
👩🏼‍❤️‍💋‍👩🏾 Kiss - Woman: Medium-Light Skin Tone, Woman: Medium-Dark Skin Tone
👨🏻‍❤️‍💋‍👩🏼 Kiss - Man: Light Skin Tone, Woman: Medium-Light Skin Tone
👨‍👧‍👶 Family: Man, Girl, Baby
👩🏿‍❤️‍💋‍👩🏼 Kiss - Woman: Dark Skin Tone, Woman: Medium-Light Skin Tone
👩🏿‍❤️‍💋‍👨🏾 Kiss - Woman: Dark Skin Tone, Man: Medium-Dark Skin Tone
👨‍❤️‍💋‍👩🏼 Kiss - Man, Woman: Medium-Light Skin Tone
👩🏼‍❤️‍💋‍👨 Kiss - Woman: Medium-Light Skin Tone, Man
👨🏼‍❤️‍💋‍👩🏻 Kiss - Man: Medium-Light Skin Tone, Woman: Light Skin Tone
👩‍❤️‍👩🏾 Couple With Heart - Woman, Woman: Medium-Dark Skin Tone
👨🏿‍❤️‍👨🏼 Couple With Heart - Man: Dark Skin Tone, Man: Medium-Light Skin Tone
👨🏼‍❤️‍👨🏿 Couple With Heart - Man: Medium-Light Skin Tone, Man: Dark Skin Tone
👨🏼‍❤️‍👩🏼 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone
👨🏽‍❤️‍👩🏾 Couple With Heart - Man: Medium Skin Tone, Woman: Medium-Dark Skin Tone
👨‍👨‍👦‍👶 Family: Man, Man, Boy, Baby
👨🏼‍❤️‍👩 Couple With Heart - Man: Medium-Light Skin Tone, Woman
👨🏼‍❤️‍👨🏻 Couple With Heart - Man: Medium-Light Skin Tone, Man: Light Skin Tone
👩🏻‍❤️‍💋‍👨🏻 Kiss - Woman: Light Skin Tone, Man: Light Skin Tone
👩‍❤️‍👩🏼 Couple With Heart - Woman, Woman: Medium-Light Skin Tone
👨🏼‍❤️‍👩🏿 Couple With Heart - Man: Medium-Light Skin Tone, Woman: Dark Skin Tone
👨🏻‍❤️‍👨🏾 Couple With Heart - Man: Light Skin Tone, Man: Medium-Dark Skin Tone
👨🏽‍❤️‍👨🏿 Couple With Heart - Man: Medium Skin Tone, Man: Dark Skin Tone
👨🏿‍👦🏿‍👶🏿 Family - Man: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
👩🏻‍❤️‍👩🏿 Couple With Heart - Woman: Light Skin Tone, Woman: Dark Skin Tone
👨🏻‍❤️‍💋‍👨🏽 Kiss - Man: Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁴󠀱󠀲󠁿 Flag for Chukha (BT-12)
👩🏻‍❤️‍👨🏽 Couple With Heart - Woman: Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁴󠀱󠀴󠁿 Flag for Samtse (BT-14)
🏴󠁢󠁴󠀱󠀵󠁿 Flag for Thimphu (BT-15)
👩🏼‍❤️‍👩🏿 Couple With Heart - Woman: Medium-Light Skin Tone, Woman: Dark Skin Tone
🏴󠁢󠁴󠀱󠀱󠁿 Flag for Paro (BT-11)
👨🏻‍❤️‍👩🏾 Couple With Heart - Man: Light Skin Tone, Woman: Medium-Dark Skin Tone
👩🏼‍👨🏼‍👶🏼‍👶🏼 Family - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁢󠁳󠁷󠁧󠁿 Flag for West Grand Bahama (BS-WG)
👨‍❤️‍👩🏿 Couple With Heart - Man, Woman: Dark Skin Tone
👩🏾‍❤️‍👩🏽 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman: Medium Skin Tone
🏴󠁢󠁴󠀱󠀳󠁿 Flag for Haa (BT-13)
🏴󠁣󠁨󠁺󠁨󠁿 Flag for Zürich (CH-ZH)
👨🏽‍👧🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁢󠁴󠀳󠀳󠁿 Flag for Bumthang (BT-33)
🏴󠁢󠁴󠀳󠀲󠁿 Flag for Trongsa (BT-32)
🏴󠁢󠁴󠀴󠀱󠁿 Flag for Trashigang (BT-41)
👨🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁢󠁴󠀲󠀳󠁿 Flag for Punakha (BT-23)
👨🏾‍❤️‍👨🏾 Couple With Heart - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
🏴󠁢󠁴󠀲󠀴󠁿 Flag for Wangdue Phodrang (BT-24)
🏴󠁢󠁴󠀳󠀴󠁿 Flag for Zhemgang (BT-34)
👩🏼‍❤️‍💋‍👨🏼 Kiss - Woman: Medium-Light Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁴󠀴󠀲󠁿 Flag for Mongar (BT-42)
🏴󠁢󠁲󠁰󠁢󠁿 Flag for Paraíba (BR-PB)
👩🏿‍❤️‍👨🏼 Couple With Heart - Woman: Dark Skin Tone, Man: Medium-Light Skin Tone
🏴󠁢󠁳󠁡󠁫󠁿 Flag for Acklins (BS-AK)
🏴󠁢󠁴󠀳󠀱󠁿 Flag for Sarpang (BT-31)
🏴󠁢󠁴󠀲󠀲󠁿 Flag for Dagana (BT-22)
🏴󠁢󠁷󠁦󠁲󠁿 Flag for Francistown (BW-FR)
👩🏻‍❤️‍💋‍👨🏽 Kiss - Woman: Light Skin Tone, Man: Medium Skin Tone
🏴󠁢󠁴󠀴󠀵󠁿 Flag for Samdrup Jongkhar (BT-45)
👨🏿‍👨🏿‍👧🏿‍👧🏿 Family - Man: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁢󠁷󠁣󠁥󠁿 Flag for Central (BW-CE)
🏴󠁢󠁳󠁳󠁳󠁿 Flag for San Salvador (BS-SS)
👩🏿‍❤️‍👩 Couple With Heart - Woman: Dark Skin Tone, Woman
🏴󠁢󠁷󠁣󠁨󠁿 Flag for Chobe (BW-CH)
👩🏿‍👧🏿‍👦🏿 Family - Woman: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁴󠀲󠀱󠁿 Flag for Tsirang (BT-21)
🏴󠁢󠁳󠁳󠁷󠁿 Flag for Spanish Wells (BS-SW)
👨‍❤️‍👩🏾 Couple With Heart - Man, Woman: Medium-Dark Skin Tone
🏴󠁢󠁴󠀴󠀴󠁿 Flag for Lhuntse (BT-44)
🏴󠁢󠁴󠁴󠁹󠁿 Flag for Trashiyangtse (BT-TY)
🏴󠁢󠁴󠀴󠀳󠁿 Flag for Pemagatshel (BT-43)
🏴󠁢󠁴󠁧󠁡󠁿 Flag for Gasa (BT-GA)
🏴󠁢󠁷󠁮󠁥󠁿 Flag for North East (BW-NE)
🏴󠁢󠁷󠁳󠁥󠁿 Flag for South East (BW-SE)
🏴󠁢󠁷󠁪󠁷󠁿 Flag for Jwaneng (BW-JW)
🏴󠁢󠁷󠁫󠁬󠁿 Flag for Kgatleng (BW-KL)
🏴󠁢󠁳󠁭󠁣󠁿 Flag for Mangrove Cay (BS-MC)
🏴󠁢󠁷󠁫󠁧󠁿 Flag for Kgalagadi (BW-KG)
🏴󠁢󠁷󠁫󠁷󠁿 Flag for Kweneng (BW-KW)
🏴󠁢󠁷󠁮󠁷󠁿 Flag for North West (BW-NW)
👨🏿‍👧🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone
👩🏼‍❤️‍💋‍👩🏿 Kiss - Woman: Medium-Light Skin Tone, Woman: Dark Skin Tone
👨🏽‍❤️‍👨 Couple With Heart - Man: Medium Skin Tone, Man
🏴󠁢󠁷󠁧󠁨󠁿 Flag for Ghanzi (BW-GH)
👨🏻‍❤️‍👩🏻 Couple With Heart - Man: Light Skin Tone, Woman: Light Skin Tone
🏴󠁢󠁪󠁡󠁱󠁿 Flag for Atlantique (BJ-AQ)
👨🏻‍👧🏻‍👦🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁢󠁧󠀰󠀴󠁿 Flag for Veliko Tarnovo (BG-04)
👨🏽‍👧🏽‍👦🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Boy: Medium Skin Tone
👨🏾‍👧🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
👨🏿‍👧🏿‍👦🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Boy: Dark Skin Tone
🏴󠁢󠁷󠁳󠁯󠁿 Flag for Southern (BW-SO)
🏴󠁢󠁷󠁳󠁴󠁿 Flag for Sowa Town (BW-ST)
👩🏾‍❤️‍👩 Couple With Heart - Woman: Medium-Dark Skin Tone, Woman
👩🏿‍❤️‍👩🏾 Couple With Heart - Woman: Dark Skin Tone, Woman: Medium-Dark Skin Tone
👨🏽‍❤️‍💋‍👨🏾 Kiss - Man: Medium Skin Tone, Man: Medium-Dark Skin Tone
👨🏻‍👨🏻‍👧🏻‍👦🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Girl: Light Skin Tone, Boy: Light Skin Tone
🏴󠁢󠁷󠁳󠁰󠁿 Flag for Selibe Phikwe (BW-SP)
👨🏼‍❤️‍👨 Couple With Heart - Man: Medium-Light Skin Tone, Man
🏴󠁢󠁳󠁣󠁩󠁿 Flag for Cat Island (BS-CI)
👨‍👩‍👶‍👧 Family: Man, Woman, Baby, Girl
🏴󠁴󠁲󠀳󠀵󠁿 Flag for Izmir (TR-35)
👩🏿‍👨🏿‍👦🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Boy: Dark Skin Tone, Baby: Dark Skin Tone
👨🏻‍👩🏻‍👦🏻 Family - Man: Light Skin Tone, Woman: Light Skin Tone, Boy: Light Skin Tone
🏴󠁢󠁹󠁨󠁯󠁿 Flag for Homel (BY-HO)
👨🏻‍👦🏻‍👦🏻 Family - Man: Light Skin Tone, Boy: Light Skin Tone, Boy: Light Skin Tone
🏴󠁢󠁹󠁨󠁭󠁿 Flag for Minsk (BY-HM)
🏴󠁢󠁹󠁨󠁲󠁿 Flag for Hrodna (BY-HR)
👨🏾‍❤️‍👩🏻 Couple With Heart - Man: Medium-Dark Skin Tone, Woman: Light Skin Tone
🏴󠁢󠁹󠁭󠁡󠁿 Flag for Magileu (BY-MA)
🏴󠁢󠁹󠁭󠁩󠁿 Flag for Minsk Region (BY-MI)
👨🏼‍❤️‍💋‍👩🏿 Kiss - Man: Medium-Light Skin Tone, Woman: Dark Skin Tone
👨🏼‍👧🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👩‍👦‍👧 Family: Woman, Boy, Girl
🏴󠁢󠁷󠁬󠁯󠁿 Flag for Lobatse (BW-LO)
🏴󠁢󠁳󠁭󠁩󠁿 Flag for Moore’s Island (BS-MI)
🏴󠁢󠁹󠁶󠁩󠁿 Flag for Vitebsk (BY-VI)
🏴󠁢󠁪󠁭󠁯󠁿 Flag for Mono (BJ-MO)
🏴󠁧󠁢󠁮󠁩󠁲󠁿 Flag for Northern Ireland (GB-NIR)
👨🏾‍👧🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
️ Variation Selector-16
🏴󠁢󠁳󠁨󠁴󠁿 Flag for Hope Town (BS-HT)
🏴󠁢󠁺󠁳󠁣󠁿 Flag for Stann Creek (BZ-SC)
🏴󠁢󠁺󠁣󠁺󠁬󠁿 Flag for Corozal (BZ-CZL)
👨🏻‍👧🏻‍👶🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone, Baby: Light Skin Tone
🏴󠁢󠁺󠁴󠁯󠁬󠁿 Flag for Toledo (BZ-TOL)
👨‍👩‍👦‍👧 Family: Man, Woman, Boy, Girl
🏴󠁮󠁰󠀵󠁿 Flag for Sudur Pashchimanchal (NP-5)
👨🏼‍👩🏼‍👶🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
👨🏽‍❤️‍💋‍👨🏼 Kiss - Man: Medium Skin Tone, Man: Medium-Light Skin Tone
👨🏻‍👧🏻‍👧🏻 Family - Man: Light Skin Tone, Girl: Light Skin Tone, Girl: Light Skin Tone
👨🏼‍👧🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁬󠁡󠁶󠁩󠁿 Flag for Vientiane Province (LA-VI)
👩🏾‍❤️‍👨🏾 Couple With Heart - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone
👨🏽‍👧🏽‍👶🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁣󠁡󠁯󠁮󠁿 Flag for Ontario (CA-ON)
🏴󠁣󠁤󠁫󠁧󠁿 Flag for Kwango (CD-KG)
👨🏾‍👧🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁣󠁤󠁨󠁵󠁿 Flag for Haut-Uélé (CD-HU)
🏴󠁣󠁤󠁳󠁵󠁿 Flag for Sud-Ubangi (CD-SU)
🏴󠁢󠁳󠁢󠁰󠁿 Flag for Black Point (BS-BP)
🏴󠁣󠁤󠁢󠁣󠁿 Flag for Bas-Congo (CD-BC)
🏴󠁣󠁤󠁭󠁡󠁿 Flag for Maniema (CD-MA)
🏴󠁣󠁤󠁳󠁡󠁿 Flag for Sankuru (CD-SA)
🏴󠁣󠁡󠁰󠁥󠁿 Flag for Prince Edward Island (CA-PE)
🏴󠁣󠁤󠁴󠁵󠁿 Flag for Tshuapa (CD-TU)
🏴󠁣󠁤󠁮󠁫󠁿 Flag for North Kivu (CD-NK)
🏴󠁣󠁤󠁭󠁯󠁿 Flag for Mongala (CD-MO)
🏴󠁣󠁦󠁢󠁢󠁿 Flag for Bamingui-Bangoran (CF-BB)
🏴󠁣󠁦󠁡󠁣󠁿 Flag for Ouham (CF-AC)
🏴󠁣󠁤󠁭󠁮󠁿 Flag for Mai-Ndombe (CD-MN)
🏴󠁢󠁳󠁨󠁩󠁿 Flag for Harbour Island (BS-HI)
👩🏽‍👦🏽‍👦🏽 Family - Woman: Medium Skin Tone, Boy: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁣󠁦󠁢󠁧󠁦󠁿 Flag for Bangui (CF-BGF)
🏴󠁣󠁤󠁫󠁮󠁿 Flag for Kinshasa (CD-KN)
🏴󠁣󠁡󠁹󠁴󠁿 Flag for Yukon (CA-YT)
🏴󠁣󠁤󠁨󠁫󠁿 Flag for Haut-Katanga (CD-HK)
🏴󠁣󠁤󠁴󠁯󠁿 Flag for Tshopo (CD-TO)
🏴󠁣󠁤󠁨󠁬󠁿 Flag for Haut-Lomami (CD-HL)
🏴󠁣󠁤󠁫󠁥󠁿 Flag for Kasaï-Oriental (CD-KE)
🏴󠁣󠁤󠁳󠁫󠁿 Flag for South Kivu (CD-SK)
🏴󠁣󠁦󠁨󠁳󠁿 Flag for Mambéré-Kadéï (CF-HS)
🏴󠁣󠁤󠁫󠁣󠁿 Flag for Kasaï Central (CD-KC)
🏴󠁣󠁤󠁫󠁳󠁿 Flag for Kasaï (CD-KS)
🏴󠁣󠁤󠁩󠁴󠁿 Flag for Ituri (CD-IT)
🏴󠁣󠁨󠁢󠁥󠁿 Flag for Bern (CH-BE)
🏴󠁣󠁧󠀲󠁿 Flag for Lékoumou (CG-2)
🏴󠁣󠁦󠁭󠁰󠁿 Flag for Ombella-M’Poko (CF-MP)
🏴󠁣󠁨󠁧󠁲󠁿 Flag for Graubünden (CH-GR)
🏴󠁣󠁨󠁡󠁧󠁿 Flag for Aargau (CH-AG)
🏴󠁣󠁨󠁮󠁷󠁿 Flag for Nidwalden (CH-NW)
🏴󠁣󠁨󠁡󠁩󠁿 Flag for Appenzell Innerrhoden (CH-AI)
🏴󠁣󠁧󠀱󠀳󠁿 Flag for Sangha (CG-13)
🏴󠁣󠁨󠁳󠁨󠁿 Flag for Schaffhausen (CH-SH)
🏴󠁣󠁤󠁫󠁬󠁿 Flag for Kwilu (CD-KL)
🏴󠁣󠁧󠀵󠁿 Flag for Kouilou (CG-5)
🏴󠁣󠁧󠀷󠁿 Flag for Likouala (CG-7)
🏴󠁣󠁨󠁬󠁵󠁿 Flag for Lucerne (CH-LU)
🏴󠁣󠁨󠁢󠁳󠁿 Flag for Basel-Stadt (CH-BS)
🏴󠁣󠁧󠁢󠁺󠁶󠁿 Flag for Brazzaville (CG-BZV)
🏴󠁣󠁨󠁳󠁧󠁿 Flag for St. Gallen (CH-SG)
🏴󠁣󠁨󠁡󠁲󠁿 Flag for Appenzell Ausserrhoden (CH-AR)
🏴󠁣󠁨󠁳󠁺󠁿 Flag for Schwyz (CH-SZ)
🏴󠁣󠁨󠁦󠁲󠁿 Flag for Fribourg (CH-FR)
🏴󠁣󠁧󠀱󠀴󠁿 Flag for Plateaux (CG-14)
🏴󠁣󠁤󠁬󠁯󠁿 Flag for Lomami (CD-LO)
🏴󠁣󠁦󠁳󠁥󠁿 Flag for Sangha-Mbaéré (CF-SE)
👨🏿‍👧🏿‍👶🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁣󠁨󠁧󠁥󠁿 Flag for Geneva (CH-GE)
🏴󠁣󠁨󠁳󠁯󠁿 Flag for Solothurn (CH-SO)
🏴󠁣󠁧󠀱󠀵󠁿 Flag for Cuvette-Ouest (CG-15)
🏴󠁣󠁧󠀸󠁿 Flag for Cuvette (CG-8)
🏴󠁣󠁨󠁯󠁷󠁿 Flag for Obwalden (CH-OW)
🏴󠁣󠁦󠁫󠁧󠁿 Flag for Kémo (CF-KG)
🏴󠁣󠁨󠁮󠁥󠁿 Flag for Neuchâtel (CH-NE)
🏴󠁣󠁦󠁬󠁢󠁿 Flag for Lobaye (CF-LB)
🏴󠁣󠁬󠁡󠁰󠁿 Flag for Arica y Parinacota (CL-AP)
🏴󠁣󠁭󠁮󠁷󠁿 Flag for Northwest (CM-NW)
🏴󠁣󠁬󠁴󠁡󠁿 Flag for Tarapacá (CL-TA)
🏴󠁣󠁩󠁬󠁧󠁿 Flag for Lagunes (CI-LG)
🏴󠁣󠁬󠁲󠁭󠁿 Flag for Santiago Metropolitan (CL-RM)
👨🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁣󠁮󠀱󠀲󠁿 Flag for Tianjin (CN-12)
🏴󠁣󠁭󠁮󠁯󠁿 Flag for North (CM-NO)
🏴󠁣󠁩󠁤󠁮󠁿 Flag for Denguélé (CI-DN)
🏴󠁣󠁩󠁧󠁤󠁿 Flag for Gôh-Djiboua (CI-GD)
🏴󠁣󠁩󠁣󠁭󠁿 Flag for Comoé (CI-CM)
🏴󠁣󠁩󠁭󠁧󠁿 Flag for Montagnes (CI-MG)
🏴󠁣󠁬󠁭󠁡󠁿 Flag for Magallanes Region (CL-MA)
🏴󠁣󠁬󠁢󠁩󠁿 Flag for Bío Bío (CL-BI)
🏴󠁣󠁬󠁡󠁩󠁿 Flag for Aysén (CL-AI)
🏴󠁣󠁬󠁶󠁳󠁿 Flag for Valparaíso (CL-VS)
🏴󠁣󠁭󠁥󠁳󠁿 Flag for East (CM-ES)
🏴󠁣󠁬󠁡󠁴󠁿 Flag for Atacama (CL-AT)
🏴󠁣󠁩󠁬󠁣󠁿 Flag for Lacs (CI-LC)
🏴󠁣󠁬󠁣󠁯󠁿 Flag for Coquimbo (CL-CO)
🏴󠁣󠁭󠁬󠁴󠁿 Flag for Littoral (CM-LT)
🏴󠁣󠁭󠁣󠁥󠁿 Flag for Centre (CM-CE)
🏴󠁣󠁩󠁢󠁳󠁿 Flag for Bas-Sassandra (CI-BS)
🏴󠁣󠁩󠁹󠁭󠁿 Flag for Yamoussoukro (CI-YM)
🏴󠁣󠁭󠁯󠁵󠁿 Flag for West (CM-OU)
🏴󠁣󠁬󠁬󠁬󠁿 Flag for Los Lagos (CL-LL)
🏴󠁣󠁭󠁡󠁤󠁿 Flag for Adamawa (CM-AD)
🏴󠁣󠁬󠁬󠁲󠁿 Flag for Los Ríos (CL-LR)
🏴󠁣󠁭󠁳󠁷󠁿 Flag for Southwest (CM-SW)
🏴󠁣󠁩󠁳󠁶󠁿 Flag for Savanes (CI-SV)
🏴󠁣󠁩󠁷󠁲󠁿 Flag for Woroba (CI-WR)
🏴󠁣󠁬󠁭󠁬󠁿 Flag for Maule (CL-ML)
🏴󠁣󠁭󠁳󠁵󠁿 Flag for South (CM-SU)
🏴󠁣󠁮󠀵󠀳󠁿 Flag for Yunnan (CN-53)
🏴󠁣󠁮󠀴󠀳󠁿 Flag for Hunan (CN-43)
🏴󠁣󠁮󠀳󠀵󠁿 Flag for Fujian (CN-35)
🏴󠁣󠁮󠀳󠀶󠁿 Flag for Jiangxi (CN-36)
🏴󠁣󠁡󠁮󠁢󠁿 Flag for New Brunswick (CA-NB)
🏴󠁣󠁯󠁢󠁯󠁹󠁿 Flag for Boyacá (CO-BOY)
🏴󠁣󠁮󠀴󠀶󠁿 Flag for Hainan (CN-46)
🏴󠁣󠁮󠀶󠀲󠁿 Flag for Gansu (CN-62)
🏴󠁣󠁮󠀴󠀲󠁿 Flag for Hubei (CN-42)
🏴󠁣󠁮󠀶󠀳󠁿 Flag for Qinghai (CN-63)
🏴󠁣󠁮󠀶󠀵󠁿 Flag for Xinjiang (CN-65)
🏴󠁣󠁮󠀳󠀲󠁿 Flag for Jiangsu (CN-32)
🏴󠁣󠁯󠁣󠁡󠁬󠁿 Flag for Caldas (CO-CAL)
🏴󠁣󠁮󠀴󠀵󠁿 Flag for Guangxi (CN-45)
🏴󠁣󠁯󠁢󠁯󠁬󠁿 Flag for Bolívar (CO-BOL)
🏴󠁣󠁮󠀲󠀳󠁿 Flag for Heilongjiang (CN-23)
🏴󠁣󠁮󠀳󠀷󠁿 Flag for Shandong (CN-37)
🏴󠁣󠁮󠀴󠀱󠁿 Flag for Henan (CN-41)
🏴󠁢󠁧󠀱󠀸󠁿 Flag for Ruse (BG-18)
🏴󠁣󠁮󠀴󠀴󠁿 Flag for Guangdong (CN-44)
🏴󠁣󠁯󠁡󠁴󠁬󠁿 Flag for Atlántico (CO-ATL)
🏴󠁣󠁮󠀵󠀰󠁿 Flag for Chongqing (CN-50)
🏴󠁣󠁯󠁣󠁡󠁱󠁿 Flag for Caquetá (CO-CAQ)
🏴󠁣󠁮󠀱󠀴󠁿 Flag for Shanxi (CN-14)
🏴󠁣󠁦󠁨󠁫󠁿 Flag for Haute-Kotto (CF-HK)
👨🏾‍👩🏾‍👦🏾‍👧🏾 Family - Man: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁣󠁮󠀲󠀲󠁿 Flag for Jilin (CN-22)
🏴󠁣󠁯󠁡󠁲󠁡󠁿 Flag for Arauca (CO-ARA)
🏴󠁣󠁲󠁧󠁿 Flag for Guanacaste (CR-G)
🏴󠁣󠁯󠁣󠁨󠁯󠁿 Flag for Chocó (CO-CHO)
🏴󠁣󠁯󠁧󠁵󠁡󠁿 Flag for Guainía (CO-GUA)
🏴󠁣󠁲󠁬󠁿 Flag for Limón (CR-L)
🏴󠁣󠁯󠁰󠁵󠁴󠁿 Flag for Putumayo (CO-PUT)
🏴󠁣󠁵󠀰󠀵󠁿 Flag for Villa Clara (CU-05)
🏴󠁣󠁯󠁶󠁡󠁣󠁿 Flag for Valle del Cauca (CO-VAC)
🏴󠁣󠁲󠁰󠁿 Flag for Puntarenas (CR-P)
🏴󠁣󠁯󠁲󠁩󠁳󠁿 Flag for Risaralda (CO-RIS)
🏴󠁣󠁯󠁣󠁵󠁮󠁿 Flag for Cundinamarca (CO-CUN)
👨🏽‍👶🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁣󠁲󠁡󠁿 Flag for Alajuela (CR-A)
🏴󠁣󠁯󠁨󠁵󠁩󠁿 Flag for Huila (CO-HUI)
👨🏿‍👧🏿‍👧🏿 Family - Man: Dark Skin Tone, Girl: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁣󠁯󠁶󠁡󠁵󠁿 Flag for Vaupés (CO-VAU)
🏴󠁢󠁺󠁣󠁹󠁿 Flag for Cayo (BZ-CY)
🏴󠁣󠁵󠀰󠀷󠁿 Flag for Sancti Spíritus (CU-07)
🏴󠁣󠁯󠁮󠁳󠁡󠁿 Flag for Norte de Santander (CO-NSA)
🏴󠁣󠁵󠀰󠀴󠁿 Flag for Matanzas (CU-04)
🏴󠁣󠁮󠀵󠀴󠁿 Flag for Tibet (CN-54)
🏴󠁣󠁯󠁣󠁡󠁵󠁿 Flag for Cauca (CO-CAU)
🏴󠁣󠁵󠀰󠀸󠁿 Flag for Ciego de Ávila (CU-08)
🏴󠁣󠁯󠁴󠁯󠁬󠁿 Flag for Tolima (CO-TOL)
🏴󠁣󠁵󠀰󠀹󠁿 Flag for Camagüey (CU-09)
🏴󠁣󠁵󠀰󠀶󠁿 Flag for Cienfuegos (CU-06)
🏴󠁣󠁯󠁧󠁵󠁶󠁿 Flag for Guaviare (CO-GUV)
🏴󠁣󠁯󠁳󠁡󠁮󠁿 Flag for Santander (CO-SAN)
👩🏾‍❤️‍💋‍👨 Kiss - Woman: Medium-Dark Skin Tone, Man
🏴󠁣󠁵󠀰󠀱󠁿 Flag for Pinar del Río (CU-01)
🏴󠁣󠁯󠁭󠁡󠁧󠁿 Flag for Magdalena (CO-MAG)
🏴󠁣󠁲󠁣󠁿 Flag for Cartago (CR-C)
🏴󠁣󠁯󠁣󠁯󠁲󠁿 Flag for Córdoba (CO-COR)
🏴󠁣󠁯󠁬󠁡󠁧󠁿 Flag for La Guajira (CO-LAG)
🏴󠁣󠁵󠀰󠀳󠁿 Flag for Havana (CU-03)
🏴󠁣󠁲󠁳󠁪󠁿 Flag for San José (CR-SJ)
🏴󠁣󠁵󠀱󠀴󠁿 Flag for Guantánamo (CU-14)
🏴󠁣󠁦󠁶󠁫󠁿 Flag for Vakaga (CF-VK)
🏴󠁣󠁺󠀵󠀱󠁿 Flag for Liberecký kraj (CZ-51)
🏴󠁣󠁹󠀰󠀴󠁿 Flag for Famagusta (CY-04)
👨🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁣󠁹󠀰󠀱󠁿 Flag for Nicosia (CY-01)
🏴󠁣󠁺󠀲󠀰󠁿 Flag for Středočeský kraj (CZ-20)
🏴󠁣󠁶󠁢󠁿 Flag for Barlavento Islands (CV-B)
🏴󠁣󠁺󠀵󠀲󠁿 Flag for Královéhradecký kraj (CZ-52)
🏴󠁣󠁺󠀴󠀱󠁿 Flag for Karlovarský kraj (CZ-41)
🏴󠁣󠁵󠀱󠀵󠁿 Flag for Artemisa (CU-15)
🏴󠁤󠁥󠁮󠁩󠁿 Flag for Lower Saxony (DE-NI)
🏴󠁣󠁵󠀱󠀱󠁿 Flag for Holguín (CU-11)
🏴󠁣󠁺󠀸󠀰󠁿 Flag for Moravskoslezský kraj (CZ-80)
🏴󠁤󠁥󠁨󠁨󠁿 Flag for Hamburg (DE-HH)
🏴󠁣󠁺󠀶󠀳󠁿 Flag for Kraj Vysočina (CZ-63)
🏴󠁣󠁵󠀱󠀳󠁿 Flag for Santiago de Cuba (CU-13)
🏴󠁤󠁥󠁢󠁢󠁿 Flag for Brandenburg (DE-BB)
🏴󠁣󠁵󠀱󠀰󠁿 Flag for Las Tunas (CU-10)
🏴󠁣󠁹󠀰󠀲󠁿 Flag for Limassol (CY-02)
🏴󠁣󠁨󠁧󠁬󠁿 Flag for Glarus (CH-GL)
🏴󠁣󠁹󠀰󠀳󠁿 Flag for Larnaca (CY-03)
🏴󠁤󠁥󠁭󠁶󠁿 Flag for Mecklenburg-Vorpommern (DE-MV)
🏴󠁣󠁶󠁳󠁿 Flag for Sotavento Islands (CV-S)
👩🏾‍👨🏾‍👧🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
👨🏿‍👶🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁤󠁥󠁨󠁥󠁿 Flag for Hesse (DE-HE)
🏴󠁣󠁵󠀱󠀶󠁿 Flag for Mayabeque (CU-16)
🏴󠁣󠁺󠀱󠀰󠁿 Flag for Praha, Hlavní mešto (CZ-10)
🏴󠁣󠁺󠀷󠀱󠁿 Flag for Olomoucký kraj (CZ-71)
🏴󠁣󠁺󠀳󠀲󠁿 Flag for Plzeňský kraj (CZ-32)
🏴󠁤󠁪󠁡󠁳󠁿 Flag for Ali Sabieh (DJ-AS)
🏴󠁤󠁫󠀸󠀴󠁿 Flag for Capital Region (DK-84)
🏴󠁣󠁦󠁯󠁰󠁿 Flag for Ouham-Pendé (CF-OP)
🏴󠁤󠁥󠁴󠁨󠁿 Flag for Thuringia (DE-TH)
🏴󠁤󠁫󠀸󠀵󠁿 Flag for Zealand (DK-85)
🏴󠁤󠁺󠀰󠀲󠁿 Flag for Chlef (DZ-02)
🏴󠁤󠁭󠀰󠀴󠁿 Flag for Saint George (DM-04)
🏴󠁤󠁯󠀳󠀳󠁿 Flag for Cibao Nordeste (DO-33)
🏴󠁤󠁭󠀰󠀷󠁿 Flag for Saint Luke (DM-07)
🏴󠁤󠁭󠀱󠀱󠁿 Flag for Saint Peter (DM-11)
🏴󠁤󠁭󠀱󠀰󠁿 Flag for Saint Paul (DM-10)
🏴󠁤󠁪󠁯󠁢󠁿 Flag for Obock (DJ-OB)
🏴󠁤󠁯󠀳󠀶󠁿 Flag for Cibao Sur (DO-36)
🏴󠁤󠁯󠀳󠀸󠁿 Flag for Enriquillo (DO-38)
🏴󠁤󠁥󠁳󠁴󠁿 Flag for Saxony-Anhalt (DE-ST)
🏴󠁤󠁯󠀳󠀴󠁿 Flag for Cibao Noroeste (DO-34)
🏴󠁤󠁯󠀴󠀲󠁿 Flag for Yuma (DO-42)
🏴󠁤󠁭󠀰󠀸󠁿 Flag for Saint Mark (DM-08)
🏴󠁤󠁯󠀳󠀹󠁿 Flag for Higüamo (DO-39)
🏴󠁲󠁵󠁭󠁯󠁳󠁿 Flag for Moscow Province (RU-MOS)
🏴󠁤󠁥󠁳󠁬󠁿 Flag for Saarland (DE-SL)
🏴󠁤󠁭󠀰󠀹󠁿 Flag for Saint Patrick (DM-09)
🏴󠁤󠁭󠀰󠀵󠁿 Flag for Saint John (DM-05)
🏴󠁣󠁮󠀵󠀱󠁿 Flag for Sichuan (CN-51)
🏴󠁤󠁭󠀰󠀲󠁿 Flag for Saint Andrew (DM-02)
🏴󠁤󠁭󠀰󠀳󠁿 Flag for Saint David (DM-03)
🏴󠁤󠁪󠁴󠁡󠁿 Flag for Tadjourah (DJ-TA)
🏴󠁤󠁯󠀴󠀱󠁿 Flag for Valdesia (DO-41)
🏴󠁤󠁺󠀲󠀵󠁿 Flag for Constantine (DZ-25)
🏴󠁤󠁺󠀲󠀲󠁿 Flag for Sidi Bel Abbès (DZ-22)
🏴󠁤󠁺󠀲󠀸󠁿 Flag for M’Sila (DZ-28)
🏴󠁤󠁺󠀳󠀳󠁿 Flag for Illizi (DZ-33)
🏴󠁤󠁺󠀰󠀶󠁿 Flag for Béjaïa (DZ-06)
👩🏿‍👨🏿‍👧🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁤󠁺󠀱󠀴󠁿 Flag for Tiaret (DZ-14)
🏴󠁤󠁺󠀱󠀷󠁿 Flag for Djelfa (DZ-17)
👨🏻‍👶🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone
🏴󠁤󠁺󠀴󠀲󠁿 Flag for Tipasa (DZ-42)
🏴󠁤󠁺󠀰󠀵󠁿 Flag for Batna (DZ-05)
🏴󠁤󠁺󠀱󠀲󠁿 Flag for Tébessa (DZ-12)
🏴󠁤󠁺󠀰󠀷󠁿 Flag for Biskra (DZ-07)
🏴󠁤󠁺󠀰󠀹󠁿 Flag for Blida (DZ-09)
🏴󠁤󠁺󠀳󠀰󠁿 Flag for Ouargla (DZ-30)
🏴󠁤󠁺󠀱󠀵󠁿 Flag for Tizi Ouzou (DZ-15)
🏴󠁤󠁺󠀲󠀶󠁿 Flag for Médéa (DZ-26)
🏴󠁤󠁺󠀰󠀴󠁿 Flag for Oum El Bouaghi (DZ-04)
🏴󠁤󠁺󠀳󠀲󠁿 Flag for El Bayadh (DZ-32)
🏴󠁤󠁺󠀳󠀸󠁿 Flag for Tissemsilt (DZ-38)
🏴󠁤󠁺󠀳󠀹󠁿 Flag for El Oued (DZ-39)
🏴󠁤󠁺󠀲󠀳󠁿 Flag for Annaba (DZ-23)
🏴󠁤󠁺󠀳󠀱󠁿 Flag for Oran (DZ-31)
🏴󠁤󠁺󠀱󠀳󠁿 Flag for Tlemcen (DZ-13)
🏴󠁤󠁺󠀴󠀳󠁿 Flag for Mila (DZ-43)
🏴󠁤󠁺󠀲󠀰󠁿 Flag for Saïda (DZ-20)
🏴󠁤󠁺󠀱󠀰󠁿 Flag for Bouira (DZ-10)
🏴󠁤󠁺󠀰󠀳󠁿 Flag for Laghouat (DZ-03)
🏴󠁤󠁺󠀳󠀶󠁿 Flag for El Tarf (DZ-36)
🏴󠁤󠁺󠀲󠀴󠁿 Flag for Guelma (DZ-24)
🏴󠁤󠁺󠀳󠀵󠁿 Flag for Boumerdès (DZ-35)
🏴󠁤󠁺󠀳󠀷󠁿 Flag for Tindouf (DZ-37)
🏴󠁤󠁺󠀴󠀰󠁿 Flag for Khenchela (DZ-40)
🏴󠁤󠁺󠀴󠀱󠁿 Flag for Souk Ahras (DZ-41)
🏴󠁤󠁺󠀲󠀷󠁿 Flag for Mostaganem (DZ-27)
🏴󠁤󠁺󠀱󠀱󠁿 Flag for Tamanghasset (DZ-11)
🏴󠁥󠁣󠁢󠁿 Flag for Bolívar (EC-B)
🏴󠁤󠁺󠀴󠀵󠁿 Flag for Naama (DZ-45)
🏴󠁤󠁺󠀴󠀷󠁿 Flag for Ghardaïa (DZ-47)
🏴󠁥󠁥󠀷󠀴󠁿 Flag for Saare (EE-74)
🏴󠁥󠁣󠁡󠁿 Flag for Azuay (EC-A)
🏴󠁥󠁣󠁣󠁿 Flag for Carchi (EC-C)
🏴󠁥󠁣󠁵󠁿 Flag for Sucumbíos (EC-U)
🏴󠁣󠁹󠀰󠀵󠁿 Flag for Paphos (CY-05)
🏴󠁤󠁺󠀴󠀸󠁿 Flag for Relizane (DZ-48)
🏴󠁥󠁣󠁳󠁿 Flag for Morona-Santiago (EC-S)
🏴󠁥󠁣󠁧󠁿 Flag for Guayas (EC-G)
🏴󠁥󠁣󠁩󠁿 Flag for Imbabura (EC-I)
🏴󠁥󠁥󠀵󠀷󠁿 Flag for Lääne (EE-57)
👨🏼‍👶🏼‍👦🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Boy: Medium-Light Skin Tone
🏴󠁤󠁺󠀴󠀶󠁿 Flag for Aïn Témouchent (DZ-46)
🏴󠁥󠁣󠁮󠁿 Flag for Napo (EC-N)
👨🏽‍👶🏽‍👦🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁥󠁥󠀶󠀷󠁿 Flag for Pärnu (EE-67)
🏴󠁥󠁥󠀷󠀸󠁿 Flag for Tartu (EE-78)
🏴󠁥󠁣󠁷󠁿 Flag for Galápagos (EC-W)
🏴󠁥󠁣󠁯󠁿 Flag for El Oro (EC-O)
🏴󠁥󠁣󠁰󠁿 Flag for Pichincha (EC-P)
🏴󠁥󠁥󠀷󠀰󠁿 Flag for Rapla (EE-70)
🏴󠁤󠁺󠀴󠀴󠁿 Flag for Aïn Defla (DZ-44)
👨🏾‍👶🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁥󠁥󠀶󠀵󠁿 Flag for Põlva (EE-65)
🏴󠁥󠁣󠁹󠁿 Flag for Pastaza (EC-Y)
🏴󠁥󠁣󠁲󠁿 Flag for Los Ríos (EC-R)
🏴󠁥󠁣󠁬󠁿 Flag for Loja (EC-L)
🏴󠁥󠁥󠀴󠀹󠁿 Flag for Jõgeva (EE-49)
🏴󠁥󠁥󠀸󠀲󠁿 Flag for Valga (EE-82)
🏴󠁥󠁣󠁤󠁿 Flag for Orellana (EC-D)
🏴󠁥󠁣󠁨󠁿 Flag for Chimborazo (EC-H)
🏴󠁥󠁣󠁳󠁥󠁿 Flag for Santa Elena (EC-SE)
🏴󠁥󠁥󠀵󠀱󠁿 Flag for Järva (EE-51)
🏴󠁥󠁳󠁡󠁲󠁿 Flag for Aragon (ES-AR)
🏴󠁥󠁧󠁫󠁮󠁿 Flag for Qena (EG-KN)
🏴󠁥󠁥󠀸󠀴󠁿 Flag for Viljandi (EE-84)
🏴󠁥󠁧󠁩󠁳󠁿 Flag for Ismailia (EG-IS)
🏴󠁥󠁧󠁧󠁨󠁿 Flag for Gharbia (EG-GH)
🏴󠁥󠁧󠁳󠁵󠁺󠁿 Flag for Suez (EG-SUZ)
🏴󠁥󠁧󠁤󠁫󠁿 Flag for Dakahlia (EG-DK)
🏴󠁥󠁧󠁦󠁹󠁭󠁿 Flag for Faiyum (EG-FYM)
🏴󠁥󠁧󠁢󠁨󠁿 Flag for Beheira (EG-BH)
🏴󠁥󠁥󠀸󠀶󠁿 Flag for Võru (EE-86)
🏴󠁥󠁧󠁪󠁳󠁿 Flag for South Sinai (EG-JS)
🏴󠁥󠁧󠁡󠁳󠁴󠁿 Flag for Asyut (EG-AST)
🏴󠁥󠁧󠁫󠁢󠁿 Flag for Qalyubia (EG-KB)
🏴󠁣󠁮󠀳󠀴󠁿 Flag for Anhui (CN-34)
👨🏿‍👶🏿‍👦🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone, Boy: Dark Skin Tone
󠁋 Tag Latin Capital Letter K
🏴󠁥󠁧󠁭󠁴󠁿 Flag for Matrouh (EG-MT)
🏴󠁥󠁲󠁧󠁢󠁿 Flag for Gash-Barka (ER-GB)
🏴󠁥󠁧󠁷󠁡󠁤󠁿 Flag for New Valley (EG-WAD)
🏴󠁥󠁧󠁭󠁮󠁿 Flag for Minya (EG-MN)
🏴󠁥󠁲󠁡󠁮󠁿 Flag for Anseba (ER-AN)
🏴󠁥󠁧󠁬󠁸󠁿 Flag for Luxor (EG-LX)
🏴󠁥󠁧󠁰󠁴󠁳󠁿 Flag for Port Said (EG-PTS)
🏴󠁥󠁲󠁤󠁵󠁿 Flag for Debub (ER-DU)
🏴󠁥󠁲󠁳󠁫󠁿 Flag for Northern Red Sea (ER-SK)
🏴󠁥󠁧󠁳󠁨󠁧󠁿 Flag for Sohag (EG-SHG)
🏴󠁥󠁧󠁡󠁳󠁮󠁿 Flag for Aswan (EG-ASN)
🏴󠁥󠁧󠁭󠁮󠁦󠁿 Flag for Monufia (EG-MNF)
🏴󠁥󠁲󠁭󠁡󠁿 Flag for Maekel (ER-MA)
🏴󠁥󠁧󠁤󠁴󠁿 Flag for Damietta (EG-DT)
🏴󠁥󠁧󠁳󠁨󠁲󠁿 Flag for Al Sharqia (EG-SHR)
🏴󠁥󠁧󠁡󠁬󠁸󠁿 Flag for Alexandria (EG-ALX)
🏴󠁥󠁧󠁫󠁦󠁳󠁿 Flag for Kafr el-Sheikh (EG-KFS)
👨🏼‍👶🏼‍👧🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Girl: Medium-Light Skin Tone
👨🏽‍👶🏽‍👧🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁤󠁺󠀲󠀹󠁿 Flag for Mascara (DZ-29)
🏴󠁣󠁮󠀳󠀳󠁿 Flag for Zhejiang (CN-33)
🏴󠁣󠁮󠀲󠀱󠁿 Flag for Liaoning (CN-21)
🏴󠁥󠁴󠁤󠁤󠁿 Flag for Dire Dawa (ET-DD)
🏴󠁦󠁩󠀱󠀳󠁿 Flag for North Karelia (FI-13)
🏴󠁥󠁳󠁭󠁬󠁿 Flag for Melilla (ES-ML)
🏴󠁥󠁴󠁴󠁩󠁿 Flag for Tigray (ET-TI)
🏴󠁥󠁴󠁡󠁭󠁿 Flag for Amhara (ET-AM)
🏴󠁥󠁳󠁭󠁣󠁿 Flag for Murcia Region (ES-MC)
🏴󠁥󠁴󠁢󠁥󠁿 Flag for Benishangul-Gumuz (ET-BE)
🏴󠁥󠁴󠁧󠁡󠁿 Flag for Gambela (ET-GA)
🏴󠁣󠁺󠀷󠀲󠁿 Flag for Zlínský kraj (CZ-72)
👨🏻‍👶🏻‍👧🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone, Girl: Light Skin Tone
👩🏾‍👧🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁦󠁩󠀰󠀵󠁿 Flag for Kainuu (FI-05)
🏴󠁦󠁩󠀰󠀳󠁿 Flag for Southern Ostrobothnia (FI-03)
🏴󠁥󠁴󠁨󠁡󠁿 Flag for Harari (ET-HA)
🏴󠁦󠁩󠀰󠀷󠁿 Flag for Central Ostrobothnia (FI-07)
🏴󠁦󠁩󠀰󠀹󠁿 Flag for Kymenlaakso (FI-09)
🏴󠁦󠁩󠀰󠀴󠁿 Flag for Southern Savonia (FI-04)
🏴󠁥󠁴󠁯󠁲󠁿 Flag for Oromia (ET-OR)
🏴󠁢󠁺󠁢󠁺󠁿 Flag for Belize (BZ-BZ)
🏴󠁥󠁳󠁲󠁩󠁿 Flag for La Rioja (ES-RI)
🏴󠁦󠁩󠀰󠀲󠁿 Flag for South Karelia (FI-02)
🏴󠁦󠁲󠁮󠁡󠁱󠁿 Flag for Nouvelle-Aquitaine (FR-NAQ)
🏴󠁦󠁲󠁣󠁰󠁿 Flag for Clipperton Island (FR-CP)
🏴󠁦󠁲󠁣󠁶󠁬󠁿 Flag for Centre-Val de Loire (FR-CVL)
🏴󠁦󠁲󠁰󠁦󠁿 Flag for French Polynesia (FR-PF)
👨🏼‍👩🏼‍👶🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Woman: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁦󠁩󠀱󠀶󠁿 Flag for Päijänne Tavastia (FI-16)
🏴󠁥󠁴󠁳󠁯󠁿 Flag for Somali (ET-SO)
🏴󠁦󠁲󠁬󠁲󠁥󠁿 Flag for La Réunion (FR-LRE)
🏴󠁦󠁲󠁭󠁦󠁿 Flag for St. Martin (FR-MF)
🏴󠁦󠁲󠁧󠁥󠁳󠁿 Flag for Grand-Est (FR-GES)
🏴󠁦󠁪󠁲󠁿 Flag for Rotuma (FJ-R)
🏴󠁦󠁲󠁢󠁦󠁣󠁿 Flag for Bourgogne-Franche-Comté (FR-BFC)
🏴󠁦󠁩󠀱󠀴󠁿 Flag for Northern Ostrobothnia (FI-14)
🏴󠁦󠁲󠁮󠁯󠁲󠁿 Flag for Normandie (FR-NOR)
🏴󠁦󠁲󠁧󠁦󠁿 Flag for French Guiana (FR-GF)
🏴󠁦󠁲󠁮󠁣󠁿 Flag for New Caledonia (FR-NC)
🏴󠁦󠁪󠁮󠁿 Flag for Northern (FJ-N)
🏴󠁦󠁩󠀱󠀷󠁿 Flag for Satakunta (FI-17)
🏴󠁦󠁩󠀱󠀱󠁿 Flag for Pirkanmaa (FI-11)
🏴󠁦󠁲󠁧󠁵󠁡󠁿 Flag for Guadeloupe (FR-GUA)
🏴󠁦󠁭󠁹󠁡󠁰󠁿 Flag for Yap (FM-YAP)
🏴󠁦󠁭󠁫󠁳󠁡󠁿 Flag for Kosrae (FM-KSA)
🏴󠁦󠁲󠁭󠁡󠁹󠁿 Flag for Mayotte (FR-MAY)
🏴󠁦󠁭󠁴󠁲󠁫󠁿 Flag for Chuuk (FM-TRK)
🏴󠁦󠁪󠁣󠁿 Flag for Central (FJ-C)
🏴󠁦󠁩󠀱󠀵󠁿 Flag for Northern Savonia (FI-15)
🏴󠁦󠁲󠁯󠁣󠁣󠁿 Flag for Occitanie (FR-OCC)
🏴󠁧󠁥󠁴󠁢󠁿 Flag for Tbilisi (GE-TB)
🏴󠁧󠁨󠁢󠁡󠁿 Flag for Brong-Ahafo (GH-BA)
🏴󠁧󠁡󠀹󠁿 Flag for Woleu-Ntem (GA-9)
🏴󠁧󠁡󠀸󠁿 Flag for Ogooué-Maritime (GA-8)
👨🏿‍👶🏿‍👧🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁧󠁥󠁳󠁪󠁿 Flag for Samtskhe-Javakheti (GE-SJ)
🏴󠁧󠁡󠀶󠁿 Flag for Ogooué-Ivindo (GA-6)
🏴󠁦󠁲󠁢󠁲󠁥󠁿 Flag for Bretagne (FR-BRE)
🏴󠁧󠁥󠁩󠁭󠁿 Flag for Imereti (GE-IM)
🏴󠁧󠁡󠀳󠁿 Flag for Moyen-Ogooué (GA-3)
👨🏻‍👶🏻‍👶🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone, Baby: Light Skin Tone
🏴󠁧󠁤󠀰󠀴󠁿 Flag for Saint John (GD-04)
🏴󠁧󠁥󠁳󠁫󠁿 Flag for Shida Kartli (GE-SK)
🏴󠁧󠁡󠀵󠁿 Flag for Nyanga (GA-5)
👨🏼‍👶🏼‍👶🏼 Family - Man: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone, Baby: Medium-Light Skin Tone
🏴󠁣󠁺󠀶󠀴󠁿 Flag for Jihomoravský kraj (CZ-64)
🏴󠁧󠁤󠀰󠀶󠁿 Flag for Saint Patrick (GD-06)
🏴󠁧󠁤󠀰󠀲󠁿 Flag for Saint David (GD-02)
🏴󠁧󠁤󠀰󠀱󠁿 Flag for Saint Andrew (GD-01)
🏴󠁧󠁨󠁡󠁡󠁿 Flag for Greater Accra (GH-AA)
🏴󠁦󠁲󠁷󠁦󠁿 Flag for Wallis & Futuna (FR-WF)
🏴󠁧󠁡󠀲󠁿 Flag for Haut-Ogooué (GA-2)
🏴󠁧󠁥󠁲󠁬󠁿 Flag for Racha-Lechkhumi and Kvemo Svaneti (GE-RL)
🏴󠁧󠁥󠁭󠁭󠁿 Flag for Mtskheta-Mtianeti (GE-MM)
🏴󠁦󠁲󠁰󠁭󠁿 Flag for St. Pierre & Miquelon (FR-PM)
🏴󠁧󠁡󠀷󠁿 Flag for Ogooué-Lolo (GA-7)
🏴󠁧󠁥󠁧󠁵󠁿 Flag for Guria (GE-GU)
🏴󠁧󠁥󠁳󠁺󠁿 Flag for Samegrelo-Zemo Svaneti (GE-SZ)
🏴󠁧󠁮󠁤󠁿 Flag for Kindia Region (GN-D)
👨🏽‍👶🏽‍👶🏽 Family - Man: Medium Skin Tone, Baby: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁧󠁬󠁱󠁡󠁿 Flag for Qaasuitsup (GL-QA)
🏴󠁧󠁲󠁥󠁿 Flag for Thessaly (GR-E)
🏴󠁧󠁬󠁳󠁭󠁿 Flag for Sermersooq (GL-SM)
🏴󠁧󠁨󠁮󠁰󠁿 Flag for Northern (GH-NP)
🏴󠁧󠁮󠁮󠁿 Flag for Nzérékoré Region (GN-N)
🏴󠁧󠁨󠁣󠁰󠁿 Flag for Central (GH-CP)
🏴󠁧󠁲󠁢󠁿 Flag for Central Macedonia (GR-B)
🏴󠁧󠁮󠁫󠁿 Flag for Kankan Region (GN-K)
🏴󠁧󠁮󠁣󠁿 Flag for Conakry (GN-C)
🏴󠁧󠁭󠁷󠁿 Flag for West Coast Division (GM-W)
🏴󠁧󠁭󠁵󠁿 Flag for Upper River Division (GM-U)
🏴󠁧󠁨󠁥󠁰󠁿 Flag for Eastern (GH-EP)
🏴󠁧󠁨󠁴󠁶󠁿 Flag for Volta (GH-TV)
🏴󠁧󠁨󠁷󠁰󠁿 Flag for Western (GH-WP)
🏴󠁧󠁮󠁭󠁿 Flag for Mamou Region (GN-M)
🏴󠁧󠁲󠁩󠁿 Flag for Attica (GR-I)
🏴󠁧󠁲󠁤󠁿 Flag for Epirus (GR-D)
🏴󠁧󠁮󠁬󠁿 Flag for Labé Region (GN-L)
🏴󠁧󠁱󠁣󠁿 Flag for Río Muni (GQ-C)
🏴󠁧󠁭󠁬󠁿 Flag for Lower River Division (GM-L)
🏴󠁧󠁲󠁦󠁿 Flag for Ionian Islands (GR-F)
🏴󠁧󠁲󠁣󠁿 Flag for West Macedonia (GR-C)
🏴󠁧󠁨󠁡󠁨󠁿 Flag for Ashanti (GH-AH)
🏴󠁧󠁨󠁵󠁷󠁿 Flag for Upper West (GH-UW)
🏴󠁧󠁭󠁭󠁿 Flag for Central River Division (GM-M)
🏴󠁧󠁲󠀶󠀹󠁿 Flag for Mount Athos (GR-69)
🏴󠁧󠁮󠁢󠁿 Flag for Boké Region (GN-B)
🏴󠁧󠁬󠁱󠁥󠁿 Flag for Qeqqata (GL-QE)
🏴󠁧󠁭󠁮󠁿 Flag for North Bank Division (GM-N)
🏴󠁧󠁲󠁨󠁿 Flag for Central Greece (GR-H)
🏴󠁧󠁬󠁫󠁵󠁿 Flag for Kujalleq (GL-KU)
🏴󠁧󠁱󠁩󠁿 Flag for Insular (GQ-I)
🏴󠁧󠁭󠁢󠁿 Flag for Banjul (GM-B)
🏴󠁧󠁲󠁬󠁿 Flag for South Aegean (GR-L)
🏴󠁧󠁨󠁵󠁥󠁿 Flag for Upper East (GH-UE)
🏴󠁧󠁮󠁦󠁿 Flag for Faranah Region (GN-F)
🏴󠁧󠁹󠁰󠁭󠁿 Flag for Pomeroon-Supenaam (GY-PM)
🏴󠁨󠁮󠁡󠁴󠁿 Flag for Atlántida (HN-AT)
👨🏾‍👶🏾‍👶🏾 Family - Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁧󠁹󠁣󠁵󠁿 Flag for Cuyuni-Mazaruni (GY-CU)
🏴󠁧󠁹󠁤󠁥󠁿 Flag for Demerara-Mahaica (GY-DE)
🏴󠁧󠁷󠁮󠁿 Flag for Norte (GW-N)
🏴󠁧󠁴󠁳󠁵󠁿 Flag for Suchitepéquez (GT-SU)
🏴󠁧󠁷󠁳󠁿 Flag for Sul (GW-S)
🏴󠁧󠁴󠁱󠁣󠁿 Flag for Quiché (GT-QC)
🏴󠁧󠁴󠁩󠁺󠁿 Flag for Izabal (GT-IZ)
🏴󠁧󠁹󠁰󠁴󠁿 Flag for Potaro-Siparuni (GY-PT)
🏴󠁧󠁴󠁨󠁵󠁿 Flag for Huehuetenango (GT-HU)
🏴󠁧󠁴󠁱󠁺󠁿 Flag for Quetzaltenango (GT-QZ)
🏴󠁧󠁴󠁣󠁭󠁿 Flag for Chimaltenango (GT-CM)
🏴󠁧󠁴󠁡󠁶󠁿 Flag for Alta Verapaz (GT-AV)
🏴󠁧󠁴󠁴󠁯󠁿 Flag for Totonicapán (GT-TO)
🏴󠁧󠁹󠁢󠁡󠁿 Flag for Barima-Waini (GY-BA)
🏴󠁧󠁹󠁥󠁳󠁿 Flag for Essequibo Islands-West Demerara (GY-ES)
👨🏿‍👶🏿‍👶🏿 Family - Man: Dark Skin Tone, Baby: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁧󠁷󠁢󠁳󠁿 Flag for Bissau (GW-BS)
🏴󠁧󠁴󠁰󠁲󠁿 Flag for El Progreso (GT-PR)
🏴󠁧󠁴󠁳󠁡󠁿 Flag for Sacatepéquez (GT-SA)
🏴󠁧󠁴󠁪󠁵󠁿 Flag for Jutiapa (GT-JU)
🏴󠁨󠁮󠁣󠁨󠁿 Flag for Choluteca (HN-CH)
🏴󠁧󠁴󠁣󠁱󠁿 Flag for Chiquimula (GT-CQ)
🏴󠁧󠁴󠁰󠁥󠁿 Flag for Petén (GT-PE)
🏴󠁧󠁴󠁢󠁶󠁿 Flag for Baja Verapaz (GT-BV)
🏴󠁧󠁴󠁥󠁳󠁿 Flag for Escuintla (GT-ES)
🏴󠁧󠁴󠁺󠁡󠁿 Flag for Zacapa (GT-ZA)
🏴󠁥󠁴󠁡󠁡󠁿 Flag for Addis Ababa (ET-AA)
🏴󠁧󠁷󠁬󠁿 Flag for Leste (GW-L)
🏴󠁧󠁴󠁪󠁡󠁿 Flag for Jalapa (GT-JA)
🏴󠁧󠁴󠁳󠁯󠁿 Flag for Sololá (GT-SO)
🏴󠁨󠁮󠁣󠁭󠁿 Flag for Comayagua (HN-CM)
🏴󠁨󠁲󠀰󠀶󠁿 Flag for Koprivnica-Križevci (HR-06)
🏴󠁨󠁲󠀰󠀷󠁿 Flag for Bjelovar-Bilogora (HR-07)
🏴󠁨󠁮󠁹󠁯󠁿 Flag for Yoro (HN-YO)
🏴󠁨󠁲󠀰󠀹󠁿 Flag for Lika-Senj (HR-09)
🏴󠁨󠁮󠁣󠁬󠁿 Flag for Colón (HN-CL)
🏴󠁨󠁮󠁧󠁤󠁿 Flag for Gracias a Dios (HN-GD)
🏴󠁨󠁮󠁩󠁮󠁿 Flag for Intibucá (HN-IN)
🏴󠁨󠁲󠀰󠀱󠁿 Flag for Zagreb County (HR-01)
🏴󠁥󠁥󠀴󠀴󠁿 Flag for Ida-Viru (EE-44)
🏴󠁨󠁴󠁣󠁥󠁿 Flag for Centre (HT-CE)
🏴󠁨󠁲󠀱󠀶󠁿 Flag for Vukovar-Syrmia (HR-16)
🏴󠁨󠁲󠀰󠀸󠁿 Flag for Primorje-Gorski Kotar (HR-08)
🏴󠁨󠁮󠁬󠁥󠁿 Flag for Lempira (HN-LE)
🏴󠁨󠁲󠀱󠀴󠁿 Flag for Osijek-Baranja (HR-14)
🏴󠁨󠁲󠀱󠀲󠁿 Flag for Brod-Posavina (HR-12)
🏴󠁨󠁲󠀱󠀷󠁿 Flag for Split-Dalmatia (HR-17)
🏴󠁨󠁲󠀱󠀸󠁿 Flag for Istria (HR-18)
🏴󠁨󠁮󠁯󠁬󠁿 Flag for Olancho (HN-OL)
🏴󠁨󠁲󠀱󠀹󠁿 Flag for Dubrovnik-Neretva (HR-19)
🏴󠁨󠁮󠁬󠁰󠁿 Flag for La Paz (HN-LP)
🏴󠁨󠁮󠁥󠁰󠁿 Flag for El Paraíso (HN-EP)
🏴󠁨󠁲󠀲󠀱󠁿 Flag for Zagreb (HR-21)
🏴󠁨󠁲󠀱󠀵󠁿 Flag for Šibenik-Knin (HR-15)
🏴󠁨󠁮󠁦󠁭󠁿 Flag for Francisco Morazán (HN-FM)
🏴󠁨󠁮󠁩󠁢󠁿 Flag for Bay Islands (HN-IB)
🏴󠁨󠁲󠀰󠀳󠁿 Flag for Sisak-Moslavina (HR-03)
🏴󠁨󠁲󠀱󠀳󠁿 Flag for Zadar (HR-13)
🏴󠁤󠁺󠀱󠀸󠁿 Flag for Jijel (DZ-18)
🏴󠁨󠁲󠀰󠀲󠁿 Flag for Krapina-Zagorje (HR-02)
🏴󠁨󠁮󠁣󠁲󠁿 Flag for Cortés (HN-CR)
🏴󠁨󠁴󠁡󠁲󠁿 Flag for Artibonite (HT-AR)
🏴󠁨󠁲󠀲󠀰󠁿 Flag for Međimurje (HR-20)
🏴󠁨󠁮󠁶󠁡󠁿 Flag for Valle (HN-VA)
🏴󠁨󠁮󠁳󠁢󠁿 Flag for Santa Bárbara (HN-SB)
🏴󠁨󠁲󠀱󠀱󠁿 Flag for Požega-Slavonia (HR-11)
🏴󠁨󠁮󠁣󠁰󠁿 Flag for Copán (HN-CP)
🏴󠁨󠁮󠁯󠁣󠁿 Flag for Ocotepeque (HN-OC)
🏴󠁨󠁵󠁨󠁶󠁿 Flag for Hódmezővásárhely (HU-HV)
🏴󠁨󠁵󠁢󠁫󠁿 Flag for Bács-Kiskun (HU-BK)
🏴󠁨󠁵󠁰󠁳󠁿 Flag for Pécs (HU-PS)
🏴󠁨󠁴󠁮󠁤󠁿 Flag for Nord (HT-ND)
🏴󠁨󠁵󠁦󠁥󠁿 Flag for Fejér (HU-FE)
🏴󠁨󠁵󠁳󠁨󠁿 Flag for Szombathely (HU-SH)
🏴󠁨󠁵󠁢󠁡󠁿 Flag for Baranya (HU-BA)
🏴󠁨󠁵󠁢󠁺󠁿 Flag for Borsod-Abaúj-Zemplén (HU-BZ)
🏴󠁨󠁵󠁣󠁳󠁿 Flag for Csongrád (HU-CS)
🏴󠁨󠁵󠁳󠁮󠁿 Flag for Sopron (HU-SN)
🏴󠁨󠁵󠁤󠁵󠁿 Flag for Dunaújváros (HU-DU)
🏴󠁨󠁵󠁮󠁹󠁿 Flag for Nyíregyháza (HU-NY)
🏴󠁨󠁴󠁯󠁵󠁿 Flag for Ouest (HT-OU)
🏴󠁨󠁵󠁳󠁤󠁿 Flag for Szeged (HU-SD)
🏴󠁨󠁵󠁢󠁵󠁿 Flag for Budapest (HU-BU)
🏴󠁨󠁵󠁫󠁥󠁿 Flag for Komárom-Esztergom (HU-KE)
🏴󠁨󠁵󠁳󠁦󠁿 Flag for Székesfehérvár (HU-SF)
🏴󠁨󠁵󠁮󠁫󠁿 Flag for Nagykanizsa (HU-NK)
🏴󠁨󠁴󠁧󠁡󠁿 Flag for Grand’Anse (HT-GA)
🏴󠁨󠁵󠁢󠁣󠁿 Flag for Békéscsaba (HU-BC)
🏴󠁨󠁴󠁳󠁤󠁿 Flag for Sud (HT-SD)
🏴󠁨󠁴󠁮󠁯󠁿 Flag for Nord-Ouest (HT-NO)
🏴󠁨󠁵󠁫󠁭󠁿 Flag for Kecskemét (HU-KM)
🏴󠁨󠁵󠁭󠁩󠁿 Flag for Miskolc (HU-MI)
🏴󠁨󠁵󠁥󠁲󠁿 Flag for Érd (HU-ER)
🏴󠁨󠁵󠁤󠁥󠁿 Flag for Debrecen (HU-DE)
🏴󠁨󠁴󠁮󠁩󠁿 Flag for Nippes (HT-NI)
🏴󠁨󠁵󠁳󠁫󠁿 Flag for Szolnok (HU-SK)
🏴󠁨󠁵󠁫󠁶󠁿 Flag for Kaposvár (HU-KV)
🏴󠁨󠁴󠁳󠁥󠁿 Flag for Sud-Est (HT-SE)
🏴󠁨󠁵󠁪󠁮󠁿 Flag for Jász-Nagykun-Szolnok (HU-JN)
🏴󠁨󠁵󠁨󠁢󠁿 Flag for Hajdú-Bihar (HU-HB)
🏴󠁨󠁵󠁨󠁥󠁿 Flag for Heves (HU-HE)
🏴󠁨󠁵󠁢󠁥󠁿 Flag for Békés (HU-BE)
🏴󠁨󠁵󠁮󠁯󠁿 Flag for Nógrád (HU-NO)
🏴󠁨󠁵󠁧󠁹󠁿 Flag for Győr (HU-GY)
🏴󠁨󠁵󠁰󠁥󠁿 Flag for Pest (HU-PE)
🏴󠁩󠁮󠁣󠁴󠁿 Flag for Chhattisgarh (IN-CT)
🏴󠁨󠁵󠁴󠁢󠁿 Flag for Tatabánya (HU-TB)
🏴󠁩󠁥󠁣󠁿 Flag for Connacht (IE-C)
🏴󠁩󠁬󠁴󠁡󠁿 Flag for Tel Aviv District (IL-TA)
🏴󠁩󠁤󠁳󠁬󠁿 Flag for Sulawesi (ID-SL)
🏴󠁩󠁥󠁵󠁿 Flag for Ulster (IE-U)
🏴󠁩󠁮󠁡󠁰󠁿 Flag for Andhra Pradesh (IN-AP)
🏴󠁨󠁵󠁶󠁥󠁿 Flag for Veszprém County (HU-VE)
🏴󠁩󠁮󠁢󠁲󠁿 Flag for Bihar (IN-BR)
🏴󠁨󠁵󠁳󠁯󠁿 Flag for Somogy (HU-SO)
🏴󠁩󠁮󠁤󠁮󠁿 Flag for Dadra and Nagar Haveli (IN-DN)
🏴󠁩󠁮󠁧󠁪󠁿 Flag for Gujarat (IN-GJ)
🏴󠁨󠁵󠁶󠁭󠁿 Flag for Veszprém (HU-VM)
🏴󠁨󠁵󠁳󠁴󠁿 Flag for Salgótarján (HU-ST)
🏴󠁩󠁬󠁺󠁿 Flag for Northern District (IL-Z)
🏴󠁩󠁤󠁫󠁡󠁿 Flag for Kalimantan (ID-KA)
🏴󠁩󠁬󠁪󠁭󠁿 Flag for Jerusalem (IL-JM)
🏴󠁩󠁮󠁡󠁮󠁿 Flag for Andaman and Nicobar Islands (IN-AN)
🏴󠁩󠁤󠁪󠁷󠁿 Flag for Java (ID-JW)
🏴󠁩󠁬󠁨󠁡󠁿 Flag for Haifa District (IL-HA)
🏴󠁩󠁮󠁧󠁡󠁿 Flag for Goa (IN-GA)
󠁈 Tag Latin Capital Letter H
🏴󠁩󠁤󠁰󠁰󠁿 Flag for Papua Islands (ID-PP)
🏴󠁨󠁵󠁺󠁥󠁿 Flag for Zalaegerszeg (HU-ZE)
🏴󠁩󠁮󠁡󠁲󠁿 Flag for Arunachal Pradesh (IN-AR)
🏴󠁨󠁵󠁳󠁳󠁿 Flag for Szekszárd (HU-SS)
🏴󠁩󠁥󠁬󠁿 Flag for Leinster (IE-L)
🏴󠁩󠁤󠁳󠁭󠁿 Flag for Sumatra (ID-SM)
🏴󠁨󠁵󠁴󠁯󠁿 Flag for Tolna (HU-TO)
🏴󠁩󠁬󠁭󠁿 Flag for Central District (IL-M)
🏴󠁩󠁬󠁤󠁿 Flag for Southern District (IL-D)
🏴󠁩󠁮󠁣󠁨󠁿 Flag for Chandigarh (IN-CH)
🏴󠁩󠁮󠁤󠁤󠁿 Flag for Daman and Diu (IN-DD)
🏴󠁩󠁤󠁮󠁵󠁿 Flag for Lesser Sunda Islands (ID-NU)
🏴󠁨󠁵󠁶󠁡󠁿 Flag for Vas (HU-VA)
🏴󠁩󠁮󠁤󠁬󠁿 Flag for Delhi (IN-DL)
🏴󠁩󠁱󠁳󠁵󠁿 Flag for Sulaymaniyah (IQ-SU)
🏴󠁩󠁮󠁴󠁲󠁿 Flag for Tripura (IN-TR)
🏴󠁩󠁮󠁵󠁰󠁿 Flag for Uttar Pradesh (IN-UP)
🏴󠁩󠁮󠁷󠁢󠁿 Flag for West Bengal (IN-WB)
🏴󠁩󠁮󠁵󠁴󠁿 Flag for Uttarakhand (IN-UT)
󠁕 Tag Latin Capital Letter U
🏴󠁩󠁱󠁢󠁡󠁿 Flag for Basra (IQ-BA)
🏴󠁩󠁮󠁫󠁬󠁿 Flag for Kerala (IN-KL)
🏴󠁩󠁮󠁰󠁹󠁿 Flag for Puducherry (IN-PY)
🏴󠁩󠁱󠁳󠁤󠁿 Flag for Saladin (IQ-SD)
🏴󠁩󠁮󠁭󠁺󠁿 Flag for Mizoram (IN-MZ)
🏴󠁩󠁮󠁮󠁬󠁿 Flag for Nagaland (IN-NL)
🏴󠁩󠁱󠁭󠁡󠁿 Flag for Maysan (IQ-MA)
🏴󠁩󠁱󠁱󠁡󠁿 Flag for Al-Qādisiyyah (IQ-QA)
🏴󠁩󠁱󠁤󠁩󠁿 Flag for Diyala (IQ-DI)
🏴󠁩󠁮󠁴󠁧󠁿 Flag for Telangana (IN-TG)
🏴󠁩󠁮󠁯󠁲󠁿 Flag for Odisha (IN-OR)
🏴󠁩󠁱󠁤󠁱󠁿 Flag for Dhi Qar (IQ-DQ)
🏴󠁩󠁱󠁡󠁮󠁿 Flag for Al Anbar (IQ-AN)
🏴󠁩󠁱󠁤󠁡󠁿 Flag for Dohuk (IQ-DA)
🏴󠁩󠁱󠁮󠁡󠁿 Flag for Najaf (IQ-NA)
🏴󠁩󠁮󠁭󠁨󠁿 Flag for Maharashtra (IN-MH)
🏴󠁩󠁱󠁭󠁵󠁿 Flag for Al Muthanna (IQ-MU)
🏴󠁩󠁱󠁮󠁩󠁿 Flag for Nineveh (IQ-NI)
🏴󠁩󠁱󠁢󠁧󠁿 Flag for Baghdad (IQ-BG)
🏴󠁩󠁮󠁰󠁢󠁿 Flag for Punjab (IN-PB)
🏴󠁩󠁱󠁫󠁡󠁿 Flag for Karbala (IQ-KA)
🏴󠁩󠁮󠁬󠁤󠁿 Flag for Lakshadweep (IN-LD)
🏴󠁩󠁮󠁭󠁰󠁿 Flag for Madhya Pradesh (IN-MP)
🏴󠁩󠁱󠁡󠁲󠁿 Flag for Erbil (IQ-AR)
🏴󠁩󠁮󠁪󠁨󠁿 Flag for Jharkhand (IN-JH)
🏴󠁩󠁮󠁳󠁫󠁿 Flag for Sikkim (IN-SK)
🏴󠁩󠁮󠁭󠁬󠁿 Flag for Meghalaya (IN-ML)
🏴󠁩󠁮󠁨󠁲󠁿 Flag for Haryana (IN-HR)
🏴󠁩󠁲󠀱󠀱󠁿 Flag for Zanjan (IR-11)
👨🏾‍👨🏾‍👦🏾 Family - Man: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁩󠁲󠀱󠀰󠁿 Flag for Khuzestan (IR-10)
🏴󠁩󠁲󠀲󠀸󠁿 Flag for Qazvin (IR-28)
🏴󠁥󠁧󠁣󠁿 Flag for Cairo (EG-C)
🏴󠁩󠁲󠀰󠀸󠁿 Flag for Chaharmahal and Bakhtiari (IR-08)
🏴󠁩󠁳󠀲󠁿 Flag for Southern Peninsula (IS-2)
🏴󠁩󠁲󠀲󠀹󠁿 Flag for South Khorasan (IR-29)
🏴󠁩󠁲󠀱󠀲󠁿 Flag for Semnan (IR-12)
🏴󠁨󠁵󠁺󠁡󠁿 Flag for Zala (HU-ZA)
🏴󠁩󠁲󠀲󠀳󠁿 Flag for Hormozgan (IR-23)
🏴󠁧󠁹󠁭󠁡󠁿 Flag for Mahaica-Berbice (GY-MA)
🏴󠁩󠁲󠀲󠀵󠁿 Flag for Yazd (IR-25)
🏴󠁩󠁲󠀱󠀷󠁿 Flag for Kermanshah (IR-17)
🏴󠁩󠁲󠀰󠀴󠁿 Flag for Isfahan (IR-04)
🏴󠁩󠁳󠀳󠁿 Flag for Western (IS-3)
🏴󠁩󠁲󠀲󠀶󠁿 Flag for Qom (IR-26)
🏴󠁩󠁲󠀲󠀲󠁿 Flag for Markazi (IR-22)
🏴󠁩󠁲󠀳󠀱󠁿 Flag for North Khorasan (IR-31)
🏴󠁩󠁲󠀰󠀶󠁿 Flag for Bushehr (IR-06)
🏴󠁩󠁲󠀲󠀰󠁿 Flag for Lorestan (IR-20)
🏴󠁩󠁴󠀲󠀱󠁿 Flag for Piedmont (IT-21)
🏴󠁩󠁲󠀰󠀵󠁿 Flag for Ilam (IR-05)
🏴󠁥󠁳󠁥󠁸󠁿 Flag for Extremadura (ES-EX)
🏴󠁩󠁳󠀵󠁿 Flag for Northwestern (IS-5)
🏴󠁩󠁱󠁷󠁡󠁿 Flag for Wasit (IQ-WA)
🏴󠁩󠁳󠀶󠁿 Flag for Northeastern (IS-6)
🏴󠁩󠁳󠀷󠁿 Flag for Eastern (IS-7)
🏴󠁥󠁳󠁣󠁮󠁿 Flag for Canary Islands (ES-CN)
🏴󠁩󠁲󠀱󠀵󠁿 Flag for Kerman (IR-15)
🏴󠁩󠁲󠀱󠀹󠁿 Flag for Gilan (IR-19)
🏴󠁩󠁳󠀱󠁿 Flag for Capital (IS-1)
🏴󠁪󠁯󠁪󠁡󠁿 Flag for Jerash (JO-JA)
🏴󠁩󠁴󠀵󠀲󠁿 Flag for Tuscany (IT-52)
🏴󠁪󠁯󠁩󠁲󠁿 Flag for Irbid (JO-IR)
🏴󠁩󠁴󠀶󠀵󠁿 Flag for Abruzzo (IT-65)
🏴󠁩󠁴󠀶󠀷󠁿 Flag for Molise (IT-67)
🏴󠁩󠁴󠀷󠀷󠁿 Flag for Basilicata (IT-77)
🏴󠁩󠁴󠀵󠀷󠁿 Flag for Marche (IT-57)
🏴󠁪󠁭󠀱󠀳󠁿 Flag for Clarendon (JM-13)
🏴󠁩󠁴󠀸󠀲󠁿 Flag for Sicily (IT-82)
🏴󠁩󠁴󠀶󠀲󠁿 Flag for Lazio (IT-62)
🏴󠁪󠁭󠀰󠀲󠁿 Flag for Saint Andrew (JM-02)
🏴󠁩󠁴󠀴󠀲󠁿 Flag for Liguria (IT-42)
🏴󠁪󠁯󠁢󠁡󠁿 Flag for Balqa (JO-BA)
🏴󠁩󠁲󠀲󠀷󠁿 Flag for Golestan (IR-27)
🏴󠁣󠁮󠀳󠀱󠁿 Flag for Shanghai (CN-31)
🏴󠁩󠁴󠀷󠀵󠁿 Flag for Apulia (IT-75)
🏴󠁪󠁯󠁡󠁴󠁿 Flag for Tafilah (JO-AT)
🏴󠁪󠁭󠀰󠀸󠁿 Flag for Saint James (JM-08)
🏴󠁪󠁭󠀰󠀶󠁿 Flag for Saint Ann (JM-06)
🏴󠁪󠁭󠀰󠀹󠁿 Flag for Hanover (JM-09)
🏴󠁪󠁯󠁡󠁺󠁿 Flag for Zarqa (JO-AZ)
🏴󠁦󠁩󠀱󠀲󠁿 Flag for Ostrobothnia (FI-12)
🏴󠁪󠁯󠁡󠁪󠁿 Flag for Ajloun (JO-AJ)
🏴󠁪󠁭󠀰󠀷󠁿 Flag for Trelawny (JM-07)
🏴󠁪󠁭󠀱󠀱󠁿 Flag for Saint Elizabeth (JM-11)
🏴󠁪󠁯󠁡󠁱󠁿 Flag for Aqaba (JO-AQ)
🏴󠁩󠁴󠀵󠀵󠁿 Flag for Umbria (IT-55)
🏴󠁪󠁯󠁡󠁭󠁿 Flag for Amman (JO-AM)
🏴󠁪󠁭󠀱󠀰󠁿 Flag for Westmoreland (JM-10)
🏴󠁪󠁰󠀰󠀸󠁿 Flag for Ibaraki (JP-08)
🏴󠁪󠁯󠁭󠁤󠁿 Flag for Madaba (JO-MD)
🏴󠁪󠁰󠀳󠀲󠁿 Flag for Shimane (JP-32)
🏴󠁪󠁰󠀲󠀶󠁿 Flag for Kyōto (JP-26)
🏴󠁣󠁬󠁡󠁲󠁿 Flag for Araucanía (CL-AR)
🏴󠁪󠁰󠀰󠀹󠁿 Flag for Tochigi (JP-09)
🏴󠁪󠁰󠀱󠀴󠁿 Flag for Kanagawa (JP-14)
🏴󠁪󠁰󠀱󠀶󠁿 Flag for Toyama (JP-16)
🏴󠁪󠁰󠀱󠀵󠁿 Flag for Niigata (JP-15)
🏴󠁪󠁰󠀲󠀹󠁿 Flag for Nara (JP-29)
🏴󠁪󠁰󠀲󠀳󠁿 Flag for Aichi (JP-23)
🏴󠁪󠁰󠀳󠀶󠁿 Flag for Tokushima (JP-36)
🏴󠁪󠁰󠀲󠀰󠁿 Flag for Nagano (JP-20)
🏴󠁪󠁰󠀳󠀱󠁿 Flag for Tottori (JP-31)
🏴󠁪󠁰󠀰󠀳󠁿 Flag for Iwate (JP-03)
🏴󠁪󠁰󠀳󠀰󠁿 Flag for Wakayama (JP-30)
🏴󠁪󠁰󠀳󠀳󠁿 Flag for Okayama (JP-33)
🏴󠁪󠁰󠀱󠀷󠁿 Flag for Ishikawa (JP-17)
🏴󠁪󠁰󠀰󠀴󠁿 Flag for Miyagi (JP-04)
🏴󠁪󠁰󠀲󠀷󠁿 Flag for Ōsaka (JP-27)
🏴󠁪󠁯󠁭󠁡󠁿 Flag for Mafraq (JO-MA)
🏴󠁪󠁰󠀳󠀵󠁿 Flag for Yamaguchi (JP-35)
🏴󠁣󠁵󠀱󠀲󠁿 Flag for Granma (CU-12)
🏴󠁪󠁰󠀰󠀵󠁿 Flag for Akita (JP-05)
🏴󠁪󠁰󠀰󠀲󠁿 Flag for Aomori (JP-02)
🏴󠁪󠁰󠀲󠀲󠁿 Flag for Shizuoka (JP-22)
🏴󠁪󠁰󠀱󠀹󠁿 Flag for Yamanashi (JP-19)
🏴󠁪󠁰󠀳󠀴󠁿 Flag for Hiroshima (JP-34)
🏴󠁪󠁯󠁭󠁮󠁿 Flag for Ma’an (JO-MN)
🏴󠁪󠁰󠀱󠀰󠁿 Flag for Gunma (JP-10)
🏴󠁪󠁰󠀲󠀴󠁿 Flag for Mie (JP-24)
🏴󠁪󠁰󠀰󠀶󠁿 Flag for Yamagata (JP-06)
🏴󠁪󠁰󠀲󠀵󠁿 Flag for Shiga (JP-25)
🏴󠁪󠁰󠀲󠀸󠁿 Flag for Hyōgo (JP-28)
🏴󠁪󠁯󠁫󠁡󠁿 Flag for Karak (JO-KA)
🏴󠁪󠁰󠀳󠀸󠁿 Flag for Ehime (JP-38)
🏴󠁪󠁰󠀱󠀲󠁿 Flag for Chiba (JP-12)
🏴󠁪󠁰󠀳󠀷󠁿 Flag for Kagawa (JP-37)
󠀧 Tag Apostrophe
🏴󠁫󠁥󠀲󠀴󠁿 Flag for Mandera (KE-24)
🏴󠁫󠁥󠀲󠀰󠁿 Flag for Laikipia (KE-20)
🏴󠁪󠁰󠀴󠀶󠁿 Flag for Kagoshima (JP-46)
🏴󠁫󠁥󠀳󠀰󠁿 Flag for Nairobi County (KE-30)
🏴󠁫󠁥󠀱󠀴󠁿 Flag for Kilifi (KE-14)
🏴󠁫󠁥󠀱󠀵󠁿 Flag for Kirinyaga (KE-15)
🏴󠁫󠁥󠀲󠀸󠁿 Flag for Mombasa (KE-28)
🏴󠁫󠁥󠀱󠀰󠁿 Flag for Kajiado (KE-10)
🏴󠁫󠁥󠀰󠀳󠁿 Flag for Bungoma (KE-03)
🏴󠁫󠁥󠀱󠀳󠁿 Flag for Kiambu (KE-13)
🏴󠁪󠁰󠀴󠀱󠁿 Flag for Saga (JP-41)
🏴󠁪󠁰󠀴󠀰󠁿 Flag for Fukuoka (JP-40)
🏴󠁫󠁥󠀰󠀴󠁿 Flag for Busia (KE-04)
🏴󠁫󠁥󠀲󠀱󠁿 Flag for Lamu (KE-21)
🏴󠁫󠁥󠀲󠀷󠁿 Flag for Migori (KE-27)
🏴󠁫󠁥󠀰󠀶󠁿 Flag for Embu (KE-06)
👩🏾‍👦🏾‍👧🏾 Family - Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone, Girl: Medium-Dark Skin Tone
🏴󠁫󠁥󠀱󠀲󠁿 Flag for Kericho (KE-12)
🏴󠁫󠁥󠀰󠀹󠁿 Flag for Isiolo (KE-09)
🏴󠁫󠁥󠀱󠀹󠁿 Flag for Kwale (KE-19)
🏴󠁪󠁰󠀴󠀵󠁿 Flag for Miyazaki (JP-45)
🏴󠁫󠁥󠀲󠀳󠁿 Flag for Makueni (KE-23)
🏴󠁪󠁰󠀳󠀹󠁿 Flag for Kōchi (JP-39)
🏴󠁫󠁥󠀰󠀲󠁿 Flag for Bomet (KE-02)
🏴󠁪󠁰󠀴󠀲󠁿 Flag for Nagasaki (JP-42)
🏴󠁫󠁥󠀰󠀸󠁿 Flag for Homa Bay (KE-08)
🏴󠁫󠁥󠀱󠀱󠁿 Flag for Kakamega (KE-11)
🏴󠁫󠁥󠀳󠀲󠁿 Flag for Nandi (KE-32)
🏴󠁫󠁥󠀲󠀲󠁿 Flag for Machakos (KE-22)
🏴󠁪󠁰󠀴󠀳󠁿 Flag for Kumamoto (JP-43)
🏴󠁫󠁥󠀲󠀶󠁿 Flag for Meru (KE-26)
🏴󠁫󠁥󠀲󠀹󠁿 Flag for Murang’a (KE-29)
🏴󠁫󠁥󠀱󠀶󠁿 Flag for Kisii (KE-16)
🏴󠁫󠁥󠀰󠀵󠁿 Flag for Elgeyo-Marakwet (KE-05)
🏴󠁪󠁰󠀴󠀴󠁿 Flag for Ōita (JP-44)
🏴󠁫󠁥󠀳󠀳󠁿 Flag for Narok (KE-33)
🏴󠁫󠁥󠀳󠀷󠁿 Flag for Samburu (KE-37)
🏴󠁫󠁥󠀴󠀷󠁿 Flag for West Pokot (KE-47)
🏴󠁫󠁧󠁧󠁯󠁿 Flag for Osh (KG-GO)
🏴󠁫󠁥󠀳󠀹󠁿 Flag for Taita-Taveta (KE-39)
🏴󠁫󠁧󠁢󠁿 Flag for Batken (KG-B)
🏴󠁫󠁥󠀴󠀱󠁿 Flag for Tharaka-Nithi (KE-41)
🏴󠁫󠁨󠀲󠀵󠁿 Flag for Tbong Khmum (KH-25)
🏴󠁫󠁥󠀳󠀶󠁿 Flag for Nyeri (KE-36)
🏴󠁫󠁨󠀱󠀸󠁿 Flag for Sihanoukville (KH-18)
🏴󠁫󠁨󠀱󠀲󠁿 Flag for Phnom Penh (KH-12)
🏴󠁫󠁧󠁧󠁢󠁿 Flag for Bishkek (KG-GB)
🏴󠁫󠁨󠀱󠀷󠁿 Flag for Siem Reap (KH-17)
🏴󠁫󠁨󠀲󠀳󠁿 Flag for Kep (KH-23)
🏴󠁫󠁨󠀱󠀰󠁿 Flag for Kratié (KH-10)
🏴󠁫󠁨󠀲󠀱󠁿 Flag for Takéo (KH-21)
🏴󠁫󠁨󠀲󠁿 Flag for Battambang (KH-2)
🏴󠁫󠁥󠀴󠀰󠁿 Flag for Tana River (KE-40)
🏴󠁫󠁨󠀱󠀳󠁿 Flag for Preah Vihear (KH-13)
🏴󠁫󠁨󠀱󠀶󠁿 Flag for Ratanakiri (KH-16)
🏴󠁫󠁥󠀴󠀲󠁿 Flag for Trans Nzoia (KE-42)
🏴󠁫󠁨󠀱󠀹󠁿 Flag for Stung Treng (KH-19)
🏴󠁫󠁥󠀳󠀵󠁿 Flag for Nyandarua (KE-35)
🏴󠁫󠁥󠀴󠀴󠁿 Flag for Uasin Gishu (KE-44)
🏴󠁫󠁥󠀴󠀵󠁿 Flag for Vihiga (KE-45)
🏴󠁫󠁧󠁪󠁿 Flag for Jalal-Abad (KG-J)
🏴󠁫󠁨󠀱󠀱󠁿 Flag for Mondulkiri (KH-11)
🏴󠁫󠁧󠁯󠁿 Flag for Osh Region (KG-O)
🏴󠁫󠁥󠀴󠀳󠁿 Flag for Turkana (KE-43)
🏴󠁫󠁨󠀱󠁿 Flag for Banteay Meanchey (KH-1)
🏴󠁫󠁧󠁮󠁿 Flag for Naryn (KG-N)
🏴󠁫󠁧󠁴󠁿 Flag for Talas (KG-T)
🏴󠁫󠁥󠀳󠀸󠁿 Flag for Siaya (KE-38)
🏴󠁫󠁥󠀳󠀴󠁿 Flag for Nyamira (KE-34)
🏴󠁫󠁨󠀲󠀴󠁿 Flag for Pailin (KH-24)
🏴󠁫󠁨󠀲󠀲󠁿 Flag for Oddar Meanchey (KH-22)
🏴󠁫󠁨󠀱󠀵󠁿 Flag for Pursat (KH-15)
🏴󠁫󠁥󠀴󠀶󠁿 Flag for Wajir (KE-46)
🏴󠁫󠁧󠁹󠁿 Flag for Issyk-Kul (KG-Y)
🏴󠁫󠁧󠁣󠁿 Flag for Chuy (KG-C)
🏴󠁫󠁨󠀱󠀴󠁿 Flag for Prey Veng (KH-14)
🏴󠁫󠁭󠁡󠁿 Flag for Anjouan (KM-A)
🏴󠁫󠁭󠁭󠁿 Flag for Mohéli (KM-M)
🏴󠁫󠁰󠀰󠀱󠁿 Flag for Pyongyang (KP-01)
🏴󠁫󠁨󠀴󠁿 Flag for Kampong Chhnang (KH-4)
🏴󠁫󠁲󠀲󠀶󠁿 Flag for Busan (KR-26)
🏴󠁫󠁰󠀰󠀳󠁿 Flag for North Pyongan (KP-03)
🏴󠁫󠁨󠀷󠁿 Flag for Kampot (KH-7)
🏴󠁫󠁨󠀹󠁿 Flag for Koh Kong (KH-9)
🏴󠁫󠁰󠀰󠀲󠁿 Flag for South Pyongan (KP-02)
🏴󠁫󠁰󠀰󠀴󠁿 Flag for Chagang (KP-04)
🏴󠁫󠁲󠀴󠀳󠁿 Flag for North Chungcheong (KR-43)
🏴󠁫󠁲󠀴󠀶󠁿 Flag for South Jeolla (KR-46)
🏴󠁫󠁰󠀰󠀶󠁿 Flag for North Hwanghae (KP-06)
🏴󠁫󠁲󠀲󠀸󠁿 Flag for Incheon (KR-28)
🏴󠁫󠁲󠀱󠀱󠁿 Flag for Seoul (KR-11)
🏴󠁫󠁨󠀵󠁿 Flag for Kampong Speu (KH-5)
🏴󠁫󠁲󠀴󠀵󠁿 Flag for North Jeolla (KR-45)
🏴󠁫󠁮󠁫󠁿 Flag for Saint Kitts (KN-K)
🏴󠁫󠁰󠀰󠀷󠁿 Flag for Kangwon (KP-07)
🏴󠁫󠁲󠀲󠀷󠁿 Flag for Daegu (KR-27)
🏴󠁫󠁨󠀳󠁿 Flag for Kampong Cham (KH-3)
🏴󠁫󠁮󠁮󠁿 Flag for Nevis (KN-N)
🏴󠁫󠁨󠀸󠁿 Flag for Kandal (KH-8)
🏴󠁫󠁨󠀶󠁿 Flag for Kampong Thom (KH-6)
🏴󠁪󠁭󠀱󠀲󠁿 Flag for Manchester (JM-12)
🏴󠁫󠁰󠀰󠀵󠁿 Flag for South Hwanghae (KP-05)
🏴󠁫󠁰󠀱󠀰󠁿 Flag for Ryanggang (KP-10)
🏴󠁫󠁰󠀰󠀸󠁿 Flag for South Hamgyong (KP-08)
🏴󠁫󠁰󠀱󠀳󠁿 Flag for Rason (KP-13)
🏴󠁫󠁲󠀴󠀲󠁿 Flag for Gangwon (KR-42)
🏴󠁫󠁲󠀳󠀱󠁿 Flag for Ulsan (KR-31)
🏴󠁫󠁲󠀴󠀴󠁿 Flag for South Chungcheong (KR-44)
🏴󠁫󠁲󠀳󠀰󠁿 Flag for Daejeon (KR-30)
🏴󠁫󠁭󠁧󠁿 Flag for Grande Comore (KM-G)
🏴󠁫󠁲󠀴󠀷󠁿 Flag for North Gyeongsang (KR-47)
🏴󠁫󠁰󠀰󠀹󠁿 Flag for North Hamgyong (KP-09)
🏴󠁬󠁡󠁨󠁯󠁿 Flag for Houaphanh (LA-HO)
🏴󠁬󠁡󠁣󠁨󠁿 Flag for Champasak (LA-CH)
󠁆 Tag Latin Capital Letter F
🏴󠁫󠁺󠁡󠁬󠁡󠁿 Flag for Almaty (KZ-ALA)
🏴󠁫󠁺󠁭󠁡󠁮󠁿 Flag for Mangystau (KZ-MAN)
🏴󠁬󠁡󠁰󠁨󠁿 Flag for Phongsaly (LA-PH)
🏴󠁫󠁺󠁡󠁫󠁭󠁿 Flag for Akmola (KZ-AKM)
🏴󠁫󠁲󠀵󠀰󠁿 Flag for Sejong (KR-50)
🏴󠁫󠁺󠁡󠁬󠁭󠁿 Flag for Almaty Region (KZ-ALM)
🏴󠁫󠁷󠁫󠁵󠁿 Flag for Al Asimah (KW-KU)
󠁏 Tag Latin Capital Letter O
🏴󠁫󠁺󠁡󠁳󠁴󠁿 Flag for Astana (KZ-AST)
🏴󠁫󠁺󠁡󠁫󠁴󠁿 Flag for Aktobe (KZ-AKT)
🏴󠁬󠁡󠁡󠁴󠁿 Flag for Attapeu (LA-AT)
🏴󠁫󠁷󠁪󠁡󠁿 Flag for Al Jahra (KW-JA)
🏴󠁫󠁷󠁨󠁡󠁿 Flag for Hawalli (KW-HA)
🏴󠁬󠁡󠁯󠁵󠁿 Flag for Oudomxay (LA-OU)
🏴󠁫󠁺󠁫󠁵󠁳󠁿 Flag for Kostanay (KZ-KUS)
🏴󠁬󠁡󠁶󠁴󠁿 Flag for Vientiane (LA-VT)
🏴󠁬󠁡󠁫󠁨󠁿 Flag for Khammouane (LA-KH)
🏴󠁫󠁺󠁺󠁨󠁡󠁿 Flag for Jambyl (KZ-ZHA)
🏴󠁬󠁡󠁬󠁰󠁿 Flag for Luang Prabang (LA-LP)
🏴󠁫󠁷󠁦󠁡󠁿 Flag for Al Farwaniyah (KW-FA)
🏴󠁫󠁺󠁫󠁡󠁲󠁿 Flag for Karagandy (KZ-KAR)
🏴󠁫󠁺󠁡󠁴󠁹󠁿 Flag for Atyrau (KZ-ATY)
🏴󠁫󠁺󠁫󠁺󠁹󠁿 Flag for Kyzylorda (KZ-KZY)
🏴󠁫󠁺󠁹󠁵󠁺󠁿 Flag for South Kazakhstan (KZ-YUZ)
󠁚 Tag Latin Capital Letter Z
🏴󠁬󠁡󠁬󠁭󠁿 Flag for Luang Namtha (LA-LM)
🏴󠁫󠁲󠀴󠀱󠁿 Flag for Gyeonggi (KR-41)
🏴󠁫󠁷󠁭󠁵󠁿 Flag for Mubarak Al-Kabeer (KW-MU)
👩🏿‍👦🏿‍👧🏿 Family - Woman: Dark Skin Tone, Boy: Dark Skin Tone, Girl: Dark Skin Tone
🏴󠁫󠁷󠁡󠁨󠁿 Flag for Al Ahmadi (KW-AH)
🏴󠁫󠁺󠁰󠁡󠁶󠁿 Flag for Pavlodar (KZ-PAV)
🏴󠁬󠁡󠁳󠁬󠁿 Flag for Salavan (LA-SL)
🏴󠁫󠁺󠁳󠁥󠁶󠁿 Flag for North Kazakhstan (KZ-SEV)
🏴󠁬󠁡󠁢󠁬󠁿 Flag for Bolikhamsai (LA-BL)
󠀽 Tag Equals Sign
🏴󠁬󠁣󠀱󠀱󠁿 Flag for Vieux Fort (LC-11)
🏴󠁬󠁣󠀰󠀷󠁿 Flag for Laborie (LC-07)
👩🏻‍👦🏻‍👶🏻 Family - Woman: Light Skin Tone, Boy: Light Skin Tone, Baby: Light Skin Tone
🏴󠁬󠁣󠀰󠀶󠁿 Flag for Gros Islet (LC-06)
🏴󠁬󠁫󠀸󠁿 Flag for Uva (LK-8)
🏴󠁬󠁡󠁸󠁡󠁿 Flag for Sainyabuli (LA-XA)
🏴󠁬󠁫󠀷󠁿 Flag for North Central (LK-7)
🏴󠁬󠁢󠁡󠁫󠁿 Flag for Akkar (LB-AK)
🏴󠁬󠁢󠁢󠁨󠁿 Flag for Baalbek-Hermel (LB-BH)
🏴󠁬󠁩󠀰󠀹󠁿 Flag for Triesen (LI-09)
🏴󠁬󠁫󠀴󠁿 Flag for Northern (LK-4)
🏴󠁬󠁩󠀰󠀱󠁿 Flag for Balzers (LI-01)
🏴󠁬󠁢󠁡󠁳󠁿 Flag for North (LB-AS)
🏴󠁬󠁩󠀰󠀴󠁿 Flag for Mauren (LI-04)
🏴󠁬󠁢󠁮󠁡󠁿 Flag for Nabatieh (LB-NA)
🏴󠁬󠁣󠀰󠀵󠁿 Flag for Dennery (LC-05)
🏴󠁬󠁢󠁪󠁡󠁿 Flag for South (LB-JA)
🏴󠁬󠁩󠀱󠀱󠁿 Flag for Vaduz (LI-11)
🏴󠁬󠁣󠀰󠀲󠁿 Flag for Castries (LC-02)
🏴󠁬󠁩󠀱󠀰󠁿 Flag for Triesenberg (LI-10)
🏴󠁬󠁩󠀰󠀵󠁿 Flag for Planken (LI-05)
🏴󠁬󠁫󠀲󠁿 Flag for Central (LK-2)
🏴󠁬󠁩󠀰󠀶󠁿 Flag for Ruggell (LI-06)
🏴󠁬󠁣󠀰󠀸󠁿 Flag for Micoud (LC-08)
🏴󠁬󠁩󠀰󠀲󠁿 Flag for Eschen (LI-02)
🏴󠁬󠁣󠀱󠀲󠁿 Flag for Canaries (LC-12)
🏴󠁬󠁢󠁢󠁡󠁿 Flag for Beirut (LB-BA)
🏴󠁬󠁡󠁸󠁩󠁿 Flag for Xiangkhouang (LA-XI)
🏴󠁬󠁣󠀱󠀰󠁿 Flag for Soufrière (LC-10)
🏴󠁫󠁥󠀰󠀷󠁿 Flag for Garissa (KE-07)
🏴󠁬󠁫󠀶󠁿 Flag for North Western (LK-6)
🏴󠁬󠁣󠀰󠀱󠁿 Flag for Anse la Raye (LC-01)
🏴󠁬󠁣󠀰󠀳󠁿 Flag for Choiseul (LC-03)
🏴󠁬󠁩󠀰󠀳󠁿 Flag for Gamprin (LI-03)
🏴󠁬󠁴󠀱󠀰󠁿 Flag for Jonava (LT-10)
🏴󠁬󠁳󠁤󠁿 Flag for Berea (LS-D)
🏴󠁬󠁲󠁧󠁧󠁿 Flag for Grand Gedeh (LR-GG)
🏴󠁬󠁴󠀱󠀲󠁿 Flag for Jurbarkas (LT-12)
🏴󠁬󠁲󠁬󠁯󠁿 Flag for Lofa (LR-LO)
🏴󠁬󠁲󠁧󠁢󠁿 Flag for Grand Bassa (LR-GB)
🏴󠁬󠁳󠁧󠁿 Flag for Quthing (LS-G)
🏴󠁬󠁴󠀱󠀶󠁿 Flag for Kaunas (LT-16)
🏴󠁬󠁲󠁭󠁯󠁿 Flag for Montserrado (LR-MO)
🏴󠁬󠁲󠁧󠁰󠁿 Flag for Gbarpolu (LR-GP)
🏴󠁬󠁳󠁫󠁿 Flag for Thaba-Tseka (LS-K)
🏴󠁬󠁴󠀰󠀵󠁿 Flag for Birštonas (LT-05)
🏴󠁬󠁲󠁭󠁧󠁿 Flag for Margibi (LR-MG)
🏴󠁬󠁲󠁮󠁩󠁿 Flag for Nimba (LR-NI)
🏴󠁬󠁳󠁦󠁿 Flag for Mohale’s Hoek (LS-F)
🏴󠁬󠁲󠁧󠁫󠁿 Flag for Grand Kru (LR-GK)
🏴󠁦󠁩󠀰󠀸󠁿 Flag for Central Finland (FI-08)
🏴󠁬󠁴󠀰󠀷󠁿 Flag for Druskininkai (LT-07)
🏴󠁬󠁴󠀱󠀵󠁿 Flag for Kauno Municipality (LT-15)
🏴󠁬󠁲󠁳󠁩󠁿 Flag for Sinoe (LR-SI)
🏴󠁬󠁴󠀰󠀴󠁿 Flag for Anykščiai (LT-04)
🏴󠁬󠁳󠁣󠁿 Flag for Leribe (LS-C)
🏴󠁬󠁴󠀱󠀱󠁿 Flag for Joniškis (LT-11)
🏴󠁬󠁲󠁢󠁭󠁿 Flag for Bomi (LR-BM)
🏴󠁬󠁴󠀱󠀳󠁿 Flag for Kaišiadorys (LT-13)
🏴󠁬󠁴󠀰󠀸󠁿 Flag for Elektrėnai (LT-08)
🏴󠁬󠁳󠁨󠁿 Flag for Qacha’s Nek (LS-H)
🏴󠁬󠁴󠀱󠀴󠁿 Flag for Kalvarija (LT-14)
🏴󠁬󠁲󠁲󠁩󠁿 Flag for Rivercess (LR-RI)
🏴󠁬󠁴󠀰󠀱󠁿 Flag for Akmenė (LT-01)
🏴󠁬󠁴󠀰󠀹󠁿 Flag for Ignalina (LT-09)
🏴󠁬󠁳󠁥󠁿 Flag for Mafeteng (LS-E)
🏴󠁬󠁳󠁢󠁿 Flag for Butha-Buthe (LS-B)
🏴󠁬󠁳󠁪󠁿 Flag for Mokhotlong (LS-J)
🏴󠁬󠁴󠀰󠀳󠁿 Flag for Alytus (LT-03)
🏴󠁬󠁴󠀰󠀶󠁿 Flag for Biržai (LT-06)
🏴󠁣󠁦󠁫󠁢󠁿 Flag for Nana-Grébizi (CF-KB)
🏴󠁬󠁴󠀵󠀴󠁿 Flag for Utena (LT-54)
🏴󠁬󠁴󠀲󠀷󠁿 Flag for Molėtai (LT-27)
🏴󠁬󠁴󠀴󠀱󠁿 Flag for Šakiai (LT-41)
🏴󠁬󠁴󠀱󠀹󠁿 Flag for Kelmė (LT-19)
🏴󠁬󠁴󠀲󠀳󠁿 Flag for Kupiškis (LT-23)
🏴󠁬󠁴󠀳󠀳󠁿 Flag for Panevėžys (LT-33)
🏴󠁬󠁴󠀵󠀶󠁿 Flag for Vilkaviškis (LT-56)
🏴󠁬󠁴󠀲󠀸󠁿 Flag for Neringa (LT-28)
🏴󠁬󠁴󠀵󠀲󠁿 Flag for Trakai (LT-52)
🏴󠁬󠁴󠀲󠀹󠁿 Flag for Pagėgiai (LT-29)
🏴󠁬󠁴󠀴󠀶󠁿 Flag for Šilutė (LT-46)
🏴󠁬󠁴󠀳󠀱󠁿 Flag for Palanga (LT-31)
🏴󠁬󠁴󠀱󠀸󠁿 Flag for Kėdainiai (LT-18)
🏴󠁬󠁴󠀴󠀰󠁿 Flag for Rokiškis (LT-40)
🏴󠁬󠁴󠀴󠀵󠁿 Flag for Šilalė (LT-45)
🏴󠁬󠁴󠀴󠀳󠁿 Flag for Šiaulių Municipality (LT-43)
🏴󠁦󠁭󠁰󠁮󠁩󠁿 Flag for Pohnpei (FM-PNI)
🏴󠁬󠁴󠀵󠀱󠁿 Flag for Telšiai (LT-51)
🏴󠁬󠁴󠀲󠀱󠁿 Flag for Klaipėda (LT-21)
🏴󠁬󠁴󠀱󠀷󠁿 Flag for Kazlų Rūda (LT-17)
🏴󠁬󠁴󠀴󠀷󠁿 Flag for Širvintos (LT-47)
🏴󠁬󠁴󠀳󠀶󠁿 Flag for Prienai (LT-36)
🏴󠁬󠁴󠀳󠀰󠁿 Flag for Pakruojis (LT-30)
🏴󠁬󠁴󠀴󠀴󠁿 Flag for Šiauliai (LT-44)
🏴󠁬󠁴󠀲󠀲󠁿 Flag for Kretinga (LT-22)
🏴󠁬󠁴󠀴󠀲󠁿 Flag for Šalčininkai (LT-42)
🏴󠁬󠁴󠀳󠀸󠁿 Flag for Raseiniai (LT-38)
🏴󠁬󠁴󠀵󠀵󠁿 Flag for Varėna (LT-55)
🏴󠁬󠁴󠀳󠀴󠁿 Flag for Pasvalys (LT-34)
🏴󠁬󠁴󠀳󠀵󠁿 Flag for Plungė (LT-35)
🏴󠁬󠁴󠀴󠀹󠁿 Flag for Švenčionys (LT-49)
🏴󠁬󠁴󠀳󠀷󠁿 Flag for Radviliškis (LT-37)
🏴󠁬󠁴󠀲󠀴󠁿 Flag for Lazdijai (LT-24)
🏴󠁬󠁴󠀵󠀰󠁿 Flag for Tauragė (LT-50)
🏴󠁬󠁴󠀴󠀸󠁿 Flag for Skuodas (LT-48)
🏴󠁬󠁴󠀵󠀳󠁿 Flag for Ukmergė (LT-53)
🏴󠁬󠁴󠀳󠀹󠁿 Flag for Rietavas (LT-39)
🏴󠁬󠁴󠀲󠀵󠁿 Flag for Marijampolė (LT-25)
🏴󠁬󠁴󠀲󠀶󠁿 Flag for Mažeikiai (LT-26)
🏴󠁬󠁵󠁣󠁬󠁿 Flag for Clervaux (LU-CL)
🏴󠁬󠁶󠀰󠀱󠀳󠁿 Flag for Baldone (LV-013)
🏴󠁬󠁶󠀰󠀰󠀶󠁿 Flag for Alsunga (LV-006)
🏴󠁬󠁵󠁤󠁩󠁿 Flag for Diekirch (LU-DI)
🏴󠁬󠁴󠁴󠁡󠁿 Flag for Tauragė County (LT-TA)
🏴󠁬󠁴󠁡󠁬󠁿 Flag for Alytus County (LT-AL)
🏴󠁬󠁶󠀰󠀰󠀲󠁿 Flag for Aizkraukle (LV-002)
🏴󠁬󠁵󠁬󠁵󠁿 Flag for Luxembourg (LU-LU)
🏴󠁬󠁴󠁭󠁲󠁿 Flag for Marijampolė County (LT-MR)
👩🏽‍👨🏽‍👶🏽 Family - Woman: Medium Skin Tone, Man: Medium Skin Tone, Baby: Medium Skin Tone
🏴󠁬󠁶󠀰󠀱󠀱󠁿 Flag for Ādaži (LV-011)
🏴󠁬󠁵󠁥󠁣󠁿 Flag for Echternach (LU-EC)
🏴󠁬󠁵󠁲󠁤󠁿 Flag for Redange (LU-RD)
🏴󠁬󠁴󠀵󠀹󠁿 Flag for Visaginas (LT-59)
🏴󠁬󠁴󠁴󠁥󠁿 Flag for Telšiai County (LT-TE)
🏴󠁬󠁶󠀰󠀰󠀸󠁿 Flag for Amata (LV-008)
🏴󠁬󠁴󠀵󠀸󠁿 Flag for Vilnius (LT-58)
🏴󠁬󠁵󠁧󠁲󠁿 Flag for Grevenmacher (LU-GR)
🏴󠁬󠁶󠀰󠀰󠀵󠁿 Flag for Aloja (LV-005)
🏴󠁬󠁵󠁭󠁥󠁿 Flag for Mersch (LU-ME)
🏴󠁬󠁵󠁶󠁤󠁿 Flag for Vianden (LU-VD)
🏴󠁬󠁴󠁵󠁴󠁿 Flag for Utena County (LT-UT)
🏴󠁬󠁴󠁳󠁡󠁿 Flag for Šiauliai County (LT-SA)
🏴󠁬󠁶󠀰󠀰󠀹󠁿 Flag for Ape (LV-009)
🏴󠁬󠁴󠁫󠁵󠁿 Flag for Kaunas County (LT-KU)
🏴󠁬󠁴󠀶󠀰󠁿 Flag for Zarasai (LT-60)
🏴󠁬󠁵󠁷󠁩󠁿 Flag for Wiltz (LU-WI)
🏴󠁬󠁶󠀰󠀰󠀱󠁿 Flag for Aglona (LV-001)
🏴󠁬󠁴󠁶󠁬󠁿 Flag for Vilnius County (LT-VL)
🏴󠁬󠁢󠁪󠁬󠁿 Flag for Mount Lebanon (LB-JL)
🏴󠁬󠁶󠀰󠀰󠀷󠁿 Flag for Alūksne (LV-007)
🏴󠁬󠁵󠁲󠁭󠁿 Flag for Remich (LU-RM)
🏴󠁬󠁶󠀰󠀰󠀴󠁿 Flag for Aknīste (LV-004)
🏴󠁬󠁵󠁥󠁳󠁿 Flag for Esch-sur-Alzette (LU-ES)
🏴󠁬󠁶󠀰󠀰󠀳󠁿 Flag for Aizpute (LV-003)
🏴󠁬󠁴󠁫󠁬󠁿 Flag for Klaipėda County (LT-KL)
🏴󠁬󠁶󠀰󠀲󠀷󠁿 Flag for Dundaga (LV-027)
🏴󠁬󠁶󠀰󠀴󠀰󠁿 Flag for Jaunpils (LV-040)
🏴󠁬󠁶󠀰󠀱󠀹󠁿 Flag for Burtnieki (LV-019)
🏴󠁬󠁶󠀰󠀱󠀵󠁿 Flag for Balvi (LV-015)
🏴󠁬󠁶󠀰󠀱󠀷󠁿 Flag for Beverīna (LV-017)
🏴󠁬󠁶󠀰󠀲󠀵󠁿 Flag for Daugavpils Municipality (LV-025)
🏴󠁬󠁶󠀰󠀲󠀱󠁿 Flag for Cesvaine (LV-021)
🏴󠁬󠁶󠀰󠀳󠀶󠁿 Flag for Ilūkste (LV-036)
🏴󠁬󠁶󠀰󠀵󠀰󠁿 Flag for Kuldīga (LV-050)
🏴󠁬󠁶󠀰󠀳󠀲󠁿 Flag for Grobiņa (LV-032)
🏴󠁬󠁶󠀰󠀳󠀳󠁿 Flag for Gulbene (LV-033)
🏴󠁬󠁶󠀰󠀴󠀳󠁿 Flag for Kandava (LV-043)
🏴󠁬󠁶󠀰󠀱󠀸󠁿 Flag for Brocēni (LV-018)
🏴󠁬󠁶󠀰󠀴󠀸󠁿 Flag for Krimulda (LV-048)
🏴󠁬󠁶󠀰󠀲󠀰󠁿 Flag for Carnikava (LV-020)
🏴󠁬󠁶󠀰󠀴󠀹󠁿 Flag for Krustpils (LV-049)
👩🏾‍👨🏾‍👶🏾 Family - Woman: Medium-Dark Skin Tone, Man: Medium-Dark Skin Tone, Baby: Medium-Dark Skin Tone
🏴󠁬󠁶󠀰󠀲󠀶󠁿 Flag for Dobele (LV-026)
🏴󠁬󠁶󠀰󠀴󠀵󠁿 Flag for Kocēni (LV-045)
🏴󠁬󠁶󠀰󠀳󠀱󠁿 Flag for Garkalne (LV-031)
🏴󠁬󠁶󠀰󠀳󠀰󠁿 Flag for Ērgļi (LV-030)
🏴󠁬󠁶󠀰󠀲󠀸󠁿 Flag for Durbe (LV-028)
🏴󠁬󠁶󠀰󠀴󠀷󠁿 Flag for Krāslava (LV-047)
🏴󠁬󠁶󠀰󠀲󠀴󠁿 Flag for Dagda (LV-024)
🏴󠁬󠁶󠀰󠀳󠀸󠁿 Flag for Jaunjelgava (LV-038)
🏴󠁬󠁶󠀰󠀱󠀶󠁿 Flag for Bauska (LV-016)
🏴󠁬󠁶󠀰󠀱󠀴󠁿 Flag for Baltinava (LV-014)
🏴󠁬󠁶󠀰󠀴󠀲󠁿 Flag for Jēkabpils Municipality (LV-042)
🏴󠁬󠁶󠀰󠀳󠀹󠁿 Flag for Jaunpiebalga (LV-039)
🏴󠁬󠁶󠀰󠀲󠀲󠁿 Flag for Cēsis (LV-022)
🏴󠁬󠁶󠀰󠀳󠀴󠁿 Flag for Iecava (LV-034)
🏴󠁬󠁶󠀰󠀵󠀱󠁿 Flag for Ķegums (LV-051)
🏴󠁬󠁶󠀰󠀳󠀵󠁿 Flag for Ikšķile (LV-035)
🏴󠁬󠁶󠀰󠀲󠀳󠁿 Flag for Cibla (LV-023)
🏴󠁬󠁶󠀰󠀴󠀴󠁿 Flag for Kārsava (LV-044)
🏴󠁬󠁶󠀰󠀲󠀹󠁿 Flag for Engure (LV-029)
🏴󠁬󠁶󠀰󠀵󠀵󠁿 Flag for Līgatne (LV-055)
🏴󠁬󠁶󠀰󠀶󠀶󠁿 Flag for Nīca (LV-066)
🏴󠁬󠁶󠀰󠀶󠀱󠁿 Flag for Mālpils (LV-061)
🏴󠁬󠁶󠀰󠀷󠀰󠁿 Flag for Pārgauja (LV-070)
🏴󠁬󠁶󠀰󠀵󠀳󠁿 Flag for Lielvārde (LV-053)
🏴󠁬󠁶󠀰󠀷󠀲󠁿 Flag for Pļaviņas (LV-072)
🏴󠁬󠁶󠀰󠀷󠀱󠁿 Flag for Pāvilosta (LV-071)
🏴󠁬󠁶󠀰󠀵󠀹󠁿 Flag for Madona (LV-059)
🏴󠁬󠁶󠀰󠀷󠀶󠁿 Flag for Rauna (LV-076)
🏴󠁬󠁶󠀰󠀵󠀴󠁿 Flag for Limbaži (LV-054)
🏴󠁬󠁶󠀰󠀶󠀴󠁿 Flag for Naukšēni (LV-064)
🏴󠁬󠁶󠀰󠀵󠀲󠁿 Flag for Ķekava (LV-052)
🏴󠁬󠁶󠀰󠀸󠀷󠁿 Flag for Salaspils (LV-087)
🏴󠁬󠁶󠀰󠀶󠀳󠁿 Flag for Mērsrags (LV-063)
🏴󠁬󠁶󠀰󠀶󠀸󠁿 Flag for Olaine (LV-068)
🏴󠁬󠁶󠀰󠀷󠀹󠁿 Flag for Roja (LV-079)
🏴󠁬󠁶󠀰󠀸󠀱󠁿 Flag for Rucava (LV-081)
🏴󠁧󠁥󠁫󠁫󠁿 Flag for Kvemo Kartli (GE-KK)
🏴󠁬󠁶󠀰󠀸󠀲󠁿 Flag for Rugāji (LV-082)
🏴󠁬󠁶󠀰󠀶󠀲󠁿 Flag for Mārupe (LV-062)
🏴󠁬󠁶󠀰󠀸󠀴󠁿 Flag for Rūjiena (LV-084)
🏴󠁬󠁶󠀰󠀸󠀹󠁿 Flag for Saulkrasti (LV-089)
🏴󠁬󠁶󠀰󠀸󠀸󠁿 Flag for Saldus (LV-088)
🏴󠁬󠁶󠀰󠀸󠀳󠁿 Flag for Rundāle (LV-083)
🏴󠁬󠁶󠀰󠀶󠀵󠁿 Flag for Nereta (LV-065)
🏴󠁬󠁶󠀰󠀶󠀹󠁿 Flag for Ozolnieki (LV-069)
🏴󠁬󠁶󠀰󠀸󠀰󠁿 Flag for Ropaži (LV-080)
🏴󠁬󠁶󠀰󠀷󠀸󠁿 Flag for Riebiņi (LV-078)
🏴󠁬󠁶󠀰󠀵󠀶󠁿 Flag for Līvāni (LV-056)
🏴󠁬󠁶󠀰󠀷󠀵󠁿 Flag for Priekuļi (LV-075)
🏴󠁬󠁶󠀰󠀵󠀸󠁿 Flag for Ludza (LV-058)
🏴󠁭󠁬󠀶󠁿 Flag for Tombouctou (ML-6)
🏴󠁬󠁶󠀰󠀷󠀴󠁿 Flag for Priekule (LV-074)
🏴󠁬󠁶󠀰󠀵󠀷󠁿 Flag for Lubāna (LV-057)
🏴󠁬󠁶󠀰󠀸󠀶󠁿 Flag for Salacgrīva (LV-086)
🏴󠁬󠁶󠀰󠀶󠀷󠁿 Flag for Ogre (LV-067)
🏴󠁬󠁶󠀰󠀷󠀳󠁿 Flag for Preiļi (LV-073)
🏴󠁬󠁶󠀱󠀰󠀷󠁿 Flag for Viesīte (LV-107)
🏴󠁬󠁶󠀰󠀹󠀴󠁿 Flag for Smiltene (LV-094)
🏴󠁬󠁹󠁫󠁦󠁿 Flag for Kufra (LY-KF)
🏴󠁬󠁶󠁤󠁧󠁶󠁿 Flag for Daugavpils (LV-DGV)
🏴󠁬󠁶󠀰󠀹󠀹󠁿 Flag for Tukums (LV-099)
👩🏿‍👨🏿‍👶🏿 Family - Woman: Dark Skin Tone, Man: Dark Skin Tone, Baby: Dark Skin Tone
🏴󠁬󠁶󠁬󠁰󠁸󠁿 Flag for Liepāja (LV-LPX)
🏴󠁬󠁶󠀱󠀰󠀳󠁿 Flag for Vārkava (LV-103)
🏴󠁬󠁶󠀱󠀰󠀰󠁿 Flag for Vaiņode (LV-100)
🏴󠁬󠁶󠁶󠁥󠁮󠁿 Flag for Ventspils (LV-VEN)
🏴󠁬󠁹󠁪󠁡󠁿 Flag for Jabal al Akhdar (LY-JA)
🏴󠁬󠁶󠁪󠁫󠁢󠁿 Flag for Jēkabpils (LV-JKB)
🏴󠁬󠁶󠀰󠀹󠀱󠁿 Flag for Sigulda (LV-091)
🏴󠁬󠁹󠁪󠁧󠁿 Flag for Jabal al Gharbi (LY-JG)
🏴󠁬󠁹󠁭󠁢󠁿 Flag for Murqub (LY-MB)
🏴󠁬󠁶󠀰󠀹󠀵󠁿 Flag for Stopiņi (LV-095)
🏴󠁬󠁹󠁧󠁴󠁿 Flag for Ghat (LY-GT)
🏴󠁬󠁹󠁤󠁲󠁿 Flag for Derna (LY-DR)
🏴󠁬󠁶󠁲󠁩󠁸󠁿 Flag for Riga (LV-RIX)
🏴󠁬󠁶󠀱󠀰󠀲󠁿 Flag for Varakļāni (LV-102)
🏴󠁬󠁶󠁪󠁥󠁬󠁿 Flag for Jelgava (LV-JEL)
🏴󠁬󠁶󠀰󠀹󠀲󠁿 Flag for Skrīveri (LV-092)
🏴󠁬󠁶󠀰󠀹󠀷󠁿 Flag for Talsi (LV-097)
🏴󠁬󠁶󠁶󠁭󠁲󠁿 Flag for Valmiera (LV-VMR)
🏴󠁬󠁹󠁢󠁡󠁿 Flag for Benghazi (LY-BA)
🏴󠁬󠁹󠁪󠁵󠁿 Flag for Jufra (LY-JU)
🏴󠁬󠁶󠁲󠁥󠁺󠁿 Flag for Rēzekne (LV-REZ)
🏴󠁬󠁶󠀰󠀹󠀳󠁿 Flag for Skrunda (LV-093)
🏴󠁬󠁶󠀱󠀱󠀰󠁿 Flag for Zilupe (LV-110)
🏴󠁬󠁶󠀰󠀹󠀶󠁿 Flag for Strenči (LV-096)
🏴󠁬󠁶󠀱󠀰󠀱󠁿 Flag for Valka (LV-101)
🏴󠁬󠁶󠀱󠀰󠀴󠁿 Flag for Vecpiebalga (LV-104)
🏴󠁬󠁶󠀱󠀰󠀵󠁿 Flag for Vecumnieki (LV-105)
🏴󠁬󠁶󠀱󠀰󠀸󠁿 Flag for Viļaka (LV-108)
🏴󠁬󠁶󠁪󠁵󠁲󠁿 Flag for Jūrmala (LV-JUR)
🏴󠁬󠁶󠀱󠀰󠀹󠁿 Flag for Viļāni (LV-109)
🏴󠁬󠁶󠀰󠀹󠀸󠁿 Flag for Tērvete (LV-098)
🏴󠁭󠁡󠀰󠀱󠁿 Flag for Tangier-Tétouan (MA-01)
🏴󠁭󠁣󠁭󠁣󠁿 Flag for Monte Carlo (MC-MC)
🏴󠁬󠁹󠁭󠁪󠁿 Flag for Marj (LY-MJ)
🏴󠁬󠁹󠁷󠁡󠁿 Flag for Al Wahat (LY-WA)
🏴󠁬󠁹󠁳󠁢󠁿 Flag for Sabha (LY-SB)
🏴󠁭󠁡󠀱󠀴󠁿 Flag for Guelmim-Es Semara (MA-14)
🏴󠁬󠁹󠁺󠁡󠁿 Flag for Zawiya (LY-ZA)
🏴󠁭󠁡󠀰󠀲󠁿 Flag for Gharb-Chrarda-Béni Hssen (MA-02)
🏴󠁭󠁣󠁣󠁯󠁿 Flag for La Condamine (MC-CO)
🏴󠁭󠁡󠀱󠀰󠁿 Flag for Doukkala-Abda (MA-10)
🏴󠁭󠁣󠁦󠁯󠁿 Flag for Fontvieille (MC-FO)
👩🏽‍👩🏽‍👦🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Boy: Medium Skin Tone
🏴󠁭󠁡󠀰󠀷󠁿 Flag for Rabat-Salé-Zemmour-Zaer (MA-07)
🏴󠁭󠁡󠀱󠀶󠁿 Flag for Oued Ed-Dahab-Lagouira (MA-16)
🏴󠁬󠁹󠁮󠁬󠁿 Flag for Nalut (LY-NL)
🏴󠁭󠁣󠁪󠁥󠁿 Flag for Jardin Exotique de Monaco (MC-JE)
🏴󠁭󠁡󠀰󠀳󠁿 Flag for Taza-Al Hoceima-Taounate (MA-03)
🏴󠁭󠁡󠀱󠀱󠁿 Flag for Marrakesh-Tensift-El Haouz (MA-11)
🏴󠁬󠁹󠁷󠁳󠁿 Flag for Wadi al Shatii (LY-WS)
🏴󠁭󠁣󠁭󠁯󠁿 Flag for Monaco-Ville (MC-MO)
🏴󠁬󠁹󠁴󠁢󠁿 Flag for Tripoli (LY-TB)
🏴󠁭󠁣󠁬󠁡󠁿 Flag for Larvotto (MC-LA)
🏴󠁬󠁹󠁮󠁱󠁿 Flag for Nuqat al Khams (LY-NQ)
🏴󠁭󠁣󠁭󠁡󠁿 Flag for Malbousquet (MC-MA)
🏴󠁭󠁡󠀱󠀲󠁿 Flag for Tadla-Azilal (MA-12)
🏴󠁭󠁡󠀰󠀸󠁿 Flag for Grand Casablanca (MA-08)
🏴󠁭󠁡󠀰󠀵󠁿 Flag for Fès-Boulemane (MA-05)
🏴󠁭󠁡󠀰󠀹󠁿 Flag for Chaouia-Ouardigha (MA-09)
🏴󠁭󠁣󠁭󠁧󠁿 Flag for Moneghetti (MC-MG)
🏴󠁬󠁹󠁭󠁱󠁿 Flag for Murzuq (LY-MQ)
🏴󠁭󠁡󠀰󠀶󠁿 Flag for Meknès-Tafilalet (MA-06)
🏴󠁬󠁹󠁷󠁤󠁿 Flag for Wadi al Hayaa (LY-WD)
🏴󠁭󠁣󠁣󠁬󠁿 Flag for La Colle (MC-CL)
🏴󠁬󠁹󠁳󠁲󠁿 Flag for Sirte (LY-SR)
🏴󠁬󠁹󠁭󠁩󠁿 Flag for Misrata (LY-MI)
🏴󠁭󠁣󠁧󠁡󠁿 Flag for La Gare (MC-GA)
🏴󠁭󠁣󠁳󠁯󠁿 Flag for La Source (MC-SO)
🏴󠁭󠁣󠁭󠁵󠁿 Flag for Moulins (MC-MU)
🏴󠁭󠁤󠁥󠁤󠁿 Flag for Edineț (MD-ED)
🏴󠁭󠁤󠁨󠁩󠁿 Flag for Hîncești (MD-HI)
🏴󠁭󠁣󠁶󠁲󠁿 Flag for Vallon de la Rousse (MC-VR)
🏴󠁭󠁤󠁣󠁲󠁿 Flag for Criuleni (MD-CR)
🏴󠁭󠁤󠁳󠁩󠁿 Flag for Sîngerei (MD-SI)
🏴󠁭󠁤󠁳󠁯󠁿 Flag for Soroca (MD-SO)
🏴󠁭󠁤󠁣󠁴󠁿 Flag for Cantemir (MD-CT)
🏴󠁭󠁤󠁦󠁡󠁿 Flag for Fălești (MD-FA)
🏴󠁭󠁤󠁳󠁤󠁿 Flag for Șoldănești (MD-SD)
🏴󠁭󠁤󠁢󠁲󠁿 Flag for Briceni (MD-BR)
🏴󠁭󠁣󠁳󠁰󠁿 Flag for Spélugues (MC-SP)
🏴󠁭󠁤󠁢󠁡󠁿 Flag for Bălţi (MD-BA)
🏴󠁭󠁤󠁤󠁵󠁿 Flag for Dubăsari (MD-DU)
🏴󠁭󠁤󠁣󠁬󠁿 Flag for Călărași (MD-CL)
🏴󠁭󠁤󠁣󠁡󠁿 Flag for Cahul (MD-CA)
🏴󠁭󠁤󠁧󠁡󠁿 Flag for Gagauzia (MD-GA)
🏴󠁭󠁤󠁯󠁲󠁿 Flag for Orhei (MD-OR)
🏴󠁭󠁤󠁤󠁲󠁿 Flag for Drochia (MD-DR)
🏴󠁭󠁣󠁰󠁨󠁿 Flag for Port Hercules (MC-PH)
🏴󠁭󠁤󠁣󠁭󠁿 Flag for Cimișlia (MD-CM)
🏴󠁭󠁤󠁯󠁣󠁿 Flag for Ocniţa (MD-OC)
🏴󠁭󠁤󠁢󠁳󠁿 Flag for Basarabeasca (MD-BS)
🏴󠁭󠁤󠁳󠁴󠁿 Flag for Strășeni (MD-ST)
🏴󠁭󠁤󠁡󠁮󠁿 Flag for Anenii Noi (MD-AN)
🏴󠁭󠁤󠁩󠁡󠁿 Flag for Ialoveni (MD-IA)
🏴󠁭󠁤󠁢󠁤󠁿 Flag for Bender (MD-BD)
🏴󠁭󠁤󠁧󠁬󠁿 Flag for Glodeni (MD-GL)
🏴󠁭󠁤󠁤󠁯󠁿 Flag for Dondușeni (MD-DO)
🏴󠁭󠁤󠁲󠁥󠁿 Flag for Rezina (MD-RE)
🏴󠁭󠁤󠁣󠁵󠁿 Flag for Chișinău (MD-CU)
🏴󠁭󠁤󠁮󠁩󠁿 Flag for Nisporeni (MD-NI)
🏴󠁭󠁤󠁦󠁬󠁿 Flag for Florești (MD-FL)
👩🏾‍👩🏾‍👦🏾 Family - Woman: Medium-Dark Skin Tone, Woman: Medium-Dark Skin Tone, Boy: Medium-Dark Skin Tone
🏴󠁭󠁤󠁲󠁩󠁿 Flag for Rîșcani (MD-RI)
🏴󠁭󠁤󠁬󠁥󠁿 Flag for Leova (MD-LE)
🏴󠁭󠁤󠁳󠁶󠁿 Flag for Ştefan Vodă (MD-SV)
🏴󠁭󠁤󠁵󠁮󠁿 Flag for Ungheni (MD-UN)
🏴󠁭󠁧󠁡󠁿 Flag for Toamasina (MG-A)
🏴󠁭󠁧󠁴󠁿 Flag for Antananarivo (MG-T)
🏴󠁭󠁧󠁭󠁿 Flag for Mahajanga (MG-M)
🏴󠁭󠁥󠀲󠀳󠁿 Flag for Petnjica (ME-23)
🏴󠁭󠁫󠀰󠀵󠁿 Flag for Bogdanci (MK-05)
🏴󠁭󠁥󠀲󠀰󠁿 Flag for Ulcinj (ME-20)
🏴󠁭󠁥󠀰󠀸󠁿 Flag for Herceg Novi (ME-08)
🏴󠁭󠁫󠀰󠀷󠁿 Flag for Bosilovo (MK-07)
🏴󠁭󠁥󠀰󠀹󠁿 Flag for Kolašin (ME-09)
🏴󠁭󠁤󠁴󠁥󠁿 Flag for Telenești (MD-TE)
🏴󠁭󠁫󠀰󠀶󠁿 Flag for Bogovinje (MK-06)
🏴󠁭󠁥󠀲󠀱󠁿 Flag for Žabljak (ME-21)
🏴󠁭󠁥󠀱󠀶󠁿 Flag for Podgorica (ME-16)
🏴󠁭󠁥󠀱󠀷󠁿 Flag for Rožaje (ME-17)
🏴󠁭󠁥󠀰󠀵󠁿 Flag for Budva (ME-05)
🏴󠁭󠁥󠀰󠀲󠁿 Flag for Bar (ME-02)
🏴󠁭󠁫󠀰󠀳󠁿 Flag for Berovo (MK-03)
🏴󠁭󠁥󠀱󠀹󠁿 Flag for Tivat (ME-19)
🏴󠁭󠁥󠀱󠀰󠁿 Flag for Kotor (ME-10)
🏴󠁭󠁨󠁬󠁿 Flag for Ralik Chain (MH-L)
🏴󠁭󠁥󠀰󠀷󠁿 Flag for Danilovgrad (ME-07)
🏴󠁭󠁥󠀱󠀳󠁿 Flag for Plav (ME-13)
🏴󠁭󠁫󠀰󠀴󠁿 Flag for Bitola (MK-04)
🏴󠁭󠁥󠀰󠀴󠁿 Flag for Bijelo Polje (ME-04)
🏴󠁭󠁥󠀰󠀱󠁿 Flag for Andrijevica (ME-01)
🏴󠁭󠁥󠀱󠀲󠁿 Flag for Nikšić (ME-12)
🏴󠁭󠁤󠁴󠁡󠁿 Flag for Taraclia (MD-TA)
🏴󠁭󠁥󠀱󠀱󠁿 Flag for Mojkovac (ME-11)
🏴󠁭󠁥󠀱󠀴󠁿 Flag for Pljevlja (ME-14)
🏴󠁭󠁥󠀱󠀵󠁿 Flag for Plužine (ME-15)
🏴󠁭󠁥󠀲󠀲󠁿 Flag for Gusinje (ME-22)
🏴󠁭󠁧󠁦󠁿 Flag for Fianarantsoa (MG-F)
🏴󠁭󠁥󠀱󠀸󠁿 Flag for Šavnik (ME-18)
🏴󠁭󠁥󠀰󠀶󠁿 Flag for Cetinje (ME-06)
🏴󠁭󠁧󠁵󠁿 Flag for Toliara (MG-U)
🏴󠁭󠁧󠁤󠁿 Flag for Antsiranana (MG-D)
🏴󠁭󠁫󠀵󠀴󠁿 Flag for Negotino (MK-54)
🏴󠁭󠁫󠀴󠀳󠁿 Flag for Kratovo (MK-43)
🏴󠁭󠁫󠀴󠀴󠁿 Flag for Kriva Palanka (MK-44)
🏴󠁭󠁫󠀴󠀲󠁿 Flag for Kočani (MK-42)
🏴󠁭󠁫󠀳󠀵󠁿 Flag for Jegunovce (MK-35)
🏴󠁭󠁫󠀳󠀴󠁿 Flag for Ilinden (MK-34)
🏴󠁭󠁫󠀴󠀹󠁿 Flag for Lozovo (MK-49)
🏴󠁭󠁫󠀳󠀳󠁿 Flag for Zrnovci (MK-33)
🏴󠁭󠁫󠀱󠀲󠁿 Flag for Vevčani (MK-12)
🏴󠁭󠁫󠀲󠀴󠁿 Flag for Demir Kapija (MK-24)
🏴󠁭󠁫󠀱󠀱󠁿 Flag for Vasilevo (MK-11)
🏴󠁭󠁫󠀳󠀰󠁿 Flag for Želino (MK-30)
🏴󠁭󠁫󠀳󠀶󠁿 Flag for Kavadarci (MK-36)
🏴󠁭󠁫󠀳󠀲󠁿 Flag for Zelenikovo (MK-32)
🏴󠁭󠁫󠀴󠀱󠁿 Flag for Konče (MK-41)
🏴󠁭󠁫󠀱󠀴󠁿 Flag for Vinica (MK-14)
🏴󠁭󠁫󠀱󠀰󠁿 Flag for Valandovo (MK-10)
🏴󠁭󠁫󠀵󠀵󠁿 Flag for Novaci (MK-55)
🏴󠁭󠁫󠀵󠀱󠁿 Flag for Makedonska Kamenica (MK-51)
🏴󠁭󠁫󠀱󠀶󠁿 Flag for Vrapčište (MK-16)
🏴󠁭󠁫󠀲󠀰󠁿 Flag for Gradsko (MK-20)
🏴󠁭󠁫󠀵󠀰󠁿 Flag for Mavrovo and Rostuša (MK-50)
🏴󠁭󠁫󠀲󠀲󠁿 Flag for Debarca (MK-22)
🏴󠁭󠁫󠀱󠀹󠁿 Flag for Gostivar (MK-19)
🏴󠁭󠁫󠀵󠀳󠁿 Flag for Mogila (MK-53)
🏴󠁭󠁫󠀵󠀶󠁿 Flag for Novo Selo (MK-56)
🏴󠁭󠁫󠀴󠀸󠁿 Flag for Lipkovo (MK-48)
🏴󠁭󠁫󠀳󠀷󠁿 Flag for Karbinci (MK-37)
🏴󠁭󠁫󠀴󠀷󠁿 Flag for Kumanovo (MK-47)
🏴󠁭󠁫󠀲󠀱󠁿 Flag for Debar (MK-21)
🏴󠁭󠁫󠀴󠀰󠁿 Flag for Kičevo (MK-40)
🏴󠁭󠁫󠀱󠀳󠁿 Flag for Veles (MK-13)
🏴󠁭󠁫󠀲󠀶󠁿 Flag for Dojran (MK-26)
🏴󠁭󠁫󠀰󠀸󠁿 Flag for Brvenica (MK-08)
🏴󠁭󠁫󠀵󠀲󠁿 Flag for Makedonski Brod (MK-52)
🏴󠁭󠁫󠀴󠀵󠁿 Flag for Krivogaštani (MK-45)
🏴󠁭󠁫󠀲󠀳󠁿 Flag for Delčevo (MK-23)
🏴󠁭󠁫󠀴󠀶󠁿 Flag for Kruševo (MK-46)
🏴󠁭󠁫󠀱󠀸󠁿 Flag for Gevgelija (MK-18)
🏴󠁭󠁫󠀵󠀸󠁿 Flag for Ohrid (MK-58)
🏴󠁭󠁫󠀶󠀶󠁿 Flag for Resen (MK-66)
🏴󠁭󠁭󠀰󠀴󠁿 Flag for Mandalay (MM-04)
🏴󠁭󠁫󠀶󠀵󠁿 Flag for Rankovce (MK-65)
🏴󠁭󠁫󠀵󠀹󠁿 Flag for Petrovec (MK-59)
🏴󠁭󠁭󠀰󠀲󠁿 Flag for Bago (MM-02)
🏴󠁭󠁫󠀸󠀱󠁿 Flag for Češinovo-Obleševo (MK-81)
🏴󠁭󠁫󠀷󠀲󠁿 Flag for Struga (MK-72)
🏴󠁭󠁫󠀸󠀲󠁿 Flag for Čučer-Sandevo (MK-82)
🏴󠁭󠁫󠀷󠀶󠁿 Flag for Tetovo (MK-76)
🏴󠁭󠁫󠀷󠀴󠁿 Flag for Studeničani (MK-74)
🏴󠁭󠁫󠀶󠀹󠁿 Flag for Sveti Nikole (MK-69)
🏴󠁭󠁫󠀷󠀳󠁿 Flag for Strumica (MK-73)
🏴󠁭󠁬󠀵󠁿 Flag for Mopti (ML-5)
🏴󠁭󠁫󠀷󠀰󠁿 Flag for Sopište (MK-70)
🏴󠁭󠁬󠀳󠁿 Flag for Sikasso (ML-3)
🏴󠁭󠁭󠀱󠀱󠁿 Flag for Kachin (MM-11)
🏴󠁭󠁫󠀷󠀸󠁿 Flag for Centar Župa (MK-78)
🏴󠁭󠁬󠁢󠁫󠁯󠁿 Flag for Bamako (ML-BKO)
🏴󠁭󠁭󠀰󠀳󠁿 Flag for Magway (MM-03)
🏴󠁭󠁫󠀶󠀲󠁿 Flag for Prilep (MK-62)
🏴󠁭󠁫󠀷󠀱󠁿 Flag for Staro Nagoričane (MK-71)
🏴󠁭󠁭󠀰󠀷󠁿 Flag for Ayeyarwady (MM-07)
🏴󠁭󠁬󠀷󠁿 Flag for Gao (ML-7)
🏴󠁭󠁫󠀸󠀳󠁿 Flag for Štip (MK-83)
🏴󠁭󠁭󠀱󠀲󠁿 Flag for Kayah (MM-12)
🏴󠁭󠁭󠀰󠀵󠁿 Flag for Tanintharyi (MM-05)
🏴󠁭󠁬󠀲󠁿 Flag for Koulikoro (ML-2)
🏴󠁭󠁫󠀶󠀳󠁿 Flag for Probištip (MK-63)
🏴󠁭󠁫󠀶󠀰󠁿 Flag for Pehčevo (MK-60)
🏴󠁭󠁬󠀴󠁿 Flag for Ségou (ML-4)
🏴󠁭󠁭󠀰󠀱󠁿 Flag for Sagaing (MM-01)
🏴󠁭󠁫󠀸󠀰󠁿 Flag for Čaška (MK-80)
🏴󠁭󠁭󠀰󠀶󠁿 Flag for Yangon (MM-06)
🏴󠁭󠁫󠀶󠀷󠁿 Flag for Rosoman (MK-67)
🏴󠁭󠁲󠀰󠀳󠁿 Flag for Assaba (MR-03)
🏴󠁭󠁮󠀰󠀵󠀳󠁿 Flag for Ömnögovi (MN-053)
🏴󠁭󠁮󠀰󠀴󠀱󠁿 Flag for Khövsgöl (MN-041)
🏴󠁭󠁮󠀰󠀶󠀹󠁿 Flag for Bayankhongor (MN-069)
🏴󠁭󠁭󠀱󠀳󠁿 Flag for Kayin (MM-13)
🏴󠁭󠁮󠀰󠀵󠀱󠁿 Flag for Sükhbaatar (MN-051)
🏴󠁭󠁮󠀰󠀶󠀱󠁿 Flag for Dornod (MN-061)
🏴󠁭󠁮󠀰󠀴󠀹󠁿 Flag for Selenge (MN-049)
🏴󠁭󠁮󠀰󠀳󠀷󠁿 Flag for Darkhan-Uul (MN-037)
🏴󠁭󠁮󠀱󠁿 Flag for Ulaanbaatar (MN-1)
🏴󠁭󠁮󠀰󠀷󠀱󠁿 Flag for Bayan-Ölgii (MN-071)
🏴󠁭󠁲󠀰󠀶󠁿 Flag for Trarza (MR-06)
󠀤 Tag Dollar Sign
🏴󠁭󠁲󠀰󠀴󠁿 Flag for Gorgol (MR-04)
🏴󠁭󠁮󠀰󠀵󠀵󠁿 Flag for Övörkhangai (MN-055)
🏴󠁭󠁮󠀰󠀴󠀶󠁿 Flag for Uvs (MN-046)
🏴󠁭󠁭󠀱󠀴󠁿 Flag for Chin (MM-14)
🏴󠁭󠁮󠀰󠀶󠀷󠁿 Flag for Bulgan (MN-067)
🏴󠁭󠁮󠀰󠀴󠀷󠁿 Flag for Töv (MN-047)
🏴󠁭󠁮󠀰󠀵󠀷󠁿 Flag for Zavkhan (MN-057)
🏴󠁭󠁮󠀰󠀶󠀳󠁿 Flag for Dornogovi (MN-063)
🏴󠁥󠁳󠁧󠁡󠁿 Flag for Galicia (ES-GA)
󠁾 Tag Tilde
🏴󠁭󠁮󠀰󠀶󠀵󠁿 Flag for Govi-Altai (MN-065)
🏴󠁭󠁲󠀱󠀱󠁿 Flag for Tiris Zemmour (MR-11)
🏴󠁭󠁮󠀰󠀵󠀹󠁿 Flag for Dundgovi (MN-059)
🏴󠁭󠁮󠀰󠀷󠀳󠁿 Flag for Arkhangai (MN-073)
🏴󠁭󠁭󠀱󠀶󠁿 Flag for Rakhine (MM-16)
🏴󠁭󠁲󠀰󠀵󠁿 Flag for Brakna (MR-05)
🏴󠁭󠁲󠀰󠀸󠁿 Flag for Dakhlet Nouadhibou (MR-08)
🏴󠁭󠁲󠀰󠀱󠁿 Flag for Hodh Ech Chargui (MR-01)
🏴󠁭󠁮󠀰󠀳󠀵󠁿 Flag for Orkhon (MN-035)
🏴󠁭󠁲󠀰󠀲󠁿 Flag for Hodh El Gharbi (MR-02)
🏴󠁭󠁭󠀱󠀸󠁿 Flag for Naypyidaw (MM-18)
🏴󠁭󠁲󠀰󠀹󠁿 Flag for Tagant (MR-09)
🏴󠁭󠁮󠀰󠀴󠀳󠁿 Flag for Khovd (MN-043)
🏴󠁭󠁲󠀱󠀲󠁿 Flag for Inchiri (MR-12)
🏴󠁭󠁴󠀱󠀹󠁿 Flag for Iklin (MT-19)
🏴󠁭󠁴󠀱󠀴󠁿 Flag for Għarb (MT-14)
🏴󠁭󠁴󠀳󠀳󠁿 Flag for Mqabba (MT-33)
🏴󠁭󠁴󠀲󠀲󠁿 Flag for Kerċem (MT-22)
🏴󠁭󠁴󠀱󠀶󠁿 Flag for Għasri (MT-16)
🏴󠁭󠁴󠀲󠀴󠁿 Flag for Lija (MT-24)
🏴󠁭󠁴󠀰󠀵󠁿 Flag for Birżebbuġa (MT-05)
🏴󠁭󠁴󠀰󠀴󠁿 Flag for Birkirkara (MT-04)
🏴󠁭󠁴󠀳󠀱󠁿 Flag for Mġarr (MT-31)
🏴󠁭󠁴󠀰󠀲󠁿 Flag for Balzan (MT-02)
🏴󠁭󠁴󠀳󠀶󠁿 Flag for Munxar (MT-36)
🏴󠁭󠁴󠀱󠀳󠁿 Flag for Għajnsielem (MT-13)
🏴󠁭󠁴󠀳󠀸󠁿 Flag for Naxxar (MT-38)
🏴󠁭󠁴󠀰󠀹󠁿 Flag for Floriana (MT-09)
🏴󠁭󠁴󠀲󠀶󠁿 Flag for Marsa (MT-26)
🏴󠁭󠁴󠀰󠀷󠁿 Flag for Dingli (MT-07)
🏴󠁣󠁡󠁮󠁳󠁿 Flag for Nova Scotia (CA-NS)
🏴󠁭󠁴󠀱󠀱󠁿 Flag for Gudja (MT-11)
🏴󠁭󠁴󠀲󠀳󠁿 Flag for Kirkop (MT-23)
🏴󠁭󠁴󠀲󠀷󠁿 Flag for Marsaskala (MT-27)
🏴󠁭󠁴󠀳󠀹󠁿 Flag for Paola (MT-39)
🏴󠁭󠁴󠀱󠀰󠁿 Flag for Fontana (MT-10)
🏴󠁭󠁴󠀳󠀴󠁿 Flag for Msida (MT-34)
🏴󠁭󠁴󠀳󠀷󠁿 Flag for Nadur (MT-37)
🏴󠁭󠁴󠀳󠀲󠁿 Flag for Mosta (MT-32)
🏴󠁭󠁴󠀳󠀵󠁿 Flag for Imtarfa (MT-35)
🏴󠁭󠁴󠀰󠀶󠁿 Flag for Cospicua (MT-06)
🏴󠁭󠁴󠀰󠀳󠁿 Flag for Birgu (MT-03)
🏴󠁭󠁲󠀱󠀴󠁿 Flag for Nouakchott Nord (MR-14)
🏴󠁭󠁴󠀱󠀲󠁿 Flag for Gżira (MT-12)
🏴󠁭󠁴󠀳󠀰󠁿 Flag for Mellieħa (MT-30)
🏴󠁭󠁴󠀱󠀷󠁿 Flag for Għaxaq (MT-17)
🏴󠁭󠁴󠀲󠀱󠁿 Flag for Kalkara (MT-21)
🏴󠁭󠁴󠀰󠀸󠁿 Flag for Fgura (MT-08)
🏴󠁭󠁴󠀰󠀱󠁿 Flag for Attard (MT-01)
🏴󠁭󠁴󠀱󠀵󠁿 Flag for Għargħur (MT-15)
🏴󠁭󠁴󠀱󠀸󠁿 Flag for Ħamrun (MT-18)
🏴󠁭󠁲󠀱󠀵󠁿 Flag for Nouakchott Sud (MR-15)
🏴󠁭󠁴󠀲󠀸󠁿 Flag for Marsaxlokk (MT-28)
🏴󠁭󠁭󠀱󠀵󠁿 Flag for Mon (MM-15)
🏴󠁭󠁴󠀴󠀱󠁿 Flag for Pietà (MT-41)
🏴󠁭󠁴󠀴󠀲󠁿 Flag for Qala (MT-42)
🏴󠁭󠁵󠁰󠁵󠁿 Flag for Port Louis (MU-PU)
🏴󠁭󠁵󠁡󠁧󠁿 Flag for Agaléga (MU-AG)
🏴󠁭󠁴󠀵󠀸󠁿 Flag for Ta’ Xbiex (MT-58)
🏴󠁭󠁵󠁧󠁰󠁿 Flag for Grand Port (MU-GP)
🏴󠁭󠁴󠀶󠀴󠁿 Flag for Żabbar (MT-64)
🏴󠁭󠁴󠀵󠀲󠁿 Flag for Sannat (MT-52)
🏴󠁭󠁴󠀴󠀷󠁿 Flag for Safi (MT-47)
🏴󠁭󠁴󠀶󠀱󠁿 Flag for Xagħra (MT-61)
🏴󠁭󠁵󠁢󠁬󠁿 Flag for Rivière Noire (MU-BL)
🏴󠁭󠁴󠀵󠀶󠁿 Flag for Sliema (MT-56)
🏴󠁭󠁴󠀴󠀴󠁿 Flag for Qrendi (MT-44)
🏴󠁭󠁵󠁦󠁬󠁿 Flag for Flacq (MU-FL)
🏴󠁭󠁴󠀴󠀰󠁿 Flag for Pembroke (MT-40)
🏴󠁭󠁴󠀵󠀷󠁿 Flag for Swieqi (MT-57)
🏴󠁭󠁴󠀶󠀸󠁿 Flag for Żurrieq (MT-68)
🏴󠁭󠁴󠀴󠀹󠁿 Flag for San Ġwann (MT-49)
󠁔 Tag Latin Capital Letter T
🏴󠁭󠁴󠀶󠀳󠁿 Flag for Xgħajra (MT-63)
🏴󠁭󠁴󠀶󠀰󠁿 Flag for Valletta (MT-60)
🏴󠁭󠁵󠁰󠁡󠁿 Flag for Pamplemousses (MU-PA)
🏴󠁭󠁴󠀴󠀳󠁿 Flag for Qormi (MT-43)
🏴󠁭󠁴󠀵󠀰󠁿 Flag for Saint Lawrence (MT-50)
🏴󠁭󠁴󠀵󠀹󠁿 Flag for Tarxien (MT-59)
🏴󠁭󠁵󠁰󠁬󠁿 Flag for Port Louis District (MU-PL)
🏴󠁭󠁵󠁣󠁵󠁿 Flag for Curepipe (MU-CU)
🏴󠁭󠁴󠀶󠀷󠁿 Flag for Żejtun (MT-67)
🏴󠁭󠁴󠀵󠀱󠁿 Flag for St. Paul’s Bay (MT-51)
🏴󠁭󠁵󠁭󠁯󠁿 Flag for Moka (MU-MO)
🏴󠁭󠁴󠀵󠀳󠁿 Flag for Santa Luċija (MT-53)
🏴󠁭󠁴󠀶󠀶󠁿 Flag for Żebbuġ (MT-66)
🏴󠁭󠁴󠀴󠀶󠁿 Flag for Rabat (MT-46)
🏴󠁭󠁴󠀵󠀵󠁿 Flag for Siġġiewi (MT-55)
👩🏽‍👩🏽‍👧🏽 Family - Woman: Medium Skin Tone, Woman: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁭󠁵󠁣󠁣󠁿 Flag for Cargados Carajos (MU-CC)
🏴󠁭󠁴󠀵󠀴󠁿 Flag for Santa Venera (MT-54)
🏴󠁭󠁴󠀴󠀵󠁿 Flag for Victoria (MT-45)
󠀮 Tag Full Stop
🏴󠁭󠁵󠁱󠁢󠁿 Flag for Quatre Bornes (MU-QB)
🏴󠁭󠁸󠁯󠁡󠁸󠁿 Flag for Oaxaca (MX-OAX)
🏴󠁭󠁸󠁮󠁬󠁥󠁿 Flag for Nuevo León (MX-NLE)
🏴󠁭󠁸󠁧󠁵󠁡󠁿 Flag for Guanajuato (MX-GUA)
🏴󠁭󠁷󠁳󠁿 Flag for Southern (MW-S)
🏴󠁭󠁵󠁶󠁰󠁿 Flag for Vacoas-Phoenix (MU-VP)
🏴󠁩󠁲󠀱󠀸󠁿 Flag for Kohgiluyeh and Boyer-Ahmad (IR-18)
🏴󠁭󠁷󠁣󠁿 Flag for Central (MW-C)
🏴󠁭󠁵󠁳󠁡󠁿 Flag for Savanne (MU-SA)
🏴󠁭󠁸󠁨󠁩󠁤󠁿 Flag for Hidalgo (MX-HID)
🏴󠁭󠁸󠁰󠁵󠁥󠁿 Flag for Puebla (MX-PUE)
🏴󠁭󠁸󠁣󠁡󠁭󠁿 Flag for Campeche (MX-CAM)
🏴󠁭󠁸󠁭󠁯󠁲󠁿 Flag for Morelos (MX-MOR)
🏴󠁭󠁸󠁣󠁯󠁡󠁿 Flag for Coahuila (MX-COA)
🏴󠁭󠁸󠁣󠁯󠁬󠁿 Flag for Colima (MX-COL)
🏴󠁭󠁶󠁭󠁬󠁥󠁿 Flag for Malé (MV-MLE)
🏴󠁭󠁷󠁮󠁿 Flag for Northern (MW-N)
🏴󠁩󠁥󠁭󠁿 Flag for Munster (IE-M)
👨🏽‍👧🏽‍👧🏽 Family - Man: Medium Skin Tone, Girl: Medium Skin Tone, Girl: Medium Skin Tone
🏴󠁭󠁸󠁭󠁩󠁣󠁿 Flag for Michoacán (MX-MIC)
👨🏻‍👨🏻‍👦🏻‍👧🏻 Family - Man: Light Skin Tone, Man: Light Skin Tone, Boy: Light Skin Tone, Girl: Light Skin Tone
󠀭 Tag Hyphen-Minus
🏴󠁭󠁶󠁣󠁥󠁿 Flag for Central Province (MV-CE)
🏴󠁭󠁶󠁳󠁵󠁿 Flag for South Province (MV-SU)
🏴󠁭󠁵󠁰󠁷󠁿 Flag for Plaines Wilhems (MU-PW)
🏴󠁭󠁶󠁵󠁮󠁿 Flag for Upper North Province (MV-UN)
🏴󠁭󠁵󠁲󠁯󠁿 Flag for Rodrigues (MU-RO)
🏴󠁭󠁸󠁺󠁡󠁣󠁿 Flag for Zacatecas (MX-ZAC)
🏴󠁭󠁸󠁳󠁩󠁮󠁿 Flag for Sinaloa (MX-SIN)
🏴󠁭󠁹󠀱󠀱󠁿 Flag for Terengganu (MY-11)
🏴󠁭󠁸󠁶󠁥󠁲󠁿 Flag for Veracruz (MX-VER)
👩🏽‍❤️‍👩 Couple With Heart - Woman: Medium Skin Tone, Woman
🏴󠁭󠁺󠁢󠁿 Flag for Manica (MZ-B)
🏴󠁥󠁳󠁣󠁴󠁿 Flag for Catalonia (ES-CT)
🏴󠁭󠁹󠀰󠀹󠁿 Flag for Perlis (MY-09)
🏴󠁭󠁺󠁱󠁿 Flag for Zambezia (MZ-Q)
🏴󠁮󠁡󠁥󠁲󠁿 Flag for Erongo (NA-ER)
🏴󠁭󠁹󠀱󠀵󠁿 Flag for Labuan (MY-15)
🏴󠁭󠁹󠀰󠀸󠁿 Flag for Perak (MY-08)
🏴󠁭󠁺󠁬󠁿 Flag for Maputo Province (MZ-L)
🏴󠁭󠁸󠁱󠁵󠁥󠁿 Flag for Querétaro (MX-QUE)
󠁀 Tag Commercial at
🏴󠁭󠁺󠁩󠁿 Flag for Inhambane (MZ-I)
🏴󠁭󠁹󠀰󠀴󠁿 Flag for Malacca (MY-04)
🏴󠁭󠁺󠁰󠁿 Flag for Cabo Delgado (MZ-P)
🏴󠁭󠁸󠁴󠁬󠁡󠁿 Flag for Tlaxcala (MX-TLA)
󠁠 Tag Grave Accent
🏴󠁭󠁸󠁴󠁡󠁭󠁿 Flag for Tamaulipas (MX-TAM)
🏴󠁮󠁡󠁣󠁡󠁿 Flag for Zambezi (NA-CA)
🏴󠁭󠁺󠁳󠁿 Flag for Sofala (MZ-S)
🏴󠁭󠁹󠀰󠀲󠁿 Flag for Kedah (MY-02)
🏴󠁭󠁺󠁡󠁿 Flag for Niassa (MZ-A)
🏴󠁭󠁺󠁭󠁰󠁭󠁿 Flag for Maputo (MZ-MPM)
🏴󠁭󠁺󠁮󠁿 Flag for Nampula (MZ-N)
🏴󠁭󠁹󠀱󠀶󠁿 Flag for Putrajaya (MY-16)
🏴󠁭󠁺󠁧󠁿 Flag for Gaza (MZ-G)
🏴󠁭󠁸󠁹󠁵󠁣󠁿 Flag for Yucatán (MX-YUC)
🏴󠁭󠁺󠁴󠁿 Flag for Tete (MZ-T)
🏴󠁭󠁹󠀰󠀵󠁿 Flag for Negeri Sembilan (MY-05)
🏴󠁮󠁡󠁨󠁡󠁿 Flag for Hardap (NA-HA)
🏴󠁭󠁹󠀱󠀳󠁿 Flag for Sarawak (MY-13)
🏴󠁮󠁡󠁯󠁤󠁿 Flag for Otjozondjupa (NA-OD)
🏴󠁮󠁥󠀴󠁿 Flag for Maradi (NE-4)
🏴󠁮󠁡󠁯󠁷󠁿 Flag for Ohangwena (NA-OW)
🏴󠁮󠁥󠀵󠁿 Flag for Tahoua (NE-5)
🏴󠁮󠁧󠁥󠁢󠁿 Flag for Ebonyi (NG-EB)
🏴󠁭󠁵󠁲󠁲󠁿 Flag for Rivière du Rempart (MU-RR)
🏴󠁮󠁥󠀱󠁿 Flag for Agadez (NE-1)
🏴󠁮󠁧󠁥󠁤󠁿 Flag for Edo (NG-ED)
🏴󠁮󠁧󠁫󠁴󠁿 Flag for Katsina (NG-KT)
🏴󠁮󠁥󠀳󠁿 Flag for Dosso (NE-3)
🏴󠁮󠁥󠀶󠁿 Flag for Tillabéri (NE-6)
🏴󠁮󠁧󠁫󠁤󠁿 Flag for Kaduna (NG-KD)
🏴󠁮󠁧󠁥󠁫󠁿 Flag for Ekiti (NG-EK)
🏴󠁮󠁡󠁯󠁨󠁿 Flag for Omaheke (NA-OH)
🏴󠁮󠁧󠁫󠁯󠁿 Flag for Kogi (NG-KO)
🏴󠁮󠁧󠁢󠁡󠁿 Flag for Bauchi (NG-BA)
🏴󠁮󠁡󠁫󠁡󠁿 Flag for Karas (NA-KA)
🏴󠁮󠁧󠁢󠁹󠁿 Flag for Bayelsa (NG-BY)
🏴󠁮󠁧󠁪󠁩󠁿 Flag for Jigawa (NG-JI)
🏴󠁮󠁧󠁢󠁥󠁿 Flag for Benue (NG-BE)
🏴󠁮󠁥󠀷󠁿 Flag for Zinder (NE-7)
🏴󠁮󠁡󠁯󠁮󠁿 Flag for Oshana (NA-ON)
👨🏻‍👶🏻‍👦🏻 Family - Man: Light Skin Tone, Baby: Light Skin Tone, Boy: Light Skin Tone
🏴󠁫󠁺󠁢󠁡󠁹󠁿 Flag for Bayqongyr (KZ-BAY)
🏴󠁮󠁧󠁫󠁥󠁿 Flag for Kebbi (NG-KE)
"""

rofi = Popen(
    args=[
        'rofi',
        '-dmenu',
        '-i',
        '-p',
        ' 😀  ',
        '-kb-custom-1',
        'Alt+c',
        '--theme-str "configuration {font: \"EmojiOne Color Regular 24";}"'
    ],
    stdin=PIPE,
    stdout=PIPE
)
(stdout, stderr) = rofi.communicate(input=emojis.encode('utf-8'))

if rofi.returncode == 1:
    exit()
else:
    emoji = stdout.split()[0]
    if rofi.returncode == 0:
        Popen(
            args=[
                'xdotool',
                'type',
                '--clearmodifiers',
                emoji.decode('utf-8')
            ]
        )
    elif rofi.returncode == 10:
        xsel = Popen(
            args=[
                'xsel',
                '-i',
                '-b'
            ],
            stdin=PIPE
        )
        xsel.communicate(input=emoji)
