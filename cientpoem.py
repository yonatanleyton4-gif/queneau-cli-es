# Cien mil millones de poemas por Raymond Queneau (Traducción)
from random import randrange

possibilities = [
    # Fila 1
    ["Don Pedro se ha quitado las pulgas de la camisa",
     "El caballo salvaje muerde el friso del Partenón",
     "Al rapé ningún marinero de Cornualles estornudaría",
     "A las cinco en punto salió la Marquesa",
     "Del playboy Azar la ninfa ya no huye",
     "Se agachó justo para recoger su maleta",
     "Cuando uno con el otro de inmediato se pone de acuerdo",
     "La prosa tomó el verso del juglar sin apretarlo",
     "La lengua ácida con la pericia del gourmet",
     "La tumba de mármol se abre con llaves tintineantes"],

    # Fila 2
    ["Los cuernos del toro deberían secarlo como un hueso",
     "Desde que Elgin dejó sus fosas nasales en la piedra",
     "Su éxtasis nasal supera al mejor Colonia",
     "Para el té, sándwiches de pepino y un bollo",
     "A través del crecimiento esnob alrededor de su dobladillo",
     "Que hordas de ladrones sintieron que tenían más derecho a poseer",
     "La respuesta es que podrían ser gemelos adultos",
     "Su exaltación sorprendió tanto a la juventud como a la anciana",
     "Lame las chuletas de mármol tallado sobre caracoles hinchados",
     "Cuando los albañiles agarran el aliento que tenemos prestado"],

    # Fila 3
    ["Las latas de carne viejas y oxidadas esparcen enfermedades",
     "Los turcos dijeron que tomes lo que quieras",
     "Sobre su viejo cofre de roble corta su queso",
     "Su chófer nativo esperaba en la brisa",
     "Su toga arrugada muy por encima de sus rodillas",
     "Se agachó y bueno, ¿qué fue lo que agarró?",
     "Respuestas como esta el cerebro atónito puede burlar",
     "El crítico comprensivo primero ve",
     "El showman hace gárgaras con fuego y espada con facilidad",
     "Formas sombrías con indecisión resollan"],

    # Fila 4
    ["Que el ante se fermente no es nada conocido",
     "Y cantó fuerte desafinado sin un tono",
     "Con huesos de cereza su suelo de la cabaña está sembrado",
     "Lo que ni el tiempo ni la marea pueden posponer por mucho tiempo",
     "Uno recoge capullos de rosa o envejece solo",
     "Las huellas dactilares y del pulgar de Al Capone",
     "Normal uno aspira a ser y compartir el trono",
     "Antes de que nuevos significados a las tribus antiguas sean arrojados",
     "Mientras los tiburones a digamos camarones en maceta son propensos",
     "Y las jaulas vacías muestran que el pájaro de la vida ha volado"],

    # Fila 5
    ["A una dulce hora de dicha mi memoria repica",
     "Oh Partenón tú sostienes las riendas del corcel",
     "Las Islas Frisias mis amigos son cosas apreciadas",
     "Cómo nos sorprendió pálidos subalternos grises",
     "Las ofrendas pisanas del viejo Galileo",
     "Oh cómo oh cómo odia tales hurtos",
     "Y sin embargo fue él a quien el destino mendigo solo arroja",
     "Ambos tienen razón, no murmuraciones indómitas",
     "El tiovivo se come las ganancias hechas en los columpios",
     "Es uno de muchos acontecimientos horribles"],

    # Fila 6
    ["Los gauchos que hacen señales muy rara vez se afeitan",
     "El Viento del Norte muerde en su arquitrabe",
     "Cuyo océano arenques nacidos muertos enfrentan locamente",
     "Cuando la llama una forma a la ira ancestral dio",
     "Fueron ollas pintadas por un esclavo",
     "Birlar la pasta que el ahorro del país ayudó a salvar",
     "Rechazando el armiño para convertirse en un bribón",
     "Que la rima medida sola puede esclavizar almas",
     "Nada puede el tímido roer del ratón evitar",
     "Con pensamientos sombríos ellos sombríamente alinean la nave"],

    # Fila 7
    ["Un carámbano de médula congelada tintinea",
     "El escandaloso Támesis una flecha problemática lanza",
     "Tal mercancía una melancolía trae",
     "Un querido barón se embolsa valiosos Mings",
     "El lingüista inclinado y camarómano canta",
     "Se ha ido a Londres cómo resuena el eco",
     "La madre fértil deja caer cambiantes como reyes",
     "Ambos tienen razón, no son conocimientos no formados",
     "En las ensaladas todos mastican larvas antes de que tengan alas",
     "La muerte orgullosa pica de manera muy i-le-gí-ti-ma"],

    # Fila 8
    ["Como sacos de dormir el paisaje silencioso pavimentan",
     "Para romper una regla el poder de Britania podría renunciar",
     "Por arbustos ardientes nunca los peces perdonaron",
     "Hasta que los bomberos lleguen con una ola gigante de manguera",
     "Palabras etruscas que Grecia y Roma graban",
     "A través de la ladera del hogar bosque roca y cueva",
     "En las cunas más puras así es como se comportan",
     "Que cada shock verbal tiene como objetivo depravar",
     "Los niños más lindos anhelan los caramelos más estrictos",
     "Los gusanos victoriosos muelen todo en la tumba"],

    # Fila 9
    ["Los peregrinos fervientes los viajes más largos no pueden deprimir",
     "La Grecia platónica no era tan sin talento",
     "Cuando se seca la tortuga no puede expresar nada",
     "El faquir que ayuna no huele menos",
     "Las mentes aturdidas pueden resoplar y soplar y adivinar",
     "Las faldas de la campesina en días de lluvia ella trenzaría",
     "El genealogista con campo y faja",
     "La licencia poética no necesita tensión ni estrés",
     "El lobo devora tanto a la oveja como a la pastora",
     "No sirve de nada que los hombres ricos lloren Bendito Cielo"],

    # Fila 10
    ["Qué cosas hicimos fuimos con todo el dichoso cerdo",
     "Un ingenio penetrante azotaría a los caballos más vivaces",
     "Chalotes y aletas de tiburón se enfrentan al leño humeante",
     "En los veranos indios los ingleses beben grog",
     "Con gravedad en el gran engranaje de la gravedad",
     "Y matar de hambre al bebé que gimotea como un perro",
     "Con pluma de cuello blanco a lo largo de su vida trotará",
     "Una lengua servirá para mantener el verso expectante",
     "Un banquete de cerebro de pájaro derrite a la audaz Señora Mog",
     "O sonriendo como un golliwog de cara pálida"],

    # Fila 11
    ["Y jugaron al croquet de montaña al ajedrez de la jungla",
     "Sócrates observó su cicuta efervescer",
     "Mientras las sedes de regreso a casa a cada vaso saciado dicen sí",
     "El coronel sigue con su escudo de armas desvestido",
     "Sobre ruedas el turista sigue a su anfitriona",
     "Observando el estiércol y el compost fusionarse",
     "Para demostrar que mamá es un adulto con un mechón",
     "Desde el fresco Parnaso hasta el salvaje Loch Ness",
     "La tierra del país simplemente prospera con el desorden del corral",
     "El pobre Yorick viene a enterrar, no a dirigirse"],

    # Fila 12
    ["El seductor diálogo del barroco sureño",
     "Sus escultores hicieron lo mejor, nuestros cascos obstruyen",
     "Las langostas en venta deben ser nuestra apología",
     "No hay necesidad de llevar tales tesoros desde la niebla",
     "Con voz quebrada a través de los Alpes ellos se esfuerzan",
     "Uno extraña el hogar del grillo y la rana que croa",
     "Pero puedo entenderte Hermano Gog",
     "Bardo adoro tu monólogo interminable",
     "El whisky siempre despertará un pantano irlandés",
     "Nos sofocaremos antes del epílogo"],

    # Fila 13
    ["Trajes que cecean lenguas españolas para quienes dicen algunos",
     "Con recuerdos de mármol entonces llenar un barrio pobre",
     "En la losa de pescado ni la ballena ni la foca han nadado nunca",
     "El Taj Mahal tiene baratijas especias y goma",
     "¿Los empleados de banco gobiernan su ábaco con el pulgar?",
     "Donde a nadie le importaba cómo uno calentaba su trasero",
     "Y te dejan libre de tus opiniones sombrías",
     "Que los ventrílocuos exploten me dejas mudo",
     "Aunque los pretzels toman los dólares del tambor de la sala de juntas",
     "Pobre lector sonríe antes de que tus labios se entumezcan"],

    # Fila 14
    ["La campana dobla sin cuota sin fi sin fo sin fum",
     "Por la gloria de Europa mientras las arpías del Destino rasguean",
     "Ellos son reyes nosotros somos primos mamíferos hi ho",
     "Y las fechas de los arrendadores tienen una suma demasiado corta",
     "¿En el coñac el brandy es ron Bacardí?",
     "Sin embargo de la tarta de la Ciudad no se sacó ni una ciruela",
     "Un pan sabio siempre conoce su migaja más humilde",
     "Los soliloquios predicen grandes cosas viejo amigo",
     "La morcilla frita y a la parrilla sigue siendo lo mejor del mundo ñam",
     "Lo mejor de todas las cosas a un fin debe llegar"]
]

def createPoem():
    poem = ''
    for i in range(len(possibilities)):
        poem = poem + (possibilities[i][randrange(len(possibilities[i]))]) + '\n'
    return poem

if __name__ == "__main__":
    print(createPoem())