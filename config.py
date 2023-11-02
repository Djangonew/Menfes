import os

api_id = int(os.environ.get("API_ID", "29479908"))
api_hash = os.environ.get("API_HASH", "56cc54bcc8284ccba5e8f4358e5bd29d")
bot_token = os.environ.get("BOT_TOKEN", "6801456940:AAGPL8PMlLxCLbem-i21aGb2Pfu_05KtfoA")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001998341695"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002066923405"))
channel_3 = int(os.environ.get("CHANNEL_3", -1002132366739"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001997868124"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6661774028"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))

# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))

# =========================================================== #

hastag = os.environ.get("HASTAG", "#mas #mba #pap #tanya #quote #curhat").replace(" ", "|").lower()

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
Hai {mention} 👋🏻

𝗚𝗝𝗡 𝗔𝘂𝘁𝗼 𝗣𝗼𝘀𝘁 adalah bot auto post pesan yang anda kirim akan masuk ke channel @MENFESS_JAWA

silahkan baca help dan rules terlebih dahulu.)

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim. <b>silahkan klik button</b> help bila butuh bantuan.)
