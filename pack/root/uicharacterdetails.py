# blackdragonx61
# __BL_CLIP_MASK__(Experimental)
# __BL_MOUSE_WHEEL_TOP_WINDOW__
# __BL_SMOOTH_SCROLL__
import ui
import localeInfo
import player
import item
import uiToolTip
import wndMgr
import app
import uiScriptLocale

LABEL_START_X = 0-10
LABEL_START_Y = 39
LABEL_WIDTH = 50
LABEL_HEIGHT = 17
LABEL_GAP = LABEL_HEIGHT+7
LABEL_NAME_POS_X = 0-10
TITLE_BAR_POS_X = 10
TITLE_BAR_WIDTH = 163

class Title:
	def __init__(self, parent, mask, text):
		self.horizontalbar = ui.HorizontalBar()
		self.horizontalbar.SetParent(parent)
		self.horizontalbar.Create(TITLE_BAR_WIDTH)
		self.horizontalbar.Show()

		self.horizontalbar_name = ui.TextLine()
		self.horizontalbar_name.SetParent(self.horizontalbar)
		self.horizontalbar_name.SetPosition(0, 0)
		self.horizontalbar_name.SetHorizontalAlignCenter()
		self.horizontalbar_name.SetVerticalAlignCenter()
		self.horizontalbar_name.SetWindowHorizontalAlignCenter()
		self.horizontalbar_name.SetWindowVerticalAlignCenter()
		self.horizontalbar_name.SetText(text)
		self.horizontalbar_name.Show()

		if app.__BL_CLIP_MASK__:
			self.horizontalbar.SetClippingMaskWindow(mask)

	def __del__(self):
		self.horizontalbar = None
		self.horizontalbar_name = None

	def SetY(self, y):
		self.horizontalbar.SetPosition(TITLE_BAR_POS_X, y)
	
	def GetGap(self):
		return LABEL_GAP

class Label:
	def __init__(self, parent, mask, text, tooltip_text, type):
		self.type = type
		
		self.label_name = ui.Button()
		self.label_name.SetParent(parent)
		self.label_name.SetUpVisual(uiScriptLocale.WINDOWS_PATH + "details.sub")
		self.label_name.SetOverVisual(uiScriptLocale.WINDOWS_PATH + "details.sub")
		self.label_name.SetDownVisual(uiScriptLocale.WINDOWS_PATH + "details.sub")
		self.label_name.SetWindowHorizontalAlignCenter()
		self.label_name.SetOverEvent( ui.__mem_func__(parent.ButtonOverIn), tooltip_text)
		self.label_name.SetOverOutEvent( ui.__mem_func__(parent.ButtonOverOut))
		self.label_name.SetText(text)
		self.label_name.Show()

		self.label = ui.ThinBoardCircle()
		self.label.SetParent(parent)
		self.label.SetSize(LABEL_WIDTH, LABEL_HEIGHT)
		self.label.SetWindowHorizontalAlignCenter()
		self.label.Show()

		self.label_value = ui.TextLine()
		self.label_value.SetParent(self.label)
		self.label_value.SetPosition(0, 0)
		self.label_value.SetHorizontalAlignCenter()
		self.label_value.SetVerticalAlignCenter()
		self.label_value.SetWindowHorizontalAlignCenter()
		self.label_value.SetWindowVerticalAlignCenter()
		self.label_value.SetText(str(player.GetStatus(self.type)))
		self.label_value.Show()

		if app.__BL_CLIP_MASK__:
			self.label_name.SetClippingMaskWindow(mask)
			self.label.SetClippingMaskWindow(mask)

	def __del__(self):
		self.label_name = None
		self.label = None
		self.label_value = None

	def SetY(self, y):
		self.label_name.SetPosition(LABEL_NAME_POS_X, y)
		self.label.SetPosition(LABEL_START_X, y + LABEL_GAP)
	
	def GetGap(self):
		return LABEL_GAP * 2
	
	def Refresh(self):
		self.label_value.SetText(str(player.GetStatus(self.type)))

class CharacterDetailsUI(ui.ScriptWindow):
	def __init__(self, parent):
		self.uiCharacterStatus = parent
		ui.ScriptWindow.__init__(self)
		self.toolTip = uiToolTip.ToolTip()

		self.object_list = []
		
		self.__LoadScript()
	
	def __del__(self):
		self.uiCharacterStatus = None
		self.toolTip = None
		ui.ScriptWindow.__del__(self)

		self.object_list = []
		
	def __LoadScript(self):
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/characterdetailswindow.py")
		except:
			import exception
			exception.Abort("CharacterDetailsUI.__LoadScript")
		
		self.Width = 253 - 3
					
		self.GetChild("TitleBar").CloseButtonHide()
		self.ScrollBar = self.GetChild("ScrollBar")
		self.ScrollBar.SetScrollEvent(ui.__mem_func__(self.ArrangePosition))
			
		self.__Initialize()
		
	def __Initialize(self):
		self.object_list.append(Title(self, self.GetChild("object_area_window"), localeInfo.DETAILS_CATE_1))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_1, localeInfo.DETAILS_TOOLTIP_1, item.GetApplyPoint( item.APPLY_ATTBONUS_HUMAN )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_2, localeInfo.DETAILS_TOOLTIP_2, item.GetApplyPoint( item.APPLY_RESIST_HUMAN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_3, localeInfo.DETAILS_TOOLTIP_3, item.GetApplyPoint( item.APPLY_ATTBONUS_ORC )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_4, localeInfo.DETAILS_TOOLTIP_4, item.GetApplyPoint( item.APPLY_ATTBONUS_UNDEAD )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_5, localeInfo.DETAILS_TOOLTIP_5, item.GetApplyPoint( item.APPLY_ATTBONUS_MONSTER )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_6, localeInfo.DETAILS_TOOLTIP_6, item.GetApplyPoint( item.APPLY_ATTBONUS_CZ )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_7, localeInfo.DETAILS_TOOLTIP_7, item.GetApplyPoint( item.APPLY_ATTBONUS_ANIMAL )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_8, localeInfo.DETAILS_TOOLTIP_8, item.GetApplyPoint( item.APPLY_ATTBONUS_MILGYO )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_9, localeInfo.DETAILS_TOOLTIP_9, item.GetApplyPoint( item.APPLY_ATTBONUS_DEVIL )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_10, localeInfo.DETAILS_TOOLTIP_10, item.GetApplyPoint( item.APPLY_ATTBONUS_DESERT )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_11, localeInfo.DETAILS_TOOLTIP_11, item.GetApplyPoint( item.APPLY_ATTBONUS_INSECT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_12, localeInfo.DETAILS_TOOLTIP_12, item.GetApplyPoint( item.APPLY_ATT_GRADE_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_13, localeInfo.DETAILS_TOOLTIP_13, item.GetApplyPoint( item.APPLY_DEF_GRADE_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_14, localeInfo.DETAILS_TOOLTIP_14, item.GetApplyPoint( item.APPLY_NORMAL_HIT_DAMAGE_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_15, localeInfo.DETAILS_TOOLTIP_15, item.GetApplyPoint( item.APPLY_NORMAL_HIT_DEFEND_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_16, localeInfo.DETAILS_TOOLTIP_16, item.GetApplyPoint( item.APPLY_SKILL_DAMAGE_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_17, localeInfo.DETAILS_TOOLTIP_17, item.GetApplyPoint( item.APPLY_SKILL_DEFEND_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_18, localeInfo.DETAILS_TOOLTIP_18, item.GetApplyPoint( item.APPLY_MELEE_MAGIC_ATTBONUS_PER )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_19, localeInfo.DETAILS_TOOLTIP_19, item.GetApplyPoint( item.APPLY_MAGIC_ATTBONUS_PER )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_20, localeInfo.DETAILS_TOOLTIP_20, item.GetApplyPoint( item.APPLY_CRITICAL_PCT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_21, localeInfo.DETAILS_TOOLTIP_21, item.GetApplyPoint( item.APPLY_PENETRATE_PCT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_22, localeInfo.DETAILS_TOOLTIP_22, item.GetApplyPoint( item.APPLY_ANTI_CRITICAL_PCT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_23, localeInfo.DETAILS_TOOLTIP_23, item.GetApplyPoint( item.APPLY_ANTI_PENETRATE_PCT )))

		self.object_list.append(Title(self, self.GetChild("object_area_window"), localeInfo.DETAILS_CATE_2))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_76, localeInfo.DETAILS_TOOLTIP_76, item.GetApplyPoint( item.APPLY_RESIST_MAGIC )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_24, localeInfo.DETAILS_TOOLTIP_24, item.GetApplyPoint( item.APPLY_RESIST_ELEC )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_25, localeInfo.DETAILS_TOOLTIP_25, item.GetApplyPoint( item.APPLY_RESIST_ICE )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_26, localeInfo.DETAILS_TOOLTIP_26, item.GetApplyPoint( item.APPLY_RESIST_DARK )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_27, localeInfo.DETAILS_TOOLTIP_27, item.GetApplyPoint( item.APPLY_RESIST_FIRE )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_28, localeInfo.DETAILS_TOOLTIP_28, item.GetApplyPoint( item.APPLY_RESIST_WIND )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_29, localeInfo.DETAILS_TOOLTIP_29, item.GetApplyPoint( item.APPLY_RESIST_EARTH )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_77, localeInfo.DETAILS_TOOLTIP_77, item.GetApplyPoint( item.APPLY_RESIST_MAGIC_REDUCTION )))
		# if app.ENABLE_ELEMENT_ADD:
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_30, localeInfo.DETAILS_30, item.GetApplyPoint( item.APPLY_ENCHANT_ELECT )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_31, localeInfo.DETAILS_31, item.GetApplyPoint( item.APPLY_ENCHANT_ICE )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_32, localeInfo.DETAILS_32, item.GetApplyPoint( item.APPLY_ENCHANT_DARK )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_33, localeInfo.DETAILS_33, item.GetApplyPoint( item.APPLY_ENCHANT_FIRE )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_34, localeInfo.DETAILS_34, item.GetApplyPoint( item.APPLY_ENCHANT_WIND )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_35, localeInfo.DETAILS_35, item.GetApplyPoint( item.APPLY_ENCHANT_EARTH )))

		self.object_list.append(Title(self, self.GetChild("object_area_window"), localeInfo.DETAILS_CATE_3))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_36, localeInfo.DETAILS_36, item.GetApplyPoint( item.APPLY_ATTBONUS_WARRIOR )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_37, localeInfo.DETAILS_37, item.GetApplyPoint( item.APPLY_ATTBONUS_ASSASSIN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_38, localeInfo.DETAILS_38, item.GetApplyPoint( item.APPLY_ATTBONUS_SURA )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_39, localeInfo.DETAILS_39, item.GetApplyPoint( item.APPLY_ATTBONUS_SHAMAN )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_40, localeInfo.DETAILS_40, item.GetApplyPoint( item.APPLY_ATTBONUS_WOLFMAN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_41, localeInfo.DETAILS_41, item.GetApplyPoint( item.APPLY_RESIST_WARRIOR )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_42, localeInfo.DETAILS_42, item.GetApplyPoint( item.APPLY_RESIST_ASSASSIN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_43, localeInfo.DETAILS_43, item.GetApplyPoint( item.APPLY_RESIST_SURA )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_44, localeInfo.DETAILS_44, item.GetApplyPoint( item.APPLY_RESIST_SHAMAN )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_45, localeInfo.DETAILS_45, item.GetApplyPoint( item.APPLY_RESIST_WOLFMAN )))
		
		self.object_list.append(Title(self, self.GetChild("object_area_window"), localeInfo.DETAILS_CATE_4))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_46, localeInfo.DETAILS_46, item.GetApplyPoint( item.APPLY_RESIST_SWORD )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_47, localeInfo.DETAILS_47, item.GetApplyPoint( item.APPLY_RESIST_TWOHAND )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_48, localeInfo.DETAILS_48, item.GetApplyPoint( item.APPLY_RESIST_DAGGER )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_49, localeInfo.DETAILS_49, item.GetApplyPoint( item.APPLY_RESIST_CLAW )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_50, localeInfo.DETAILS_50, item.GetApplyPoint( item.APPLY_RESIST_BELL )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_51, localeInfo.DETAILS_51, item.GetApplyPoint( item.APPLY_RESIST_FAN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_52, localeInfo.DETAILS_52, item.GetApplyPoint( item.APPLY_RESIST_BOW )))
		# if app.ENABLE_PENDANT:
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_SWORD, localeInfo.DETAILS_TOOLTIP_ATTBONUS_SWORD, item.GetApplyPoint( item.APPLY_ATTBONUS_SWORD )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_TWOHAND, localeInfo.DETAILS_TOOLTIP_ATTBONUS_TWOHAND, item.GetApplyPoint( item.APPLY_ATTBONUS_TWOHAND )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_DAGGER, localeInfo.DETAILS_TOOLTIP_ATTBONUS_DAGGER, item.GetApplyPoint( item.APPLY_ATTBONUS_DAGGER )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_BELL, localeInfo.DETAILS_TOOLTIP_ATTBONUS_BELL, item.GetApplyPoint( item.APPLY_ATTBONUS_BELL )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_FAN, localeInfo.DETAILS_TOOLTIP_ATTBONUS_FAN, item.GetApplyPoint( item.APPLY_ATTBONUS_FAN )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_BOW, localeInfo.DETAILS_TOOLTIP_ATTBONUS_BOW, item.GetApplyPoint( item.APPLY_ATTBONUS_BOW )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_ATTBONUS_CLAW, localeInfo.DETAILS_TOOLTIP_ATTBONUS_CLAW, item.GetApplyPoint( item.APPLY_ATTBONUS_CLAW )))
		# 	self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_RESIST_MOUNT_FALL, localeInfo.DETAILS_TOOLTIP_RESIST_MOUNT_FALL, item.GetApplyPoint( item.APPLY_RESIST_MOUNT_FALL )))

		self.object_list.append(Title(self, self.GetChild("object_area_window"), localeInfo.DETAILS_CATE_5))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_53, localeInfo.DETAILS_53, item.GetApplyPoint( item.APPLY_STUN_PCT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_54, localeInfo.DETAILS_54, item.GetApplyPoint( item.APPLY_SLOW_PCT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_55, localeInfo.DETAILS_55, item.GetApplyPoint( item.APPLY_POISON_PCT )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_56, localeInfo.DETAILS_56, item.GetApplyPoint( item.APPLY_POISON_REDUCE )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_57, localeInfo.DETAILS_57, item.GetApplyPoint( item.APPLY_BLEEDING_PCT )))
		# self.item_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_58, localeInfo.DETAILS_58, item.GetApplyPoint( item.APPLY_BLEEDING_REDUCE )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_59, localeInfo.DETAILS_59, item.GetApplyPoint( item.APPLY_STEAL_HP )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_60, localeInfo.DETAILS_60, item.GetApplyPoint( item.APPLY_STEAL_SP )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_61, localeInfo.DETAILS_61, item.GetApplyPoint( item.APPLY_HP_REGEN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_62, localeInfo.DETAILS_62, item.GetApplyPoint( item.APPLY_SP_REGEN )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_63, localeInfo.DETAILS_63, item.GetApplyPoint( item.APPLY_BLOCK )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_64, localeInfo.DETAILS_64, item.GetApplyPoint( item.APPLY_DODGE )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_65, localeInfo.DETAILS_65, item.GetApplyPoint( item.APPLY_REFLECT_MELEE )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_66, localeInfo.DETAILS_66, item.GetApplyPoint( item.APPLY_KILL_HP_RECOVER )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_67, localeInfo.DETAILS_67, item.GetApplyPoint( item.APPLY_KILL_SP_RECOVER )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_68, localeInfo.DETAILS_68, item.GetApplyPoint( item.APPLY_EXP_DOUBLE_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_69, localeInfo.DETAILS_69, item.GetApplyPoint( item.APPLY_GOLD_DOUBLE_BONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_70, localeInfo.DETAILS_70, item.GetApplyPoint( item.APPLY_ITEM_DROP_BONUS )))

		self.object_list.append(Title(self, self.GetChild("object_area_window"), localeInfo.DETAILS_CATE_6))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_71, localeInfo.DETAILS_71, item.GetApplyPoint( item.APPLY_MALL_ATTBONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_72, localeInfo.DETAILS_72, item.GetApplyPoint( item.APPLY_MALL_DEFBONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_73, localeInfo.DETAILS_73, item.GetApplyPoint( item.APPLY_MALL_EXPBONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_74, localeInfo.DETAILS_74, item.GetApplyPoint( item.APPLY_MALL_ITEMBONUS )))
		self.object_list.append(Label(self, self.GetChild("object_area_window"), localeInfo.DETAILS_75, localeInfo.DETAILS_75, item.GetApplyPoint( item.APPLY_MALL_GOLDBONUS )))
		
		self.total_gap = LABEL_START_Y
		for obj in self.object_list:
			self.total_gap += obj.GetGap()

		self.ScrollBar.SetScrollStep(0.05)
		
		self.ArrangePosition()
		
	def Show(self):
		ui.ScriptWindow.Show(self)
		self.SetTop()
		if app.__BL_MOUSE_WHEEL_TOP_WINDOW__:
			wndMgr.SetWheelTopWindow(self.hWnd)
		
	def Close(self):
		self.Hide()
		if app.__BL_MOUSE_WHEEL_TOP_WINDOW__:
			wndMgr.ClearWheelTopWindow()
	
	def AdjustPosition(self, x, y):
		self.SetPosition(x + self.Width, y)
			
	def RefreshLabel(self):
		for obj in self.object_list:
			if isinstance(obj, Label):
				obj.Refresh()

	# def OnTop(self):
	# 	if self.uiCharacterStatus:
	# 		self.uiCharacterStatus.SetTop()

	def ButtonOverIn(self, tooltip_text):
		arglen = len(tooltip_text)
		pos_x, pos_y = wndMgr.GetMousePosition()
		
		self.toolTip.ClearToolTip()
		self.toolTip.SetThinBoardSize(11 * arglen)
		self.toolTip.SetToolTipPosition(pos_x + 50, pos_y + 50)
		self.toolTip.AppendTextLine(tooltip_text, 0xffffff00)
		self.toolTip.Show()	

	def ButtonOverOut(self):
		self.toolTip.Hide()

	def ArrangePosition(self):
		y = -self.ScrollBar.GetPos() * (self.total_gap - 350)
		for obj in self.object_list:
			obj.SetY(y + LABEL_START_Y)
			y += obj.GetGap()

	if app.__BL_MOUSE_WHEEL_TOP_WINDOW__:
		def OnMouseWheelButtonUp(self):
			if self.ScrollBar:
				self.ScrollBar.OnUp()
				return True
		
			return False
		
		def OnMouseWheelButtonDown(self):
			if self.ScrollBar:
				self.ScrollBar.OnDown()
				return True
		
			return False