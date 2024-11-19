import re

class Routes:
    #Menu_Principal
    Menu="/menu"
    Catalog="/catalogo"
    Favorites="/favs"
    Meet_us="/meet"
    
    #Menu_Catalogo
    Back="/back"
    Forward="/forward"
    Uno="/uno"
    Dos="/dos"
    Three="/tres"
    Sublime="/sublime"
    Five="/cincp"
    Delete="/erase"
    
    #Menu_Filtro
    Buscar="/search"
    Name="/name"
    Filtro="/ask"
    
    Pos="/rol"
    League="/league"
    value="/price"
    Filtrar="/do"
    borrar="/borrar"
    #Menu_Filtro_Pos
    One_F="/1_Filt"
    Two_F="/2_Filt"
    Tre_F="/3_Filt"
    Jhinn_F="/4_Filt"
    Cinco_F="/5_Filt"
   
    #Menu_Player
    Add_fav=re.compile(r'^Position:.*')