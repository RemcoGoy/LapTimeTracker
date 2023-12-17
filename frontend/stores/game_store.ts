import { defineStore } from 'pinia';
import { mande } from 'mande'

// const api = mande(`${process.env.BACKEND_URL}/games`);

export const useGamesStore = defineStore('games', {
  state: () => ({ games: [{}], current_game: null }),
  getters: {
    currentGame: (state) => state.current_game
  },
  actions: {
    fetchGames() {
      this.games = [{}];
    }
  }
})