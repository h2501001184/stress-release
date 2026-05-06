"""Cognitive Behavioral Therapy tools and cognitive distortion definitions."""

COGNITIVE_DISTORTIONS = {
    "All-or-Nothing Thinking": {
        "description": "Seeing things in black-and-white categories. If something is not perfect, it's a total failure.",
        "example": "If I don't get an A, I'm completely stupid.",
        "reframe": "I didn't get the grade I wanted, but that doesn't mean I'm stupid. I can learn from this.",
        "icon": "⚫⚪"
    },
    "Overgeneralization": {
        "description": "Seeing a single negative event as a never-ending pattern of defeat.",
        "example": "I failed this interview, I'll never get a job.",
        "reframe": "This one interview didn't go well, but that doesn't predict all future interviews.",
        "icon": "🔄"
    },
    "Mental Filter": {
        "description": "Picking out a single negative detail and dwelling on it exclusively, ignoring all positive aspects.",
        "example": "The presentation went well, but I stumbled on one slide, so it was terrible.",
        "reframe": "I stumbled on one slide, but the rest of the presentation was strong and well-received.",
        "icon": "🔍"
    },
    "Disqualifying the Positive": {
        "description": "Rejecting positive experiences by insisting they 'don't count' for some reason.",
        "example": "They only said nice things because they felt sorry for me.",
        "reframe": "People are giving me genuine positive feedback. I can accept it.",
        "icon": "❌✅"
    },
    "Mind Reading": {
        "description": "Assuming you know what others are thinking, usually something negative about you.",
        "example": "They didn't reply to my text. They must be mad at me.",
        "reframe": "There could be many reasons they haven't replied. I don't know for sure.",
        "icon": "🧠"
    },
    "Fortune Telling": {
        "description": "Anticipating that things will turn out badly, and feeling convinced your prediction is fact.",
        "example": "I'm going to fail this exam, I just know it.",
        "reframe": "I can't predict the future. I can only prepare and do my best.",
        "icon": "🔮"
    },
    "Catastrophizing": {
        "description": "Blowing things out of proportion or imagining the worst possible outcome.",
        "example": "If I make a mistake at work, I'll get fired and lose everything.",
        "reframe": "Making a mistake is normal. It doesn't automatically lead to the worst outcome.",
        "icon": "🏔️"
    },
    "Emotional Reasoning": {
        "description": "Assuming that because you feel a certain way, what you think must be true.",
        "example": "I feel like a failure, so I must be one.",
        "reframe": "Feelings are not facts. I can feel like a failure and still be capable and worthy.",
        "icon": "💭"
    },
    "Should Statements": {
        "description": "Using 'should,' 'must,' or 'ought to' statements that create pressure and guilt.",
        "example": "I should be able to handle this without getting stressed.",
        "reframe": "It's okay to feel stressed. I'm human, and I'm doing my best.",
        "icon": "📋"
    },
    "Labeling": {
        "description": "Attaching a negative label to yourself or others instead of describing the behavior.",
        "example": "I'm such an idiot for forgetting that.",
        "reframe": "I forgot something. That doesn't make me an idiot — it makes me human.",
        "icon": "🏷️"
    },
    "Personalization": {
        "description": "Seeing yourself as the cause of some negative external event which you were not responsible for.",
        "example": "My friend is upset. It must be because of something I did.",
        "reframe": "My friend might be upset for reasons that have nothing to do with me.",
        "icon": "🎯"
    },
}

GROUNDING_TECHNIQUES = {
    "5-4-3-2-1 Senses": {
        "steps": [
            "👁️ **5 things you can SEE** — Look around and name 5 objects you can see right now.",
            "✋ **4 things you can TOUCH** — Feel 4 things around you (your clothes, the chair, the floor).",
            "👂 **3 things you can HEAR** — Listen for 3 sounds (birds, traffic, your breathing).",
            "👃 **2 things you can SMELL** — Notice 2 scents (coffee, fresh air, soap).",
            "👅 **1 thing you can TASTE** — Notice 1 taste in your mouth or take a sip of water."
        ],
        "description": "A powerful grounding technique that brings you back to the present moment through your senses."
    },
    "Box Breathing": {
        "steps": [
            "🫁 **Inhale** for 4 counts",
            "⏸️ **Hold** for 4 counts",
            "😮‍💨 **Exhale** for 4 counts",
            "⏸️ **Hold** for 4 counts",
            "🔁 Repeat for 4-5 cycles"
        ],
        "description": "Used by Navy SEALs to stay calm under pressure. Regulates the autonomic nervous system."
    },
    "Cold Water Reset": {
        "steps": [
            "🚰 Fill a bowl with cold water",
            "🧊 Add ice if available",
            "🙌 Submerge your face or hold ice in your hands",
            "⏱️ Hold for 30 seconds",
            "💙 Notice your heart rate slowing down"
        ],
        "description": "Activates the mammalian dive reflex, which rapidly calms the nervous system."
    },
    "Grounding Objects": {
        "steps": [
            "🪨 Find a small object (stone, key, coin)",
            "🔍 Observe its texture, weight, temperature",
            "👆 Trace its edges with your fingers",
            "🧠 Describe it in detail in your mind",
            "🌬️ Breathe slowly while holding it"
        ],
        "description": "Carry a grounding object with you. Touching it creates an anchor to the present moment."
    },
    "Category Game": {
        "steps": [
            "🎲 Pick a category (animals, cities, foods)",
            "📝 List as many items as you can in 60 seconds",
            "🔤 Try going through the alphabet (A-Z)",
            "🧩 Focus completely on the task",
            "✅ Notice your mind shifting away from anxiety"
        ],
        "description": "Occupies the thinking mind with a structured task, interrupting anxious thought loops."
    }
}

SLEEP_STORIES = [
    {
        "title": "The Starlight Garden",
        "preview": "Imagine a garden that only blooms under starlight...",
        "duration": "12 min",
        "full_text": """Close your eyes and imagine a garden that exists only under the light of the stars. This is no ordinary garden. The flowers here are made of soft, glowing light — gentle blues, silvers, and pale golds that pulse slowly like a calm heartbeat. You walk barefoot on a path of cool moss. With each step, tiny lights rise from the ground like fireflies, swirling around your ankles before drifting back down to rest. In the center of the garden stands an ancient willow tree. Its branches sway without wind, moving in rhythm with your breathing. As you inhale, they rise. As you exhale, they fall. You sit beneath the willow and lean against its trunk. It feels warm and solid, like the embrace of an old friend. Above you, the stars peek through the branches, twinkling in patterns that seem almost familiar, like a language you once knew. A small stream winds through the garden. The water doesn't rush — it glides, whispering secrets to the stones it passes. You can hear it if you listen closely: shhh... shhh... let go... let go... The air smells of jasmine and rain. Each breath you take fills you with a warmth that starts in your chest and spreads slowly to your fingertips, your toes, the top of your head. The flowers begin to dim, but not because they're fading. They're matching your rhythm, growing softer as you grow calmer. The garden is teaching you how to rest. You are safe here. You are held here. The stars have been watching over this garden for a thousand years, and they will watch over you tonight. Let your thoughts drift like the fireflies. Let them rise, glow for a moment, and then settle back into the soft moss. There is nothing you need to do right now. There is nowhere you need to be. The willow sways. The stream whispers. The stars watch. And you... you rest."""
    },
    {
        "title": "The Cloud Collector",
        "preview": "A gentle journey through skies of infinite softness...",
        "duration": "15 min",
        "full_text": """You are lying on a bed of clouds. Not falling through them — resting on them, as if they were the softest mattress ever made. The clouds hold you gently, cradling you like a hammock woven from moonlight and mist. Above you, the sky stretches forever in shades of twilight purple and deep blue. Other clouds drift past, each one unique. One looks like a sleeping cat. Another resembles a castle with tall, fluffy towers. A third seems to be a ship sailing to a dreamland just over the horizon. You reach out and touch a passing cloud. It doesn't burst or dissipate. Instead, it wraps around your hand like cool silk, then slowly releases you, continuing on its journey across the sky. The cloud beneath you begins to move, carrying you gently through the atmosphere. You pass through a soft rain shower — but the drops are warm and tingle lightly against your skin, washing away any tension you've been carrying. Below, you can see the world, but it's far away and unimportant right now. The lights of cities look like scattered stars. The oceans reflect the moon like sheets of dark glass. Everything seems peaceful from up here. A cloud shaped like a bird flies alongside you. It doesn't make a sound, but you can feel its presence — a companion on this gentle journey. The air is perfectly temperatured — neither warm nor cool, just comfortable. You realize you've stopped trying to hold yourself tense. Your shoulders have dropped. Your jaw has unclenched. Your hands rest open and relaxed. The clouds begin to glow softly with the first light of dawn, but it's a dawn that never fully arrives — it stays in that magical moment just before sunrise, when the world is full of possibility and peace. You can stay here as long as you like. The clouds will carry you. The sky will hold you. And sleep will find you when you're ready. Breathe in the cool, clean air. Breathe out everything else. The clouds have you now."""
    },
    {
        "title": "The Library of Dreams",
        "preview": "Wander through infinite shelves of stories waiting to be dreamed...",
        "duration": "10 min",
        "full_text": """You stand before enormous wooden doors carved with images of sleeping moons and resting stars. As you push them open, they make no sound — only a gentle rush of air that smells of old paper and vanilla. Inside is the Library of Dreams. The ceiling is so high it disappears into shadow. The shelves stretch in every direction, filled with books that glow softly in every color imaginable. Each book contains a dream. Some are adventures. Some are memories. Some are conversations you wish you'd had. Some are places you've never been but somehow remember. You walk down the central aisle. Your footsteps make no sound on the thick carpet. The carpet's pattern shifts as you walk — first showing waves, then forests, then constellations, then simple, soothing geometric shapes. A book on a low shelf catches your attention. Its cover is the color of a sunset reflected on calm water. You don't open it — you don't need to. Simply touching it fills you with a sense of completion, as if something inside you that was searching has finally found what it was looking for. You continue walking, running your fingers along the spines. Each one hums at a different frequency, and together they create a chord so perfect it could lull the world to sleep. At the end of the aisle, you find a reading nook — a window seat piled with pillows. Outside the window, a gentle snow falls upward, drifting into a sky of soft amber. You settle into the pillows. They're somehow exactly the right softness. The book you touched earlier has followed you, floating gently to rest on your lap. You don't need to read it. The dream inside knows how to find you. Close your eyes. The Library will keep your thoughts safe while you rest. The books will wait. The snow will fall. And you... you will drift."""
    }
]

GUIDED_MEDITATIONS = [
    {
        "title": "Commute Calm",
        "duration": 5,
        "description": "Transform your commute into a mindful journey.",
        "script": [
            "Sit comfortably and feel the seat beneath you. You are exactly where you need to be.",
            "Notice 3 sounds around you. Don't judge them — just observe them as passing events.",
            "Feel your hands on your lap or the steering wheel. Notice the temperature and texture.",
            "Take a deep breath in for 4 counts... hold for 4... exhale for 6.",
            "With each exhale, imagine tension leaving your shoulders and jaw.",
            "You are not rushing toward the future. You are traveling through the present.",
            "One more deep breath. Carry this calm with you as you continue your journey."
        ]
    },
    {
        "title": "Deep Work Focus",
        "duration": 10,
        "description": "Clear mental clutter before important tasks.",
        "script": [
            "Close your eyes and take 3 deep breaths. In through the nose, out through the mouth.",
            "Imagine your mind as a clear blue sky. Thoughts are clouds passing through.",
            "Acknowledge each thought: 'I see you, but I don't need to follow you right now.'",
            "Focus on the sensation of breathing. The cool air entering, the warm air leaving.",
            "Set an intention: 'For the next hour, I give myself permission to focus fully.'",
            "Feel your feet on the floor. You are grounded. You are capable.",
            "When ready, open your eyes and begin your work with clarity and calm."
        ]
    },
    {
        "title": "Walking Meditation",
        "duration": 15,
        "description": "Mindful movement for when sitting still feels impossible.",
        "script": [
            "Begin walking at a natural, comfortable pace.",
            "Notice the heel-to-toe roll of each foot. The shift of weight.",
            "Feel the air on your skin. Notice the temperature, the movement.",
            "With each step, silently say: 'Breathing in, I arrive. Breathing out, I am home.'",
            "When your mind wanders, gently return to the sensation of walking.",
            "You don't need to get anywhere. The walking itself is the destination.",
            "Continue for as long as feels right. There is no goal, only presence."
        ]
    },
    {
        "title": "Receiving Difficult News",
        "duration": 8,
        "description": "Ground yourself when facing challenging information.",
        "script": [
            "Place one hand on your heart and one on your belly. Feel your life force.",
            "Breathe deeply and slowly. Your body is processing. Give it time.",
            "Repeat silently: 'I can handle this. I have handled hard things before.'",
            "Notice where tension lives in your body. Send breath to that place.",
            "You don't need to solve anything right now. You only need to be present.",
            "Feel the support of the ground beneath you. You are not alone.",
            "When ready, release your hands. Carry this grounding with you."
        ]
    },
    {
        "title": "Body Scan Relaxation",
        "duration": 20,
        "description": "Systematic relaxation from head to toe.",
        "script": [
            "Lie down comfortably. Allow your body to feel heavy and supported.",
            "Bring attention to your toes. Notice any sensation. Breathe into them.",
            "Slowly move up through your feet, ankles, calves, knees, thighs.",
            "Continue to your hips, lower back, stomach, chest, shoulders.",
            "Move down your arms — upper arms, elbows, forearms, wrists, hands, fingers.",
            "Finally, your neck, jaw, face, forehead, scalp.",
            "Your entire body is now relaxed. Rest in this awareness for as long as you like."
        ]
    }
]

CRISIS_RESOURCES = [
    {"name": "988 Suicide & Crisis Lifeline", "phone": "988", "description": "24/7 free and confidential support"},
    {"name": "Crisis Text Line", "phone": "Text HOME to 741741", "description": "Text-based crisis support"},
    {"name": "SAMHSA National Helpline", "phone": "1-800-662-4357", "description": "Treatment referral and info"},
    {"name": "National Sexual Assault Hotline", "phone": "1-800-656-4673", "description": "Confidential support 24/7"},
    {"name": "Veterans Crisis Line", "phone": "988 then press 1", "description": "For veterans and their families"},
    {"name": "Trevor Project (LGBTQ+)", "phone": "1-866-488-7386", "description": "Crisis intervention for LGBTQ youth"},
]

GRATITUDE_PROMPTS = [
    "What made you smile today, even for a moment?",
    "Who is someone you're grateful to have in your life?",
    "What's something beautiful you noticed today?",
    "What challenge did you overcome recently?",
    "What's a simple pleasure you enjoyed today?",
    "What about your body are you grateful for right now?",
    "What's something you learned recently?",
    "What made you laugh today?",
    "What's a memory that always warms your heart?",
    "What opportunity do you have that others might not?",
    "What's something in nature you appreciated today?",
    "What skill or talent do you have that you're thankful for?",
    "What's a small win you had today?",
    "What comfort do you have access to right now?",
    "Who believed in you when you didn't believe in yourself?",
]

PANIC_FIRST_AID = {
    "Recognize": "You are having a panic attack. This is temporary. You are NOT dying. Your body is having a false alarm.",
    "Breathe": "Breathe in for 4 counts... hold for 4... out for 6. The out-breath activates your parasympathetic nervous system.",
    "Ground": "Name 5 things you see. 4 you can touch. 3 you hear. 2 you smell. 1 you taste.",
    "Accept": "Don't fight the panic. Accept the sensations. Fighting makes it worse. Let it wash over you like a wave.",
    "Remind": "This has happened before and you survived. This will pass. It ALWAYS passes. Usually within 10-20 minutes.",
    "After": "When it passes, be gentle with yourself. Rest. Drink water. You just survived something incredibly difficult.",
}

PROGRESSIVE_MUSCLE_RELAXATION = [
    ("Hands", "Clench your fists tightly for 5 seconds... now release and feel the warmth flow in."),
    ("Forearms", "Bend your hands back at the wrists, feeling tension... now let go completely."),
    ("Biceps", "Tense your biceps by making a muscle... hold... and release."),
    ("Shoulders", "Shrug your shoulders up to your ears... hold... and drop them down."),
    ("Forehead", "Raise your eyebrows as high as you can... hold... and relax."),
    ("Eyes", "Squint your eyes shut tightly... hold... and release."),
    ("Jaw", "Clench your jaw... hold... now let your mouth fall open slightly."),
    ("Neck", "Press your head back gently... hold... and release to neutral."),
    ("Chest", "Take a deep breath and hold it... hold... now exhale completely."),
    ("Stomach", "Tighten your stomach muscles... hold... and let them soften."),
    ("Lower Back", "Arch your back slightly... hold... and relax into the surface."),
    ("Thighs", "Tighten your thigh muscles... hold... and release."),
    ("Calves", "Point your toes toward your face... hold... and let go."),
    ("Feet", "Curl your toes under... hold... and release, feeling them spread."),
]

DAILY_CALM_PLANS = {
    "Monday": {
        "morning": {"activity": "5-Minute Mindful Breathing", "type": "breathwork", "duration": 5},
        "midday": {"activity": "Brain Dump - Clear Mental Clutter", "type": "cbt", "duration": 10},
        "evening": {"activity": "Sleep Story + Brown Noise", "type": "sleep", "duration": 15},
    },
    "Tuesday": {
        "morning": {"activity": "Body Scan Meditation", "type": "meditation", "duration": 10},
        "midday": {"activity": "Gratitude Journaling", "type": "journal", "duration": 5},
        "evening": {"activity": "Progressive Muscle Relaxation", "type": "pmr", "duration": 20},
    },
    "Wednesday": {
        "morning": {"activity": "Box Breathing for Focus", "type": "breathwork", "duration": 5},
        "midday": {"activity": "Cognitive Reframing Exercise", "type": "cbt", "duration": 15},
        "evening": {"activity": "Theta Binaural Beats", "type": "sound", "duration": 20},
    },
    "Thursday": {
        "morning": {"activity": "Walking Meditation", "type": "meditation", "duration": 15},
        "midday": {"activity": "Worry Time Scheduling", "type": "cbt", "duration": 10},
        "evening": {"activity": "Deep Sleep Delta Waves", "type": "sound", "duration": 30},
    },
    "Friday": {
        "morning": {"activity": "Energizing Breath (4-2-4)", "type": "breathwork", "duration": 5},
        "midday": {"activity": "Mood Check-in + Trigger Analysis", "type": "tracker", "duration": 5},
        "evening": {"activity": "Commute Calm Meditation", "type": "meditation", "duration": 5},
    },
    "Saturday": {
        "morning": {"activity": "Long Body Scan (20 min)", "type": "meditation", "duration": 20},
        "midday": {"activity": "Community Support Check-in", "type": "community", "duration": 10},
        "evening": {"activity": "Sleep Story: The Starlight Garden", "type": "sleep", "duration": 12},
    },
    "Sunday": {
        "morning": {"activity": "Gratitude + Intention Setting", "type": "journal", "duration": 10},
        "midday": {"activity": "Weekly Mood Review", "type": "tracker", "duration": 10},
        "evening": {"activity": "Ocean Waves + Pink Noise", "type": "sound", "duration": 30},
    },
}

POSITIVE_AFFIRMATIONS = [
    "I am doing the best I can, and that is enough.",
    "I choose peace over worry.",
    "My breath is my anchor to the present moment.",
    "I release what I cannot control.",
    "I am resilient, and I have survived every hard day so far.",
    "My feelings are valid, and they are temporary.",
    "I deserve rest without guilt.",
    "Each breath I take calms my mind and body.",
    "I am allowed to take up space and ask for help.",
    "Progress, not perfection, is my goal.",
    "I trust the process of my own healing.",
    "My mind is clearing, like clouds parting to reveal blue sky.",
    "I am safe in this moment, right here, right now.",
    "Small steps still move me forward.",
    "I am worthy of love, compassion, and understanding.",
]

MORE_SLEEP_STORIES = [
    {
        "title": "The Midnight Train to Nowhere",
        "preview": "A gentle train ride through starlit valleys...",
        "duration": "14 min",
        "full_text": """You find yourself on a vintage train, its interior lined with velvet seats the color of midnight blue. The train is nearly empty — just you and the soft glow of brass lamps. Outside your window, the world passes in a dreamlike blur of pine forests and misty valleys. The rhythm of the wheels on the tracks creates a steady, hypnotic beat: clack-clack... clack-clack... like a giant metronome keeping time with your slowing heart. A gentle rain begins to tap against the glass, each drop sliding down in lazy trails that catch the lamplight like tiny falling stars. The conductor, an elderly man with kind eyes, offers you a cup of chamomile tea. It warms your hands. You sip slowly. The train is going nowhere in particular, and that is the point. There is no destination to reach, no schedule to keep. You are simply traveling through the night, carried by something older and steadier than your worries. The seats are impossibly comfortable. The air smells of old books and rain. Somewhere in the distance, a bell tolls softly — once, twice, three times — and each tone seems to pull you deeper into rest. The train will keep going all night. You don't need to stay awake to watch the journey. Close your eyes. The tracks will hold you. The rain will sing you to sleep. And when you wake, the sun will be rising over a new valley, and you will have arrived exactly where you need to be."""
    },
    {
        "title": "The Lighthouse Keeper's Cottage",
        "preview": "A cozy refuge by the sea, where the waves tell old stories...",
        "duration": "11 min",
        "full_text": """You are in a small cottage at the edge of a cliff. The walls are thick stone, covered in soft wool tapestries that absorb every sound. A fire crackles in the hearth, casting dancing shadows that seem to perform silent plays on the ceiling. Through the small, round window, you can see the lighthouse beam sweeping across the dark ocean — a steady, faithful rhythm of light that has guided sailors home for a hundred years. The cottage belongs to no one and everyone. It exists for tired souls who need a place to rest. The bed is piled high with quilts that smell of lavender and sun-dried linen. When you lie down, the mattress seems to remember your shape, cradling you like it has been waiting for you. Outside, the waves crash against the rocks below, but from here they sound like whispers — shhh, shhh, all is well, all is well. A cat, gray as storm clouds, curls up at your feet. Its purr vibrates through the blankets, a living lullaby. The lighthouse beam passes across your window every twelve seconds, and you begin to time your breath to it — inhale as it approaches, exhale as it fades. The fire pops softly. The rain begins to tap the roof. The cat purrs. The waves whisper. The light turns. And you drift, held by the oldest comforts in the world — warmth, shelter, and the sound of the sea keeping its endless, patient watch."""
    },
]

BREATHING_SOUNDS = {
    "Ocean Wave": {"inhale_freq": 200, "exhale_freq": 150, "wave_type": "sine"},
    "Tibetan Bowl": {"inhale_freq": 180, "exhale_freq": 160, "wave_type": "sine"},
    "Soft Chime": {"inhale_freq": 523, "exhale_freq": 440, "wave_type": "sine"},
    "Deep Drone": {"inhale_freq": 110, "exhale_freq": 82, "wave_type": "sine"},
}
