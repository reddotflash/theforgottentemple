from flask import Flask render_template, request, url_for
import random
import json

app = Flask (__name__)

player_stats= {
    "health": 100
    "max_health": 100
    "inventory": []
    "level": 1
    "xp": 0
    "gold": 250
    "current_enemy": None
}

def spawn_enemy(enemy_name, hp, attack_power):
    player_stats["current_enemy"] = {
        "name": enemy_name,
        "hp": hp,
        "max_hp": hp,
        "attack": attack_power
    }

    @app.route("/attack")
    def attack():
        enemy = player_stats["current_enemy"]
        if not enemy or enemy["hp"] <= 0:
            return redirect(url_for("scene", scene_id="you win"))

        # player doing dmg
        player_damage = random.randint(5, 15) + (player_stats["level"] * 2)
        enemy["hp"] -= player_damage

        # enemy ded?

        if enemy hp <= 0:
            player_stats["xp"] += random.randint(15, 30)
            player_stats["gold"] += random.randint(10, 30)
            player_stats["current_enemy"] = none

        # mabye level up xd

        if player_stats["xp"] >= player_stats["level"] * 100:
            player_stats["level"] += 1
            player_stats["max_health"] += random.randint(5, 20)
            player_stats["health"] = player_stats["max_health"]
        return redirect(url_for("scene", scene_id="combat_win"))


    # enemy dmg back
    enemy_damage = random.randint(2, enemy["attack"])
    player_stats["health"] -= enemy_damage

    if player_stats["health"] <= 0:
        return redirect(url_for("scene", scene_id="game_over"))

    
    return redirect(url_for("scene", scene_id="combat_loop"))


    @app.route("/use_item/<item_name>")
    def use_item(item_name):
        if item_name in player_stats["inventory"]:
            if item_name == "Healing Potion":
                player_stats["health"] = min(player_stats["max_health"], player_stats["health"] + random.randint(15, 30)) 
                player_stats["inventory"].remove(item_name)
            elif item_name == "Iron_Key":

                pass


        return redirect(request.referrer or url_for("index"))


    @app.route("/save")
    def save_game():
        with open ("savefile.json", "w") as file:
            json.dump(player_stats, f)
        return redirect(request.referrer or url_for("index"))
        
    @app.route("/load")
    def load_game():
        try:
            with open("savefile.json", "r") as file:
                player_stats = json.load(f)
        except: FileNotFoundError:

            pass
        return redirect(url_for("scene", scene_id="start"))


    return render_template(
        "the-forgotten-temple.html",
        story_text=current_scene["text"],
        choices=current_scene["choices"]
        stats=player_stats,
        enemy=player_stats["current_enemy"]
    )


if __name__ == "__main__":
    app.run(debug=True)
