import random

from discord import Colour, Embed
from functools import cached_property
from typing import List
from unidecode import unidecode


RUNE_COLOUR = Colour.from_rgb(75, 157, 143)


class Rune:
    def __init__(
        self,
        symbol: str,
        transliteration: str,
        meaning: str,
        poem_oe: List[str],
        poem_en: List[str],
        url: str,
    ):
        self.symbol = symbol
        self.transliteration = transliteration
        self.meaning = meaning
        self.poem_oe = poem_oe
        self.poem_en = poem_en
        self.url = url

    @cached_property
    def discord_string(self) -> str:
        return "**{0}** ({1})\n{2}\n\n{3}".format(
            self.transliteration,
            self.symbol,
            "\n".join(["> {0}".format(line) for line in self.poem_oe]),
            "\n".join(["> {0}".format(line) for line in self.poem_en]),
        )

    @cached_property
    def embed(self) -> Embed:
        description = "{0}\n\n{1}\n\n{2}".format(
            self.meaning,
            "\n".join(["> {0}".format(line) for line in self.poem_oe]),
            "\n".join(["> {0}".format(line) for line in self.poem_en]),
        )
        return Embed(
            title=f"{self.symbol} · {self.transliteration}",
            description=description,
            colour=RUNE_COLOUR,
            url=self.url,
        )


class RuneDatabase:
    def __init__(self, runes: List[Rune] = []):
        self.runes = runes

    def search(self, query: str) -> Rune | None:
        for rune in self.runes:
            if unidecode(rune.transliteration) == unidecode(query):
                return rune
        return None

    def random(self) -> Rune:
        return random.choice(self.runes)

    @cached_property
    def discord_string(self) -> str:
        return "\n".join(
            [f"• {rune.symbol} · {rune.transliteration}" for rune in self.runes]
        )

    @classmethod
    def construct(cls):
        return cls(
            [
                Rune(
                    "ᚠ",
                    "feoh",
                    "wealth",
                    [
                        "feoh byþ frófur fira gehwylcum;",
                        "sceal ðéah manna gehwylc miclun hyt dǽlan",
                        "gif hé wile for drihtne dómes hléotan.",
                    ],
                    [
                        "wealth is a comfort to all men;",
                        "yet must every man bestow it freely,",
                        "if he wish to gain honour in the sight of the lord.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%a0-feoh/",
                ),
                Rune(
                    "ᚢ",
                    "úr",
                    "aurochs",
                    [
                        "úr byþ anmód and oferhyrned,",
                        "felafrécne déor, feohteþ mid hornum",
                        "mǽre mórstapa; þæt is módig wuht!",
                    ],
                    [
                        "the aurochs is proud and has great horns;",
                        "it is a very savage beast and fights with its horns",
                        "a great ranger of the moors, it is a creature of mettle.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%a2-ur/",
                ),
                Rune(
                    "ᚦ",
                    "þorn",
                    "thorn",
                    [
                        "ðorn byþ ðearla scearp; ðegna gehwyclum",
                        "anfengys yfyl, ungemetum réþe",
                        "manna gehwylcun, ðe him mid resteð.",
                    ],
                    [
                        "the thorn is exceedingly sharp,",
                        "an evil thing for any knight to touch,",
                        "uncommonly severe on all who sit among them.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%a6-dorn/",
                ),
                Rune(
                    "ᚩ",
                    "ós",
                    "god",
                    [
                        "ós byþ ordfruma ǽlere sprǽce,",
                        "wísdómes wraþu ond witena frófur",
                        "and eorla gehwám éadnys ond tóhiht.",
                    ],
                    [
                        "god is the source of all language,",
                        "a pillar of wisdom and a comfort to wise men,",
                        "a blessing and a joy to every knight.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%a9-os/",
                ),
                Rune(
                    "ᚱ",
                    "rád",
                    "riding",
                    [
                        "rád byþ on recyde rinca gehwyclum",
                        "séfte, and swíþhwæt ðámðe sitteþ on ufan",
                        "méare mægenheardum ofer mílpaþas.",
                    ],
                    [
                        "riding seems easy to every warrior while he is indoors",
                        "and very courageous to him who traverses the high-roads",
                        "on the back of a stout horse.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%b1-rad/",
                ),
                Rune(
                    "ᚳ",
                    "cén",
                    "torch",
                    [
                        "cén byþ cwicera gehwám, cúþ on fýre",
                        "blác ond beorhtlíc, byrneþ oftust",
                        "dǽr hí æþelingas inne restaþ.",
                    ],
                    [
                        "the torch is known to every living man",
                        "by its pale, bright flame; it always burns",
                        "where princes sit within.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%b3-cen/",
                ),
                Rune(
                    "ᚷ",
                    "giefu",
                    "gift",
                    [
                        "giefu gumena byþ gleng and herenys,",
                        "wraþu and wyrþscype and wræcna gehwám",
                        "ár and ætwist, ðe byþ óþra leas.",
                    ],
                    [
                        "generosity brings credit and honour, which",
                        "support one's dignity; it furnishes help",
                        "and subsistence to all broken men",
                        "who are devoid of aught else.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%b7-gyfu/",
                ),
                Rune(
                    "ᚹ",
                    "wynn",
                    "bliss",
                    [
                        "wynn ne brúceþ, ðe can wéana lýt",
                        "sáres and sorge and him sylfa hæfþ",
                        "blǽd and blysse and éac byrga geniht.",
                    ],
                    [
                        "bliss he enjoys who knows not suffering,",
                        "sorrow nor anxiety, and has prosperity",
                        "and happiness and a good enough house.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%b9-wyn/",
                ),
                Rune(
                    "ᚻ",
                    "hægl",
                    "hail",
                    [
                        "hægl byþ hwítust corna;",
                        "hwyrft hit of heofones lyfte,",
                        "wealcaþ hit windes scúra;",
                        "weorþeþ hit tó wætere syððan.",
                    ],
                    [
                        "hail is the whitest of grain;",
                        "it is whirled from the vault of heaven",
                        "and it is tossed about by gusts of wind",
                        "and then it melts into water.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%bb-haegl/",
                ),
                Rune(
                    "ᚾ",
                    "nýd",
                    "trouble",
                    [
                        "nýd byþ nearu on bréostan;",
                        "weorþeþ hí ðéah oft niþa bearnum",
                        "tó helpe and tó hǽle gehwæþre,",
                        "gif hí his hlystaþ ǽror.",
                    ],
                    [
                        "trouble is oppressive to the heart;",
                        "yet often it proves a source of help and salvation",
                        "to the children of men, to everyone who heeds it betimes.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%be-nyd/",
                ),
                Rune(
                    "ᛁ",
                    "ís",
                    "ice",
                    [
                        "ís byþ oferceald, ungemetum slidor",
                        "glisnaþ glæshlúttur gimmum gelícust",
                        "flór forste geworuht, fæger ansýne.",
                    ],
                    [
                        "ice is very cold and immeasurably slippery;",
                        "it glistens as clear as glass and most like to gems;",
                        "it is a floor wrought by the frost, fair to look upon.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%81-is/",
                ),
                Rune(
                    "ᛄ",
                    "géar",
                    "summer",
                    [
                        "géar byþ gumena hiht, ðon God lǽteþ,",
                        "hálig heofones cyning, hrúsan syllan",
                        "beorhte bléda beornum and ðearfum.",
                    ],
                    [
                        "summer is a joy to all men, when God,",
                        "the holy King of Heaven, suffers the earth to",
                        "bring forth shining fruits for rich and poor alike.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%84-ger/",
                ),
                Rune(
                    "ᛇ",
                    "éoh",
                    "yew",
                    [
                        "éoh byþ útan unsméþe tréow,",
                        "heard hrúsan fæst, hyrde fýres,",
                        "wyrtrumun underwreþyd, wynan on éþle.",
                    ],
                    [
                        "the yew is a tree with rough bark,",
                        "hard and fast in the earth, supported by its roots,",
                        "a guardian of flame and a joy upon an estate.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%87-eoh/",
                ),
                Rune(
                    "ᛈ",
                    "peorð",
                    "game(?)",
                    [
                        "peorð byþ symble plega and hlehter",
                        "wlancum [...], ðár wigan sittaþ",
                        "on béorsele blíþe ætsomne.",
                    ],
                    [
                        "the game(?) is ever play and laughter,",
                        "to the proud [...], where warriors sit",
                        "in the beer-hall blithe together.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%88-poerd/",
                ),
                Rune(
                    "ᛉ",
                    "eolhxsecg",
                    "elk grass",
                    [
                        "eolhxsecg eard hæfþ oftust on fenne",
                        "wexeð on wature, wundaþ grimme,",
                        "blode bréneð beorna gewylcne",
                        "ðe him ǽnigne onfeng gedéð.",
                    ],
                    [
                        "elk grass is mostly to be found in a marsh;",
                        "it grows in the water and makes a ghastly wound,",
                        "covering with blood every warrior who touches it.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%89-eolhxsecg/",
                ),
                Rune(
                    "ᛋ",
                    "sigel",
                    "sun",
                    [
                        "sigel sémannum symble biþ on hihte,",
                        "ðonn hí hine feriaþ ofer fisces beþ,",
                        "oþ hí brimhengest bringeþ tó lande.",
                    ],
                    [
                        "the sun is ever a joy in the hopes of seafarers",
                        "when they journey away over the fishes' bath,",
                        "until the courser of the deep bears them to land.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%8b-sigel/",
                ),
                Rune(
                    "ᛏ",
                    "tír",
                    "Tiw",
                    [
                        "tír biþ tácna sum, healdeð trýwa wel",
                        "wiþ æþelingas; á biþ on færylde",
                        "ofer nihta genipu, nǽfre swíceþ.",
                    ],
                    [
                        "Tiw is a guiding star;",
                        "well does it keep faith with princes;",
                        "it is ever on its course over the mists of night",
                        "and never fails.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%8f-tir/",
                ),
                Rune(
                    "ᛒ",
                    "beorc",
                    "poplar, birch",
                    [
                        "beorc byþ bléda léas, bereþ efne swá ðéah",
                        "tánas bútan túdder, biþ on telgum wlitig,",
                        "héah on helme hrysted fægere,",
                        "geloden léafum, lyfte getenge.",
                    ],
                    [
                        "the poplar bears no fruit; yet without seed",
                        "it brings forth suckers, for it is generated from its leaves.",
                        "Splendid are its branches and gloriously adorned",
                        "its lofty crown which reaches to the skies.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%92-beorc/",
                ),
                Rune(
                    "ᛖ",
                    "eh",
                    "horse",
                    [
                        "eh byþ for eorlum æþelinga wyn,",
                        "hors hófum wlanc, ðǽr him hæleþas ymb,",
                        "welege on wicgum wrixlaþ sprǽce",
                        "and biþ unstyllum ǽfre frófur.",
                    ],
                    [
                        "the horse is a joy to princes in the presence of warriors.",
                        "A steed in the pride of its hoofs,",
                        "when rich men on horseback bandy words about it;",
                        "and it is ever a source of comfort to the restless.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%96-eh/",
                ),
                Rune(
                    "ᛗ",
                    "man",
                    "human",
                    [
                        "man byþ on myrgþe his mágan léof:",
                        "sceal þéah ánra gehwylc óðrum swícan,",
                        "for ðám dryhten wyle dóme síne",
                        "þæt earme flǽsc eorþan betǽcan.",
                    ],
                    [
                        "the joyous man is dear to his kinsmen;",
                        "yet every man is doomed to fail his fellow,",
                        "since the Lord  by his decree will commit",
                        "the vile carrion to the earth.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%97-man/",
                ),
                Rune(
                    "ᛚ",
                    "lagu",
                    "ocean",
                    [
                        "lagu byþ léodum langsum geþúht,",
                        "gif hí sculun néþun on nacan tealtum",
                        "and hí sǽýþa swýþe brégaþ",
                        "and se brimhengest brídles ne gýmeð.",
                    ],
                    [
                        "the ocean seems interminable to men,",
                        "if they venture on the rolling bark",
                        "and the waves of the sea terrify them",
                        "and the courser of the deep heed not its bridle.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%9a-lagu/",
                ),
                Rune(
                    "ᛝ",
                    "ing",
                    "Ing",
                    [
                        "ing wæs ǽrest mid éast-denum",
                        "gesewen secgun, oþ hé siððan ést",
                        "ofer wǽg gewát; wǽn æfter ran;",
                        "ðus heardingas ðone hæle nemdum.",
                    ],
                    [
                        "Ing was first seen by men among the East-Danes,",
                        "till, followed by his chariot,",
                        "he departed eastwards over the waves.",
                        "So the Heardingas named the hero.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%9d-ing/",
                ),
                Rune(
                    "ᛟ",
                    "éðel",
                    "estate, home",
                    [
                        "éðel byþ oferléof ǽghwylcum men,",
                        "gif he mót ðǽr rihtes and gerysena on",
                        "brúcan on bolde bléadum oftast.",
                    ],
                    [
                        "an estate is very dear to every man,",
                        "if he can enjoy there in his house",
                        "whatever is right and proper in constant prosperity.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%9f-edel/",
                ),
                Rune(
                    "ᛞ",
                    "dæg",
                    "day",
                    [
                        "dæg byþ drihtnes sond, déore mannum,",
                        "mǽre metodes léoht, myrgþ and tóhiht",
                        "éadgum and earmum, eallum bríce.",
                    ],
                    [
                        "day, the glorious light of the Creator,",
                        "is sent by the Lord; it is beloved of men,",
                        "a source of hope and happiness to rich and poor,",
                        "and of service to all.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%9e-daeg/",
                ),
                Rune(
                    "ᚪ",
                    "ác",
                    "oak",
                    [
                        "ác byþ on eorþan elda bearnum",
                        "flǽsces fódor, fereþ gelóme",
                        "ofer ganotes bæþ; garsecg fandaþ",
                        "hwæþer ác hæbbe æþele tréowe.",
                    ],
                    [
                        "the oak fattens the flesh of pigs for",
                        "the children of men. Often it traverses",
                        "the gannet's bath, and the ocean proves whether",
                        "the oak keeps faith in honourable fashion.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%aa-ac/",
                ),
                Rune(
                    "ᚣ",
                    "ýr",
                    "Yr; yew/bow(?)",
                    [
                        "ýr byþ æþelinga and eorla gehwæs",
                        "wyn and wyrþmynd, byþ on wicge fæger,",
                        "fæstlíc on færelde, fyrdgeatewa sum.",
                    ],
                    [
                        "Yr is a source of joy and honour",
                        "to every prince and knight;",
                        "it looks well on a horse and",
                        "is a reliable equipment for a journey.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9a%a3-yr/",
                ),
                Rune(
                    "ᛡ",
                    "íor",
                    "eel; beaver(?)",
                    [
                        "íor byþ éafixa and ðéah á brúceþ",
                        "fódres on foldan, hafaþ fægerne eard",
                        "wætre beworpen, ðǽr hé wynnum leofaþ.",
                    ],
                    [
                        "Íor is a river fish and yet it always feeds on land;",
                        "it has a fair abode encompassed by water,",
                        "where it lives in happiness.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%a1-iar-ior/",
                ),
                Rune(
                    "ᛠ",
                    "éar",
                    "grave",
                    [
                        "éar byþ egle eorla gehwylcun,",
                        "ðonn fæstlíce flǽsc onginneþ,",
                        "hráw cólian, hrúsan céosan",
                        "blác tó gebeddan; bléda gedréosaþ,",
                        "wynna gewítaþ, wéra geswícaþ.",
                    ],
                    [
                        "the grave is horrible to every knight,",
                        "when the corpse quickly begins to cool",
                        "and is laid in the bosom of the dark earth.",
                        "Prosperity declines, happiness passes away",
                        "and covenants are broken.",
                    ],
                    "https://runesoftheoerp.wordpress.com/%e1%9b%a0-ear/",
                ),
            ]
        )
