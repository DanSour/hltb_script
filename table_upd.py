import pandas as pd 
from variables import games_table
from howlongtobeatpy import HowLongToBeat
import sys


def main():
    try:
        while True:
            games_data = []
            game = input('Game name: ').lower()
            if game == '/q' or game == '/Q':
                break

            results = HowLongToBeat().search(game)
            if results == []:
                print('Game not found')
                
            else:
                game = results[0]
                game_vars = vars(game)

                keys_to_keep = ["game_name", "game_image_url", "release_world", "main_story", "main_extra", "completionist"]
                game_vars = {k: v for k, v in game_vars.items() if k in keys_to_keep}
                game_vars['game_image_url'] = f'<img src={game_vars["game_image_url"]} alt="img" width="100" />'
                # games_data.append()
                games_data = pd.DataFrame([game_vars])

                games_data = games_data.to_markdown(index=False)
                games_data = games_data.split('\n')[2:]
                games_data = games_data[0]

                with open(games_table, 'a', encoding='utf-8') as file:
                    file.write(games_data + '\n')
                    file.close


    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()