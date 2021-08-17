<template>
  <v-container v-if="month">
    <v-layout>
      <v-card>
        <v-row dense>
          <v-col cols="8" offset="2">
            <v-date-picker
              v-model="month"
              full-width
              no-title
              type="month"
              @change="fetchTransactions()"
            />
          </v-col>
        </v-row>
      </v-card>
    </v-layout>
    <v-data-table
      :items="transactions"
      :headers="headers"
      @click:row="viewDetail"
    >
      <template #[`item.transactionDate`]="{item}">
        <span>{{ item.transactionDate | time }}</span>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { mapFields } from 'vuex-map-fields'
export default {

  data () {
    return {
      headers: [

        {
          text: 'account',
          align: 'start',
          value: 'account'
        },
        {
          text: 'amount',
          align: 'start',
          value: 'amount'
        },
        {
          text: 'currency',
          align: 'start',
          value: 'currency'
        },
        {
          text: 'category',
          align: 'start',
          value: 'category'
        },
        {
          text: 'date',
          align: 'start',
          value: 'transactionDate'
        }
      ]
    }
  },

  created () {
    if (!this.month) {
      this.setMonth(this.$moment().startOf('month').format('YYYY-MM-DD'))
      this.fetchTransactions()
    }
  },

  computed: {
    ...mapGetters(['transactions']),
    ...mapFields(['month'])
  },

  methods: {
    ...mapActions(['fetchTransactions', 'setMonth']),

    pickTime (item) {
      this.setMonth(item)
      this.fetchTransactions()
    },

    viewDetail (item) {
      this.$router.push({ name: 'detail', params: { transaction: item.transaction } })
    }
  }
}
</script>
