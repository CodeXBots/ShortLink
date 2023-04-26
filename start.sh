echo "Cloning Repo...."
git clone https://github.com/learnandearnwithkarthik/Shortner-Converter-Bot.git /Shortner-Converter-Bot
cd /Shortner-Converter-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
