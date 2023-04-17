import numpy as np


# Pixel-space filters for cleaning up the AlphaPose 2D pose predictions. 
# NOTE: This uses "new" system view numbering!
AP_view_filters = {
        '001': {"x_min": None, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": None, "bbx_h_max": None},
        '002': {"x_min": 1700, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": None, "bbx_h_max": None},
        '003': {"x_min": None, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": 1000, "bbx_h_max": None},
        '004': {"x_min": None, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": 1000, "bbx_h_max": None},
        '005': {"x_min": None, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": None, "bbx_h_max": None},
        '006': {"x_min": None, "x_max": None, "bbx_w_min": None, "bbx_w_max": 2920, "bbx_h_min": None, "bbx_h_max": None},
        '007': {"x_min":  960, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": None, "bbx_h_max": None},
        '008': {"x_min": None, "x_max": None, "bbx_w_min": None, "bbx_w_max": None, "bbx_h_min": None, "bbx_h_max": None},
}

# Collection of timestamp (?) filters for AlphaPose outputs of "free_form_oval" task for CH3 (row1) and CH4 (row2)
ts_row1_filters = {
        'S01': np.concatenate((np.arange(840,960), np.arange(1250,1375), np.arange(1675,1805), np.arange(2300,2430))),
        'S02': np.concatenate((np.arange(615,675), np.arange(840,900), np.arange(1105,1165), np.arange(1395,1455), np.arange(1640,1700))),
        'S03': np.concatenate((np.arange(220,280), np.arange(450,510), np.arange(685,755), np.arange(920,985), np.arange(1160,1230))),
        'S04': np.concatenate((np.arange(200,250), np.arange(410,460), np.arange(600,670), np.arange(830,880), np.arange(1040,1100))),
        'S05': np.concatenate((np.arange(160,240), np.arange(480,560), np.arange(770,850), np.arange(1040,1140))),
        'S06': np.concatenate((np.arange(230,280), np.arange(430,480), np.arange(630,680), np.arange(820,870))),
        'S07': np.concatenate((np.arange(155,195), np.arange(330,370), np.arange(500,540), np.arange(670,710), np.arange(840,880))),
        'S08': np.concatenate((np.arange(130,185), np.arange(360,440), np.arange(650,700))),
        'S09': np.concatenate((np.arange(295,345), np.arange(510,570), np.arange(750,815))),
        'S10': np.concatenate((np.arange(235,300), np.arange(500,580), np.arange(750,830))),
        'S11': np.concatenate((np.arange(230,290), np.arange(480,540), np.arange(730,810))),
        'S12': np.concatenate((np.arange(265,330), np.arange(505,570), np.arange(790,840))),
        'S13': np.concatenate((np.arange(170,210), np.arange(345,380), np.arange(520,565), np.arange(695,740))),
        'S14': np.concatenate((np.arange(260,370), np.arange(600,700))),
        'S15': np.concatenate((np.arange(160,210), np.arange(390,435), np.arange(620,670), np.arange(840,900))),
        'S16': np.concatenate((np.arange(180,240), np.arange(430,500), np.arange(710,765))),
        'S17': np.concatenate((np.arange(170,220), np.arange(400,460), np.arange(650,700))),
        'S18': np.concatenate((np.arange(290,340), np.arange(510,580), np.arange(780,830))), 
        'S19': np.concatenate((np.arange(290,340), np.arange(500,550), np.arange(710,760))),
        'S20': np.concatenate((np.arange(260,320), np.arange(520,590), np.arange(790,870))),
        'S21': np.concatenate((np.arange(240,290), np.arange(450,495), np.arange(640,680), np.arange(820,870))),
        'S22': np.concatenate((np.arange(230,280), np.arange(410,460), np.arange(760,810))),
        'S23': np.concatenate((np.arange(210,280), np.arange(480,550), np.arange(780,850))),
        'S24': np.concatenate((np.arange(220,270), np.arange(420,470), np.arange(620,690))),
        'S25': np.concatenate((np.arange(200,260), np.arange(400,460), np.arange(610,670), np.arange(800,860))),
        'S26': np.concatenate((np.arange(250,310), np.arange(450,510), np.arange(650,710))),
        'S27': np.concatenate((np.arange(230,290), np.arange(445,505), np.arange(670,730))),
        'S28': np.concatenate((np.arange(840,960), np.arange(1280,1400), np.arange(1780,1900), np.arange(2280,2400))),
        'S29': np.concatenate((np.arange(390,510), np.arange(780,900), np.arange(1160,1280))),
        'S30': np.concatenate((np.arange(220,270), np.arange(420,490), np.arange(650,695), np.arange(840,880))),
        'S31': np.concatenate((np.arange(1000,1190), np.arange(1570,1780))),
        'S32': np.concatenate((np.arange(230,270), np.arange(400,450), np.arange(590,640))),
        'S33': np.concatenate((np.arange(500,560), np.arange(700,770))),
        'S34': np.concatenate((np.arange(210,270), np.arange(430,490), np.arange(650,710))),
        'S35': np.concatenate((np.arange(210,260), np.arange(430,490), np.arange(690,740))),
        }

ts_row2_filters = {
        'S01': np.concatenate((np.arange(840,960), np.arange(1250,1375), np.arange(1675,1805), np.arange(2300,2430))),
        'S02': np.concatenate((np.arange(605,665), np.arange(830,890), np.arange(1095,1155), np.arange(1385,1445), np.arange(1630,1690))),
        'S03': None,
        'S04': None,
        'S05': None,
        'S06': None,
        'S07': None,
        'S08': None,
        'S09': None,
        'S10': None,
        'S11': None,
        'S12': None,
        'S13': None,
        'S14': None,
        'S15': None,
        'S16': None,
        'S17': None,
        'S18': None, 
        'S19': None,
        'S20': None,
        'S21': None,
        'S22': None,
        'S23': None,
        'S24': None,
        'S25': np.concatenate((np.arange(194,254), np.arange(394,454), np.arange(604,664), np.arange(794,854))),
        'S26': np.concatenate((np.arange(246,306), np.arange(446,506), np.arange(646,706))),
        'S27': np.concatenate((np.arange(225,285), np.arange(440,500), np.arange(665,725))),
        'S28': np.concatenate((np.arange(840,960), np.arange(1280,1400), np.arange(1780,1900), np.arange(2280,2400))),
        'S29': np.concatenate((np.arange(390,510), np.arange(780,900), np.arange(1160,1280))),
        'S30': None,
        'S31': None,
        'S32': None,
        'S33': None,
        'S34': None,
        'S35': None,
        }