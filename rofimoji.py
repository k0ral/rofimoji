#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import sys
from subprocess import Popen, PIPE
from typing import List, Tuple, Union

emoji_list = """😀 grinning face <small>(face, grin, grinning face)</small>
😃 grinning face with big eyes <small>(face, grinning face with big eyes, mouth, open, smile)</small>
😄 grinning face with smiling eyes <small>(eye, face, grinning face with smiling eyes, mouth, open, smile)</small>
😁 beaming face with smiling eyes <small>(beaming face with smiling eyes, eye, face, grin, smile)</small>
😆 grinning squinting face <small>(face, grinning squinting face, laugh, mouth, satisfied, smile)</small>
😅 grinning face with sweat <small>(cold, face, grinning face with sweat, open, smile, sweat)</small>
🤣 rolling on the floor laughing <small>(face, floor, laugh, rolling, rolling on the floor laughing)</small>
😂 face with tears of joy <small>(face, face with tears of joy, joy, laugh, tear)</small>
🙂 slightly smiling face <small>(face, slightly smiling face, smile)</small>
🙃 upside-down face <small>(face, upside-down)</small>
😉 winking face <small>(face, wink, winking face)</small>
😊 smiling face with smiling eyes <small>(blush, eye, face, smile, smiling face with smiling eyes)</small>
😇 smiling face with halo <small>(angel, face, fantasy, halo, innocent, smiling face with halo)</small>
🥰 smiling face with hearts <small>(adore, crush, hearts, in love, smiling face with hearts)</small>
😍 smiling face with heart-eyes <small>(eye, face, love, smile, smiling face with heart-eyes)</small>
🤩 star-struck <small>(eyes, face, grinning, star, star-struck)</small>
😘 face blowing a kiss <small>(face, face blowing a kiss, kiss)</small>
😗 kissing face <small>(face, kiss, kissing face)</small>
☺ smiling face <small>(face, outlined, relaxed, smile, smiling face)</small>
😚 kissing face with closed eyes <small>(closed, eye, face, kiss, kissing face with closed eyes)</small>
😙 kissing face with smiling eyes <small>(eye, face, kiss, kissing face with smiling eyes, smile)</small>
😋 face savoring food <small>(delicious, face, face savoring food, savouring, smile, yum)</small>
😛 face with tongue <small>(face, face with tongue, tongue)</small>
😜 winking face with tongue <small>(eye, face, joke, tongue, wink, winking face with tongue)</small>
🤪 zany face <small>(eye, goofy, large, small, zany face)</small>
😝 squinting face with tongue <small>(eye, face, horrible, squinting face with tongue, taste, tongue)</small>
🤑 money-mouth face <small>(face, money, money-mouth face, mouth)</small>
🤗 hugging face <small>(face, hug, hugging)</small>
🤭 face with hand over mouth <small>(face with hand over mouth, whoops)</small>
🤫 shushing face <small>(quiet, shush, shushing face)</small>
🤔 thinking face <small>(face, thinking)</small>
🤐 zipper-mouth face <small>(face, mouth, zipper, zipper-mouth face)</small>
🤨 face with raised eyebrow <small>(distrust, face with raised eyebrow, skeptic)</small>
😐 neutral face <small>(deadpan, face, meh, neutral)</small>
😑 expressionless face <small>(expressionless, face, inexpressive, meh, unexpressive)</small>
😶 face without mouth <small>(face, face without mouth, mouth, quiet, silent)</small>
😏 smirking face <small>(face, smirk, smirking face)</small>
😒 unamused face <small>(face, unamused, unhappy)</small>
🙄 face with rolling eyes <small>(eyeroll, eyes, face, face with rolling eyes, rolling)</small>
😬 grimacing face <small>(face, grimace, grimacing face)</small>
🤥 lying face <small>(face, lie, lying face, pinocchio)</small>
😌 relieved face <small>(face, relieved)</small>
😔 pensive face <small>(dejected, face, pensive)</small>
😪 sleepy face <small>(face, sleep, sleepy face)</small>
🤤 drooling face <small>(drooling, face)</small>
😴 sleeping face <small>(face, sleep, sleeping face, zzz)</small>
😷 face with medical mask <small>(cold, doctor, face, face with medical mask, mask, sick)</small>
🤒 face with thermometer <small>(face, face with thermometer, ill, sick, thermometer)</small>
🤕 face with head-bandage <small>(bandage, face, face with head-bandage, hurt, injury)</small>
🤢 nauseated face <small>(face, nauseated, vomit)</small>
🤮 face vomiting <small>(face vomiting, sick, vomit)</small>
🤧 sneezing face <small>(face, gesundheit, sneeze, sneezing face)</small>
🥵 hot face <small>(feverish, heat stroke, hot, hot face, red-faced, sweating)</small>
🥶 cold face <small>(blue-faced, cold, cold face, freezing, frostbite, icicles)</small>
🥴 woozy face <small>(dizzy, intoxicated, tipsy, uneven eyes, wavy mouth, woozy face)</small>
😵 dizzy face <small>(dizzy, face)</small>
🤯 exploding head <small>(exploding head, shocked)</small>
🤠 cowboy hat face <small>(cowboy, cowgirl, face, hat)</small>
🥳 partying face <small>(celebration, hat, horn, party, partying face)</small>
😎 smiling face with sunglasses <small>(bright, cool, face, smiling face with sunglasses, sun, sunglasses)</small>
🤓 nerd face <small>(face, geek, nerd)</small>
🧐 face with monocle <small>(face with monocle, stuffy)</small>
😕 confused face <small>(confused, face, meh)</small>
😟 worried face <small>(face, worried)</small>
🙁 slightly frowning face <small>(face, frown, slightly frowning face)</small>
☹ frowning face <small>(face, frown, frowning face)</small>
😮 face with open mouth <small>(face, face with open mouth, mouth, open, sympathy)</small>
😯 hushed face <small>(face, hushed, stunned, surprised)</small>
😲 astonished face <small>(astonished, face, shocked, totally)</small>
😳 flushed face <small>(dazed, face, flushed)</small>
🥺 pleading face <small>(begging, mercy, pleading face, puppy eyes)</small>
😦 frowning face with open mouth <small>(face, frown, frowning face with open mouth, mouth, open)</small>
😧 anguished face <small>(anguished, face)</small>
😨 fearful face <small>(face, fear, fearful, scared)</small>
😰 anxious face with sweat <small>(anxious face with sweat, blue, cold, face, rushed, sweat)</small>
😥 sad but relieved face <small>(disappointed, face, relieved, sad but relieved face, whew)</small>
😢 crying face <small>(cry, crying face, face, sad, tear)</small>
😭 loudly crying face <small>(cry, face, loudly crying face, sad, sob, tear)</small>
😱 face screaming in fear <small>(face, face screaming in fear, fear, munch, scared, scream)</small>
😖 confounded face <small>(confounded, face)</small>
😣 persevering face <small>(face, persevere, persevering face)</small>
😞 disappointed face <small>(disappointed, face)</small>
😓 downcast face with sweat <small>(cold, downcast face with sweat, face, sweat)</small>
😩 weary face <small>(face, tired, weary)</small>
😫 tired face <small>(face, tired)</small>
🥱 yawning face <small>(bored, tired, yawn, yawning face)</small>
😤 face with steam from nose <small>(face, face with steam from nose, triumph, won)</small>
😡 pouting face <small>(angry, face, mad, pouting, rage, red)</small>
😠 angry face <small>(angry, face, mad)</small>
🤬 face with symbols on mouth <small>(face with symbols on mouth, swearing)</small>
😈 smiling face with horns <small>(face, fairy tale, fantasy, horns, smile, smiling face with horns)</small>
👿 angry face with horns <small>(angry face with horns, demon, devil, face, fantasy, imp)</small>
💀 skull <small>(death, face, fairy tale, monster, skull)</small>
☠ skull and crossbones <small>(crossbones, death, face, monster, skull, skull and crossbones)</small>
💩 pile of poo <small>(dung, face, monster, pile of poo, poo, poop)</small>
🤡 clown face <small>(clown, face)</small>
👹 ogre <small>(creature, face, fairy tale, fantasy, monster, ogre)</small>
👺 goblin <small>(creature, face, fairy tale, fantasy, goblin, monster)</small>
👻 ghost <small>(creature, face, fairy tale, fantasy, ghost, monster)</small>
👽 alien <small>(alien, creature, extraterrestrial, face, fantasy, ufo)</small>
👾 alien monster <small>(alien, creature, extraterrestrial, face, monster, ufo)</small>
🤖 robot <small>(face, monster, robot)</small>
😺 grinning cat <small>(cat, face, grinning, mouth, open, smile)</small>
😸 grinning cat with smiling eyes <small>(cat, eye, face, grin, grinning cat with smiling eyes, smile)</small>
😹 cat with tears of joy <small>(cat, cat with tears of joy, face, joy, tear)</small>
😻 smiling cat with heart-eyes <small>(cat, eye, face, heart, love, smile, smiling cat with heart-eyes)</small>
😼 cat with wry smile <small>(cat, cat with wry smile, face, ironic, smile, wry)</small>
😽 kissing cat <small>(cat, eye, face, kiss, kissing cat)</small>
🙀 weary cat <small>(cat, face, oh, surprised, weary)</small>
😿 crying cat <small>(cat, cry, crying cat, face, sad, tear)</small>
😾 pouting cat <small>(cat, face, pouting)</small>
🙈 see-no-evil monkey <small>(evil, face, forbidden, monkey, see, see-no-evil monkey)</small>
🙉 hear-no-evil monkey <small>(evil, face, forbidden, hear, hear-no-evil monkey, monkey)</small>
🙊 speak-no-evil monkey <small>(evil, face, forbidden, monkey, speak, speak-no-evil monkey)</small>
💋 kiss mark <small>(kiss, kiss mark, lips)</small>
💌 love letter <small>(heart, letter, love, mail)</small>
💘 heart with arrow <small>(arrow, cupid, heart with arrow)</small>
💝 heart with ribbon <small>(heart with ribbon, ribbon, valentine)</small>
💖 sparkling heart <small>(excited, sparkle, sparkling heart)</small>
💗 growing heart <small>(excited, growing, growing heart, nervous, pulse)</small>
💓 beating heart <small>(beating, beating heart, heartbeat, pulsating)</small>
💞 revolving hearts <small>(revolving, revolving hearts)</small>
💕 two hearts <small>(love, two hearts)</small>
💟 heart decoration <small>(heart, heart decoration)</small>
❣ heart exclamation <small>(exclamation, heart exclamation, mark, punctuation)</small>
💔 broken heart <small>(break, broken, broken heart)</small>
❤ red heart <small>(heart, red heart)</small>
🧡 orange heart <small>(orange, orange heart)</small>
💛 yellow heart <small>(yellow, yellow heart)</small>
💚 green heart <small>(green, green heart)</small>
💙 blue heart <small>(blue, blue heart)</small>
💜 purple heart <small>(purple, purple heart)</small>
🤎 brown heart <small>(brown, heart)</small>
🖤 black heart <small>(black, black heart, evil, wicked)</small>
🤍 white heart <small>(heart, white)</small>
💯 hundred points <small>(100, full, hundred, hundred points, score)</small>
💢 anger symbol <small>(anger symbol, angry, comic, mad)</small>
💥 collision <small>(boom, collision, comic)</small>
💫 dizzy <small>(comic, dizzy, star)</small>
💦 sweat droplets <small>(comic, splashing, sweat, sweat droplets)</small>
💨 dashing away <small>(comic, dash, dashing away, running)</small>
🕳 hole <small>(hole)</small>
💣 bomb <small>(bomb, comic)</small>
💬 speech balloon <small>(balloon, bubble, comic, dialog, speech)</small>
👁️‍🗨️ eye in speech bubble
🗨 left speech bubble <small>(dialog, left speech bubble, speech)</small>
🗯 right anger bubble <small>(angry, balloon, bubble, mad, right anger bubble)</small>
💭 thought balloon <small>(balloon, bubble, comic, thought)</small>
💤 zzz <small>(comic, sleep, zzz)</small>
👋 waving hand <small>(hand, wave, waving)</small>
🤚 raised back of hand <small>(backhand, raised, raised back of hand)</small>
🖐 hand with fingers splayed <small>(finger, hand, hand with fingers splayed, splayed)</small>
✋ raised hand <small>(hand, raised hand)</small>
🖖 vulcan salute <small>(finger, hand, spock, vulcan, vulcan salute)</small>
👌 OK hand <small>(hand, OK)</small>
🤏 pinching hand <small>(pinching hand, small amount)</small>
✌ victory hand <small>(hand, v, victory)</small>
🤞 crossed fingers <small>(cross, crossed fingers, finger, hand, luck)</small>
🤟 love-you gesture <small>(hand, ILY, love-you gesture)</small>
🤘 sign of the horns <small>(finger, hand, horns, rock-on, sign of the horns)</small>
🤙 call me hand <small>(call, call me hand, hand)</small>
👈 backhand index pointing left <small>(backhand, backhand index pointing left, finger, hand, index, point)</small>
👉 backhand index pointing right <small>(backhand, backhand index pointing right, finger, hand, index, point)</small>
👆 backhand index pointing up <small>(backhand, backhand index pointing up, finger, hand, point, up)</small>
🖕 middle finger <small>(finger, hand, middle finger)</small>
👇 backhand index pointing down <small>(backhand, backhand index pointing down, down, finger, hand, point)</small>
☝ index pointing up <small>(finger, hand, index, index pointing up, point, up)</small>
👍 thumbs up <small>(+1, hand, thumb, thumbs up, up)</small>
👎 thumbs down <small>(-1, down, hand, thumb, thumbs down)</small>
✊ raised fist <small>(clenched, fist, hand, punch, raised fist)</small>
👊 oncoming fist <small>(clenched, fist, hand, oncoming fist, punch)</small>
🤛 left-facing fist <small>(fist, left-facing fist, leftwards)</small>
🤜 right-facing fist <small>(fist, right-facing fist, rightwards)</small>
👏 clapping hands <small>(clap, clapping hands, hand)</small>
🙌 raising hands <small>(celebration, gesture, hand, hooray, raised, raising hands)</small>
👐 open hands <small>(hand, open, open hands)</small>
🤲 palms up together <small>(palms up together, prayer)</small>
🤝 handshake <small>(agreement, hand, handshake, meeting, shake)</small>
🙏 folded hands <small>(ask, folded hands, hand, please, pray, thanks)</small>
✍ writing hand <small>(hand, write, writing hand)</small>
💅 nail polish <small>(care, cosmetics, manicure, nail, polish)</small>
🤳 selfie <small>(camera, phone, selfie)</small>
💪 flexed biceps <small>(biceps, comic, flex, flexed biceps, muscle)</small>
🦾 mechanical arm <small>(accessibility, mechanical arm, prosthetic)</small>
🦿 mechanical leg <small>(accessibility, mechanical leg, prosthetic)</small>
🦵 leg <small>(kick, leg, limb)</small>
🦶 foot <small>(foot, kick, stomp)</small>
👂 ear <small>(body, ear)</small>
🦻 ear with hearing aid <small>(accessibility, ear with hearing aid, hard of hearing)</small>
👃 nose <small>(body, nose)</small>
🧠 brain <small>(brain, intelligent)</small>
🦷 tooth <small>(dentist, tooth)</small>
🦴 bone <small>(bone, skeleton)</small>
👀 eyes <small>(eye, eyes, face)</small>
👁 eye <small>(body, eye)</small>
👅 tongue <small>(body, tongue)</small>
👄 mouth <small>(lips, mouth)</small>
👶 baby <small>(baby, young)</small>
🧒 child <small>(child, gender-neutral, unspecified gender, young)</small>
👦 boy <small>(boy, young)</small>
👧 girl <small>(girl, Virgo, young, zodiac)</small>
🧑 person <small>(adult, gender-neutral, person, unspecified gender)</small>
👱 person: blond hair <small>(blond, blond-haired person, hair, person: blond hair)</small>
👨 man <small>(adult, man)</small>
🧔 man: beard <small>(beard, man, man: beard, person)</small>
👱‍♂️ man: blond hair
👨‍🦰 man: red hair
👨‍🦱 man: curly hair
👨‍🦳 man: white hair
👨‍🦲 man: bald
👩 woman <small>(adult, woman)</small>
👱‍♀️ woman: blond hair
👩‍🦰 woman: red hair
👩‍🦱 woman: curly hair
👩‍🦳 woman: white hair
👩‍🦲 woman: bald
🧓 older person <small>(adult, gender-neutral, old, older person, unspecified gender)</small>
👴 old man <small>(adult, man, old)</small>
👵 old woman <small>(adult, old, woman)</small>
🙍 person frowning <small>(frown, gesture, person frowning)</small>
🙍‍♂️ man frowning
🙍‍♀️ woman frowning
🙎 person pouting <small>(gesture, person pouting, pouting)</small>
🙎‍♂️ man pouting
🙎‍♀️ woman pouting
🙅 person gesturing NO <small>(forbidden, gesture, hand, person gesturing NO, prohibited)</small>
🙅‍♂️ man gesturing NO
🙅‍♀️ woman gesturing NO
🙆 person gesturing OK <small>(gesture, hand, OK, person gesturing OK)</small>
🙆‍♂️ man gesturing OK
🙆‍♀️ woman gesturing OK
💁 person tipping hand <small>(hand, help, information, person tipping hand, sassy, tipping)</small>
💁‍♂️ man tipping hand
💁‍♀️ woman tipping hand
🙋 person raising hand <small>(gesture, hand, happy, person raising hand, raised)</small>
🙋‍♂️ man raising hand
🙋‍♀️ woman raising hand
🧏 deaf person <small>(accessibility, deaf, deaf person, ear, hear)</small>
🧏‍♂️ deaf man
🧏‍♀️ deaf woman
🙇 person bowing <small>(apology, bow, gesture, person bowing, sorry)</small>
🙇‍♂️ man bowing
🙇‍♀️ woman bowing
🤦 person facepalming <small>(disbelief, exasperation, face, palm, person facepalming)</small>
🤦‍♂️ man facepalming
🤦‍♀️ woman facepalming
🤷 person shrugging <small>(doubt, ignorance, indifference, person shrugging, shrug)</small>
🤷‍♂️ man shrugging
🤷‍♀️ woman shrugging
👨‍⚕️ man health worker
👩‍⚕️ woman health worker
👨‍🎓 man student <small>(graduate, man, student)</small>
👩‍🎓 woman student <small>(graduate, student, woman)</small>
👨‍🏫 man teacher <small>(instructor, man, professor, teacher)</small>
👩‍🏫 woman teacher <small>(instructor, professor, teacher, woman)</small>
👨‍⚖️ man judge
👩‍⚖️ woman judge
👨‍🌾 man farmer <small>(farmer, gardener, man, rancher)</small>
👩‍🌾 woman farmer <small>(farmer, gardener, rancher, woman)</small>
👨‍🍳 man cook <small>(chef, cook, man)</small>
👩‍🍳 woman cook <small>(chef, cook, woman)</small>
👨‍🔧 man mechanic <small>(electrician, man, mechanic, plumber, tradesperson)</small>
👩‍🔧 woman mechanic <small>(electrician, mechanic, plumber, tradesperson, woman)</small>
👨‍🏭 man factory worker <small>(assembly, factory, industrial, man, worker)</small>
👩‍🏭 woman factory worker <small>(assembly, factory, industrial, woman, worker)</small>
👨‍💼 man office worker <small>(architect, business, man, man office worker, manager, white-collar)</small>
👩‍💼 woman office worker <small>(architect, business, manager, white-collar, woman, woman office worker)</small>
👨‍🔬 man scientist <small>(biologist, chemist, engineer, man, physicist, scientist)</small>
👩‍🔬 woman scientist <small>(biologist, chemist, engineer, physicist, scientist, woman)</small>
👨‍💻 man technologist <small>(coder, developer, inventor, man, software, technologist)</small>
👩‍💻 woman technologist <small>(coder, developer, inventor, software, technologist, woman)</small>
👨‍🎤 man singer <small>(actor, entertainer, man, rock, singer, star)</small>
👩‍🎤 woman singer <small>(actor, entertainer, rock, singer, star, woman)</small>
👨‍🎨 man artist <small>(artist, man, palette)</small>
👩‍🎨 woman artist <small>(artist, palette, woman)</small>
👨‍✈️ man pilot
👩‍✈️ woman pilot
👨‍🚀 man astronaut <small>(astronaut, man, rocket)</small>
👩‍🚀 woman astronaut <small>(astronaut, rocket, woman)</small>
👨‍🚒 man firefighter <small>(firefighter, firetruck, man)</small>
👩‍🚒 woman firefighter <small>(firefighter, firetruck, woman)</small>
👮 police officer <small>(cop, officer, police)</small>
👮‍♂️ man police officer
👮‍♀️ woman police officer
🕵 detective <small>(detective, sleuth, spy)</small>
🕵️‍♂️ man detective
🕵️‍♀️ woman detective
💂 guard <small>(guard)</small>
💂‍♂️ man guard
💂‍♀️ woman guard
👷 construction worker <small>(construction, hat, worker)</small>
👷‍♂️ man construction worker
👷‍♀️ woman construction worker
🤴 prince <small>(prince)</small>
👸 princess <small>(fairy tale, fantasy, princess)</small>
👳 person wearing turban <small>(person wearing turban, turban)</small>
👳‍♂️ man wearing turban
👳‍♀️ woman wearing turban
👲 man with Chinese cap <small>(gua pi mao, hat, man, man with Chinese cap)</small>
🧕 woman with headscarf <small>(headscarf, hijab, mantilla, tichel, woman with headscarf)</small>
🤵 man in tuxedo <small>(groom, man, man in tuxedo, tuxedo)</small>
👰 bride with veil <small>(bride, bride with veil, veil, wedding)</small>
🤰 pregnant woman <small>(pregnant, woman)</small>
🤱 breast-feeding <small>(baby, breast, breast-feeding, nursing)</small>
👼 baby angel <small>(angel, baby, face, fairy tale, fantasy)</small>
🎅 Santa Claus <small>(celebration, Christmas, claus, father, santa, Santa Claus)</small>
🤶 Mrs. Claus <small>(celebration, Christmas, claus, mother, Mrs., Mrs. Claus)</small>
🦸 superhero <small>(good, hero, heroine, superhero, superpower)</small>
🦸‍♂️ man superhero
🦸‍♀️ woman superhero
🦹 supervillain <small>(criminal, evil, superpower, supervillain, villain)</small>
🦹‍♂️ man supervillain
🦹‍♀️ woman supervillain
🧙 mage <small>(mage, sorcerer, sorceress, witch, wizard)</small>
🧙‍♂️ man mage
🧙‍♀️ woman mage
🧚 fairy <small>(fairy, Oberon, Puck, Titania)</small>
🧚‍♂️ man fairy
🧚‍♀️ woman fairy
🧛 vampire <small>(Dracula, undead, vampire)</small>
🧛‍♂️ man vampire
🧛‍♀️ woman vampire
🧜 merperson <small>(mermaid, merman, merperson, merwoman)</small>
🧜‍♂️ merman
🧜‍♀️ mermaid
🧝 elf <small>(elf, magical)</small>
🧝‍♂️ man elf
🧝‍♀️ woman elf
🧞 genie <small>(djinn, genie)</small>
🧞‍♂️ man genie
🧞‍♀️ woman genie
🧟 zombie <small>(undead, walking dead, zombie)</small>
🧟‍♂️ man zombie
🧟‍♀️ woman zombie
💆 person getting massage <small>(face, massage, person getting massage, salon)</small>
💆‍♂️ man getting massage
💆‍♀️ woman getting massage
💇 person getting haircut <small>(barber, beauty, haircut, parlor, person getting haircut)</small>
💇‍♂️ man getting haircut
💇‍♀️ woman getting haircut
🚶 person walking <small>(hike, person walking, walk, walking)</small>
🚶‍♂️ man walking
🚶‍♀️ woman walking
🧍 person standing <small>(person standing, stand, standing)</small>
🧍‍♂️ man standing
🧍‍♀️ woman standing
🧎 person kneeling <small>(kneel, kneeling, person kneeling)</small>
🧎‍♂️ man kneeling
🧎‍♀️ woman kneeling
👨‍🦯 man with probing cane <small>(accessibility, blind, man, man with probing cane)</small>
👩‍🦯 woman with probing cane <small>(accessibility, blind, woman, woman with probing cane)</small>
👨‍🦼 man in motorized wheelchair <small>(accessibility, man, man in motorized wheelchair, wheelchair)</small>
👩‍🦼 woman in motorized wheelchair <small>(accessibility, wheelchair, woman, woman in motorized wheelchair)</small>
👨‍🦽 man in manual wheelchair <small>(accessibility, man, man in manual wheelchair, wheelchair)</small>
👩‍🦽 woman in manual wheelchair <small>(accessibility, wheelchair, woman, woman in manual wheelchair)</small>
🏃 person running <small>(marathon, person running, running)</small>
🏃‍♂️ man running
🏃‍♀️ woman running
💃 woman dancing <small>(dancing, woman)</small>
🕺 man dancing <small>(dance, man, man dancing)</small>
🕴 man in suit levitating <small>(business, man, man in suit levitating, suit)</small>
👯 people with bunny ears <small>(bunny ear, dancer, partying, people with bunny ears)</small>
👯‍♂️ men with bunny ears
👯‍♀️ women with bunny ears
🧖 person in steamy room <small>(person in steamy room, sauna, steam room)</small>
🧖‍♂️ man in steamy room
🧖‍♀️ woman in steamy room
🧗 person climbing <small>(climber, person climbing)</small>
🧗‍♂️ man climbing
🧗‍♀️ woman climbing
🤺 person fencing <small>(fencer, fencing, person fencing, sword)</small>
🏇 horse racing <small>(horse, jockey, racehorse, racing)</small>
⛷ skier <small>(ski, skier, snow)</small>
🏂 snowboarder <small>(ski, snow, snowboard, snowboarder)</small>
🏌 person golfing <small>(ball, golf, person golfing)</small>
🏌️‍♂️ man golfing
🏌️‍♀️ woman golfing
🏄 person surfing <small>(person surfing, surfing)</small>
🏄‍♂️ man surfing
🏄‍♀️ woman surfing
🚣 person rowing boat <small>(boat, person rowing boat, rowboat)</small>
🚣‍♂️ man rowing boat
🚣‍♀️ woman rowing boat
🏊 person swimming <small>(person swimming, swim)</small>
🏊‍♂️ man swimming
🏊‍♀️ woman swimming
⛹ person bouncing ball <small>(ball, person bouncing ball)</small>
⛹️‍♂️ man bouncing ball
⛹️‍♀️ woman bouncing ball
🏋 person lifting weights <small>(lifter, person lifting weights, weight)</small>
🏋️‍♂️ man lifting weights
🏋️‍♀️ woman lifting weights
🚴 person biking <small>(bicycle, biking, cyclist, person biking)</small>
🚴‍♂️ man biking
🚴‍♀️ woman biking
🚵 person mountain biking <small>(bicycle, bicyclist, bike, cyclist, mountain, person mountain biking)</small>
🚵‍♂️ man mountain biking
🚵‍♀️ woman mountain biking
🤸 person cartwheeling <small>(cartwheel, gymnastics, person cartwheeling)</small>
🤸‍♂️ man cartwheeling
🤸‍♀️ woman cartwheeling
🤼 people wrestling <small>(people wrestling, wrestle, wrestler)</small>
🤼‍♂️ men wrestling
🤼‍♀️ women wrestling
🤽 person playing water polo <small>(person playing water polo, polo, water)</small>
🤽‍♂️ man playing water polo
🤽‍♀️ woman playing water polo
🤾 person playing handball <small>(ball, handball, person playing handball)</small>
🤾‍♂️ man playing handball
🤾‍♀️ woman playing handball
🤹 person juggling <small>(balance, juggle, multitask, person juggling, skill)</small>
🤹‍♂️ man juggling
🤹‍♀️ woman juggling
🧘 person in lotus position <small>(meditation, person in lotus position, yoga)</small>
🧘‍♂️ man in lotus position
🧘‍♀️ woman in lotus position
🛀 person taking bath <small>(bath, bathtub, person taking bath)</small>
🛌 person in bed <small>(hotel, person in bed, sleep)</small>
🧑‍🤝‍🧑 people holding hands <small>(couple, hand, hold, holding hands, people holding hands, person)</small>
👭 women holding hands <small>(couple, hand, holding hands, women, women holding hands)</small>
👫 woman and man holding hands <small>(couple, hand, hold, holding hands, man, woman, woman and man holding hands)</small>
👬 men holding hands <small>(couple, Gemini, holding hands, man, men, men holding hands, twins, zodiac)</small>
💏 kiss <small>(couple, kiss)</small>
👩‍❤️‍💋‍👨 kiss: woman, man
👨‍❤️‍💋‍👨 kiss: man, man
👩‍❤️‍💋‍👩 kiss: woman, woman
💑 couple with heart <small>(couple, couple with heart, love)</small>
👩‍❤️‍👨 couple with heart: woman, man
👨‍❤️‍👨 couple with heart: man, man
👩‍❤️‍👩 couple with heart: woman, woman
👪 family <small>(family)</small>
👨‍👩‍👦 family: man, woman, boy
👨‍👩‍👧 family: man, woman, girl
👨‍👩‍👧‍👦 family: man, woman, girl, boy
👨‍👩‍👦‍👦 family: man, woman, boy, boy
👨‍👩‍👧‍👧 family: man, woman, girl, girl
👨‍👨‍👦 family: man, man, boy
👨‍👨‍👧 family: man, man, girl
👨‍👨‍👧‍👦 family: man, man, girl, boy
👨‍👨‍👦‍👦 family: man, man, boy, boy
👨‍👨‍👧‍👧 family: man, man, girl, girl
👩‍👩‍👦 family: woman, woman, boy
👩‍👩‍👧 family: woman, woman, girl
👩‍👩‍👧‍👦 family: woman, woman, girl, boy
👩‍👩‍👦‍👦 family: woman, woman, boy, boy
👩‍👩‍👧‍👧 family: woman, woman, girl, girl
👨‍👦 family: man, boy
👨‍👦‍👦 family: man, boy, boy
👨‍👧 family: man, girl
👨‍👧‍👦 family: man, girl, boy
👨‍👧‍👧 family: man, girl, girl
👩‍👦 family: woman, boy
👩‍👦‍👦 family: woman, boy, boy
👩‍👧 family: woman, girl
👩‍👧‍👦 family: woman, girl, boy
👩‍👧‍👧 family: woman, girl, girl
🗣 speaking head <small>(face, head, silhouette, speak, speaking)</small>
👤 bust in silhouette <small>(bust, bust in silhouette, silhouette)</small>
👥 busts in silhouette <small>(bust, busts in silhouette, silhouette)</small>
👣 footprints <small>(clothing, footprint, footprints, print)</small>
🦰 red hair <small>(ginger, red hair, redhead)</small>
🦱 curly hair <small>(afro, curly, curly hair, ringlets)</small>
🦳 white hair <small>(gray, hair, old, white)</small>
🦲 bald <small>(bald, chemotherapy, hairless, no hair, shaven)</small>
🐵 monkey face <small>(face, monkey)</small>
🐒 monkey <small>(monkey)</small>
🦍 gorilla <small>(gorilla)</small>
🦧 orangutan <small>(ape, orangutan)</small>
🐶 dog face <small>(dog, face, pet)</small>
🐕 dog <small>(dog, pet)</small>
🦮 guide dog <small>(accessibility, blind, guide, guide dog)</small>
🐕‍🦺 service dog <small>(accessibility, assistance, dog, service)</small>
🐩 poodle <small>(dog, poodle)</small>
🐺 wolf <small>(face, wolf)</small>
🦊 fox <small>(face, fox)</small>
🦝 raccoon <small>(curious, raccoon, sly)</small>
🐱 cat face <small>(cat, face, pet)</small>
🐈 cat <small>(cat, pet)</small>
🦁 lion <small>(face, Leo, lion, zodiac)</small>
🐯 tiger face <small>(face, tiger)</small>
🐅 tiger <small>(tiger)</small>
🐆 leopard <small>(leopard)</small>
🐴 horse face <small>(face, horse)</small>
🐎 horse <small>(equestrian, horse, racehorse, racing)</small>
🦄 unicorn <small>(face, unicorn)</small>
🦓 zebra <small>(stripe, zebra)</small>
🦌 deer <small>(deer)</small>
🐮 cow face <small>(cow, face)</small>
🐂 ox <small>(bull, ox, Taurus, zodiac)</small>
🐃 water buffalo <small>(buffalo, water)</small>
🐄 cow <small>(cow)</small>
🐷 pig face <small>(face, pig)</small>
🐖 pig <small>(pig, sow)</small>
🐗 boar <small>(boar, pig)</small>
🐽 pig nose <small>(face, nose, pig)</small>
🐏 ram <small>(Aries, male, ram, sheep, zodiac)</small>
🐑 ewe <small>(ewe, female, sheep)</small>
🐐 goat <small>(Capricorn, goat, zodiac)</small>
🐪 camel <small>(camel, dromedary, hump)</small>
🐫 two-hump camel <small>(bactrian, camel, hump, two-hump camel)</small>
🦙 llama <small>(alpaca, guanaco, llama, vicuña, wool)</small>
🦒 giraffe <small>(giraffe, spots)</small>
🐘 elephant <small>(elephant)</small>
🦏 rhinoceros <small>(rhinoceros)</small>
🦛 hippopotamus <small>(hippo, hippopotamus)</small>
🐭 mouse face <small>(face, mouse)</small>
🐁 mouse <small>(mouse)</small>
🐀 rat <small>(rat)</small>
🐹 hamster <small>(face, hamster, pet)</small>
🐰 rabbit face <small>(bunny, face, pet, rabbit)</small>
🐇 rabbit <small>(bunny, pet, rabbit)</small>
🐿 chipmunk <small>(chipmunk, squirrel)</small>
🦔 hedgehog <small>(hedgehog, spiny)</small>
🦇 bat <small>(bat, vampire)</small>
🐻 bear <small>(bear, face)</small>
🐨 koala <small>(bear, koala)</small>
🐼 panda <small>(face, panda)</small>
🦥 sloth <small>(lazy, sloth, slow)</small>
🦦 otter <small>(fishing, otter, playful)</small>
🦨 skunk <small>(skunk, stink)</small>
🦘 kangaroo <small>(Australia, joey, jump, kangaroo, marsupial)</small>
🦡 badger <small>(badger, honey badger, pester)</small>
🐾 paw prints <small>(feet, paw, paw prints, print)</small>
🦃 turkey <small>(bird, turkey)</small>
🐔 chicken <small>(bird, chicken)</small>
🐓 rooster <small>(bird, rooster)</small>
🐣 hatching chick <small>(baby, bird, chick, hatching)</small>
🐤 baby chick <small>(baby, bird, chick)</small>
🐥 front-facing baby chick <small>(baby, bird, chick, front-facing baby chick)</small>
🐦 bird <small>(bird)</small>
🐧 penguin <small>(bird, penguin)</small>
🕊 dove <small>(bird, dove, fly, peace)</small>
🦅 eagle <small>(bird, eagle)</small>
🦆 duck <small>(bird, duck)</small>
🦢 swan <small>(bird, cygnet, swan, ugly duckling)</small>
🦉 owl <small>(bird, owl, wise)</small>
🦩 flamingo <small>(flamboyant, flamingo, tropical)</small>
🦚 peacock <small>(bird, ostentatious, peacock, peahen, proud)</small>
🦜 parrot <small>(bird, parrot, pirate, talk)</small>
🐸 frog <small>(face, frog)</small>
🐊 crocodile <small>(crocodile)</small>
🐢 turtle <small>(terrapin, tortoise, turtle)</small>
🦎 lizard <small>(lizard, reptile)</small>
🐍 snake <small>(bearer, Ophiuchus, serpent, snake, zodiac)</small>
🐲 dragon face <small>(dragon, face, fairy tale)</small>
🐉 dragon <small>(dragon, fairy tale)</small>
🦕 sauropod <small>(brachiosaurus, brontosaurus, diplodocus, sauropod)</small>
🦖 T-Rex <small>(T-Rex, Tyrannosaurus Rex)</small>
🐳 spouting whale <small>(face, spouting, whale)</small>
🐋 whale <small>(whale)</small>
🐬 dolphin <small>(dolphin, flipper)</small>
🐟 fish <small>(fish, Pisces, zodiac)</small>
🐠 tropical fish <small>(fish, tropical)</small>
🐡 blowfish <small>(blowfish, fish)</small>
🦈 shark <small>(fish, shark)</small>
🐙 octopus <small>(octopus)</small>
🐚 spiral shell <small>(shell, spiral)</small>
🐌 snail <small>(snail)</small>
🦋 butterfly <small>(butterfly, insect, pretty)</small>
🐛 bug <small>(bug, insect)</small>
🐜 ant <small>(ant, insect)</small>
🐝 honeybee <small>(bee, honeybee, insect)</small>
🐞 lady beetle <small>(beetle, insect, lady beetle, ladybird, ladybug)</small>
🦗 cricket <small>(cricket, grasshopper)</small>
🕷 spider <small>(insect, spider)</small>
🕸 spider web <small>(spider, web)</small>
🦂 scorpion <small>(scorpio, Scorpio, scorpion, zodiac)</small>
🦟 mosquito <small>(disease, fever, insect, malaria, mosquito, virus)</small>
🦠 microbe <small>(amoeba, bacteria, microbe, virus)</small>
💐 bouquet <small>(bouquet, flower)</small>
🌸 cherry blossom <small>(blossom, cherry, flower)</small>
💮 white flower <small>(flower, white flower)</small>
🏵 rosette <small>(plant, rosette)</small>
🌹 rose <small>(flower, rose)</small>
🥀 wilted flower <small>(flower, wilted)</small>
🌺 hibiscus <small>(flower, hibiscus)</small>
🌻 sunflower <small>(flower, sun, sunflower)</small>
🌼 blossom <small>(blossom, flower)</small>
🌷 tulip <small>(flower, tulip)</small>
🌱 seedling <small>(seedling, young)</small>
🌲 evergreen tree <small>(evergreen tree, tree)</small>
🌳 deciduous tree <small>(deciduous, shedding, tree)</small>
🌴 palm tree <small>(palm, tree)</small>
🌵 cactus <small>(cactus, plant)</small>
🌾 sheaf of rice <small>(ear, grain, rice, sheaf of rice)</small>
🌿 herb <small>(herb, leaf)</small>
☘ shamrock <small>(plant, shamrock)</small>
🍀 four leaf clover <small>(4, clover, four, four-leaf clover, leaf)</small>
🍁 maple leaf <small>(falling, leaf, maple)</small>
🍂 fallen leaf <small>(fallen leaf, falling, leaf)</small>
🍃 leaf fluttering in wind <small>(blow, flutter, leaf, leaf fluttering in wind, wind)</small>
🍇 grapes <small>(fruit, grape, grapes)</small>
🍈 melon <small>(fruit, melon)</small>
🍉 watermelon <small>(fruit, watermelon)</small>
🍊 tangerine <small>(fruit, orange, tangerine)</small>
🍋 lemon <small>(citrus, fruit, lemon)</small>
🍌 banana <small>(banana, fruit)</small>
🍍 pineapple <small>(fruit, pineapple)</small>
🥭 mango <small>(fruit, mango, tropical)</small>
🍎 red apple <small>(apple, fruit, red)</small>
🍏 green apple <small>(apple, fruit, green)</small>
🍐 pear <small>(fruit, pear)</small>
🍑 peach <small>(fruit, peach)</small>
🍒 cherries <small>(berries, cherries, cherry, fruit, red)</small>
🍓 strawberry <small>(berry, fruit, strawberry)</small>
🥝 kiwi fruit <small>(food, fruit, kiwi)</small>
🍅 tomato <small>(fruit, tomato, vegetable)</small>
🥥 coconut <small>(coconut, palm, piña colada)</small>
🥑 avocado <small>(avocado, food, fruit)</small>
🍆 eggplant <small>(aubergine, eggplant, vegetable)</small>
🥔 potato <small>(food, potato, vegetable)</small>
🥕 carrot <small>(carrot, food, vegetable)</small>
🌽 ear of corn <small>(corn, ear, ear of corn, maize, maze)</small>
🌶 hot pepper <small>(hot, pepper)</small>
🥒 cucumber <small>(cucumber, food, pickle, vegetable)</small>
🥬 leafy green <small>(bok choy, cabbage, kale, leafy green, lettuce)</small>
🥦 broccoli <small>(broccoli, wild cabbage)</small>
🧄 garlic <small>(flavoring, garlic)</small>
🧅 onion <small>(flavoring, onion)</small>
🍄 mushroom <small>(mushroom, toadstool)</small>
🥜 peanuts <small>(food, nut, peanut, peanuts, vegetable)</small>
🌰 chestnut <small>(chestnut, plant)</small>
🍞 bread <small>(bread, loaf)</small>
🥐 croissant <small>(bread, crescent roll, croissant, food, french)</small>
🥖 baguette bread <small>(baguette, bread, food, french)</small>
🥨 pretzel <small>(pretzel, twisted)</small>
🥯 bagel <small>(bagel, bakery, schmear)</small>
🥞 pancakes <small>(crêpe, food, hotcake, pancake, pancakes)</small>
🧇 waffle <small>(indecisive, iron, waffle)</small>
🧀 cheese wedge <small>(cheese, cheese wedge)</small>
🍖 meat on bone <small>(bone, meat, meat on bone)</small>
🍗 poultry leg <small>(bone, chicken, drumstick, leg, poultry)</small>
🥩 cut of meat <small>(chop, cut of meat, lambchop, porkchop, steak)</small>
🥓 bacon <small>(bacon, food, meat)</small>
🍔 hamburger <small>(burger, hamburger)</small>
🍟 french fries <small>(french, fries)</small>
🍕 pizza <small>(cheese, pizza, slice)</small>
🌭 hot dog <small>(frankfurter, hot dog, hotdog, sausage)</small>
🥪 sandwich <small>(bread, sandwich)</small>
🌮 taco <small>(mexican, taco)</small>
🌯 burrito <small>(burrito, mexican, wrap)</small>
🥙 stuffed flatbread <small>(falafel, flatbread, food, gyro, kebab, stuffed)</small>
🧆 falafel <small>(chickpea, falafel, meatball)</small>
🥚 egg <small>(egg, food)</small>
🍳 cooking <small>(cooking, egg, frying, pan)</small>
🥘 shallow pan of food <small>(casserole, food, paella, pan, shallow, shallow pan of food)</small>
🍲 pot of food <small>(pot, pot of food, stew)</small>
🥣 bowl with spoon <small>(bowl with spoon, breakfast, cereal, congee)</small>
🥗 green salad <small>(food, green, salad)</small>
🍿 popcorn <small>(popcorn)</small>
🧈 butter <small>(butter, dairy)</small>
🧂 salt <small>(condiment, salt, shaker)</small>
🥫 canned food <small>(can, canned food)</small>
🍱 bento box <small>(bento, box)</small>
🍘 rice cracker <small>(cracker, rice)</small>
🍙 rice ball <small>(ball, Japanese, rice)</small>
🍚 cooked rice <small>(cooked, rice)</small>
🍛 curry rice <small>(curry, rice)</small>
🍜 steaming bowl <small>(bowl, noodle, ramen, steaming)</small>
🍝 spaghetti <small>(pasta, spaghetti)</small>
🍠 roasted sweet potato <small>(potato, roasted, sweet)</small>
🍢 oden <small>(kebab, oden, seafood, skewer, stick)</small>
🍣 sushi <small>(sushi)</small>
🍤 fried shrimp <small>(fried, prawn, shrimp, tempura)</small>
🍥 fish cake with swirl <small>(cake, fish, fish cake with swirl, pastry, swirl)</small>
🥮 moon cake <small>(autumn, festival, moon cake, yuèbǐng)</small>
🍡 dango <small>(dango, dessert, Japanese, skewer, stick, sweet)</small>
🥟 dumpling <small>(dumpling, empanada, gyōza, jiaozi, pierogi, potsticker)</small>
🥠 fortune cookie <small>(fortune cookie, prophecy)</small>
🥡 takeout box <small>(oyster pail, takeout box)</small>
🦀 crab <small>(Cancer, crab, zodiac)</small>
🦞 lobster <small>(bisque, claws, lobster, seafood)</small>
🦐 shrimp <small>(food, shellfish, shrimp, small)</small>
🦑 squid <small>(food, molusc, squid)</small>
🦪 oyster <small>(diving, oyster, pearl)</small>
🍦 soft ice cream <small>(cream, dessert, ice, icecream, soft, sweet)</small>
🍧 shaved ice <small>(dessert, ice, shaved, sweet)</small>
🍨 ice cream <small>(cream, dessert, ice, sweet)</small>
🍩 doughnut <small>(dessert, donut, doughnut, sweet)</small>
🍪 cookie <small>(cookie, dessert, sweet)</small>
🎂 birthday cake <small>(birthday, cake, celebration, dessert, pastry, sweet)</small>
🍰 shortcake <small>(cake, dessert, pastry, shortcake, slice, sweet)</small>
🧁 cupcake <small>(bakery, cupcake, sweet)</small>
🥧 pie <small>(filling, pastry, pie)</small>
🍫 chocolate bar <small>(bar, chocolate, dessert, sweet)</small>
🍬 candy <small>(candy, dessert, sweet)</small>
🍭 lollipop <small>(candy, dessert, lollipop, sweet)</small>
🍮 custard <small>(custard, dessert, pudding, sweet)</small>
🍯 honey pot <small>(honey, honeypot, pot, sweet)</small>
🍼 baby bottle <small>(baby, bottle, drink, milk)</small>
🥛 glass of milk <small>(drink, glass, glass of milk, milk)</small>
☕ hot beverage <small>(beverage, coffee, drink, hot, steaming, tea)</small>
🍵 teacup without handle <small>(beverage, cup, drink, tea, teacup, teacup without handle)</small>
🍶 sake <small>(bar, beverage, bottle, cup, drink, sake)</small>
🍾 bottle with popping cork <small>(bar, bottle, bottle with popping cork, cork, drink, popping)</small>
🍷 wine glass <small>(bar, beverage, drink, glass, wine)</small>
🍸 cocktail glass <small>(bar, cocktail, drink, glass)</small>
🍹 tropical drink <small>(bar, drink, tropical)</small>
🍺 beer mug <small>(bar, beer, drink, mug)</small>
🍻 clinking beer mugs <small>(bar, beer, clink, clinking beer mugs, drink, mug)</small>
🥂 clinking glasses <small>(celebrate, clink, clinking glasses, drink, glass)</small>
🥃 tumbler glass <small>(glass, liquor, shot, tumbler, whisky)</small>
🥤 cup with straw <small>(cup with straw, juice, soda)</small>
🧃 beverage box <small>(beverage box, juice box)</small>
🧉 mate <small>(drink, mate)</small>
🧊 ice <small>(cold, ice, ice cube, iceberg)</small>
🥢 chopsticks <small>(chopsticks, hashi)</small>
🍽 fork and knife with plate <small>(cooking, fork, fork and knife with plate, knife, plate)</small>
🍴 fork and knife <small>(cooking, cutlery, fork, fork and knife, knife)</small>
🥄 spoon <small>(spoon, tableware)</small>
🔪 kitchen knife <small>(cooking, hocho, kitchen knife, knife, tool, weapon)</small>
🏺 amphora <small>(amphora, Aquarius, cooking, drink, jug, zodiac)</small>
🌍 globe showing Europe-Africa <small>(Africa, earth, Europe, globe, globe showing Europe-Africa, world)</small>
🌎 globe showing Americas <small>(Americas, earth, globe, globe showing Americas, world)</small>
🌏 globe showing Asia-Australia <small>(Asia, Australia, earth, globe, globe showing Asia-Australia, world)</small>
🌐 globe with meridians <small>(earth, globe, globe with meridians, meridians, world)</small>
🗺 world map <small>(map, world)</small>
🗾 map of Japan <small>(Japan, map, map of Japan)</small>
🧭 compass <small>(compass, magnetic, navigation, orienteering)</small>
🏔 snow-capped mountain <small>(cold, mountain, snow, snow-capped mountain)</small>
⛰ mountain <small>(mountain)</small>
🌋 volcano <small>(eruption, mountain, volcano)</small>
🗻 mount fuji <small>(fuji, mount fuji, mountain)</small>
🏕 camping <small>(camping)</small>
🏖 beach with umbrella <small>(beach, beach with umbrella, umbrella)</small>
🏜 desert <small>(desert)</small>
🏝 desert island <small>(desert, island)</small>
🏞 national park <small>(national park, park)</small>
🏟 stadium <small>(stadium)</small>
🏛 classical building <small>(classical, classical building)</small>
🏗 building construction <small>(building construction, construction)</small>
🧱 brick <small>(brick, bricks, clay, mortar, wall)</small>
🏘 houses <small>(houses)</small>
🏚 derelict house <small>(derelict, house)</small>
🏠 house <small>(home, house)</small>
🏡 house with garden <small>(garden, home, house, house with garden)</small>
🏢 office building <small>(building, office building)</small>
🏣 Japanese post office <small>(Japanese, Japanese post office, post)</small>
🏤 post office <small>(European, post, post office)</small>
🏥 hospital <small>(doctor, hospital, medicine)</small>
🏦 bank <small>(bank, building)</small>
🏨 hotel <small>(building, hotel)</small>
🏩 love hotel <small>(hotel, love)</small>
🏪 convenience store <small>(convenience, store)</small>
🏫 school <small>(building, school)</small>
🏬 department store <small>(department, store)</small>
🏭 factory <small>(building, factory)</small>
🏯 Japanese castle <small>(castle, Japanese)</small>
🏰 castle <small>(castle, European)</small>
💒 wedding <small>(chapel, romance, wedding)</small>
🗼 Tokyo tower <small>(Tokyo, tower)</small>
🗽 Statue of Liberty <small>(liberty, statue, Statue of Liberty)</small>
⛪ church <small>(Christian, church, cross, religion)</small>
🕌 mosque <small>(islam, mosque, Muslim, religion)</small>
🛕 hindu temple <small>(hindu, temple)</small>
🕍 synagogue <small>(Jew, Jewish, religion, synagogue, temple)</small>
⛩ shinto shrine <small>(religion, shinto, shrine)</small>
🕋 kaaba <small>(islam, kaaba, Muslim, religion)</small>
⛲ fountain <small>(fountain)</small>
⛺ tent <small>(camping, tent)</small>
🌁 foggy <small>(fog, foggy)</small>
🌃 night with stars <small>(night, night with stars, star)</small>
🏙 cityscape <small>(city, cityscape)</small>
🌄 sunrise over mountains <small>(morning, mountain, sun, sunrise, sunrise over mountains)</small>
🌅 sunrise <small>(morning, sun, sunrise)</small>
🌆 cityscape at dusk <small>(city, cityscape at dusk, dusk, evening, landscape, sunset)</small>
🌇 sunset <small>(dusk, sun, sunset)</small>
🌉 bridge at night <small>(bridge, bridge at night, night)</small>
♨ hot springs <small>(hot, hotsprings, springs, steaming)</small>
🎠 carousel horse <small>(carousel, horse)</small>
🎡 ferris wheel <small>(amusement park, ferris, wheel)</small>
🎢 roller coaster <small>(amusement park, coaster, roller)</small>
💈 barber pole <small>(barber, haircut, pole)</small>
🎪 circus tent <small>(circus, tent)</small>
🚂 locomotive <small>(engine, locomotive, railway, steam, train)</small>
🚃 railway car <small>(car, electric, railway, train, tram, trolleybus)</small>
🚄 high-speed train <small>(high-speed train, railway, shinkansen, speed, train)</small>
🚅 bullet train <small>(bullet, railway, shinkansen, speed, train)</small>
🚆 train <small>(railway, train)</small>
🚇 metro <small>(metro, subway)</small>
🚈 light rail <small>(light rail, railway)</small>
🚉 station <small>(railway, station, train)</small>
🚊 tram <small>(tram, trolleybus)</small>
🚝 monorail <small>(monorail, vehicle)</small>
🚞 mountain railway <small>(car, mountain, railway)</small>
🚋 tram car <small>(car, tram, trolleybus)</small>
🚌 bus <small>(bus, vehicle)</small>
🚍 oncoming bus <small>(bus, oncoming)</small>
🚎 trolleybus <small>(bus, tram, trolley, trolleybus)</small>
🚐 minibus <small>(bus, minibus)</small>
🚑 ambulance <small>(ambulance, vehicle)</small>
🚒 fire engine <small>(engine, fire, truck)</small>
🚓 police car <small>(car, patrol, police)</small>
🚔 oncoming police car <small>(car, oncoming, police)</small>
🚕 taxi <small>(taxi, vehicle)</small>
🚖 oncoming taxi <small>(oncoming, taxi)</small>
🚗 automobile <small>(automobile, car)</small>
🚘 oncoming automobile <small>(automobile, car, oncoming)</small>
🚙 sport utility vehicle <small>(recreational, sport utility, sport utility vehicle)</small>
🚚 delivery truck <small>(delivery, truck)</small>
🚛 articulated lorry <small>(articulated lorry, lorry, semi, truck)</small>
🚜 tractor <small>(tractor, vehicle)</small>
🏎 racing car <small>(car, racing)</small>
🏍 motorcycle <small>(motorcycle, racing)</small>
🛵 motor scooter <small>(motor, scooter)</small>
🦽 manual wheelchair <small>(accessibility, manual wheelchair)</small>
🦼 motorized wheelchair <small>(accessibility, motorized wheelchair)</small>
🛺 auto rickshaw <small>(auto rickshaw, tuk tuk)</small>
🚲 bicycle <small>(bicycle, bike)</small>
🛴 kick scooter <small>(kick, scooter)</small>
🛹 skateboard <small>(board, skateboard)</small>
🚏 bus stop <small>(bus, busstop, stop)</small>
🛣 motorway <small>(highway, motorway, road)</small>
🛤 railway track <small>(railway, railway track, train)</small>
🛢 oil drum <small>(drum, oil)</small>
⛽ fuel pump <small>(diesel, fuel, fuelpump, gas, pump, station)</small>
🚨 police car light <small>(beacon, car, light, police, revolving)</small>
🚥 horizontal traffic light <small>(horizontal traffic light, light, signal, traffic)</small>
🚦 vertical traffic light <small>(light, signal, traffic, vertical traffic light)</small>
🛑 stop sign <small>(octagonal, sign, stop)</small>
🚧 construction <small>(barrier, construction)</small>
⚓ anchor <small>(anchor, ship, tool)</small>
⛵ sailboat <small>(boat, resort, sailboat, sea, yacht)</small>
🛶 canoe <small>(boat, canoe)</small>
🚤 speedboat <small>(boat, speedboat)</small>
🛳 passenger ship <small>(passenger, ship)</small>
⛴ ferry <small>(boat, ferry, passenger)</small>
🛥 motor boat <small>(boat, motor boat, motorboat)</small>
🚢 ship <small>(boat, passenger, ship)</small>
✈ airplane <small>(aeroplane, airplane)</small>
🛩 small airplane <small>(aeroplane, airplane, small airplane)</small>
🛫 airplane departure <small>(aeroplane, airplane, check-in, departure, departures)</small>
🛬 airplane arrival <small>(aeroplane, airplane, airplane arrival, arrivals, arriving, landing)</small>
🪂 parachute <small>(hang-glide, parachute, parasail, skydive)</small>
💺 seat <small>(chair, seat)</small>
🚁 helicopter <small>(helicopter, vehicle)</small>
🚟 suspension railway <small>(railway, suspension)</small>
🚠 mountain cableway <small>(cable, gondola, mountain, mountain cableway)</small>
🚡 aerial tramway <small>(aerial, cable, car, gondola, tramway)</small>
🛰 satellite <small>(satellite, space)</small>
🚀 rocket <small>(rocket, space)</small>
🛸 flying saucer <small>(flying saucer, UFO)</small>
🛎 bellhop bell <small>(bell, bellhop, hotel)</small>
🧳 luggage <small>(luggage, packing, travel)</small>
⌛ hourglass done <small>(hourglass done, sand, timer)</small>
⏳ hourglass not done <small>(hourglass, hourglass not done, sand, timer)</small>
⌚ watch <small>(clock, watch)</small>
⏰ alarm clock <small>(alarm, clock)</small>
⏱ stopwatch <small>(clock, stopwatch)</small>
⏲ timer clock <small>(clock, timer)</small>
🕰 mantelpiece clock <small>(clock, mantelpiece clock)</small>
🕛 twelve o’clock <small>(00, 12, 12:00, clock, o’clock, twelve)</small>
🕧 twelve-thirty <small>(12, 12:30, clock, thirty, twelve, twelve-thirty)</small>
🕐 one o’clock <small>(00, 1, 1:00, clock, o’clock, one)</small>
🕜 one-thirty <small>(1, 1:30, clock, one, one-thirty, thirty)</small>
🕑 two o’clock <small>(00, 2, 2:00, clock, o’clock, two)</small>
🕝 two-thirty <small>(2, 2:30, clock, thirty, two, two-thirty)</small>
🕒 three o’clock <small>(00, 3, 3:00, clock, o’clock, three)</small>
🕞 three-thirty <small>(3, 3:30, clock, thirty, three, three-thirty)</small>
🕓 four o’clock <small>(00, 4, 4:00, clock, four, o’clock)</small>
🕟 four-thirty <small>(4, 4:30, clock, four, four-thirty, thirty)</small>
🕔 five o’clock <small>(00, 5, 5:00, clock, five, o’clock)</small>
🕠 five-thirty <small>(5, 5:30, clock, five, five-thirty, thirty)</small>
🕕 six o’clock <small>(00, 6, 6:00, clock, o’clock, six)</small>
🕡 six-thirty <small>(6, 6:30, clock, six, six-thirty, thirty)</small>
🕖 seven o’clock <small>(00, 7, 7:00, clock, o’clock, seven)</small>
🕢 seven-thirty <small>(7, 7:30, clock, seven, seven-thirty, thirty)</small>
🕗 eight o’clock <small>(00, 8, 8:00, clock, eight, o’clock)</small>
🕣 eight-thirty <small>(8, 8:30, clock, eight, eight-thirty, thirty)</small>
🕘 nine o’clock <small>(00, 9, 9:00, clock, nine, o’clock)</small>
🕤 nine-thirty <small>(9, 9:30, clock, nine, nine-thirty, thirty)</small>
🕙 ten o’clock <small>(00, 10, 10:00, clock, o’clock, ten)</small>
🕥 ten-thirty <small>(10, 10:30, clock, ten, ten-thirty, thirty)</small>
🕚 eleven o’clock <small>(00, 11, 11:00, clock, eleven, o’clock)</small>
🕦 eleven-thirty <small>(11, 11:30, clock, eleven, eleven-thirty, thirty)</small>
🌑 new moon <small>(dark, moon, new moon)</small>
🌒 waxing crescent moon <small>(crescent, moon, waxing)</small>
🌓 first quarter moon <small>(first quarter moon, moon, quarter)</small>
🌔 waxing gibbous moon <small>(gibbous, moon, waxing)</small>
🌕 full moon <small>(full, moon)</small>
🌖 waning gibbous moon <small>(gibbous, moon, waning)</small>
🌗 last quarter moon <small>(last quarter moon, moon, quarter)</small>
🌘 waning crescent moon <small>(crescent, moon, waning)</small>
🌙 crescent moon <small>(crescent, moon)</small>
🌚 new moon face <small>(face, moon, new moon face)</small>
🌛 first quarter moon face <small>(face, first quarter moon face, moon, quarter)</small>
🌜 last quarter moon face <small>(face, last quarter moon face, moon, quarter)</small>
🌡 thermometer <small>(thermometer, weather)</small>
☀ sun <small>(bright, rays, sun, sunny)</small>
🌝 full moon face <small>(bright, face, full, moon)</small>
🌞 sun with face <small>(bright, face, sun, sun with face)</small>
🪐 ringed planet <small>(ringed planet, saturn, saturnine)</small>
⭐ star <small>(star)</small>
🌟 glowing star <small>(glittery, glow, glowing star, shining, sparkle, star)</small>
🌠 shooting star <small>(falling, shooting, star)</small>
🌌 milky way <small>(milky way, space)</small>
☁ cloud <small>(cloud, weather)</small>
⛅ sun behind cloud <small>(cloud, sun, sun behind cloud)</small>
⛈ cloud with lightning and rain <small>(cloud, cloud with lightning and rain, rain, thunder)</small>
🌤 sun behind small cloud <small>(cloud, sun, sun behind small cloud)</small>
🌥 sun behind large cloud <small>(cloud, sun, sun behind large cloud)</small>
🌦 sun behind rain cloud <small>(cloud, rain, sun, sun behind rain cloud)</small>
🌧 cloud with rain <small>(cloud, cloud with rain, rain)</small>
🌨 cloud with snow <small>(cloud, cloud with snow, cold, snow)</small>
🌩 cloud with lightning <small>(cloud, cloud with lightning, lightning)</small>
🌪 tornado <small>(cloud, tornado, whirlwind)</small>
🌫 fog <small>(cloud, fog)</small>
🌬 wind face <small>(blow, cloud, face, wind)</small>
🌀 cyclone <small>(cyclone, dizzy, hurricane, twister, typhoon)</small>
🌈 rainbow <small>(rain, rainbow)</small>
🌂 closed umbrella <small>(closed umbrella, clothing, rain, umbrella)</small>
☂ umbrella <small>(clothing, rain, umbrella)</small>
☔ umbrella with rain drops <small>(clothing, drop, rain, umbrella, umbrella with rain drops)</small>
⛱ umbrella on ground <small>(rain, sun, umbrella, umbrella on ground)</small>
⚡ high voltage <small>(danger, electric, high voltage, lightning, voltage, zap)</small>
❄ snowflake <small>(cold, snow, snowflake)</small>
☃ snowman <small>(cold, snow, snowman)</small>
⛄ snowman without snow <small>(cold, snow, snowman, snowman without snow)</small>
☄ comet <small>(comet, space)</small>
🔥 fire <small>(fire, flame, tool)</small>
💧 droplet <small>(cold, comic, drop, droplet, sweat)</small>
🌊 water wave <small>(ocean, water, wave)</small>
🎃 jack-o-lantern <small>(celebration, halloween, jack, jack-o-lantern, lantern)</small>
🎄 Christmas tree <small>(celebration, Christmas, tree)</small>
🎆 fireworks <small>(celebration, fireworks)</small>
🎇 sparkler <small>(celebration, fireworks, sparkle, sparkler)</small>
🧨 firecracker <small>(dynamite, explosive, firecracker, fireworks)</small>
✨ sparkles <small>(*, sparkle, sparkles, star)</small>
🎈 balloon <small>(balloon, celebration)</small>
🎉 party popper <small>(celebration, party, popper, tada)</small>
🎊 confetti ball <small>(ball, celebration, confetti)</small>
🎋 tanabata tree <small>(banner, celebration, Japanese, tanabata tree, tree)</small>
🎍 pine decoration <small>(bamboo, celebration, Japanese, pine, pine decoration)</small>
🎎 Japanese dolls <small>(celebration, doll, festival, Japanese, Japanese dolls)</small>
🎏 carp streamer <small>(carp, celebration, streamer)</small>
🎐 wind chime <small>(bell, celebration, chime, wind)</small>
🎑 moon viewing ceremony <small>(celebration, ceremony, moon, moon viewing ceremony)</small>
🧧 red envelope <small>(gift, good luck, hóngbāo, lai see, money, red envelope)</small>
🎀 ribbon <small>(celebration, ribbon)</small>
🎁 wrapped gift <small>(box, celebration, gift, present, wrapped)</small>
🎗 reminder ribbon <small>(celebration, reminder, ribbon)</small>
🎟 admission tickets <small>(admission, admission tickets, ticket)</small>
🎫 ticket <small>(admission, ticket)</small>
🎖 military medal <small>(celebration, medal, military)</small>
🏆 trophy <small>(prize, trophy)</small>
🏅 sports medal <small>(medal, sports medal)</small>
🥇 1st place medal <small>(1st place medal, first, gold, medal)</small>
🥈 2nd place medal <small>(2nd place medal, medal, second, silver)</small>
🥉 3rd place medal <small>(3rd place medal, bronze, medal, third)</small>
⚽ soccer ball <small>(ball, football, soccer)</small>
⚾ baseball <small>(ball, baseball)</small>
🥎 softball <small>(ball, glove, softball, underarm)</small>
🏀 basketball <small>(ball, basketball, hoop)</small>
🏐 volleyball <small>(ball, game, volleyball)</small>
🏈 american football <small>(american, ball, football)</small>
🏉 rugby football <small>(ball, football, rugby)</small>
🎾 tennis <small>(ball, racquet, tennis)</small>
🥏 flying disc <small>(flying disc, ultimate)</small>
🎳 bowling <small>(ball, bowling, game)</small>
🏏 cricket game <small>(ball, bat, cricket game, game)</small>
🏑 field hockey <small>(ball, field, game, hockey, stick)</small>
🏒 ice hockey <small>(game, hockey, ice, puck, stick)</small>
🥍 lacrosse <small>(ball, goal, lacrosse, stick)</small>
🏓 ping pong <small>(ball, bat, game, paddle, ping pong, table tennis)</small>
🏸 badminton <small>(badminton, birdie, game, racquet, shuttlecock)</small>
🥊 boxing glove <small>(boxing, glove)</small>
🥋 martial arts uniform <small>(judo, karate, martial arts, martial arts uniform, taekwondo, uniform)</small>
🥅 goal net <small>(goal, net)</small>
⛳ flag in hole <small>(flag in hole, golf, hole)</small>
⛸ ice skate <small>(ice, skate)</small>
🎣 fishing pole <small>(fish, fishing pole, pole)</small>
🤿 diving mask <small>(diving, diving mask, scuba, snorkeling)</small>
🎽 running shirt <small>(athletics, running, sash, shirt)</small>
🎿 skis <small>(ski, skis, snow)</small>
🛷 sled <small>(sled, sledge, sleigh)</small>
🥌 curling stone <small>(curling stone, game, rock)</small>
🎯 direct hit <small>(bullseye, dart, direct hit, game, hit, target)</small>
🪀 yo-yo <small>(fluctuate, toy, yo-yo)</small>
🪁 kite <small>(fly, kite, soar)</small>
🎱 pool 8 ball <small>(8, ball, billiard, eight, game, pool 8 ball)</small>
🔮 crystal ball <small>(ball, crystal, fairy tale, fantasy, fortune, tool)</small>
🧿 nazar amulet <small>(bead, charm, evil-eye, nazar, nazar amulet, talisman)</small>
🎮 video game <small>(controller, game, video game)</small>
🕹 joystick <small>(game, joystick, video game)</small>
🎰 slot machine <small>(game, slot, slot machine)</small>
🎲 game die <small>(dice, die, game)</small>
🧩 puzzle piece <small>(clue, interlocking, jigsaw, piece, puzzle)</small>
🧸 teddy bear <small>(plaything, plush, stuffed, teddy bear, toy)</small>
♠ spade suit <small>(card, game, spade suit)</small>
♥ heart suit <small>(card, game, heart suit)</small>
♦ diamond suit <small>(card, diamond suit, game)</small>
♣ club suit <small>(card, club suit, game)</small>
♟ chess pawn <small>(chess, chess pawn, dupe, expendable)</small>
🃏 joker <small>(card, game, joker, wildcard)</small>
🀄 mahjong red dragon <small>(game, mahjong, mahjong red dragon, red)</small>
🎴 flower playing cards <small>(card, flower, flower playing cards, game, Japanese, playing)</small>
🎭 performing arts <small>(art, mask, performing, performing arts, theater, theatre)</small>
🖼 framed picture <small>(art, frame, framed picture, museum, painting, picture)</small>
🎨 artist palette <small>(art, artist palette, museum, painting, palette)</small>
🧵 thread <small>(needle, sewing, spool, string, thread)</small>
🧶 yarn <small>(ball, crochet, knit, yarn)</small>
👓 glasses <small>(clothing, eye, eyeglasses, eyewear, glasses)</small>
🕶 sunglasses <small>(dark, eye, eyewear, glasses, sunglasses)</small>
🥽 goggles <small>(eye protection, goggles, swimming, welding)</small>
🥼 lab coat <small>(doctor, experiment, lab coat, scientist)</small>
🦺 safety vest <small>(emergency, safety, vest)</small>
👔 necktie <small>(clothing, necktie, tie)</small>
👕 t-shirt <small>(clothing, shirt, t-shirt, tshirt)</small>
👖 jeans <small>(clothing, jeans, pants, trousers)</small>
🧣 scarf <small>(neck, scarf)</small>
🧤 gloves <small>(gloves, hand)</small>
🧥 coat <small>(coat, jacket)</small>
🧦 socks <small>(socks, stocking)</small>
👗 dress <small>(clothing, dress)</small>
👘 kimono <small>(clothing, kimono)</small>
🥻 sari <small>(clothing, dress, sari)</small>
🩱 one-piece swimsuit <small>(bathing suit, one-piece swimsuit)</small>
🩲 briefs <small>(bathing suit, briefs, one-piece, swimsuit, underwear)</small>
🩳 shorts <small>(bathing suit, pants, shorts, underwear)</small>
👙 bikini <small>(bikini, clothing, swim)</small>
👚 woman’s clothes <small>(clothing, woman, woman’s clothes)</small>
👛 purse <small>(clothing, coin, purse)</small>
👜 handbag <small>(bag, clothing, handbag, purse)</small>
👝 clutch bag <small>(bag, clothing, clutch bag, pouch)</small>
🛍 shopping bags <small>(bag, hotel, shopping, shopping bags)</small>
🎒 backpack <small>(backpack, bag, rucksack, satchel, school)</small>
👞 man’s shoe <small>(clothing, man, man’s shoe, shoe)</small>
👟 running shoe <small>(athletic, clothing, running shoe, shoe, sneaker)</small>
🥾 hiking boot <small>(backpacking, boot, camping, hiking)</small>
🥿 flat shoe <small>(ballet flat, flat shoe, slip-on, slipper)</small>
👠 high-heeled shoe <small>(clothing, heel, high-heeled shoe, shoe, woman)</small>
👡 woman’s sandal <small>(clothing, sandal, shoe, woman, woman’s sandal)</small>
🩰 ballet shoes <small>(ballet, ballet shoes, dance)</small>
👢 woman’s boot <small>(boot, clothing, shoe, woman, woman’s boot)</small>
👑 crown <small>(clothing, crown, king, queen)</small>
👒 woman’s hat <small>(clothing, hat, woman, woman’s hat)</small>
🎩 top hat <small>(clothing, hat, top, tophat)</small>
🎓 graduation cap <small>(cap, celebration, clothing, graduation, hat)</small>
🧢 billed cap <small>(baseball cap, billed cap)</small>
⛑ rescue worker’s helmet <small>(aid, cross, face, hat, helmet, rescue worker’s helmet)</small>
📿 prayer beads <small>(beads, clothing, necklace, prayer, religion)</small>
💄 lipstick <small>(cosmetics, lipstick, makeup)</small>
💍 ring <small>(diamond, ring)</small>
💎 gem stone <small>(diamond, gem, gem stone, jewel)</small>
🔇 muted speaker <small>(mute, muted speaker, quiet, silent, speaker)</small>
🔈 speaker low volume <small>(soft, speaker low volume)</small>
🔉 speaker medium volume <small>(medium, speaker medium volume)</small>
🔊 speaker high volume <small>(loud, speaker high volume)</small>
📢 loudspeaker <small>(loud, loudspeaker, public address)</small>
📣 megaphone <small>(cheering, megaphone)</small>
📯 postal horn <small>(horn, post, postal)</small>
🔔 bell <small>(bell)</small>
🔕 bell with slash <small>(bell, bell with slash, forbidden, mute, quiet, silent)</small>
🎼 musical score <small>(music, musical score, score)</small>
🎵 musical note <small>(music, musical note, note)</small>
🎶 musical notes <small>(music, musical notes, note, notes)</small>
🎙 studio microphone <small>(mic, microphone, music, studio)</small>
🎚 level slider <small>(level, music, slider)</small>
🎛 control knobs <small>(control, knobs, music)</small>
🎤 microphone <small>(karaoke, mic, microphone)</small>
🎧 headphone <small>(earbud, headphone)</small>
📻 radio <small>(radio, video)</small>
🎷 saxophone <small>(instrument, music, sax, saxophone)</small>
🎸 guitar <small>(guitar, instrument, music)</small>
🎹 musical keyboard <small>(instrument, keyboard, music, musical keyboard, piano)</small>
🎺 trumpet <small>(instrument, music, trumpet)</small>
🎻 violin <small>(instrument, music, violin)</small>
🪕 banjo <small>(banjo, music, stringed)</small>
🥁 drum <small>(drum, drumsticks, music)</small>
📱 mobile phone <small>(cell, mobile, phone, telephone)</small>
📲 mobile phone with arrow <small>(arrow, cell, mobile, mobile phone with arrow, phone, receive)</small>
☎ telephone <small>(phone, telephone)</small>
📞 telephone receiver <small>(phone, receiver, telephone)</small>
📟 pager <small>(pager)</small>
📠 fax machine <small>(fax, fax machine)</small>
🔋 battery <small>(battery)</small>
🔌 electric plug <small>(electric, electricity, plug)</small>
💻 laptop computer <small>(computer, laptop computer, pc, personal)</small>
🖥 desktop computer <small>(computer, desktop)</small>
🖨 printer <small>(computer, printer)</small>
⌨ keyboard <small>(computer, keyboard)</small>
🖱 computer mouse <small>(computer, computer mouse)</small>
🖲 trackball <small>(computer, trackball)</small>
💽 computer disk <small>(computer, disk, minidisk, optical)</small>
💾 floppy disk <small>(computer, disk, floppy)</small>
💿 optical disk <small>(cd, computer, disk, optical)</small>
📀 dvd <small>(blu-ray, computer, disk, dvd, optical)</small>
🧮 abacus <small>(abacus, calculation)</small>
🎥 movie camera <small>(camera, cinema, movie)</small>
🎞 film frames <small>(cinema, film, frames, movie)</small>
📽 film projector <small>(cinema, film, movie, projector, video)</small>
🎬 clapper board <small>(clapper, clapper board, movie)</small>
📺 television <small>(television, tv, video)</small>
📷 camera <small>(camera, video)</small>
📸 camera with flash <small>(camera, camera with flash, flash, video)</small>
📹 video camera <small>(camera, video)</small>
📼 videocassette <small>(tape, vhs, video, videocassette)</small>
🔍 magnifying glass tilted left <small>(glass, magnifying, magnifying glass tilted left, search, tool)</small>
🔎 magnifying glass tilted right <small>(glass, magnifying, magnifying glass tilted right, search, tool)</small>
🕯 candle <small>(candle, light)</small>
💡 light bulb <small>(bulb, comic, electric, idea, light)</small>
🔦 flashlight <small>(electric, flashlight, light, tool, torch)</small>
🏮 red paper lantern <small>(bar, lantern, light, red, red paper lantern)</small>
🪔 diya lamp <small>(diya, lamp, oil)</small>
📔 notebook with decorative cover <small>(book, cover, decorated, notebook, notebook with decorative cover)</small>
📕 closed book <small>(book, closed)</small>
📖 open book <small>(book, open)</small>
📗 green book <small>(book, green)</small>
📘 blue book <small>(blue, book)</small>
📙 orange book <small>(book, orange)</small>
📚 books <small>(book, books)</small>
📓 notebook <small>(notebook)</small>
📒 ledger <small>(ledger, notebook)</small>
📃 page with curl <small>(curl, document, page, page with curl)</small>
📜 scroll <small>(paper, scroll)</small>
📄 page facing up <small>(document, page, page facing up)</small>
📰 newspaper <small>(news, newspaper, paper)</small>
🗞 rolled-up newspaper <small>(news, newspaper, paper, rolled, rolled-up newspaper)</small>
📑 bookmark tabs <small>(bookmark, mark, marker, tabs)</small>
🔖 bookmark <small>(bookmark, mark)</small>
🏷 label <small>(label)</small>
💰 money bag <small>(bag, dollar, money, moneybag)</small>
💴 yen banknote <small>(banknote, bill, currency, money, note, yen)</small>
💵 dollar banknote <small>(banknote, bill, currency, dollar, money, note)</small>
💶 euro banknote <small>(banknote, bill, currency, euro, money, note)</small>
💷 pound banknote <small>(banknote, bill, currency, money, note, pound)</small>
💸 money with wings <small>(banknote, bill, fly, money, money with wings, wings)</small>
💳 credit card <small>(card, credit, money)</small>
🧾 receipt <small>(accounting, bookkeeping, evidence, proof, receipt)</small>
💹 chart increasing with yen <small>(chart, chart increasing with yen, graph, growth, money, yen)</small>
💱 currency exchange <small>(bank, currency, exchange, money)</small>
💲 heavy dollar sign <small>(currency, dollar, heavy dollar sign, money)</small>
✉ envelope <small>(email, envelope, letter)</small>
📧 e-mail <small>(e-mail, email, letter, mail)</small>
📨 incoming envelope <small>(e-mail, email, envelope, incoming, letter, receive)</small>
📩 envelope with arrow <small>(arrow, e-mail, email, envelope, envelope with arrow, outgoing)</small>
📤 outbox tray <small>(box, letter, mail, outbox, sent, tray)</small>
📥 inbox tray <small>(box, inbox, letter, mail, receive, tray)</small>
📦 package <small>(box, package, parcel)</small>
📫 closed mailbox with raised flag <small>(closed, closed mailbox with raised flag, mail, mailbox, postbox)</small>
📪 closed mailbox with lowered flag <small>(closed, closed mailbox with lowered flag, lowered, mail, mailbox, postbox)</small>
📬 open mailbox with raised flag <small>(mail, mailbox, open, open mailbox with raised flag, postbox)</small>
📭 open mailbox with lowered flag <small>(lowered, mail, mailbox, open, open mailbox with lowered flag, postbox)</small>
📮 postbox <small>(mail, mailbox, postbox)</small>
🗳 ballot box with ballot <small>(ballot, ballot box with ballot, box)</small>
✏ pencil <small>(pencil)</small>
✒ black nib <small>(black nib, nib, pen)</small>
🖋 fountain pen <small>(fountain, pen)</small>
🖊 pen <small>(ballpoint, pen)</small>
🖌 paintbrush <small>(paintbrush, painting)</small>
🖍 crayon <small>(crayon)</small>
📝 memo <small>(memo, pencil)</small>
💼 briefcase <small>(briefcase)</small>
📁 file folder <small>(file, folder)</small>
📂 open file folder <small>(file, folder, open)</small>
🗂 card index dividers <small>(card, dividers, index)</small>
📅 calendar <small>(calendar, date)</small>
📆 tear-off calendar <small>(calendar, tear-off calendar)</small>
🗒 spiral notepad <small>(note, pad, spiral, spiral notepad)</small>
🗓 spiral calendar <small>(calendar, pad, spiral)</small>
📇 card index <small>(card, index, rolodex)</small>
📈 chart increasing <small>(chart, chart increasing, graph, growth, trend, upward)</small>
📉 chart decreasing <small>(chart, chart decreasing, down, graph, trend)</small>
📊 bar chart <small>(bar, chart, graph)</small>
📋 clipboard <small>(clipboard)</small>
📌 pushpin <small>(pin, pushpin)</small>
📍 round pushpin <small>(pin, pushpin, round pushpin)</small>
📎 paperclip <small>(paperclip)</small>
🖇 linked paperclips <small>(link, linked paperclips, paperclip)</small>
📏 straight ruler <small>(ruler, straight edge, straight ruler)</small>
📐 triangular ruler <small>(ruler, set, triangle, triangular ruler)</small>
✂ scissors <small>(cutting, scissors, tool)</small>
🗃 card file box <small>(box, card, file)</small>
🗄 file cabinet <small>(cabinet, file, filing)</small>
🗑 wastebasket <small>(wastebasket)</small>
🔒 locked <small>(closed, locked)</small>
🔓 unlocked <small>(lock, open, unlock, unlocked)</small>
🔏 locked with pen <small>(ink, lock, locked with pen, nib, pen, privacy)</small>
🔐 locked with key <small>(closed, key, lock, locked with key, secure)</small>
🔑 key <small>(key, lock, password)</small>
🗝 old key <small>(clue, key, lock, old)</small>
🔨 hammer <small>(hammer, tool)</small>
🪓 axe <small>(axe, chop, hatchet, split, wood)</small>
⛏ pick <small>(mining, pick, tool)</small>
⚒ hammer and pick <small>(hammer, hammer and pick, pick, tool)</small>
🛠 hammer and wrench <small>(hammer, hammer and wrench, spanner, tool, wrench)</small>
🗡 dagger <small>(dagger, knife, weapon)</small>
⚔ crossed swords <small>(crossed, swords, weapon)</small>
🔫 pistol <small>(gun, handgun, pistol, revolver, tool, weapon)</small>
🏹 bow and arrow <small>(archer, arrow, bow, bow and arrow, Sagittarius, zodiac)</small>
🛡 shield <small>(shield, weapon)</small>
🔧 wrench <small>(spanner, tool, wrench)</small>
🔩 nut and bolt <small>(bolt, nut, nut and bolt, tool)</small>
⚙ gear <small>(cog, cogwheel, gear, tool)</small>
🗜 clamp <small>(clamp, compress, tool, vice)</small>
⚖ balance scale <small>(balance, justice, Libra, scale, zodiac)</small>
🦯 probing cane <small>(accessibility, blind, probing cane)</small>
🔗 link <small>(link)</small>
⛓ chains <small>(chain, chains)</small>
🧰 toolbox <small>(chest, mechanic, tool, toolbox)</small>
🧲 magnet <small>(attraction, horseshoe, magnet, magnetic)</small>
⚗ alembic <small>(alembic, chemistry, tool)</small>
🧪 test tube <small>(chemist, chemistry, experiment, lab, science, test tube)</small>
🧫 petri dish <small>(bacteria, biologist, biology, culture, lab, petri dish)</small>
🧬 dna <small>(biologist, dna, evolution, gene, genetics, life)</small>
🔬 microscope <small>(microscope, science, tool)</small>
🔭 telescope <small>(science, telescope, tool)</small>
📡 satellite antenna <small>(antenna, dish, satellite)</small>
💉 syringe <small>(medicine, needle, shot, sick, syringe)</small>
🩸 drop of blood <small>(bleed, blood donation, drop of blood, injury, medicine, menstruation)</small>
💊 pill <small>(doctor, medicine, pill, sick)</small>
🩹 adhesive bandage <small>(adhesive bandage, bandage)</small>
🩺 stethoscope <small>(doctor, heart, medicine, stethoscope)</small>
🚪 door <small>(door)</small>
🛏 bed <small>(bed, hotel, sleep)</small>
🛋 couch and lamp <small>(couch, couch and lamp, hotel, lamp)</small>
🪑 chair <small>(chair, seat, sit)</small>
🚽 toilet <small>(toilet)</small>
🚿 shower <small>(shower, water)</small>
🛁 bathtub <small>(bath, bathtub)</small>
🪒 razor <small>(razor, sharp, shave)</small>
🧴 lotion bottle <small>(lotion, lotion bottle, moisturizer, shampoo, sunscreen)</small>
🧷 safety pin <small>(diaper, punk rock, safety pin)</small>
🧹 broom <small>(broom, cleaning, sweeping, witch)</small>
🧺 basket <small>(basket, farming, laundry, picnic)</small>
🧻 roll of paper <small>(paper towels, roll of paper, toilet paper)</small>
🧼 soap <small>(bar, bathing, cleaning, lather, soap, soapdish)</small>
🧽 sponge <small>(absorbing, cleaning, porous, sponge)</small>
🧯 fire extinguisher <small>(extinguish, fire, fire extinguisher, quench)</small>
🛒 shopping cart <small>(cart, shopping, trolley)</small>
🚬 cigarette <small>(cigarette, smoking)</small>
⚰ coffin <small>(coffin, death)</small>
⚱ funeral urn <small>(ashes, death, funeral, urn)</small>
🗿 moai <small>(face, moai, moyai, statue)</small>
🏧 ATM sign <small>(atm, ATM sign, automated, bank, teller)</small>
🚮 litter in bin sign <small>(litter, litter bin, litter in bin sign)</small>
🚰 potable water <small>(drinking, potable, water)</small>
♿ wheelchair symbol <small>(access, wheelchair symbol)</small>
🚹 men’s room <small>(lavatory, man, men’s room, restroom, wc)</small>
🚺 women’s room <small>(lavatory, restroom, wc, woman, women’s room)</small>
🚻 restroom <small>(lavatory, restroom, WC)</small>
🚼 baby symbol <small>(baby, baby symbol, changing)</small>
🚾 water closet <small>(closet, lavatory, restroom, water, wc)</small>
🛂 passport control <small>(control, passport)</small>
🛃 customs <small>(customs)</small>
🛄 baggage claim <small>(baggage, claim)</small>
🛅 left luggage <small>(baggage, left luggage, locker, luggage)</small>
⚠ warning <small>(warning)</small>
🚸 children crossing <small>(child, children crossing, crossing, pedestrian, traffic)</small>
⛔ no entry <small>(entry, forbidden, no, not, prohibited, traffic)</small>
🚫 prohibited <small>(entry, forbidden, no, not, prohibited)</small>
🚳 no bicycles <small>(bicycle, bike, forbidden, no, no bicycles, prohibited)</small>
🚭 no smoking <small>(forbidden, no, not, prohibited, smoking)</small>
🚯 no littering <small>(forbidden, litter, no, no littering, not, prohibited)</small>
🚱 non-potable water <small>(non-drinking, non-potable, water)</small>
🚷 no pedestrians <small>(forbidden, no, no pedestrians, not, pedestrian, prohibited)</small>
📵 no mobile phones <small>(cell, forbidden, mobile, no, no mobile phones, phone)</small>
🔞 no one under eighteen <small>(18, age restriction, eighteen, no one under eighteen, prohibited, underage)</small>
☢ radioactive <small>(radioactive, sign)</small>
☣ biohazard <small>(biohazard, sign)</small>
⬆ up arrow <small>(arrow, cardinal, direction, north, up arrow)</small>
↗ up-right arrow <small>(arrow, direction, intercardinal, northeast, up-right arrow)</small>
➡ right arrow <small>(arrow, cardinal, direction, east, right arrow)</small>
↘ down-right arrow <small>(arrow, direction, down-right arrow, intercardinal, southeast)</small>
⬇ down arrow <small>(arrow, cardinal, direction, down, south)</small>
↙ down-left arrow <small>(arrow, direction, down-left arrow, intercardinal, southwest)</small>
⬅ left arrow <small>(arrow, cardinal, direction, left arrow, west)</small>
↖ up-left arrow <small>(arrow, direction, intercardinal, northwest, up-left arrow)</small>
↕ up-down arrow <small>(arrow, up-down arrow)</small>
↔ left-right arrow <small>(arrow, left-right arrow)</small>
↩ right arrow curving left <small>(arrow, right arrow curving left)</small>
↪ left arrow curving right <small>(arrow, left arrow curving right)</small>
⤴ right arrow curving up <small>(arrow, right arrow curving up)</small>
⤵ right arrow curving down <small>(arrow, down, right arrow curving down)</small>
🔃 clockwise vertical arrows <small>(arrow, clockwise, clockwise vertical arrows, reload)</small>
🔄 counterclockwise arrows button <small>(anticlockwise, arrow, counterclockwise, counterclockwise arrows button, withershins)</small>
🔙 BACK arrow <small>(arrow, back, BACK arrow)</small>
🔚 END arrow <small>(arrow, end, END arrow)</small>
🔛 ON! arrow <small>(arrow, mark, on, ON! arrow)</small>
🔜 SOON arrow <small>(arrow, soon, SOON arrow)</small>
🔝 TOP arrow <small>(arrow, top, TOP arrow, up)</small>
🛐 place of worship <small>(place of worship, religion, worship)</small>
⚛ atom symbol <small>(atheist, atom, atom symbol)</small>
🕉 om <small>(Hindu, om, religion)</small>
✡ star of David <small>(David, Jew, Jewish, religion, star, star of David)</small>
☸ wheel of dharma <small>(Buddhist, dharma, religion, wheel, wheel of dharma)</small>
☯ yin yang <small>(religion, tao, taoist, yang, yin)</small>
✝ latin cross <small>(Christian, cross, latin cross, religion)</small>
☦ orthodox cross <small>(Christian, cross, orthodox cross, religion)</small>
☪ star and crescent <small>(islam, Muslim, religion, star and crescent)</small>
☮ peace symbol <small>(peace, peace symbol)</small>
🕎 menorah <small>(candelabrum, candlestick, menorah, religion)</small>
🔯 dotted six-pointed star <small>(dotted six-pointed star, fortune, star)</small>
♈ Aries <small>(Aries, ram, zodiac)</small>
♉ Taurus <small>(bull, ox, Taurus, zodiac)</small>
♊ Gemini <small>(Gemini, twins, zodiac)</small>
♋ Cancer <small>(Cancer, crab, zodiac)</small>
♌ Leo <small>(Leo, lion, zodiac)</small>
♍ Virgo <small>(Virgo, zodiac)</small>
♎ Libra <small>(balance, justice, Libra, scales, zodiac)</small>
♏ Scorpio <small>(Scorpio, scorpion, scorpius, zodiac)</small>
♐ Sagittarius <small>(archer, Sagittarius, zodiac)</small>
♑ Capricorn <small>(Capricorn, goat, zodiac)</small>
♒ Aquarius <small>(Aquarius, bearer, water, zodiac)</small>
♓ Pisces <small>(fish, Pisces, zodiac)</small>
⛎ Ophiuchus <small>(bearer, Ophiuchus, serpent, snake, zodiac)</small>
🔀 shuffle tracks button <small>(arrow, crossed, shuffle tracks button)</small>
🔁 repeat button <small>(arrow, clockwise, repeat, repeat button)</small>
🔂 repeat single button <small>(arrow, clockwise, once, repeat single button)</small>
▶ play button <small>(arrow, play, play button, right, triangle)</small>
⏩ fast-forward button <small>(arrow, double, fast, fast-forward button, forward)</small>
⏭ next track button <small>(arrow, next scene, next track, next track button, triangle)</small>
⏯ play or pause button <small>(arrow, pause, play, play or pause button, right, triangle)</small>
◀ reverse button <small>(arrow, left, reverse, reverse button, triangle)</small>
⏪ fast reverse button <small>(arrow, double, fast reverse button, rewind)</small>
⏮ last track button <small>(arrow, last track button, previous scene, previous track, triangle)</small>
🔼 upwards button <small>(arrow, button, red, upwards button)</small>
⏫ fast up button <small>(arrow, double, fast up button)</small>
🔽 downwards button <small>(arrow, button, down, downwards button, red)</small>
⏬ fast down button <small>(arrow, double, down, fast down button)</small>
⏸ pause button <small>(bar, double, pause, pause button, vertical)</small>
⏹ stop button <small>(square, stop, stop button)</small>
⏺ record button <small>(circle, record, record button)</small>
⏏ eject button <small>(eject, eject button)</small>
🎦 cinema <small>(camera, cinema, film, movie)</small>
🔅 dim button <small>(brightness, dim, dim button, low)</small>
🔆 bright button <small>(bright, bright button, brightness)</small>
📶 antenna bars <small>(antenna, antenna bars, bar, cell, mobile, phone)</small>
📳 vibration mode <small>(cell, mobile, mode, phone, telephone, vibration)</small>
📴 mobile phone off <small>(cell, mobile, off, phone, telephone)</small>
♀ female sign <small>(female sign, woman)</small>
♂ male sign <small>(male sign, man)</small>
⚕ medical symbol <small>(aesculapius, medical symbol, medicine, staff)</small>
♾ infinity <small>(forever, infinity, unbounded, universal)</small>
♻ recycling symbol <small>(recycle, recycling symbol)</small>
⚜ fleur-de-lis <small>(fleur-de-lis)</small>
🔱 trident emblem <small>(anchor, emblem, ship, tool, trident)</small>
📛 name badge <small>(badge, name)</small>
🔰 Japanese symbol for beginner <small>(beginner, chevron, Japanese, Japanese symbol for beginner, leaf)</small>
⭕ hollow red circle <small>(circle, hollow red circle, large, o, red)</small>
✅ check mark button <small>(✓, button, check, mark)</small>
☑ check box with check <small>(✓, box, check, check box with check)</small>
✔ check mark <small>(✓, check, mark)</small>
✖ multiplication sign <small>(×, cancel, multiplication, multiply, sign, x)</small>
❌ cross mark <small>(×, cancel, cross, mark, multiplication, multiply, x)</small>
❎ cross mark button <small>(×, cross mark button, mark, square, x)</small>
➕ plus sign <small>(+, math, plus, sign)</small>
➖ minus sign <small>(-, −, math, minus, sign)</small>
➗ division sign <small>(÷, division, math, sign)</small>
➰ curly loop <small>(curl, curly loop, loop)</small>
➿ double curly loop <small>(curl, double, double curly loop, loop)</small>
〽 part alternation mark <small>(mark, part, part alternation mark)</small>
✳ eight-spoked asterisk <small>(*, asterisk, eight-spoked asterisk)</small>
✴ eight-pointed star <small>(*, eight-pointed star, star)</small>
❇ sparkle <small>(*, sparkle)</small>
‼ double exclamation mark <small>(!, !!, bangbang, double exclamation mark, exclamation, mark)</small>
⁉ exclamation question mark <small>(!, !?, ?, exclamation, interrobang, mark, punctuation, question)</small>
❓ question mark <small>(?, mark, punctuation, question)</small>
❔ white question mark <small>(?, mark, outlined, punctuation, question, white question mark)</small>
❕ white exclamation mark <small>(!, exclamation, mark, outlined, punctuation, white exclamation mark)</small>
❗ exclamation mark <small>(!, exclamation, mark, punctuation)</small>
〰 wavy dash <small>(dash, punctuation, wavy)</small>
© copyright <small>(c, copyright)</small>
® registered <small>(r, registered)</small>
™ trade mark <small>(mark, tm, trade mark, trademark)</small>
#️⃣ keycap: #
*️⃣ keycap: *
0️⃣ keycap: 0
1️⃣ keycap: 1
2️⃣ keycap: 2
3️⃣ keycap: 3
4️⃣ keycap: 4
5️⃣ keycap: 5
6️⃣ keycap: 6
7️⃣ keycap: 7
8️⃣ keycap: 8
9️⃣ keycap: 9
🔟 keycap: 10
🔠 input latin uppercase <small>(ABCD, input, latin, letters, uppercase)</small>
🔡 input latin lowercase <small>(abcd, input, latin, letters, lowercase)</small>
🔢 input numbers <small>(1234, input, numbers)</small>
🔣 input symbols <small>(〒♪&amp;%, input, input symbols)</small>
🔤 input latin letters <small>(abc, alphabet, input, latin, letters)</small>
🅰 A button (blood type) <small>(a, A button (blood type), blood type)</small>
🆎 AB button (blood type) <small>(ab, AB button (blood type), blood type)</small>
🅱 B button (blood type) <small>(b, B button (blood type), blood type)</small>
🆑 CL button <small>(cl, CL button)</small>
🆒 COOL button <small>(cool, COOL button)</small>
🆓 FREE button <small>(free, FREE button)</small>
ℹ information <small>(i, information)</small>
🆔 ID button <small>(id, ID button, identity)</small>
Ⓜ circled M <small>(circle, circled M, m)</small>
🆕 NEW button <small>(new, NEW button)</small>
🆖 NG button <small>(ng, NG button)</small>
🅾 O button (blood type) <small>(blood type, o, O button (blood type))</small>
🆗 OK button <small>(OK, OK button)</small>
🅿 P button <small>(P button, parking)</small>
🆘 SOS button <small>(help, sos, SOS button)</small>
🆙 UP! button <small>(mark, up, UP! button)</small>
🆚 VS button <small>(versus, vs, VS button)</small>
🈁 Japanese “here” button <small>(“here”, Japanese, Japanese “here” button, katakana, ココ)</small>
🈂 Japanese “service charge” button <small>(“service charge”, Japanese, Japanese “service charge” button, katakana, サ)</small>
🈷 Japanese “monthly amount” button <small>(“monthly amount”, ideograph, Japanese, Japanese “monthly amount” button, 月)</small>
🈶 Japanese “not free of charge” button <small>(“not free of charge”, ideograph, Japanese, Japanese “not free of charge” button, 有)</small>
🈯 Japanese “reserved” button <small>(“reserved”, ideograph, Japanese, Japanese “reserved” button, 指)</small>
🉐 Japanese “bargain” button <small>(“bargain”, ideograph, Japanese, Japanese “bargain” button, 得)</small>
🈹 Japanese “discount” button <small>(“discount”, ideograph, Japanese, Japanese “discount” button, 割)</small>
🈚 Japanese “free of charge” button <small>(“free of charge”, ideograph, Japanese, Japanese “free of charge” button, 無)</small>
🈲 Japanese “prohibited” button <small>(“prohibited”, ideograph, Japanese, Japanese “prohibited” button, 禁)</small>
🉑 Japanese “acceptable” button <small>(“acceptable”, ideograph, Japanese, Japanese “acceptable” button, 可)</small>
🈸 Japanese “application” button <small>(“application”, ideograph, Japanese, Japanese “application” button, 申)</small>
🈴 Japanese “passing grade” button <small>(“passing grade”, ideograph, Japanese, Japanese “passing grade” button, 合)</small>
🈳 Japanese “vacancy” button <small>(“vacancy”, ideograph, Japanese, Japanese “vacancy” button, 空)</small>
㊗ Japanese “congratulations” button <small>(“congratulations”, ideograph, Japanese, Japanese “congratulations” button, 祝)</small>
㊙ Japanese “secret” button <small>(“secret”, ideograph, Japanese, Japanese “secret” button, 秘)</small>
🈺 Japanese “open for business” button <small>(“open for business”, ideograph, Japanese, Japanese “open for business” button, 営)</small>
🈵 Japanese “no vacancy” button <small>(“no vacancy”, ideograph, Japanese, Japanese “no vacancy” button, 満)</small>
🔴 red circle <small>(circle, geometric, red)</small>
🟠 orange circle <small>(circle, orange)</small>
🟡 yellow circle <small>(circle, yellow)</small>
🟢 green circle <small>(circle, green)</small>
🔵 blue circle <small>(blue, circle, geometric)</small>
🟣 purple circle <small>(circle, purple)</small>
🟤 brown circle <small>(brown, circle)</small>
⚫ black circle <small>(black circle, circle, geometric)</small>
⚪ white circle <small>(circle, geometric, white circle)</small>
🟥 red square <small>(red, square)</small>
🟧 orange square <small>(orange, square)</small>
🟨 yellow square <small>(square, yellow)</small>
🟩 green square <small>(green, square)</small>
🟦 blue square <small>(blue, square)</small>
🟪 purple square <small>(purple, square)</small>
🟫 brown square <small>(brown, square)</small>
⬛ black large square <small>(black large square, geometric, square)</small>
⬜ white large square <small>(geometric, square, white large square)</small>
◼ black medium square <small>(black medium square, geometric, square)</small>
◻ white medium square <small>(geometric, square, white medium square)</small>
◾ black medium-small square <small>(black medium-small square, geometric, square)</small>
◽ white medium-small square <small>(geometric, square, white medium-small square)</small>
▪ black small square <small>(black small square, geometric, square)</small>
▫ white small square <small>(geometric, square, white small square)</small>
🔶 large orange diamond <small>(diamond, geometric, large orange diamond, orange)</small>
🔷 large blue diamond <small>(blue, diamond, geometric, large blue diamond)</small>
🔸 small orange diamond <small>(diamond, geometric, orange, small orange diamond)</small>
🔹 small blue diamond <small>(blue, diamond, geometric, small blue diamond)</small>
🔺 red triangle pointed up <small>(geometric, red, red triangle pointed up)</small>
🔻 red triangle pointed down <small>(down, geometric, red, red triangle pointed down)</small>
💠 diamond with a dot <small>(comic, diamond, diamond with a dot, geometric, inside)</small>
🔘 radio button <small>(button, geometric, radio)</small>
🔳 white square button <small>(button, geometric, outlined, square, white square button)</small>
🔲 black square button <small>(black square button, button, geometric, square)</small>
🏁 chequered flag <small>(checkered, chequered, chequered flag, racing)</small>
🚩 triangular flag <small>(post, triangular flag)</small>
🎌 crossed flags <small>(celebration, cross, crossed, crossed flags, Japanese)</small>
🏴 black flag <small>(black flag, waving)</small>
🏳 white flag <small>(waving, white flag)</small>
🏳️‍🌈 rainbow flag
🏴‍☠️ pirate flag
🇦🇨 flag: Ascension Island
🇦🇩 flag: Andorra
🇦🇪 flag: United Arab Emirates
🇦🇫 flag: Afghanistan
🇦🇬 flag: Antigua &amp; Barbuda
🇦🇮 flag: Anguilla
🇦🇱 flag: Albania
🇦🇲 flag: Armenia
🇦🇴 flag: Angola
🇦🇶 flag: Antarctica
🇦🇷 flag: Argentina
🇦🇸 flag: American Samoa
🇦🇹 flag: Austria
🇦🇺 flag: Australia
🇦🇼 flag: Aruba
🇦🇽 flag: Åland Islands
🇦🇿 flag: Azerbaijan
🇧🇦 flag: Bosnia &amp; Herzegovina
🇧🇧 flag: Barbados
🇧🇩 flag: Bangladesh
🇧🇪 flag: Belgium
🇧🇫 flag: Burkina Faso
🇧🇬 flag: Bulgaria
🇧🇭 flag: Bahrain
🇧🇮 flag: Burundi
🇧🇯 flag: Benin
🇧🇱 flag: St. Barthélemy
🇧🇲 flag: Bermuda
🇧🇳 flag: Brunei
🇧🇴 flag: Bolivia
🇧🇶 flag: Caribbean Netherlands
🇧🇷 flag: Brazil
🇧🇸 flag: Bahamas
🇧🇹 flag: Bhutan
🇧🇻 flag: Bouvet Island
🇧🇼 flag: Botswana
🇧🇾 flag: Belarus
🇧🇿 flag: Belize
🇨🇦 flag: Canada
🇨🇨 flag: Cocos (Keeling) Islands
🇨🇩 flag: Congo - Kinshasa
🇨🇫 flag: Central African Republic
🇨🇬 flag: Congo - Brazzaville
🇨🇭 flag: Switzerland
🇨🇮 flag: Côte d’Ivoire
🇨🇰 flag: Cook Islands
🇨🇱 flag: Chile
🇨🇲 flag: Cameroon
🇨🇳 flag: China
🇨🇴 flag: Colombia
🇨🇵 flag: Clipperton Island
🇨🇷 flag: Costa Rica
🇨🇺 flag: Cuba
🇨🇻 flag: Cape Verde
🇨🇼 flag: Curaçao
🇨🇽 flag: Christmas Island
🇨🇾 flag: Cyprus
🇨🇿 flag: Czechia
🇩🇪 flag: Germany
🇩🇬 flag: Diego Garcia
🇩🇯 flag: Djibouti
🇩🇰 flag: Denmark
🇩🇲 flag: Dominica
🇩🇴 flag: Dominican Republic
🇩🇿 flag: Algeria
🇪🇦 flag: Ceuta &amp; Melilla
🇪🇨 flag: Ecuador
🇪🇪 flag: Estonia
🇪🇬 flag: Egypt
🇪🇭 flag: Western Sahara
🇪🇷 flag: Eritrea
🇪🇸 flag: Spain
🇪🇹 flag: Ethiopia
🇪🇺 flag: European Union
🇫🇮 flag: Finland
🇫🇯 flag: Fiji
🇫🇰 flag: Falkland Islands
🇫🇲 flag: Micronesia
🇫🇴 flag: Faroe Islands
🇫🇷 flag: France
🇬🇦 flag: Gabon
🇬🇧 flag: United Kingdom
🇬🇩 flag: Grenada
🇬🇪 flag: Georgia
🇬🇫 flag: French Guiana
🇬🇬 flag: Guernsey
🇬🇭 flag: Ghana
🇬🇮 flag: Gibraltar
🇬🇱 flag: Greenland
🇬🇲 flag: Gambia
🇬🇳 flag: Guinea
🇬🇵 flag: Guadeloupe
🇬🇶 flag: Equatorial Guinea
🇬🇷 flag: Greece
🇬🇸 flag: South Georgia &amp; South Sandwich Islands
🇬🇹 flag: Guatemala
🇬🇺 flag: Guam
🇬🇼 flag: Guinea-Bissau
🇬🇾 flag: Guyana
🇭🇰 flag: Hong Kong SAR China
🇭🇲 flag: Heard &amp; McDonald Islands
🇭🇳 flag: Honduras
🇭🇷 flag: Croatia
🇭🇹 flag: Haiti
🇭🇺 flag: Hungary
🇮🇨 flag: Canary Islands
🇮🇩 flag: Indonesia
🇮🇪 flag: Ireland
🇮🇱 flag: Israel
🇮🇲 flag: Isle of Man
🇮🇳 flag: India
🇮🇴 flag: British Indian Ocean Territory
🇮🇶 flag: Iraq
🇮🇷 flag: Iran
🇮🇸 flag: Iceland
🇮🇹 flag: Italy
🇯🇪 flag: Jersey
🇯🇲 flag: Jamaica
🇯🇴 flag: Jordan
🇯🇵 flag: Japan
🇰🇪 flag: Kenya
🇰🇬 flag: Kyrgyzstan
🇰🇭 flag: Cambodia
🇰🇮 flag: Kiribati
🇰🇲 flag: Comoros
🇰🇳 flag: St. Kitts &amp; Nevis
🇰🇵 flag: North Korea
🇰🇷 flag: South Korea
🇰🇼 flag: Kuwait
🇰🇾 flag: Cayman Islands
🇰🇿 flag: Kazakhstan
🇱🇦 flag: Laos
🇱🇧 flag: Lebanon
🇱🇨 flag: St. Lucia
🇱🇮 flag: Liechtenstein
🇱🇰 flag: Sri Lanka
🇱🇷 flag: Liberia
🇱🇸 flag: Lesotho
🇱🇹 flag: Lithuania
🇱🇺 flag: Luxembourg
🇱🇻 flag: Latvia
🇱🇾 flag: Libya
🇲🇦 flag: Morocco
🇲🇨 flag: Monaco
🇲🇩 flag: Moldova
🇲🇪 flag: Montenegro
🇲🇫 flag: St. Martin
🇲🇬 flag: Madagascar
🇲🇭 flag: Marshall Islands
🇲🇰 flag: North Macedonia
🇲🇱 flag: Mali
🇲🇲 flag: Myanmar (Burma)
🇲🇳 flag: Mongolia
🇲🇴 flag: Macao SAR China
🇲🇵 flag: Northern Mariana Islands
🇲🇶 flag: Martinique
🇲🇷 flag: Mauritania
🇲🇸 flag: Montserrat
🇲🇹 flag: Malta
🇲🇺 flag: Mauritius
🇲🇻 flag: Maldives
🇲🇼 flag: Malawi
🇲🇽 flag: Mexico
🇲🇾 flag: Malaysia
🇲🇿 flag: Mozambique
🇳🇦 flag: Namibia
🇳🇨 flag: New Caledonia
🇳🇪 flag: Niger
🇳🇫 flag: Norfolk Island
🇳🇬 flag: Nigeria
🇳🇮 flag: Nicaragua
🇳🇱 flag: Netherlands
🇳🇴 flag: Norway
🇳🇵 flag: Nepal
🇳🇷 flag: Nauru
🇳🇺 flag: Niue
🇳🇿 flag: New Zealand
🇴🇲 flag: Oman
🇵🇦 flag: Panama
🇵🇪 flag: Peru
🇵🇫 flag: French Polynesia
🇵🇬 flag: Papua New Guinea
🇵🇭 flag: Philippines
🇵🇰 flag: Pakistan
🇵🇱 flag: Poland
🇵🇲 flag: St. Pierre &amp; Miquelon
🇵🇳 flag: Pitcairn Islands
🇵🇷 flag: Puerto Rico
🇵🇸 flag: Palestinian Territories
🇵🇹 flag: Portugal
🇵🇼 flag: Palau
🇵🇾 flag: Paraguay
🇶🇦 flag: Qatar
🇷🇪 flag: Réunion
🇷🇴 flag: Romania
🇷🇸 flag: Serbia
🇷🇺 flag: Russia
🇷🇼 flag: Rwanda
🇸🇦 flag: Saudi Arabia
🇸🇧 flag: Solomon Islands
🇸🇨 flag: Seychelles
🇸🇩 flag: Sudan
🇸🇪 flag: Sweden
🇸🇬 flag: Singapore
🇸🇭 flag: St. Helena
🇸🇮 flag: Slovenia
🇸🇯 flag: Svalbard &amp; Jan Mayen
🇸🇰 flag: Slovakia
🇸🇱 flag: Sierra Leone
🇸🇲 flag: San Marino
🇸🇳 flag: Senegal
🇸🇴 flag: Somalia
🇸🇷 flag: Suriname
🇸🇸 flag: South Sudan
🇸🇹 flag: São Tomé &amp; Príncipe
🇸🇻 flag: El Salvador
🇸🇽 flag: Sint Maarten
🇸🇾 flag: Syria
🇸🇿 flag: Eswatini
🇹🇦 flag: Tristan da Cunha
🇹🇨 flag: Turks &amp; Caicos Islands
🇹🇩 flag: Chad
🇹🇫 flag: French Southern Territories
🇹🇬 flag: Togo
🇹🇭 flag: Thailand
🇹🇯 flag: Tajikistan
🇹🇰 flag: Tokelau
🇹🇱 flag: Timor-Leste
🇹🇲 flag: Turkmenistan
🇹🇳 flag: Tunisia
🇹🇴 flag: Tonga
🇹🇷 flag: Turkey
🇹🇹 flag: Trinidad &amp; Tobago
🇹🇻 flag: Tuvalu
🇹🇼 flag: Taiwan
🇹🇿 flag: Tanzania
🇺🇦 flag: Ukraine
🇺🇬 flag: Uganda
🇺🇲 flag: U.S. Outlying Islands
🇺🇳 flag: United Nations
🇺🇸 flag: United States
🇺🇾 flag: Uruguay
🇺🇿 flag: Uzbekistan
🇻🇦 flag: Vatican City
🇻🇨 flag: St. Vincent &amp; Grenadines
🇻🇪 flag: Venezuela
🇻🇬 flag: British Virgin Islands
🇻🇮 flag: U.S. Virgin Islands
🇻🇳 flag: Vietnam
🇻🇺 flag: Vanuatu
🇼🇫 flag: Wallis &amp; Futuna
🇼🇸 flag: Samoa
🇽🇰 flag: Kosovo
🇾🇪 flag: Yemen
🇾🇹 flag: Mayotte
🇿🇦 flag: South Africa
🇿🇲 flag: Zambia
🇿🇼 flag: Zimbabwe
🏴󠁧󠁢󠁥󠁮󠁧󠁿 flag: England
🏴󠁧󠁢󠁳󠁣󠁴󠁿 flag: Scotland
🏴󠁧󠁢󠁷󠁬󠁳󠁿 flag: Wales
"""

skin_tone_selectable_emojis = {'☝', '⛹', '✊', '✋', '✌', '✍', '🎅', '🏂', '🏃', '🏄', '🏇', '🏊',
                               '🏋', '🏌', '👂', '👃', '👆', '👇', '👈', '👉', '👊', '👋', '👌',
                               '👍', '👎', '👏', '👐', '👦', '👧', '👨', '👩', '👪', '👫', '👬',
                               '👭', '👮', '👯', '👰', '👱', '👲', '👳', '👴', '👵', '👶', '👷',
                               '👸', '👼', '💁', '💂', '💃', '💅', '💆', '💇', '💏', '💑', '💪',
                               '🕴', '🕵', '🕺', '🖐', '🖕', '🖖', '🙅', '🙆', '🙇', '🙋', '🙌',
                               '🙍', '🙎', '🙏', '🚣', '🚴', '🚵', '🚶', '🛀', '🛌', '🤏', '🤘',
                               '🤙', '🤚', '🤛', '🤜', '🤝', '🤞', '🤟', '🤦', '🤰', '🤱', '🤲',
                               '🤳', '🤴', '🤵', '🤶', '🤷', '🤸', '🤹', '🤼', '🤽', '🤾', '🦵',
                               '🦶', '🦸', '🦹', '🦻', '🧍', '🧎', '🧏', '🧑', '🧒', '🧓', '🧔',
                               '🧕', '🧖', '🧗', '🧘', '🧙', '🧚', '🧛', '🧜', '🧝'}

fitzpatrick_modifiers = {
    '': 'neutral',
    '🏻': 'light skin',
    '🏼': 'medium-light skin',
    '🏽': 'moderate skin',
    '🏾': 'dark brown skin',
    '🏿': 'black skin'
}

fitzpatrick_modifiers_reversed = {" ".join(name.split()[:-1]): modifier for modifier, name in
                                  fitzpatrick_modifiers.items() if name != "neutral"}


def main() -> None:
    args = parse_arguments()
    active_window = get_active_window()

    returncode, stdout = open_main_rofi_window(args.rofi_args, load_emojis(args.file))

    if returncode == 1:
        sys.exit()
    else:
        emojis = compile_chosen_emojis(stdout.splitlines(), args.skin_tone, args.rofi_args)

        if returncode == 0:
            if args.copy_only:
                copy_emojis_to_clipboard(emojis)
            else:
                insert_emojis(emojis, active_window, args.insert_with_clipboard)
        elif returncode == 10:
            copy_emojis_to_clipboard(emojis)
        elif returncode == 11:
            type_emojis(emojis, active_window)
        elif returncode == 12:
            copy_paste_emojis(emojis, active_window)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Select, insert or copy Unicode emojis using rofi')
    parser.add_argument('--version', action='version', version='rofimoji 4.0.0-SNAPSHOT')
    parser.add_argument(
        '--insert-with-clipboard',
        '-p',
        dest='insert_with_clipboard',
        action='store_true',
        help='Do not type the emoji directly, but copy it to the clipboard, insert it from there '
             'and then restore the clipboard\'s original value '
    )
    parser.add_argument(
        '--copy-only',
        '-c',
        dest='copy_only',
        action='store_true',
        help='Only copy the emoji to the clipboard but do not insert it'
    )
    parser.add_argument(
        '--skin-tone',
        '-s',
        dest='skin_tone',
        action='store',
        choices=['neutral', 'light', 'medium-light', 'moderate', 'dark brown', 'black', 'ask'],
        default='ask',
        help='Decide on a skin-tone for all supported emojis. If not set (or set to "ask"), '
             'you will be asked for each one '
    )
    parser.add_argument(
        '--emoji-file',
        '-f',
        dest='file',
        action='store',
        default=None,
        help='Read emojis from this file instead, one entry per line'
    )
    parser.add_argument(
        '--rofi-args',
        dest='rofi_args',
        action='store',
        default='',
        help='A string of arguments to give to rofi'
    )
    parsed_args = parser.parse_args()
    parsed_args.rofi_args = parsed_args.rofi_args.split()

    return parsed_args


def get_active_window() -> str:
    xdotool = Popen(args=['xdotool', 'getactivewindow'], stdout=PIPE)
    return xdotool.communicate()[0].decode("utf-8")[:-1]


def load_emojis(file_name: Union[str, None]):
    if file_name is not None:
        try:
            with open(file_name, "r") as file:
                return file.read()
        except IOError:
            return emoji_list
    else:
        return emoji_list


def open_main_rofi_window(args: List[str], emojis: str) -> Tuple[int, bytes]:
    rofi = Popen(
        [
            'rofi',
            '-dmenu',
            '-markup-rows',
            '-i',
            '-multi-select',
            '-p',
            ' 😀   ',
            '-kb-custom-1',
            'Alt+c',
            '-kb-custom-2',
            'Alt+t',
            '-kb-custom-3',
            'Alt+p',
            *args
        ],
        stdin=PIPE,
        stdout=PIPE
    )
    (stdout, _) = rofi.communicate(input=emojis.encode('UTF-8'))
    return rofi.returncode, stdout


def compile_chosen_emojis(chosen_emojis: List[bytes], skin_tone: str, rofi_args: List[str]) -> str:
    emojis = ""
    for line in chosen_emojis:
        emoji = line.decode('utf-8').split()[0]

        if emoji in skin_tone_selectable_emojis:
            emoji = select_skin_tone(emoji, skin_tone, rofi_args)

        emojis += emoji

    return emojis


def select_skin_tone(selected_emoji: chr, skin_tone: str, rofi_args: List[str]) -> str:
    if skin_tone == 'neutral':
        return selected_emoji
    elif skin_tone != 'ask':
        return selected_emoji + fitzpatrick_modifiers_reversed[skin_tone]
    else:
        modified_emojis = '\n'.join(map(
            lambda modifier: selected_emoji + modifier + " " + fitzpatrick_modifiers[modifier],
            fitzpatrick_modifiers.keys()
        ))

        rofi_skin = Popen(
            [
                'rofi',
                '-dmenu',
                '-i',
                '-p',
                selected_emoji + '   ',
                *rofi_args
            ],
            stdin=PIPE,
            stdout=PIPE
        )

        (stdout_skin, _) = rofi_skin.communicate(input=modified_emojis.encode('utf-8'))

        if rofi_skin.returncode == 1:
            return ''

        return stdout_skin.split()[0].decode('utf-8')


def insert_emojis(emojis: str, active_window: str, insert_with_clipboard: bool = False) -> None:
    if insert_with_clipboard:
        copy_paste_emojis(emojis, active_window)
    else:
        type_emojis(emojis, active_window)


def copy_paste_emojis(emojis: str, active_window: str) -> None:
    old_clipboard_content = Popen(args=['xsel', '-o', '-b'], stdout=PIPE) \
        .communicate()[0]
    old_primary_content = Popen(args=['xsel', '-o', '-p'], stdout=PIPE) \
        .communicate()[0]

    Popen(args=['xsel', '-i', '-b'], stdin=PIPE) \
        .communicate(input=emojis.encode('utf-8'))
    Popen(args=['xsel', '-i', '-p'], stdin=PIPE) \
        .communicate(input=emojis.encode('utf-8'))

    Popen([
        'xdotool',
        'windowfocus',
        '--sync',
        active_window,
        'key',
        '--clearmodifiers',
        'Shift+Insert',
        'sleep',
        '0.05',
    ]).wait()

    Popen(args=['xsel', '-i', '-b'], stdin=PIPE) \
        .communicate(input=old_clipboard_content)
    Popen(args=['xsel', '-i', '-p'], stdin=PIPE) \
        .communicate(input=old_primary_content)


def type_emojis(emojis: str, active_window: str) -> None:
    Popen([
        'xdotool',
        'type',
        '--clearmodifiers',
        '--window',
        active_window,
        emojis
    ])


def copy_emojis_to_clipboard(emojis: str) -> None:
    xsel = Popen(
        [
            'xsel',
            '-i',
            '-b'
        ],
        stdin=PIPE
    )
    xsel.communicate(input=emojis.encode('utf-8'))


if __name__ == "__main__":
    main()
