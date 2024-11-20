from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext

from Controladores.SheetsService import SheetsService
from Controladores.MenuTemplate import MenuTemplate
from Controladores.Routes import Routes
import pandas as pd
 
 
#Constantes
SHEET_ID = "1TF6WowBqd2DSielZoNMwK_pIWnU-9WZBOx09RuE8sf4"
BOT_TOKEN = "7973933074:AAERhA0iLihF2y-J0f4uZP_5-gpyrJBjx2w"
Mascota_del_proyecto="https://postimg.cc/4K8nHMD4"

L_pos=["DF", "MF", "FW", "GK", "MF,FW" ,"FW,MF", "MF,DF", "DF,FW", "FW,DF", "DF,MF"]
L_league=["La-Liga", "Ligue-1", "Premier-League", "Serie-A", "Bundesliga"]
L_value=["1000000","5000000","20000000","60000000","180000000"]
   
#credenciales del csv
sheetConfig=SheetsService("footrade-telegram-bot-0450121faf53.json")
sheet= sheetConfig.get_sheet_by_id(SHEET_ID) 


#Variables GLobales
pag=0
pag2=0
bckp=5
Filt=[" "," "," "]
band=False
band2=False
band_F=False
select_filt=-1
df_filt=pd.DataFrame()
reg=0

#Cargamos los datos a memoria
clog_list=sheet.sheet1.get_all_values()
df= pd.DataFrame(clog_list[1:],columns=clog_list[0])

clog_list=0


#Controladores

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
   global pag, band2, pag2, band_F,band, Filt

   pag=0
   band2=False
   pag2=0
   band_F=False
   band=False
   Filt=[" "," "," "]
   
   (Menu_text, reply_markup)= MenuTemplate.get_principal_menu_view()

   await update.message.reply_photo(photo=Mascota_del_proyecto,caption=Menu_text,reply_markup=reply_markup)

    

   

async def show_menu(update: Update, context: CallbackContext):
    global pag, band2, pag2, band_F,band, Filt

    pag=0
    band2=False
    pag2=0
    band_F=False
    band=False
    Filt=[" "," "," "]

    (Menu_text, reply_markup)= MenuTemplate.get_principal_menu_view()
   
    
   

    await update.callback_query.answer()
    await update.callback_query.message.reply_photo(photo=Mascota_del_proyecto,caption=Menu_text,reply_markup=reply_markup)
    await update.callback_query.delete_message()


async def show_catalog(update: Update, context: CallbackContext):

   
   global pag, band2, pag2, band_F, band

   message=update.callback_query.message
   

   if(band_F):
      band2=False
      pag2=0
      band_F=False
      band=False
   else:
      pag+=5
      

   text, reply_markup=MenuTemplate.get_players_view_from_table_values(df, pag, len(df))

   await update.callback_query.answer()
   await message.reply_text(text, reply_markup=reply_markup)
   await update.callback_query.delete_message() 


async def next_catalog(update: Update, context: CallbackContext):
      
   

      global pag, pag2, band2, L_pos, L_league, L_value, select_filt
      message=update.callback_query.message
      await update.callback_query.answer()

      if(band2):
        if(select_filt==0):
         if(pag2<len(L_pos)):
               pag2+=5
               text, reply_markup=MenuTemplate.position(L_pos,pag2,len(L_pos),select_filt)
               await message.edit_text(text, reply_markup=reply_markup)
        elif(select_filt==1):
         if(pag2<len(L_league)):
               pag2+=5
               text, reply_markup=MenuTemplate.position(L_league,pag2,len(L_league),select_filt)
               await message.edit_text(text, reply_markup=reply_markup)    
        else:
         if(pag2<len(L_value)):
               pag2+=5
               text, reply_markup=MenuTemplate.position(L_value,pag2,len(L_value),select_filt)
               await message.edit_text(text, reply_markup=reply_markup)            
      else:
       pag+=5
       if(band_F):
          text, reply_markup=MenuTemplate.get_players_view_from_table_values(df_filt, pag, len(df_filt))
       else:
          text, reply_markup=MenuTemplate.get_players_view_from_table_values(df, pag, len(df))
       await message.edit_text(text, reply_markup=reply_markup)

async def select_one(update:Update, context:CallbackContext):
  global band_F,pag, reg

  message=update.callback_query.message
  await update.callback_query.answer()
  
  
  aux_pl=pag-5
  reg=aux_pl
  if(band_F):
     player_text,reply_markup=MenuTemplate.player_info(df_filt,aux_pl,len(df_filt),1)
  else:
     player_text,reply_markup=MenuTemplate.player_info(df,aux_pl,len(df),0)

  await message.reply_text(player_text, reply_markup=reply_markup)

async def select_two(update:Update, context:CallbackContext):
  global band_F,pag, reg

  message=update.callback_query.message
  await update.callback_query.answer()
  
  
  aux_pl=pag-4
  reg=aux_pl
  if(band_F):
     player_text,reply_markup=MenuTemplate.player_info(df_filt,aux_pl,len(df_filt),1)
  else:
     player_text,reply_markup=MenuTemplate.player_info(df,aux_pl,len(df),0)

  await message.reply_text(player_text, reply_markup=reply_markup)

async def select_tre(update:Update, context:CallbackContext):
  global band_F,pag, reg

  message=update.callback_query.message
  await update.callback_query.answer()
  
  
  aux_pl=pag-3
  reg=aux_pl
  if(band_F):
     player_text,reply_markup=MenuTemplate.player_info(df_filt,aux_pl,len(df_filt),1)
  else:
     player_text,reply_markup=MenuTemplate.player_info(df,aux_pl,len(df),0)

  await message.reply_text(player_text, reply_markup=reply_markup)

async def select_jhinn(update:Update, context:CallbackContext):
  global band_F,pag

  message=update.callback_query.message
  await update.callback_query.answer()
  
  
  aux_pl=pag-2
  reg=aux_pl
  if(band_F):
     player_text,reply_markup=MenuTemplate.player_info(df_filt,aux_pl,len(df_filt),1)
  else:
     player_text,reply_markup=MenuTemplate.player_info(df,aux_pl,len(df),0)

  await message.reply_text(player_text, reply_markup=reply_markup)    

async def select_cinco(update:Update, context:CallbackContext):
  global band_F,pag,reg

  message=update.callback_query.message
  await update.callback_query.answer()
  
  
  aux_pl=pag-1
  reg=aux_pl

  if(band_F):
     player_text,reply_markup=MenuTemplate.player_info(df_filt,aux_pl,len(df_filt),1)
  else:
     player_text,reply_markup=MenuTemplate.player_info(df,aux_pl,len(df),0)

  await message.reply_text(player_text, reply_markup=reply_markup)

async def back_catalog(update: Update, context: CallbackContext):

   global pag,pag2, band2, L_pos, L_league, L_value, select_filt

   await update.callback_query.answer()
 
   message=update.callback_query.message

   if(band2):
      if(select_filt==0):  
        if(pag2!=5):
            pag2-=5
            text, reply_markup=MenuTemplate.position(L_pos,pag2,len(L_pos),select_filt)
            await message.edit_text(text, reply_markup=reply_markup)
      elif(select_filt==1):
         if(pag2!=5):
            pag2-=5
            text, reply_markup=MenuTemplate.position(L_league,pag2,len(L_league),select_filt)
            await message.edit_text(text, reply_markup=reply_markup)
      else:
         if(pag2!=5):
            pag2-=5
            text, reply_markup=MenuTemplate.position(L_value,pag2,len(L_value),select_filt)
            await message.edit_text(text, reply_markup=reply_markup)    
   else:
    if(band_F):
      if(pag!=5):
         pag-=5
         text, reply_markup=MenuTemplate.get_players_view_from_table_values(df_filt, pag, len(df_filt))
         await message.edit_text(text, reply_markup=reply_markup)
    else:  
      if(pag!=5):
         pag-=5
         text, reply_markup=MenuTemplate.get_players_view_from_table_values(df, pag, len(df))
         await message.edit_text(text, reply_markup=reply_markup)

async def delete(update: Update, context: CallbackContext):
 
  await update.callback_query.delete_message()

async def add_fav(update: Update, context: CallbackContext):
    global band_F

    await update.callback_query.answer()
    username = update.effective_user.username
    fullname=update.effective_user.full_name
    position = update.callback_query.data.split(":")[1]
    
    player = df_filt.iloc[int(position), 1] if band_F else df.iloc[int(position), 1]
    nation = df_filt.iloc[int(position), 2] if band_F else df.iloc[int(position), 2]

    worksheet=sheet.get_worksheet(1)
    worksheet.append_row([username, fullname ,player, nation])
    

  

async def menu_filtro(update: Update, context: CallbackContext):
    global pag, band,band2, pag2,band_F
    band_F=True
    if(band2):
      pag2=0
      band=False
      Filt=[" ", " ", " "]

    message=update.callback_query.message

    (menu_text,reply_markup)=MenuTemplate.filtre_menu()
   
    await update.callback_query.answer()
    await message.edit_text(menu_text,reply_markup=reply_markup)
 
async def filtros(update: Update, context: CallbackContext):
   global Filt, band2,pag2, pag, select_filt
  
   if(band2):
      pag2=0
      select_filt=-1

   message= update.callback_query.message
   menu_text,reply_markup=MenuTemplate.filtre_tag(Filt, band)

   await update.callback_query.answer()
   await message.edit_text(menu_text, reply_markup=reply_markup)

async def position(update:Update, context: CallbackContext):
   global pag2, band2, select_filt, L_pos
   select_filt=0
   band2=True
   pag2+=5
   
   
   message=update.callback_query.message
   posit_text, reply_markup=MenuTemplate.position(L_pos,pag2,len(L_pos),select_filt)
   await update.callback_query.answer()
   await message.edit_text(posit_text,reply_markup=reply_markup)

async def leagues(update: Update, context:CallbackContext):
   global pag2, band2, select_filt, L_league
   select_filt=1
   band2=True
   pag2+=5
   
   
   message=update.callback_query.message
   posit_text, reply_markup=MenuTemplate.position(L_league,pag2,len(L_pos),select_filt)
   await update.callback_query.answer()
   await message.edit_text(posit_text,reply_markup=reply_markup)

async def values(update:Update, context: CallbackContext):
   global pag2, band2, select_filt, L_pos
   select_filt=2
   band2=True
   pag2+=5
   
   
   message=update.callback_query.message
   posit_text, reply_markup=MenuTemplate.position(L_value,pag2,len(L_pos),select_filt)
   await update.callback_query.answer()
   await message.edit_text(posit_text,reply_markup=reply_markup)



async def select_one_filt(update: Update, context: CallbackContext):
 global band2, pag2, Filt, band, select_filt, L_pos, L_league, L_value

 band=True
 aux=(pag2-5)
 pag2=0
 if(select_filt==0):
   
   filt_text="📍 Posicion: "
   filt_text+=L_pos[aux]

 elif(select_filt==1):
  
  filt_text="🛡 Liga: "
  filt_text+=L_league[aux]
 elif(select_filt==2):
  
  filt_text="💸 Precio: "
  filt_text+=L_value[aux]

 Filt[select_filt]=filt_text
 
 message= update.callback_query.message
 menu_text,reply_markup=MenuTemplate.filtre_tag(Filt, band)

 await update.callback_query.answer()
 await message.edit_text(menu_text, reply_markup=reply_markup)


async def select_two_filt(update: Update, context: CallbackContext):
 
 global band2, pag2, Filt, band, select_filt, L_pos, L_league, L_value

 band=True
 aux=(pag2-4)
 pag2=0
 if(select_filt==0):
   
   filt_text="📍 Posicion: "
   filt_text+=L_pos[aux]

 elif(select_filt==1):
  
  filt_text="🛡 Liga: "
  filt_text+=L_league[aux]
 elif(select_filt==2):
  
  filt_text="💸 Precio: "
  filt_text+=L_value[aux]

 Filt[select_filt]=filt_text
 
 message= update.callback_query.message
 menu_text,reply_markup=MenuTemplate.filtre_tag(Filt, band)

 await update.callback_query.answer()
 await message.edit_text(menu_text, reply_markup=reply_markup)

async def select_tre_filt(update: Update, context: CallbackContext):
 global band2, pag2, Filt, band, select_filt, L_pos, L_league, L_value

 band=True
 aux=(pag2-3)
 pag2=0
 if(select_filt==0):
   
   filt_text="📍 Posicion: "
   filt_text+=L_pos[aux]

 elif(select_filt==1):
  
  filt_text="🛡 Liga: "
  filt_text+=L_league[aux]
 elif(select_filt==2):
  
  filt_text="💸 Precio: "
  filt_text+=L_value[aux]

 Filt[select_filt]=filt_text
 
 message= update.callback_query.message
 menu_text,reply_markup=MenuTemplate.filtre_tag(Filt, band)

 await update.callback_query.answer()
 await message.edit_text(menu_text, reply_markup=reply_markup)

async def select_Jhinn_filt(update: Update, context: CallbackContext):
 global band2, pag2, Filt, band, select_filt, L_pos, L_league, L_value

 band=True
 aux=(pag2-2)
 pag2=0
 if(select_filt==0):
   
   filt_text="📍 Posicion: "
   filt_text+=L_pos[aux]

 elif(select_filt==1):
  
  filt_text="🛡 Liga: "
  filt_text+=L_league[aux]
 elif(select_filt==2):
  
  filt_text="💸 Precio: "
  filt_text+=L_value[aux]

 Filt[select_filt]=filt_text
 
 message= update.callback_query.message
 menu_text,reply_markup=MenuTemplate.filtre_tag(Filt, band)

 await update.callback_query.answer()
 await message.edit_text(menu_text, reply_markup=reply_markup)

async def select_Cinco_filt(update: Update, context: CallbackContext):
 global band2, pag2, Filt, band, select_filt, L_pos, L_league, L_value

 band=True
 aux=(pag2-1)
 pag2=0
 if(select_filt==0):
   
   filt_text="📍 Posicion: "
   filt_text+=L_pos[aux]

 elif(select_filt==1):
  
  filt_text="🛡 Liga: "
  filt_text+=L_league[aux]
 elif(select_filt==2):
  
  filt_text="💸 Precio: "
  filt_text+=L_value[aux]

 Filt[select_filt]=filt_text
 
 message= update.callback_query.message
 menu_text,reply_markup=MenuTemplate.filtre_tag(Filt, band)

 await update.callback_query.answer()
 await message.edit_text(menu_text, reply_markup=reply_markup)

async def limpar_F(update: Update, context:CallbackContext):
   global band,band2,pag2, Filt

   band=False
   Filt=[" ", " ", " "]
   pag2=0


   message=update.callback_query.message
   menu_text,reply_markup=MenuTemplate.filtre_tag(Filt,band)

   await update.callback_query.answer()
   await message.edit_text(menu_text,reply_markup=reply_markup)

async def buscar(update: Update, context:CallbackContext):
  global Filt, df_filt, band2, pag2, pag, band_F
  df_filt=df
  message=update.callback_query.message
  

  band2=False
  pag2=0
  pag=5

  for i in Filt:
    if(i!=" "):
     aux=i.split()

     if(aux[1]=="Posicion:"):
       mask=df_filt["position"]==aux[2]
       df_filt=df_filt[mask]
       
     elif(aux[1]=="Liga:"):  
       mask=df_filt["league"]==aux[2]
       df_filt=df_filt[mask]

     else:
       mask=df_filt["value"]<=aux[2]
       df_filt=df_filt[mask]

  text, reply_markup=MenuTemplate.get_players_view_from_table_values(df_filt, pag, len(df_filt))

  await message.edit_text(text, reply_markup=reply_markup)

async def filtrar_nombre(update:Update, context: ContextTypes):
  message=update.callback_query.message
  update.callback_query.answer()
  text, reply_markup=MenuTemplate.buscar_nombre()
  
  await message.edit_text(text, reply_markup=reply_markup)

async def buscar_nombre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Asegúrate de que se haya pasado un argumento
    if not context.args:
        await update.message.reply_text("Por favor, proporciona un nombre de jugador.")
        return

    # Obtener el nombre del primer argumento
    name = context.args[0]+" "+context.args[1]
    

    # Filtrar el DataFrame para encontrar jugadores que coincidan con el nombre
    mask = df["player"].str.lower() == name.lower()  # Comparar sin distinción entre mayúsculas y minúsculas
    player = df[mask]

    # Verificar cuántos jugadores se encontraron
    if len(player) == 1:
        player_info, reply_markup = MenuTemplate.player_info(player, 0, len(player), 1)
        await update.message.reply_text(player_info, reply_markup=reply_markup)
    elif len(player) > 1:
        player_info = "Se encontraron múltiples jugadores con ese nombre. Por favor, sé más específico."
        await update.message.reply_text(player_info)
    else:
        player_info = "Nombre inválido. No se encontró ningún jugador con ese nombre."
        await update.message.reply_text(player_info)

# Iniciar el bot
application = ApplicationBuilder().token(BOT_TOKEN).build()

#handlers
application.add_handler(CommandHandler("start",start))

application.add_handler(CallbackQueryHandler(show_catalog, pattern=Routes.Catalog))

application.add_handler(CallbackQueryHandler(show_menu,Routes.Menu))

application.add_handler(CallbackQueryHandler(next_catalog,Routes.Forward))

application.add_handler(CallbackQueryHandler(select_one,Routes.Uno))

application.add_handler(CallbackQueryHandler(select_two,Routes.Dos))

application.add_handler(CallbackQueryHandler(select_tre,Routes.Three))

application.add_handler(CallbackQueryHandler(select_jhinn,Routes.Sublime))

application.add_handler(CallbackQueryHandler(select_cinco,Routes.Five))

application.add_handler(CallbackQueryHandler(back_catalog,Routes.Back))

application.add_handler(CallbackQueryHandler(delete,Routes.Delete))

application.add_handler(CallbackQueryHandler(add_fav,Routes.Add_fav))

application.add_handler(CallbackQueryHandler(menu_filtro,Routes.Buscar))

application.add_handler(CallbackQueryHandler(filtros,Routes.Filtro))

application.add_handler(CallbackQueryHandler(position,Routes.Pos))

application.add_handler(CallbackQueryHandler(leagues,Routes.League))

application.add_handler(CallbackQueryHandler(values,Routes.value))

application.add_handler(CallbackQueryHandler(select_one_filt,Routes.One_F))

application.add_handler(CallbackQueryHandler(select_two_filt,Routes.Two_F))

application.add_handler(CallbackQueryHandler(select_tre_filt,Routes.Tre_F))

application.add_handler(CallbackQueryHandler(select_Jhinn_filt,Routes.Jhinn_F))

application.add_handler(CallbackQueryHandler(select_Cinco_filt,Routes.Cinco_F))

application.add_handler(CallbackQueryHandler(limpar_F,Routes.borrar))

application.add_handler(CallbackQueryHandler(buscar,Routes.Filtrar))

application.add_handler(CallbackQueryHandler(filtrar_nombre, Routes.Name))

application.add_handler(CommandHandler("buscar", buscar_nombre))
#run
application.run_polling(allowed_updates=Update.ALL_TYPES)


