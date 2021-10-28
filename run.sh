# python3 main.py --n_images=250 \
#                 --n_lines=1 \
#                 --textdir="./name.txt" \
#                 --outdir="./ho_ten" \
#                 --name_font_size 40 \
#                 --name_fontdir="./font" \
#                 --text_color="#ff0000" \
#                 --transparent_bg \
#                 --name_uppercase_prob=0.0

# python3 main.py --n_images=50 \
#                 --n_lines=1 \
#                 --textdir="./name.txt" \
#                 --outdir="./ho_ten" \
#                 --name_font_size 40 \
#                 --name_fontdir="./font/VTIMESN.TTF" \
#                 --text_color="#ff0000" \
#                 --transparent_bg \
#                 --name_uppercase_prob=1.0

# python3 concat_title_name.py --namedir="name.txt" \
#                              --titledir="title.txt" \
#                              --outdir="title_name.txt" \
#                              --max_length_ratio=3.0

# python3 main.py --n_images=300 \
#                 --n_lines=2 \
#                 --textdir="./title_name.txt" \
#                 --outdir="./ho_ten_chuc_danh" \
#                 --name_font_size 40 \
#                 --title_font_size 20 50 \
#                 --name_fontdir="./font" \
#                 --title_fontdir="./title_font" \
#                 --text_color="#ff0000" \
#                 --transparent_bg \
#                 --line_spacing 10 25 \
#                 --title_first_prob=0.8 \
#                 --name_uppercase_prob=0.0 \
#                 --title_uppercase_prob=0.9 \
#                 --title_name_max_width_ratio 1.5 \
#                 --title_name_max_height_ratio 2.0