from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from Controladores.Routes import Routes

from typing import Tuple 

import pandas as pd

class MenuTemplate:
    
 
 
    def get_principal_menu_view()-> Tuple[str, InlineKeyboardButton]:
        menu_view_text="**Menu Principal**"
        
        keyboard=[
            [InlineKeyboardButton("💱 Ver Catalogo", callback_data=Routes.Catalog), InlineKeyboardButton("👁‍🗨 Conocenos", callback_data= Routes.Meet_us)]
        ]

        reply_markup=InlineKeyboardMarkup(keyboard)

        return(menu_view_text, reply_markup)
    
  
  
    def get_players_view_from_table_values(table: pd.DataFrame, pos: int, max: int):
      

        keyboard=[[InlineKeyboardButton("◀", callback_data=Routes.Back), InlineKeyboardButton("1️⃣", callback_data=Routes.Uno),
                   InlineKeyboardButton("2️⃣", callback_data=Routes.Dos), InlineKeyboardButton("3️⃣", callback_data=Routes.Three),
                   InlineKeyboardButton("4️⃣", callback_data=Routes.Sublime), InlineKeyboardButton("5️⃣",callback_data=Routes.Five),
                   InlineKeyboardButton("▶", callback_data=Routes.Forward)
                  ],
                    
                  [InlineKeyboardButton("🔙", callback_data=Routes.Menu),
                   InlineKeyboardButton("🔎 ", callback_data=Routes.Buscar)],
                ]

        players_str="** ⚽ Listado de Jugadores **"
        players_str+="\n"+(len(players_str)*"-")+"\n"
        j=1

        if(pos>max):
            pos-=max
            
            for i in range(1, pos):
             
             player=table.iloc[(-i),1]
             nation=table.iloc[(-i),2]
             nation=nation.split()

             show_players=str(j)+" -"+nation[0]+" | "+player

             players_str+= show_players + "\n"*2
             j+=1 

        else:

          
          for i in range(pos-5 ,pos):
            player=table.iloc[i,1]
            nation=table.iloc[i,2]
            nation=nation.split()

            show_players=str(j)+" -"+nation[0]+" | "+player


            players_str+= show_players + "\n"*2
            j+=1 

        reply_markup=InlineKeyboardMarkup(keyboard)
        return (players_str, reply_markup)
    
    def filtre_menu()-> Tuple[str, InlineKeyboardButton]:
        menu_text="**🔍Seleccione su metodo de busqueda**"

        keyboard=[[InlineKeyboardButton("🚹 Nombre",callback_data=Routes.Name), InlineKeyboardButton("💬 Filtros",callback_data=Routes.Filtro)],
                    [InlineKeyboardButton("🔙", callback_data=Routes.Catalog)]
                    ]
        
        reply_markup=InlineKeyboardMarkup(keyboard)

        return(menu_text, reply_markup)
    
    def filtre_tag(reg:list, bnd: bool)->Tuple[str, InlineKeyboardButton]:

       if(bnd):
        menu_selection_text="**Filtros a aplicar:\n"

        for i in reg:
         keyboard=[ [InlineKeyboardButton("📍 Posicion",callback_data=Routes.Pos), InlineKeyboardButton("🛡 Liga",callback_data=Routes.League),
                    InlineKeyboardButton("💸 Precio", callback_data=Routes.value)],
                    
                    [InlineKeyboardButton("🗑",callback_data=Routes.borrar),InlineKeyboardButton("🔎",callback_data=Routes.Filtrar)],

                    [InlineKeyboardButton("🔙", callback_data=Routes.Buscar)]
                  ]


         if(i!=" "):
          menu_selection_text+=i+"\n"

       else:
          menu_selection_text="**Seleccione los filtros deseados**:"

          keyboard=[ [InlineKeyboardButton("📍 Posicion",callback_data=Routes.Pos), InlineKeyboardButton("🛡 Liga",callback_data=Routes.League),
                      InlineKeyboardButton("💸 Precio", callback_data=Routes.value)],

                     [InlineKeyboardButton("🔙", callback_data=Routes.Buscar)]
                ]
      
       reply_markup=InlineKeyboardMarkup(keyboard)

       return(menu_selection_text,reply_markup)

    def position(pos:list, n: int, max_value:int, select: int):
        keyboard=[[InlineKeyboardButton("◀", callback_data=Routes.Back), InlineKeyboardButton("1️⃣", callback_data=Routes.One_F),
             InlineKeyboardButton("2️⃣", callback_data=Routes.Two_F), InlineKeyboardButton("3️⃣", callback_data=Routes.Tre_F),
             InlineKeyboardButton("4️⃣", callback_data=Routes.Jhinn_F), InlineKeyboardButton("5️⃣",callback_data=Routes.Cinco_F),
             InlineKeyboardButton("▶", callback_data=Routes.Forward)
              ],
                   
              [InlineKeyboardButton("🔙", callback_data=Routes.Filtro)],
               ]

        j = 1

        if(select==0):    
            filt_str = "** 📍 Posiciones posibles**"
            filt_str += "\n" + (len(filt_str) * "-") + "\n"
        elif(select==1):
             filt_str = "** 🛡 Ligas disponibles**"
             filt_str += "\n" + (len(filt_str) * "-") + "\n"
        else:
            filt_str = "** 💸 Rango de presupuesto**"
            filt_str += "\n" + (len(filt_str) * "-") + "\n"
       
        if n > len(pos):
            n = len(pos)  

        if n > max_value:
            n -= max_value 
            for i in range(1, n + 1):  
                pos_slt = pos[-i] 
                show_pos = str(j) + " - " + pos_slt
                filt_str += show_pos + "\n\n" 
                j += 1
        else:
            
            start_index = max(0, n - 5) 
            for i in range(start_index, n):
                pos_slt = pos[i]
                show_pos = str(j) + " - " + pos_slt
                filt_str += show_pos + "\n\n"  
                j += 1


        reply_markup=InlineKeyboardMarkup(keyboard)
        return (filt_str, reply_markup)
    
    
    def player_info(table: pd.DataFrame, pos: int, max: int, band: int):
        L_aux=["⚽ Jugador \n| ", "🗺 Pais\n| ","📍 Posicion\n| ","🖇 Equipo\n| ","🛡 Liga \n| ", "📅 Edad \n| ","🦶 Dominante\n| ","📐 Altura\n| ","💵 Valor\n | ", "🕹 Juegos\n| ","⏱ Minutos de Juego\n| ","🥅 Goles\n| ","👏 Asistencias\n| ","🟨 Tarjetas Amarillas\n| ", "🟥 Tarjetas Rojas\n| "]
        players_str="** 📃 Informacion del Jugador"
        players_str+="\n"+(len(players_str)*"-")+"\n"
        
      
        keyboard=[[InlineKeyboardButton("❌",callback_data=Routes.Delete)]]
       

        for i in range(1,len(L_aux)+1):
            players_str+=L_aux[i-1]+table.iloc[pos,i]+"\n\n"

        reply_markup=InlineKeyboardMarkup(keyboard)

        return(players_str,reply_markup)

    def buscar_nombre():
      text="🔍 Para realizar la busqueda ingresa el comando:\n </buscar + [Nombre del Jugador]>"
      keyboard=[[InlineKeyboardButton("🔙", callback_data=Routes.Buscar)]]
      reply_markup=InlineKeyboardMarkup(keyboard)

      return(text, reply_markup)
