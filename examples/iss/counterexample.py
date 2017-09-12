"Counter-example trace generated using HyLAA"

import sys
from scipy.sparse import csc_matrix
from hylaa.check_trace import check, plot

def check_instance():
    'define parameters for one instance and call checking function'

    data = [-0.38869800053422848, -0.60077790048969182, -1.9781353996378603, -1.9784867775809558, -3.1942620584955201, -3.9682178117785005, -5.275619638417095, -5.3175948840994778, -6.1969279615561392, -6.2040941747860634, -6.6375567021662727, -6.6430161113305868, -14.915018757978681, -15.320723266147203, -28.924018790642677, -28.924072776090892, -31.359978809603582, -31.666312465231737, -34.377263622771878, -34.377277483408193, -37.181787323151582, -37.229417234255301, -62.939633757771496, -65.885181623540802, -65.946064684744385, -71.92528893700306, -84.946036519181575, -85.054119790798993, -85.261840203209374, -91.27308085400216, -91.28250837756076, -95.439947217127028, -95.43994803775135, -95.45726538360978, -95.457265422690682, -95.491716579635224, -95.491716599179185, -105.23597141172976, -105.31638333210933, -115.8247202509848, -116.34355299085961, -178.24774814714044, -178.73346449516458, -233.47697101658648, -305.20294294521881, -306.11334549785346, -335.99779230843529, -338.1158744354293, -437.90888576656164, -444.22579529775936, -467.28069469131515, -468.98140825741876, -505.12318781393975, -505.13898153129213, -730.75133638312116, -730.76254136113801, -749.98731122489232, -749.98750785564005, -831.10115145720147, -831.10221120514666, -908.84641986462645, -909.06206446649355, -934.40167944903862, -934.43053156965391, -1013.9200195626344, -1013.9233719028293, -1089.8703957289717, -1089.8866943994296, -1122.1223277613494, -1122.1239738583115, -1147.7191902571403, -1147.7191902571403, -1147.92353318091, -1147.9235352137714, -1148.2329128103509, -1148.232914843486, -1219.5990409941223, -1230.3811433873796, -1442.9023202840269, -1532.2712542994714, -1532.5569626098415, -1608.7722654011816, -1609.1347890962995, -1752.0154466602476, -1752.1516572804233, -1782.2235263734819, -1782.2238075346463, -1808.3951729448265, -1808.9947620377145, -1846.1450042339893, -1846.1450102493397, -1910.8990032110285, -1910.8991841862921, -1948.5193166229153, -1948.5447963720635, -1948.9608979528873, -1948.9660684573198, -2050.7241043927811, -2050.7522970703303, -2091.302206218415, -2091.4464764426325, -2180.58415374366, -2180.8133697091548, -2190.9904779401372, -2196.9308752506126, -2288.2266909585728, -2302.1232434605354, -2575.4005684303329, -2576.1384726325673, -2757.4794140632148, -2758.1221391472941, -2772.3088475784834, -2797.8181723402904, -2926.6100465692152, -2926.8206198396333, -3146.5421166913757, -3150.7785614778736, -3212.8195201932344, -3213.4273642308422, -3281.1134169567758, -3291.2214932340089, -3291.3656164894678, -3427.5980459042944, -3427.5980763480543, -3428.8212424322746, -3428.8212471167653, -3429.2770351304603, -3429.2770702664784, -3448.1826213512577, -3448.1826471885984, -3449.0489959139973, -3449.049044071453, -3452.3442400338163, -3452.3442400338163, -3762.5794087110185, 1.0, -0.0062345649449999999, 1.0, -0.0077509863919999998, 1.0, -0.01406462015, 1.0, -0.014065869250000002, 1.0, -0.017872498590000001, 1.0, -0.019920386070000001, 1.0, -0.022968717070000002, 1.0, -0.02305991085, 1.0, -0.024893629630000001, 1.0, -0.024908019140000001, 1.0, -0.025763456100000002, 1.0, -0.025774049180000001, 1.0, -0.038619967320000004, 1.0, -0.039141695500000004, 1.0, -0.053781055020000003, 1.0, -0.053781105209999999, 1.0, -0.055999981080000004, 1.0, -0.056272828669999997, 1.0, -0.058632127389999997, 1.0, -0.058632139209999996, 1.0, -0.06097687047, 1.0, -0.061015913690000007, 1.0, -0.079334503060000006, 1.0, -0.081169687460000001, 1.0, -0.081207182370000006, 1.0, -0.084808778399999993, 1.0, -0.09216617412, 1.0, -0.092224790479999999, 1.0, -0.092337338169999991, 1.0, -0.095536946179999999, 1.0, -0.095541880019999997, 1.0, -0.097693370920000008, 1.0, -0.097693371340000001, 1.0, -0.097702234050000003, 1.0, -0.097702234070000005, 1.0, -0.097719863170000004, 1.0, -0.097719863180000005, 1.0, -0.1025845853, 1.0, -0.1026237708, 1.0, -0.10762189380000001, 1.0, -0.10786266870000001, 1.0, -0.13350945590000002, 1.0, -0.13369123550000001, 1.0, -0.15279953239999999, 1.0, -0.17470058470000002, 1.0, -0.17496095149999999, 1.0, -0.18330242559999999, 1.0, -0.18387927409999999, 1.0, -0.2092627262, 1.0, -0.21076664710000001, 1.0, -0.21616676309999999, 1.0, -0.21655978579999999, 1.0, -0.2247494578, 1.0, -0.2247529714, 1.0, -0.27032412699999997, 1.0, -0.27032619950000003, 1.0, -0.27385896209999999, 1.0, -0.27385899800000002, 1.0, -0.28828825009999998, 1.0, -0.28828843389999997, 1.0, -0.30147079789999998, 1.0, -0.30150656120000002, 1.0, -0.30567984549999999, 1.0, -0.3056845648, 1.0, -0.3184211079, 1.0, -0.31842163429999998, 1.0, -0.33013185179999999, 1.0, -0.33013432029999995, 1.0, -0.33498094389999999, 1.0, -0.33498118960000001, 1.0, -0.33878004519999999, 1.0, -0.33878004519999999, 1.0, -0.33881020249999999, 1.0, -0.33881020280000002, 1.0, -0.33885585620000003, 1.0, -0.33885585650000005, 1.0, -0.34922758209999999, 1.0, -0.35076789239999995, 1.0, -0.37985554100000002, 1.0, -0.39144236540000005, 1.0, -0.39147885799999999, 1.0, -0.40109503429999999, 1.0, -0.4011402235, 1.0, -0.41857083590000005, 1.0, -0.41858710649999997, 1.0, -0.42216389309999997, 1.0, -0.42216392640000006, 1.0, -0.42525229840000001, 1.0, -0.4253227906, 1.0, -0.42966789550000001, 1.0, -0.42966789620000001, 1.0, -0.43713830799999998, 1.0, -0.43713832869999997, 1.0, -0.44142035710000005, 1.0, -0.44142324320000004, 1.0, -0.44147037249999999, 1.0, -0.44147095810000003, 1.0, -0.45284921379999998, 1.0, -0.45285232659999997, 1.0, -0.45730757769999997, 1.0, -0.45732335130000001, 1.0, -0.46696725299999997, 1.0, -0.46699179540000002, 1.0, -0.46808017239999999, 1.0, -0.46871429200000003, 1.0, -0.47835412519999998, 1.0, -0.47980446469999999, 1.0, -0.50748404589999996, 1.0, -0.50755674290000008, 1.0, -0.52511707399999996, 1.0, -0.52517826870000006, 1.0, -0.52652719280000004, 1.0, -0.52894405870000005, 1.0, -0.54098151970000008, 1.0, -0.54100098149999998, 1.0, -0.56094047070000008, 1.0, -0.56131796350000007, 1.0, -0.56681738860000008, 1.0, -0.56687100509999999, 1.0, -0.5728100398, 1.0, -0.5736916849, 1.0, -0.57370424580000001, 1.0, -0.58545691950000001, 1.0, -0.5854569221, 1.0, -0.58556137530000008, 1.0, -0.5855613757, 1.0, -0.58560029329999996, 1.0, -0.58560029629999999, 1.0, -0.58721228030000006, 1.0, -0.58721228250000002, 1.0, -0.58728604579999999, 1.0, -0.5872860499, 1.0, -0.58756652730000003, 1.0, -0.58756652730000003, 1.0, -0.61339868019999999, 7.075738793216324e-07, -0.50662067166023739, -1.178945046697992e-10, -8.1481926646259292e-06, -2.8374707039605096e-06, -0.43872914664137763, 0.036494624445064398, 6.5640996506983107e-06, -0.014834740940270319, -0.00015397909303230478, 0.010699679571784906, -4.7189071738616781e-05, 4.4819359055446595e-06, -0.18348385229665887, -0.00013118916405466138, 1.4321568762517797e-05, -2.3503972388511096e-07, -0.10194680844115701, 8.3625083432646439e-05, 5.8760133235436261e-06, -5.9251751278414228e-07, 0.037588656933930001, -0.068524731010211642, -7.5635533574210101e-05, -0.018658043189479622, 0.0013939791271709856, -0.099921897178689989, 3.1500870991319927e-06, -0.14677684174015104, -1.115950236774783e-07, 0.012348247117146076, -2.5598266607567804e-05, 7.9975570972739601e-08, 1.117392831123576e-05, 1.1804382398071903e-06, 3.0684402688565842e-06, -1.3712074462206066e-06, -1.3062805947691714e-05, -0.035276562020583435, -1.8536328046128009e-05, -0.08131535593545465, -0.0044784644128471728, -5.1617740780679749e-06, -0.00042514839658473053, -9.6891134342032281e-06, 0.064983836493975974, 0.004123036420556012, -4.5821291343165881e-05, -0.0018318062646183464, -0.020001088564929638, -0.0061950156202108357, -0.001041389062545986, 2.6892587210425182e-05, 0.0001004696396958403, -0.0062848714882649927, -0.0305564235838095, -0.0001152501460817548, 0.00013763548450267373, 1.180255185401912e-06, 0.00043811148794235084, 6.5478567320071504e-06, -0.0050359121285041839, -0.0045682244837376047, -7.8888691651410835e-05, 0.00057634405470348231, 0.00017215499573631791, -5.1704707851202395e-05, -0.0054866296679374474, -0.0054376342638241511, 0.00031666516618596477, -1.2616792191738576e-06, 4.1452123887726408e-06, -2.2451571120608446e-05, 9.8304326645985785e-06, -2.2194534698327835e-05, -3.3025387898621353e-06, 0.24221484541322541, 8.8813032662007733e-05, -1.1952346159660596, 0.0014984246924678176, 0.023606999966782977, 0.0029050455780455777, -0.013599902353642831, 0.00015565519994299986, -0.021483055159559263, -0.00031681574022451739, 0.00056935431917117495, -0.0011199300223888693, 0.00054889763472315296, 4.9723387965633383e-06, 4.9100693482157263e-10, 4.9188610772072184e-05, 0.00015051010925923699, 0.00063176692604072194, 0.006180695496445115, 0.0012237214527630849, 0.0017744116178130182, -0.0049765083950843343, 0.012330250296058226, 0.0154304705464204, -0.0004903080695889087, 0.020252652340956193, -0.0010618506137156257, -0.075295683486325232, 0.0020217762668403461, 0.10388971150874418, -0.19345900934139099, -3.2976607296075282e-05, -0.014882205961574461, -0.00027497924565823622, -0.0091551114830204956, -0.0012731190097589988, -0.011331840787705449, -1.0054857553700857e-07, 0.0055521023608403573, 0.092187765614180017, 0.0026713362178403983, -3.974960912648119e-05, 0.0010552022664765633, 0.0042997497564386776, 4.9177796509105925e-05, 0.0051307461546947573, -2.6483371662236439e-05, 2.7939637495257952e-06, 8.7618566636396597e-06, 6.750599252833735e-07, -2.0209074882367826e-05, 1.7931032353384009e-06, -2.3735598372607671e-05, -1.7903283252613545e-06, 2.0305012343740545e-05, 1.7888238904405158e-06, -2.1437220358829109e-07, 1.9937182003786463e-08, 0.0093569608906835869, 0.14128372804309661, -0.0001193831391122604, -7.4209077836834822e-10, -0.011051584858161047, -0.017999542373465325, -9.6277086862504372e-05, 2.3959645228603869e-05, -0.0016156254482397221, -1.7813133192608839e-05, 0.006732557291405321, 8.4365151206157271e-06, 0.0063216747806373163, 0.08420842550487273, -2.142842887522776e-05, -7.2262851088839207e-06, 0.0011905839633229781, -0.030750936757117448, 1.9165506413879483e-05, -1.143593282551311e-06, -0.00036539069470698123, 0.018604714604927894, -1.4813797295469641e-05, 0.0034099928681311986, -0.072934509771642925, 0.00011390001907199677, 0.86514514887703076, 0.0018634848314941764, -0.0030872898269059556, 0.0022358893167733493, 0.0022772358713103848, -1.5689557912688831e-05, 4.1292945214972144e-07, -2.2157304187634782e-05, 6.5102120669912866e-07, -8.8568933827442554e-06, 1.4740436896758313e-06, 3.4433118693343335e-06, 0.026419697481619726, -7.516722784239814e-05, -0.043783308180402089, -9.972292788998176e-05, 9.2377185566884558e-05, -0.0043648140082128096, -0.06437323620006305, -0.0519064039575532, 0.0002139286991562824, -0.00062444315686265798, 0.010422356762578206, 0.35853944249103564, 0.0002088888314635109, 0.45414413599573988, -0.41616394002722262, 2.9601845440518002e-06, -0.013985638017815417, -0.0071941813595049788, 0.0017199492539402203, -0.00011461405123285148, 0.0007908839155445534, -2.543967440038635e-05, -9.828278400349479e-06, -1.8366515394311579e-05, 6.5275546746754425e-05, 9.6011992548477448e-05, -0.00116082697934629, 3.6045845265416733e-05, -0.0011353030794646508, -0.00027271231588195887, 2.4149779154284178e-05, 3.6796979245833555e-05, 0.0005478241133995837, 3.075673353703013e-06, -1.03951839043938e-05, 3.1599249275904158e-06, -1.4815343736105127e-05, -2.9022381068240571e-07, 8.9200238415722501e-06, 0.0015138004822681213, 0.023045230995554868, -0.0063102759884754427, -0.0072565071201953005, 0.00018271084175987994, -0.016819417553774654, -0.00012965813605983974, -0.018794569800485481, 0.0010014094976180071, 0.00056430182294520343, 0.00031009208042553753, 0.00058536313282968311, 0.00065079408117563859, -9.8471880935549483e-06, -1.1222662543725898e-09, -0.00022687106256786849, 5.1321443066386808e-05, 0.00017695740106714284, 0.00032645639482005136, 0.00019930123165470956, 1.6867778715057626e-05, -0.011416532363376357, -0.0035990966349508909, 0.0016228057472923237, 0.0042589137542270016, 0.0043904271204498746, 0.014846294552745432, -0.014032514085860745, -0.039024395021013167, 0.51887288304628409, 0.32778235738904193, 8.5028950568234382e-05, 0.0012963921771736878, 0.013625030342338983, -0.00032325169828751346, 0.0034081873991286156, 0.00054552395591031912, -0.0002881840510907366, -0.00025119182138368492, 0.00038023878423420901, -0.053335626982083578, 0.0027228904654499099, 0.00010517990527339176, 0.015694712160254358, 0.0067973305728004476, -5.1325347604924622e-05, 1.2671293026251687e-06, 8.4548801810252061e-06, -1.1027391538671622e-07, 2.7178225942589948e-06, 2.7709311853588925e-07, 7.3770497498618948e-06, 4.9165574753492182e-07, -6.7173477905912485e-06, -2.2688103571138147e-07, 7.6133487815790913e-06, 7.4510783680380107e-08, -1.260837773596005e-07, -0.00015898184903807394, 6.5391949619160228e-06, -0.036276589523845569, -1.936028163559593e-11, -1.7212666455938183e-06, -3.9165281392397334e-06, -0.0300230736943486, 0.079402605486580541, 4.6055700004357138e-05, -0.057110453938165204, -0.00012594822289573645, 0.044060262230786892, 3.8115801689457031e-06, 7.8715831619204796e-06, -0.018073489501677129, -0.00098968768028615071, 2.9171910519123405e-07, 2.7620527939953686e-05, -0.013061485323973833, 0.00056631298410516739, 1.1913827218199436e-06, -2.0965307884928842e-05, 0.0054979729936334102, -0.46585363625217219, -0.00025307714936506414, -0.029033515445209532, -0.00025457003832072937, 0.48228425577538769, -9.0546271907273969e-05, 0.60815346090881928, 1.4395018791587319e-05, -0.014481620946307283, 6.1056722633928031e-05, -2.6976832232913457e-07, -2.6667156034098518e-05, -2.0967524046129212e-06, -7.269552092965754e-06, 3.3060339546734652e-06, 6.9845001608772082e-05, 0.0065433441314405871, 0.00012439113487676395, 0.031319308857917325, -0.018757395734806635, 2.3087991394235997e-05, -0.00052336206272497526, 5.3608296629202774e-05, -0.00624674321443757, 0.031733380464028349, -0.00010100998138812571, -0.010540353180872472, 0.0066286738878220432, -0.50666622971649522, -0.56217412603984707, -0.0033639840595646869, -0.00032624265724946728, 0.0001035107862693919, 0.00128745949006798, 0.00088724410379133873, 0.00015113742697157111, -6.4530029150631623e-05, -0.0033707088942420893, -2.5361186481013557e-05, 0.0014387474764852724, 0.02528457589892218, 0.00058977653595067357, -0.0025507509388791594, -8.7534536753508155e-05, 9.027548876952388e-06, -3.7179624494118097e-05, 0.00015171724423563817, -1.8048901089714957e-05, 1.1409407164069793e-06, -1.0081586303462853e-07, 5.9826473999719838e-05, 4.4949378766703924e-06, 6.0458732920363678e-05, -5.3806935666441793e-08, 0.014898205802561619, -0.00020995943917218995, -0.08102400275693028, 0.00020511677347619705, 0.0038478255120533399, 0.00030640183329819952, 0.011914970330082278, 0.0016063368933585441, 0.01525739689207955, 0.00046200358237534088, -0.00033678467049619737, 0.014128948775682071, -0.00031025842018229705, 2.6278756626892446e-06, 2.2290493836282633e-10, -0.00021282697484361121, -0.00012872412162022128, -0.001089197926779572, -0.0085195132379974788, -0.0021921689710280331, -0.0020570614488061049, 0.0099946088444305518, -0.022364905641816521, -0.030353246429296449, 0.00064389956756263239, -0.046048748080329049, 0.001324110977113361, 0.17315131826356012, -0.0018451890747523585, -0.31624302096015544, 0.50735055312950372, 8.903023610537476e-05, 0.026467109011837853, 0.0002069817588391209, 0.014075440346582858, 0.00084288018107966239, 0.077110277471779176, -3.9860309919006326e-05, -0.0065610146818986231, -0.0082240636823375894, -0.00070800125135874489, 8.596642726226025e-06, 0.011092087753148766, -0.0027018895986419822, -5.6598253983952077e-05, -0.0051117889831650207, 1.4289036229427808e-05, -1.9637657478996744e-06, -4.7226092235851638e-06, -2.7930657591083723e-07, 1.0883077873135065e-05, -8.253825793193494e-07, 1.2400937337369846e-05, 7.4256101474002529e-07, -1.0593694456252556e-05, -6.2278440157523347e-07, 1.1079641082262115e-07, -9.1707572305031227e-08, -0.028368434426301388]
    indices = [135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 0, 135, 1, 136, 2, 137, 3, 138, 4, 139, 5, 140, 6, 141, 7, 142, 8, 143, 9, 144, 10, 145, 11, 146, 12, 147, 13, 148, 14, 149, 15, 150, 16, 151, 17, 152, 18, 153, 19, 154, 20, 155, 21, 156, 22, 157, 23, 158, 24, 159, 25, 160, 26, 161, 27, 162, 28, 163, 29, 164, 30, 165, 31, 166, 32, 167, 33, 168, 34, 169, 35, 170, 36, 171, 37, 172, 38, 173, 39, 174, 40, 175, 41, 176, 42, 177, 43, 178, 44, 179, 45, 180, 46, 181, 47, 182, 48, 183, 49, 184, 50, 185, 51, 186, 52, 187, 53, 188, 54, 189, 55, 190, 56, 191, 57, 192, 58, 193, 59, 194, 60, 195, 61, 196, 62, 197, 63, 198, 64, 199, 65, 200, 66, 201, 67, 202, 68, 203, 69, 204, 70, 205, 71, 206, 72, 207, 73, 208, 74, 209, 75, 210, 76, 211, 77, 212, 78, 213, 79, 214, 80, 215, 81, 216, 82, 217, 83, 218, 84, 219, 85, 220, 86, 221, 87, 222, 88, 223, 89, 224, 90, 225, 91, 226, 92, 227, 93, 228, 94, 229, 95, 230, 96, 231, 97, 232, 98, 233, 99, 234, 100, 235, 101, 236, 102, 237, 103, 238, 104, 239, 105, 240, 106, 241, 107, 242, 108, 243, 109, 244, 110, 245, 111, 246, 112, 247, 113, 248, 114, 249, 115, 250, 116, 251, 117, 252, 118, 253, 119, 254, 120, 255, 121, 256, 122, 257, 123, 258, 124, 259, 125, 260, 126, 261, 127, 262, 128, 263, 129, 264, 130, 265, 131, 266, 132, 267, 133, 268, 134, 269, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269]
    indptr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255, 257, 259, 261, 263, 265, 267, 269, 271, 273, 275, 277, 279, 281, 283, 285, 287, 289, 291, 293, 295, 297, 299, 301, 303, 305, 307, 309, 311, 313, 315, 317, 319, 321, 323, 325, 327, 329, 331, 333, 335, 337, 339, 341, 343, 345, 347, 349, 351, 353, 355, 357, 359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379, 381, 383, 385, 387, 389, 391, 393, 395, 397, 399, 401, 403, 405, 540, 675, 810]
    a_matrix = csc_matrix((data, indices, indptr), dtype=float, shape=(273, 273))
    b_matrix = None
    inputs = None

    step = 0.01
    max_time = 0.5

    start_point = [0.0, -0.0001, 0.0, 0.0, 0.0, -0.0001, 0.0001, 0.0, -0.0001, -0.0001, 0.0001, 0.0, 0.0, -0.0001, -0.0001, 0.0, 0.0001, -0.0001, 0.0001, 0.0, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, -0.0001, -0.0001, 0.0001, -0.0001, -0.0001, 0.0001, -0.0001, 0.0, 0.0001, 0.0, 0.0001, 0.0, -0.0001, -0.0001, -0.0001, -0.0001, -0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, -0.0001, 0.0001, 0.0001, 0.0001, -0.0001, -0.0001, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0001, 0.0, 0.0, -0.0001, -0.0001, -0.0001, 0.0, -0.0001, 0.0001, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0001, 0.0, -0.0001, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, -0.0001, 0.0001, 0.0001, -0.0001, 0.0001, -0.0001, -0.0001, 0.0001, 0.0001, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0001, -0.0001, -0.0001, -0.0001, -0.0001, 0.0001, -0.0001, 0.0001, 0.0001, 0.0001, 0.0001, 0.0, -0.0001, 0.0, 0.0001, 0.0, 0.0001, 0.0, -0.0001, 0.0, 0.0, 0.0, 0.0001, 0.0, 0.0001, 0.0, 0.0, 0.0, 0.0001, -0.0001, 0.0, 0.0001, 0.0, -0.0001, 0.0, 0.0, -0.0001, -0.0001, 0.0, 0.0, -0.0001, 0.0001, 0.0, 0.0, 0.0001, -0.0001, -0.0001, -0.0001, 0.0001, 0.0001, -0.0001, 0.0001, 0.0, 0.0001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0001, -0.0001, -0.0001, 0.0001, 0.0, 0.0001, 0.0, -0.0001, 0.0001, -0.0001, -0.0001, 0.0001, -0.0001, -0.0001, 0.0001, 0.0001, 0.0001, -0.0001, -0.0001, -0.0001, 0.0001, -0.0001, 0.0, 0.0001, 0.0001, 0.0001, -0.0001, -0.0001, 0.0, -0.0001, 0.0, 0.0, 0.0, 0.0, 0.0001, 0.0, 0.0001, 0.0, -0.0001, -0.0001, 0.0001, -0.0001, -0.0001, -0.0001, -0.0001, 0.0001, 0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0, 0.0, -0.0001, -0.0001, -0.0001, -0.0001, -0.0001, -0.0001, 0.0001, -0.0001, -0.0001, 0.0001, -0.0001, 0.0001, 0.0001, -0.0001, 0.0001, -0.0001, 0.0, -0.0001, -0.0001, -0.0001, -0.0001, -0.0001, 0.0, -0.0001, -0.0001, -0.0001, 0.0, 0.0001, -0.0001, 0.0, -0.0001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0001, 0.0, 1.0, 1.0]
    normal_vec = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.3036088720000002e-09, -4.4271908320000002e-05, -2.0607891320000001e-14, -1.5190254430000001e-09, -2.591238169e-09, -3.8672690609999999e-05, 3.2497922209999999e-05, 2.374680976e-08, -3.9650834149999997e-05, -9.2511897049999996e-08, 3.110302433e-05, 1.286925554e-09, 7.1361019050000003e-09, -2.0776364400000001e-05, -9.3587771450000001e-07, 4.8503033190000001e-10, 3.073929536e-08, -1.429959998e-05, 5.6640412419999996e-07, 1.2932844820000001e-09, -2.453659427e-08, 5.8449114429999998e-06, -0.00071004862179999996, -4.4657355540000002e-07, -4.2143093930000001e-05, 4.5825985529999999e-07, 0.00060259207490000004, -1.158924453e-07, 0.00075831308740000004, 1.9028823009999999e-08, -1.760128745e-05, 9.0683437929999999e-08, -3.8217271299999999e-10, -3.9627003369999998e-08, -3.024923357e-09, -1.080943395e-08, 4.9123494220000001e-09, 9.5442310869999996e-08, 5.0546751569999996e-06, 1.7756223659999999e-07, 3.8255408780000001e-05, -2.5122978500000001e-05, 3.5647652609999999e-08, -8.8326364100000001e-07, 9.0962462890000003e-08, -7.5304372379999997e-06, 8.5332090280000004e-05, -1.4902215199999999e-07, -1.8586013049999999e-05, 1.099450788e-05, -0.00089401966689999998, -0.00099197308669999999, -6.0059502950000004e-06, -5.7553681480000003e-07, -1.234945139e-07, 8.0272533570000005e-07, 1.643867903e-06, 2.889442694e-07, -1.2110863760000001e-07, -6.2718008320000003e-06, -4.6838979330000003e-08, 2.5021590050000002e-06, 4.703291417e-05, 1.1043527420000001e-06, -4.7306345130000002e-06, -1.5125094289999999e-07, 1.3249347649999999e-08, -1.7176120949999999e-07, 5.5040309179999998e-08, -1.8961238439999999e-08, 2.0254684359999999e-09, 1.0477986939999999e-10, 1.0975331210000001e-07, 9.0396438550000008e-09, 1.109461569e-07, -3.3950810800000002e-10, 3.3058395280000003e-05, -3.7233487110000001e-07, -0.00016611465490000001, 3.7419492339999999e-07, 6.6528469239999996e-06, 6.1000788830000002e-07, 1.6445040660000001e-05, 2.3612498590000001e-06, 2.0418083170000001e-05, 6.9911224980000004e-07, -4.1590333270000002e-07, 2.3037130070000001e-05, -3.9204540270000001e-07, 4.0622198560000001e-09, 3.2240923870000001e-13, -3.3394061860000003e-07, -1.69489017e-07, -1.510416928e-06, -1.132878229e-05, -3.0700108549999999e-06, -2.6337575370000001e-06, 1.3308031729999999e-05, -2.9680818169999998e-05, -4.0243086069999998e-05, 8.3950268510000004e-07, -6.0806020899999999e-05, 1.704561505e-06, 0.0002285082064, -2.3231437350000002e-06, -0.00041647177389999998, 0.00066465316879999999, 9.2145252939999998e-08, 2.68439262e-05, 2.3840923710000001e-07, 1.7667044690000001e-05, 8.4270003940000001e-07, 0.0001053980927, -1.0514595259999999e-08, -3.1862938039999999e-06, -7.3915591620000004e-06, -7.0901706080000002e-07, 3.9590246700000002e-09, 1.386548771e-05, -2.512068087e-06, -5.9999120419999995e-08, -6.2215829749999996e-06, -1.7292731310000002e-08, -1.480644984e-09, 5.7334211400000004e-09, -2.6633705509999999e-11, -1.324096305e-08, -3.5952006840000002e-10, -1.63987147e-08, 8.4376502089999998e-11, 1.405510944e-08, -1.6174674840000001e-10, -1.4731757529999999e-10, -1.2063184720000001e-10, -5.7811895729999998e-05, 0.0, 0.0, 0.0]
    normal_val = -0.00017

    end_val = -0.000170742878172
    sim_states, sim_times = check(a_matrix, b_matrix, step, max_time, start_point, inputs, normal_vec, end_val)

    if len(sys.argv) < 2 or sys.argv[1] != "noplot":
        plot(sim_states, sim_times, inputs, normal_vec, normal_val, max_time, step)

if __name__ == "__main__":
    check_instance()
