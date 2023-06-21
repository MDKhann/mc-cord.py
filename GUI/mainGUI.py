import customtkinter
import tkinter
import tkinter.messagebox
from tkinter import filedialog
import ctypes
from PIL import Image, ImageTk
import contextlib
import threading
import json
import asyncio
try:
    from GUI.frames import nav_frames
except:
    from frames import nav_frames

class mc_cord_GUI(customtkinter.CTk):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.initial_load_save(path="GUI_config.json")
        self.configure_self()
        self.create_main_frames()
    
    def configure_self(self):
        self.geometry("1000x600")
        self.title("Mc-Cord")
        myappid = 'Apocorn.mc-cord.pre-alpha' # arbitrary string == 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        ico = Image.open("./GUI/logo.png")
        customtkinter.set_default_color_theme("green")
        #ico = ico.resize(resample=Image.Resampling.LANCZOS,size=((60,80)))
        icon = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, icon, icon)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
    
    def create_main_frames(self):
        self.frame_top = self.create_single_main_frame("red", 0)
        self.frame_bottom = self.create_single_main_frame("green", 1)
        self.load_all_frames()

    def create_single_main_frame(self, fg_color, row):
        result = customtkinter.CTkFrame(
            master=self, fg_color=fg_color, corner_radius=0
        )
        result.grid(row=row, column=0, sticky="nsew")
        result.grid_rowconfigure(0, weight=0)
        result.grid_rowconfigure(1, weight=1)
        result.grid_columnconfigure(0, weight=0)
        result.grid_columnconfigure(1, weight=1)

        return result
        
    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.dump_into_save()
            self.destroy()

    async def frame_handler(self):
        global active_frame
        if len(active_frame) == 1:
            (self.all_frames[active_frame[0]]).grid(row=1, column=1, sticky="nswe")
        while True:
            try:
                await asyncio.sleep(0.1)
                self.update()
                if (
                    len(active_frame) > 1
                    and str(type(active_frame[-1])) == "<class 'str'>"
                    and str(type(active_frame[-2])) == "<class 'str'>"
                    and active_frame[-1] != active_frame[-2]
                ):
                    (self.all_frames[active_frame[-2]]).grid_remove()
                    (self.all_frames[active_frame[-1]]).grid(row=1, column=1, sticky="nswe")
                    active_frame.pop(0)
            except Exception:
                print(f"Error in frame_hanler: {Exception}")
                break
    
    def load_all_frames(self, reset_frames=False):
        global active_frame
        if reset_frames:
            for i in self.all_frames:
                with contextlib.suppress(Exception):
                    i.grid_forget()
        self.all_frames = {}
        nav_buttons = []
        all_nav_frames = dict([(name, cls) for name, cls in nav_frames.__dict__.items() if isinstance(cls, type)])
        for frame_name in list(all_nav_frames.keys()):
            self.all_frames[frame_name] = all_nav_frames[frame_name](launcher_settings, self.frame_top)
            nav_buttons.append((self.all_frames[frame_name].frame_description["button_text"], frame_name))
        #self.all_frames["dashboard"] = Dashboard
        #self.all_frames["settings"] = Settings(self.frame_top)
        #self.all_frames["run_bot_test"] = Run_Bot_Test(self.frame_top)
        self.nav_bar = Navigation_Bar(nav_buttons ,master=self.frame_bottom).grid(row=1, column=1, sticky="nswe")
        #if list_of_scripts != {}:
            #for i in list(list_of_scripts.keys()):
                #self.all_frames[i] = Creator(self.frame_right, header_name="RightMenu", fg_color="gray30", script_id=i)#.grid(row=1, column=0, sticky="nswe")
        active_frame = ["dashboard"]#wie queue designen (einfach immer neue namen appenden)
    
    def initial_load_save(self, path):
        global launcher_settings, savefile_path
        savefile_path = path
        try:
            all_vars = self.load_from_save()
            launcher_settings = all_vars["launcher_settings"]
        except Exception:
            all_vars = {"launcher_settings":{"fonts":{"usual_font":"Lucida Sans Unicode", "usual_font_size":14, "big_font_size":18}}}
            launcher_settings = all_vars["launcher_settings"]
            self.dump_into_save()
            print("New savefile generated")
    
    def load_from_save(self):
        with open(savefile_path, "r") as openfile:
            json_object = json.load(openfile)
        print("Loaded from file")
        return json_object

    def dump_into_save(self):
        all_vars = {"launcher_settings":launcher_settings}
        with open(savefile_path, "w") as outfile:
            json.dump(all_vars, outfile)
        print("Saved to file")
    

class Navigation_Bar(customtkinter.CTkFrame):
    def __init__(self, new_buttons: list = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if new_buttons is None:
            self.new_buttons = [("Bot", "run_bot_test"), ("Dashboard","dashboard"), ("Settings","settings")]
        else:
            self.new_buttons = new_buttons
        self.configure(bg_color="yellow", fg_color="yellow")
        self.init_main_frame_and_weights()
        self.create_buttons(self.new_buttons)
    
    def init_main_frame_and_weights(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.child_nav_frame = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.child_nav_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
        self.child_nav_frame.grid_columnconfigure(0, weight=0)
        self.child_nav_frame.grid_columnconfigure(tuple(range(1, len(self.new_buttons) + 1)), weight=1)
        self.child_nav_frame.grid_rowconfigure(0, weight=0)
        self.child_nav_frame.grid_rowconfigure(1, weight=1)
    
    def create_buttons(self, button_list: list):##maybe buttons in dict
        for button_num in range(len(button_list)):
            self.create_nav_button(
                            button_list[button_num][0],
                            button_list[button_num][1]
                ).grid(row=1, column=(button_num + 1), pady=0, padx=0, sticky="nsew")
    
    def create_nav_button(self, text, frame_name):
        return customtkinter.CTkButton(master=self.child_nav_frame,
                                            text=text,
                                            anchor=tkinter.CENTER,
                                            command=lambda: self.change_frame(frame_name),
                                            font=((launcher_settings["fonts"]["usual_font"]), (launcher_settings["fonts"]["usual_font_size"]))
                                            ) 
    
    def change_frame(self, frame_name):
        global active_frame
        active_frame.append(frame_name)


async def main(debug=False):
    if debug:
        window = mc_cord_GUI(asyncio.get_event_loop()).frame_handler()
        await window
    else:
        with contextlib.suppress(Exception):
            window = mc_cord_GUI(asyncio.get_event_loop()).frame_handler()
            await window
       

if __name__ == "__main__":
    asyncio.run(main(debug=True))