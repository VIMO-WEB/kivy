from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: "20dp"
    spacing: "20dp"
    
    MDTextField:
        id: phone_input
        hint_text: "Enter Phone Number"
        size_hint_x: None
        width: "280dp"
        pos_hint: {"center_x": 0.5}
        mode: "rectangle"
        multiline: False

    MDRaisedButton:
        text: "Get Phone Details"
        size_hint: None, None
        width: "200dp"
        pos_hint: {"center_x": 0.5}
        on_release: app.get_phone_details()

    MDCard:
        size_hint: None, None
        size: "280dp", "200dp"
        pos_hint: {"center_x": 0.5}
        padding: "10dp"
        spacing: "10dp"
        elevation: 10
        orientation: 'vertical'
        id: phone_details_card

        MDLabel:
            id: country_label
            theme_text_color: "Secondary"
            halign: "center"
        
        MDLabel:
            id: carrier_label
            theme_text_color: "Secondary"
            halign: "center"
        
        MDLabel:
            id: timezone_label
            theme_text_color: "Secondary"
            halign: "center"

    MDRaisedButton:
        text: "Check Another"
        size_hint: None, None
        width: "200dp"
        pos_hint: {"center_x": 0.5}
        on_release: app.clear_input()
'''

class PhoneDetailApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def get_phone_details(self):
        phone_number = self.root.ids.phone_input.text
        try:
            parsed_number = phonenumbers.parse(phone_number)
            country = geocoder.description_for_number(parsed_number, "en")
            phone_carrier = carrier.name_for_number(parsed_number, "en")
            timezones = timezone.time_zones_for_number(parsed_number)
            
            # Displaying the details in the card
            self.root.ids.country_label.text = f"Country: {country}"
            self.root.ids.carrier_label.text = f"Carrier: {phone_carrier}"
            self.root.ids.timezone_label.text = f"Timezone: {', '.join(timezones)}"
        
        except phonenumbers.phonenumberutil.NumberParseException:
            self.root.ids.country_label.text = "Invalid Phone Number"
            self.root.ids.carrier_label.text = ""
            self.root.ids.timezone_label.text = ""
    
    def clear_input(self):
        # Reset the input and output fields
        self.root.ids.phone_input.text = ""
        self.root.ids.country_label.text = ""
        self.root.ids.carrier_label.text = ""
        self.root.ids.timezone_label.text = ""

PhoneDetailApp().run()
