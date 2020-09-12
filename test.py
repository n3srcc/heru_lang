from decoder.DecodeLang import DecodeLang

""" Write a program that answers the following questions to a given Herucode text:
1) How many prepositions are there in the text?
2) How many verbs are there in the text?
3) How many of those verbs in the text are in the subjunctive form?
4) Generate a vocabulary list with distinct words ordered Herucode's alphabetical order.
5) How many distinct pretty numbers are in the text?
""" 

test_case_a = """shoce pq podciy nfwh phfer epgdc dgsloqe do rhfl qhmoixw cmfur qdrulxogji whc ermjdhsx
py en yco ienqm wjuln dwuch qinhmjul mjxdqfrnlg iygsex qihmu grewyluhfs ucf us xclpedqmi
yrx qinexwo qx rqw wxflpdn rsogxd cpqmxj lgchqdin fdw nwcrus coj nj qplfjnwidg fwdmslqn
cwj hysucxdqm ms hdmwpe igxweo sqflo ycqlinro ghu hgecdfj mw xrpmyenq fgixsr
fpwcnguieh fclgj ghepqyd jxhwe cejfugn ujxqh ihncrl mlceo udr fm ocxfsjdng sfoqmd
pdoymnwxei spqinedf ql ncsepfl icmqsdj chwjlg yiq ifl syejrqd lwnepmcg xlmnfqry
ghlyopuncw qx iw sionpux cop dmqpchuyf ojxfqhernm ignpeyf rseoyl emjocsild rfimdy mwd
oewgjfr uo irmcunfgx ylduwpsnh xrdng gcxr ng prfmjicud srdueqhgiy nmodwsqijh dcnql"""


test_case_b = """dufqwh ndis eqclrnguo ceqrugs meod eofxlrd uqpwmni xrhm qgro hlwgimn fjnomcledi silruxh
efwh uxfrpsnqd fyejhi fxdn swfruc eopq hcgeox lhimoynsr rwjxecpmfl gimqxwuyr eujh rfs
qncuyiel hwuiqlne umyldn uwflpqc gywlc oxmegsdi sqemywlg cnfimrgows hnxyfd exmdnos
djpsogiy xyp myngercj yeujqcoih sgljco xy lruneodc frqog hqsgcy wmi hyfgqj iecusqjp
ugnmqfypsd yp rxoew lqeshijndg umynehjsci rnc xhrjyocde mnefpj rcyihwxq oihjwrup
gquscxhw ucrfdsoeq drg nqhodjsm snp cwoen ehyldsnmf pmrs cghuwpfxly ifwpnx wqdgrl
xocpjedsfm oegli url rylnsph ijucmxw jwispgefdo heixgmcy gm sdhfnoxg hc jqwpdo eo
hmypjfu xuedl nqpge cnyosu dniefl lf xcdupho wixmhcuynj poy ous jwroheqm xchm
jnufdshiqe liyrexhmu cjlxoiquef fwqrijemcd csxpy eqxghfry fhnwomgyuq yj euhxmosc"""


lang = DecodeLang(text=test_case_b)
lang.count_prepositions()
lang.count_subjunctive_and_verbs()
lang.ordered_alphabetical()
lang.count_distinct_pretty_numbers()

