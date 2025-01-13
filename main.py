from howlongtobeatpy import HowLongToBeat
import json
import re
import traceback
import pandas as pd
import variables

def main(path):
    try:
         # Создаем пустой список для хранения данных о играх
        games_data = []

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('- '):
                    game = line[2:].strip()
                    if game == "":
                        continue

                    results = HowLongToBeat().search(game)
                    if results == []:
                        game_vars = {"game_name": game}
                        games_data.append(game_vars)
                        continue

                    game = results[0]
                    game_vars = vars(game)

                    keys_to_keep = ["game_name", "game_image_url", "release_world", "main_story", "main_extra", "completionist"]
                    game_vars = {k: v for k, v in game_vars.items() if k in keys_to_keep}
                    game_vars['game_image_url'] = f'<img src={game_vars["game_image_url"]} alt="img" width="100" />'

                    games_data.append(game_vars)

        # Преобразуем список словарей в DataFrame
        games_data = pd.DataFrame(games_data)
        markdown_table = games_data.to_markdown(index=False)
        # with open('output.md', 'w') as f:
        with open(r'D:\Obsidian_vault\Vault\Игры, Фильмы, Сериалы\Games_table.md', 'w', encoding='utf-8') as file:
            file.write(markdown_table)
            file.close
    except Exception as e:
        print(f"Ошибка: {e}")
        traceback.print_exc()


if __name__ == '__main__':
    path = variables.path
    main(path = path)