import tkinter
from typing import Callable, Tuple, Any, Literal
import customtkinter as ctk

ctk.CTk

class Botao(ctk.CTkButton):
    def __init__(self,
                 master: Any,
                 width: int = 140,
                 height: int = 28,
                 corner_radius: int | None = None,
                 border_width: int | None = None,
                 border_spacing: int = 2,
                 
                 bg_color: str | Tuple[str, str] = "transparent",
                 fg_color: str | Tuple[str, str] | None = None,
                 hover_color: str | Tuple[str, str] | None = None,
                 border_color: str | Tuple[str, str] | None = None,
                 text_color: str | Tuple[str, str] | None = None,
                 text_color_disabled: str | Tuple[str, str] | None = None,
                 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
                 round_width_to_even_numbers: bool = True,
                 round_height_to_even_numbers: bool = True,
                 
                 text: str = "CTkButton",
                 font: tuple | ctk.CTkFont | None = None,
                 textvariable: ctk.Variable | None = None,
                 image: ctk.CTkImage | Any | None = None,
                 state: str = "normal", hover: bool = True,
                 command: Callable[[], Any] | None = None,
                 compound: str = "left", anchor: str = "center",
                 **kwargs):
        
        super().__init__(
            master, width, height, corner_radius, border_width, border_spacing, bg_color, 
            fg_color, hover_color, border_color, text_color, text_color_disabled, 
            background_corner_colors, round_width_to_even_numbers, round_height_to_even_numbers,
            text, font, textvariable, image, state, hover, command, compound, anchor, **kwargs)



class Frame(ctk.CTkFrame):
    def __init__(self, 
                 master: Any,
                 width: int = 200,
                 height: int = 200,
                 corner_radius: int | str | None = None,
                 border_width: int | str | None = None,
                 
                 bg_color: str | Tuple[str] = "transparent",
                 fg_color: str | Tuple[str] | None = None,
                 border_color: str | Tuple[str] | None = None,
                 
                 background_corner_colors: Tuple[str | Tuple[str]] | None = None,
                 overwrite_preferred_drawing_method: str | None = None,
                 **kwargs):
        
        super().__init__(
            master, width, height, corner_radius, border_width, bg_color, fg_color, border_color,
            background_corner_colors, overwrite_preferred_drawing_method, **kwargs)



class Texto(ctk.CTkLabel):
    def __init__(self, 
                 master: Any, 
                 width: int = 0,
                 height: int = 28,
                 corner_radius: int | None = None,
                 
                 bg_color: str | Tuple[str] = "transparent",
                 fg_color: str | Tuple[str] | None = None,
                 text_color: str | Tuple[str] | None = None,
                 text_color_disabled: str | Tuple[str] | None = None, 
                 
                 text: str = "CTkLabel", 
                 font: Tuple | ctk.CTkFont | None = None,
                 image: ctk.CTkImage | None = None,
                 compound: str = "center",
                 anchor: str = "center", 
                 wraplength: int = 0, 
                 **kwargs):
        
        super().__init__(
            master, width, height, corner_radius, bg_color, fg_color, text_color,
            text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)



class EntradaTexto(ctk.CTkEntry):
    def __init__(self, 
                 master: Any,
                 width: int = 140,
                 height: int = 28, 
                 corner_radius: int | None = None, 
                 border_width: int | None = None,
                 
                 bg_color: str | Tuple[str] = "transparent",
                 fg_color: str | Tuple[str] | None = None,
                 border_color: str | Tuple[str] | None = None,
                 text_color: str | Tuple[str] | None = None,
                 placeholder_text_color: str | Tuple[str] | None = None, 
                 
                 textvariable: ctk.Variable | None = None,
                 placeholder_text: str | None = None,
                 font: Tuple | ctk.CTkFont | None = None, 
                 state: str = tkinter.NORMAL, 
                 **kwargs):
        
        super().__init__(
            master, width, height, corner_radius, border_width, bg_color, fg_color, border_color,
            text_color, placeholder_text_color, textvariable, placeholder_text, font, state, **kwargs)



class Fonte(ctk.CTkFont):
    def __init__(self, 
                 family: str | None = None,
                 size: int | None = None,
                 weight: Literal['normal'] | Literal['bold'] = None,
                 slant: Literal['italic'] | Literal['roman'] = "roman",
                 underline: bool = False,
                 overstrike: bool = False):
        
        super().__init__(family, size, weight, slant, underline, overstrike)



class CaixaMarcar(ctk.CTkCheckBox):
    def __init__(self,
                 master: Any,
                 width: int = 100,
                 height: int = 24,
                 checkbox_width: int = 24,
                 checkbox_height: int = 24,
                 corner_radius: int | None = None,
                 border_width: int | None = None,
                 
                 bg_color: str | Tuple[str] = "transparent",
                 fg_color: str | Tuple[str] | None = None,
                 hover_color: str | Tuple[str] | None = None,
                 border_color: str | Tuple[str] | None = None,
                 checkmark_color: str | Tuple[str] | None = None,
                 text_color: str | Tuple[str] | None = None,
                 text_color_disabled: str | Tuple[str] | None = None,
                 
                 text: str = "CTkCheckBox",
                 font: Tuple | ctk.CTkFont | None = None,
                 textvariable: tkinter.Variable | None = None,
                 state: str = tkinter.NORMAL,
                 hover: bool = True, 
                 command: Callable[[], Any] | None = None,
                 onvalue: int | str = 1,
                 offvalue: int | str = 0,
                 variable: tkinter.Variable | None = None,
                 **kwargs):
        
        super().__init__(
            master, width, height, checkbox_width, checkbox_height, corner_radius, border_width, 
            bg_color, fg_color, hover_color, border_color, checkmark_color, text_color, text_color_disabled, 
            text, font, textvariable, state, hover, command, onvalue, offvalue, variable, **kwargs)



class FrameSc(ctk.CTkScrollableFrame):
    def __init__(self, 
                 master: Any,
                 width: int = 200,
                 height: int = 200,
                 corner_radius: int | str | None = None,
                 border_width: int | str | None = None,
                 bg_color: str | Tuple[str] = "transparent",
                 fg_color: str | Tuple[str] | None = None,
                 border_color: str | Tuple[str] | None = None,
                 scrollbar_fg_color: str | Tuple[str] | None = None,
                 scrollbar_button_color: str | Tuple[str] | None = None,
                 scrollbar_button_hover_color: str | Tuple[str] | None = None,
                 label_fg_color: str | Tuple[str] | None = None, 
                 label_text_color: str | Tuple[str] | None = None,
                 label_text: str = "",
                 label_font: Tuple | ctk.CTkFont | None = None,
                 label_anchor: str = "center",
                 orientation: Literal['vertical'] | Literal['horizontal'] = "vertical"):
        
        super().__init__(
            master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, 
            scrollbar_fg_color, scrollbar_button_color, scrollbar_button_hover_color, label_fg_color,
            label_text_color, label_text, label_font, label_anchor, orientation)


class Dialogo(ctk.CTkInputDialog):
    def __init__(self,
                 fg_color: str | Tuple[str] | None = None,
                 text_color: str | Tuple[str] | None = None,
                 button_fg_color: str | Tuple[str] | None = None,
                 button_hover_color: str | Tuple[str] | None = None,
                 button_text_color: str | Tuple[str] | None = None, 
                 entry_fg_color: str | Tuple[str] | None = None,
                 entry_border_color: str | Tuple[str] | None = None,
                 entry_text_color: str | Tuple[str] | None = None,
                 title: str = "CTkDialog",
                 font: Tuple | ctk.CTkFont | None = None, 
                 text: str = "CTkDialog"):
        
        super().__init__(
            fg_color, text_color, button_fg_color, button_hover_color, button_text_color,
            entry_fg_color, entry_border_color, entry_text_color, title, font, text)