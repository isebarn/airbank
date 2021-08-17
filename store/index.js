import { getField, updateField } from 'vuex-map-fields'

export const state = () => ({
  transactions: [],
  month: null
})

export const mutations = {
  updateField,

  transactions: (state, payload) => {
    state.transactions = payload
  },

  month: (state, payload) => {
    state.month = payload
  }

}

export const getters = {
  getField,

  transactions: (state) => { return state.transactions },
  month: (state) => { return state.month }
}

export const actions = {
  fetchTransactions ({ commit, state }) {
    this.$axios.post('api/data', [state.month, this.$moment(new Date(state.month)).add(1, 'month').format('YYYY-MM-DD')]).then((response) => {
      commit('transactions', response.data)
    })
  },

  setMonth ({ commit }, month) {
    commit('month', month)
  }
}
