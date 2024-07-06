import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import random
from PIL import Image, ImageTk

# Function to get current season
def get_season():
    month = datetime.now().month
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4]:
        return "Spring"
    elif month in [5]:
        return "Summer"
    else:
        return "Autumn"

# Health tips dictionary
health_tips = {
    "Winter": [
        "Stay hydrated by drinking plenty of water.",
        'Use a humidifier to keep indoor air moist.',
       ' Eat immune-boosting foods like citrus fruits and leafy greens.',
        'Dress in layers to stay warm.',
        'Moisturize your skin regularly to prevent dryness.',
       ' Take vitamin D supplements if you are not getting enough sunlight.',
        'Wash your hands frequently to avoid catching colds and flu.',
        'Exercise indoors to stay active.',
        'Get a flu shot.',
        'Stay active with winter sports like skiing or snowshoeing.',
        'Use a scarf to cover your nose and mouth in very cold weather.',
       ' Keep your home warm but not too hot.',
       ' Drink herbal teas to stay warm and hydrated.',
        'Get enough sleep to boost your immune system.',
        'Avoid close contact with sick people.',
        'Eat plenty of fiber to keep your digestive system healthy.',
        'Take breaks from screen time to avoid eye strain.',
        'Keep your feet warm and dry to prevent frostbite.',
        'Stay social to ward off winter blues.',
        'Practice good respiratory hygiene.',
        'Avoid alcohol as it can lower your body temperature.',
        'Stretch regularly to stay flexible.',
       ' Take warm baths to relax muscles and relieve stress.',
        'Use hand cream to prevent chapped hands.',
        'Protect your lips with a good lip balm.',
       ' Avoid heavy, greasy foods.',
        'Stay positive and practice mindfulness.',
       ' Keep your windows slightly open to let fresh air in.',
        'Eat seasonal vegetables like root vegetables and squashes.',
        'Don’t skip meals to keep your energy levels up.',
       ' Wear a hat to keep your head warm.',
        'Drink bone broth for added nutrients.',
       ' Avoid smoking and secondhand smoke.',
       ' Keep your throat and nose clear with saline sprays.',
        'Eat probiotic-rich foods to maintain gut health.',
        'Stay active with indoor fitness classes.',
        'Avoid sugary snacks that can lower your immunity.',
       'Take care of your mental health with meditation or yoga.',
        'Use essential oils like eucalyptus or peppermint.',
        'Stay hydrated with soups and broths.',
        'Keep your home clean to avoid germs.',
        'Avoid touching your face to prevent the spread of germs.',
        'Stay connected with friends and family.',

        'Use natural light to boost your mood.',

       'Take care of your feet by wearing warm, dry socks.',

        'Eat plenty of protein to maintain muscle mass.',

        'Wear sunglasses to protect your eyes from glare.',

       ' Practice deep breathing exercises.',

       " Keep your stress levels low.",

        'Stay informed about weather conditions.'
    ],
    "Spring": [
        " Stay hydrated by drinking plenty of water.",
        'Eat fresh, seasonal fruits and vegetables.',
        'Get outside to enjoy the sunlight and boost vitamin D.',
        'Stay active with outdoor activities like walking or biking.',
        'Practice good hand hygiene to avoid spring colds.',
        'Use allergy medications if you suffer from hay fever.',
        'Eat immune-boosting foods like berries and leafy greens.',
        'Stay active with spring sports like tennis or golf.',
        'Get enough sleep to support your immune system.',
        'Moisturize your skin to prevent dryness.',
        'Drink herbal teas to stay hydrated.',
        'Keep your home well-ventilated.',
        'Wear layers to adapt to changing temperatures.',
        'Take vitamin supplements if needed.',
        'Eat plenty of fiber-rich foods.',
        'Avoid excessive alcohol consumption.',
       'Stretch regularly to stay flexible.',
        'Take breaks from screen time to avoid eye strain.',
        'Stay social to avoid seasonal blues.',
        'Practice good respiratory hygiene.',
        'Avoid sugary snacks.',
        'Stay positive and practice mindfulness.',
        'Keep your windows open to let fresh air in.',
        'Eat a variety of colorful vegetables.',
        'Do nott skip meals to maintain energy levels.',
        'Wear sunscreen to protect your skin from UV rays.',
        'Drink plenty of water to stay hydrated.',
        'Use insect repellent to avoid bug bites.',
        'Eat probiotic-rich foods for gut health.',
        'Stay active with outdoor fitness classes.',
        'Avoid heavy, greasy foods.',
        'Take care of your mental health with meditation or yoga.',
        'Use essential oils like lavender or chamomile.',
        'Stay hydrated with soups and broths.',
        'Keep your home clean to avoid germs.',
        'Avoid touching your face to prevent the spread of germs.',
        'Stay connected with friends and family.',
        'Use natural light to boost your mood.',
        'Take care of your feet with comfortable shoes.',
        'Eat plenty of protein to maintain muscle mass.'

    ],
    "Summer": [
        "Stay hydrated by drinking plenty of water.",
        'Wear sunscreen to protect your skin from UV rays.',
        'Eat light, hydrating foods like fruits and vegetables.',
        'Exercise early in the morning or late in the evening to avoid heat.',
        'Wear loose, breathable clothing.',
        'Avoid caffeinated and alcoholic beverages.',
        'Take cool showers to lower your body temperature.',
        'Stay in the shade whenever possible.',
        'Use a hat and sunglasses to protect your face and eyes.',
        'Keep your home cool with fans or air conditioning.',
        'Avoid heavy meals that can make you feel sluggish.',
        'Stay active with water sports like swimming.',
        'Use insect repellent to avoid bug bites.',
        'Take breaks in air-conditioned places.',
        'Eat small, frequent meals to stay energized.',
        'Stay informed about heat advisories.',
        'Use aloe vera to soothe sunburns.',
        'Practice good hygiene to avoid infections.',
        'Stay cool with cold compresses.',
        'Avoid sugary drinks that can dehydrate you.',
        'Keep your skin moisturized.',
        'Avoid prolonged exposure to the sun.',
        'Use fans to circulate air in your home.',
       'Wear UV-protective clothing.',
        'Keep your windows closed during the hottest part of the day.',
        'Stay cool with frozen treats like ice pops.',
        'Drink electrolyte-rich beverages if you are sweating a lot.',
       ' Use a wide-brimmed hat for extra sun protection.',
        'Eat foods rich in antioxidants like berries.',
        'Keep your feet cool with sandals or open shoes.',
        'Stay active with early morning yoga or stretching.',
        'Use cooling towels during workouts.',
        'Avoid strenuous activities during peak heat hours.',
        'Stay hydrated with coconut water.',
        'Use a cooling pillow or mattress pad at night.',
        'Eat hydrating snacks like cucumber or watermelon.',
        'Wear light-colored clothing to reflect heat.',
        'Take cool breaks if you are working outside.',
        'Stay connected with friends to avoid isolation.',
        'Use natural insect repellents like citronella.',
        'Avoid hot, heavy foods.',
        'Keep your home ventilated.',
        'Use after-sun lotions if you have been in the sun.',
        'Stay positive and enjoy outdoor activities.',
        'Avoid leaving pets or children in hot cars.',
        'Eat plenty of fiber to stay regular.',
        'Stay active with light, low-impact exercises.',
        'Use sunscreen with high SPF.',
        'Keep your stress levels low.',
        'Stay informed about weather conditions.'

    ],
    "Autumn": [
        "Stay hydrated by drinking plenty of water.",
         'Eat seasonal fruits and vegetables like pumpkins and apples.',
        'Dress in layers to adapt to changing temperatures.',
        'Stay active with outdoor activities like hiking.',
        'Use a humidifier to keep indoor air moist.. Take vitamin D supplements as sunlight decreases.',
        'Eat immune-boosting foods like garlic and ginger.',
        'Practice good hand hygiene to avoid colds.',
        'Get a flu shot.',
       ' Moisturize your skin to prevent dryness.',
       ' Drink herbal teas to stay warm and hydrated.. Stay active with fall sports like football or soccer.',
        'Use a scarf to protect your throat from chilly winds.',
        'Keep your home warm but well-ventilated.',
        'Get enough sleep to support your immune system.',
        'Avoid close contact with sick people.',
        'Eat plenty of fiber-rich foods.',
        'Take breaks from screen time to avoid eye strain.',
        'Keep your feet warm and dry.',
        'Stay social to avoid seasonal blues.',
        'Practice good respiratory hygiene.',
        'Avoid excessive alcohol consumption.',
        'Stretch regularly to stay flexible.',
        'Take warm baths to relax muscles and relieve stress.',
        'Use hand cream to prevent chapped hands.',
        'Avoid heavy, greasy foods.',
        'Stay positive and practice mindfulness.',
        'Keep your windows slightly open to let fresh air in.',
        'Eat root vegetables and squashes.',
        'Don’t skip meals to maintain energy levels.',
        'Wear a hat to keep your head warm.',
        'Drink bone broth for added nutrients.',
        'Avoid smoking and secondhand smoke.',
        'Keep your throat and nose clear with saline sprays.',
        'Eat probiotic-rich foods for gut health.',
        'Stay active with indoor fitness classes.',
        'Avoid sugary snacks.',
        'Take care of your mental health with meditation or yoga.',
        'Use essential oils like eucalyptus or peppermint.',
        'Stay hydrated with soups and broths.',
        'Keep your home clean to avoid germs.',
        'Avoid touching your face to prevent the spread of germs.',
        'Stay connected with friends and family.',
        'Use natural light to boost your mood.',
        'Take care of your feet with warm, dry socks.'
        'Eat plenty of protein to maintain muscle mass.',
        'Wear sunglasses to protect your eyes from glare.',
        'Practice deep breathing exercises.',
        'Keep your stress levels low.',
        'Stay informed about weather conditions.'

    ]
}

# Function to display health tip in a new window
def display_health_tip():
    season = get_season()
    tip = random.choice(health_tips[season])
    
    # Create a new top-level window for displaying the health tip
    tip_window = tk.Toplevel()
    tip_window.title("Health Tip")
    tip_window.geometry("400x200")
    tip_window.configure(bg="#E0D9FF")
    
    # Create and place the tip display label
    tip_label = ttk.Label(tip_window, text=tip, font=("Helvetica", 14), wraplength=380, justify="center", background="#E0D9FF")
    tip_label.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("Seasonal Health Tip Generator")
root.geometry("600x400")

# Load background image
bg_image = Image.open(r"C:\\Users\\shraddha hebbar\\OneDrive\\Desktop\\Frontend_mini_project\\images\\health.jpg")
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#F5F5DC")  # Label style
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#FFA07A", foreground="#00008B")  # Button style

# Create and place the title label
title_label = ttk.Label(root, text="Seasonal Health Tip Generator", font=("Helvetica", 24, "bold"), background="#F5F5DC")
title_label.pack(pady=20)

# Create and place the tagline label
tagline_label = ttk.Label(root, text="Find your rhythm every season", font=("Helvetica", 16, "italic"), background="#F5F5DC", foreground="#8B0000")
tagline_label.pack(pady=5)

# Create and place the tip display label
tip_display_label = ttk.Label(root, text="Click the button below to generate a health tip.", background="#F5F5DC")
tip_display_label.pack(pady=20)

# Create and place the generate button with a highlighted style
generate_button = ttk.Button(root, text="Generate Health Tip", command=display_health_tip, style="TButton")
generate_button.pack(pady=20)

# Add footer with season display
season = get_season()
footer_label = ttk.Label(root, text=f"Current Season: {season}", font=("Helvetica", 12), background="#F5F5DC")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the main event loop
root.mainloop()
