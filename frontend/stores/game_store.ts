import { defineStore } from 'pinia';

export const useGamesStore = defineStore('games', {
  state: () => ({ games: [{}], current_game: null }),
  getters: {
    currentGame: (state) => state.current_game
  },
  actions: {
    fetchGames() {
      this.games = [{
        'name': "TestGame"
      }]
    }
  }
})