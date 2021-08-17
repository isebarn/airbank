<template>
  <v-container v-if="details">
    <v-layout>
      <v-row>
        <v-col offset="3" cols="6">
          <v-card>
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title class="text-h5">
                  {{ details.account }}
                </v-list-item-title>
                <v-list-item-subtitle>{{ details.transactionDate | time }}</v-list-item-subtitle>
                <v-list-item-subtitle>{{ details.category }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-card-text>
              <v-row align="center">
                <v-col
                  class="text-h3"
                  cols="6"
                >
                  {{ details.amount }} {{ details.currency }}
                </v-col>
              </v-row>
            </v-card-text>

            <v-list class="transparent">
              <v-list-item>
                <v-list-item-title>Description</v-list-item-title>
                <v-list-item-subtitle class="text-right">
                  {{ details.description }}
                </v-list-item-subtitle>
              </v-list-item>
              <v-list-item v-if="details.reference">
                <v-list-item-title>
                  Reference
                </v-list-item-title>
                <v-list-item-subtitle class="text-right">
                  {{ details.reference }}
                </v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Status</v-list-item-title>
                <v-list-item-subtitle class="text-right">
                  {{ details.status }}
                </v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Transaction Id</v-list-item-title>
                <v-list-item-subtitle class="text-right">
                  {{ details.transaction }}
                </v-list-item-subtitle>
              </v-list-item>
              </v-list-item>
            </v-list>

            <v-divider />

            <v-card-actions>
              <v-btn text>
                <NuxtLink to="/">
                  Back
                </NuxtLink>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
  </v-container>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  props: {
    transaction: {
      type: String,
      default: ''
    }
  },

  computed: {
    ...mapGetters(['transactions']),

    details () {
      return this.transactions.find(x => x.transaction === this.$route.params.transaction)
    }
  }
}
</script>
