import math as m
from tabulate import tabulate as t
cos={0:m.cos(0),1:m.cos(1),2:m.cos(2),3:m.cos(3),4:m.cos(4),5:m.cos(5),6:m.cos(6),7:m.cos(7),8:m.cos(8),9:m.cos(9),10:m.cos(10),11:m.cos(11),12:m.cos(12),13:m.cos(13),14:m.cos(14),15:m.cos(15),16:m.cos(16),
17:m.cos(17),18:m.cos(18),19:m.cos(19),20:m.cos(20),21:m.cos(21),22:m.cos(22),23:m.cos(23),24:m.cos(24),25:m.cos(25),26:m.cos(26),27:m.cos(27),28:m.cos(28),29:m.cos(29),30:m.cos(30),31:m.cos(31),32:m.cos(32),33:m.cos(33),34:m.cos(34),35:m.cos(35),36:m.cos(36),37:m.cos(37),38:m.cos(38),39:m.cos(39),40:m.cos(40),41:m.cos(41),42:m.cos(42),
43:m.cos(43),44:m.cos(44),45:m.cos(45),46:m.cos(46),47:m.cos(47),48:m.cos(48),49:m.cos(49),50:m.cos(50),51:m.cos(51),52:m.cos(52),53:m.cos(53),54:m.cos(54),55:m.cos(55),56:m.cos(56),57:m.cos(57),58:m.cos(58),59:m.cos(59),60:m.cos(60),61:m.cos(61),62:m.cos(62),63:m.cos(63),64:m.cos(64),65:m.cos(65),66:m.cos(66),67:m.cos(67),68:m.cos(68),69:m.cos(69),70:m.cos(70),71:m.cos(71),72:m.cos(72),73:m.cos(73),74:m.cos(74),75:m.cos(75),76:m.cos(76),77:m.cos(77),78:m.cos(78),79:m.cos(79),
80:m.cos(80),81:m.cos(81),82:m.cos(82),83:m.cos(83),84:m.cos(84),85:m.cos(85),86:m.cos(86),87:m.cos(87),88:m.cos(88),89:m.cos(89),90:m.cos(90),91:m.cos(91),92:m.cos(92),93:m.cos(93),94:m.cos(94),95:m.cos(95),96:m.cos(96),97:m.cos(97),98:m.cos(98),99:m.cos(99),100:m.cos(100),
101:m.cos(101),102:m.cos(102),103:m.cos(103),104:m.cos(104),105:m.cos(105),106:m.cos(106),107:m.cos(107),108:m.cos(108),109:m.cos(109),110:m.cos(110),111:m.cos(111),112:m.cos(112),113:m.cos(113),114:m.cos(114),115:m.cos(115),116:m.cos(116),
117:m.cos(117),118:m.cos(118),119:m.cos(119),120:m.cos(120),121:m.cos(121),122:m.cos(122),123:m.cos(123),124:m.cos(124),125:m.cos(125),126:m.cos(126),127:m.cos(127),128:m.cos(128),129:m.cos(129),130:m.cos(130),131:m.cos(131),132:m.cos(132),133:m.cos(133),134:m.cos(134),135:m.cos(135),136:m.cos(136),137:m.cos(137),138:m.cos(138),139:m.cos(139),140:m.cos(140),141:m.cos(141),142:m.cos(142),
143:m.cos(143),144:m.cos(144),145:m.cos(145),146:m.cos(146),147:m.cos(147),148:m.cos(148),419:m.cos(149),150:m.cos(150),151:m.cos(151),152:m.cos(152),153:m.cos(153),154:m.cos(154),155:m.cos(155),156:m.cos(156),157:m.cos(157),158:m.cos(158),159:m.cos(159),160:m.cos(160),161:m.cos(161),162:m.cos(162),163:m.cos(163),164:m.cos(164),165:m.cos(165),166:m.cos(166),167:m.cos(167),168:m.cos(168),169:m.cos(169),170:m.cos(170),171:m.cos(171),172:m.cos(172),173:m.cos(173),174:m.cos(174),175:m.cos(175),176:m.cos(176),177:m.cos(177),178:m.cos(178),179:m.cos(179),
180:m.cos(180),181:m.cos(181),182:m.cos(182),183:m.cos(183),184:m.cos(184),185:m.cos(185),186:m.cos(186),187:m.cos(187),188:m.cos(188),189:m.cos(189),190:m.cos(190),191:m.cos(191),192:m.cos(192),193:m.cos(193),194:m.cos(194),195:m.cos(195),196:m.cos(196),197:m.cos(197),198:m.cos(198),199:m.cos(199),200:m.cos(200),
201:m.cos(201),202:m.cos(202),203:m.cos(203),204:m.cos(204),205:m.cos(205),206:m.cos(206),207:m.cos(207),208:m.cos(208),209:m.cos(209),210:m.cos(210),211:m.cos(211),212:m.cos(212),213:m.cos(213),214:m.cos(214),215:m.cos(215),216:m.cos(216),
217:m.cos(217),218:m.cos(218),219:m.cos(219),220:m.cos(220),221:m.cos(221),222:m.cos(222),223:m.cos(223),224:m.cos(224),225:m.cos(225),226:m.cos(226),227:m.cos(227),228:m.cos(228),229:m.cos(229),230:m.cos(230),231:m.cos(231),232:m.cos(232),233:m.cos(233),234:m.cos(234),235:m.cos(235),236:m.cos(236),237:m.cos(237),238:m.cos(238),239:m.cos(239),240:m.cos(240),241:m.cos(241),242:m.cos(242),
243:m.cos(243),244:m.cos(244),245:m.cos(245),246:m.cos(246),247:m.cos(247),248:m.cos(248),249:m.cos(249),250:m.cos(250),251:m.cos(251),252:m.cos(252),253:m.cos(253),254:m.cos(254),255:m.cos(255),256:m.cos(256),257:m.cos(257),258:m.cos(258),259:m.cos(259),260:m.cos(260),261:m.cos(261),262:m.cos(262),263:m.cos(263),264:m.cos(264),265:m.cos(265),266:m.cos(266),267:m.cos(267),268:m.cos(268),269:m.cos(269),270:m.cos(270),271:m.cos(271),272:m.cos(272),273:m.cos(273),274:m.cos(274),275:m.cos(275),276:m.cos(276),277:m.cos(277),278:m.cos(278),279:m.cos(279),
280:m.cos(280),281:m.cos(281),282:m.cos(282),83:m.cos(283),284:m.cos(284),285:m.cos(285),286:m.cos(286),287:m.cos(287),288:m.cos(288),289:m.cos(289),290:m.cos(290),291:m.cos(291),292:m.cos(292),293:m.cos(293),294:m.cos(294),295:m.cos(295),296:m.cos(296),297:m.cos(297),298:m.cos(298),299:m.cos(299),300:m.cos(300),
301:m.cos(301),302:m.cos(302),303:m.cos(303),304:m.cos(304),305:m.cos(305),306:m.cos(306),307:m.cos(307),308:m.cos(308),309:m.cos(9),310:m.cos(310),311:m.cos(311),312:m.cos(312),313:m.cos(313),314:m.cos(314),315:m.cos(315),316:m.cos(316),
317:m.cos(317),318:m.cos(318),319:m.cos(319),320:m.cos(320),321:m.cos(321),322:m.cos(322),323:m.cos(323),324:m.cos(324),325:m.cos(325),326:m.cos(326),327:m.cos(327),328:m.cos(328),329:m.cos(329),330:m.cos(330),331:m.cos(331),332:m.cos(332),333:m.cos(333),334:m.cos(334),335:m.cos(335),336:m.cos(336),337:m.cos(337),338:m.cos(338),339:m.cos(339),340:m.cos(340),341:m.cos(341),342:m.cos(342),
343:m.cos(343),344:m.cos(344),345:m.cos(345),346:m.cos(346),347:m.cos(347),348:m.cos(348),349:m.cos(349),350:m.cos(350),351:m.cos(351),352:m.cos(352),353:m.cos(353),354:m.cos(354),355:m.cos(355),356:m.cos(356),357:m.cos(357),358:m.cos(358),359:m.cos(359),360:m.cos(360)}
# or
# cos={m.cos(choice)}

choice=int(input("wiche angle? \n"))
table=[['1)Radians'],
        ['2)Degree']]
print(t(table,tablefmt='fancy_grid'))
typ=int(input("wiche type?"))
if typ==1:
    choice=choice*57.2958
    ch=str(choice)
    dict_ra={ch:m.cos(choice)}
    print(dict_ra[ch])
elif typ==2:

    print(cos[choice])