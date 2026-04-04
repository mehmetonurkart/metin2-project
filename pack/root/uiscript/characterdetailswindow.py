# blackdragonx61
# __BL_CLIP_MASK__(Experimental)
# __BL_MOUSE_WHEEL_TOP_WINDOW__
# __BL_SMOOTH_SCROLL__
import localeInfo

MAINBOARD_WIDTH = 200
MAINBOARD_HEIGHT = 364#361

window = {
	"name" : "CharacterDetailsWindow",
	"style" : ("float",),
	
	"x" : 274, #24+253-3,
	"y" : (SCREEN_HEIGHT - 398) / 2,

	"width" : MAINBOARD_WIDTH,
	"height" : MAINBOARD_HEIGHT,
	
	"children" :
	(
		## MainBoard
		{
			"name" : "MainBoard",
			"type" : "board",
			"style" : ("attach","ltr"),
			
			## CharacterWindow.py ���� ����
			"x" : 0,
			"y" : 0,

			"width" : MAINBOARD_WIDTH,
			"height" : MAINBOARD_HEIGHT,
			
			"children" :
			(
				## Ÿ��Ʋ��
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 7,

					"width" : MAINBOARD_WIDTH - 13,
					
					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : 0, "text": localeInfo.DETAILS_TITLE, "all_align":"center" },
					),
				},
							
				## ��ũ�� ��
				{
					"name" : "ScrollBar",
					"type" : "scrollbar",

					"x" : 24,
					"y" : 31,
					"size" : MAINBOARD_HEIGHT - 40,
					"horizontal_align" : "right",
                    "smooth": 1,
				},
                
				{
					"name" : "object_area_window",
					"type" : "window",
					"style" : ("attach",),
					
					"x" : 10+5,
					"y" : 32+5,
					"width"		: 155,
					"height"	: 310,
				},
			),
		}, ## MainBoard End
	),
}