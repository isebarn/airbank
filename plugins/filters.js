import Vue from 'vue'
import moment from 'moment'

function time (date) {
  return date !== '' ? moment(date).format('LLL') : ''
}

Vue.filter('time', time)
