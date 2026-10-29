"""
wisdom_engine.py - El Gran Libro de Sabiduría del Bosque de los Cien Acres
Incluye:
- Metadatos de poses auténticas 2D para cada personaje.
- Frases icónicas y reflexiones de vida.
- MODO ESTUDIO: Consejos filosóficos, tiernos y motivacionales de Winnie the Pooh
  específicamente dedicados al estudio del Derecho en Perú.
"""

import random

CHARACTER_POSES = {
    "pooh": [
        {"file": "pooh_pose1.png", "caption": "Paseando tímido y feliz por el sendero ♡"},
        {"file": "pooh_pose2.png", "caption": "¡Hora de la merienda! Con la carita adentro del tarro de miel 🍯"},
        {"file": "pooh_pose3.png", "caption": "Abrazando feliz su tarrito de 'MIEL' en el suelo"},
        {"file": "pooh_pose4.png", "caption": "Flotando suavecito hacia el cielo con su globo rojo 🎈"},
        {"file": "pooh_pose5.png", "caption": "Sentado pensando: 'Piensa, piensa, piensa...'"},
        {"file": "pooh_pose6.png", "caption": "Haciendo equilibrio alegremente sobre el tronco del arroyo"}
    ],
    "piglet": [
        {"file": "piglet_pose1.png", "caption": "Saludando con una patita arriba y suéter a rayas rosas 🌸"},
        {"file": "piglet_pose2.png", "caption": "Mirando con admiración y ternura a sus amigos"},
        {"file": "piglet_pose3.png", "caption": "Dando pasitos valientes por el bosque 🍃"},
        {"file": "piglet_pose4.png", "caption": "Esperando sonriente en la puerta de madera"},
        {"file": "piglet_pose5.png", "caption": "Sosteniendo una pequeña flor silvestre para ti 🌼"}
    ],
    "tigger": [
        {"file": "tigger_pose1.png", "caption": "¡Dando un salto gigante por los aires! ¡Hoo-hoo-hooo! 🐯"},
        {"file": "tigger_pose2.png", "caption": "Rebotando enérgico sobre su cola en espiral"},
        {"file": "tigger_pose3.png", "caption": "Sentado descansando y riéndose a carcajadas"},
        {"file": "tigger_pose4.png", "caption": "Acurrucado contento en el tronco del roble"},
        {"file": "tigger_pose5.png", "caption": "Cruzando el puente a puros rebotes y alegría"}
    ],
    "eeyore": [
        {"file": "eeyore_pose1.png", "caption": "Sentado tranquilo con el lazo rosa en su cola 🎀"},
        {"file": "eeyore_pose2.png", "caption": "Caminando despacito y mirando hacia atrás"},
        {"file": "eeyore_pose3.png", "caption": "Paseando con la cabecita baja pero el corazón lleno"},
        {"file": "eeyore_pose4.png", "caption": "Visitando a Pooh en el sendero florecido"},
        {"file": "eeyore_pose5.png", "caption": "Reflexionando con paciencia: gracias por notar que estoy aquí"}
    ],
    "christopher": [
        {"file": "christopher_pose1.png", "caption": "Sosteniendo el gran globo rojo y la colita de Igor 🎈"},
        {"file": "christopher_pose2.png", "caption": "Liderando la caminata de los amigos por el puente de piedra"},
        {"file": "christopher_pose3.png", "caption": "Cruzando el arroyo en equilibrio con los brazos abiertos"},
        {"file": "christopher_pose4.png", "caption": "Recordándote: 'Eres más valiente de lo que crees...'"}
    ],
    "rabbit": [
        {"file": "rabbit_pose1.png", "caption": "Asombrado mirando las flores del huerto 🥕"},
        {"file": "rabbit_pose2.png", "caption": "Conversando con Piglet y organizando el paseo"},
        {"file": "rabbit_pose3.png", "caption": "Caminando apurado hacia la merienda"},
        {"file": "rabbit_pose4.png", "caption": "Sosteniendo una zanahoria fresca con orgullo"}
    ],
    "owl": [
        {"file": "owl_pose1.png", "caption": "Abriendo sus alas con sabiduría desde las alturas 🦉"},
        {"file": "owl_pose2.png", "caption": "Posado en la rama observando a todos con cariño"},
        {"file": "owl_pose3.png", "caption": "Volando sobre el arroyo de los Cien Acres"},
        {"file": "owl_pose4.png", "caption": "Acomodándose sus gafas de lectura para contar una historia"}
    ]
}

# CONSEJOS FILOSÓFICOS DE POOH PARA EL MODO ESTUDIO (DERECHO EN PERÚ)
LAW_STUDY_WISDOM = [
    {
        "quote": "Yo soy solo un osito con muy poco cerebro y no entiendo de códigos ni de leyes tan gruesas como troncos... pero sé que tú sí, porque eres increíblemente inteligente. Y sé que las leyes existen para cuidar a los que tienen miedo, igual que yo cuido a Piglet cuando tiembla en el bosque.",
        "lesson": "El verdadero Derecho nace de la empatía: proteger a quien lo necesita.",
        "context": "Pooh acompañándote en tu escritorio con una taza de té."
    },
    {
        "quote": "En Perú tienen montañas tan altas que tocan las nubes, y ríos que cruzan valles enteros. Los ríos nunca tienen prisa por llegar al mar; van con calma, curva por curva. No te desesperes por memorizar todo hoy; un artículo a la vez, con paciencia y calma.",
        "lesson": "Respeta tu propio ritmo de aprendizaje. La sabiduría no se apresura.",
        "context": "Mirando las ramas flotar en el río hacia el mar."
    },
    {
        "quote": "Dicen que la justicia lleva una balanza en la mano. A mí me recuerda a cuando peso un tarro de miel contra otro para asegurarme de que a Igor no le falte nada. El Derecho no son solo palabras difíciles en latín; es el arte de no dejar a nadie desamparado.",
        "lesson": "La justicia más pura es la que devuelve la dignidad y el abrigo a las personas.",
        "context": "Pooh pesando tarros de miel para compartirlos."
    },
    {
        "quote": "A veces las personas creen que un gran abogado es el que habla más fuerte o el que tiene la oficina más elegante. Pero Christopher Robin me enseñó que la verdadera grandeza está en escuchar con el corazón a quien nadie más escucha. Tú tienes esa ternura que tanta falta hace en el mundo.",
        "lesson": "Tu capacidad de conectar con el dolor y la verdad de la gente será tu mayor poder.",
        "context": "Una lección de Christopher Robin bajo el roble."
    },
    {
        "quote": "Si hoy te sientes cansada y los párrafos del libro parecen abejas zumbando en círculos, cierra los ojos cinco minutos. Apoya tu cabecita. Descansar no es perder tiempo; es darle permiso a tu mente brillante para florecer.",
        "lesson": "Cuida tu bienestar. Un corazón descansado razona con mucha más claridad.",
        "context": "Hora de una pequeña siesta reparadora bajo el árbol."
    },
    {
        "quote": "Cuando leas sobre la Constitución y sobre la justicia en tu país, recuerda que detrás de cada expediente hay una familia, una historia y una lágrima. Tu vocación será ser la voz de los que no pueden defenderse solos. Qué afortunado es el Perú de tener a una futura abogada con un corazón tan noble como el tuyo.",
        "lesson": "Detrás de cada norma jurídica siempre late una vida humana.",
        "context": "Reflexión al atardecer en la colina."
    },
    {
        "quote": "Búho siempre usa palabras de diez sílabas para parecer importante, pero casi nadie le entiende... Tú no necesitas palabras complicadas para hacer justicia. Tu honestidad, tu mirada sincera y tu bondad son tus mejores argumentos ante cualquier tribunal.",
        "lesson": "La sencillez y la sinceridad convencen más que la arrogancia.",
        "context": "Conversando en la biblioteca de Búho."
    },
    {
        "quote": "¿Sabes qué es lo más valiente del mundo? Sentarte a estudiar frente a libros enormes cuando tienes sueño, solo porque tienes un sueño aún más grande en el pecho. Recuerda siempre la promesa: eres más valiente de lo que crees, más fuerte de lo que pareces y mucho más inteligente de lo que piensas.",
        "lesson": "Tu esfuerzo silencioso de hoy construirá la justicia del mañana.",
        "context": "La promesa eterna de Christopher Robin."
    },
    {
        "quote": "Si un examen no sale perfecto o un caso se siente enredado como una pita de cometa, no pasa nada. Comeremos un poquito de miel, respiraremos hondo y volveremos a empezar. Tu valor como persona no cabe en una calificación, cabe en la luz que le das al mundo.",
        "lesson": "Un tropiezo es solo una piedra en el sendero; no define quién eres.",
        "context": "Pooh desenredando la pita de una cometa con calma."
    },
    {
        "quote": "El Derecho, en el fondo, es como cuidar el bosque: limpiar las ramas caídas para que nadie tropiece, sembrar flores donde hubo dolor y asegurarse de que todos, desde los más grandes como Tigger hasta los más pequeños como Piglet, tengan un rincón seguro para ser felices.",
        "lesson": "Construir orden con amor es la esencia de las leyes justas.",
        "context": "Caminando juntos por los senderos limpios de los Cien Acres."
    },
    {
        "quote": "Estoy muy orgulloso de ti. Mientras estudias, yo me quedo aquí sentadito a tu lado haciéndote compañía en silencio, cuidando tu merienda y recordándote sonreír cada vez que levantes la vista del papel.",
        "lesson": "Nunca estás sola en tus desvelos. Siempre hay cariño acompañándote.",
        "context": "Pooh sentado junto a tus apuntes con una sonrisa dulce."
    }
]

CHARACTERS_DATA = {
    "pooh": {
        "name": "Winnie the Pooh",
        "title": "El Oso Bobito de Gran Corazón",
        "description": "Amante de la miel, reflexivo, inocente y el amigo más fiel del bosque.",
        "iconic_quotes": [
            {
                "quote": "Si vives hasta los cien años, yo quiero vivir cien años menos un día, para no tener que vivir nunca sin ti.",
                "lesson": "El amor verdadero no se mide en días, sino en no querer soltar a quien te hace bien.",
                "context": "Dicho a Christopher Robin en una tarde de sol."
            },
            {
                "quote": "A veces, las cosas más pequeñas son las que ocupan el espacio más grande dentro de tu corazón.",
                "lesson": "Un mensaje inesperado, una risa compartida... ahí habita la verdadera magia.",
                "context": "Sobre los pequeños detalles de cada día."
            },
            {
                "quote": "—¿Qué día es hoy? —preguntó Pooh.\n—Es hoy —chilló Piglet emocionado.\n—Mi día favorito —dijo Pooh con una sonrisa.",
                "lesson": "No esperes a un día especial en el calendario; hoy ya es un regalo por el solo hecho de respirar y sonreír.",
                "context": "Caminando de la mano por el bosque."
            },
            {
                "quote": "Los ríos lo saben muy bien: no hay ninguna prisa. Llegaremos algún día.",
                "lesson": "Deja de angustiarte por correr. Las cosas buenas florecen a su propio ritmo.",
                "context": "Mirando las ramas flotar en el río desde el puente."
            },
            {
                "quote": "Un día sin un amigo es como un tarrito al que no le queda ni una sola gota de miel adentro.",
                "lesson": "La vida sin alguien con quien compartir tus días se siente vacía; cuida a quienes endulzan tu mundo.",
                "context": "Buscando provisiones para la merienda."
            },
            {
                "quote": "Qué afortunado soy de tener algo que hace que decir adiós sea tan difícil.",
                "lesson": "El dolor de extrañar a alguien es el reflejo más puro de lo profundo que fue el cariño.",
                "context": "Al despedirse de Christopher Robin."
            },
            {
                "quote": "No puedes quedarte en tu rincón del bosque esperando a que otros vengan a ti. A veces tienes que salir tú y dar el primer pasito.",
                "lesson": "El mundo y el cariño están afuera, esperando que te animes a abrir la puerta.",
                "context": "Animando a Piglet a dar un paseo."
            },
            {
                "quote": "A veces me siento y pienso... y otras veces, simplemente me siento.",
                "lesson": "Descansar la cabecita sin culpa es una de las mayores sabidurías de la vida.",
                "context": "Bajo la sombra del viejo roble."
            },
            {
                "quote": "Una pequeña consideración, un poquito de ternura por los demás, hace toda la diferencia del mundo.",
                "lesson": "La amabilidad nunca es pequeña; es la miel que endulza cualquier corazón herido.",
                "context": "Llevándole una flor a Igor."
            },
            {
                "quote": "Si alguna vez llega un día en que no podamos estar juntos, guárdame en tu corazón. Me quedaré allí para siempre.",
                "lesson": "La distancia física no existe para quienes se quieren de verdad.",
                "context": "Promesa eterna a sus amigos."
            }
        ]
    },
    "piglet": {
        "name": "Piglet (Puerquito)",
        "title": "El Pequeño Amigo Valiente",
        "description": "Tímido y de corazón gigante; demuestra que la ternura es la mayor fuerza.",
        "iconic_quotes": [
            {
                "quote": "—¿Cómo se deletrea 'Amor'? —preguntó Piglet.\n—No se deletrea, Piglet... se siente —respondió Pooh suavemente.",
                "lesson": "Los sentimientos más puros no necesitan explicaciones lógicas, solo vivirse.",
                "context": "Sentados juntos viendo caer las hojas de otoño."
            },
            {
                "quote": "Incluso el animalito más pequeño puede tener un corazón gigantesco y hacer cosas maravillosas.",
                "lesson": "Nunca te sientas pequeña ante el mundo. Tu calidez tiene un poder inmenso.",
                "context": "Cuando Piglet salvó a Pooh y Búho en la tormenta."
            },
            {
                "quote": "Piglet descubrió que aunque sus patitas temblaran de miedo, mientras sostuviera la mano de Pooh, el bosque ya no era tan oscuro.",
                "lesson": "El amor y la compañía de las personas correctas ahuyentan cualquier temor.",
                "context": "Cruzando el bosque en una noche ventosa."
            },
            {
                "quote": "Las cosas que me hacen diferente y tímido son exactamente las cosas que me hacen ser yo.",
                "lesson": "Abrázate con tus rarezas y tu sensibilidad; no necesitas ser ruidosa para ser valiosa.",
                "context": "Conversando con Christopher Robin."
            },
            {
                "quote": "—Pooh, ¿prometes que nunca me olvidarás? ¿Ni siquiera cuando tenga cien años?\n—Ni en mil mañanas, Piglet.",
                "lesson": "La verdadera lealtad no tiene fecha de vencimiento.",
                "context": "En la cima de la colina de los Cien Acres."
            },
            {
                "quote": "A veces da mucho miedo ser pequeño en un mundo tan grande, pero me gusta saber que hay alguien cuidando de mí.",
                "lesson": "Permítete ser cuidada y querida; es seguro bajar la guardia con quien te aprecia.",
                "context": "Acurrucado junto a Pooh frente al fuego."
            }
        ]
    },
    "eeyore": {
        "name": "Igor (Eeyore)",
        "title": "El Burrito Reflexivo y Honesto",
        "description": "Melancólico, pero agradecido; nos enseña el valor de acompañar sin juzgar.",
        "iconic_quotes": [
            {
                "quote": "Podría llover... o tal vez no. De todos modos, gracias por notar que existo.",
                "lesson": "A veces, hacerle saber a alguien que estás ahí y que lo ves, cambia por completo su día gris.",
                "context": "En su rincón sombrío con su casita de palos."
            },
            {
                "quote": "No todos podemos... y algunos de nosotros no lo hacemos. Eso es todo. No hay necesidad de quejarse.",
                "lesson": "Está bien tener días donde solo puedes dar lo mínimo. Respeta tus procesos.",
                "context": "Mirando su reflejo en el arroyo."
            },
            {
                "quote": "A veces no necesito que nadie arregle nada... solo que alguien se siente a mi lado en silencio mientras pasa la lluvia.",
                "lesson": "La empatía no es dar discursos de optimismo forzado, es compañía paciente.",
                "context": "Cuando Pooh y Piglet se quedaron con él bajo la tormenta."
            },
            {
                "quote": "Un poco de consideración, un poco de pensamiento por los demás... eso es lo que hace que este lugar sea soportable.",
                "lesson": "Un gesto sincero de bondad puede sostener el día más pesado.",
                "context": "Al recibir un globo desinflado pero lleno de amor."
            },
            {
                "quote": "No espero mucho del día, pero verte venir por el sendero hace que el pasto sepa un poco más dulce.",
                "lesson": "Incluso en los corazones más tristes, el cariño deja una lucecita encendida.",
                "context": "Viendo llegar a Christopher Robin."
            },
            {
                "quote": "La nieve seguirá cayendo, pero las colas se pueden volver a colocar con un clavito y una cinta bonita.",
                "lesson": "Casi todo lo que sentimos que se rompió por dentro, con paciencia y cariño, se puede sanar.",
                "context": "Cuando Pooh encontró su cola perdida."
            }
        ]
    },
    "tigger": {
        "name": "Tigger",
        "title": "El Tigre Saltarín del Optimismo",
        "description": "Lleno de energía, saltos y alegría contagiosa; el recordatorio de abrazar la vida con chispa.",
        "iconic_quotes": [
            {
                "quote": "¡Lo más maravilloso de los Tiggers es que los Tiggers son cosas maravillosas! ¡Y lo mejor de todo es que soy el único! ¡Hoo-hoo-hoo-hooo!",
                "lesson": "Eres única en todo este universo. Nadie tiene tu risa ni tu magia; celébrate con orgullo.",
                "context": "Rebotando por todo el bosque sobre su cola."
            },
            {
                "quote": "¡El rebote es lo que los Tiggers hacen mejor! La vida es demasiado corta para caminar arrastrando los pies.",
                "lesson": "Ponle entusiasmo a lo que amas. ¡Atrévete a dar saltos de fe!",
                "context": "Enseñándole a saltar a Rito."
            },
            {
                "quote": "¡No hay nada que un buen salto y un abrazo sorpresa no puedan solucionar!",
                "lesson": "El optimismo y el cariño activo desarman cualquier día nublado.",
                "context": "Sorprendiendo a Pooh en su puerta."
            },
            {
                "quote": "A veces saltamos tan alto que quedamos atrapados en las ramas de un árbol... pero lo importante fue atreverse a subir.",
                "lesson": "No le temas a equivocarte por soñar en grande. Siempre habrá amigos para ayudarte a bajar.",
                "context": "En lo alto del árbol más grande del bosque."
            },
            {
                "quote": "Un verdadero amigo es aquel que te deja rebotar sobre él... y luego se ríe contigo en el suelo.",
                "lesson": "Ríanse juntos, jueguen y no tomen la vida con tanta seriedad.",
                "context": "Abrazando a Pooh tras un tropiezo divertido."
            }
        ]
    },
    "christopher": {
        "name": "Christopher Robin",
        "title": "El Guía Dulce de la Infancia",
        "description": "La voz del amor incondicional, la valentía y el refugio protector.",
        "iconic_quotes": [
            {
                "quote": "Prométeme que siempre recordarás esto: Eres más valiente de lo que crees, más fuerte de lo que pareces y mucho más inteligente de lo que piensas.",
                "lesson": "Grábate esta frase en el alma para cada momento en que dudes de ti misma. Puedes con todo.",
                "context": "El consejo más icónico y conmovedor de la historia de Pooh."
            },
            {
                "quote": "Si alguna vez nos separamos o crecemos, solo recuerda: siempre estaré contigo, incluso si no me puedes ver.",
                "lesson": "Los lazos de afecto sincero van más allá del tiempo y la distancia.",
                "context": "En el lugar encantado del bosque antes de partir a la escuela."
            },
            {
                "quote": "Eres mi oso bobito preferido, y jamás, pase lo que pase, te voy a dejar solo.",
                "lesson": "Sentirse elegida y querida incondicionalmente es el refugio más seguro que existe.",
                "context": "Abrazando a Pooh bajo la lluvia."
            },
            {
                "quote": "No crecemos para olvidar el Bosque de los Cien Acres; crecemos para llevar su ternura en el corazón todos los días.",
                "lesson": "Nunca pierdas tu capacidad de asombro, de jugar y de conmoverte con lo simple.",
                "context": "La despedida en el libro original de A.A. Milne."
            }
        ]
    },
    "rabbit": {
        "name": "Conejo (Rabbit)",
        "title": "El Organizador del Huerto",
        "description": "Pragmático y un poco gruñón por fuera, pero con un corazón tierno y protector.",
        "iconic_quotes": [
            {
                "quote": "El orden y las listas de tareas son importantes, pero cuando un amigo toca a tu puerta, la tetera siempre se pone al fuego.",
                "lesson": "Las personas que quieres siempre están por encima de las agendas y las prisas.",
                "context": "Abriendo la puerta a Pooh a la hora del té."
            },
            {
                "quote": "A veces las zanahorias tardan semanas en brotar bajo tierra sin que se vea nada... Ten paciencia con tus propios frutos.",
                "lesson": "Aunque no veas resultados inmediatos hoy, todo tu esfuerzo silencioso está echando raíces.",
                "context": "Regando su huerto con dedicación."
            },
            {
                "quote": "Me quejo de que Pooh se atasca en mi puerta después de comer miel, pero secretamente me alegra que sea mi casa a la que siempre viene.",
                "lesson": "Ser el lugar seguro de alguien es un privilegio hermoso.",
                "context": "Limpiando su despensa."
            }
        ]
    },
    "owl": {
        "name": "Búho (Owl)",
        "title": "El Erudito Relator de Historias",
        "description": "Sabio, amante de los libros y de las anécdotas largas y reconfortantes.",
        "iconic_quotes": [
            {
                "quote": "Las palabras largas y elegantes son maravillosas en los libros, pero un '¿cómo estás hoy?' sincero siempre es más elocuente.",
                "lesson": "No necesitas grandes discursos para demostrar cariño; la sencillez del afecto lo dice todo.",
                "context": "Desde su biblioteca en el hueco del árbol."
            },
            {
                "quote": "Una taza de té caliente y una buena historia compartida abrigan el alma más que cualquier abrigo de lana.",
                "lesson": "Crea momentos de calma, lee, conversa y date tiempo para disfrutar de las pausas.",
                "context": "Recibiendo visitas en una tarde de viento."
            }
        ]
    }
}

SCENARIOS_DATA = {
    "pooh_house": {
        "id": "pooh_house",
        "name": "La Casa de Pooh",
        "subtitle": "Bajo el letrero rústico 'Mr Sanders' con aroma a madera cálida 🍯",
        "file": "bg_pooh_house.png"
    },
    "bridge": {
        "id": "bridge",
        "name": "El Puente de Piedra",
        "subtitle": "El puente clásico sobre el arroyo donde las ramas flotan en paz 🍃",
        "file": "bg_bridge.png"
    },
    "galleons_lap": {
        "id": "galleons_lap",
        "name": "El Tronco en el Arroyo",
        "subtitle": "Donde Christopher y Pooh hacen equilibrio sobre el agua 🌊",
        "file": "bg_galleons_lap.png"
    },
    "everest_forest": {
        "id": "everest_forest",
        "name": "El Gran Bosque",
        "subtitle": "Cielos suaves y colinas verdes del Bosque de los Cien Acres 🌳",
        "file": "bg_everest_forest.png"
    },
    "meadow_sun": {
        "id": "meadow_sun",
        "name": "Prado del Sol Naciente",
        "subtitle": "El sol dorado asomándose sobre las colinas florecidas 🌅",
        "file": "bg_meadow_sun.png"
    },
    "honey_room": {
        "id": "honey_room",
        "name": "Rincón de la Miel",
        "subtitle": "Cálida habitación de madera con los tarros de miel de Pooh 🍯",
        "file": "bg_honey_room.png"
    }
}

SECRET_LETTER = {
    "title": "Para una Persona Tan Especial como la Miel 🍯✨",
    "content": (
        "Hay personas en este mundo que iluminan los días como un rayito de sol en el Bosque de los Cien Acres.\n\n"
        "Esta pequeña aplicación fue creada pensando en ti: para recordarte siempre lo valiosa, dulce, fuerte y única que eres.\n\n"
        "Cada personaje de esta historia tiene un pedacito de enseñanza para tu vida: la calma de Pooh, el coraje de Piglet, la compañía sincera de Igor y la fe de Christopher Robin.\n\n"
        "Cuando el mundo se sienta pesado, vuelve a este libro, cambia de paisaje, escucha a los personajes y recuerda que hay alguien que admira tu sonrisa y que te desea lo más bonito de la vida.\n\n"
        "Con todo mi cariño. ❤️"
    )
}

def get_character_info(char_id: str) -> dict:
    return CHARACTERS_DATA.get(char_id, CHARACTERS_DATA["pooh"])

def get_character_quotes(char_id: str) -> list:
    info = get_character_info(char_id)
    return info["iconic_quotes"]

def get_character_poses(char_id: str) -> list:
    return CHARACTER_POSES.get(char_id, CHARACTER_POSES["pooh"])

def get_random_quote_for_character(char_id: str) -> dict:
    quotes = get_character_quotes(char_id)
    selected = random.choice(quotes)
    info = get_character_info(char_id)
    return {
        "char_id": char_id,
        "speaker": info["name"],
        "title": info["title"],
        "quote": selected["quote"],
        "lesson": selected["lesson"],
        "context": selected.get("context", "")
    }

def get_random_law_study_quote() -> dict:
    selected = random.choice(LAW_STUDY_WISDOM)
    return {
        "char_id": "pooh",
        "speaker": "Winnie the Pooh",
        "title": "Compañero de Estudio & Filosofía de Vida",
        "quote": selected["quote"],
        "lesson": selected["lesson"],
        "context": selected["context"]
    }

def analyze_and_get_wisdom(user_text: str, current_char_id="pooh") -> dict:
    if not user_text or not user_text.strip():
        return get_random_quote_for_character(current_char_id)

    clean = user_text.lower()
    
    # Detección de estudio o derecho
    if any(k in clean for k in ["estudi", "derecho", "examen", "peru", "ley", "leyes", "caso", "abogad", "justicia"]):
        return get_random_law_study_quote()
        
    if "piglet" in clean or "puerquito" in clean:
        return get_random_quote_for_character("piglet")
    elif "igor" in clean or "eeyore" in clean or "triste" in clean or "llorar" in clean or "gris" in clean:
        return get_random_quote_for_character("eeyore")
    elif "tigger" in clean or "alegr" in clean or "saltar" in clean or "energia" in clean:
        return get_random_quote_for_character("tigger")
    elif "christopher" in clean or "valiente" in clean or "miedo" in clean or "fuerza" in clean:
        return get_random_quote_for_character("christopher")
    elif "conejo" in clean or "rabbit" in clean or "orden" in clean or "paciencia" in clean:
        return get_random_quote_for_character("rabbit")
    elif "buho" in clean or "búho" in clean or "owl" in clean or "libro" in clean or "consejo" in clean:
        return get_random_quote_for_character("owl")
        
    quotes = get_character_quotes(current_char_id)
    for q in quotes:
        combined = (q["quote"] + " " + q["lesson"] + " " + q.get("context", "")).lower()
        words = clean.split()
        if any(w in combined for w in words if len(w) > 3):
            info = get_character_info(current_char_id)
            return {
                "char_id": current_char_id,
                "speaker": info["name"],
                "title": info["title"],
                "quote": q["quote"],
                "lesson": q["lesson"],
                "context": q.get("context", "")
            }
            
    return get_random_quote_for_character(current_char_id)

def get_secret_letter():
    return SECRET_LETTER
