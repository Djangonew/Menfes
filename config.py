import os

api_id = int(os.environ.get("API_ID", "20247370"))
api_hash = os.environ.get("API_HASH", "813309fab8cd9fce260ce7269e543bdb")
bot_token = os.environ.get("BOT_TOKEN", "6427697471:AAE61o_mvEw8z-DPi3X8X3iT3Dizg7KjWyc")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001993237586"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002030295294"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1001993237586"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001710755987"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1748872441"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))

# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))

-pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/71bfda32ec9ff478aa314.jpg")
-pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/c0f732bfb29a7a2be3aa5.jpg")

# =========================================================== #

hastag = os.environ.get("HASTAG", "#LpmGirl #LpmBoy #LpmAsk #LpmFind #LpmSpill #LpmStory").replace(" ", "|").lower()

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#LpmBoy / #LpmGirl untuk Mencari Pasangan,Teman , Partner dll
#LpmAsk untuk Bertanya
#LpmStory untuk Berbagi Cerita
#LpmSpill untuk Spill Masalah
#LpmFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#LpmBoy / #LpmGirl untuk Mencari Pasangan,Teman , Partner dll
#LpmAsk untuk Bertanya
#LpmStory untuk Berbagi Cerita
#LpmSpill untuk Spill Masalah
#LpmFind untuk Mencari Pasangan, Teman, Partner dll
""")