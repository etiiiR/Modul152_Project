/* global localStorage */

import axios from 'axios'

const API_URL = process.env.API_URL || 'http://localhost:8001/'

export default axios.create({
  baseURL: API_URL,
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + localStorage.token
  }
})
