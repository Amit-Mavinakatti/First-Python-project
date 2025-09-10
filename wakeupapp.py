import random
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar 
from kivy.uix.image import Image
from kivy.uix.colorpicker import ColorPicker
import json
import os
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from datetime import datetime, timedelta
import json
KV = """
MDScreenManager:
    WelcomeScreen:
    LoginScreen:
    SignupScreen:
    HomeScreen:
    ProfileScreen:
    FactScreen:
    AboutScreen:
    ContactScreen:
    AchievementsScreen:

<WelcomeScreen>:
    name: "welcome"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Welcome to FACTory!"
            halign: "center"
            font_style: "H3"
            theme_text_color: "Primary"

        MDLabel:
            text: "Discover interesting facts on Science, AI, Physics, Space, Technology, and more."
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: "40dp"

        MDRaisedButton:
            text: "Let's Explore APP"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("login")
            
        MDLabel:
            text: "Designed and Developed By : Mr. AMIT M D"
            pos_hint: {"center_x": 0.5}
            font_style: "Overline"
            color: 0, 0, 0, 0.5

<LoginScreen>:
    name: "login"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Login"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: login_mobile_input
            hint_text: "Enter your mobile number"
            mode: "rectangle"
            input_filter: 'int'

        MDTextField:
            id: login_password_input
            hint_text: "Enter your password"
            password: True
            mode: "rectangle"

        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5}
            on_release: app.login_user(login_mobile_input.text, login_password_input.text)

        MDRaisedButton:
            text: "Sign Up"
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("signup")

<SignupScreen>:
    name: "signup"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Sign Up"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: signup_mobile_input
            hint_text: "Enter your mobile number"
            mode: "rectangle"
            input_filter: 'int'

        MDTextField:
            id: signup_password_input
            hint_text: "Create a password"
            password: True
            mode: "rectangle"

        MDRaisedButton:
            text: "Sign Up"
            pos_hint: {"center_x": 0.5}
            on_release: app.signup_user(signup_mobile_input.text, signup_password_input.text)

        MDRaisedButton:
            text: "Back to Login"
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("login")

<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "FACTory"
            pos_hint: {"top": 1}
            right_action_items: [["theme-light-dark", lambda x: app.toggle_theme()], ["account-circle", lambda x: app.change_screen('profile')]]

        MDTextField:
            id: search_input
            hint_text: "Search Facts"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
            on_text: app.search_facts(self.text)

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height

                MDRaisedButton:
                    text: "Start"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.change_screen('fact')

                MDRaisedButton:
                    text: "Customize Theme Color"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.open_color_picker()

                MDRaisedButton:
                    text: "App Info"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.change_screen('about')

                MDRaisedButton:
                    text: "Contact Support"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.change_screen('contact')
                
                MDRaisedButton:
                    text: "View Achievements"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.change_screen('achievements')

                 
                MDRaisedButton:
                    text: "Rate Us"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.show_thank_you_dialog()

                MDRaisedButton:
                    text: "Clear All Facts"
                    size_hint_x: 0.8
                    pos_hint: {"center_x": 0.5}
                    on_release: app.clear_facts()

                MDLabel:
                    text: "Developed By: Mr. AMIT M D"
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 1
                    bold:True 
                
                MDLabel:
                    text: "> For more info :"
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                MDLabel:
                    text: " ~~ Contact: 9353912665"
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                MDLabel:
                    text: " ~~ Email : amitmavinakatti1@gmail.com"
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                MDLabel:
                    text: " ~~ Whatsapp : 9353912665 "
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                MDLabel:
                    text: " ~~ Follow me at : www.instagram.com/a_m_i_t_m__08 "
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                MDLabel:
                    text: "> CopyRight 2025 "
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                MDLabel:
                    text: "> All Rights Reserved "
                    pos_hint: {"right":1,"bottom":0}
                    font_style: "Overline"
                    color: 0, 0, 0, 0.5
                    bold:False

                


<ProfileScreen>:
    name: "profile"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDTopAppBar:
            title: "Profile"
            elevation: 4
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]

        MDLabel:
            text: "PLEASE ENTER YOUR DETAILS:"
            halign: "center"
            size_hint_y: None 
            height: "40dp"

        MDTextField:
            id: name_input
            hint_text: "Enter your name"
            mode: "rectangle"
            size_hint_y: None
            height: "40dp"
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: mobile_input
            hint_text: "Enter your mobile number"
            mode: "rectangle"
            size_hint_y: None
            height: "40dp"
            input_filter: 'int'  # To allow only numbers
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: email_input
            hint_text: "Enter your email"
            mode: "rectangle"
            size_hint_y: None
            height: "40dp"
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Save"
            size_hint_y: None
            height: "50dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.save_profile(name_input.text, mobile_input.text, email_input.text)




<FactScreen>:
    name: "fact"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)

        MDTopAppBar:
            title: "Random Fact"
            pos_hint: {"top": 1}
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]

        MDTextField:
            id: search_input
            hint_text: "Search Facts"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
            on_text: app.search_facts(self.text)


        MDLabel:
            id: fact_label
            text: "Please press New Fact to Start"
            halign: "center"
            font_style: "H6"

        MDRaisedButton:
            text: "New Fact"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5}
            on_release: app.show_fact()

<AboutScreen>:
    name: "about"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDTopAppBar:
            title: "About FACTory!"
            pos_hint: {"top": 1}
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]

        MDLabel:
            text: "FACTory is an app that shares quick, random facts in fields such as SCIENCE, AI, PHYSICS, SPACE, TECHNOLOGY, etc."
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "It helps users to develop knowledge and curiosity."
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "Created by AMIT M D [Using: Python, Kivy, and Visual Studio Code]"
            halign: "center"
            font_style: "H4"
            bold: True
            theme_text_color: "Primary"

<ContactScreen>:
    name: "contact"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDTopAppBar:
            title: "Contact Support"
            pos_hint: {"top": 1}
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]

        MDLabel:
            text: "Creator: AMIT"
            halign: "center"
            font_style: "H4"
            bold: True

        MDLabel:
            text: "Mobile: 9353912665"
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "Email: amitmavinakatti1@gmail.com"
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "Instagram: instagram.com/a_m_i_t_m__08"
            halign: "center"
            font_style: "H5"

        MDLabel:
            text: "WhatsApp: 9353912665"
            halign: "center"
            font_style: "H5"
        
<AchievementsScreen>:
    name: "achievements"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDTopAppBar:
            title: "Achievements"
            left_action_items: [["arrow-left", lambda x: app.change_screen('home')]]

        MDLabel:
            text: "Achievements"
            halign: "center"
            font_style: "H4"

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                # Display achievement badges here
                MDLabel:
                    text: "Milestone 1: Read 10 Facts"
                    theme_text_color: "Secondary"

                
                MDLabel:
                    text: "Badge: Science Enthusiast"
                    theme_text_color: "Secondary"
"""
class WelcomeScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class SignupScreen(MDScreen):
    pass


class HomeScreen(MDScreen):
    pass


class ProfileScreen(MDScreen):
    pass


class FactScreen(MDScreen):
    pass


class AboutScreen(MDScreen):
    pass


class ContactScreen(MDScreen):
    pass

class AchievementsScreen(MDScreen):
    pass


class WakeUpApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.facts = []
        self.shuffled_facts = []
        self.users = {}
        self.achievements = {}  # Add a dictionary to store achievements

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"
        self.load_facts()
        self.load_users()
        self.load_achievements()  # Load achievements for user
        
        root_widget = Builder.load_string(KV)
        self.root = root_widget
        self.change_screen("welcome")
        return self.root

    def load_facts(self):
        """Loads facts from facts.txt, shuffles them, and resets the list when needed."""
        try:
            with open("facts.txt", "r", encoding="utf-8") as file:
                self.facts = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            self.facts = ["No facts found! Please add a facts.txt file."]
        self.reset_fact_list()

    def reset_fact_list(self):
        """Shuffles facts and resets tracking to avoid immediate repetition."""
        self.shuffled_facts = random.sample(self.facts, len(self.facts))

    def toggle_theme(self):
        """Toggles between Light and Dark theme."""
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

    def change_screen(self, screen_name):
        self.root.current = screen_name

    def show_fact(self):
        """Displays a random fact without immediate repetition."""
        if not self.shuffled_facts:
            self.reset_fact_list()

        fact_label = self.root.get_screen('fact').ids.fact_label
        fact_label.text = self.shuffled_facts.pop()

        # Check achievements after showing a new fact
        user = "test_user"  # Replace with actual logged-in user
        self.check_achievements(user)

    def show_thank_you_dialog(self):
        """Displays a thank-you dialog when the 'Rate Us' button is pressed."""
        dialog = MDDialog(
            title="Thank You!",
            text="Thanks for using the app. Please rate us on the Play Store!(Press Black screen to navigate.)",
            size_hint=(0.8, 1)
        )
        dialog.open()

    def clear_facts(self):
        """Clears all facts and resets the list."""
        self.reset_fact_list()
        fact_label = self.root.get_screen('fact').ids.fact_label
        fact_label.text = "All facts cleared!"

    def save_profile(self, name, mobile, email):
        """Saves the profile data."""
        print(f"Name: {name}, Mobile: {mobile}, Email: {email}")
        # Example: Save to a file
        with open("profile_data.txt", "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Mobile: {mobile}\n")
            file.write(f"Email: {email}\n")

        Snackbar(text="Thank you! Your response has been saved.").open()

    def open_color_picker(self):
        """Opens the Kivy ColorPicker to change the theme's primary color."""
        color_picker = ColorPicker()
        color_picker.bind(color=self.on_color_selected)

        dialog = MDDialog(
            title="Select Primary Color",
            type="custom",
            content_cls=color_picker,  # Use content_cls instead of content
            size_hint=(0.8, 0.8)
        )
        dialog.open()

    def on_color_selected(self, instance, color):
        """Sets the selected color as the app's primary color."""
        r, g, b, _ = color  # Extract RGB values
        self.theme_cls.primary_palette = self.rgb_to_palette(r, g, b)

    def rgb_to_palette(self, r, g, b):
        """Convert RGB values to a close color palette."""
        if r > 0.7 and g > 0.7 and b > 0.7:
            return "Light"
        elif r > 0.5:
            return "Red"
        elif g > 0.5:
            return "Green"
        elif b > 0.5:
            return "Blue"
        return "Cyan"

    def search_facts(self, search_query):
        """Filter the facts based on the search query."""
        filtered_facts = [fact for fact in self.facts if search_query.lower() in fact.lower()]

        # Update the fact display to show filtered facts
        if filtered_facts:
            self.shuffled_facts = filtered_facts
            self.show_fact()  # Show the first filtered fact
        else:
            self.shuffled_facts = self.facts  # Reset if no results
            Snackbar(text="No matching facts found.").open()

    def display_facts(self, facts_list):
        """Displays the list of facts."""
        fact_list_layout = self.root.get_screen('fact').ids.fact_list_layout
        fact_list_layout.clear_widgets()

        for fact in facts_list:
            fact_label = MDLabel(
                text=fact,
                theme_text_color="Secondary",
                size_hint_y=None,
                height=dp(40)
            )
            fact_list_layout.add_widget(fact_label)

    def load_users(self):
        """Load user data from a JSON file."""
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def save_users(self):
        """Save user data to a JSON file."""
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def signup_user(self, mobile, password):
        """Sign up new users."""
        if mobile in self.users:
            Snackbar(text="User already exists. Please login.").open()
        else:
            self.users[mobile] = password
            self.save_users()
            Snackbar(text="Sign up successful! Please log in.").open()
            self.change_screen("login")

    def login_user(self, mobile, password):
        """Login existing users."""
        if self.users.get(mobile) == password:
            self.change_screen("home")
        else:
            Snackbar(text="Invalid credentials. Please try again.").open()

    def check_first_time_user(self):
        """Check if the user is logging in for the first time."""
        if not self.users:
            self.change_screen("signup")
        else:
            self.change_screen("login")
    
    def load_achievements(self):
        """Load achievements from a JSON file."""
        try:
            with open("achievements.json", "r") as file:
                self.achievements = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.achievements = {}

    def save_achievements(self):
        """Save achievements to a JSON file."""
        with open("achievements.json", "w") as file:
            json.dump(self.achievements, file)

    def unlock_achievement(self, user, achievement):
        """Unlock a new achievement for the user."""
        if user not in self.achievements:
            self.achievements[user] = []

        if achievement not in self.achievements[user]:
            self.achievements[user].append(achievement)
            self.save_achievements()  # Save achievements to file

            Snackbar(text=f"Achievement Unlocked: {achievement}").open()

    def check_achievements(self, user):
        """Check and unlock achievements based on user actions."""
        if user not in self.achievements:
            self.achievements[user] = []

        # Example conditions to unlock achievements
        fact_count = len(self.facts)
        if fact_count >= 10 and "Read 10 Facts" not in self.achievements[user]:
            self.unlock_achievement(user, "Read 10 Facts")

        # Add other achievements based on your app's criteria
        # E.g., "Read 50 Facts", "Logged in for 7 days", etc.

    def show_achievements(self):
        """Display the user's achievements in the Achievements Screen."""
        user = "test_user"  # For example, this can be dynamically determined based on logged-in user
        self.check_achievements(user)

        achievements = self.achievements.get(user, [])
        achievement_screen = self.root.get_screen("achievements")
        achievement_screen.clear_widgets()

        for achievement in achievements:
            achievement_screen.add_widget(
                MDLabel(
                    text=f"Achievement: {achievement}",
                    theme_text_color="Secondary",
                    size_hint_y=None,
                    height=dp(40)
                )
            )

if __name__ == "__main__":
    WakeUpApp().run()
