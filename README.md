The purpose of this script is to compute for a friend the probability of a certain number of events occurring in a game.

Given three probabilities: P_one = 0.1852, P_two = 0.2030, and P_three = 0.1740, the challenge is to compute the total probability of 10 or more successes on 12 independent trials with probability P_one, 12 independent trials with probability P_two, and 12 independent trials with probably P_three.

The strategy is to take the product of three binomial distribution probability density functions, and sum over success counts less than 10 in order to compute the probability of having less than 10 successes. The result is then subtracted from 1 to compute the probability of at least 10 successes.

The result of the calculation is below. The output is verbose as it shows the computation at each step, but simply scroll to the bottom to see the computed result:

```
(env) [wclark@mercury binomial_dist]$ python main.py
0 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.000567378230527177
cumulative probability at this point in the calculation is 0.000567378230527177
0 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0014342442437539293
cumulative probability at this point in the calculation is 0.0020016224742811064
0 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.0016617091298698667
cumulative probability at this point in the calculation is 0.003663331604150973
0 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0011668175488190344
cumulative probability at this point in the calculation is 0.004830149152970007
0 drops from C'thun, 0 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0005530376154511524
cumulative probability at this point in the calculation is 0.00538318676842116
0 drops from C'thun, 0 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.00018639911881549733
cumulative probability at this point in the calculation is 0.005569585887236658
0 drops from C'thun, 0 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 4.58099529292324e-05
cumulative probability at this point in the calculation is 0.00561539584016589
0 drops from C'thun, 0 drops from Faerlina, and 7 drops from Kel'thuzad has probability: 8.271461580442512e-06
cumulative probability at this point in the calculation is 0.0056236673017463325
0 drops from C'thun, 0 drops from Faerlina, and 8 drops from Kel'thuzad has probability: 1.089009015584895e-06
cumulative probability at this point in the calculation is 0.005624756310761918
0 drops from C'thun, 0 drops from Faerlina, and 9 drops from Kel'thuzad has probability: 1.0195726053902164e-07
cumulative probability at this point in the calculation is 0.005624858268022457
0 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0017341698488885862
cumulative probability at this point in the calculation is 0.007359028116911043
0 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.004383712644648145
cumulative probability at this point in the calculation is 0.011742740761559189
0 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.005078950364319944
cumulative probability at this point in the calculation is 0.016821691125879133
0 drops from C'thun, 1 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0035663331855999595
cumulative probability at this point in the calculation is 0.020388024311479094
0 drops from C'thun, 1 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0016903383077026442
cumulative probability at this point in the calculation is 0.022078362619181738
0 drops from C'thun, 1 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0005697217734436029
cumulative probability at this point in the calculation is 0.02264808439262534
0 drops from C'thun, 1 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.00014001636804969903
cumulative probability at this point in the calculation is 0.02278810076067504
0 drops from C'thun, 1 drops from Faerlina, and 7 drops from Kel'thuzad has probability: 2.5281405784137968e-05
cumulative probability at this point in the calculation is 0.022813382166459176
0 drops from C'thun, 1 drops from Faerlina, and 8 drops from Kel'thuzad has probability: 3.3285143813862038e-06
cumulative probability at this point in the calculation is 0.02281671068084056
0 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.002429360898725354
cumulative probability at this point in the calculation is 0.025246071579565914
0 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.006141047889271839
cumulative probability at this point in the calculation is 0.03138711946883775
0 drops from C'thun, 2 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.007114991319652722
cumulative probability at this point in the calculation is 0.03850211078849047
0 drops from C'thun, 2 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.004995998747455904
cumulative probability at this point in the calculation is 0.04349810953594638
0 drops from C'thun, 2 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0023679582441028892
cumulative probability at this point in the calculation is 0.045866067780049265
0 drops from C'thun, 2 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0007981108658090124
cumulative probability at this point in the calculation is 0.04666417864585828
0 drops from C'thun, 2 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.00019614589074967254
cumulative probability at this point in the calculation is 0.04686032453660795
0 drops from C'thun, 2 drops from Faerlina, and 7 drops from Kel'thuzad has probability: 3.5416172594717755e-05
cumulative probability at this point in the calculation is 0.04689574070920267
0 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0020625690608165907
cumulative probability at this point in the calculation is 0.048958309770019255
0 drops from C'thun, 3 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.005213854962451625
cumulative probability at this point in the calculation is 0.05417216473247088
0 drops from C'thun, 3 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.00604074963567337
cumulative probability at this point in the calculation is 0.060212914368144244
0 drops from C'thun, 3 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.004241688606162897
cumulative probability at this point in the calculation is 0.06445460297430713
0 drops from C'thun, 3 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0020104371541316878
cumulative probability at this point in the calculation is 0.06646504012843882
0 drops from C'thun, 3 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0006776098107872418
cumulative probability at this point in the calculation is 0.06714264993922606
0 drops from C'thun, 3 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.00016653122468500013
cumulative probability at this point in the calculation is 0.06730918116391106
0 drops from C'thun, 4 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.00118203063805267
cumulative probability at this point in the calculation is 0.06849121180196373
0 drops from C'thun, 4 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.002987990281179147
cumulative probability at this point in the calculation is 0.07147920208314287
0 drops from C'thun, 4 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.003461872517056226
cumulative probability at this point in the calculation is 0.0749410746001991
0 drops from C'thun, 4 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0024308547940588504
cumulative probability at this point in the calculation is 0.07737192939425795
0 drops from C'thun, 4 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0011521545422203874
cumulative probability at this point in the calculation is 0.07852408393647833
0 drops from C'thun, 4 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.00038832908541665343
cumulative probability at this point in the calculation is 0.07891241302189499
0 drops from C'thun, 5 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0004817108547547144
cumulative probability at this point in the calculation is 0.0793941238766497
0 drops from C'thun, 5 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0012176903931329826
cumulative probability at this point in the calculation is 0.08061181426978267
0 drops from C'thun, 5 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.001410810782358673
cumulative probability at this point in the calculation is 0.08202262505214135
0 drops from C'thun, 5 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0009906419537143221
cumulative probability at this point in the calculation is 0.08301326700585566
0 drops from C'thun, 5 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0004695355022750086
cumulative probability at this point in the calculation is 0.08348280250813067
0 drops from C'thun, 6 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.00014314327156136536
cumulative probability at this point in the calculation is 0.08362594577969204
0 drops from C'thun, 6 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0003618440084989478
cumulative probability at this point in the calculation is 0.08398778978819099
0 drops from C'thun, 6 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.00041923089120277595
cumulative probability at this point in the calculation is 0.08440702067939376
0 drops from C'thun, 6 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.00029437520205521787
cumulative probability at this point in the calculation is 0.08470139588144898
0 drops from C'thun, 7 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 3.1250852260574126e-05
cumulative probability at this point in the calculation is 0.08473264673370956
0 drops from C'thun, 7 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 7.899731176764985e-05
cumulative probability at this point in the calculation is 0.08481164404547721
0 drops from C'thun, 7 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 9.152594111578799e-05
cumulative probability at this point in the calculation is 0.084903169986593
0 drops from C'thun, 8 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 4.9748455214057e-06
cumulative probability at this point in the calculation is 0.08490814483211441
0 drops from C'thun, 8 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 1.2575638557742254e-05
cumulative probability at this point in the calculation is 0.08492072047067216
0 drops from C'thun, 9 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 5.631638872691243e-07
cumulative probability at this point in the calculation is 0.08492128363455943
1 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0015475471029990158
cumulative probability at this point in the calculation is 0.08646883073755846
1 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.003911959262786859
cumulative probability at this point in the calculation is 0.09038079000034531
1 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.004532378952163465
cumulative probability at this point in the calculation is 0.09491316895250877
1 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.003182542121373861
cumulative probability at this point in the calculation is 0.09809571107388264
1 drops from C'thun, 0 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0015084324945736883
cumulative probability at this point in the calculation is 0.09960414356845633
1 drops from C'thun, 0 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0005084111458708411
cumulative probability at this point in the calculation is 0.10011255471432717
1 drops from C'thun, 0 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.0001249485019513084
cumulative probability at this point in the calculation is 0.10023750321627849
1 drops from C'thun, 0 drops from Faerlina, and 7 drops from Kel'thuzad has probability: 2.2560746460941877e-05
cumulative probability at this point in the calculation is 0.10026006396273943
1 drops from C'thun, 0 drops from Faerlina, and 8 drops from Kel'thuzad has probability: 2.9703161956748538e-06
cumulative probability at this point in the calculation is 0.1002630342789351
1 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.004730018497999502
cumulative probability at this point in the calculation is 0.1049930527769346
1 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.011956753781867991
cumulative probability at this point in the calculation is 0.11694980655880259
1 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.013853042819912427
cumulative probability at this point in the calculation is 0.13080284937871503
1 drops from C'thun, 1 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.009727318202844074
cumulative probability at this point in the calculation is 0.14053016758155912
1 drops from C'thun, 1 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.004610466194205151
cumulative probability at this point in the calculation is 0.14514063377576428
1 drops from C'thun, 1 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0015539392112187817
cumulative probability at this point in the calculation is 0.14669457298698305
1 drops from C'thun, 1 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.000381900314621565
cumulative probability at this point in the calculation is 0.14707647330160462
1 drops from C'thun, 1 drops from Faerlina, and 7 drops from Kel'thuzad has probability: 6.895605819178723e-05
cumulative probability at this point in the calculation is 0.1471454293597964
1 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.006626180242178726
cumulative probability at this point in the calculation is 0.15377160960197514
1 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.01674995683495058
cumulative probability at this point in the calculation is 0.17052156643692573
1 drops from C'thun, 2 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.019406426986740558
cumulative probability at this point in the calculation is 0.18992799342366629
1 drops from C'thun, 2 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.013626788925314189
cumulative probability at this point in the calculation is 0.20355478234898047
1 drops from C'thun, 2 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.006458702014843227
cumulative probability at this point in the calculation is 0.2100134843638237
1 drops from C'thun, 2 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.002176879710571857
cumulative probability at this point in the calculation is 0.21219036407439554
1 drops from C'thun, 2 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.0005349958610727445
cumulative probability at this point in the calculation is 0.2127253599354683
1 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.005625740648943044
cumulative probability at this point in the calculation is 0.21835110058441135
1 drops from C'thun, 3 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.01422100057505215
cumulative probability at this point in the calculation is 0.2325721011594635
1 drops from C'thun, 3 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.01647638928610763
cumulative probability at this point in the calculation is 0.24904849044557115
1 drops from C'thun, 3 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.011569377464821335
cumulative probability at this point in the calculation is 0.2606178679103925
1 drops from C'thun, 3 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.005483548762079362
cumulative probability at this point in the calculation is 0.26610141667247184
1 drops from C'thun, 3 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0018482082026185156
cumulative probability at this point in the calculation is 0.26794962487509033
1 drops from C'thun, 4 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0032240364383999192
cumulative probability at this point in the calculation is 0.27117366131349024
1 drops from C'thun, 4 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0081498645077228
cumulative probability at this point in the calculation is 0.27932352582121306
1 drops from C'thun, 4 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.009442397498657041
cumulative probability at this point in the calculation is 0.2887659233198701
1 drops from C'thun, 4 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0066302549022047
cumulative probability at this point in the calculation is 0.2953961782220748
1 drops from C'thun, 4 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0031425481770134866
cumulative probability at this point in the calculation is 0.2985387263990883
1 drops from C'thun, 5 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0013138858659878217
cumulative probability at this point in the calculation is 0.2998526122650761
1 drops from C'thun, 5 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.003321299864627811
cumulative probability at this point in the calculation is 0.3031739121297039
1 drops from C'thun, 5 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.003848043547758855
cumulative probability at this point in the calculation is 0.30702195567746277
1 drops from C'thun, 5 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.002702016050484425
cumulative probability at this point in the calculation is 0.3097239717279472
1 drops from C'thun, 6 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.00039042907059152966
cumulative probability at this point in the calculation is 0.3101144007985387
1 drops from C'thun, 6 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0009869441881296779
cumulative probability at this point in the calculation is 0.31110134498666836
1 drops from C'thun, 6 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.0011434692349153771
cumulative probability at this point in the calculation is 0.31224481422158373
1 drops from C'thun, 7 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 8.523796522324489e-05
cumulative probability at this point in the calculation is 0.312330052186807
1 drops from C'thun, 7 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.00021546836729556337
cumulative probability at this point in the calculation is 0.31254552055410256
1 drops from C'thun, 8 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 1.3569092644541026e-05
cumulative probability at this point in the calculation is 0.3125590896467471
2 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.001934623808437405
cumulative probability at this point in the calculation is 0.3144937134551845
2 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.00489042919130424
cumulative probability at this point in the calculation is 0.31938414264648873
2 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.005666029946825855
cumulative probability at this point in the calculation is 0.3250501725933146
2 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.003978568243533892
cumulative probability at this point in the calculation is 0.32902874083684847
2 drops from C'thun, 0 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0018857257473892477
cumulative probability at this point in the calculation is 0.33091446658423773
2 drops from C'thun, 0 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0006355763293864
cumulative probability at this point in the calculation is 0.3315500429136241
2 drops from C'thun, 0 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.00015620096230682713
cumulative probability at this point in the calculation is 0.33170624387593095
2 drops from C'thun, 0 drops from Faerlina, and 7 drops from Kel'thuzad has probability: 2.8203701945404266e-05
cumulative probability at this point in the calculation is 0.33173444757787635
2 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.005913103635324366
cumulative probability at this point in the calculation is 0.3376475512132007
2 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.014947409673798156
cumulative probability at this point in the calculation is 0.3525949608869989
2 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.017318003701967108
cumulative probability at this point in the calculation is 0.369912964588966
2 drops from C'thun, 1 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.012160341582495059
cumulative probability at this point in the calculation is 0.38207330617146107
2 drops from C'thun, 1 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.005763648582986459
cumulative probability at this point in the calculation is 0.3878369547544475
2 drops from C'thun, 1 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.001942614728212385
cumulative probability at this point in the calculation is 0.3897795694826599
2 drops from C'thun, 1 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.00047742226371321324
cumulative probability at this point in the calculation is 0.3902569917463731
2 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.008283538530539092
cumulative probability at this point in the calculation is 0.3985405302769122
2 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0209395017575855
cumulative probability at this point in the calculation is 0.41948003203449774
2 drops from C'thun, 2 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.02426041547458755
cumulative probability at this point in the calculation is 0.4437404475090853
2 drops from C'thun, 2 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.01703515856569101
cumulative probability at this point in the calculation is 0.4607756060747763
2 drops from C'thun, 2 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.008074170191849916
cumulative probability at this point in the calculation is 0.4688497762666262
2 drops from C'thun, 2 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0027213668055823437
cumulative probability at this point in the calculation is 0.47157114307220854
2 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.007032866255539255
cumulative probability at this point in the calculation is 0.4786040093277478
2 drops from C'thun, 3 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.017777996055164606
cumulative probability at this point in the calculation is 0.49638200538291244
2 drops from C'thun, 3 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.020597508746722185
cumulative probability at this point in the calculation is 0.5169795141296346
2 drops from C'thun, 3 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.014463141734986517
cumulative probability at this point in the calculation is 0.5314426558646211
2 drops from C'thun, 3 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.00685510894581988
cumulative probability at this point in the calculation is 0.538297764810441
2 drops from C'thun, 4 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.004030441232393419
cumulative probability at this point in the calculation is 0.5423282060428344
2 drops from C'thun, 4 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.010188330863483606
cumulative probability at this point in the calculation is 0.552516536906318
2 drops from C'thun, 4 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.011804155734084516
cumulative probability at this point in the calculation is 0.5643206926404025
2 drops from C'thun, 4 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.008288632355652562
cumulative probability at this point in the calculation is 0.5726093249960551
2 drops from C'thun, 5 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0016425185850456499
cumulative probability at this point in the calculation is 0.5742518435811007
2 drops from C'thun, 5 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.00415203245227036
cumulative probability at this point in the calculation is 0.5784038760333711
2 drops from C'thun, 5 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.004810526703175222
cumulative probability at this point in the calculation is 0.5832144027365462
2 drops from C'thun, 6 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0004880842554056605
cumulative probability at this point in the calculation is 0.5837024869919519
2 drops from C'thun, 6 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.001233801362332953
cumulative probability at this point in the calculation is 0.5849362883542849
2 drops from C'thun, 7 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.00010655791774226467
cumulative probability at this point in the calculation is 0.5850428462720272
3 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.001465767997556077
cumulative probability at this point in the calculation is 0.5865086142695832
3 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0037052343570182678
cumulative probability at this point in the calculation is 0.5902138486266015
3 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.004292868377320195
cumulative probability at this point in the calculation is 0.5945067170039218
3 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.003014362783106189
cumulative probability at this point in the calculation is 0.597521079787028
3 drops from C'thun, 0 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0014287203748015412
cumulative probability at this point in the calculation is 0.5989498001618295
3 drops from C'thun, 0 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.00048154449436410286
cumulative probability at this point in the calculation is 0.5994313446561936
3 drops from C'thun, 0 drops from Faerlina, and 6 drops from Kel'thuzad has probability: 0.00011834568081829647
cumulative probability at this point in the calculation is 0.5995496903370119
3 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.00448006379177742
cumulative probability at this point in the calculation is 0.6040297541287893
3 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.011324907018439774
cumulative probability at this point in the calculation is 0.6153546611472291
3 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.013120987913616055
cumulative probability at this point in the calculation is 0.6284756490608452
3 drops from C'thun, 1 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0092132844914011
cumulative probability at this point in the calculation is 0.6376889335522463
3 drops from C'thun, 1 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.004366829150585389
cumulative probability at this point in the calculation is 0.6420557627028317
3 drops from C'thun, 1 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.0014718223190350749
cumulative probability at this point in the calculation is 0.6435275850218668
3 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0062760241198487965
cumulative probability at this point in the calculation is 0.6498036091417156
3 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.015864816419181946
cumulative probability at this point in the calculation is 0.6656684255608976
3 drops from C'thun, 2 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.018380907158785858
cumulative probability at this point in the calculation is 0.6840493327196834
3 drops from C'thun, 2 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.012906690256774569
cumulative probability at this point in the calculation is 0.696956022976458
3 drops from C'thun, 2 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.006117396168919181
cumulative probability at this point in the calculation is 0.7030734191453771
3 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.005328452096734864
cumulative probability at this point in the calculation is 0.708401871242112
3 drops from C'thun, 3 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.013469501183998058
cumulative probability at this point in the calculation is 0.72187137242611
3 drops from C'thun, 3 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.015605705366932371
cumulative probability at this point in the calculation is 0.7374770777930424
3 drops from C'thun, 3 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.010958001347240643
cumulative probability at this point in the calculation is 0.7484350791402831
3 drops from C'thun, 4 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0030536643603308023
cumulative probability at this point in the calculation is 0.7514887435006139
3 drops from C'thun, 4 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.007719190295848323
cumulative probability at this point in the calculation is 0.7592079337964622
3 drops from C'thun, 4 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.008943420233809738
cumulative probability at this point in the calculation is 0.768151354030272
3 drops from C'thun, 5 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0012444544344233936
cumulative probability at this point in the calculation is 0.7693958084646955
3 drops from C'thun, 5 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0031457879649831066
cumulative probability at this point in the calculation is 0.7725415964296786
3 drops from C'thun, 6 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0003697971039974158
cumulative probability at this point in the calculation is 0.772911393533676
4 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0007496140458782735
cumulative probability at this point in the calculation is 0.7736610075795542
4 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0018949081450288562
cumulative probability at this point in the calculation is 0.7755559157245832
4 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.0021954323181508657
cumulative probability at this point in the calculation is 0.777751348042734
4 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0015415868577814788
cumulative probability at this point in the calculation is 0.7792929349005155
4 drops from C'thun, 0 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0007306673787184612
cumulative probability at this point in the calculation is 0.780023602279234
4 drops from C'thun, 0 drops from Faerlina, and 5 drops from Kel'thuzad has probability: 0.00024626852086588326
cumulative probability at this point in the calculation is 0.7802698708000998
4 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.002291166644616656
cumulative probability at this point in the calculation is 0.7825610374447165
4 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.005791714229975276
cumulative probability at this point in the calculation is 0.7883527516746918
4 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.006710254864511303
cumulative probability at this point in the calculation is 0.795063006539203
4 drops from C'thun, 1 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.004711801236581785
cumulative probability at this point in the calculation is 0.7997748077757848
4 drops from C'thun, 1 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.0022332568815033524
cumulative probability at this point in the calculation is 0.8020080646572881
4 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0032096456194661183
cumulative probability at this point in the calculation is 0.8052177102767543
4 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.008113486747512416
cumulative probability at this point in the calculation is 0.8133311970242667
4 drops from C'thun, 2 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.00940025038422443
cumulative probability at this point in the calculation is 0.8227314474084911
4 drops from C'thun, 2 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.006600660076089791
cumulative probability at this point in the calculation is 0.829332107484581
4 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0027250441687646267
cumulative probability at this point in the calculation is 0.8320571516533456
4 drops from C'thun, 3 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.006888489375763366
cumulative probability at this point in the calculation is 0.838945641029109
4 drops from C'thun, 3 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.007980973768287578
cumulative probability at this point in the calculation is 0.8469266147973965
4 drops from C'thun, 4 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0015616862284607823
cumulative probability at this point in the calculation is 0.8484883010258573
4 drops from C'thun, 4 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.003947700780903285
cumulative probability at this point in the calculation is 0.8524360018067605
4 drops from C'thun, 5 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0006364312258520229
cumulative probability at this point in the calculation is 0.8530724330326125
5 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.000272613689340513
cumulative probability at this point in the calculation is 0.853345046721953
5 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0006891251614321928
cumulative probability at this point in the calculation is 0.8540341718833852
5 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.0007984174085842715
cumulative probability at this point in the calculation is 0.8548325892919694
5 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.0005606320786669216
cumulative probability at this point in the calculation is 0.8553932213706363
5 drops from C'thun, 0 drops from Faerlina, and 4 drops from Kel'thuzad has probability: 0.00026572331573619835
cumulative probability at this point in the calculation is 0.8556589446863725
5 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0008332333089504264
cumulative probability at this point in the calculation is 0.856492177995323
5 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0021062846841265015
cumulative probability at this point in the calculation is 0.8585984626794495
5 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.002440332255095716
cumulative probability at this point in the calculation is 0.8610387949345453
5 drops from C'thun, 1 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.001713550493892875
cumulative probability at this point in the calculation is 0.8627523454284381
5 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0011672584560139916
cumulative probability at this point in the calculation is 0.8639196038844521
5 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0029506484941370635
cumulative probability at this point in the calculation is 0.8668702523785892
5 drops from C'thun, 2 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.003418608485337977
cumulative probability at this point in the calculation is 0.8702888608639271
5 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0009910224448801352
cumulative probability at this point in the calculation is 0.8712798833088072
5 drops from C'thun, 3 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0025051511681715767
cumulative probability at this point in the calculation is 0.8737850344769789
5 drops from C'thun, 4 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0005679416583425367
cumulative probability at this point in the calculation is 0.8743529761353214
6 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 7.229102987666527e-05
cumulative probability at this point in the calculation is 0.8744252671651981
6 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0001827405210441611
cumulative probability at this point in the calculation is 0.8746080076862423
6 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.00021172237123397354
cumulative probability at this point in the calculation is 0.8748197300574763
6 drops from C'thun, 0 drops from Faerlina, and 3 drops from Kel'thuzad has probability: 0.00014866704033378281
cumulative probability at this point in the calculation is 0.87496839709781
6 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.00022095476634825172
cumulative probability at this point in the calculation is 0.8751893518641582
6 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0005585394093645878
cumulative probability at this point in the calculation is 0.8757478912735228
6 drops from C'thun, 1 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 0.0006471213253776155
cumulative probability at this point in the calculation is 0.8763950125989004
6 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0003095307360449474
cumulative probability at this point in the calculation is 0.8767045433349453
6 drops from C'thun, 2 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.0007824457346995765
cumulative probability at this point in the calculation is 0.8774869890696448
6 drops from C'thun, 3 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 0.0002627969026228537
cumulative probability at this point in the calculation is 0.8777497859722677
7 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 1.4084050844896286e-05
cumulative probability at this point in the calculation is 0.8777638700231126
7 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 3.5602298019544124e-05
cumulative probability at this point in the calculation is 0.8777994723211322
7 drops from C'thun, 0 drops from Faerlina, and 2 drops from Kel'thuzad has probability: 4.124866731804324e-05
cumulative probability at this point in the calculation is 0.8778407209884502
7 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 4.304736243182855e-05
cumulative probability at this point in the calculation is 0.8778837683508821
7 drops from C'thun, 1 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 0.00010881706144994917
cumulative probability at this point in the calculation is 0.877992585412332
7 drops from C'thun, 2 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 6.030411562752395e-05
cumulative probability at this point in the calculation is 0.8780528895279596
8 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 2.0007718278065113e-06
cumulative probability at this point in the calculation is 0.8780548902997873
8 drops from C'thun, 0 drops from Faerlina, and 1 drops from Kel'thuzad has probability: 5.057641133728808e-06
cumulative probability at this point in the calculation is 0.878059947940921
8 drops from C'thun, 1 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 6.1152825251401015e-06
cumulative probability at this point in the calculation is 0.8780660632234462
9 drops from C'thun, 0 drops from Faerlina, and 0 drops from Kel'thuzad has probability: 2.0211800715091137e-07
cumulative probability at this point in the calculation is 0.8780662653414533
Calculation done!
The probability of having less than 10 total drops of the three items in 12 weeks is 0.8780662653414533.
The probability of having 10 or more total drops of the three items in 12 weeks is 0.12193373465854673.
```
