import customtkinter
import tkinter

class nav_frames:
    class settings(customtkinter.CTkFrame):
        def __init__(self, launcher_settings: dict = None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.description()
            if launcher_settings is None:
                launcher_settings = {
                        "fonts": {
                            "usual_font": "Lucida Sans Unicode",
                            "usual_font_size": 14,
                            "big_font_size": 18,
                        }
                    }
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.options_frame = customtkinter.CTkFrame(master=self, fg_color="gray30", corner_radius=10, bg_color="gray30")
            self.options_frame.grid(row=0, column=0, sticky="nsew", padx=3, pady=3)
            self.options_frame.grid_columnconfigure(0, weight=5)
            self.options_frame.grid_rowconfigure(0, weight=5)
            self.combo_label_1 = customtkinter.CTkLabel(master=self.options_frame,
                                                text="Settings",
                                                anchor=tkinter.CENTER,
                                                font=((launcher_settings["fonts"]["usual_font"]), (launcher_settings["fonts"]["usual_font_size"]))
                                                )  # font name and size in px
            self.combo_label_1.grid(row=0, column=0, pady=3, padx=10, sticky="nsew")
        
        def description(self):
            self.frame_description = {"button_text":"Settings"}

    class dashboard(customtkinter.CTkFrame):
        def __init__(self, launcher_settings: dict = None, *args, **kwargs):#
            super().__init__(*args, **kwargs)
            self.description()
            if launcher_settings is None:
                launcher_settings = {
                        "fonts": {
                            "usual_font": "Lucida Sans Unicode",
                            "usual_font_size": 14,
                            "big_font_size": 18,
                        }
                    }
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.child_dashboard_frame = customtkinter.CTkFrame(master=self, corner_radius=10)
            self.child_dashboard_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
            self.child_dashboard_frame.grid_columnconfigure(0, weight=5)
            self.child_dashboard_frame.grid_rowconfigure(0, weight=5)
            self.combo_label_1 = customtkinter.CTkLabel(master=self.child_dashboard_frame,
                                                text="Dashboard",
                                                anchor=tkinter.CENTER,
                                                font=((launcher_settings["fonts"]["usual_font"]), (launcher_settings["fonts"]["usual_font_size"]))
                                                )  # font name and size in px
            self.combo_label_1.grid(row=0, column=0, pady=0, padx=0, sticky="nsew")
        
        def description(self):
            self.frame_description = {"button_text":"Dashboard"}


    class run_bot_test(customtkinter.CTkFrame):
        def __init__(self, launcher_settings: dict = None, *args, **kwargs):#, launcher_settings: dict = None
            super().__init__(*args, **kwargs)
            self.description()
            if launcher_settings is None:
                launcher_settings = {
                        "fonts": {
                            "usual_font": "Lucida Sans Unicode",
                            "usual_font_size": 14,
                            "big_font_size": 18,
                        }
                    }
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.child_bot_frame = customtkinter.CTkFrame(master=self, corner_radius=10)
            self.child_bot_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
            self.child_bot_frame.grid_columnconfigure(0, weight=5)
            self.child_bot_frame.grid_rowconfigure(0, weight=5)
            self.combo_label_1 = customtkinter.CTkButton(master=self.child_bot_frame,
                                                text="Run Bot",
                                                anchor=tkinter.CENTER,
                                                command=lambda: self.loop.create_task(self.bot_test()),
                                                font=((launcher_settings["fonts"]["usual_font"]), (launcher_settings["fonts"]["usual_font_size"]))
                                                )  # font name and size in px
            self.combo_label_1.grid(row=0, column=0, pady=0, padx=0, sticky="nsew")
        
        def description(self):
            self.frame_description = {"button_text":"Bot Test"}
        
        async def bot_test(self):
            pass